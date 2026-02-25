.. _eval-cn0368-sdpz:

EVAL-CN0368-SDPZ
=================

Magneto-Resistive Rotational Position Measurement.

Overview
--------

:adi:`CN0368` is a contactless, AMR (anisotropic magneto-resistive) based
angle measurement solution ideal for angle and linear position measurements.
The system is capable of providing better than 0.2 degree accuracy. This
translates into a linear position accuracy of 2 mil (0.002 inches).

The circuit is ideal for applications where high-speed, accurate, non-contact
angle and length measurements are critical, such as brushless DC motor control.

.. figure:: cn0368.jpg
   :width: 600px
   :align: center

   EVAL-CN0368-SDPZ evaluation board

Required Equipment
------------------

- :adi:`EVAL-CN0368-SDPZ <CN0368>` evaluation board
- :adi:`EVAL-SDP-CB1Z` evaluation board (SDP-B board)
- CN0368 Evaluation Software
- USB Type-A to USB Mini-B cable
- One of the following power supplies:

  - 6 V DC wall wart (EVAL-CFTL-6V-PWRZ)
  - DC power supply with a 0--6 V output (HP6236B)

- Diametrically magnetized neodymium magnet (for rotational testing)
- Neodymium magnet approximately 2 inches in length, magnetized along the
  length of the magnet (for linear testing)

Minimum PC/System Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Windows XP SP2, Windows Vista, or Windows 7
  Business/Enterprise/Ultimate editions
- Intel Pentium processor (x86 compatible), 1 GHz or faster
- 512 MB RAM and 2 GB available hard disk space
- .NET 3.5 Framework

Installing the Software
------------------------

#. Extract the files within the file **CN0368 SDP Eval Software.zip** and open
   the file **setup.exe**. It is recommended that you install the CN0368 SDP
   Evaluation Software to the default directory path
   ``C:\Program Files\Analog Devices\CN0368\`` and all National Instruments
   products to ``C:\Program Files\National Instruments\``.

   .. figure:: software_2.png
      :width: 600px
      :align: center

      CN0368 SDP Eval Software installer

#. Press **Next**.

   .. figure:: software_3.png
      :width: 600px
      :align: center

      License agreement

#. Press **Next**.

   .. figure:: software_5.png
      :width: 600px
      :align: center

      Installation progress

#. Press **Next**.

#. Upon completion of the installation of the **CN0368 SDP Eval Software**,
   the installer for the **ADI SDP Drivers** will execute. Follow the
   on-screen prompts to install the drivers. It is recommended that you close
   all other applications before clicking **Next**. This will make it possible
   to update relevant system files without having to reboot your computer.

   .. figure:: software_6.png
      :width: 600px
      :align: center

      ADI SDP Drivers installer

#. Press **Next**.

#. It is recommended that you install the drivers to the default directory
   path ``C:\Program Files\Analog Devices\SDP\Drivers\``.

#. Press **Install** to install the drivers and complete the installation of
   all software necessary to evaluate the **EVAL-CN0368-SDPZ**.

Hardware Setup
--------------

#. Connect the +6 V power supply to the evaluation board.
#. Mount magnets for rotational or linear position testing.
#. Connect the 120-pin connector on the CN0368 board to **CON A** on the
   :adi:`EVAL-SDP-CB1Z`.
#. Connect the USB cable from the PC to the SDP-B board.

Opening and Enabling the Evaluation Software
----------------------------------------------

#. Launch the executable found at
   ``C:\Program Files\Analog Devices\CN0368`` and press the **Connect**
   button.
#. The software will connect to the SDP board and the evaluation interface
   will become active.

   .. figure:: software_8.png
      :width: 600px
      :align: center

      CN0368 evaluation software interface

Calibration Methods
--------------------

Single Temperature Calibration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Single Temperature Calibration method allows the user to calculate
VSIN_Offset and VCOS_Offset before calculating the magnetic field angle. This
eliminates any error sources associated with a dynamic calibration procedure
but requires extra steps and time.

#. Select **Single Temperature Calibration** from the drop-down menu.

   .. figure:: single_temperature_calibration.png
      :width: 600px
      :align: center

      Single Temperature Calibration mode

#. A prompt will appear instructing the user to rotate the magnetic stimulus
   through 360 degrees. During this time the software is actively calculating
   VSIN_Offset and VCOS_Offset.
#. Press **End Calibration** when finished. The software will display the
   magnetic field angle, VSIN_Offset, and VCOS_Offset.
#. Press **Sample Data** to actively calculate the magnetic field angle using
   the offsets calculated during the Single Temperature Calibration.

   .. figure:: sample_data.png
      :width: 600px
      :align: center

      Sampling data after Single Temperature Calibration

#. Press **Click to Stop** when finished.

Multiple Temperature Calibration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Multiple Temperature Calibration procedure is a method of compensating for
temperature effects experienced by the amplifier and ADC. The temperature
coefficients and offsets are calculated to provide a more accurate magnetic
field angle and system response.

#. Select **Multiple Temperature Calibration** from the drop-down menu.
#. Place the hardware in a temperature-controlled environment at the desired
   T1.

   .. figure:: multiple_temperature_calibration_1.png
      :width: 600px
      :align: center

      Enter the temperature T1

#. Press **Ok**.

   .. figure:: multiple_temperature_calibration_2.png
      :width: 600px
      :align: center

      Rotate stimulus through 360 degrees for T1 calibration

#. Rotate the stimulus through 360 degrees while VSIN_Offset_T1 and
   VCOS_Offset_T1 are calculated.
#. Press **Ok**.

   .. figure:: multiple_temperature_calibration_3.png
      :width: 600px
      :align: center

      T1 calibration complete, enter temperature T2

#. Place the hardware in a temperature-controlled environment at the desired
   T2.
#. Press **Ok**.

   .. figure:: multiple_temperature_calibration_4.png
      :width: 600px
      :align: center

      Rotate stimulus through 360 degrees for T2 calibration

#. Rotate the stimulus through 360 degrees while VSIN_Offset_T2 and
   VCOS_Offset_T2 are calculated.
#. Press **Ok**.
#. Press **Sample Data** to observe the magnetic field angle results corrected
   for temperature and offset effects.

Dynamic Calibration
~~~~~~~~~~~~~~~~~~~~

The Dynamic Calibration method actively calculates VSIN_Offset and VCOS_Offset
as the magnetic stimulus rotates through 360 degrees. The software then
subtracts these offsets in real time. This method is simpler than the Single
Temperature Calibration and Multiple Temperature Calibration and can be
implemented faster, with more ease.

#. Select **Dynamic Calibration** from the drop-down menu.

   .. figure:: dynamic_calibration_2.png
      :width: 600px
      :align: center

      Dynamic Calibration mode

#. The software will automatically begin to sample and convert the VSIN and
   VCOS channels of the ADA4571.
#. Rotate the magnetic stimulus through 360 degrees.
#. The software will display the magnetic field angle, VSIN_Offset, and
   VCOS_Offset as the stimulus is rotated. Early calculations for the magnetic
   field angle will have large errors until the offsets are calculated more
   precisely; the accuracy of the system will quickly improve with as few as
   one or two rotations.
#. Press **Click to Stop** when finished. The software will revert to its
   starting position allowing you to experiment with a new calibration method,
   or simply to sample data with the existing calibration data.

Documents
---------

- :adi:`CN0368 Circuit Note <CN0368>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0368-SDPZ Design & Integration Files
   <https://www.analog.com/cn0368-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials

Additional Information
----------------------

- :adi:`ADA4571 Product Page <ADA4571>`
- :adi:`AD7866 Product Page <AD7866>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
