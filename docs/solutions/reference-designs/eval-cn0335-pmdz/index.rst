.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0335

.. _eval-cn0335-pmdz:

EVAL-CN0335-PMDZ
=================

Isolated +/-10 V Single Supply Analog-to-Digital Conversion System.

.. figure:: cn0335_hw_375.jpg
   :align: center
   :width: 375px

   EVAL-CN0335-PMDZ evaluation board

Overview
--------

:adi:`CN0335 <CN0335>` provides a robust and complete solution for +/-10 V
voltage-to-digital conversion with isolation, for measurements where voltage is
used as the standard interface. The design solution is optimized for high
precision and low cost measurement, using only three active devices, and has a
total unadjusted error of less than 0.1% FSR. The accuracy depends on the
calibration.

The circuit incorporates the :adi:`AD8606 <AD8606>` precision op-amp, the
:adi:`AD7091R <AD7091R>` 12-bit successive approximation (SAR) ADC, and the
:adi:`ADuM5401 <ADUM5401>` digital isolator with integrated isolated power
supply to create a standard +/-10 V measurement system.

.. figure:: overview_fig_1.png
   :align: center

   +/-10 V single supply analog-to-digital conversion with isolation
   (all connections and decoupling not shown)

The circuit has a 12-pin PMOD connector on board, which can be used for
connection to a customer microprocessor or FPGA. The :adi:`CN0335 Circuit Note
<CN0335>` discusses the design steps needed to optimize the circuit for a
specific bandwidth including noise analysis and component selection
considerations.

The performance of the circuit can be demonstrated with the use of the Analog
Devices SDP controller :adi:`EVAL-SDP-CB1Z` and the SDP-to-PMOD interposer
board :adi:`SDP-PMD-IB1Z <SDP-PMD-IB1Z>`, both optional purchase items.

Required Equipment
------------------

- :adi:`EVAL-SDP-CB1Z` controller board (SDP-B board)
- EVAL-CN0335-PMDZ evaluation board (CN0335 board)
- :adi:`EVAL-CFTL-6V-PWRZ` (+6 V power supply) or equivalent
- :adi:`SDP-PMD-IB1Z <SDP-PMD-IB1Z>` SDP-to-PMOD interposer board
- Voltage source (voltage generator)
- Multimeter (to measure the input current)
- CN0335 evaluation software (supplied on CD in kit)
- USB Type-A to USB Type Mini-B cable
- PC with the following minimum requirements:

  - Windows XP Service Pack 2 (32-bit)
  - USB Type-A port
  - Processor rated at 1 GHz or faster
  - 512 MB RAM and 500 MB available hard disk space

General Setup
-------------

- The **EVAL-CFTL-6V-PWRZ** (+6 V DC power supply) powers the
  EVAL-CN0335-PMDZ (CN0335 board) via the DC barrel jack.
- The **SDP-PMD-IB1Z** (interposer board) connects to the **EVAL-SDP-CB1Z**
  (SDP-B board) via the 120-pin connector A.
- The **EVAL-SDP-CB1Z** (SDP-B board) connects to the PC via the USB cable.
- The **EVAL-CN0335-PMDZ** (CN0335 board) connects to the **SDP-PMD-IB1Z**
  (interposer board) via the 12-pin header PMOD connectors (**J1** and **J3**).
- The +/-10 V source (voltage generator) connects to the EVAL-CN0335-PMDZ
  (CN0335 board) via the terminal block **J2**.

.. figure:: general_setup.png
   :align: center

   General hardware setup

Installing the Software
------------------------

1. Load the evaluation software by placing the CN0335 evaluation software disc
   in the CD drive of the PC, or download the most up-to-date copy from the
   CN0335 product page. Open the file **setup.exe**.

   .. note::

      It is recommended that you install the CN0335 evaluation software to the
      default directory path
      **C:\\Program Files\\Analog Devices\\CN0335\\** and all National
      Instruments products to **C:\\Program Files\\National Instruments\\**.

   .. figure:: installing_sw_1.png
      :align: center

      CN0335 evaluation software installer

2. Click **Next** to view the installation review page.

   .. figure:: installing_sw_2.png
      :align: center

      Installation review page

3. Click **Next** to start the installation.

   .. figure:: installing_sw_3.png
      :align: center

      Installation progress

4. Upon completion of the installation of the **CN0335 Evaluation Software**,
   the installer for the **ADI SDP Drivers** will execute.

   .. note::

      It is recommended that you close all other applications before clicking
      **Next**. This will make it possible to update relevant system files
      without having to reboot your computer.

   .. figure:: installing_sw_4.png
      :align: center

      ADI SDP Drivers installer

5. Press **Next** to set the installation location for the **SDP Drivers**.

   .. note::

      It is recommended that you install the drivers to the default directory
      path **C:\\Program Files\\Analog Devices\\SDP\\DriversR2**.

   .. figure:: installing_sw_5.png
      :align: center

      SDP Drivers installation location

6. Press **Next** to install the **SDP Drivers** and complete the installation
   of all software. Click **Finish** when done.

   .. figure:: installing_sw_6.png
      :align: center

      SDP Drivers installation progress

   .. figure:: installing_sw_6a.png
      :align: center

      Installation complete

Connecting the Hardware
------------------------

1. Connect the +6 V DC power supply (wall wart) to the barrel jack **J1** of
   the SDP-PMD-IB1Z (interposer board).

   .. note::

      Make sure that the jumper is positioned as shown on the board label.

   .. figure:: connecthw_1.png
      :align: center
      :width: 600px

      Connecting the +6 V power supply to the interposer board

2. Connect the 120-pin connector on the SDP-PMD-IB1Z (interposer board) to the
   120-pin connector marked **CON A** on the EVAL-SDP-CB1Z (SDP-B board).

   .. figure:: connecthw_2.png
      :align: center
      :width: 600px

      Connecting the interposer board to the SDP-B board

