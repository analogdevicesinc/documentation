Activity: An Ohm's Law Experiment - ADALM2000
=============================================

Objective:
----------

| Covered in this Lab Activity:
| How electrical charge relates to voltage, current, and resistance.
| What voltage, current, and resistance are.
| What Ohm's Law is and how to use it to understand electricity.
| A simple experiment to demonstrate these concepts.

Electricity Basics:
-------------------

When beginning to explore electricity and Electrical Engineering, it is useful to start by understanding the basic relationships between voltage, current, and resistance. These are the three basic quantities required to understand and use electricity. At first, these concepts can be difficult to understand because they cannot be physically "seen". We cannot see with the unaided eye the energy flowing through a wire or the voltage of a battery sitting on a bench. Even lightning in the sky, while visible, is not truly the energy exchange occurring from the clouds to the ground, but it is the heating of the air by the energy passing through it that produces the flashes of light. In order to detect this electrical energy, we must use measurement tools such as multi-meters, oscilloscopes and spectrum analyzers to visualize what is happening with the electrical signals in a system. Fear not, however, this lab activity will give you the basic understanding of voltage, current, and resistance and how the three relate to each other.

Electrical Charge:
~~~~~~~~~~~~~~~~~~

Electricity is the movement (flow) of electrons. Electrons are atomic particles with a negative charge. Moving these charges can be harnessed to do work. A light bulb, a fan, a radio, a mobile phone, etc., are all harnessing the movement of the electrons in order to perform some function. They all operate using the same basic energy source: the storage and movement of electrons.

The three basic principles for this activity can be explained using electrons, or more specifically, the charge they create:

| 1. Voltage is the difference in charge (more electrons, less electrons) between two points in space.
| 2. Current is the rate at which charge (electrons) is flowing between two points usually through some material.
| 3. Resistance is a material's tendency to resist the flow of charge (electrical current). Materials with very low resistance are called conductors. Materials with a very high resistance are called insulators.

So, when we talk about these values, we're really describing the movement of charge, and thus, the behavior of electrons. A circuit is a closed loop that allows charge to move from one place to another. Components in the circuit allow us to control this charge and use it to do work.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/georg-ohm.png
   :align: center
   :width: 200px

.. container:: centeralign

   Georg Ohm


Georg Ohm was a Bavarian scientist who studied electricity. Ohm starts by describing a unit of resistance that is defined by current and voltage. So, let's start with voltage and go from there.

Voltage
~~~~~~~

