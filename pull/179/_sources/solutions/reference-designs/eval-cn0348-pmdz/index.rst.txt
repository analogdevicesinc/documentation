.. _eval-cn0348-pmdz:

.. |black_led| image:: black_led_button.png
.. |green_led| image:: green_led_button.png
.. |red_led| image:: red_led_button.png

EVAL-CN0348-PMDZ
=================

Precision 16-Bit Digital-to-Analog Converter with Wide Dynamic Signal Range.

Overview
--------

:adi:`CN0348` showcases a solution for precision 16-bit digital-to-analog
conversion with wide dynamic signal range in a single-supply system. It
utilizes a 5 V voltage reference (:adi:`ADR4550`), a voltage output
digital-to-analog converter (:adi:`AD5541A`), and a rail-to-rail amplifier as
the output buffer (:adi:`ADA4500-2`). The :adi:`ADA4500-2` exhibits zero
crossover distortion, making it an excellent choice as an output buffer to
maintain the linearity of the :adi:`AD5541A` over its input digital code and
provide a wide dynamic output range. The combination of parts provides
industry-leading 16-bit integral nonlinearity (INL) of +/-1 LSB and
differential nonlinearity (DNL) of +/-1 LSB with guaranteed monotonicity.

.. figure:: cn0348_simplified_schematic.png
   :align: center

   CN0348 simplified schematic

Required Equipment
------------------

- :adi:`EVAL-SDP-CB1Z` controller board (SDP-B board)
- :adi:`EVAL-CN0348-SDPZ <CN0348>` evaluation board (CN-0348 board)
- CN0348 Evaluation Software (supplied with provided CD in kit)
- USB Type-A to USB Mini-B cable
- SMB connector
- PC with the following minimum requirements:

  - Windows XP SP2, Windows Vista, or Windows 7
  - USB Type-A port
  - Processor rated at 1 GHz or faster
  - 512 MB RAM and 500 MB available hard disk space

- For INL/DNL data collection:

  - GPIB-USB HS controller (NI-488.2 3.1.1 GPIB controller driver available
    from `National Instruments <https://www.ni.com/en-us/support/model.gpib-usb-hs.html>`__)
  - Agilent 3458A multimeter

.. note::

   Any multimeter can be used with this board. However, for INL/DNL
   measurement, the software interface was written with the Agilent 3458A in
   mind.

Installing the Software
------------------------

#. Open the file **setup.exe** that is provided from the CD in kit.

   .. note::

      It is recommended that you install the CN0348 Evaluation Software to the
      default directory path ``C:\Program Files\Analog Devices\CN0348\`` and
      all National Instruments products to
      ``C:\Program Files\National Instruments\``.

   .. figure:: cn0348-install1.png
      :align: center

      CN0348 SDP Evaluation Software destination directory

#. Click **Next** to view the installation review page.

   .. figure:: cn0348-install2.png
      :align: center

      CN0348 installation review page

#. Click **Next** to start the installation.

#. Upon completion of the installation of the **CN0348 SDP Evaluation
   Software**, the installer for the **ADI SDP Drivers** will execute.

   .. note::

      It is recommended that you close all other applications before clicking
      **Next**. This will make it possible to update relevant system files
      without having to reboot your computer.

   .. figure:: cn0348-install3.png
      :align: center

      ADI SDP Drivers setup wizard

#. Click **Next** to set the installation location for the **SDP Drivers**.

   It is recommended that you install the drivers to the default directory
   path ``C:\Program Files\Analog Devices\SDP\DriversR2``.

   .. figure:: cn0348-install4.png
      :align: center

      SDP Drivers install location

#. Click **Next** to install the **SDP Drivers** and complete the installation
   of all software.

Using the Evaluation Software
------------------------------

Software Control and Indicator Descriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: software1.png
   :align: center

   CN0348 evaluation software main window

The evaluation software provides the following controls and indicators:

#. **LDAC Control** -- Always check this box before starting any test.

#. **Write to DAC Button** -- Enter the digital input code in **DIN**. When
   the **WRITE TO DAC** button is clicked, the digital input code is sent to
   the DAC.

#. **Output Indicator** -- The LED string indicates the digital input code
   being written to the DAC (from bit 15 to bit 0).

#. **System Status String / LED Indicator** -- The string indicator displays a
   message detailing the current state of the software. The LED indicator
   displays the current state in the form of a colored LED:

   - |black_led| Black: Inactive
   - |green_led| Green: Busy
   - |red_led| Red: Error

   .. figure:: software2.png
      :align: center

      CN0348 evaluation software -- INL/DNL measurement controls

#. **Code Step Control** -- Enter the code step between each digital input to
   be written to the DAC.

#. **Agilent 3458A GPIB Address Control** -- Enter the GPIB address of the
   multimeter. The GPIB address can be determined from the multimeter by
   pressing SHIFT+Local. By default it should be 22.

#. **Current Code / Voltage Indicator** -- Indicates the current digital input
   code and output voltage of the DAC.

#. **File Directory Control** -- Enter the file directory and name to save the
   INL/DNL measurement data.

#. **INL / DNL Measurement Graphs** -- Display the INL and DNL vs. input
   digital code when data collection is done.

   .. figure:: software3.png
      :align: center

      INL and DNL measurement graphs

#. **Transfer Function Graph** -- Shows the transfer function of the DAC
   output voltage vs. input digital code.

   .. figure:: software4.png
      :align: center

      Transfer function graph

#. **SDP Board Firmware Information** -- Provides up-to-date information on
   the SDP board firmware.

Connecting the Hardware and Taking Measurements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Connect the SDP board to the CN0348 board.
#. Connect +6 V and analog ground to the CN0348 board at **J1**.
#. Connect the USB cable supplied with the SDP board to the USB port on the
   PC and the SDP board.
#. Connect **Vout** (**J3**) to a multimeter.
#. Open **CN0348.exe** (located in
   ``C:\Program Files\Analog Devices\CN0348\``).
#. The application will attempt to connect to the board immediately.
#. Check the **LDAC** box.
#. Perform a functionality test by entering the following in **DIN** and
   clicking **WRITE TO DAC**:

   a. ``0000`` -- multimeter should read close to 0 V.
   b. ``FFFF`` -- multimeter should read close to 5 V.
   c. **OUTPUT** (Bit 15 to Bit 0) should also light up the associated LED
      indicator.

INL/DNL Data Collection
~~~~~~~~~~~~~~~~~~~~~~~~

#. Connect Vout to the Agilent 3458A multimeter.
#. Connect the Agilent 3458A to the PC using a GPIB-to-USB Type-A connector
   (for data collection via LabVIEW software).
#. Set the multimeter to have NPLC as 1.
#. Enter the GPIB address of the Agilent 3458A.
#. Enter the desired **Code Step**:

   - Code Step = 16 takes approximately 4 min 10 sec to finish measurement.
   - Code Step = 32 takes approximately 2 min 5 sec to finish measurement.

#. Enter the file name and path to save data in the **Enter file name to save
   data before running** field.
#. Click **Start**.
#. **Current Code** and **Current Voltage** should show the progress of
   measurements.
#. To exit, go to File > Exit.

Documents
---------

- :adi:`CN0348 Circuit Note <CN0348>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0348-SDPZ Design & Integration Files
   <https://www.analog.com/cn0348-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials

Additional Information
----------------------

- :adi:`AD5541A Product Page <AD5541A>`
- :adi:`ADR4550 Product Page <ADR4550>`
- :adi:`ADA4500-2 Product Page <ADA4500-2>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
