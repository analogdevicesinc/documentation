Mechanical and Thermal Considerations
=====================================

Stacking Considerations
-----------------------

In order to maintain the dual-polarization lattice spacing of 7.5 mm between on-tile HMC8108s and between tiles when stacked vertically, there are a few things that need to be considered. The parts placement in layout needs to be done so that there is no more than 7.5 mm of space between each Rx channel on tile. Additionally, part heights need to be verified to make sure that stacking is possible. The tallest component in the BOM for this design is the LTM8020 power module, coming in at 2.42mm. This ensures that the tiles can be vertically stacked with leeway.

Another stacking consideration that is made is the choice of tile-to-backplane controls/data connector. The main points of concern for this connector selection are number of positions, right angle mount, part height, and on-board termination. For this application, the `SAMTEC ERF5-RA <https://www.samtec.com/products/erf5-ra>`_ right-angle board mounted socket is ideal. This connector has a height of 4.75mm while containing 100 positions and supporting high speed applications with up to 28 Gbps performance.

The same stacking consideration has to be made for the on-tile power connector. The main points of concern for this are voltage rating (12 V), continuous current rating (1.5 A) and surge current rating (4.5 A) in addition to the aforementioned physical specs including part height, PCB mount orientation and termination method. The standard `TSM-102-01-L-SH-P-TR <https://www.samtec.com/products/tsm-102-01-l-sh-p-tr>`_ surface mount 0.1000" pitch TSM series header from SAMTEC is ideal for fitting these specifications.

Thermal Considerations
----------------------

A steady-state thermal simulation on ANSYS FLUENT was conducted to assess the thermal safety of the power dissipating devices in an eight-tile stackup using preliminary on-tile parts placement. A fan was applied within the simulation with a rotational speed of 3000 RPM that was positioned 200mm away from the platform and blew laterally between the tiles. The results showed that with the fan on at 3000 RPM, all devices on all eight boards are thermally safe with the exception of the LTC6953 chip on Tile 6 in the stack. The simulation result is shown below.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_overalltemp.png
   :width: 600px

**Figure 1: Overall Thermal Simulation Result for 8-Tile Stackup**

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_tile6temp.png
   :width: 600px

**Figure 2: Tile 6 Temperature Hotspot**

It is observed that on Tile 6, the junction temperature of the LTC6953 chip is 131.91 degrees Celsius, which is 1.91 degrees over the rated junction temperature of the chip. It also seems that the main hotspot of each board is centered around the LTC6953. This makes sense due to the relatively higher power consumption of this chip compared to the other chips on the board. A few potential solutions for this problem include shifting these chips closer to the middle of the board so that there is more surface area for heat dissipation or including thermal vias underneath the LTC6953 chips which may not be possible due to the stacking considerations mentioned in the previous section.