We define voltage as the amount of potential energy between two points on a circuit. One point has more charge (electrons) than another. This difference in charge between the two points is called voltage. It is measured in volts, which, technically, is the potential energy difference between two points that will impart one joule of energy per coulomb of charge that passes through it (don't panic if this physics jargon makes no sense, it is not really important at this point). The unit “volt” is named after the Italian physicist Alessandro Volta who invented what is considered the first chemical battery. Voltage is represented in equations and schematics by the capital letter “V”.

When describing electrical properties like voltage, current, and resistance, a common analogy is a water tank. In this analogy, charge is analogous to the volume water, voltage is represented by the water pressure (depth of the water), and current is represented by the water flow. So for this analogy, remember:

| Water = Charge
| Pressure = Voltage
| Flow = Current

Consider a water tank at a certain height above the ground. At the bottom of this tank there is a hose. The pressure at the end of the hose can represent voltage. The water in the tank represents charge. The more water in the tank, the higher the charge, and the more pressure is measured at the end of the hose.

We can think of the water tank as a battery, a place where we store a certain amount of energy and then release it. If we drain our tank a certain amount, the pressure created at the end of the hose goes down. We can think of this as decreasing voltage, like when a flashlight gets dimmer as the batteries run down. There is also a decrease in the amount of water that will flow through the hose. Less pressure means less water is flowing, which brings us to current.

Current
~~~~~~~

We can think of the amount of water flowing through the hose from the tank as current. The higher the pressure, the higher the flow, and vice-versa. With water, we would measure the volume of the water flowing through the hose over a certain period of time. With electricity, we measure the amount of charge flowing through the circuit over a period of time. Current is measured in Amperes (usually just referred to as “Amps”). An ampere is defined as 6.241x10\ :sup:`18` electrons (1 Coulomb) passing through a point in a circuit per second. Amps are represented in equations by the capital letter “I”.

Let's say now that we have two tanks the same size with the same amount of water in them, but the hose on one tank is narrower (smaller diameter) than the hose on the other. We measure the same pressure at the end of both hoses because there is the same amount of water pressing down, but when the water begins to flow, the flow rate of the water in the tank with the narrower hose will be less than the flow rate of the water in the tank with the wider hose.

In electrical terms, the current through the narrower hose is less than the current through the wider hose. If we want the flow to be the same through both hoses, we have to increase the amount of water (charge) and thus the pressure in the tank with the narrower hose. This increased pressure (voltage) at the end of the narrower hose pushes more water through the tank. This is analogous to an increase in voltage that causes an increase in current.

Now we're starting establish the relationship between voltage and current. But there is a third factor to be considered here: the diameter of the hose. In this analogy, the diameter of the hose determines the resistance to the flow of water (charge). This means we need to add another term to our model:

| Water = Charge (measured in Coulombs)
| Pressure = Voltage (measured in Volts)
| Flow = Current (measured in Amperes, or “Amps” for short)
| Hose Diameter = Resistance

Resistance
~~~~~~~~~~

Consider again the two water tanks, one with a small diameter pipe and one with a large diameter pipe.

It stands to reason that we can't fit the same volume of water through a narrow pipe than a wider one at the same pressure. This is resistance. The narrow pipe “resists” the flow of water through it even though the water is at the same pressure as the tank with the wider pipe.

In electrical terms, this is represented by two circuits with equal voltages and different resistances. The circuit with the higher resistance will allow less charge to flow; meaning the circuit with higher resistance has less current flowing through it.

This brings us back to Georg Ohm. Ohm defines the unit of resistance of “1 Ohm” as the resistance between two points in a conductor where the application of 1 volt will cause 1 ampere, or 6.241x10\ :sup:`18` electrons per second to flow. This value is usually represented in schematics with the Greek letter “Ω”, which is pronounced omega, and sounds a lot like “ohm”.

Ohm's Law
~~~~~~~~~

Combining the elements of voltage, current, and resistance, Ohm developed the formula:

:math:`V=I \times R`

| Where:
| V = Voltage in volts
| I = Current in amps
| R = Resistance in ohms

This is called Ohm's law. For example, say that we have a circuit with the potential of 1 volt, a current of 1 amp, and resistance of 1 ohm. Using Ohm's Law we can say:

:math:`1V=1A \times 1Omega`

Going back to the water analogy, say this represents our tank with a wide hose. The amount of water in the tank is defined as 1 volt and the “narrowness” (resistance to flow) of the hose is defined as 1 ohm. Using Ohms Law, this gives us a flow (current) of 1 amp.

Now consider at the tank with the narrow hose. Because the hose is narrower, its resistance to flow is higher. For the case with a narrower hose we can define the resistance to be twice as much or 2 ohms. The amount of water in the tank is the same as the other tank so the voltage is the same. Using Ohm's Law, our equation for the tank with the narrow hose is:

:math:`1V=?A \times 2Omega`

But what is the current? Because the resistance is greater, and the voltage is the same, this gives us a current value of 0.5 amps:

:math:`1V=0.5A \times 2Omega`

So, the current is lower in the tank with higher resistance as we predicted. Now we can see that if we know two of the values for Ohm's law, we can solve for the third.

Let's demonstrate this with an experiment.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For this experiment, we want to light up an LED (Light Emitting Diode). LEDs are somewhat fragile and should have only a certain amount of current flowing through them. Current larger than the maximum allowed can burn them out. In the datasheet for an LED, there will always be a “current rating”. This is the maximum amount of current that can flow through the particular LED before it is damaged.

We will be using the +5V power supply from the ADALM2000 as the voltage source.

Materials:
~~~~~~~~~~

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 1 LED, the longer of the two leads is the anode (+) and the shorter lead is the cathode (-)
| 1 Resistor
| NOTE: LEDs are known as “non-ohmic” devices. This means that the equation for the current flowing through the LED itself is not the simple linear relationship V=IR. The LED is a special kind of diode. All diodes have something called an internal “voltage drop”. However, in this experiment we are simply trying to protect the LED from conducting too much current, so we can neglect the non-ohmic current characteristics of the LED for the moment and choose the resistor value using just Ohm's Law in order insure that the current through the LED will be safely less than 20mA.

For this example, we have the V+ output of the ADALM2000 configured to generate 5V and a (red) LED with a current rating of 20 milliamps, or 0.020 amps. To be safe, we would rather not drive the LED at its maximum current but rather its suggested current, which is listed on its datasheet as 18mA, or 0.018 amps. If we simply connect the LED directly to the battery, the values for Ohm's law look like this:

:math:`V=IR`

Rearranging for I:

:math:`I=V/R`

With just wire and no resistor yet:

:math:`\displaystyle I=\frac{5}{0}`

Dividing by zero results in infinite current! Not actually infinite in practice, but as much current as the +5 volt supply of the ADALM2000 can deliver. We certainly do not want that much current flowing through the LED. We are going to need to include a resistor.

Our circuit connections should look like this:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/led_power_5v.png
   :align: center
   :width: 400px

.. container:: centeralign

   Schematic, Circuit to power LED from +5 V power supply


We can use Ohm's Law to determine the resistor value that will give us the desired current value:

:math:`V=IR`

Rearranging for R:

:math:`R=V/I`

Plugging in the values 5 Volts and 0.018 Amps:

:math:`\displaystyle R=\frac{5}{0}.018`

Solving for the resistance:

:math:`R=277Omega`

So, the resistor value we need for R\ :sub:`1` is around 277 ohms to keep the current through the LED under the maximum current rating.

277 Ohms is not a common value for off-the-shelf resistors, so for this experiment use a 470 ohm resistor (yellow purple brown) which is the next closest value greater than 277 in the ADALP2000 parts kit. Below is what your circuit should look like all put together.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/led_power_5v_bb.png
   :align: center
   :width: 900px

.. container:: centeralign

   Breadboard, Circuit to power LED from +5 V power supply


Success! We've chosen a resistor value that is high enough to keep the current through the LED below its maximum rating, but low enough that the current is sufficient to keep the LED nice and bright. Enable the positive power supply to 5V. If the LED does not light up be sure to double check that the (+) and (-) ends of the LED are connected correctly.

This LED/current-limiting resistor example is a common occurrence in electronics. You'll often need to use Ohm's Law to change the amount of current flowing through the circuit.

Current Limiting Before or After the LED?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To make things a little more complicated, you can place the current limiting resistor on either side of the LED, and it works just the same.

|image1| Many readers learning electronics for the first time struggle with the idea that a current limiting resistor can be inserted on either side of the LED and the circuit will still function as usual. Try swapping the resistor and LED in your circuit. Does the LED still light up with the same brightness for both cases?

Here is yet another water analogy, imagine a water pipe that is a continuous loop with a pump that continuously circulates the water. If we were to place a valve somewhere in the pipe, with the valve closed the water in entire pipe would stop flowing, not just one section. Now imagine we open the valve a little which restricts the flow of the water. It wouldn't matter where in the loop the partly open valve is inserted, it will still slow the flow in the entire pipe. The water does not back up behind the valve. The pressure in the section of the pipe between the outlet side of the pump and the valve increases while the pressure in the section of the pipe between the valve and the outlet side of the pump decreases. The pump is analogous to the voltage source increasing the voltage while the valve is analogous to the resistor decreasing the voltage.

This is an oversimplification, as the current limiting resistor can only be placed in the circuit in two places; it can be placed on either side of the LED to perform its function.

For a more scientific answer, we turn to Kirchoff's Voltage Law. It is because of this law that the current limiting resistor can go on either side of the LED and still have the same effect. For more info and some practice problems using KVL, :doc:`visit this website </wiki-migration/university/courses/electronics/text/chapter-1>`.

Measuring the actual Voltage and Current
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADALM2000 also has two input channels that can be used as a voltmeter. We can connect them as shown in the next schematic to measure the actual voltages in the circuit, The Channel 1 voltmeter input is connected to measure the +5 V power supply and the Channel 2 voltmeter is connected to measure the voltage at the (+), positive, end of the diode.


|image2|

.. container:: centeralign

   Schematic, Measure the actual voltages in the circuit.


Connect the voltmeter inputs as shown.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/measure_voltage_bb.png
   :align: center
   :width: 900px

.. container:: centeralign

   Breadboard connections for measuring the actual voltages in the circuit.


Start the Scopy Voltmeter tool. The interface looks like this.



|image3|

.. container:: centeralign

   Voltmeter tool screen


| Click on the green Run button and the circuit voltages will be displayed. The Channel 1 Voltage should display the actual value of the +5 V power supply. The Channel 2 Voltage should display the actual voltage across the LED diode. In this example for a red LED the voltage was 1.84 volts. The difference between these two voltages, Channel 1-Channel 2 V, will be the voltage across the resistor which in this example was 3.12 volts.
| We can use Ohm's law to calculate the current in the resistor:

:math:`I=V/R`

Or:

:math:`\displaystyle I=3.\frac{12}{470}=0.0066A`

Or:

6.6 mA

Resources and Going Further
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now you should understand the concepts of voltage, current, resistance, and how the three are related. Congratulations! The majority of equations and laws for analyzing circuits can be derived directly from Ohm's Law. By knowing this simple law, you understand the concept that is the basis for the analysis of any electrical circuit!

These concepts are just the tip of the iceberg. If you're looking to study further into more complex applications of Ohm's Law and the design of electrical circuits, be sure to check out the following hands on activities.

.. admonition:: Download
   :class: download

   **Lab Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/ohm_law_bb`
   -  LTSpice files: :git-education_tools:`m2k/ltspice/ohm_law_ltspice`
   


**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/limiting_before_after.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/measure_voltage.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/voltmeter_interface.png
   :width: 900px
