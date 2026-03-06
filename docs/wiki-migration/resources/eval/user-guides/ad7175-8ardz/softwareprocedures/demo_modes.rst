Demo Modes
==========

Hardware Link for Noise Demo Mode
---------------------------------

+-------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Link Number | Default Position | Description                                                                                                                                                                                                                                                                                                                                     |
+=============+==================+=================================================================================================================================================================================================================================================================================================================================================+
| LK1         | B                | Selects the voltage applied to the AVDD1 pin. Operates using the AVDD 5V supply (default). When inserted in **Position A**, sets the AVDD1 voltage to the 3.3V supply from the ADP150 (U6) regulator. Setting AVDD1 = 3.3V is not allowed when AVSS = -2.5V.                                                                                    |
+-------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK2         | B                | Selects the voltage applied to the AVDD2 pin. Operates using the AVDD 5V supply (default). When inserted in **Position A**, sets the AVDD2 voltage to the 3.3V supply from the ADP150 (U6) regulator. Setting AVDD2 = 3.3V is not allowed when AVSS = -2.5V.                                                                                    |
+-------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK3         | B                | Selects the external clock input or internal clock output (default). When inserted in **Position A**, selects the CRYSTAL OPTION.                                                                                                                                                                                                               |
+-------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK4         | Inserted         | Insert to connect REF- to AVSS.                                                                                                                                                                                                                                                                                                                 |
+-------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK5         | B                | Connects REF+ to 5V external reference (default). When inserted in **Position A**, REF+ is connected to 2.5V internal reference.                                                                                                                                                                                                                |
+-------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK6         | A                | Turns ON the :adi:`LTC3129 <en/products/LTC3129.html>` (U3) to supply 7V to the LDO linear regulators (default). When inserted in **Position B**, turns OFF the :adi:`LTC3129 <en/products/LTC3129.html>` (U3).                                                                                                                                 |
+-------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK7         | B                | Shifts the voltage of AVDD 5.5V to 7V when inserted in **Position A**. When inserted in **Position B**, AVDD 5.5V is set to 5.5V (default).                                                                                                                                                                                                     |
+-------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK8         | A                | Turns ON the :adi:`ADP7118 <en/products/ADP7118.html>` (U10) to supply for AVDD 5.5V. The AVDD 5.5V is supplied with 5.5V from ADP7118 regulator (default). When inserted in **Position B**, turns OFF the :adi:`ADP7118 <en/products/ADP7118.html>` (U10).                                                                                     |
+-------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK9         | A                | Turns ON the 5V LDO to supply for AVDD 5V. The AVDD 5V is supplied with 5V from :adi:`ADP7118 <en/products/ADP7118.html>` (U11) regulator (default). When inserted in **Position B**, turns OFF the :adi:`ADP7118 <en/products/ADP7118.html>` (U11).                                                                                            |
+-------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK10        | A                | Turns ON the 2.5V LDO to supply for AVDD 2.5V. The AVDD 2.5V is supplied with 2.5V from :adi:`LT1962 <en/products/LT1962.html>` (U4) regulator (default). When inserted in **Position B**, turns OFF the :adi:`LT1962 <en/products/LT1962.html>` (U4).                                                                                          |
+-------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK11        | A                | Turns ON the :adi:`LT1983 <en/products/LT1983.html>` (U2) to supply for the ADP7182 (U5) 2.5V linear regulator (default). When inserted in **Position B**, turns OFF the :adi:`LT1983 <en/products/LT1983.html>` (U2).                                                                                                                          |
+-------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK12        | A                | Turns ON the :adi:`ADP7182 <en/products/ADP7182.html>` (U5) to supply for -2.5V. The -2.5V is supplied with -2.5V from the ADP7182 regulator (default); AVSS can be connected to ground depending on S1. When inserted in **Position B**, turns OFF the :adi:`ADP7182 <en/products/ADP7182.html>` (U5).                                         |
+-------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK13        | A                | Turns ON the 3.3V LDO to supply for IOVDD 3.3V. The IOVDD 3.3V is supplied with 3.3V from :adi:`ADP150 <en/products/ADP150.html>` (U6) regulator (default). When inserted in **Position B**, turns OFF the :adi:`ADP150 <en/products/ADP150.html>` (U6).                                                                                        |
+-------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK14        | Inserted         | Insert LK14 when performing Noise Test.                                                                                                                                                                                                                                                                                                         |
+-------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK15        | B                | Set to **A**, connects REFOUT to VCM (default). Set to **B**, connects REFOUT to A0. **Remove** LK15 when using an external VCM from J15.                                                                                                                                                                                                       |
+-------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK16        | B                | Set to **A**, connects AIN0 to ADC Driver. Set to **B**, connects/directs AIN0 to ADC (default). **Remove** LK16 when connecting AIN0 to surfboard.                                                                                                                                                                                             |
+-------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK17        | B                | Set to **A**, connects AIN1 to ADC Driver. Set to **B**, connects/directs AIN1 to ADC (default). **Remove** LK17 when connecting AIN0 to surfboard.                                                                                                                                                                                             |
+-------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK18        | A                | Set to **A**, connects -VS to GND (default). Set to **B**, connects -VS to -2.5 V. **Remove** LK18 when using external supply.                                                                                                                                                                                                                  |
+-------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK19        | B                | Set to **A**, connects +VS to AVDD 5 V. Set to **B**, connects +VS to AVDD 5.5 V (default). **Remove** LK19 when using external supply.                                                                                                                                                                                                         |
+-------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK20        | Inserted         | When **inserted**, initiates power down for the :adi:`ADA4945 <en/products/ADA4945.html>`/:adi:`ADA4940 <en/products/ADA4940.html>`. **Remove** when using the ADC DRIVER. **Insert** LK20 when performing Noise Test or when Surfboard is connected.                                                                                           |
+-------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK21        | A                | Set to **A**, connects SCLK to standard Arduino connection (default). Set to **B** when using multiple boards; connects SCLK to alternative Arduino connection.                                                                                                                                                                                 |
+-------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK22        | A                | Set to **A**, connects DOUT to standard Arduino connection (default). Set to **B** when using multiple boards; connects DOUT to alternative Arduino connection.                                                                                                                                                                                 |
+-------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK23        | A                | Set to **A**, connects DIN to standard Arduino connection (default). Set to **B** when using multiple boards; connects DIN to alternative Arduino connection.                                                                                                                                                                                   |
+-------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LK24        | A                | Set to **A**, connects CS to standard Arduino connection (default). Otherwise, select different CS for stacking multiple boards.                                                                                                                                                                                                                |
+-------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Noise test Demo
---------------

