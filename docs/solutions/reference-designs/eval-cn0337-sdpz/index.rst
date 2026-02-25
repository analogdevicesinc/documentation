.. _eval-cn0337-sdpz:

EVAL-CN0337-SDPZ
=================

Isolated RTD Temperature Measurement System (SDP Interface).

The :adi:`EVAL-CN0337-SDPZ <CN0337>` provides a robust and complete solution for
temperature-to-digital conversion with isolation, for measurements where
standard RTD sensors are used. The design solution is optimized for high
precision and low-cost measurement, using only three active devices, and has a
total unadjusted temperature error of less than 0.039% FSR/C. The accuracy
depends on the calibration.

Overview
--------

The circuit shown in Figure 1 incorporates the :adi:`AD8608` op amp, the
:adi:`AD7091R` 12-bit successive approximation (SAR) ADC, and the
:adi:`ADuM5401` isolator to create a standard temperature measurement system.
The circuit has a 12-pin PMOD connector on board, which can be used for
connection to a customer microprocessor or FPGA.

.. figure:: overview-fig1.png
   :align: center
   :width: 700

   Figure 1. Resistance Deviation to Digital Conversion with Isolation Using
   Pt100 RTD Sensor (All Connections and Decoupling Not Shown)

The :adi:`CN0337 Circuit Note <CN0337>` discusses the design steps needed to
optimize the circuit for a specific temperature range including component
selection considerations.

The performance of the circuit can be demonstrated with the use of the Analog
Devices SDP controller :adi:`EVAL-SDP-CB1Z` and the SDP-to-PMOD interposer
board :adi:`SDP-PMD-IB1Z`, both optional purchase items.

Supported Devices
-----------------

- :adi:`AD7091R` -- 12-bit SAR ADC
- :adi:`AD8608` -- Precision CMOS Op Amp
- :adi:`ADuM5401` -- Quad-Channel Digital Isolator

Required Equipment
------------------

- :adi:`EVAL-SDP-CB1Z` controller board (SDP-B board)
- :adi:`EVAL-CN0337-PMDZ <CN0337>` evaluation board (CN0337 board)
- :adi:`EVAL-CFTL-6V-PWRZ` (+6V power supply) or equivalent
- :adi:`SDP-PMD-IB1Z` SDP-to-PMOD interposer board
- Resistance decade box (to simulate RTD input resistance), e.g. IET RS-200.
  If no calibration procedure is performed, the temperature can be measured
  using a real sensor.
- CN0337 evaluation software (supplied on CD in the kit, or download from the
  :adi:`CN0337` product page)
- PC with Windows XP SP2 (32-bit) or later, USB type A port, 1 GHz+ processor,
  512 MB RAM and 500 MB available hard disk space
- USB type A to USB type mini-B cable

General Setup
-------------

- The :adi:`EVAL-CFTL-6V-PWRZ` (+6V DC power supply) powers the
  EVAL-CN0337-SDPZ (CN0337 board) via the DC barrel jack.
- The :adi:`SDP-PMD-IB1Z` (interposer board) connects to the
  :adi:`EVAL-SDP-CB1Z` (SDP-B board) via the 120-pin connector A.
- The :adi:`EVAL-SDP-CB1Z` (SDP-B board) connects to the PC via the USB cable.
- The EVAL-CN0337-SDPZ (CN0337 board) connects to the SDP-PMD-IB1Z
  (interposer board) via the 12-pin header PMOD connector (J1 and J3).
- The Pt100 resistance decade connects to the EVAL-CN0337-SDPZ (CN0337 board)
  via the terminal block **J2**.

.. figure:: general_setup.png
   :align: center
   :width: 600

   General hardware setup diagram

Installing the Software
-----------------------

1. Load the evaluation software by placing the CN0337 evaluation software disc
   in the CD drive of the PC. You can also download the most up-to-date copy
   from the :adi:`CN0337` product page. Open the file ``setup.exe``.

   .. note::

      It is recommended to install the CN0337 evaluation software to the
      default directory path ``C:\Program Files\Analog Devices\CN0337\`` and
      all National Instruments products to
      ``C:\Program Files\National Instruments\``.

   .. figure:: installing_sw1.png
      :align: center

      CN0337 software installer

