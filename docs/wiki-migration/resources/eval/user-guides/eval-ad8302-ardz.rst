EVAL-AD8302-ARDZ
================

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/AD8302-top-clean.jpg
   :alt: EVAL-AD8302-ARDZ
   :width: 600px

| The :adi:`EVAL-AD8302-ARDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD8302-ARDZ.html>` shield illustrates the functionality of the :adi:`AD8302 <en/products/amplifiers/rf-power-detectors/log-detectors/ad8302.html>`, a **gain and phase detector** which operates for frequencies **up to 2.7 GHz**. The voltage outputs of the AD8302 are routed to the ANALOG IN connector of the Arduino base board. This allows the RF power detector’s output voltage to be easily digitized and processed by the Arduino base board’s integrated six-channel ADC.
| The power supply for the board comes from the Arduino base board through the POWER connector (5V). So there is **no need to connect an external power supply**.
| The EVAL-AD8302-ARDZ is designed to work as a shield for **EVAL-ADICUP3029** and **DC2026C**\ (also called **Linduino One**). For **EVAL-ADICUP3029**, PC software GUI and device development drivers are available.

Shield Specifications
---------------------

-  Input RF Frequency Range: DC to 2.7GHz
-  Input RF Power Range: -60dBm to 0dBm
-  Maximum RF Input Power (Abs Max Rating): 10dBm
-  Supply:

   -  Voltage: 5V
   -  Operates at around 35mA

-  Quiescent Current: 19mA to 25mA
-  Input signal characteristic:
-  Recommended Calibration:
-  Output Voltage Range:

   -  VMAG: ~30mV to ~1.8V
   -  VPHASE: ~30mV to ~1.8V
   -  VREF: ~1.72V to ~1.88V

-  Has power down interface

Functional Block Diagram
------------------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/functional_diagram.jpg
   :alt: Functional Block Diagram

Typical Hardware Setup for Measurement
--------------------------------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad8302-ardz-setup.png
   :alt: Operational Setup

Software GUI for EVAL-ADICUP3029
================================

Software Installation
---------------------

-  Set up **EVAL-ADICUP3029 serial driver** as in :doc:`1. Install mBed windows serial driver... </wiki-migration/resources/eval/user-guides/eval-adicup3029/tools/keil_iar_support>`
-  Download the software on the :adi:`product page <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad8302-ardz.html#>` or click :adi:`here <media/en/evaluation-boards-kits/evaluation-software/eval-ad8302-ardz-evaluation-software.zip>`.
   <WRAP>

.. important::

   If previously downloaded evaluation software cannot detect board, download the evaluation software again to get the software fix version.


</WRAP>

-  Extract the Software GUI.zip to your computer.
-  Connect the EVAL-ADICUP3029 board using micro USB cable
-  Set the **S2 switch to USB**.

|EVAL-ADICUP3029pic_selectUSB|

-  In the extracted files look for **power_detector-firmware.hex** then copy the hex file to **Computer>>DAPLINK** drive
   |\|DAPLINK_screencap|
   <WRAP>

.. important::

   After loading the hex file to the DAPLINK drive the window explorer must automatically close or else you need to load the hex file to the drive again.


</WRAP>

-  After the **windows explorer automatically closes**, reset the EVAL-ADICUP3029 board by pressing the S1 (reset) button on the board.
-  Go to extracted files and look for **power_detector.exe** file and double click to run the software. The Connection Window will open.

|APP_window|

Software Operation
------------------

Connection Window
~~~~~~~~~~~~~~~~~

-  Mount EVAL-AD8302-ARDZ to the EVAL-ADICUP3029 and connect EVAL-ADICUP3029 to computer as in `Typical Hardware Setup for Measurement <https://wiki.analog.com/>`__
-  Click the **refresh button** on Port Name to Identify the **port** where an EVAL-ADICUP3029 is installed
   |image1| <WRAP>

.. note::

   If there is more than one EVAL-ADICUP3029 installed, select the port where EVAL-ADICUP3029 and EVAL-AD8302-ARDZ connected


</WRAP>

-  Set Baudrate to 115200
-  Select Auto-detect on Shield type.
-  Click Connect. The Measurement Window should Open.

<WRAP>

.. important::

   Console Log must indicate **AD8302 shield detected with ADiCUP**. If previously downloaded evaluation software cannot connect, go back to `Software Installation <https://wiki.analog.com/>`__ step 2 and **download the evaluation software again** to get the software fix version.


</WRAP>

Measurement Window
~~~~~~~~~~~~~~~~~~

