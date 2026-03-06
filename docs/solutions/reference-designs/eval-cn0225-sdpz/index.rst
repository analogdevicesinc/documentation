.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0225

.. _eval-cn0225-sdpz:

EVAL-CN0225-SDPZ
=================

Industrial Signal Digitization Analog Front End (+/-10 V).

Overview
--------

:adi:`CN0225` is a complete analog front end for digitizing +/-10 V industrial
level signals with a 16-bit differential input PulSAR ADC. The circuit
provides a high impedance instrumentation amplifier input with high CMR,
level shifting, attenuation, and differential conversion, with only two
analog components. The two active components which drive an :adi:`AD7687`
differential input 16-bit PulSAR ADC are the :adi:`AD8295` precision
instrumentation amplifier and the :adi:`AD8275` level translator/ADC driver.
An :adi:`ADR431` low noise 2.5 V XFET reference supplies the voltage
reference for the ADC.

The :adi:`AD8295` has two uncommitted on-chip signal processing amplifiers and
two precisely matched 20 k-ohm resistors in a small 4 mm x 4 mm package.

The :adi:`AD8275` is a G = 0.2 difference amplifier that can be used to
attenuate +/-10 V industrial signals, and the attenuated signal can be easily
interfaced to a single supply low voltage ADC. The :adi:`AD8275` performs the
attenuation and level shifting function in the circuit, maintaining good CMR
without any need for external components.

The CN0225 needs +15 V, -15 V and +6 V power supply inputs and thus requires
a triple output DC power supply. The board also connects to ADI's System
Demonstration Platform (SDP).

.. figure:: cn0225-hw-1024.jpg
   :align: center

   EVAL-CN0225-SDPZ evaluation board

Required Equipment
------------------

- :adi:`EVAL-CN0225-SDPZ <CN0225>` evaluation board
- :adi:`EVAL-SDP-CB1Z` controller board (SDP-B board)
- CN0225 Evaluation Software
- +/-25 V/1 A triple output DC power supply (Agilent E3631A or equivalent)
- Low distortion single-ended or differential signal source (Agilent 81150A
  or Audio Precision System Two 2322)
- USB cable
- PC with USB interface running Windows 7 or higher

Hardware Setup
--------------

Block Assignments
~~~~~~~~~~~~~~~~~

.. figure:: cn0225-hw-1024-edited.jpg
   :align: center

   EVAL-CN0225-SDPZ board layout

- The EVAL-CN0225-SDPZ (CN0225 Board) connects to the :adi:`EVAL-SDP-CB1Z`
  (SDP-B Board) via the 120-pin connector (SDP Conn).
- The :adi:`EVAL-SDP-CB1Z` (SDP-B Board) connects to the PC via the USB
  cable.
- Terminal block **J1** is the +/- analog signal input.
- Terminal block **J2** is the +6 V power supply input.
- Terminal block **J3** is the +/-15 V power supply input.
- Terminal block **J4** contains the test points for the SPI signals.

.. important::

   Connect the EVAL-CN0225-SDPZ and the SDP-B board, then power the
   EVAL-CN0225-SDPZ through the triple output power supply before connecting
   the SDP-B board to the PC.

Setup Block Diagram
~~~~~~~~~~~~~~~~~~~

.. figure:: cn0225-03-1024.png
   :align: center

   CN0225 setup block diagram

Jumper Settings
~~~~~~~~~~~~~~~

See the table below for the jumper settings. Values in red are the default
settings for the EVAL-CN0225-SDPZ.

.. figure:: 11-2-2017_3-45-44_pm.png
   :align: center

   EVAL-CN0225-SDPZ jumper settings table

Software Setup
--------------

Installing the Software
~~~~~~~~~~~~~~~~~~~~~~~~

#. Extract **CN0225 Evaluation Software** and open **setup.exe**.

   .. note::

      It is recommended to install the software to the default path
      ``C:\Program Files (x86)\Analog Devices\`` and all National Instruments
      products to ``C:\Program Files\National Instruments\``.

   .. figure:: 11-2-2017_3-51-12_pm.png
      :align: center

      CN0225 evaluation software setup wizard

#. Press **Next** to view the National Instruments Software License Agreement.

   .. figure:: 11-2-2017_3-52-02_pm.png
      :align: center

      National Instruments Software License Agreement

#. Select the option which **accepts** the License Agreement and press
   **Next** to view the installation review page.

   .. figure:: 11-2-2017_3-52-35_pm.png
      :align: center

      Installation review page

