ADIS16228 EVALUATION ON THE EVAL-ADIS
=====================================

OVERVIEW
--------

The :adi:`ADIS16228` iSensor® is a complete vibration sensing system that combines triaxial acceleration sensing with advanced time domain and frequency domain signal processing. Time domain signal processing includes a programmable decimation filter and selectable windowing function. The electrical connection typically only requires 5 I/O lines for synchronous data collection, as shown in the following figure:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-228-hookup.png
   :width: 400px

ADIS16228/PCBZ BREAKOUT BOARD
-----------------------------

For those who are on a tight timeline, connecting the :adi:`ADIS16228` to an embedded controller will provide the most flexibility in developing application firmware and will more closely reflect the final system design. The :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>` is the breakout board for the :adi:`ADIS16228` and may provide assistance in the process of hooking it up to an existing embedded processor system. For more information, click on the following link: :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>`

For tips on interfacing to the :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>` with a ribbon cable, check out the following Engineer Zone post:

:ez:`ADIS16228/PCBZ Breakout Board Cables (Engineer Zone FAQ) <mems/w/documents/4496/faq-adis16228-pcbz-breakout-board-cables>`

EVAL-ADIS: PC EVALUATION
------------------------

For those who would prefer to perform PC-based evaluation of the :adi:`ADIS16228`, before developing their own embedded system, the :adi:`EVAL-ADIS` is the appropriate system to use. The remainder of this Wiki site will focus on PC-based evaluation with the :adi:`EVAL-ADIS` system.

PART LIST FOR ORDERING
----------------------

:adi:`EVAL-ADIS`

:adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16210/products/EVAL-ADIS16228/eb.html>`

SYSTEM REQUIREMENTS
-------------------

Windows XP, Vista, 7

.NET Framework 3.5

NOTE: Newer versions of the .NET framework do not currently support the Vibration Evaluation Program.

PHYSICAL SETUP
--------------

The :adi:`ADIS16228/PCBZ <ADIS16228>` provides the :adi:`ADIS16228 <en/mems-sensors/mems-accelerometers/adis16228/products/product.html>` on a small printed circuit board (PCB) that simplifies the connection to an existing processor system. This PCB includes a silkscreen, for proper placement, and four mounting holes that have threads for M2 × 0.4 mm machine screws. The second set of mounting holes on the interface boards are in the four corners of the PCB and provide clearance for 4-40 machine screws. The third set of mounting holes provides a pattern that matches the EVAL-ADIS evaluation system, using M2 × 0.4mm × 4 mm machine screws. These boards are made of IS410 material and are 0.063 inches thick. J1 is a 16-pin connector, in a dual row, 2 mm geometry that enables simple connection to a 1 mm ribbon cable system. For example, use Molex P/N 87568-1663 for the mating connector and 3M P/N 3625/16 for the ribbon cable. For direct connection to the :adi:`EVAL-ADIS` evaluation system, use these parts to make a 16-pin cable or remove pins 13, 14, 15 and 16. The LEDs (D1 and D2) are not populated, but the pads are available to install to provide a visual representation of the DIO1 and DIO2 signals. The pads accommodate Chicago Miniature Lighting Part No. CMD28-21VRC/TR8/T1, which works well when resistors R1 and R2 are approximately 400 Ω (0603 pad sizes).The mating connector for the :adi:`ADIS16228 <en/mems-sensors/mems-accelerometers/adis16228/products/product.html>`, J2, is AVX P/N 04-6288-015-000-846. The picture below provides a close-up view of this connector, which clamps down on the flex cable to press its metal pads onto the metal pads inside the mating connector. The schematic is for the :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>` board.

NOTE: Some of the illustrations show the :adi:`ADIS16210/PCBZ <en/mems-sensors/mems-accelerometers/adis16210/products/EVAL-ADIS16210/eb.html>` instead of the :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>`. The package and setup process is identical for both of these products.

|image1| |image2| |image3| |image4|

NOTE: Do not plug the :adi:`EVAL-ADIS` into the USB cable at this stage of the setup. Wait until the software installation is complete.

Step #1 - Install ADIS16228CMLZ onto Interface Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Slide the :adi:`ADIS16228CMLZ <en/mems-sensors/mems-accelerometers/adis16228/products/product.html>` part into the mating J2 connector on the :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>`. Press the J2 clamp down onto the flex connector to complete the :adi:`ADIS16228CMLZ <en/mems-sensors/mems-accelerometers/adis16228/products/product.html>` part connection to the :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>`. Then secure the part using the M2 × 0.4mm × 4 mm machine screws provided with the :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>`. The following pictures provide a visual reference for correct connection but are actually :adi:`ADIS16228CMLZ <en/mems-sensors/mems-accelerometers/adis16228/products/product.html>` parts that share the same mechanical body.

|image5| |image6| |image7|

