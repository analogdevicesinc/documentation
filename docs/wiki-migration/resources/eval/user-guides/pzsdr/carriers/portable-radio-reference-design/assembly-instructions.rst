Portable Radio Reference Design - Assembly Instructions
=======================================================

These are the assembly instructions for the radio.

Stage 1 - Partial Assembly
--------------------------

Belly Plate
~~~~~~~~~~~

OLED Installation
^^^^^^^^^^^^^^^^^

-  Cut a strip of electric tape to place over the exposed vias found on the OLED PCB.

   -


   |image1|

-  Place the OLED into the rectangular opening.
-  Place 4 pcs of M2.5 X 4mm screws through the belly plate and OLED.

   -  Apply loctite.

-  Attach 4 pcs of M2.5 nuts and tighten.

   -  Cut off the ends of the screw if it extends beyond the nut.

-  Insert 1x `20 Position FMC Cable <https://www.digikey.com/WM11498-ND>`__ into OLED connector, with the exposed copper of the cable, facing away from the PCB.
-  Close the black bracket to secure the cable.
-  Apply some hot glue to the connector and part of the cable so it cannot be accidentally removed.

   -  Be careful here... if you have to remove this glue for any reason, you have to be gentle so as not to damage the OLED connector. It happens... I've done it...

-  Bend the cable backwards so it sticks out past the end of the belly plate.

   -


   |image2|

Nav Switch Installation
^^^^^^^^^^^^^^^^^^^^^^^

