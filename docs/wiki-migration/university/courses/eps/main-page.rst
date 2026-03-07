Energy & Power Systems Activities Outline
=========================================

Objective:
----------

The objectives of the Lab Activities centered around the Energy and Power Systems (EPS) Hardware Module are to explore a variety of electrical engineering concepts related to the generation, storage and control of energy and power.

Some of the experiments are best constructed first on a solder-less breadboard before incorporating them onto the main system board. Some things like the motor and generator only work well when firmly attached to a board. Many of the basic components can be found in the Analog Parts Kits but additional quantities of certain parts will be needed beyond those in the Kit. A complete list is included later in this document.

Electrical Engineering Concepts:
--------------------------------

-   Electronic component characteristics

   -   :doc:`Diode I/V characteristics </wiki-migration/university/courses/eps/diode-curves>`

      -   Conventional Si diode
      -   Schottky barrier diode
      -   Zener (avalanche) breakdown diode
      -   Light Emitting Diode (LED)

         -   LED as a photo diode (miniature solar cell)

   -   NPN and PNP BJT transistors

      -   :doc:`I/V characteristics </wiki-migration/university/courses/eps/bjt-i-v-curves>`
      -   Current Gain
      -   Application as an amplifier
      -   :doc:`Application as a switch </wiki-migration/university/courses/eps/bjt-switch>`

-   Voltage reference circuits

   -   :doc:`Zener diode </wiki-migration/university/courses/eps/zener-regulator>`
   -   :doc:`Bang-gap reference </wiki-migration/university/courses/eps/band-gap-regulator>`

-   :doc:`Photovoltaic Solar Cells </wiki-migration/university/courses/eps/photovoltaic>`

   -   Open circuit voltage
   -   Short circuit current
   -   Output current vs. output voltage characteristics
   -   Output voltage and current for maximum power
   -   Control circuits

      -   Linear voltage regulator (LDO circuits)
      -   Switch mode regulator, Buck, Boost or Buck-Boost types

-   :doc:`Rechargeable battery characteristics </wiki-migration/university/courses/eps/rechargeable-battery>` (NiCd / NiMH)

   -   Internal resistance vs. state of charge
   -   Open circuit voltage vs. state of charge
   -   Optimal charge / discharge rate

-   Characterization of DC motors

   -   DC resistance and energy lost to heat (measure rise in case temperature)
   -   No load RPM vs. voltage and current
   -   Stall current

-   Characterization of DC generator (use DC motor as a generator)

   -   Output voltage and current vs. shaft RPM
   -   Efficiency of combined motor/generator set, including DC resistance losses
   -   Case temperature rise vs. load on generator

-   DC motor driver and control circuits

   -   Linear driver
   -   Switch mode driver, Pulse Width Modulation (PWM)
   -   Driver efficiency

-   Electrical measurement techniques

   -   Analog multiplexing
   -   Voltage divider
   -   Current sense (shunt resistor)

      -   Difference amplifier circuit

   -   Calibration to correct for errors
   -   Tachometers, measuring rotational speed

      -   Hall Effect sensors
      -   Optical sensors
      -   Strobe
      -   Frequency-to-voltage circuits

   -   Temperature sensing

-   Control systems

   -   Negative feedback
   -   Stability
   -   Frequency compensation
   -   Settling time, damping factor

Energy and Power Systems (EPS) Hardware Module:
-----------------------------------------------

The hardware module consists of a roughly 3.5" X 4" circuit board that provides space for a small mechanically interconnected motor-generator set that can serve as a model for a power plant that utilizes expendable fuels. A port for connecting a small solar panel is provided to model an intermittent renewable energy source. Six switchable LEDs serve as a variable load to the simulated power system.

It models power generation, and distribution in a simulated real-life setting. Analog Discovery along with the Waveforms software and custom software is used to measure the operating parameters and control the system as the power produced from the motor-generator and solar panel change and as the load changes. A rechargeable battery is connected to store excess power when generation is larger than the load and release power when the load demand is greater than the generation capacity. This is measured through things such as the power produced and consumed, as well as an RPM measurement from the motor-generator.

Figure 1 is the schematic of the system board. Figure 2 shows a completed board connected to the Discovery module, a 9V 6 cell AA battery holder (to power the DC motor), a small solar array and a rechargeable NiCd battery pack. A Hall effect sensor and magnet mounted on the motor-generator shaft measures the RPM.

.. image:: https://wiki.analog.com/_media/university/courses/eps/energy_power_adg.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 1, Energy and Power Systems (EPS) Hardware Module schematic