| |image2|
| The shield measures Gain and Phase Difference based on a 2-point calibrated linear response characterized for a specific frequency. By using default calibration coefficients, the 2-point linear response corresponds to the :adi:`datasheet specifications of AD8302 <media/en/technical-documentation/data-sheets/AD8302.pdf>`. By using the user calibration coefficients, the frequency dependent 2-point linear response corresponds to the calibration made by the user.
| <WRAP>

.. note::

   If calibration is skipped at some frequencies, the default calibration coefficients will be used (user calibration coefficients and default calibration coefficients are INITIALLY the same).


</WRAP>

| Related topic: `Calibration of EVAL-AD8302-ARDZ <https://wiki.analog.com/>`__

To skip Calibration and use Default Calibration Coefficients:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  **Check** the box to use **default** calibration coefficients
-  **Uncheck** to use **user** calibration coefficients

To make single measurement:
^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Enter the frequency of the input RF signal
-  Uncheck Continuous Measurement
-  Click Measure Button

| <WRAP>

.. important::

   Not entering the correct frequency may result to less accurate measurements.


</WRAP>

To continuously make measurements:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Enter the frequency of the input RF signal
-  Check Continuous Measurement
-  Click Measure Button
-  Click Stop to stop measuring at the last measurement

| <WRAP>

.. important::

   Not entering the correct frequency may result to less accurate measurements.


</WRAP>

To switch windows:
^^^^^^^^^^^^^^^^^^

Click **Connection** or **Calibration** to switch to respective window.

Calibration Window
~~~~~~~~~~~~~~~~~~

-  Gain Calibration

| |image3|

::

     * Select the frequency
       * Input to J1 an RF signal of-20dBm 
       * Input to J2 an RF signal of-40dBm 
       * Click **Measure**
       * Input to J1 an RF signal of-40dBm 
       * Input to J2 an RF signal of-20dBm 
       * Click **Measure**
       * Click **Calibrate**
   * Phase Calibration\\

| |image4|

-  Select frequency
-  Set the signal power of inputs to -30dBm
-  Set phase between inputs to be 45º
-  Click measure
-  Set phase between inputs to be 135º
-  Click measure
-  Click **Calibrate**

.. tip::

   User must be able to synchronize the phase of input signals perhaps, by using external devices/equipment, to do this calibration


.. tip::

   If desired frequency of calibration or measurement is not on the list, calibrate on the immediate higher frequency available and on the immediate lower frequency available. If desired frequency is higher/lower than the available frequency selection, calibrate only on the highest/lowest frequency selection


Calibration Methodology
=======================

Calibration can be implemented using 2, 3, or 4-point calibration techniques which can be used to approximate nearly linear response characteristics such as in AD8302. A typical characteristic of the AD8302 for magnitude difference of 1.9GHz input signals is shown in Figure 1. This is TPC4 from the AD8302 datasheet.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad8302-ardz-ad8302_datasheet_TPC4.png
   :alt: fig50
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1. AD8302 Characteristic Response to Magnitude Difference for 1.9GHz Signals


**Two-point calibration** is the simplest calibration technique. This models the magnitude transfer function of the AD8302 and ADC as a **single straight line**

::

   MAG = (CODE/SLOPE)+INTERCEPT

Where

MAG is the RF Power Magnitude being measured

CODE is the ADC code

SLOPE is the slope of the AD8302transfer function's linear model (unit is LSBs/dB)

INTERCEPT is the (extrapolated) input RF power level which would yield and ADC code of 0 (this is a theoretical value with a unit of dBm)

SLOPE and INTERCEPT are calculated and stored during the calibration process by applying two known RF power levels, MAG1 and MAG2 (these RF power levels should be within the linear input range of the AD8302) and measuring the corresponding ADC codes, CODE1 and CODE2. The equations for calculating SLOPE and INTERCEPT are as follows:

::

   SLOPE = (CODE1–CODE2)/(MAG1−MAG2)


   | 

::

   INTERCEPT = MAG1-(CODE1/SLOPE)

If there is some non-linearity in the transfer function of the RF detector, the number of calibration points can be increased to improve measurement accuracy. To implement **three-point calibration**, three known power levels are applied MAG1, MAG2 and MAG3 (MAG1 should be greater than MAG2 which should be greater than MAG3) and the corresponding ADC codes are noted (CODE1, CODE2, CODE3)

This results in two SLOPE values and two INTERCEPT values which are calculated using the equations

::

   SLOPE1 = (CODE1–CODE2)/(MAG1−MAG2)

|

| SLOPE2 = (CODE2–CODE3)/(MAG2−MAG3)
| INTERCEPT1 = MAG1-(CODE1/SLOPE1)
| INTERCEPT2 = MAG2-(CODE2/SLOPE2)

