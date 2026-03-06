DC1959B-A,B,C,D ACE Software User Guide
=======================================

Description
-----------

Demonstration circuit 1959B features the LTC6948, an Ultralow Noise and Spurious Fractional-N Synthesizer with Integrated VCO. There are four options of the DC1959B, one for each version of the LTC6948. Table 1 summarizes the available DC1959B options. The DC1959B provides 50Ω SMA connectors for the reference frequency input fREF (REF+IN) and the differential RF output (RF+ and RF–). A DC2026A USB serial controller board is used for SPI communication with the LTC6948, controlled by the ACE™ software and LTC6948 Plugin.


|image1|

.. note::

   Figure 1: DC1959B Board View and Connectors


+------------------+---------------+--------------------------+-------------------------+
| Assembly Version | Part Number   | VCO Frequency Range(GHz) | Output Divider Settings |
+==================+===============+==========================+=========================+
| DC1959B-A        | LTC6948IUFD-1 | 2.240 to 3.740           | Integers 1 through 6    |
+------------------+---------------+--------------------------+-------------------------+
| DC1959B-B        | LTC6948IUFD-2 | 3.080 to 4.910           | Integers 1 through 6    |
+------------------+---------------+--------------------------+-------------------------+
| DC1959B-C        | LTC6948IUFD-3 | 3.840 to 5.790           | Integers 1 through 6    |
+------------------+---------------+--------------------------+-------------------------+
| DC1959B-D        | LTC6948IUFD-4 | 4.200 to 6.390           | Integers 1 through 6    |
+------------------+---------------+--------------------------+-------------------------+

.. note::

   Table 1: DC1959B Options and Frequency Ranges


Getting Started
---------------

The DC1959B is easy to set up to evaluate the performance of the LTC6948. Follow the procedure below. The ACE Software and the DC2026A are required to control the DC1959B through a personal computer (PC).

DC2026A Linduino Board Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Refer to Figure 2. Set the JP3 jumper to the 3.3V (preferred) or 5V position. Connect the DC2026A to one of your computer’s USB ports with the included USB cable. The DC2026A has the ability to run Linduino code, refer to :adi:`Design Center <en/design-center/evaluation-hardware-and-software/linduino.html?doc=DC2609A.pdf>`.


|image2|

.. note::

   Figure 2: DC2026A Connector Location


ACE and Plugin Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can install the LTC6952 plug-in from the ACE start-up page. You can install ACE from :adi:`ACE Software Page <en/design-center/evaluation-hardware-and-software/ace-software.html>`

-  On the ACE start-up page locate and click the Plug-in Manager on the sidebar.
-  Select Available Packages from the panel second sidebar
-  Search for Board.LTC6952 and install plug-in

|image3|

.. note::

   Figure 3: ACE Plugin Search Screen


Evaluation Board Setup
~~~~~~~~~~~~~~~~~~~~~~

-  Connect a 100MHz reference frequency source to REF +IN (at J1) and signal analyzers to RF+ and/or RF– (at J5 and/or J4) using the SMA connectors (see Figure 1 and the Typical DC1959B Requirements and Characteristics table).
-  Choose the MUTE jumper setting:

   -  JP1: GND/3.3V – MUTE position. Select GND to mute the RF output, 3.3V to un-mute.

-  Connect the GND, 3.3V, and 5V banana jacks to a power supply and apply power (see Figure 1 and the Typical DC1959B Requirements and Characteristics table).
-  Connect the DC2026A to the DC1959B with the provided ribbon cable.
-  Run ACE application. Double click the LTC6948 icon that appears on the Attached Hardware tab when the DC2026A board is connected and attached to the board. If the icon does not appear, consider re-installing the LTC6948 plug-in or try refreshing Attached hardware icon.
-  Connection is automatically established with DC2026A. You can navigate to board and chip view.
-  Double Click the LTC6948 Board Icon and tab shown in Figure 5 appears.
-  Double click the LTC6948 icon that appears on the LTC6948 Board tab to open main control window shown in Figure 6.

|image4|

.. note::

   Figure 4: Attached Hardware Tab


   |image5|

.. note::

   Figure 5: LTC6948 Board Page


General Software Features
~~~~~~~~~~~~~~~~~~~~~~~~~

In chip view one can find various control features of LTC6948. One can read and control all registers which mentioned in the :adi:`LTC6948 datasheet <LTC6948>`. When plugin opens first time, all settings are modified in order to operate with 100 MHz reference and output is set to 907MHz. User can click on “Apply Changes” to upload pre-defined register to test board. When all modified register is uploaded to board, STAT LED on the board will illuminate. Register Hb00 can easily read by clicking “Check Status Register” button. Small Tick box will be filled if register bit value is high. Stat Pin output mask register value can be set visually to reflect which information will be carried to Stat Pin Output. The main controls are available in the high-level register map shown in Figure 7. To modify registers, perform the following steps:

