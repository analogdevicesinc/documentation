Activity: Characteristics of Photovoltaic Solar Cells, For ADALM2000
====================================================================

Objective:
----------

The objective of this Lab activity is to study and measure the output voltage and current characteristics of a photovoltaic solar panel and develop an equivalent electrical model for use in computer simulation.

Background:
-----------

A solar cell is a semiconductor PN junction diode as shown in figure 1. The large surface area indicated in light blue is exposed to incident light energy. Solar cells are usually coated with anti-reflective materials so that they absorb the maximum amount of light energy. Normally no external bias is applied to the cell. When a photon of light is absorbed near the PN junction a hole / electron pair is produced. This occurs when the energy of the photon is higher than the energy band-gap of the semiconductor. The built in electric field of the junction cause the pair to separate and head toward the respective + and - terminals. The energy from the light causes a current to flow in an external load when the cell is illuminated.

.. image:: https://wiki.analog.com/_media/university/courses/eps/eps_photovoltais-f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 Structure of a basic solar cell.


A typical voltage vs. current characteristic, known as an I/V curve, of a PN diode without illumination is shown in green in figure 2. The applied voltage is in the forward bias direction. The curve shows the turn-on and the buildup of the forward bias current in the diode. Without illumination, no current flows through the diode unless there is external potential applied. With incident sunlight, the I/V curve shifts up showing that there is external current flow from the solar cell to a resistive load as shown with the red curve.

.. image:: https://wiki.analog.com/_media/university/courses/eps/eps_photovoltais-f2.png
   :align: center
   :width: 350px

.. container:: centeralign

   Figure 2 Shift of the solar cell I/V curve with increasing incident light.


Short circuit current, I\ :sub:`SC`, flows when the external resistance is zero (V = 0) and is the maximum current delivered by the solar cell at a given illumination level. The short circuit current is a function of the PN junction area collecting the light. Similarly, the open circuit voltage, V\ :sub:`OC`, is the potential that develops across the terminals of the solar cell when the external load resistance is very large, R\ :sub:`LOAD` = ∞. For silicon based cells a single PN junction produces a voltage near 0.5V. Multiple PN junctions are connected in series in a larger solar panel to produce higher voltages. Photovoltaic cells can be arranged in a series configuration to form small modules, and modules can then be connected in parallel-series configurations to form larger arrays. When connecting cells or modules in series to produce higher output voltages, they must have the same current rating ( if not the cell with the lowest current specification will limit the ultimate current of the module ), and similarly, modules must have the same voltage specification when connected in parallel to generate larger currents. The power delivered to the load is of course zero at both extremes of the I/V curve and reaches a maximum (P\ :sub:`MAX`) at a single load resistance value. In figure 3, P\ :sub:`MAX` is shown as the area of the shaded rectangle.

.. image:: https://wiki.analog.com/_media/university/courses/eps/eps_photovoltais-f3.png
   :align: center
   :width: 350px

.. container:: centeralign

   Figure 3 The maximum power delivered by a solar cell, P\ :sub:`MAX`, is the area of the largest rectangle under the I/V curve.


A commonly used parameter that characterizes a solar cell is the fill factor, FF, which is defined as the ratio of P\ :sub:`MAX` to the area of the rectangle formed by V\ :sub:`OC` and I\ :sub:`SC`.

.. image:: https://wiki.analog.com/_media/university/courses/eps/eps_photovoltais-e1.png
   :align: center
   :width: 150px

The efficiency of a solar cell is the ratio of the electrical power it delivers to the load, to the optical power incident on the cell. Maximum efficiency is when power delivered to the load is P\ :sub:`MAX`. Incident optical power is normally specified as the power from sunlight on the surface of the earth which is approximately 1mW/mm\ :sup:`2`. Spectral distribution of sunlight is close to a blackbody spectrum at 6000º C minus the atmospheric absorption spectrum. The maximum efficiency ?\ :sub:`MAX` may be written as:

.. image:: https://wiki.analog.com/_media/university/courses/eps/eps_photovoltais-e2.png
   :align: center
   :width: 250px

For a cell of a certain size, I\ :sub:`SC` is directly proportional to the incident optical power P\ :sub:`IN`. However, V\ :sub:`OC` increases logarithmically with the incident power. So, we would expect the overall efficiency of the solar cell to also increase logarithmically with incident power. However, thermal effects at high sunlight concentrations and electrical losses in the series resistance of the solar cell limit the enhancement in efficiency that can be achieved. So the efficiency of practical solar cells peaks at some finite light concentration level.

