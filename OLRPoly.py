#Tables and functions for doing polynomial fit to OLR(CO2,T)
#Modified for Neoproterozoic review paper calculations.
#Includes effect of pressure broadening, and keeping mass of N2/O2 air
#fixed at 1 bar.

#Note that the argument is not pCO2, but a measure of the
#mass of CO2 in the atmosphere -- the pressure the CO2 would
#have in isolation. Thus, pCO2bar/g is the mass added, and 12/44 of
#this is the mass of carbon added per square meter of surface.

from ClimateUtilities import * # needed for polint and interpolation object
import math

#%-------------Table:Cubic fit to (T-275)----------------------------------------------------
#%**Layout: Make sure this table comes after the corresponding figure
#%Y = M0 + M1*x + ... M8*x\u8\n + M9*x\u9
#\begin{table}
#\begin{tabular}{lcccc}
#$CO_2$ , $a_o$   , $a_1$  , $a_2$      ,  $a_3$     \\
CO2Vals = [1,10.,100.,1000.,10000.,100000.,200000.]
logCO2Vals = [math.log(co2) for co2 in CO2Vals]
fitTcoeffs = []
#1 Pa
fitTcoeffs.append([	273.64, 129.45, -23.005, -24.558])
#Pa 
fitTcoeffs.append([	261.53, 126.63, -15.683, -20.914])
#100 Pa
fitTcoeffs.append([	247.92, 120.72, -9.6234, -16.334])
#1000 Pa
fitTcoeffs.append([	231.35, 111.94, -3.4677, -11.163])
#10000 Pa
fitTcoeffs.append([	205.21, 97.516, 7.7354, -1.9642])
#100000 Pa
fitTcoeffs.append([	150.83, 61.94, 21.96, 13.443])
#200000 Pa
fitTcoeffs.append([	125.16, 44.672, 23.01, 15.982])

#\end{tabular}
#\caption{Coefficients for polynomial fit $OLR = a_o + a_1 x + a_2 x^2 + a_3 x^3$,
#where $x = T_g - 275$. Calculation carried out with $rh = .5$.}
#\label{table:OLRvsTfit}
#\end{table}
#%---------------------------------------------------------------------------------------------


#Utility to evaluate polynomial
def evalPoly(coeffs,x):
    sum = coeffs[-1]
    for i in range(2,len(coeffs)+1):
        sum = x*sum + coeffs[-i]
    return sum

#CO2 stand-alone pressure in Pa
def OLRT(CO2,T):
    x = (T-280.)/(330.-280.)
    y = math.log(CO2)
    #interpolate coefficients
    coeffs = []
    for i in range(len(fitTcoeffs[0])):
        a = [fitTcoeffs[j][i] for j in range(len(logCO2Vals))]
        coeffs.append(polint(logCO2Vals,a,y))
    #Evaluate the polynomial
    return evalPoly(coeffs,x)


