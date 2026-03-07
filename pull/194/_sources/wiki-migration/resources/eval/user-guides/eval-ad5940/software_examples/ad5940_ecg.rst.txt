AD5940_ECG
==========

This demo will use **EVAL-ADICUP3029** and **EVAL_AD5940BIOZ** boards to carry out ECG measurements. Note an ECG simulator is also required to provide the ECG signal. The AD5940 evaluation kit must never be connected to the human body.

Overview
--------

This example project is designed to carry out electrocardiograph (ECG) measurements. The EVAL-AD5940BIOZ evaluation board has both the AD5940 and also the AD8233 ECG front end devices. The AD8233 filters the ECG signal and is connected to the AD5940 which measures the output of the AD8233 through it's SAR ADC.

Measurement Requirements
------------------------

The following is a list of items required to carry out the measurement.

-  Hardware

   -  EVAL-ADICUP3029
   -  EVAL-AD5940BIOZ
   -  Mirco USB to USB cable
   -  PC or Laptop with a USB port
   -  Custom Cables connected to ECG simulator

-  Software

   -  AD5940_ECG Example Project (Git Lab)
   -  SensoPal
   -  Serial Terminal Program, Such as Putty or RealTerm
   -  IDE such as IAR or Keil

Setting up the Hardware
-----------------------

-  Set switch S2 to USB Arduino function in order to view data over UART. The UART baud rate is **230400**
-  Set S5 to Wall/USB to power the board from the USB cable\

|image1|

-  Place the **EVAL-AD5940BIOZ** on top of the **EVAL-ADICUP3029**.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/software_examples/eval-ad5940bioz_ecg.jpg
   :align: center
   :width: 600px

-  Connect the provided ECG cables to an ECG simulator as per above image.
-  There are a number of jumpers that can figure the AD8233 in different configuration. For optimum performance leave them in the default configuration. Optionally refer to the :adi:`AD8233 <media/en/technical-documentation/data-sheets/ad8233.pdf>` datasheet and the :doc:`AD5940 Bio-Electric Shield </wiki-migration/resources/eval/user-guides/eval-ad5940/hardware/eval-ad5940bioz>` board page for details
-  Plug in the micro USB cable into the (P10) USB port on the EVAL-ADICUP3029, and the other end into the PC or laptop.
-  The following table shows the jumper settins to configure the ECG measurement system

+------------------------+----------------+------------------------------------------------------------+
| Connector              | Jmpr Position. | Description                                                |
+========================+================+============================================================+
| JP5 (Default DNI)      | A              | Pull up resistor (R25) connected to electrode bias         |
+------------------------+----------------+------------------------------------------------------------+
|                        | B              | Pull down resistor (R25)connected electrode bias           |
+------------------------+----------------+------------------------------------------------------------+
| JP6 (Default DNI)      | A              | Pull up resistor (R42) connected to electrode bias         |
+------------------------+----------------+------------------------------------------------------------+
|                        | B              | Pull down resistor (R42)connected electrode bias           |
+------------------------+----------------+------------------------------------------------------------+
| JP7 (Bias Select)      | 3-1            | Electrode bias connected to REFOUTS                        |
+------------------------+----------------+------------------------------------------------------------+
|                        | 3-4            | Electrode bias connected RLD                               |
+------------------------+----------------+------------------------------------------------------------+
|                        | 3-5            | Electrode bias connected to VDD (Default)                  |
+------------------------+----------------+------------------------------------------------------------+
| P7 (AC/DC pin control) | 1-2            | ACDC connected to DVDD (ac leads off mode)(Default)        |
+------------------------+----------------+------------------------------------------------------------+
|                        | 2-3            | ACDC connected to DGND (dc leads off mode)                 |
+------------------------+----------------+------------------------------------------------------------+
| P10 (AD8233 Power)     | 1-2            | AD8233 supply connected to AVDD (Default)                  |
+------------------------+----------------+------------------------------------------------------------+
|                        | 2-3            | AD8233 supply connected to LDO_OUT)                        |
+------------------------+----------------+------------------------------------------------------------+
| P16                    | 1-2            | Pull up resistor R46 for ECG_P to electrode bias (Default) |
+------------------------+----------------+------------------------------------------------------------+
|                        | 2-3            | Pull down resistor R46 for ECG_P to GND                    |
+------------------------+----------------+------------------------------------------------------------+
| P17                    | 1-2            | Pull up resistor R23 for ECG_N to electrode bias (Default) |
+------------------------+----------------+------------------------------------------------------------+
|                        | 2-3            | Pull down resistor R23 for ECG_N to GND                    |
+------------------------+----------------+------------------------------------------------------------+

Obtaining the Source Code
-------------------------

The source code and include files for the project can be found on Git

.. admonition:: Download
   :class: download

   
   `AD5940 Source Code <https://github.com/analogdevicesinc/ad5940-examples>`_
   


Configuring the Software
------------------------

The SDK provides firmware to measure the ECG signal. However the firmware is configured to send the raw ADC results to a terminal program. For an ECG measurement SensorPal will configure the ECG measurement and graph the results. The following image shows the ECG results in SensoPal


|image2|

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/img_20170612_144023_hdr.jpg
   :width: 800px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/software_examples/sensorpal_ecg.png
   :width: 600px
