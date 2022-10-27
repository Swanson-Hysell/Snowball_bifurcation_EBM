#--------------------------------------------------------------
#
# This Python script was used to do the computations that
# went into the basic ice-albedo bifurcation diagram in
# Figure 3 .
#--------------------------------------------------------------
#Note that the graph in Figure 3 has been fancied up using Adobe
#illustrator. The software below just produces the basic set of
#curves that are the basis of the graph. It does not automatically
#mark the unstable branch with dashed lines, as has been done
#in Figure 3. This code could be easily modified to do that, but
#that feature has been left out in order to keep the code simpler
#and easier to understand. 

#-----Import needed libararies---
#The following two libraries are distributed free as
#part of the courseware supplement for Principles of Planetary Climate.
#They can be downloaded from
#   http://geosci.uchicago.edu/~rtp1/PrinciplesPlanetaryClimate/Courseware/coursewarePortal.html
#The module ClimateUtilities needs the module ClimateGraphics.py, if you
#intend to install Ngl graphics and do your graphics within Python, or
#DummyGraphics.py if you plan to dump the results to a text file and
#plot it using some other graphics package.
#
from ClimateUtilities import *
import phys

#The following is a specialized form of the polynomial fit
#to OLR vs surface temperature and CO2, including the effects
#of pressure broadening.  It is distributed as part of the
#supplementary material on the AREPS site
import OLRPoly

#Define albedo and OLR functions here
#Radiating pressure pRad, in mb, is a global
#Note that the CO2 inventory is not the conventional
#CO2 concentration, but instead the CO2 inventory (in Pa)
#defined in the article.  The pressure broadening is
#computed on the basis of 1 bar (1.e5 Pa) of non-CO2 dry
#air. The effect of water vapor with 50% relative humidity
#is included.
def OLR(T,CO2):
    return OLRPoly.OLRT(CO2,T)

#Write Newton solver to get T(CO2)
def fOLR(CO2,params):
    return OLRPoly.OLRT(CO2,params.T) - params.flux
m = newtSolve(fOLR)
params = Dummy()
m.setParams(params)

#Parameters of albedo function are globals
def albedo(T):
    if T < T1:
        return alpha_ice
    elif (T >= T1)&(T<=T2):
        r = (T-T2)**2/(T2-T1)**2
        return alpha_0 + (alpha_ice - alpha_0)*r
    else:
        return alpha_0

def BifurcCO2(Tlist,L,cloud=0.):
    CO2L = 100.
    SabsList = []
    CO2List = []
    OLRlist = []
    NetFluxlist = []
    Glist = []

    for T in Tlist:
        params.flux = (1.-albedo(T))*L/4. + cloud
        params.T = T
        try:
            CO2L = m(CO2L)
            slask = 1.*CO2L
            CO2List.append(CO2L)
        except:
            CO2List.append(1.e-5)
            CO2L = 1000.
    return CO2List

#Utilitity for finding left and right limits of
#hysteresis loop. V is the  list of values of the
#control parameter corresoponding to the list of
#temperatures in ascending order. Typically V
#would contain CO2 concentrations or inventories
def TurningPoints(V):
    results = []
    for i in range(3,len(V)-3):
        if (V[i-3]-V[i])*(V[i]-V[i+3]) < 0.:
            results.append(V[i])
    return results

#=========Function Definitions Done============================
#              Main body of script starts here
#==============================================================

#Set up a list of temperature values for the bifurcation plot
Tlist = [340.-i  for i in range(340-220)]

#Set up a Curve() object to contain the results. The
#results consist of a set of columns of the CO2 values
#that correspond to each temperature, including ice-albedo
#feedback
c = Curve()
c.addCurve(Tlist,'Ts')
#Plotting options. (ignored if you aren't using
#the plot function in ClimateUtilities, and are
#instead just dumping the results to a text file)
c.switchXY = True #Switches axis so it looks like a hysteresis plot
c.PlotTitle = 'Bifurcation diagram'
c.Xlabel = 'Surface Temperature (K)'
c.Ylabel = 'CO2 (Pa)'
c.XlogAxis = True

#Now loop over the parameters you wish to vary, and
#add a curve to the bifurcation diagram for each parameter
#set. This loop is set up to vary the ice albedo, but you
#can instead loop over anything else you want to explore
for alpha_ice in [.55,.6,.65]:
    L = .94*1367. #Neoproterozoic value of solar constant
    #alpha_ice = .6 # Ice albedo.
                    #Set value here if you are looping over something else
    alpha_0 = .2 #Ocean albedo
    T1 = 260.    #Temperature at which planet is ice-covered
    T2 = 290.    #Temperature at which planet is ice-free
    cloudOffset = 20. #Cloud longwave forcing (W/m**2)
    #Now calculate the list of CO2 corresponding to the temperatures
    CO2List = BifurcCO2(Tlist,L,cloudOffset)
    #Put results in the Curve. The second argument makes a column
    #header tagged with the value of the parameter you are varying
    c.addCurve(CO2List,'CO2_%f'%alpha_ice) 

#Note that the portions of the diagram where the CO2 goes
#below 1 Pa are unphysical, since the OLR fits are not valid
#at such low values.  These were masked out in Figure 3 in
#the article
    
#Plot results, or dump to text file
#Uncomment the following two lines to plot
#the results and save the plot to postscript
#w = plot(c)
#w.save('SnowballBifurcation')
#
#Dump the results to a text file for plotting
c.dump('SnowballBifurcationData.txt')





