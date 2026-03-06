Activity: What is Polarity and Why do we care?
==============================================

Background:
-----------

In the study of electricity and electronics, polarity indicates if a component is symmetric or not. For a component with just two terminals this means the two terminals are interchangeable. For a non-polarized component, a part without polarity, the terminals can be connected in either direction and it will still function the way it is supposed to. A symmetric component generally has only two terminals, and every terminal on the component is equivalent. A network of multiple symmetric two terminal components could also possible be symmetric. You can connect a non-polarized component in any direction, and it will function just the same.

A polarized component, a part with polarity, can only be connected in a circuit in one direction. That is to say that the more positive terminal voltage and more negative terminal voltage can only be connected to the proper terminals. Also the current in the terminal will only flow generally in one direction. Polarity is generally indicated by using positive (+) and negative (-) signs on schematics and marking on the actual components themselves. Other markings and pin designations can be used as well to distinguish which pin or terminal is which.

A polarized component might have two, twenty, or even two-hundred pins, and each one has a unique function and/or position. When a polarized component is connected in a circuit incorrectly, at the very best it will not function as intended. At worst, an incorrectly connected polarized component will become damaged and will no longer function again even when connected properly.

Polarity is a very important concept in electronics, especially when physically constructing circuits. Whether you are plugging parts into a breadboard, soldering them to a PCB, it’s critical to be able to identify polarized components and to connect them in the proper direction. That is objective of this lab activity. We will discuss which components do and do not have polarity, how to identify component polarity, and how to test some components for polarity.

Some Simple Non-polarized Examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

So called passive components like resistors, capacitors and inductors are generally not polarized. There are of course exceptions to that rule.

Special case Capacitors
~~~~~~~~~~~~~~~~~~~~~~~

Not all capacitors are polarized, but when they are, it’s very important not to mix up their polarity.

Ceramic capacitors – the small (typicaly 1µF and less), commonly blue or yellow colored ceramic bodies – are not polarized. You can connect those either way in the circuit.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-polarity-f1.png
   :align: center
   :width: 400px

.. container:: centeralign

   Ceramic caps are NOT polarized.


Through-hole and SMD 0.1µF ceramic capacitors. These are NOT polarized.

Electrolytic and Tantalum Capacitors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Electrolytic capacitors (they contain electrolytes), which look like little tin cans, are polarized. The negative pin of the capacitor is usually indicated by a (-) marking, and/or a colored strip along the can. They might also have a longer positive leg. Below is an electrolytic capacitor which has a dash symbol to mark the negative leg, as well as a longer positive leg and a tantalum capacitor.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-polarity-f2.png
   :align: center
   :width: 400px

.. container:: centeralign

   Polarized electrolytic and tantalum capacitors


Applying a negative voltage for an extended period to a polarized electrolytic or tantalum capacitor will result in a briefly exciting, but catastrophic, failure. They’ll make a pop, and the top of the cap will either swell or burst open. Tantalum capacitors can even catch on fire. From then on the cap will be as good as dead, acting like a short circuit.

Polarized Components
--------------------

Batteries and Power Supplies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Getting polarity right in your circuit starts and ends with getting the power supply connected correctly. Whether your project is getting power from a wall powered supply, a battery or even the ADALM1000, it is critical to make sure you do not accidently connect the positive and negative terminals backwards and effectively apply -9V or -5V to your circuit by accident.

Anyone that has ever replaced batteries knows how to find their polarity. Most batteries will indicate the positive and negative terminals with a “+” or “-” symbol. Other indicators of polarity might be the color of the wires, red for positive and black for negative.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-polarity-f3.png
   :align: center
   :width: 400px

.. container:: centeralign

   All batteries should have some way to identify polarity


All batteries. Lithium polymer, coin cell, 9V alkaline, AA alkaline, and AA NiMH have some way to represent the positive and negative terminals.

Power supplies usually have a standardized connector, which should usually have polarity itself. A barrel jack, for example, has two conductors: outer and inner; the inner/center conductor is usually the positive terminal. Other connectors, have keys so you they cannot be inserted backwards.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-polarity-f4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Power supply connectors


For extra protection against reversing power supply polarity, you can add reverse polarity protection using a diode, or a MOSFET.

Diode and LED Polarity
~~~~~~~~~~~~~~~~~~~~~~