After calibration when measuring RF input power, the power is calculated using the appropriate equation

::

   MAG = (CODE/SLOPE1)+INTERCEPT1   (if CODE > CODE2)

   or

   MAG = (CODE/SLOPE2)+INTERCEPT2   (if CODE < CODE2)

To decide which equation and calibration coefficients to use, the CODE from the ADC should be compared to CODE2 (CODE2 is the demarcation point between the two calibration regions). This will indicate which region of the AD8302's transfer function the RF power magnitude is located. For example, if the ADC CODE is greater than CODE2, this will indicate that the input power is greater than MAG2. So SLOPE1 and INTERCEPT1 should be used to calculate the input power. Because of the need to identify the region in which the measured RF input power is located, the CODE2 value should also be stored after calibration along with the SLOPE1, SLOPE2, INTERCEPT1 AND INTERCEPT2.

This technique can be extended to four or more calibration points. This may improve measurement accuracy at the cost of more complex calibration.

Development on EVAL-ADICUP3029
==============================

Development packages are available for C and Python. Other development environments may be used but this development guided is focused on software development on CrossCore Embedded Studio (for C) and on Pycharm(for Python).

C Development Guide
-------------------

Installations
~~~~~~~~~~~~~

-  Download and install :adi:`CrossCore Embedded Studio (CCES) 2.8.1 <en/design-center/processors-and-dsp/evaluation-and-development-software/adswt-cces.html#relatedsoftware>`
-  Download and install `mBed windows serial driver <https://developer.mbed.org/handbook/Windows-serial-configuration>`__

.. note::

   Assumes a fresh installation of all required software


Setting Up CrossCore Embedded Studio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Install the following packs by following the :doc:`How to install or upgrade Packs for CCES </wiki-migration/resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide>` guide:

   -  **ARM.CMSIS.5.4.0**
   -  **AnalogDevices.ADuCM302x_DFP.3.1.2**

-  Switch back to **C/C++ window** |c-dev-window| and close CCES 2.8.1
-  Download `power_detector_sample_c_code_and_header_files.zip <https://wiki.analog.com/_media/resources/eval/user-guides/power_detector_sample_c_code_and_header_files.zip>`__ and unzip it.
-  Run the "AD8302 Sample C Code and Header Files.exe" and select "C:\\Users\\YourUsername\\cces\\2.8.1" as the destination folder. The ad8302 folder should appear in C:\\Users\\YourUsername\\cces\\2.8.1 .

|rfdet-c-unzip|

   |rfdet-c-folder-ad8302|
-  Launch CCES 2.8.1 and select workspace C:\\Users\\YourUsername\\cces\\2.8.1. If the ad8302 has been installed elsewhere, choose that location as workspace. Switch to **C/C++ window** if it's not the current window.

|rfdet-c-workspace|

   \* To open the unzipped folder in the workspace, click **File -> Open Projects from File System**. A new window will pop up and ask you to select the project or folder that you want to open. Select the proper directory then click **Finish**.

   |rfdet-c-import-ad8302|

| On the left side of the window, the structure of the loaded sample code should match the structure in the image shown below.
| |rfdet-c-proj-ad8302|

Development on CrossCore Embedded Studio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Setup Crosscore as in `Setting Up CrossCore Embedded Studio <https://wiki.analog.com/>`__
-  Connect your EVAL-ADICUP3029 and power up the RF power detector shield then click Build |rfdet-c-hammer|.

|rfdet-c-console-ad8302|

-  After it finishes building, click Debug and click Application with GDB and OpenOCD (Emulator). Copy the following Debug configurations on the new window that will appear then click the Debug button.
-  On the Debug window, click the Resume to run and display the results on the Console window.

Python Development Guide
------------------------

.. _installations-1:

Installations
~~~~~~~~~~~~~

Assumes a fresh installation of all required software

-  Download `python 3.7.0 <https://wiki.analog.com/http/www.python.org/downloads/release/python-370>`__ version. Choose the right version depending on operating system. For windows, choose `Windows x86-64 executable installer <http://www.python.org/downloads/release/python-370/>`__. (Do not run installer yet)
-  Run installer as Administrator. During installation, \**check **Add Python 3.7 to PATH** before clicking **Install Now**\ \*\*

|rfdet-py-path|

-  Install **pyserial**. For windows, enter **pip3.7 install pyserial** on command prompt.
-  Download and install `PyCharm <https://www.jetbrains.com/pycharm/download/#section=windows>`__ **community version**
-  Download and install `mBed windows serial driver <https://developer.mbed.org/handbook/Windows-serial-configuration>`__

Setting Up PyCharm
~~~~~~~~~~~~~~~~~~

