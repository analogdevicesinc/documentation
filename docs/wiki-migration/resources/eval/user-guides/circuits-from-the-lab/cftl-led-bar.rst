CftL-LED-Bar
============

Description
-----------

The :adi:`CftL-LED-Bar` is a boards that contains LED's with 3 different spectral outputs (627nm, 530nm and 470nm). Each of the three channels contains a string of four LED's in series able to handle currents of up to 1A.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cftl-led-bar/cftl-led-bar.jpg
   :align: center

**Recommended LEDs**

-  Lumileds Red LED- **LXM5-PD01**
-  Lumileds Green LED- **LXML-PM01-0080**
-  Lumileds Blue LED- **LXML-PB02**
-  `Lumileds Datasheet <https://www.lumileds.com/uploads/265/DS68-pdf>`__

Connectors
----------

Screw Terminals
~~~~~~~~~~~~~~~

Screw terminals P1, P5 and P9 are connectors for the anode and cathode for each of the red, green and blue channels of the :adi:`CftL-LED-BAR`. Pin 1 is the anode and is to be connected to the positive terminal of the source while pin 2 is the cathode and is to be connected to the negative terminal of the source.

3 Pin Headers
~~~~~~~~~~~~~

The 3 pin header is used to add LED's to series string of each channel. Placing a shunt on +XLEDN, where X is for the channel to be controlled and N refers to the LED number, adds the next LED on the string and placing the shunt on GND position terminates the string, connecting the last LED to the negative terminal.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cftl-led-bar/cftl-led-bar_silkscreen.jpg
   :align: center

LED Ratings
-----------

Red Channel
~~~~~~~~~~~

Each LED on this string has a typical forward voltage of 2.9V and tested with 500mA of current. Adding LED's to the string of LED's in series will result in a higher forward voltage. Please see below table for reference:

============ ================================
No. of LED's Minimum Forward Voltage Required
1            2.9V
2            5.8V
3            8.7V
4            11.6V
============ ================================

Green Channel
~~~~~~~~~~~~~

Each LED on this string has a typical forward voltage of 3.21V and tested with 500mA of current. Adding LED's to the string of LED's in series will result in a higher forward voltage. Please see below table for reference:

============ ================================
No. of LED's Minimum Forward Voltage Required
1            3.21V
2            6.42V
3            9.63V
4            12.84V
============ ================================

Blue Channel
~~~~~~~~~~~~

Each LED on this string has a typical forward voltage of 2.95V and tested with 500mA of current. Adding LED's to the string of LED's in series will result in a higher forward voltage. Please see below table for reference:

============ ================================
No. of LED's Minimum Forward Voltage Required
1            2.95V
2            5.90V
3            8.85V
4            11.80V
============ ================================

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download
   :class: download

   
   :adi:`CFTL-LED-BAR Design & Integration Files <media/en/reference-design-documentation/design-integration-files/cftl-led-bar-designsupport.zip>`
   
   -  Schematic
   -  PCB Layout
   -  Bill of Materials
   -  Allegro Project
   


Related Hardware
----------------

-  :doc:`CN0410 3-Channel LED Driver </wiki-migration/resources/eval/user-guides/eval-adicup3029/hardware/cn0410>`

Registration
------------

.. tip::

   Receive software update notifications, documentation updates, view the latest videos, and more when you register your hardware. `Register <https://form.analog.com/Form_Pages/FeedBack/CFTL-LED-BAR?&v=Rev A>`__ to receive all these great benefits and more!


// End of Document //