#. Press **Next** to start the installation.

   .. figure:: 11-2-2017_3-53-43_pm.png
      :align: center

      Installation progress

#. Upon completion of the CN0225 Evaluation Software installation, the
   installer for the ADI SDP Drivers will execute.

   .. note::

      It is recommended to close all other applications before clicking
      **Next**. This will make it possible to update relevant system files
      without having to reboot your computer.

   .. figure:: 11-2-2017_3-55-25_pm.png
      :align: center

      ADI SDP Drivers installer

#. Press **Next** to set the installation location for the SDP Drivers.

   .. note::

      It is recommended to install the drivers to the default path
      ``C:\Program Files\Analog Devices\SDP\Drivers``.

   .. figure:: 11-2-2017_3-54-25_pm.png
      :align: center

      SDP Drivers installation location

#. Press **Next** to install the SDP Drivers. When prompted by Windows
   Security, press **Install**.
#. Press **Finish** to complete the installation.

   .. figure:: 11-2-2017_3-55-36_pm.png
      :align: center

      SDP Drivers installation complete

#. (Optional) Restart the PC when prompted by the installer.

   .. figure:: 11-2-2017_3-56-02_pm.png
      :align: center

      System restart prompt

Using the Evaluation Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Main Window
^^^^^^^^^^^

.. figure:: 11-3-2017_3-29-38_pm_-_edited.png
   :align: center

   CN0225 evaluation software main window

The evaluation software main window provides the following controls and
indicators:

**Board Connection Control Section:**

- **Connect** button -- Starts the connection with the CN0225 evaluation
  board.
- **Disconnect** button -- Ends the connection with the CN0225 evaluation
  board.
- **STOP APP** button -- Exits the software application.

**Data Acquisition Control Section:**

- **Connector Select** -- Selects which 120-pin connection of the SDP-B
  board to use.
- **Fs (Hz)** field -- Sets the sampling frequency of the CN0225 ADC.
- **Samples** field -- Sets the number of samples the CN0225 ADC takes.
- **SCLK (Hz)** field -- Sets the SPI clock frequency used by the evaluation
  board.
- **Acquire Samples** button -- Commands the CN0225 ADC to sample at the set
  sampling frequency and read the set number of samples.
- **Save Data to File** button -- Saves the current sample readings to an
  output file.

**Activity Frame:**

- **Time Domain** tab -- Displays the measured ADC sample values vs. time
  plot.
- **Frequency Domain** tab -- Plots the FFT of the ADC samples with the
  amplitude in dB of the full scale ADC value.

.. figure:: 11-3-2017_3-30-08_pm_-_edited.png
   :align: center

   Frequency Domain tab - FFT plot of ADC samples

- **Histogram** tab -- Plots the number of occurrences of ADC sample values.

.. figure:: 11-3-2017_3-30-27_pm_-_edited.png
   :align: center

   Histogram tab - distribution of ADC sample values

- **S/W Version Info** tab -- Shows the software and hardware versions,
  vendor and product IDs.

  - **Flash LED** button -- Tests the SDP communication to the CN0225.
  - **Read Firmware** button -- Reads the current SDP firmware for debugging.

.. figure:: 11-3-2017_3-30-38_pm_-_edited.png
   :align: center

   S/W Version Info tab - software and hardware version details

Running the System
^^^^^^^^^^^^^^^^^^

#. Open the **CN0225.exe** application from the default installation
   location.
#. Set the correct connector and SCLK settings for the board in the Data
   Acquisition Control.
#. Click the **Connect** button.
#. Set the desired sampling frequency in Hz and the number of samples to
   read.
#. Click the **Acquire Samples** button.
#. Click the **Time Domain** tab to view the ADC sample values vs. time
   plot.
#. Click the **Frequency Domain** tab to view the FFT plot of the sample
   values.
#. Click the **Histogram** tab to view the number of occurrences of ADC
   sample values.
#. Click the **S/W Version Info** tab to view the hardware and software
   versions.
#. Click the **Save Data to File** button if you want to save the current
   sample readings.
#. Click the **Disconnect** button if finished.
#. Click the **STOP APP** button to exit the software.

Documents
---------

- :adi:`CN0225 Circuit Note <CN0225>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0225-SDPZ Design & Integration Files
   <https://www.analog.com/CN0225-DesignSupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - PADS Project

Additional Information
----------------------

- :adi:`AD7687 Product Page <AD7687>`
- :adi:`AD8295 Product Page <AD8295>`
- :adi:`AD8275 Product Page <AD8275>`
- :adi:`ADR431 Product Page <ADR431>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