2. Click **Next** to view the installation review page.

   .. figure:: installing_sw2.png
      :align: center

      Installation review page

3. Click **Next** to start the installation.

   .. figure:: installing_sw3.png
      :align: center

      Installation progress

4. Upon completion of the CN0337 evaluation software installation, the
   installer for the ADI SDP drivers will execute.

   .. note::

      It is recommended to close all other applications before clicking
      **Next**. This will make it possible to update relevant system files
      without having to reboot your computer.

   .. figure:: installing_sw4.png
      :align: center

      ADI SDP drivers installer

5. Press **Next** to set the installation location for the SDP drivers.

   .. note::

      It is recommended to install the drivers to the default directory path
      ``C:\Program Files\Analog Devices\SDP\DriversR2``.

   .. figure:: installing_sw5.png
      :align: center

      SDP drivers installation location

6. Press **Next** to install the SDP drivers and complete the installation of
   all software. Click **Finish** when done.

   .. figure:: installing_sw6.png
      :align: center

      SDP drivers installation progress

   .. figure:: installing_sw6-b.png
      :align: center

      SDP drivers installation complete

Connecting the Hardware
-----------------------

1. Connect the :adi:`EVAL-CFTL-6V-PWRZ` (+6V DC power supply) to the barrel
   jack **J1** of the :adi:`SDP-PMD-IB1Z` (interposer board) as depicted below.

   .. note::

      Make sure that the jumper is positioned as shown below.

   .. figure:: cn0336-connectinghw1.png
      :align: center
      :width: 600

      Power supply connection to interposer board

2. Connect the 120-pin connector on the :adi:`SDP-PMD-IB1Z` (interposer board)
   to the 120-pin connector marked **CON A** on the :adi:`EVAL-SDP-CB1Z`
   (SDP-B board).

   .. figure:: cn0336-connectinghw2.png
      :align: center
      :width: 600

      Interposer board to SDP-B board connection

3. Connect the USB cable supplied with the :adi:`EVAL-SDP-CB1Z` (SDP-B board)
   to the USB port on the PC and the SDP board.

   .. figure:: cn0336-connectinghw3.png
      :align: center
      :width: 600

      USB cable connection

   .. note::

      Verify that the SDP drivers are loaded properly. Open the Device Manager
      and check if the SDP board is recognized. If not, repeat the software
      installation steps.

   .. figure:: cn0336-connectinghw3a.png
      :align: center
      :width: 600

      SDP board in Device Manager

4. Connect the EVAL-CN0337-PMDZ (CN0337 board) to the :adi:`SDP-PMD-IB1Z`
   (interposer board) via the 12-pin header PMOD connector.

   .. figure:: cn0336-connectinghw4.png
      :align: center
      :width: 600

      CN0337 board to interposer board connection

5. Connect the input resistance source (resistance decade or RTD sensor) to
   terminal block **J2**. The polarity is shown in the picture below.

   .. figure:: cn0336-connectinghw5.png
      :align: center
      :width: 600

      Input connection to terminal block J2

Using the Evaluation Software
-----------------------------

Software Control and Indicator Descriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: using_sw_1.png
   :align: center

   CN0337 evaluation software -- Acquire Data Main tab

.. figure:: using_sw_2.png
   :align: center

   CN0337 evaluation software -- Calibrate System tab

.. figure:: using_sw_3.png
   :align: center

   CN0337 evaluation software -- SDP Revision tab

1. **Connect/Reconnect Button** -- When pressed, the SDP-B board makes a USB
   connection to the CN0337 board. A connection to the SDP-B board must be made
   to use the software.
2. **Run Button** -- When pressed, the SDP-B board collects conversion data and
   presents the acquisitions in the chart.
3. **Stop Button** -- When pressed, the software stops collecting data from the
   CN0337 board.
4. **Clear Data Button** -- When pressed, the software clears all data collected
   from the chart history.
