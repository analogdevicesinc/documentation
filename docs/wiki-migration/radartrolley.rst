Overview
========

This is a setup guide for a programmable trolley slider designed by Dustin, Victor, and Jon. As an example project, the trolley is being used as a automatic target slider to test Victor's SDR radar setup (insert link once I get that page set up). Previously, distance-sensing radar tests were performed by hand, inching a target backwards 1 cm at a time. This trolley will help automate this time-consuming task.

| |image1|

Setup Overview
--------------

The main components of the trolley setup are illustrated in the diagram below:


|image2|

Sub-blocks:

-  **Pi 4:** Sends high-level movement commands (target position, etc.) to Pi 0 based motor control system
-  **Pi 0 based motor control system:** Handles commands for Motor Driver
-  **Motor Driver:** Drives motor via voltage pulses
-  **Motor, coupler, and actuator shaft:** Deliver power to the Slider to move
-  **Limit Switches and Trip:** Notifies Pi 0 when the slider reaches a limit switch

The details for building each sub-block are described in detail in the subsequent sections.

--------------

Materials
=========

-  bulleted
-  list
-  of parts, ideally with part numbers and sizes if possible
-  **stepper motor coupler:** of the right diameters to match the stepper motor and actuator shafts. A caliper may help.

--------------

Building the Trolley
====================

We will be installing our trolley in the following order:

-  Limit Switches
-  Motor
-  Protoboard solderin
-  Wiring/Settings

Limit Switches
--------------

First, we will install the optical limit switches and the trip.

These will keep the slider inside your set limits. We will install one of these towards each end of the rail at least 8 cm from the end so that the slider won’t hit the rail ends when triggering the switch.

Find the nuts inside the side of the rail on the same side as the actuator shaft. Using gravity and/or a thin rod, move a pair of nuts to each of the two limit switch locations. Rest of nuts? Find the shorter versions of the hex bolts as the ones we used to mount the bracket to the rail. Insert these through the two large holes in the limit switch mounting bracket and screw them tightly into the nuts at each limit switch location.

Then use two of the tiny screws to install the limit switches on top of the brackets as shown.

|image3| |image4| |image5|

Using the same tiny screws, screw the trip to the two holes in the side of the slider. This should be on the same side as the limit switches. Move the slider through each limit switch to make sure the trip goes between the pillars of each limit switch without hitting them.

| 

Motor
-----

Next, we will connect the motor to the actuator shaft via an axle coupler.

Check the stepper motor mounting bracket to see if the holes are drilled. We only need the 8 holes circled in the image below: 4 to mount the bracket to the rail and 4 to mount the stepper motor to the bracket. If they are not drilled, drill the holes with a 1/8” drill bit.

.. image:: https://wiki.analog.com/_media/trolley_mounting_bracket_1.jpg
   :width: 200px

Using the supplied Hex Bolts (X4), connect the mounting bracket to the actuator over the actuator shaft. This will require a 5/32 inch hex screw. Do not remove the cube of fluff in the side of the rail when installing the mounting bracket.

|image6| |image7|

Locate the groove in the actuator shaft.

.. image:: https://wiki.analog.com/_media/trolley_mounting_bracket_4.jpg
   :width: 340px

Get the stepper motor coupler.

.. image:: https://wiki.analog.com/_media/trolley_mounting_bracket_5.jpg
   :width: 427px

Line up the small set screw in the larger hole of the coupler with the flat groove in the actuator shaft and tighten the screw. If there are no set screws, you may skip directions regarding the set screws.

.. image:: https://wiki.analog.com/_media/trolley_mounting_bracket_6.jpg
   :width: 546px

Now we need to line up the second set screw to the motor shaft’s groove.

Without inserting the motor shaft into the coupler yet, align the motor so that the wires stream towards the other side of the rail. This will help with wiring later on.

Rotate the coupler/actuator shaft until the set screw in the smaller hole of the coupler lines up with the flat groove in the stepper motor shaft. Insert the lined-up stepper motor shaft into the coupler, but do not tighten the set screw yet.

Using four 6-32 X ¾” pan head screws and matching nuts, mount the stepper motor to the bracket.

.. image:: https://wiki.analog.com/_media/trolley_mounting_bracket_7.jpg
   :width: 347px

Making sure the set screws line up with the grooves, tighten the set screw.

.. image:: https://wiki.analog.com/_media/trolley_mounting_bracket_8.jpg
   :width: 326px

Rotate the coupler until you can see the larger cinch screws and tighten them. (If you don’t have set screws, then make sure the cinch screws are very tight to avoid slipping.)