-  **Warning:** The evaluation software and drivers must be installed before connecting the EVAL-AD7175-8ARDZ evaluation board and EVAL-SDP-CK1Z board to the USB port of the PC to ensure the PC correctly recognizes the evaluation system.

If you have not set up the EVAL-AD7175-8ARDZ and controller board previously please go to the :doc:`Quick Start Guide </wiki-migration/resources/eval/eval-ad7175-8ardz>`

If you have not set up/installed the ACE plugin before please go to :doc:`Installation Guide </wiki-migration/resources/eval/user-guides/eval-ad7175-8ardz/software>`

-  Double click the AD7175-8 Eval Board icon to open the AD7175-8 Eval Board view window. The demo wizard will be on the left, either as shown in the figure below (Label 1) or already expanded. Expand the wizard by clicking the arrow (Label 2).


|image1|

-  With the wizard expanded, select the noise test button (Label 3).
-  The settings required for the demo are displayed to be viewed prior to writing to the AD7175-8 (Label 4). Click apply (Label 5) to write these settings to the board.
-  The summary is then displayed once the write is complete (Label 1).

|image2|

-  From here navigate to the chip view by double-clicking the AD7175-8 chip (Label 2).
-  To make further changes to the configuration click on the dark blue block in the chip view (Label 1) or double click the memory map option (Label 2)
-  To begin capturing data double click the Analysis button (Label 3).

|image3|

-  To gather samples, change the Samples Count (Label 1) to the number of samples required, then click the Run Once button (Label 2) to acquire the samples from the ADC. The image below shows an example of the main window after running a noise test.\

|image4|

-  For more information on the Waveform window go to the software section :doc:`here </wiki-migration/resources/eval/user-guides/ad4130-8/softwareprocedures>`

Reading Samples from the ADC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The evaluation board is set up to use the external 5 V on-board reference (:adi:`ADR4550 <en/products/ADR4550.html>`). To read samples from the ADC, do the following:

-  The value in the Refin1(+/−) field on the Configuration tab is set to 5 V by default to use the external 5 V on-board reference (:adi:`ADR4550 <en/products/ADR4550.html>`). If a different reference is used to the AD7175-8, the Refin1(+/−) field should be updated accordingly. (The analysis results are based on the value set in this input field.)

   -  Information on the reference choice can be viewed in the :doc:`Reference Options Tab </wiki-migration/resources/eval/user-guides/eval-ad7175-8ardz/hardware_guide>`

-  When selecting Run Once, a batch of samples is read when clicking the button; the batch size is set by the value in the Samples field.

   -  When selecting Run Continuous, the software performs a continuous capture from the ADC by clicking the Run Once button. Click the Stop Capture button again to stop capturing data.

-  Use the navigation tools within each graph to control the cursor, zooming, and panning.

.. _reading-samples-from-the-adc-1:

Reading Samples from the ADC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Find the waveforms resulting from the gathered samples in the Analysis tab. The waveform graph shows each successive sample of the ADC output (input referred). The indicators beside this graph show the channels converting. The navigation tools allow you to control the cursor, zooming, and panning. You can also display the conversions as voltages or codes. Below the graph are parameters, such as peak-to-peak noise and rms noise, in the Results section for the current batch of samples. If there are several enabled analog input channels, you can select each enabled channel and the conversions through the analyzed channel using the Results Tab. To save the data into an Excel file, select the Export button from the Results Tab. A Save dialog box is displayed, prompting you to save the data to an appropriate folder location.

--------------

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130-8/softwareprocedures/ad4130_8_ace_noise_test.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130-8/softwareprocedures/ad4130_8_ace_noise_test_summary.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130-8/softwareprocedures/ad4130_8_ace_noise_test_chip_view.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130-8/softwareprocedures/ad4130_8_ace_noise_test_data.png
   :width: 600px