3. Connect the USB cable supplied with the EVAL-SDP-CB1Z (SDP-B board) to the
   USB port on the PC and the SDP board.

   .. figure:: connecthw_3.png
      :align: center
      :width: 600px

      Connecting the USB cable to the SDP-B board

   .. note::

      Verify that the SDP drivers are loaded properly. Open the Device Manager
      and check if the SDP board is recognized. If not, repeat steps 1--3.

   .. figure:: connecthw_3a.png
      :align: center

      SDP board recognized in Device Manager

4. Connect the EVAL-CN0335-PMDZ (CN0335 board) to the SDP-PMD-IB1Z
   (interposer board) via the 12-pin header PMOD connector.

   .. figure:: connecthw_4.png
      :align: center
      :width: 600px

      Connecting the CN0335 board to the interposer board

5. Connect the input voltage source to the **J2** terminal block. The polarity
   is marked on the board.

   .. figure:: connecthw_5.png
      :align: center
      :width: 600px

      Connecting the input voltage source to terminal block J2

Using the Evaluation Software
------------------------------

Software Control and Indicator Descriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: using_sw_1.png
   :align: center

   CN0335 evaluation software -- main controls

.. figure:: using_sw_2.png
   :align: center

   CN0335 evaluation software -- calibration and indicators

.. figure:: using_sw_3.png
   :align: center

   CN0335 evaluation software -- SDP revision information

1. **Connect/Reconnect Button** -- Makes a USB connection between the SDP-B
   board and the CN0335 board. A connection to the SDP-B board must be made to
   use the software.

2. **Run Button** -- Collects conversion data and presents the acquisitions in
   the chart.

3. **Stop Button** -- Stops collecting data from the CN0335 board.

4. **Clear Data Button** -- Clears all data collected from the chart history.

5. **Save Data Button** -- Saves the data collected to a tab-delimited ASCII
   spreadsheet file.

6. **Control Tabs**:

   - **Acquire Data/Main** -- Brings the data collection graph to the front.
   - **Calibrate System** -- Brings the system calibration settings to the
     front.
   - **SDP Revision** -- Brings the SDP board information window to the front.

7. **Numerical Indicator** -- Displays the current reading value. The value
   units depend on the chosen graph units.

8. **Graph** -- Displays the collected data. The units on the graph depend on
   the chosen graph units.

9. **Graph Controls** -- Allow the user to zoom in, zoom out, and pan through
   the data collected.

10. **Graph Units Radio Buttons** -- Determines the units of the data displayed
    in the chart and the numerical indicator.

11. **System Status String Indicator** -- Displays a message detailing the
    current state of the software.

12. **System Status LED Indicator** -- Displays the current state of the
    software as an LED with four status colors:

    - |inactive| **Inactive**
    - |busy| **Busy**
    - |error| **Error**
    - |waiting| **Waiting for user action**

    .. |inactive| image:: using_sw_12inactive.png
    .. |busy| image:: using_sw_12busy.png
    .. |error| image:: using_sw_12error.png
    .. |waiting| image:: using_sw_12waiting.png

13. **Calibrate System Controls** -- Allow the user to calibrate the CN0335
    board. Two voltage inputs in the range +/-10 V are required. For best
    performance, the inputs should be "-10 V" and "+10 V". Follow the
    on-screen instructions to perform the calibration.

14. **SDP Firmware Revision** -- Read-only data. After the connection is
    established with the SDP board, the basic controller information can be
    found here.

Establishing a USB Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Follow the instructions to properly install the software and connect the
   hardware as described in the previous sections.

2. Open the file named **CN0335.exe** in the installation directory.

   .. note::

      If the software was installed to the default location it will be found
      at **C:\\Program Files\\Analog Devices\\CN0335\\CN0335.exe**.

3. Click the **Connect/Reconnect Button**. A window with a progress bar will
   load.

   .. figure:: establishing_connection_3.png
      :align: center

      USB connection progress bar

4. Upon success, the **System Status String Indicator** will display
   *SDP Board Ready to Acquire Data*.

Calibrating the CN0335 Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Establish a USB connection link.
2. Click the **Calibrate System** tab.
3. Apply the first calibration current to the input connector **J2** of the
   CN0335.
4. Write down the applied current to the **Calibration Current 1** indicator.
5. Press the **Calibrate 1** button.
6. Apply the second calibration current to the input connector **J2** of the
   CN0335 (different from the previous calibration current).
7. Write down the applied current to the **Calibration Current 2** indicator.
8. Press the **Calibrate 2** button.

Capturing Data
~~~~~~~~~~~~~~~

1. Establish a USB connection link.
2. Click the **Run Button**.
3. Click the **Stop Button** when acquisition is complete.

Saving Data to a Spreadsheet File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Establish a USB connection link.
2. Capture data.
3. Click the **Save Data Button**.

   .. figure:: saving_data_3.png
      :align: center

      Save data dialog

4. Click the **OK Button**.
5. Browse to the directory location where the spreadsheet file is to be saved.
6. Name the file.
7. Click the **OK Button**.
8. Open the saved file with Notepad or similar text editor. The saved data
   shows the ADC Codes (decimal).

.. note::

   The software saves the spreadsheet file as ASCII text with columns
   separated by tabs.

Documents
---------

- :adi:`CN0335 Circuit Note <CN0335>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0335-PMDZ Design & Integration Files
   <https://www.analog.com/cn0335-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials

Additional Information
----------------------

- :adi:`AD8606 Product Page <AD8606>`
- :adi:`AD7091R Product Page <AD7091R>`
- :adi:`ADuM5401 Product Page <ADUM5401>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