Shunt Resistance and Series Resistance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Photovoltaic cells can be modeled as a current source in parallel with a diode as depicted in figure 4. When there is no light present to generate any current, the cell behaves like a diode. As the intensity of incident light increases, current is generated by the PV cell.

In an ideal cell, where R\ :sub:`SH` is infinite and R\ :sub:`S` is zero, the load current I is equal to the current I\ :sub:`l` generated by the photoelectric effect minus the diode current I\ :sub:`D`, according to the equation:

.. image:: https://wiki.analog.com/_media/university/courses/eps/eps_photovoltais-e3.png
   :align: center
   :width: 350px

Where I\ :sub:`S` is the saturation current of the diode, q is the charge on an electron, 1.6x10\ :sup:`:math:`s`-:math:`s` 19` Coulombs, k is Boltzmann's constant, 1.38x10\ :sup:`:math:`s`-:math:`s` 23` J/K, T is the cell temperature in degrees Kelvin, and V is the measured cell voltage that is either produced (power quadrant) or applied (voltage bias). A more accurate model would include two diode terms, however, we will limit the model to a single diode for this discussion.

Expanding the equation gives the simplified circuit model shown below and the following associated equation, where n is the diode ideality factor (typically between 1 and 2), and R\ :sub:`S` and R\ :sub:`SH` represents the series and shunt resistances.

.. image:: https://wiki.analog.com/_media/university/courses/eps/eps_photovoltais-e4.png
   :align: center
   :width: 350px

.. image:: https://wiki.analog.com/_media/university/courses/eps/eps_photovoltais-f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4 Electrical model of solar cell


During operation, the efficiency of solar cells is reduced by the dissipation of power across internal resistances. These parasitic resistances can be modeled as a parallel shunt resistance (R\ :sub:`SH`) and series resistance (R\ :sub:`S`). For an ideal cell, R\ :sub:`SH` would be infinite and would not provide an alternate path for current to flow, while R\ :sub:`S` would be zero, resulting in no voltage drop and power loss before the load. Decreasing R\ :sub:`SH` and increasing R\ :sub:`s` will decrease the fill factor (FF) and P\ :sub:`MAX` as shown in figure 5. If R\ :sub:`SH` is decreased too much, V\ :sub:`OC` will drop, while increasing R\ :sub:`S` excessively can cause I\ :sub:`SC` to drop instead.

|eps_photovoltais-f5.png|\ |image1|

.. container:: centeralign

   Figure 5 - Effect of changing R\ :sub:`SH` & R\ :sub:`S` from ideality


It is possible to approximate the series and shunt resistances, R\ :sub:`S` and R\ :sub:`SH`, from the slopes of the I/V curve at V\ :sub:`OC` and I\ :sub:`SC`, respectively. The resistance at V\ :sub:`OC`, however, is at best proportional to the series resistance but it is larger than the series resistance. R\ :sub:`SH` is represented by the slope at I\ :sub:`SC`. Typically, the resistances at I\ :sub:`SC` and at V\ :sub:`OC` will be measured and noted, as shown in figure 6.

.. image:: https://wiki.analog.com/_media/university/courses/eps/eps_photovoltais-f7.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 6 - Obtaining values for R\ :sub:`S` and R\ :sub:`SH` from the I/V curve


I-V Curves for Modules
~~~~~~~~~~~~~~~~~~~~~~

For a module or array of solar cells, the shape of the I/V curve does not change. However, it is scaled based on the number of cells connected in series and in parallel. If n is the number of cells connected in series and m is the number of cells connected in parallel and I\ :sub:`SC` and V\ :sub:`OC` are values for individual cells, then the short circuit current for the array is nI\ :sub:`SC` and the open circuit voltage is mV\ :sub:`OC`. An example I/V curve is shown in figure 8 with an overall I\ :sub:`SC` of about 80mA and a V\ :sub:`OC` of about 4.2V and P\ :sub:`MAX` is slightly higher than 160mW.

.. image:: https://wiki.analog.com/_media/university/courses/eps/eps_photovoltais-f8.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 8, example solar panel I/V and power curves


Materials:
----------

| ADALM2000 Lab hardware
| Solder-less breadboard, and jumper wire kit
| 1 or more Solar Panels (see appendix for suggested types)
| Light source, preferably full sunlight
| 1 10 Ω resistor (R\ :sub:`1`)
| 1 470 Ω resistor (R\ :sub:`2`)
| 1 IRF510 NMOS power transistor (M\ :sub:`1`)
| 2 1.5 V AA or AAA batteries with a battery holder

Directions:
-----------