.. image:: https://wiki.analog.com/_media/university/courses/eps/eps_12.jpg
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 2, Energy and Power Systems (EPS) Hardware with solar panel and battery


\*\* Hardware User's Guide \*\*

:doc:`EPS Hardware User's Guide </wiki-migration/university/courses/eps/users-guide>`

**PC Board design files:**

| Eagle CAD and Gerber files `schematic and board files <https://wiki.analog.com/_media/university/courses/eps/power_system_adg.zip>`_
| **Parts List:**

Table 1 lists the required parts to build out the EPS system board. Suggested sources with part numbers for the various parts are included. Table 2 lists the generic passive devices needed.

+-------------------------------------------------+----------+---------------+---------------+-----------+------------+
| Description                                     | Quantity | Supplier      | Part Number   | Unit Cost | Total Cost |
+=================================================+==========+===============+===============+===========+============+
| 9V DC motor                                     | 2        | Jameco        | 232144        | $2.95     | $5.90      |
+-------------------------------------------------+----------+---------------+---------------+-----------+------------+
| Neodymium Ring Magnet, diametrically magnetized | 1        | K&J Magnetics | R424DIA       | $0.61     | $0.61      |
+-------------------------------------------------+----------+---------------+---------------+-----------+------------+
| Solar panel, 60X60X2MM                          | 2        | Jameco        | 1928142       | $7.95     | $15.90     |
+-------------------------------------------------+----------+---------------+---------------+-----------+------------+
| 3.6 V Rechargeable battery                      | 1        | Sears         | SPM7155360313 | $0.99     | $0.99      |
+-------------------------------------------------+----------+---------------+---------------+-----------+------------+
| 2N3904 NPN transistor                           | 6        | Jameco        | 38360         | $0.05     | $0.50      |
+-------------------------------------------------+----------+---------------+---------------+-----------+------------+
| TIP32 PNP transistor                            | 1        | Jameco        | 181841        | $0.35     | $0.35      |
+-------------------------------------------------+----------+---------------+---------------+-----------+------------+
| 1N5230BTR 4.7V 0.5W Zener Diode                 | 1        | Jameco        | 179039        | $0.07     | $0.07      |
+-------------------------------------------------+----------+---------------+---------------+-----------+------------+
| 1N5817 Schottky diode                           | 2        | Jameco        | 177949        | $0.14     | $0.28      |
+-------------------------------------------------+----------+---------------+---------------+-----------+------------+
| 5 mm LED, various colors                        | 6        | Jameco        | 333973        | $0.12     | $0.72      |
+-------------------------------------------------+----------+---------------+---------------+-----------+------------+
| Dual opamp, AD822 or similar                    | 3        | ADI           | AD822ANZ      |           |            |
+-------------------------------------------------+----------+---------------+---------------+-----------+------------+
| Dual 4:1 analog Mux, ADG609                     | 1        | ADI           | ADG609BNZ     |           |            |
+-------------------------------------------------+----------+---------------+---------------+-----------+------------+
| Hall effect sensor                              | 1        | Jameco        | 1915835       | $1.19     | $1.19      |
+-------------------------------------------------+----------+---------------+---------------+-----------+------------+
| 30 pin right angle female header                | 1        | Digikey       | S5568-ND      | $2.60     | $2.60      |
+-------------------------------------------------+----------+---------------+---------------+-----------+------------+
| 8 position DIP switch                           | 1        | Jameco        | 38842         | $0.79     | $0.79      |
+-------------------------------------------------+----------+---------------+---------------+-----------+------------+
| 2 pin male headers                              | 11       | Jameco        | 108338        | $0.25     | $2.75      |
+-------------------------------------------------+----------+---------------+---------------+-----------+------------+
| SPDT slide switch (9V power)                    | 1        | DigiKey       | 679-1849-ND   | $0.59     | $0.59      |
+-------------------------------------------------+----------+---------------+---------------+-----------+------------+
| SPDT slide switch (feedback)                    | 1        | Digikey       | 679-1848-ND   | $0.60     | $0.60      |
+-------------------------------------------------+----------+---------------+---------------+-----------+------------+

.. container:: centeralign

   Table 1