::

     * Place 4 pcs of M2.5 X 8mm screws through the belly plate.
       * Apply loctite 242.
     * Place 4 pcs of [[https://www.digikey.com/908-135-ND|908-135]] onto the screws, to act as spacers.
     * Place the Nav Switch PCB into the circular opening, with the connector closer to the middle of the belly plate.
     * Attach 4 pcs of M2.5 nuts and tighten
       * {{:resources:eval:user-guides:pzsdr:carriers:packrf:nav_close.jpg?400|}}
       * {{:resources:eval:user-guides:pzsdr:carriers:packrf:nav_switch.jpg?400|}}
     * Insert the ribbon cable into the connector on the Nav Switch so the ribbon cable extends towards the battery.
     * Now bend the cable towards the red line and pull it out to the left side.
     * Apply some hot glue to the connector and a fraction of the cable to secure everything.
       * There is a clearance constraint between this cable header and a component on the bottom of the PCB.  As a result, any glue applied must be restricted to below the top of the cable header, when it is plugged into the Nav Switch PCB.
       * {{ :resources:eval:user-guides:pzsdr:carriers:adrv1cc-box:belly_plate_with_battery_on_side.jpg?600 |}}
   * [[https://www.batteryspace.com/Custom-Polymer-Li-Ion-battery-3.7V-3200mAh-11.8-Wh-with-Thermistor.aspx|Battery CU-J479-V6: Molex 51065-0300]] Installation.
     * Clean the area between the two PCB's of dust or debris with a dry cloth.
     * Cut a 1-inch to 1.25-inch piece of double sided tape.  Peel off the cover and place the tape firmly between the PCBs.
     * Place the battery firmly onto the tape, with the yellow and white labels facing away from the belly plate.
       * {{ :resources:eval:user-guides:pzsdr:carriers:adrv1cc-box:belly_plate_inside.jpg?600 |}}
       * This image doesn't have the ribbon cable oriented properly (pull it out to the right, not the left).

Preparing the ADRV936x PCB
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `Heatsink <https://www.digikey.com/345-1146-ND>`__ Installation.

   -  Apply a circle of thermal grease to the protruding portion of the Xilinx FPGA.
   -  Spread the paste around.

      -


      |Initial Placement of Thermal Grease, Spreading of Grease.|

   -  Carefully place the heat sink making sure the plastic frame snaps into place.

      -  Be careful of C108. The plastic of the heat sink frame can catch on this component and possibly damage it if too much force is applied.

         -


         |image3|

         -

         |image4|

-  Boot Switch Configuration

   -  We want the PCB to boot using the micro SD card connector found on the carrier board.
   -  Using a pair of tweezers or small screw driver, move the switch 'S1' into the 'SDC' position. There is text located on either side of the switch to aide in selecting the correct orientation.

      -


      |image5|

Connecting the PCB's
~~~~~~~~~~~~~~~~~~~~

-  Line up the ADRV936x PCB connectors with those found on the carrier card.

   -  The boards will only mate in one orientation so rotate the PCB by 180 degrees if it does not fit.
   -  Do not force the connection. If properly aligned, little force is required to secure the PCB.

      -


      |image6|

   -  The image below shows the cards before being pressed together. Notice the gaps at the edges of the connectors.

      -


      |image7|

   -  The following image shows the cards properly mated.

      -


      |image8|

   -  Make sure to press all four corners to ensure a solid connection.

Connecting the RF cables
~~~~~~~~~~~~~~~~~~~~~~~~

-  Connecting 12 U.FL to SMA cables to the pair of PCB's and face plate of the box is a challenging but critical step. Take care to make the correct connections, and to route the cables carefully and gently.

   -  Fasten all the cables to the face plate THEN connect them to the PCB's. Make sure you hold the connector in place when you tighten the nut so you don't damage the face plate.
   -  This is a bit of a tedious process. Each cable connects to a specific connector on the PCB. I recommend firmly connecting one cable before moving on to the next.
   -  Be sure to make the correct connections otherwise, dis-assembling the unit later will frustrate you.

      -


      |image9|

   -  All TX cables go through the hole in the PCB closest to them.

      -


      |image10|

   -  None of the RX cables go through the PCB holes.
   -  GPS cables go through both holes.

Securing the RF Cables
~~~~~~~~~~~~~~~~~~~~~~

-  The connections of the U.FL connectors are delicate. Too much movement by the wires, or heavy hands by the assembler can cause permanent damage. As a result, a piece of plastic was designed (3D printed) to hold all the connectors and cables in place.

   -  Make sure each U.FL connector is perpendicular to the edge of the board. It must be oriented correctly or the brace will not slide into place properly.
   -  Gently place the brace down on top of the cables and PCB making sure to align the holes of the brace with the holes of the PCB.

      -  3D Model of the bottom of the cable brace showing detailed design for holding the U.FL connector in place.

         -


         |image11|

      -  Picture of the bottom of the cable brace.

         -


         |image12|

      -  Cable brace fitted on the PCB

         -


         |image13|

      -  cable holder 3D file.

         -  `u.fl_cable_holder.zip <https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/u.fl_cable_holder.zip>`__

Securing the PCB's
~~~~~~~~~~~~~~~~~~

-  Place 4x `5mm nylon spacers <https://www.digikey.com/R40-6710594>`__ between the PCB's.

   -  Align the spacers with the corner holes of the SOM PCB.

-  Insert 2x `#6-32 metal screws <https://www.digikey.com/PMS 632 0075 PH>`__ on the cable brace side.

   -  Apply loctite 242 to screw.
   -  Secure these 2 screws using `metal hex nuts <https://www.digikey.com/HNSS 632>`__.
   -  Don't over-tighten the nuts.

-  Insert 2x `#6-32 nylon screw <https://www.digikey.com/NY PMS 632 0050 PH>`__ in the other two mounting holes.

   -  Apply loctite 242 to screw.
   -  Secure this screw using a `nylon hex nut <https://www.digikey.com/H620-ND>`__.
   -  Don't over-tighten the nuts.

-  This is what the set up should look like at this point.

   -


   |image14|

Once these steps are complete, you can being the radio :doc:`Partial Assembly Test </wiki-migration/resources/eval/user-guides/pzsdr/carriers/packrf/testing>`.

Stage 2 - Full Assembly
-----------------------

Body Plate
~~~~~~~~~~

-  IMU Assembly

   -  Connect IMU to adapter PCB.

      -  Be sure to properly align the header with the receptacle.

   -  Plug ribbon cable into adapter PCB.
   -  Insert Screws into the body plate.
   -  Place IMU into the screws, with the adapter PCB away from the case.
   -  Add loctite to the screws.
   -  Add nuts to the screws and tighten.

      -  Tighten the screws according to the :doc:`ADIS16460 instructions </wiki-migration/resources/eval/user-guides/inertial-mems/imu/adis16imu4-pcb>`. A torque wrench is required so as not to damage the unit.

         -


         |image15|

      -  Apply hot glue to connector.

Cutting a Slot for the JTAG Adapter Cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  The following procedure needs to be performed on only half of the boxes.
-  Using a table saw, cut a 1.25" opening down the second shelf.

   -  This allows JTAG Adapter cable to protrude from the case.
   -  The JTAG adapter cable (same PN as the IMU cable and Nav switch cable) will be added AFTER the PCB's are inserted into the case.

-


|image16|

Inserting the PCB's
~~~~~~~~~~~~~~~~~~~

-  Now to slide the PCB's into the case. Lay both units on the table as below.

   -


   |image17|

-  Gently pull the face plate and cables above the PCB.

   -


   |image18|

-  All the cables must protrude past the edge of the PCB so they do not get stuck between the PCB and the case.

   -


   |image19|

-  There should be 4 empty rows on the side of the case. The PCB slotting into the 5th row from the bottom.

   -


   |image20|

-  Keep the cables and face plate from being caught between the side of the box and the PCB.

   -


   |image21|

-  The FPGA is intended to make contact with the metal case. Be careful when inserting the PCB's, you might have to flex the case slightly for the FPGA to fit.

   -


   |image22|

-  Make sure none of the U.FL to SMA cables are caught between the plastic and the IMU adapter PCB. This can cause damage to the cables and seriously impact the RF performance.

   -


   |image23|

-  Now, using a pair of tweezers, connect the JTAG Adapter Cable so it protrudes from the opening cut into the box previously.

   -  Apply hot glue to the cable so it does not come loose.

Inserting the Belly Plate
~~~~~~~~~~~~~~~~~~~~~~~~~

-  Flip the unit over so the flat surface is down. The belly plate slides into the outer most slot as seen below.

   -


   |image24|

-  Keep the OLED cable, battery cable and navigation switch cable from catching on anything. If the cables catch on something and are pulled too hard... they can break or they can break things off.

   -  Sometimes the battery needs to be pressed towards the belly plate so it fits just right.
   -  A small screwdriver, tweezers or dentist like tool will come in handy for manipulating the cables.
   -

   |image25|

-  Make sure the OLED connector found on the carrier card is open. The plastic frame should be pulled gently AWAY from the connector itself.

   -


   |image26|

-  From here the cable should be inserted into the connector, and the black plastic closed so as to secure the cable

   -


   |image27|

-  Add some hot glue to the connector and the cable so any force is applied to the glue and not the connector itself.
-  Connect the battery cable to the battery plug.

   -


   |image28|

-  Slide the belly plate so it is flush with either end of the box.

Connecting the IMU
~~~~~~~~~~~~~~~~~~

-  Using tweezers, pliers or other tool... grab the IMU cable and gently push it into the connector.

   -


   |image29|

-  Once the connector is firmly in place, use the hot glue gun to apply glue to the cable and connector so it cannot be disconnected unintentionally. This doesn't take a lot of glue.

   -


   |image30|

-  Let the glue dry for a minute.

Face Plate
~~~~~~~~~~

-  Make sure the button is facing the same direction as the beveled screw holes on the face plate

   -


   |image31|

-  Add hex nut and tighten slightly.
-  Add the male pin header to the Power Switch Adapter PCB, protruding TOWARD the face plate.

   -  Solder the pins to the PCB.

-  Add the Power Switch Adapter PCB to the power switch, as seen below.
-  Solder the four pins.

   -


   |image32|

-  Attach the Power Switch Cable to the header (orientation to follow the picture above).
-  We need the Power Switch Adapter PCB to be parallel to the bottom of the face plate.
-  We need the hex nut to be parallel to the bottom of the face plate.

   -  These can both be tricky tasks but the end result is the P.S.A PCB, the face plate bottom edge, and the hex nut all being parallel.
   -  This is also results in the hex nut being tightened and some loctite applied.

-  Add hot glue to the connector on the Adapter PCB so the cable cannot be disconnected.
-  Let the glue dry for a minute.

Connecting the Power Switch and Navigation Switch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Slide the belly plate away, so there is access to the Power Switch Connector (P9) and Navigation Switch Connector (P11).

   -


   |image33|

-  Connect the power switch cable to P9.

   -  Let the cable hang to the side.

-  Apply some hot glue to the connector so it cannot be easily removed.

   -  Make sure no glue goes outside the white line in the silkscreen, this will make the PCB difficult to slide in and out.

-  Connect the navigation cable to P11.
-  Slide the case back to its starting position.
-  Apply some hot glue to the connector so it cannot be easily removed.

Adding the plastic frames
~~~~~~~~~~~~~~~~~~~~~~~~~

-  Be careful when placing the black plastic frame over the faceplates. It requires a little maneuvering but can be done with placing any tension on the cables.
-  The first step is to position the plastic frame so one of the short sides of the face plate goes through the opening.

   -


   |image34|

-  The second step is to gently push the face plate through the plastic frame.

   -


   |image35|

-  The last step is to push the plastic frame flush to the case.

Securing the face plates
~~~~~~~~~~~~~~~~~~~~~~~~

-  SMA Face Plate

   -  Ensure the U.FL cables do not get pinched or are resting in any damaging condition.
   -  For example, make sure none of the U.FL cables are caught between the edge of the PCB and the face plate as you press the face plate flush to the end of the case.
   -

   |image36|

-  Insert screws and secure using a screwdriver (or power tool if you have one).

   -  Be careful when using power tools for screws and nuts. If you over tighten anything, you risk stripping the threads and damage.

-  Ethernet Face Plate

   -  Make sure the connectors fit properly into the holes. They should be flush and the face plate should not require force to align.

      -


      |image37|

   -  Insert screws and secure using a screwdriver (or power tool if you have one).

Adding Face Plate Labels
~~~~~~~~~~~~~~~~~~~~~~~~

-  Because the silkscreen was not included on the first set of boxes, two labels need to be added to the SMA's to match the text in the image below

   -


   |image38|

-  In future builds, the silkscreen will be etched with the correct labels and this will not be a necessary step

Once these steps are complete, you can being the radio :doc:`Full Assembly Test </wiki-migration/resources/eval/user-guides/pzsdr/carriers/packrf/testing>`.

PackRF - Assembly Instructions
==============================

-  Place one finished radio in each slot.

   -  Only one of the radios should have the JTAG adapter cable hanging out of the side.

-  Place one TPE-115GI POE injector in each slot.
-  Place 20 RF antennas in the slot.
-  The rest of the items are placed into the large open rectangle on the left. Some of the items should be folded and the air pressed out of the plastic so everything fits.

   -  2x Micro SD card's
   -  2x USB OTG Cable
   -  2x GPS Antenna
   -  2x Ethernet Cable
   -  2x Car Adapter
   -  2x DC Wallwart
   -  2x Webcam (De-boxed)
   -  1x JTAG Adapter
   -  2x USB Cables

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/oled_with_tape.jpg
   :width: 300px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/oled_connected_to_belly_plate.jpg
   :width: 600px
.. |Initial Placement of Thermal Grease, Spreading of Grease.| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/adrv1cc-box/grease_fpga.jpg
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/adrv1cc-box/c108.jpg
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/heatsink_image.jpg
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/microsd_card_position.jpg
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/aligning_the_cards.jpg
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/card_aligned_not_connected.jpg
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/card_aligned_connected.jpg
   :width: 600px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/adrv1cc-box/u.fl_cables_connected_to_face_plate.jpg
   :width: 600px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/adrv1cc-box/feeding_tx_cables_through_holes_2_.jpg
   :width: 600px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/cable_brace_-_bottom.png
   :width: 600px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/cable_brace_final.jpg
   :width: 600px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/secure_rf_cable.jpg
   :width: 600px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/som_carrier.jpg
   :width: 600px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/adrv1cc-box/case_and_imu.jpg
   :width: 600px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/portable-radio-reference-design/case_saw_cut_for_jtag.jpg
   :width: 600px
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/inserting_pcb_s_1.jpg
   :width: 600px
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/inserting_pcb_s_2.jpg
   :width: 600px
.. |image19| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/inserting_pcb_s_3.jpg
   :width: 600px
.. |image20| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/shelf_position.jpg
   :width: 400px
.. |image21| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/inserting_pcb_s_4.jpg
   :width: 600px
.. |image22| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/inserting_pcb_s_5.jpg
   :width: 600px
.. |image23| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/inserting_pcb_s_6.jpg
   :width: 600px
.. |image24| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/inserting_belly_plate_1.jpg
   :width: 600px
.. |image25| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/handy_tools.jpg
   :width: 600px
.. |image26| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/oled_connector_open.jpg
   :width: 600px
.. |image27| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/oled_cable_secured.jpg
   :width: 600px
.. |image28| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/battery_and_oled_connected_2.jpg
   :width: 600px
.. |image29| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/imu_cable_connected.jpg
   :width: 600px
.. |image30| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/glueing_imu.jpg
   :width: 600px
.. |image31| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/face_plate_with_power_switch.jpg
   :width: 600px
.. |image32| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/pcb_buton.jpg
   :width: 400px
.. |image33| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/connecting_power_switch_cable_and_navigation_switch_cable.jpg
   :width: 400px
.. |image34| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/first_step_in_applying_plastic_frame.jpg
   :width: 600px
.. |image35| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/second_step_in_applying_plastic_frame.jpg
   :width: 600px
.. |image36| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/closing_the_face_plate.jpg
   :width: 600px
.. |image37| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/ethernet_face_plate.jpg
   :width: 600px
.. |image38| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/portable-radio-reference-design/labels_for_face_plate.jpg
   :width: 400px
