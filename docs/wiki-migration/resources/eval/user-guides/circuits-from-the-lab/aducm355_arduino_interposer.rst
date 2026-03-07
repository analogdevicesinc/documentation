ADuCM355 Arduino Interposer
===========================

Description
-----------

The Arduino interface can be found on many microprocessor development platforms and are a great way to begin prototyping a design. The :adi:`EVAL-M355-ARDZ-INT` was developed to enable quick and easy connection of the ADuCM355 based sensor boards to the :adi:`EVAL-ADICUP3029` development board or any equivalent Arduino MCU controller boards. This allows for testing the functionality as well as the performance of the circuit using a controlled evaluation environment.

Product Overview
----------------

:adi:`ADuCM355` base Sensor Shield Board Interface Connectors:


|image1|

.. important::

   Check if connectors P1, P2, P3 and P4 were correctly installed. The notch found for all headers should be at the bottom left near the header number 14 of the silk screen.


Arduino Shield Board Interface Connectors:



|image2|

Pictured above is the EVAL-M355-ARDZ-INT interposer board which was developed to quickly and easily connect ADICUP3029 development board or any equivalent Arduino MCU controller boards.

EVAL-M355-ARDZ-INT Sensor Connector
-----------------------------------

The EVAL-M355-ARDZ-INT takes customized connectors to the ADuCM355 sensor surf boards, and allows up to four channels of sensor boards to be used with the EVAL-ADICUP3029 platform. Because the ADICUP3029 is an Arduino form factor compatible development board, many other equivalent Arduino form factor compatible development board can also be used simply by writing custom code. Below is the pinout of the custom connector of the sensor surf boards.

| |image3|
| ===== EVAL-M355-ARDZ-INT Power Rails ===== EVAL-M355-ARDZ-INT provides 3.3V power supply to an ADuCM355 base sensor shield board modules from ADICUP3029 development board or any equivalent Arduino MCU controller boards.

Switch Matrix
-------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/eval-aducm355-ardz-int/swithch_matrix_actual.png
   :align: center
   :width: 600px

Digital Communication Interfaces Supported
------------------------------------------

The EVAL-M355-ARDZ-INT can accommodate up to four ADuCM355 sensor surf board at the same time. The software and hardware support communications via:

-  SPI - Available on P7 and P9
-  I2C - Available on P7
-  UART - Available on P8

Arduino shield boards follow a standard pinout for the Arduino form factor compatible development boards.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/eval-aducm355-ardz-int/arduino_schematic_config.png
   :align: center
   :width: 600px

SWD/JTAG Connector
------------------

The debugger from the ADICuP3029 can be used and can be linked to the interposer board through the SWD_DEBUG (P10). The user can use a standard 10-pin ARM JTAG/SWD ribbon cable to connect to the ADICuP3029 debugger to the interposer board.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/eval-aducm355-ardz-int/aducm3029_to_daughter_board_swd.png
   :align: center
   :width: 400px

|image4| |image5|

| There is a way to cut the SWD traces on the ADICUP3029 board right at the break away section of the board. By cutting the trace for the SWD_DIO, SWD_CLK and SWD_RST located near P12. There are two(2) traces on the top of the board that must be cut using a knife, and one(1) trace found at the bottom of ADICUP3029 (the outter most trace), This allows customers to program both the ADICUP3029 and M355-INT boards without losing the ability to stream serial data back to the USB port. |image6|\ |image7|

Debug/Programming Channel Selector for ADuCM355 Sensor Surf Boards
------------------------------------------------------------------

The EVAL-M355-ARDZ-INT can accommodate up to four ADuCM355 sensor surf board and communicate to these boards at the same time through SPI communication protocol. Debugging and programming is being done independently for each channel by configuring the following switch matrix labeled SWD_DEBUG_CH_SW (S1) found on the silkscreen of the interposer board and with a corresponding LED indicator of which senor board is being accessed.

=============== ===
SWD_DEBUG_CH_SW LED
=============== ===
CH1             DS1
CH2             DS2
CH3             DS3
CH4             DS4
=============== ===

Digital Communication Protocol Selector
---------------------------------------

By default the ADuCM355 sensor surf boards come preloaded with SPI communication protocol back to the ADICUP3029.

Sensor shield board can also communicated either through UART or I2C depending on the firmware loaded on the sensor surf board and on the switch (S2) located on the EVAL-M355-ARDZ-INT.

.. important::

   It's important that the software and the hardware are set to the same digital communication protocol, so you receive and display data.


Hardware Setup Procedure
------------------------

If you are using the ADICUP3029 development board with the EVAL-M355-ARDZ-INT adaptor board, please use the following setup procedure:

-  Set the SWD_DEBUG_CH_SW(S1) of EVAL-M355-ARDZ-INT initially at CH1
-  Set the UART switch(S2) on the EVAL-ADICUP3029 to the "USB" position in order to stream data back to the serial terminal.
-  Place EVAL-M355-ARDZ-INT on top of the EVAL-ADICUP3029\

|image8|

-  Placed on the desired number of ADuCM355 sensor daughter board on top of the interposer board(up to 4).

|image9|

-  Plug in EVAL-ADICUP3029 into USB port of computer using the micro USB cable. (You may need to wait for the ADICUP3029 device drivers to install if this is the first time the device was plugged in.)

ADuCM355 Compatible Boards
--------------------------

Following is a table of current ADuCM355 base Sensor Shield Board offered by Analog Devices, and will connect to the EVAL-M355-ARDZ-INT adaptor board.

+--------------------------------------------+---------------+------------------------------------+
| Webpage                                    | Application   | EVAL-ADICUP3029 Software Available |
+============================================+===============+====================================+
| :adi:`cn0428`                              | Water Quality | Yes                                |
+--------------------------------------------+---------------+------------------------------------+
| :adi:`cn0429`                              | Gas Sensor    | Yes                                |
+--------------------------------------------+---------------+------------------------------------+

Software Available
------------------

:git-EVAL-ADICUP3029:`EVAL-ADICUP3029 Source Code for CN0428 and CN0429 <projects/ADuCM3029_demo_cn0428_cn0429>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download
   :class: download

   
   :adi:`EVAL-M355-ARDZ-INT Design & Integration Files <media/en/evaluation-documentation/evaluation-design-files/eval-m355-ardz-int-designsupport.zip>`
   
   -  Schematic
   -  PCB Layout
   -  Bill of Materials
   -  Allegro Project
   


Registration
------------

.. tip::

   Receive software update notifications, documentation updates, view the latest videos, and more when you register your hardware. `Register <https://form.analog.com/Form_Pages/FeedBack/EVAL-M355-ARDZ-INT?&v=Rev A>`_ to receive all these great benefits and more!


*End of Document*

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/eval-aducm355-ardz-int/pin_header.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/eval-aducm355-ardz-int/arduino_shield_board_actual.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/eval-aducm355-ardz-int/sensor_board_connector_header.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/eval-aducm355-ardz-int/jtag_swd_10_connector.png
   :width: 300px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/eval-aducm355-ardz-int/swd_debugger_connectors_actual_1.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/eval-aducm355-ardz-int/adicup3029_primary_cut.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/eval-aducm355-ardz-int/adicup3029_secondary_cut.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/eval-aducm355-ardz-int/shield_board_to_adicup_connections_actual.png
   :width: 600px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/eval-aducm355-ardz-int/sensor_shield_connections_actual.png
   :width: 600px
