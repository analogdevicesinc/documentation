.. _eval-ad7616-sdz quickstart sdp-k1:

SDP-K1 Quick Start Guide
===============================================================================

.. image:: ../images/ad7616_sdp-k1_setup.jpg
   :width: 800

.. esd-warning::

This guide provides quick instructions on how to setup the
:adi:`EVAL-AD7616SDZ` on:

- :adi:`SDP-K1` using a fly-wire SPI connection

Using no-OS as software
-------------------------------------------------------------------------------

Necessary files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following files are needed:

- no-OS project: :git-no-OS:`projects/ad7616-st`

Instructions on how to build the project from source can be found here:

- :external+no-OS:doc:`build_guide`

Required software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- AMD Xilinx Vitis or STM32CubeIDE — see the :external+no-OS:doc:`build_guide`
  for the supported toolchain
- A UART terminal (Putty/Tera Term/Minicom, etc.) with baud rate 230400 (8N1)
- (Optional) `IIO Oscilloscope <https://analogdevicesinc.github.io/documentation/software/iio-oscilloscope/>`__
  to visualize the captured data over the IIO serial backend

Required hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :adi:`SDP-K1` microcontroller board and its power supply
- :adi:`EVAL-AD7616SDZ` evaluation board and its power supply
- STLINK-V3 programmer
- Fly-wires for SPI connections

More details as to why you need these, can be found at
:ref:`eval-ad7616-sdz prerequisites`.

Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Creating the setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Follow the steps in this order, to avoid damaging the components:

#. Configure the EVAL-AD7616-SDZ jumpers as follows for the SDP-K1:

   .. list-table::
      :header-rows: 1

      * - Jumper/Solder link
        - Position
        - Description
      * - SL1
        - Unmounted
        - Channel Sequencer Enable
      * - SL2
        - Unmounted
        - RC Enable Input
      * - SL3
        - Unmounted
        - Selects 1 MISO mode
      * - SL4
        - Unmounted
        - Oversampling Ratio Selection OS2
      * - SL5
        - Mounted
        - If mounted, selects serial interface
      * - SL6
        - Unmounted
        - Oversampling Ratio Selection OS1
      * - SL7
        - Unmounted
        - Oversampling Ratio Selection OS0
      * - LK40
        - A
        - Onboard 5V power supply selected
      * - LK41
        - A
        - Onboard 3.3V power supply selected

#. Connect the :adi:`EVAL-AD7616SDZ` to the :adi:`SDP-K1` Arduino header
   using fly-wires as follows:

   .. list-table::
      :header-rows: 1

      * - EVAL-AD7616-SDZ
        - SDP-K1 Arduino
      * - SCLK
        - D13
      * - DB10/SDI
        - D11
      * - DB12/SDOA
        - D12
      * - CS
        - D10
      * - CONVST
        - D5
      * - RESET
        - D7
      * - BUSY
        - D6

#. Connect the power supply to the :adi:`EVAL-AD7616SDZ` barrel jack
#. Connect the power supply to the :adi:`SDP-K1` barrel jack
#. Connect the STLINK-V3 programmer to the :adi:`SDP-K1` and to your host PC
#. Connect a USB cable for UART from the :adi:`SDP-K1` to your host PC
#. Build and flash the no-OS project:

   #. Refer to the :external+no-OS:doc:`build_guide` for toolchain setup.
   #. Clone the no-OS repository and navigate to the project:

      .. code-block:: bash

         $ git clone --recursive https://github.com/analogdevicesinc/no-OS.git
         $ cd no-OS/projects/ad7616-st

   #. Build and flash the project:

      .. code-block:: bash

         $ make reset
         $ make
         $ make run

      To debug instead of flash:

      .. code-block:: bash

         $ make debug

#. Connect to the IIO server running on the SDP-K1:

   - **IIO Oscilloscope**: connect using the serial backend at
     ``serial:/dev/ttyUSB0,230400`` (or the appropriate COM port on Windows)
   - **UART terminal**: open at **230400** baud to view the console log

.. warning::

   Make sure to power both the :adi:`EVAL-AD7616SDZ` and the :adi:`SDP-K1`
   via their respective barrel jack connectors.

.. TODO: uncomment when no-OS boot log is available
.. Console output
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
..
.. The project launches an IIO server on the SDP-K1. After connecting via
.. IIO Oscilloscope or ``iio_info -u serial:/dev/ttyUSB0,230400``, the AD7616
.. channels become available for data capture and visualization.
..
.. The following is what is printed in the serial console when the application
.. starts:
..
.. .. collapsible:: Complete console log
..
..    ::
..
..       .. TODO: Paste the complete console output here.
