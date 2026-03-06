EVAL-ADL5902-ARDZ
=================

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ADL5902-top-clean.jpg
   :alt: EVAL-ADL5902-ARDZ
   :align: center
   :width: 600px

The :adi:`EVAL-ADL5902-ARDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADL5902-ARDZ.html#eb-overview>` shield illustrates the functionality of the :adi:`ADL5902 <en/products/rf-microwave/rf-power-detectors/rms-responding-power-detectors/adl5902.html>`\ **, a 50 MHz to 9 GHz 65 dB TruPwr™ RMS responding RF power detector**. The voltage outputs of the ADL5902 are routed to the **ANALOG IN** connector of the Arduino base board. This allows the RF power detector’s output voltage to be easily digitized and processed by the Arduino base board’s integrated six-channel ADC. The output of the ADL5902’s on-board temperature sensor is also routed to one of the ANALOG IN pins.

The **power supply** for the board comes from the Arduino base board through the POWER connector (5V). So while there is **no need to connect an external power supply**, the board can be powered by an external supply (6 Volt wall wart on **P3** or 6V connected to the **P1** screw terminals.

The EVAL-ADL5902-ARDZ is designed to work as a shield for **EVAL-ADICUP3029** and **DC2026C**\ (also called **Linduino One**). For **EVAL-ADICUP3029** , a **PC software GUI application** (`EVAL-ADICUP3029 <https://wiki.analog.com/>`__) is available. Using this, the user can make RF power measurements and also calibrate the device to decrease measurement error. **Device development drivers** for `EVAL-ADICUP3029 <https://wiki.analog.com/>`__ are also available, which the user may use to **develop their own code** for RF measurement, device calibration, and more.

Shield Specifications
=====================

::

   *Input Frequency Range: 50MHz to 9GHz
   *RF Input Range: 65dB (+3 dBm to -62 dBm)
   *Maximum RF Input Power (Abs Max Rating): 21dBm
   *Supply: 
   * 5V Internal from Arduino base board (short pin1 and pin2 of P4) 
   * 6V External (for operation with an external supply or operation without Arduino base board) 
     * 6V External supply (short pin1 and pin2 of P2; short pin2 and pin3 of P4)
     * 6V Wall wart supply (short pin2 and pin3 of P2; short pin2 and pin3 of P4)
   *Quiescent Current: < 100mA
   *Input signal characteristic: CW or modulated carriers with large crest factors (e.g. QAM, XCDMA, OFDM, LTE)
   *Recommended Calibration: 3-point
   *Output Voltage Range:
   * VOUT: ~0.175V to ~2.45V
   * VTEMP: 1.1V to 1.8V

Functional Block Diagram
------------------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adl5902-ardz-functional-diagram.png
   :alt: functionaldiagram

Setting Up the Hardware
=======================

Power Options Jumper Setting
----------------------------

Choose among the power option to Power up the EVAL-ADL5902-ARDZ by shorting the correct pins using the provided shorting jumper caps.

Option 1: 5V of EVAL-ADICUP3029 or Linduino One
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| |power-5v|

-  Connect **pin1 and pin2** of pin header **P4**.
-  Mount EVAL-ADL5902-ARDZ to EVAL-ADICUP3029 or Linduino One.

|

.. note::

   This works regardless of the connections on pin header P2


Option 2: 6V DC supply
~~~~~~~~~~~~~~~~~~~~~~

| |power-dc|
| \* Connect **pin2 and pin3** of pin header **P4**

-  Connect **pin1 and pin2** of pin header **P2**
-  Connect 6V to the EVAL-ADL5902-ARDZ via the **Screw terminal block**

.. note::

   
   | EVAL-ADL5902-ARDZ is already functional using this option, even without EVAL-ADICUP3029 or Linduino One


Option 3: 6V Wall wart
~~~~~~~~~~~~~~~~~~~~~~

| |power-wall|
| \* Connect **pin2 and pin3** of pin header **P4**

-  Connect **pin2 and pin3** of pin header **P2**
-  Connect 6V wall wart to the EVAL-ADL5902-ARDZ via the **DC Jack**

.. note::

   
   | EVAL-ADL5902-ARDZ is already functional using this option, even without EVAL-ADICUP3029 or Linduino One


Typical Hardware Setup for Measurement
======================================

| |typical setup|

Software GUI for EVAL-ADICUP3029
================================

Software Installation
---------------------

-  Set up **EVAL-ADICUP3029 serial driver** as in :doc:`1. Install mBed windows serial driver... </wiki-migration/resources/eval/user-guides/eval-adicup3029/tools/keil_iar_support>`
-  Download the software on the :adi:`product page <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad8302-ardz.html#>` or click :adi:`here <media/en/evaluation-boards-kits/evaluation-software/eval-ad8302-ardz%20evaluation%20software.zip>`.
-  Extract the Software GUI.zip to your computer.
-  Connect the EVAL-ADICUP3029 board using micro USB cable.
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

-  Mount EVAL-ADL5902-ARDZ to the EVAL-ADICUP3029 and connect EVAL-ADICUP3029 to computer as in `Typical Hardware Setup for Measurement <https://wiki.analog.com/>`__
-  Click the **refresh button** on Port Name to Identify the **port** where an EVAL-ADICUP3029 is installed
   |image1| <WRAP>

.. note::

   If there is more than one EVAL-ADICUP3029 installed, select the port where EVAL-ADICUP3029 and EVAL-ADL5902-ARDZ connected


</WRAP>

-  Set Baudrate to 115200
-  Select Auto-detect on Shield type.
-  Click Connect. The Measurement Window should Open.

<WRAP>

.. important::

   Console Log must indicate **ADL5902 shield detected with ADiCUP**


</WRAP>

Measurement Window
~~~~~~~~~~~~~~~~~~

| |image2|
| The EVAL-ADL5902-ARDZ shield converts the measured ADC code to RF input power in dBm using stored calibration coefficients. A 3-point calibration methodology is used. The software program includes default calibration coefficients that correspond to the default response of the ADL5902 across RF power level and frequency. :adi:`datasheet specifications of ADL5902 <media/en/technical-documentation/data-sheets/ADL5902.pdf>`. Because of part-to-part device variation, observed accuracy using the default calibration coefficients will be sub-optimal. By availing of the software program's 3-point calibration function, measurement accuracy can be increased.
| <WRAP>

.. note::

   If calibration is skipped at some frequencies, the default calibration coefficients will be used (user calibration coefficients and default calibration coefficients are INITIALLY the same).


</WRAP>

| Related topic: `Calibration of EVAL-ADL5902-ARDZ <https://wiki.analog.com/>`__

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

Click "Connection" or "Calibration" to switch to respective window.

Calibration Window
~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adl5902-ardz-calibrate.png
   :alt: APP_window

To calibrate at a specific frequency, take the following steps
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Select the frequency using the frequency pull-down menu
-  Input an RF signal of 0dBm at the selected frequency. Click the Measure button beside 0dBm.
-  Input an RF signal of -45dBm at the selected frequency. Click the Measure button beside -45dBm.
-  Input an RF signal of -60dBm at the selected frequency. Click the Measure button beside -60dBm.
-  Click the Calibrate button. Console Log will indicate "User calibration coefficient for (frequency used) is updated."

| <WRAP>

.. important::

   Follow steps exactly. User calibration coefficients will not update if the Calibrate Button is not clicked.


</WRAP>

|

.. tip::

   If you plan to operate at a frequency not on the list, make sure the calibrate at least on the adjacent upper and lower calibration frequencies (the software program will interpolate these data to ensure accuracy at the operating frequency. If the operating frequency is higher or lower than the available calibration frequencies, calibrate only on the highest or lowest calibration frequencies.


Calibration Methodology
=======================

Calibration can be implemented using 2, 3 or 4-point calibration techniques which are used to approximate the transfer function of the ADL5902. Because the response of the ADL5902 changes with frequency, it is necessary to calibrate across frequency. If you are operating at a frequency that is in between two calibration frequencies, the software program will perform a weighted interpolation of the two sets of calibration coefficients.

The typical Vout vs. Pin characteristic of ADL5902 at 2.14GHz input is shown below (Figure 50 from the ADL5902 datasheet).

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adl5902-ardz-adl5902-datasheet-fig50.png
   :alt: fig50
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1. ADL5902 Characteristic Response at 2.14GHz


**Two-point calibration** is the simplest calibration technique. This models the transfer function of the ADL5902 and ADC as a **single straight line**

::

   PIN = (CODE/SLOPE)+INTERCEPT

Where

PIN is the RF input power being measured

CODE is the ADC code

SLOPE is the slope of the ADL5902 transfer function's linear model (unit is LSBs/dB)

INTERCEPT is the (extrapolated) input RF power level which would yield and ADC code of 0 (this is a theoretical value with a unit of dBm)

SLOPE and INTERCEPT are calculated and stored during the calibration process by applying two known RF power levels, PIN1 and PIN2 (these RF power levels should be within the linear input range of the ADL5902) and measuring the corresponding ADC codes, CODE1 and CODE2. The equations for calculating SLOPE and INTERCEPT are as follows:

::

   SLOPE = (CODE1–CODE2)/(PIN1−PIN2)


   | 

::

   INTERCEPT = PIN1-(CODE1/SLOPE)

If there is some non-linearity in the transfer function of the RF detector, the number of calibration points can be increased to improve measurement accuracy. To implement **three-point calibration**, three known power levels are applied PIN1, PIN2 and PIN3 (PIN1 should be greater than PIN2 which should be greater than PIN3) and the corresponding ADC codes are noted (CODE1, CODE2, CODE3)

This results in two SLOPE values and two INTERCEPT values which are calculated using the equations

::

   SLOPE1 = (CODE1–CODE2)/(PIN1−PIN2)

|

| SLOPE2 = (CODE2–CODE3)/(PIN2−PIN3)
| INTERCEPT1 = PIN1-(CODE1/SLOPE1)
| INTERCEPT2 = PIN2-(CODE2/SLOPE2)

After calibration when measuring RF input power, the power is calculated using the appropriate equation

::

   PIN = (CODE/SLOPE1)+INTERCEPT1   (if CODE > CODE2)

   or

   PIN = (CODE/SLOPE2)+INTERCEPT2   (if CODE < CODE2)

To decide which equation and calibration coefficients to use, the CODE from the ADC should be compared to CODE2 (CODE2 is the demarcation point between the two calibration regions). This will indicate which region of the ADL5902's transfer function the RF input power is located. For example, if the ADC CODE is greater than CODE2, this will indicate that the input power is greater than PIN2. So SLOPE1 and INTERCEPT1 should be used to calculate the input power. Because of the need to identify the region in which the measured RF input power is located, the CODE2 value should also be stored after calibration along with the SLOPE1, SLOPE2, INTERCEPT1 AND INTERCEPT2.

This technique can be extended to four or more calibration points. This may improve measurement accuracy at the cost of more complex calibration.

Development on EVAL-ADICUP3029
==============================

Development drivers are available for **C** and **Python**. Other development environments may be used but this development guided is focused on software development on **CrossCore Embedded Studio** (for C) and on **Pycharm**\ (for Python).

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
-  Run the "ADL5902 Sample C Code and Header Files.exe" and select "C:\\Users\\YourUsername\\cces\\2.8.1" as the destination folder. The adl5902 folder should appear in C:\\Users\\YourUsername\\cces\\2.8.1 .

|rfdet-c-unzip|

   |rfdet-c-folder-adl5902|
-  Launch CCES 2.8.1 and select workspace C:\\Users\\YourUsername\\cces\\2.8.1. If the adl5902 has been installed elsewhere, choose that location as workspace. Switch to **C/C++ window** if it's not the current window.

|rfdet-c-workspace|

   \* To open the unzipped folder in the workspace, click **File -> Open Projects from File System**. A new window will pop up and ask you to select the project or folder that you want to open. Select the proper directory then click **Finish**.

   |rfdet-c-import-adl5902|

| On the left side of the window, the structure of the loaded sample code should match the structure in the image shown below.
| |rfdet-c-proj-adl5902|

Development on CrossCore Embedded Studio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Setup Crosscore as in `Setting Up CrossCore Embedded Studio <https://wiki.analog.com/>`__
-  Connect your EVAL-ADICUP3029 and power up the RF power detector shield then click Build |rfdet-c-hammer|.

|rfdet-c-console-adl5902|

-  After it finishes building, click Debug and click Application with GDB and OpenOCD (Emulator). Copy the following Debug configurations on the new window that will appear then click the Debug button.
-  On the Debug window, click the Resume to run and display the results on the Console window.

Python Development Guide
------------------------

.. _installations-1:

Installations
~~~~~~~~~~~~~

Assumes a fresh installation of all required software

-  Download `python 3.7.0 <https://wiki.analog.com/http/www.python.org/downloads/release/python-370>`__ version. Choose the right version depending on operating system. For windows, choose `Windows x86-64 executable installer <http://www.python.org/downloads/release/python-370/>`__. (Do not run installer yet)
-  Run installer as Administrator. During installation, **check "Add Python 3.7 to PATH" before clicking "Install Now"**

|rfdet-py-path|

-  Install **pyserial**. For windows, enter **pip3.7 install pyserial** on command prompt.
-  Download and install any python IDE (eg. `PyCharm <https://www.jetbrains.com/pycharm/download/#section=windows>`__ **community version**)
-  Download and install `mBed windows serial driver <https://developer.mbed.org/handbook/Windows-serial-configuration>`__

Setting Up Python Development Library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Download `power_detector_python_code_example.zip <https://wiki.analog.com/_media/resources/eval/user-guides/power_detector_python_code_example.zip>`__ and unzip.
-  Install **Power Detector Python Code Example.exe**, the destination folder used is the “Scripts” directory where the python3.7 is located. For windows, the location path is similar to **C:\\Users\\MyUsername\\AppData\\Local\\Programs\\Python\\Python37\\Scripts**

|rfdet-py-scripts|

-  Launch Python IDE and make sure to chose the python 3.7 as the interpreter.

Running Python Development Example Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Connect the EVAL-ADICUP3029 board using micro USB cable.
-  In the EVAL-ADICUP3029, set the S2 switch to USB.
-  Unzip **power detector development code-release.zip** from :adi:`evaluation software <media/en/evaluation-boards-kits/evaluation-software/eval-ad8302-ardz%20evaluation%20software.zip>`
-  Find and copy **power_detector-firmware.hex** to the DAPLINK directory. Wait for the window to exit automatically.
-  Press S1 (reset) button on the EVAL-ADICUP3029 and mount the EVAL-ADL5902-ARDZ to the EVAL-ADICUP3029
-  On Python IDE, go to File>>Open and browse for the `\\example code <https://wiki.analog.com/>`__ directory.
-  Click Project Tab located at left side of IDE and go to **adl5902** folder and double click **adl5902-getShieldReadings.py**
-  Change the default Port number (“COM10”) in the example code. On your computer go to Control Panel>>Device Manager look for Ports (COM & LPT) find the port number of “mbed Serial Port”.
-  Right click on any point in the working space and click **Run ltc5596-getShieldReadings**

Hardware Reference Information
==============================

|

.. admonition:: Download
   :class: download

   `EVAL-ADL5902-ARDZ Design Files <https://wiki.analog.com/_media/resources/eval/user-guides/eval-adl5902-ardz-rev0_design_files.zip>`__

   
   -  Schematic Diagram of EVAL-ADL5902-ARDZ
   -  Layout Design of EVAL-ADL5902-ARDZ
   -  Fab Files of EVAL-ADL5902-ARDZ
   -  Assembly Files of EVAL-ADL5902-ARDZ
   


Help and Support
================

For any queries regarding the hardware and evaluation software, contact us at :ez:`EngineerZone <rf>`.

.. |power-5v| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adl5902-ardz-power-5v.png
   :width: 300px
.. |power-dc| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adl5902-ardz-power-dc.png
   :width: 300px
.. |power-wall| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adl5902-ardz-power-wall.png
   :width: 300px
.. |typical setup| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adl5902-ardz-setup.png
.. |EVAL-ADICUP3029pic_selectUSB| image:: https://wiki.analog.com/_media/resources/eval/user-guides/rfdet-adicup3029-usb.png
.. |\|DAPLINK_screencap| image:: /resources/eval/user-guides/rfdet-daplink.png
.. |APP_window| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad8302-ardz-connection.png
.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad8302-ardz-connection-refresh.png
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adl5902-ardz-measurement.png
.. |c-dev-window| image:: https://wiki.analog.com/_media/resources/eval/user-guides/rfdet-c-dev-window.png
.. |rfdet-c-unzip| image:: https://wiki.analog.com/_media/resources/eval/user-guides/rfdet-c-unzip.png
.. |rfdet-c-folder-adl5902| image:: https://wiki.analog.com/_media/resources/eval/user-guides/rfdet-c-folder-adl5902.png
.. |rfdet-c-workspace| image:: https://wiki.analog.com/_media/resources/eval/user-guides/rfdet-c-workspace.png
.. |rfdet-c-import-adl5902| image:: https://wiki.analog.com/_media/resources/eval/user-guides/rfdet-c-import-adl5902.png
.. |rfdet-c-proj-adl5902| image:: https://wiki.analog.com/_media/resources/eval/user-guides/rfdet-c-proj-adl5902.png
.. |rfdet-c-hammer| image:: https://wiki.analog.com/_media/resources/eval/user-guides/rfdet-c-hammer.png
.. |rfdet-c-console-adl5902| image:: https://wiki.analog.com/_media/resources/eval/user-guides/rfdet-c-console-adl5902.png
.. |rfdet-py-path| image:: https://wiki.analog.com/_media/resources/eval/user-guides/rfdet-py-path.png
.. |rfdet-py-scripts| image:: https://wiki.analog.com/_media/resources/eval/user-guides/rfdet-py-scripts.png