============= ======= ======== ================== ==========
Resistors     Value   Quantity mcmelectronics.com 20 pack 5% 
============= ======= ======== ================== ==========
1/4 W         1.5 Ω   5                                      
1/8 or 1/4 W  100 Ω   7        373-100            $0.49      
1/8 or 1/4 W  1 KΩ    1        373-1K             $0.49      
1/8 or 1/4 W  1.5 KΩ  1        373-1.5K           $0.49      
1/8 or 1/4 W  5.6 KΩ  6        373-5.6K           $0.49      
1/8 or 1/4 W  10 KΩ   10       373-10K            $0.49      
1/8 or 1/4 W  33 KΩ   10       373-33K            $0.49      
1/8 or 1/4 W  47 KΩ   6        373-47K            $0.49      
1/8 or 1/4 W  220 KΩ  10       373-220K           $0.49      
Potentiometer Value   Quantity DigiKey part #                
\             50KΩ    1        3386P-503TLF-ND    $2.30      
Capacitors    Value   Quantity                               
\             0.01 uF 2                                      
\             0.1 uF  3                                      
\             1.0 uF  2                                      
\             10.0 uF 1                                      
============= ======= ======== ================== ==========

.. container:: centeralign

   Table 2


Most suppliers sell passive components like resistors in large minimum quantities of 100 or 200 pieces at very low effective unit prices. Radio Shack offers resistors in quantities of 5 but at a much higher unit cost. MCMElectronics.com offers 1/8 watt resistors in quantities of 20 at reasonable cost as listed in table 2. DigiKey will sell any quantity down to single resistors at $0.10 each for 1/6 watt 5% carbon film types. Electronix Express sells 1/4 watt resistors in minimum quantities of 10 at $0.06 each.

Notes on alternate sources:
~~~~~~~~~~~~~~~~~~~~~~~~~~~

No one supplier can provide the complete list of components. Prices can vary widely from supplier to supplier for essentially the same component. It's a matter of how much time one wishes to put into shopping around to find the best prices for each major component.

The same 60X60 mm 4.5 Volt solar panels are available from `Electronic Goldmine <http://www.goldmine-elec-products.com/prodinfo.asp?number=G16394>`_, part number G16394, for $3.50 each which is less than half the Jameco price.

The same 9V DC motors are available from DigiKey, part number P14356-ND, for $3.53 each. The 3.6V rechargeable NiCd or NiMH three cell batteries are commonly used in cordless telephone handsets and can be sourced from many places such as this one from Sears: Item# SPM7155360313, OEM Cordless Phone Battery, 3.6V / 800mAh, Uniden BT-446.

Supplier web site links:
~~~~~~~~~~~~~~~~~~~~~~~~

| http://www.analog.com/
| http://www.jameco.com/
| http://www.bgmicro.com/
| http://www.goldmine-elec-products.com/
| http://www.kjmagnetics.com/
| http://www.digikey.com/
| http://www.elexp.com/
| http://www.radioshack.com/

Construction directions:
~~~~~~~~~~~~~~~~~~~~~~~~

To assemble the Power and Energy Systems PC board, you need certain hand tools such as a wire cutter, wire stripper, long nose pliers, and a soldering iron. Use caution with the soldering iron, as it get very hot! When soldering parts onto a circuit board, it is best to start with the shortest pieces and work your way up to the taller ones. The reason is that when you turn the board over to solder, the shorter pieces will not be held in by the table if taller pieces are already placed on the board. Often it is helpful to use small pieces of masking tape to hold the smaller components in place while soldering. The following steps are ordered for ease of installation.

.. note::

   Under construction

   
   DC Motors -The two mechanically coupled 9V DC motors comprise a motor/generator set. The first motor takes electrical energy from the battery and converts it into mechanical energy. This models the actual process whereby the mechanical force from an energy source such as wind, flowing water or a spinning a turbine from burning fuels is converted into a physical motion,. The second motor (GEN) is the generator that takes mechanical energy from the first motor and converts it back into electricity in our case.
   
   Hall Effect Sensor - The Hall effect sensor measures how fast the motor is spinning (RPM) by detecting the magnet mounted on the shafts along with the heat shrink tubing connecting the motors. It is powered by the Discovery 5V power supply, and uses a pull-up resistor connected to the open drain output of the sensor to a generate a logic level detectable by a digital input. Digital input DI 15 then reads 5 V pulses using an edge count, which is converted into an RPM in the software program.


**Energy Expenditure**

The power provided by the mechanical and solar energy sources is combined and used to power up to six LEDs, representing any kind of load that might be used in a real-life power system (lights, air conditioners, etc.). The power must reach a certain threshold before the LEDs will turn on. LEDs-The LEDs provide the function of simulating a load. Lighting the LEDs is the ultimate purpose of the power system, and so it is essential that the proper power is applied to them. The LEDs operate at around 1.67 V, and will usually turn on when about 4.5 V is applied to the generator (may vary depending on efficiency of the motors, battery life, etc.). In the case of real-life loads powered by plants, there exists a variable demand for power. Since electrical energy cannot be stored, it must be continually generated to meet the demand, requiring some sort of control system.