Diodes are two terminal components that only allow current to flow in one direction, and they are always polarized. The positive terminal (+) is called the anode, and the negative terminal is called the cathode.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-polarity-f5.png
   :align: center
   :width: 550px

.. container:: centeralign

   Diode circuit symbols, with anode/cathode labeled


Current through a diode can only flow from the anode to the cathode, which would explain why it’s important for a diode to be connected in the correct direction. Physically, every diode should have some sort of indication for either the anode or cathode pin. Usually the diode will have a line near the cathode pin, which matches the vertical line in the diode circuit symbol.

Below are a few examples of diodes. The diode with a black plastic body is a 1N4001 rectifier and it has a grey ring near the cathode. The diode with a glass body is a 1N914 signal diode with a black ring to mark the cathode.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-polarity-f6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Diode polarity indicators


Light Emitting Diodes, LEDs
~~~~~~~~~~~~~~~~~~~~~~~~~~~

LED stands for light-emitting diode, which means that much like other normal diodes, they’ are polarized. There are a handful of identifiers for distinguishing the positive and negative pins on an LED. One is to identify the longer leg, which should indicate the positive, anode pin. Sometimes the leads have been trimmed, try finding the flat edge on the LED’s outer casing. The pin nearest the flat edge will be the negative, cathode pin.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-polarity-f7.png
   :align: center
   :width: 600px

.. container:: centeralign

   LED polarity indicators


There might be other indicators as well. SMD diodes have a range of anode/cathode identifiers. Sometimes it’s easiest to just use a multi-meter to test for polarity. Turn the multi-meter to the diode setting (usually indicated by a diode symbol), and touch each probe to one of the LED terminals. If the LED lights up, the positive probe is touching the anode, and the negative probe is touching the cathode. If it doesn’t light up, try swapping the probes around. Some LEDs like Blue or White LEDs with higher forward voltages will not light in either direction using the diode test function on a multi-meter.

LED polarity test with ALM1000
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The polarity of an LED can be tested with a digital multimeter. If the positive lead touches the anode and negative touches the cathode, the LED should light up. The ALICE Desktop Ohmmeter tool can be used to test diodes and LEDs as well as measure resistors. Connect the positive end of the diode to CH A and the negative end to CH B.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-polarity-f8.png
   :align: center
   :width: 400px

.. container:: centeralign

   ALICE Ohmmeter tool (using internal 50 Ω resistor)


Diodes certainly aren’t the only polarized component. There are tons of parts out there that won’t work if connected incorrectly. Next we’ll discuss some of the other common polarized components, beginning with integrated circuits.

Transistors, MOSFETs, and Voltage Regulators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These (traditionally) three-terminal, polarized components are lumped together because they share similar package types. Through-hole transistors, MOSFETs, and voltage regulators commonly come in a TO-92 or TO-220 package, seen below. To find which pin is which, look for the flat edge on the TO-92 package or the metal heatsink on the TO-220, and match that up to the pin-out in the datasheet.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-polarity-f9.png
   :align: center
   :width: 550px

.. container:: centeralign

   TO-92 transistor, TO-220 NMOS and Vreg


Above, a 2N3904 transistor in a TO-92 package, note the curved and straight edges. Devices in a TO-220 package can have two, three or more leads. An adjustable regulator in a TO-220 package, note the metal heatsink TAB on the back.

This is just the tip of the polarized-component iceberg. Even non-polarized components, like resistors, can come in multi-lead packages. A resistor pack – a grouping of five-or-so pre-arranged resistors – is one such example.

Resistor arrays
~~~~~~~~~~~~~~~

A SIP resistor pack, is an array of five 330Ω resistors, all tied together at one end. The dot represents the first, common pin. The resistors in side are not individually "polarized" but the common connection makes the overall array non-symetric.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-polarity-f10.png
   :align: center
   :width: 600px

.. container:: centeralign

   SIP resistor pack


Fortunately, every polarized component should have some way to inform you which pin is which. Be sure to always read the datasheets, and check the package or case for dots or other markers.

**Resources and Going Further**

Now that you know what polarity is, and how to identify it, why not check out some of these related tutorials:

**For Further Reading:**

**Return to** :doc:`Introduction to Electrical Engineering </wiki-migration/university/labs/intro_ee>` **Lab Activity Table of Contents**
