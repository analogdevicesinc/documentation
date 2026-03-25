.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0346

.. _eval-cn0346-pmdz:

EVAL-CN0346-PMDZ
=================

Relative Humidity Measurement System.

Overview
--------

:adi:`CN0346` provides a contactless, capacitive-based relative humidity (RH)
measurement solution with 2% RH accuracy from 0% RH to 100% RH. This circuit
replaces bulky hygrometer-based methods and is ideal for applications where
accurate, temperature-controlled, noncontact humidity measurements are
critical, such as HVAC, telecommunication cabinets, infant incubators, and
other industrial or medical applications.

.. figure:: cn0346_hw_375.jpg
   :width: 300px
   :align: center

   EVAL-CN0346-PMDZ evaluation board

Required Equipment
------------------

- :adi:`EVAL-CN0346-SDPZ <CN0346>` evaluation board
- :adi:`EVAL-SDP-CB1Z` controller board (SDP-B)
- :adi:`EVAL-SDP-PMOD <EVAL_SDP-PMOD>` interposer board (SDP-to-PMOD)
- CN0346 Evaluation Software
- USB Type-A to USB Mini-B cable
- Boveda calibration packs or other humidity-controlled environment
- 6 V power supply

Minimum PC/System Requirements
------------------------------

- Windows XP SP2, Windows Vista, or Windows 7 Business/Enterprise/Ultimate
- Intel Pentium processor (x86 compatible), 1 GHz or faster
- 512 MB RAM and 2 GB available hard disk space
- .NET 3.5 Framework

Software Installation
---------------------

#. Extract the files within **CN0341 SDP Eval Software.zip** and run
   **setup.exe**. It is recommended to install the CN0341 SDP Evaluation
   Software to the default directory path
   ``C:\Program Files\Analog Devices\CN0341\`` and all National Instruments
   products to ``C:\Program Files\National Instruments\``.

   .. figure:: destination_directory.png
      :width: 600px
      :align: center

      Destination directory selection

#. Press **Next**.

   .. figure:: begin_install.png
      :width: 600px
      :align: center

      Begin installation

#. Press **Next**.
#. Upon completion of the CN0341 SDP Eval Software installation, the ADI SDP
   Drivers installer will execute. Follow the on-screen prompts to install the
   drivers. It is recommended to close all other applications before clicking
   **Next** so that relevant system files can be updated without a reboot.
#. Press **Next**.

   .. figure:: sdp_drivers.png
      :width: 500px
      :align: center

      ADI SDP Drivers installer

#. Install the drivers to the default directory path
   ``C:\Program Files\Analog Devices\SDP\Drivers\``.

   .. figure:: sdp_drivers_location.png
      :width: 500px
      :align: center

      SDP drivers install location

#. Press **Install** to complete the installation of all software necessary to
   evaluate the EVAL-CN0346-SDPZ.

Opening and Enabling the Evaluation Software
---------------------------------------------

#. Launch the executable found at
   ``C:\Program Files\Analog Devices\CN0346`` and press the **Connect**
   button.

   .. figure:: software.jpg
      :width: 600px
      :align: center

      CN0346 evaluation software main window

Calibration Procedure
---------------------

The following is a step-by-step guide for calibrating the EVAL-CN0346-SDPZ:

#. Calibration requires the user to identify and input the maximum and minimum
   values of humidity and sensor capacitance.
#. Place the PCB into a humidity-controlled environment and adjust the
   environment to the desired minimum humidity value.
#. Use an external LCR meter to measure the sensor capacitance.
#. Place both values into the calibration tab in the evaluation software.
#. Repeat these steps for the desired maximum humidity value and enter the
   values into the software.
#. Input the calculated CAPDAC value into the box found at the bottom of the
   Calibration tab.

   .. figure:: software-calibration_tab.jpg
      :width: 600px
      :align: center

      Calibration tab for humidity and capacitance values

Documents
---------

- :adi:`CN0346 Circuit Note <CN0346>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0346-PMDZ Design & Integration Files
   <https://www.analog.com/cn0346-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