-  Modify the registers as desired.
-  Click Apply Changes to load the modified settings to the device. This action loads the updated registers only

By clicking Proceed to Memory Map button or Memory Map Side-By-Side button, register values can be seen.


|image6|

.. note::

   Figure 6: Chip View of LTC6948 on ACE Software


Typical DC1959B Requirements and Characteristic
-----------------------------------------------

+-------------------+-----------+-------------------------------+------------------------------------------------------------------------------------------------------------------+
| Parameter         | Direction | Physical Location             | Details                                                                                                          |
+===================+===========+===============================+==================================================================================================================+
| 3.3V Power Supply | Input     | J6 Banana Jack                | Requires Low-Noise and Spur-Free 3.3V, 130mA                                                                     |
+-------------------+-----------+-------------------------------+------------------------------------------------------------------------------------------------------------------+
| 5V Power Supply   | Input     | J8 Banana Jack                | Requires Low-Noise and Spur-Free 5V, 33mA.                                                                       |
+-------------------+-----------+-------------------------------+------------------------------------------------------------------------------------------------------------------+
| GND               | Output    | J7 and J9 Banana Jack         | -                                                                                                                |
+-------------------+-----------+-------------------------------+------------------------------------------------------------------------------------------------------------------+
| RF+; RF–          | Output    | J3 and J4 SMA\*               | Frequency: 907MHz, Power: 0dBm, Frequency Range: Depends on the Version of the LTC6948 Device – Refer to Table 1 |
+-------------------+-----------+-------------------------------+------------------------------------------------------------------------------------------------------------------+
| REF+              | Input     | J1 SMA                        | Low-Noise 100MHz, 6dBm to 10dBm into 50Ω, See Note Below                                                         |
+-------------------+-----------+-------------------------------+------------------------------------------------------------------------------------------------------------------+
| Loop Bandwidth    | -         | Set By Loop Filter Components | Approximately 160kHz Depending on the DC1959B Version                                                            |
+-------------------+-----------+-------------------------------+------------------------------------------------------------------------------------------------------------------+

.. note::

   *Any unused RF Output must be powered down and terminated with 50Ω, or poor spurious performance may result


.. note::

   A low noise 100MHz reference frequency, such as the Wenzel 501-04516D OCXO, is recommended. If using a different frequency, make sure to update the Fref and R_DIV boxes Chip View tab in ACE so that Fpfd is still 50MHz. For example, if a 250MHz clock is used, Fref should be changed to 250MHz and R_DIV to 5. Ref BST and FILT under the Chip View tab in ACE might need to be changed if the reference frequency and/or power is different than what is recommended in the table above. More information can be found in the LTC6948 data sheet.


Troubleshooting
---------------

**If the red LED does not illuminate:**

-  Verify that you are able to communicate with the DC1959B. The bottom status line in ACE Plugin Status must be “GOOD”. If status is “Unavailable”, it means ACE cannot communicate with DC2026AA. You can check communication by verifying DC1959B and LTC6948 Plugin Communication. If status is “Unknown”, it means USB serial board is recognized and cannot communicate with DC1959B Board.
-  Verify that the 3.3V and 5V have the correct voltages on them and that the reference frequency is applied to the REF+IN SMA input.

If the red LED is on but you cannot detect an RF output, make sure jumper JP1 is at the 3.3V position.

**Verify DC1959B and LTC6948 Plugin Communication:** To verify communication with the DC1959B, go to start page or system view page and click the button shown in below.


|image7|

.. note::

   Figure 7: This button lights an LED on USB Serial Board to Verify Communication


LEDs on the Serial Interface Boards don’t light up, then perform the following steps:

-  Ensure the DC2026A is connected to PC
-  Disconnect and Reconnect DC2026A to PC
-  Ensure DC2026A is connected to DC1959B
-  Close ACE and restart
-  Verify the DC2026A has the DC2026AB Emulator sketch loaded by contacting the factory or following these steps.

   -  `Download QuikEval™ <http://ltspice.analog.com/software/ltcqev.exe>`__
   -  Run QuikEval (Linduino connected to the PC)

If QuikEval does not find a DC2026AB, reload the DC2026A Linduino sketch. To use the LTSketchbook refer to the :adi:`Linduino Design Center <en/design-center/evaluation-hardware-and-software/linduino.html?doc=DC2609A.pdf>` for instructions on how to start using Linduino.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/ltc6948boardview.png
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dc2026-connector-location.png
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ace-plugin-search-screen.png
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/board.ltc6948-plugin-attached-hardware-screen.png
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/ltc6948-boardview-on-ace.png
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/ltc6948-chipview-on-ace.png
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/ltc6948-verify-comm.png
