.. _eval-cn0588-ebz:

EVAL-CN0588-EBZ
===============

DC to 10 kHz MEMS-Based IEPE Vibration Sensor.

Overview
--------

The :adi:`CN0588` is a MEMS-based IEPE vibration sensor optimized
for condition-based monitoring (CbM) applications. This solution has a
constant current supply of 4mA and a DC voltage bias ranging from
around 8.75V to 14.75V.

.. figure:: eval-cn0588-ebz_top.jpg
   :width: 400px

.. figure:: cn0588_q_front.png
   :width: 400px

Since Piezoelectric sensors are predominantly used in CbM applications, IEPE
is the de facto standard in CbM vibration sensing ecosystem. The IEPE
interface, also commercially known as ICP, is a 2-wire protocol, signal and
ground. In this protocol a data logger supplies a constant current via the
signal line to the vibration sensor and the sensor modulates the voltage
according to the measured, typically between 10V to 30V. This reference
design enables a direct IEPE piezoelectric sensor replacement with benefits of
high bandwidth, temperature stability and ultralow noise MEMS accelerometers.
This allows customers to easily evaluate an IEPE MEMS accelerometer solution
for CbM applications on the same ICP piezoelectric sensor platform.

Features
~~~~~~~~~

- Mechanically enclosed and machine mountable
- IEPE interface to retrofit into existing machines
- Power and data over a single wire, power comes from host
- Has a frequency range from DC up to 10 kHz and response within ±3 dB
- Resonant frequency around 12.5 kHz

Applications
~~~~~~~~~~~~

- Predictive Maintenance
- Vibration Analysis
- Condition Monitoring
- Industrial Machinery Control

Block Diagram
~~~~~~~~~~~~~~

.. figure:: cn0588_block_diagram.png

Hardware Setup
--------------

Equipment Needed
~~~~~~~~~~~~~~~~

- EVAL-CN0588-EBZ
- Current Source (e.g., Keithley 6220), or an IEPE-compatible DAQ such as the
  :adi:`CN0582`, :adi:`CN0540`, :adi:`CN0579`
- Vibration Shaker (e.g., King Design 9363-ED-2F4K-5N)
- Signal Generator
- SMA Cable (10-32)
- BNC Cable

Setting up the Hardware
-----------------------

.. figure:: eval-cn0588-ebz_setup0.png

#. Mount the EVAL-CN0588-EBZ to the vibration shaker.
#. Connect the SMA cable to the EVAL-CN0588-EBZ.
#. Connect the other end of the SMA cable to the current source.
#. Set the output constant current to 4 mA, and controlled voltage to 26V.
#. Connect the BNC cable to the vibration shaker.
#. Connect the other end of the BNC cable to the signal generator (output).
#. Set the frequency settings to your requirement.
#. The voltage of the current source is the output. Without an external
   acceleration, the IEPE output should be around 12V.

The EVAL-CN0588-EBZ is ready for experiment.

Sample Measurements
-------------------

Using CN0588 with the CN0582 Quad-Channel IEPE DAQ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For applications requiring 4 channels, the CN0582 is the recommended IEPE
vibration measurement equipment to be paired with the CN0588. Follow below
procedure to set up the system for evaluation.

Equipment Needed
^^^^^^^^^^^^^^^^

- EVAL-CN0588-EBZ
- EVAL-CN0582-USBZ
- Host PC (Windows 10)

  * with installed `CN0582 Evaluation Software <http://swdownloads.analog.com/cse/cftl/CN0582/CN0582%20EVALUATION%20SOFTWARE%20INSTALLER.EXE>`__

- Vibration Shaker (e.g., King Design 9363-ED-2F4K-5N)
- Reference Sensor (PCBM352C67)
- Power Supply (19 V)
- USB Type-C Cable
- Two (2) SMA Cables
- BNC Cable

.. tip::
   This measurement demonstration uses the EVAL-CN0582-USBZ as IEPE-compatible
   vibration measurement equipment, and requires the CN0582 Evaluation Software
   to be installed.

For instructions on how to obtain and install the software, visit the
:dokuwiki:`CN0582 User Guide </resources/eval/user-guides/circuits-from-the-lab/cn0582>`.

.. figure:: eval-cn0588-ebz_setup3.png

#. Mount the EVAL-CN0588-EBZ to the vibration shaker.
#. Connect the EVAL-CN0582-USBZ to the vibration shaker using a BNC connector.
#. By using SMA connector, connect the Piezo reference sensor of the vibration
   shaker to Channel 0.
#. Attach another SMA connector from the EVAL-CN0588-EBZ going to Channel 1 of
   the EVAL-CN0582-USBZ.
#. Power up the EVAL-CN0582-USBZ by connecting the Type C end of the USB cable
   to the board and the other end to the host PC.

   .. tip::
      The RED and GREEN LED should light up, indicating proper power up.

#. Turn on the vibration shaker by plugging in the 19 V power supply.
#. Ready the shaker by clicking the tune button. Two (2) green LEDs must light
   up.

   .. figure:: eval-cn0588-ebz_hw_2.png

#. Download and install the
   `CN0582 Evaluation Software <http://swdownloads.analog.com/cse/cftl/CN0582/CN0582%20EVALUATION%20SOFTWARE%20INSTALLER.EXE>`__.

   .. tip::
      Only the GREEN LED should light up on the board during installation. This
      indicates successful firmware upload.

#. Follow the installation prompts until the main window of the GUI appears.

   .. figure:: eval-cn0588-ebz_setup4.png

#. On the GUI dashboard, navigate to the left and click **‘Vibration Testing’**
   to launch the window.

#. Toggle ON the current source in the Reference & DUT Sensor Setup Section (5).

   .. figure:: vs_interface.png

#. Set the acceleration sensitivity and the sensor DC bias (mV) using the
   following values:

   **Reference**

   - Current Source = ON
   - Sensitivity = 100 mV/g
   - Sensor DC Bias = 10700 mV

   **DUT**

   - Enable = ON
   - Current Source = ON
   - Sensitivity = 60 mV/g
   - Sensor DC Bias = 8000 to 13000 mV

#. Adjust the frequency settings to your requirements.
#. Connect the other end of the BNC cable to the EVAL-CN0582-USBZ (J6).
#. Click Start to launch the test. Then wait for it to finish.

   .. figure:: eval-cn0588-ebz_freq.png

.. tip::
   The CN0588’s IEPE interface makes it suitable to be used with different
   IEPE-compatible data acquisition systems. Analog Devices has various IEPE
   reference designs that users can readily evaluate and prototype with.

   For CbM applications requiring one channel measurement, the
   :adi:`CN0540 24-Bit IEPE data acquisition system <cn0540>` is recommended.

   For applications requiring Arduino form-factor, the :adi:`CN0579 <CN0579>` is
   the suggested IEPE vibration sensor measurement system to use with the CN0588.

Resources
---------

- :adi:`ADXL1002 Product Page <ADXL1002>`
- :adi:`ADR5043/ADR5045 Product Page <ADR5045>`
- :adi:`LT6015 Product Page <LT6015>`
- :adi:`CN0582 Product Page <CN0582>`

Design & Integration Files
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Download

   :download:`EVAL-CN0588-EBZ Design & Integration Files <cn0588-designsupport.zip>`

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Allegro Project

Help and Support
~~~~~~~~~~~~~~~~

For questions and more information about this product, connect with us through
the Analog Devices :ez:`ez/reference-designs`.
