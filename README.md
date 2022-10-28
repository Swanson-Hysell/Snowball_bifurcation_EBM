# Snowball bifurcation energy-balance model

This repository hosts a notebook that implements the 0-D energy balance model of Pierrehumbert et al. (2011). It utilizes the Python script published by Pierrehumbert et al. (2011) which itself uses the ClimateUtilities modules. 

A run of the model with slightly modified variables is visualized in a simplified plot of just the upper and lower limb without showing the unstable branches. In addition, CO<sub>_2</sub> decrease scenarios are shown (2 CO<sub>_2</sub> halvings) starting at different initial global mean temperatures. These scenarios illustrate that the effect of a decrease in CO<sub>_2</sub> (say driven by changing paleogeographic boundary conditions) on Earth's climate state will be quite different depending on the initial starting condition.

![Figure of results from energy-balance model illustrating Snowball bifurcation](https://github.com/Swanson-Hysell/Snowball_bifurcation_EBM/blob/main/Snowball_bifurcation_figure.png)

The results shown are for calculations with a solar constant of 1,285 Wm<sup>−2</sup> (94% of present day), ice albedo of 0.7, and an adjusted outgoing longwave radiation forcing of -25 Wm<sup>−2</sup>. The colored boxes illustrate that ice-covered and ice-free temperatures using the same values assigned in Pierrehumbert et al. 2011. Note that while the x-axis is shown as a mixing ratio in parts per million by volume so that the values are more interpretable, the values are actually the CO<sub>_2</sub> inventory in Pa multiplied by 6.6. This approximation is valid up until $\sim$6,600 ppm and then is distorted. 