The +/- 5 volt User power supplies and waveform generators in the ALM2000 hardware can source / sink up to only 50 mA and all but the smallest solar panels can supply much more current than that. In order to measure these larger currents we must use power transistors as current amplifiers and provide external voltage sources such as batteries that can support the higher current.

On your solder-less breadboard construct the circuit shown in figure 9. This measurement setup will work for solar panels with open circuit voltages less than 5 volts. Power NMOS transistor M\ :sub:`1` along with resistor R\ :sub:`2` acts as a source follower. It will force a variable voltage, provided by waveform generator W1, across the solar panel. The 10 Ω resistor R\ :sub:`1` is used to measure the current flowing in the solar panel. The solar panel current flows from the + terminal through the two batteries, B\ :sub:`1,2`, M\ :sub:`1` and R\ :sub:`1` back to the negative terminal thus not needing to flow in any of the Discovery supplies.

.. image:: https://wiki.analog.com/_media/university/courses/eps/eps_photovoltais-f9.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9, solar panel measurement circuit


Scope channel 1 measures the solar panel voltage with input 1+ connected to the + terminal of the panel and input 1- connected to the - terminal of the panel. Scope channel 2 measures the current by measuring the voltage across 10 Ω resistor R\ :sub:`1` with input 2+ connected to the source terminal of M\ :sub:`1` and input 2- connected to the - terminal of the panel.

The configuration shown in figure 9 can measure only part of the I/V curve for panels with V\ :sub:`OC` greater than about 5V. It should be used to measure I\ :sub:`SC`\ for any panel. To measure the rest of the I/V curve for panels with V\ :sub:`OC` up to 10 volts the circuit can be modified as shown in figure 10. The waveform generator in the ALM2000 can swing a maximum of 10 Volts (-5 to +5) so that will be the ultimate limit of the total voltage range of any I/V measurements that can be produced using these setups.

.. image:: https://wiki.analog.com/_media/university/courses/eps/eps_photovoltaics-f10-r1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 10, solar panel measurement circuit, V\ :sub:`OC` > 5 V


For panels with high V\ :sub:`OC` is will be necessary to take data in each configuration to obtain data for both I\ :sub:`SC` and V\ :sub:`OC`. The data from the two configurations can be combined to get a complete I/V curve.

Hardware Setup:
---------------

Set the vertical scale of scope channel 1 to 1V/div. The vertical scale of channel 2 will depend on the maximum current your panel can generate. Turn on the XY display mode. Set the frequency of waveform generator 1 to 20 Hz, and the horizontal time base so that at least one full 0 to V\ :sub:`OC` sweep is displayed.

Set the amplitude of waveform generator 1 to slightly more than 5V peak-to-peak. Depending on the V\ :sub:`GS` of NMOS transistor M\ :sub:`1`, the offset of the generator will need to be set to -2.5 V + V\ :sub:`GS`. This may take a little experimentation to center the signal ramp applied to the solar panel.

Procedure:
----------

Measure the dimensions of the panel or cell to determine the area in mm\ :sup:`2`\ that collects light. You will need this to estimate the amount of input power from the sunlight. Ideally you should take data outside under constant temperature and sunlight conditions - i.e. no clouds. This may not always be practical depending on the computer used with the Discovery hardware. A sun facing window would work but it would be best to open the window and remove any shades or screens that might reduce the amount of sunlight. You should also make your measurements quickly to avoid the heating of the panel from the direct sunlight that may then change the characteristics during the data-collection. Make sure that you don't cast any shadows or reflections over the panel during the experiment. Once you have fixed the position of the panel with relation to the sun it is NOT TO BE MOVED DURING THE EXPERIMENT.

Once you have obtained an I/V plot using the Waveforms software, export a data file in .csv format. Load the .csv data file into a data analysis software program like MatLab or a spreadsheet (Excel). You should have adjusted the horizontal time base of the scope to display a little more than one sweep of the voltage ramp. Your output data file will probably contain more than one set of voltage and current values from 0 to V\ :sub:`OC`. You should remove this extra data before generating a plot of your data. Remember to convert the channel 2 voltage data to current by dividing by the value of R\ :sub:`1` (10Ω). You should also calculate the power ( I\*V ) for each data point. From your I/V curves calculate values for the fill factor, FF, P\ :sub:`MAX`, maximum efficiency η\ :sub:`MAX` (based on approximately 1mW/mm\ :sup:`2`\ for the incident light power) R\ :sub:`S` and R\ :sub:`SH`.

Repeat taking data for other positions where the panel faces away from the sun.

Questions:
----------