.. image:: https://wiki.analog.com/_media/trolley_mounting_bracket_9.jpg
   :width: 305px

| 

Protoboard Soldering
--------------------

Now we will wire and solder the protoboard.

Locate the Level shifter board and Rpi protoboard. NOTE: On the protoboard, we will call the side with the solder balls the top/up and the side with the black pin holes the bottom/down. This will eventually be the orientation when we attach the protoboard to the Pi 0.

.. image:: https://wiki.analog.com/_media/trolley_protoboard_1.jpg
   :width: 305px

For reference, the finished version will look like the two images below. We will walk you through the steps to get there.

.. image:: https://wiki.analog.com/_media/trolley_protoboard_finished.jpg
   :width: 305px

Insert and solder two rows 6 header pins to the protoboard with the long end up in the locations shown below. Make sure you solder them so they point straight up. (If they are not already there, also solder the GPIO pins on the back.)

.. image:: https://wiki.analog.com/_media/trolley_protoboard_2.jpg
   :width: 305px

Assemble the protoboard as shown below. **Red lines indicate insulated wires on the top side and yellow lines indicate solder bridges in the bottom side.** **\*NOTE: Do not solder all the way to the row of holes on the edge of the board. Even though they are shown below as if they are soldered there, you should wait to insert pins and/or wires for the motor and limit control before soldering there.**\ \* Also: make sure any wires going between the two rows of 6 header pins are as flat as possible so that we can fit the level shifter on top of the pins.

|image8|\\

|image9|\\

|image10|\\

|image11|\\

|image12|\\

|image13|\\

.. image:: https://wiki.analog.com/_media/trolley_protoboard_gnd.jpg
   :width: 305px

Over the header pins, install and solder the level shifter with the IC chips down, LV1 on the top right and leaving a gap for the wires underneath.

.. image:: https://wiki.analog.com/_media/trolley_protoboard_level_shifter.jpg
   :width: 305px

Wiring and Settings
-------------------

Below are the sensor and motor driver connections. Solder 4 wires to the 4 motor driver ports shown below. The limit switch wires (3 each) should already be long enough to reach the protoboard, so you can solder those wires directly to the board with wire colors shown in the image.

.. image:: https://wiki.analog.com/_media/trolley_protoboard_wiring.jpg
   :alt: 400

Connect the four wires from the protoboard to the motor driver into the appropriate spots (DIR- to DIR-, etc.). See the image earlier on protoboard-motor driver connections.

.. image:: https://wiki.analog.com/_media/trolley_driver_wiring.jpg
   :alt: 400

.. image:: https://wiki.analog.com/_media/trolley_driver_wiring_2.jpg
   :alt: 400

Connect the V+ and GND to a 24V 3A Power Supply. DIP switches are set up as shown below. Flick 3 and 7 up and the rest down.

.. image:: https://wiki.analog.com/_media/trolley_driver_wiring_3.jpg
   :alt: 400

| 
| ====== Programming the Trolley ====== Software documentation

.. |image1| image:: https://wiki.analog.com/_media/trolley_gif_small.gif
.. |image2| image:: https://wiki.analog.com/_media/trolley_diagram_v2.jpg
.. |image3| image:: https://wiki.analog.com/_media/trolley_limit_switch_1.jpg
   :width: 200px
.. |image4| image:: https://wiki.analog.com/_media/trolley_limit_switch_2.jpg
   :width: 200px
.. |image5| image:: https://wiki.analog.com/_media/trolley_limit_switch_3.jpg
   :width: 200px
.. |image6| image:: https://wiki.analog.com/_media/trolley_mounting_bracket_2.jpg
   :width: 200px
.. |image7| image:: https://wiki.analog.com/_media/trolley_mounting_bracket_3.jpg
   :width: 300px
.. |image8| image:: https://wiki.analog.com/_media/trolley_protoboard_3.jpg
   :width: 305px
.. |image9| image:: https://wiki.analog.com/_media/trolley_protoboard_3_3v.jpg
   :width: 305px
.. |image10| image:: https://wiki.analog.com/_media/trolley_protoboard_5v.jpg
   :width: 305px
.. |image11| image:: https://wiki.analog.com/_media/trolley_protoboard_dir.jpg
   :width: 305px
.. |image12| image:: https://wiki.analog.com/_media/trolley_protoboard_pul.jpg
   :width: 305px
.. |image13| image:: https://wiki.analog.com/_media/trolley_protoboard_lim.jpg
   :width: 305px