-  Download `power_detector_python_code_example.zip <https://wiki.analog.com/_media/resources/eval/user-guides/power_detector_python_code_example.zip>`__ and unzip.
-  Install **Power Detector Python Code Example.exe**, the destination folder used is the “Scripts” directory where the python3.7 is located. For windows, the location path is similar to **C:\\Users\\MyUsername\\AppData\\Local\\Programs\\Python\\Python37\\Scripts**

|rfdet-py-scripts|

-  Launch PyCharm and set up PyCharm interpreter by clicking file>>settings>>Project>>Project Interpreter choose python 3.7 then click “Ok”.

Python Development
~~~~~~~~~~~~~~~~~~

-  Connect the EVAL-ADICUP3029 board using micro USB cable.
-  In the EVAL-ADICUP3029, set the S2 switch to USB.
-  Unzip **power detector development code-release.zip** from :adi:`evaluation software <media/en/evaluation-boards-kits/evaluation-software/eval-ad8302-ardz%20evaluation%20software.zip>`
-  Find and copy **power_detector-firmware.hex** to the DAPLINK directory. Wait for the window to exit automatically. Else, repeat the `Development on PyCharm <https://wiki.analog.com/>`__ guide.
-  Press S1 (reset) button on the EVAL-ADICUP3029 and mount the EVAL-AD8302-ARDZ to the EVAL-ADICUP3029
-  On pyCharm, go to File>>Open and browse for the `\\PycharmProjects\\example code <https://wiki.analog.com/>`__ directory.
-  Click Project Tab located at left side of IDE and go to **ad8302** folder and double click **ad8302-getShieldReadings.py**
-  Change the default Port number (“COM10”) in the example code. On your computer go to Control Panel>>Device Manager look for Ports (COM & LPT) find the port number of “mbed Serial Port”.
-  Right click on any point in the working space and click **Run ltc5596-getShieldReadings**

Hardware Reference Information
==============================

|

.. admonition:: Download
   :class: download

   | Downloadable files contain the hardware reference information of EVAL-AD8302-ARDZ:
   | `Schematic Diagram of EVAL-AD8302-ARDZ <https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad8302-ardz-sch.pdf>`__
   
   `Layout Design of EVAL-AD8302-ARDZ <https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad8302-ardz-layout.pdf>`__
   
   `Bill of Materials of EVAL-AD8302-ARDZ <https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad8302-ardz-bom.xlsx>`__
   
   `Archive of .art files of EVAL-AD8302-ARDZ <https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad8302-ardz-art.zip>`__
   


Help and Support
================

For any queries regarding the hardware and evaluation software, contact as at :ez:`EngineerZone <rf>`.

.. |EVAL-ADICUP3029pic_selectUSB| image:: https://wiki.analog.com/_media/resources/eval/user-guides/rfdet-adicup3029-usb.png
.. |\|DAPLINK_screencap| image:: /resources/eval/user-guides/rfdet-daplink.png
.. |APP_window| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad8302-ardz-connection.png
.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad8302-ardz-connection-refresh.png
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad8302-ardz-measurement.png
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad8302-ardz-calibrate_gain-steps.png
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad8302-ardz-calibrate_phase-steps.png
.. |c-dev-window| image:: https://wiki.analog.com/_media/resources/eval/user-guides/rfdet-c-dev-window.png
.. |rfdet-c-unzip| image:: https://wiki.analog.com/_media/resources/eval/user-guides/rfdet-c-unzip.png
.. |rfdet-c-folder-ad8302| image:: https://wiki.analog.com/_media/resources/eval/user-guides/rfdet-c-folder-ad8302.png
.. |rfdet-c-workspace| image:: https://wiki.analog.com/_media/resources/eval/user-guides/rfdet-c-workspace.png
.. |rfdet-c-import-ad8302| image:: https://wiki.analog.com/_media/resources/eval/user-guides/rfdet-c-import-ad8302.png
.. |rfdet-c-proj-ad8302| image:: https://wiki.analog.com/_media/resources/eval/user-guides/rfdet-c-proj-ad8302.png
.. |rfdet-c-hammer| image:: https://wiki.analog.com/_media/resources/eval/user-guides/rfdet-c-hammer.png
.. |rfdet-c-console-ad8302| image:: https://wiki.analog.com/_media/resources/eval/user-guides/rfdet-c-console-ad8302.png
.. |rfdet-py-path| image:: https://wiki.analog.com/_media/resources/eval/user-guides/rfdet-py-path.png
.. |rfdet-py-scripts| image:: https://wiki.analog.com/_media/resources/eval/user-guides/rfdet-py-scripts.png