In your lab report, compare the voltage (V) vs current (A) graphs for each panel position and note any differences.

Compare the different maximum powers, voltages, currents and external resistances for the different panel positions and comment on their comparison.

Comment on how power output is affected by the external resistance connected to a photovoltaic panel.

| Calculate the maximum output efficiency for each part as follows:
| Maximum efficiency (%) = (P\ :sub:`MAX`/P\ :sub:`IN`) x 100

Comment on the significance of the size of the efficiency.

Extra Questions:
~~~~~~~~~~~~~~~~

Measure the amount of current flowing through, and power output of your photovoltaic panel over time. Based on the size of your panel determine how large of a PV system you need to supply all the daily energy needs for a typical household.

Each solar Photovoltaic panel produced has certain specifications related to its power output and current flow. Your solar panel is rated at how many Watts of power at how many milliamperes of current. In this lab you should measure the current flow of this panel over a 20 minute period. You should also calculate its power output and energy production over time. You can then calculate how large of an array (panels wired together in parallel / series) you would need to completely supply the energy needed for a typical residence.

Can you determine the relationship between the voltage output of the solar panel and thickness of experimental "clouds"?

Additional Materials: a few sheets of 8" X 11" white translucent paper ( wax paper may be a good choice ) , radiation lamp with 150W bulb, meter stick, ring stand with clamps.

This part of the lab will simulate how the solar panel is affected by varying amounts of cloud cover using sheets of somewhat transparent or translucent paper to simulate cloud thickness. You will be looking to see if there is a mathematical relationship between cloud thickness and voltage output of the panel. While the voltage produced is not the true measure of energy being collected in this situation, it will show the relationship we are looking for.

Determine if changing the angle of your panel over time to follow the Sun would add up to substantial savings in your energy bill?

You will need a protractor or inclinometer to measure the angle of the panel to the incident sunlight.

Much is made of the amount of energy lost by fixed Photovoltaic systems because they don't always point with the optimal angle of the sun. In this lab you should investigate how changing the angle of your panel varies the amount of current produced by the panel, and how that would relate to a typical energy bill. You will need to perform this lab at a time when sky cover is very consistent. It is preferable to have sunny skies, but a uniform cloud cover will work.

**For Further Reading:**

| http:*en.wikipedia.org/wiki/Solar_cell
  http:*\ en.wikipedia.org/wiki/Theory_of_solar_cells
| http:*pveducation.org/pvcdrom/characterisation/introduction
  http:*\ users.df.uba.ar/sgil/physics_paper_doc/papers_phys/e&m/I-V_measure_solar_cell.pdf
| Mathworks Solar Cell model: http://www.mathworks.com/help/physmod/elec/ref/solarcell.html?searchHighlight=solar+cell
| Solar Cell Spice model: http://www.intusoft.com/nlhtm/nl78.htm#The_Solar_Cell_SPICE_Model

**Return to EPS Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/eps/main-page>`\ **.**

Appendix :
~~~~~~~~~~

Solar panels come in many sizes with various voltage and current specifications and various prices. Just about any panel or combination of panels that provide between 5V and 9 V and current up to 100 mA will work for these lab ( and related ) activities. The following are a few sources for solar panels.

Sun Power panels are made of Copper Indium Diselenide. They are 60mm (2-3/8") square, with nominal 4.5 V\ :sub:`OC` and 90mA I\ :sub:`SC` in full sunlight. Two of these small panels could be used in series.

.. image:: https://wiki.analog.com/_media/university/courses/eps/eps_photovoltais-f11.jpg
   :align: center
   :width: 300px

.. container:: centeralign

   60mm square solar panel


| Suppliers:
| `SOLAR CELL, 3V 40MA <https://www.allelectronics.com/item/spl-30/solar-cell-3v-40ma/1.html>`_
| OSEPP SC10072 Monocrystalline Solar Cell - Barrel Plug Termination, 100mA I\ :sub:`SC`, 7.2 V\ :sub:`OC`. This one comes prewired with a power plug. A matching jack would be needed to connect the panel to your experiments.

.. image:: https://wiki.analog.com/_media/university/courses/eps/eps_photovoltais-f12.jpg
   :align: center
   :width: 400px

| Supplier:
| http://www.tigerdirect.com/applications/SearchTools/item-details.asp?EdpNo=4368549&csid=_61

.. |eps_photovoltais-f5.png| image:: https://wiki.analog.com/_media/university/courses/eps/eps_photovoltais-f5.png
   :width: 350px
.. |image1| image:: https://wiki.analog.com/_media/university/courses/eps/eps_photovoltais-f6.png
   :width: 350px