WARNING: Make sure that the connector cable going from J1 on the :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>` is properly aligned to the J1 connector on the :adi:`EVAL-ADIS`. The 16 pin cable is included with the :adi:`EVAL-ADIS`.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis-16pin-conn.png
   :width: 600px

Step #2 - Install ADIS16228/PCBZ onto EVAL-ADIS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mounting to the system frame is accomplished using 4 M2 x.4 x 6mm machine screws included with the :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>`. The mounting location holes are marked as an example in the picture below. Use the 4 holes to secure the :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>` to the :adi:`EVAL-ADIS`.

|image8| |image9| |image10| |image11|

Step #3 - Set Power Supply Level
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following picture shows JP1 in the **+3.3V** position (factory-default). That is the correct JP1 jumper setting on the :adi:`EVAL-ADIS` required for the :adi:`ADIS16228CMLZ <en/mems-sensors/mems-accelerometers/adis16228/products/product.html>` operation.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis-3.3v.png
   :width: 400px

VIBRATION EVALUATION PROGRAM OVERVIEW
-------------------------------------

The following sections provide a general description of the functions available in the Vibration Evaluation Program. For a set of :adi:`ADIS16288 <ADIS16228>`-specific instructions, please jump down to the section.

PROGRAM DOWNLOAD
----------------

.. include:: vibrationevaluationprogram.rst

USB DRIVER INSTALLATION
-----------------------

.. include:: vibrationevaluationprogram.rst

LAUNCH SOFTWARE
---------------

.. include:: vibrationevaluationprogram.rst

:doc:`Click here for an overview of Main Screen Features </wiki-migration/resources/eval/user-guides/inertial-mems/imu/vibrationevaluationprogram>`

ADIS16228 FUNCTION TUTORIALS
----------------------------

This section provides specific, "how-to" steps for exercising the many functions and user-configurable parameters available in the :adi:`ADIS16228`.

Fastest Path to Data
~~~~~~~~~~~~~~~~~~~~

For starters, here the quickest and easiest way to get a response from the :adi:`ADIS16228` is through the **Main Screen**, using the **Manual FFT** data collection mode.

After selecting the :adi:`ADIS16228` as the **Device** in the **Main Screen**, click on the **Start** button to trigger a set of FFT results on each axis.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_228_mainscreen_quickplot.png
   :width: 600px

Generating and Displaying Spectral Results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Vibration Evaluation Program provides a large area for displaying both time and frequency domain data from the :adi:`ADIS16228`

.. include:: vibrationevaluationprogram.rst

.. include:: vibrationevaluationprogram.rst

MANUAL FFT MODE
---------------

When using **Manual FFT** mode, the :adi:`ADIS16228` will collect and analyze data when prompted through a software or hardware "start" command. The **Start** button in the **Main Screen** causes the Vibration Evaluation Program (VEP) to send a software "start" command (set GLOB_CMD[11] = 1) to the :adi:`ADIS16228`. Through the **REC_CTRL** and **AVG_CNT** registers, the :adi:`ADIS16228` can support data record production on four different sample rates: SR0, SR1, SR2 and SR3. **REC_CTRL[11:8]]** provides on/off bits for each of these sample rates, while each nibble in the **AVG_CNT** provides a control entry for configuring these sample rates. In **Manual FFT** mode, each "trigger" will cause data production at one of the enabled rates, start with the lowest "" value (SRx), incrementing with each trigger/data production event.

Example #1 - Manual Mode FFT, One Sample Rate Example #2 - Manual Mode FFT, Four sample Rates

Data Capture
------------

Click on the following file links for examples on how to use the Data Capture function.

`ADIS16228 Data Capture Tutorial <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_adis16228_datacaptureexample.pdf>`_

Coming soon = Example with Alarms

VIBRATION EVALUATION PROGRAM TUTORIALS
--------------------------------------

Manual FFT Mode, Single Sample Rate

Manual FFT Mode, Single Sample Rate, with Alarms

Manual FFT Mode, Single Sample Rate, with Alarms, with Data Capture

Manual FFT Mode, Four Sample Rate Scan

Manual FFT Mode, Four Sample Rate Scan, with Alarms

Manual FFT Mode, Four Sample Rate Scan, with Alarms, with Data Capture

Periodic FFT Mode, Single Sample Rate

Periodic FFT Mode, Single Sample Rate, with Alarms

Periodic FFT Mode, Single Sample Rate, with Alarms, with Data Capture

Periodic FFT Mode, Four Sample Rate Scan

Periodic FFT Mode, Four Sample Rate Scan, with Alarms

Periodic FFT Mode, Four Sample Rate Scan, with Alarms, with Data Capture

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228pcbz-mnt.png
   :width: 300px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228-part-dimensions.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/210-mating-connector.png
   :width: 300px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228pcbz-schematic.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228-pcbz-parts.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/210-pcbz-j2-slide1.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/210-pcbz-j2-slide2.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis-210mnt-holes.png
   :width: 500px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/210-eval-adis-unplugged-conn.png
   :width: 500px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/210-mounted-to-eval-adis.png
   :width: 500px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/210-on-eval-adis-closeup.png
   :width: 500px