5. **Save Data Button** -- When pressed, the software saves the data collected
   to a tab-delimited ASCII spreadsheet file.
6. **Control Tabs**:

   - *Acquire Data Main* -- Brings the data collection graph to the front.
   - *Calibrate System* -- Brings the system calibration settings to the front.
   - *SDP Revision* -- Brings the SDP board information window to the front.

7. **Numerical Indicator** -- Displays the current reading value. The value
   units depend on the chosen graph units (10).
8. **Graph** -- Displays the collected data. The units on the graph depend on
   the chosen graph units (10).
9. **Graph Controls** -- Allow the user to zoom in, zoom out, and pan through
   the data collected.
10. **Graph Units Radio Buttons** -- Determines the units of the data displayed
    in the chart and the numerical indicator.
11. **System Status String Indicator** -- Displays a message detailing the
    current state of the software.
12. **System Status LED Indicator** -- Displays the current state of the
    software in the form of an LED. There are four status LED colors:

    - |led_inactive| Inactive
    - |led_busy| Busy
    - |led_error| Error
    - |led_waiting| Waiting for user action

13. **Calibrate System Controls** -- Allow the user to calibrate the CN0337
    board. For the calibration procedure two input resistance values are
    required. For best performance the inputs should be selected as 100 ohm
    and 212 ohm. Follow the instructions on the screen to perform the
    calibration.

    .. note::

       If other temperature ranges or sensors are used, the user must consult
       the sensor reference table to choose the appropriate resistance
       calibration values.

14. **SDP Firmware Revision** -- Read-only data. After the connection is
    established with the SDP board, the basic information for the controller
    can be found here.

.. |led_inactive| image:: led_inactive.png
.. |led_busy| image:: led_busy.png
.. |led_error| image:: led_error.png
.. |led_waiting| image:: led_waiting.png

Establishing a USB Connection Link
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Follow the instructions to properly install the software and connect the
   hardware as described in the previous sections.
2. Open the file named ``CN0337.exe`` in the installation directory.

   .. note::

      If the software was installed to the default location, it will be found
      at ``C:\Program Files\Analog Devices\CN0337\CN0337.exe``.

3. Click the **Connect/Reconnect Button**. A window with a progress bar will
   load.

   .. figure:: establishing_usb_connection.png
      :align: center

      USB connection progress bar

4. Upon success, the System Status String Indicator will display *SDP Board
   Ready to Acquire Data*.

Calibrating the CN0337 Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Establish a USB connection link.
2. Click the **Calibrate System** tab.
3. Apply the first calibration resistance to the input connector **J2** of the
   CN0337 board.
4. Write the applied resistance value in the **Calibration Resistance 1**
   indicator.
5. Press the **Calibrate 1** button.
6. Apply a different second calibration resistance to the input connector **J2**
   of the CN0337 board.
7. Write the applied resistance value in the **Calibration Resistance 2**
   indicator.
8. Press the **Calibrate 2** button.

Capturing Data
~~~~~~~~~~~~~~

1. Establish a USB connection link.
2. Click the **Run** button.
3. Click the **Stop** button when acquisition is complete.

Saving Data to a Spreadsheet File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Establish a USB connection link.
2. Capture data.
3. Click the **Save Data** button.

   .. figure:: saving_data_1.png
      :align: center

      Save data dialog

4. Click the **OK** button.
5. Browse to the directory location where the spreadsheet file is to be saved.
6. Name the file.
7. Click the **OK** button.
8. Open with Notepad or similar editor. The saved data shows the ADC codes in
   decimal format.

.. note::

   The software saves the spreadsheet file as ASCII text with columns separated
   by tabs.

Documents
---------

- :adi:`CN0337 Circuit Note <CN0337>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0337-SDPZ Design & Integration Files
   <https://www.analog.com/cn0337-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials

Additional Information
----------------------

- :adi:`AD7091R Product Page <AD7091R>`
- :adi:`AD8608 Product Page <AD8608>`
- :adi:`ADuM5401 Product Page <ADuM5401>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
