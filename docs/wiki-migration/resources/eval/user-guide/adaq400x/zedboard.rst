Evaluating the ADAQ4001/ADAQ4003 16-/18-Bit, 2 MSPS, µModule® Data Acquisition Solution using Zedboard
======================================================================================================

Features
--------

-  Fully-featured Pmod™ evaluation board with a Pmod™-to-FMC interposer board
-  Versatile analog signal conditioning circuitry
-  On-board reference and ADC drivers
-  PC software for control and data analysis of time and frequency domain
-  Is supported on `ZedBoard <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`__

Evaluation Kit Contents
-----------------------

-  :adi:`EVAL-ADAQ4001PMDZ <eval-adaq40xx>` or :adi:`EVAL-ADAQ4003PMDZ <eval-adaq40xx>` Pmod™ evaluation board
-  :adi:`EVAL-PMD-IB1Z Pmod™ <eval-adaq40xx>` to FMC interposer board

Hardware Required
-----------------

-  `ZedBoard <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`__ Rev D or later board

   -  16GB (or larger) Class 10 (or faster) micro-SD card
   -  12Vdc, 3A power supply
   -  Standard USB A to Micro USB cable
   -  Ethernet cable

-  User interface setup (choose one):

   -  HDMI monitor, keyboard, and mouse plugged directly into the `ZedBoard <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`__
   -  Host Windows/Linux/Mac computer on the same network as the `ZedBoard <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`__

-  Precision signal source
-  Cable (SMB input to evaluation board)
-  Band-pass filter suitable for 16-bit/18-bit testing (value based on signal frequency)

Software Required
-----------------

-  You need a Host PC (Windows® 10 or Linux)
-  A UART terminal (Putty/Tera Term/Minicom, etc.), Baud rate 115200 (8N1)
-  IIO Scope Download
-  :doc:`Kuiper Linux Image </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`

General Description
-------------------

The :adi:`ADAQ4001` and :adi:`ADAQ4003` µModule® data acquisition system evaluation kit (:adi:`EVAL-ADAQ4001FMCZ <eval-adaq40xx>` / :adi:`EVAL-ADAQ4003FMCZ <eval-adaq40xx>`) contains the EVAL-ADAQ4001PMDZ or EVAL-ADAQ4003PMDZ peripheral module (Pmod™) board and the EVAL-PMD-IB1Z Pmod™ to field programmable grid array (FPGA) mezzanine card (FMC) interposer board that ``interfaces with the system demonstration controller board (EVAL-SDP-CH1Z) via a 160-pin FMC connector, as shown in Figure 1.``

The ADAQ4001 µModule and the ADAQ4003 µModule combine multiple common signal processing and conditioning blocks into a single device that includes a low noise, fully differential analog-to-digital converter (ADC) driver, a stable reference buffer, a high resolution, 16-bit or 18-bit, 2 MSPS successive approximation register (SAR) ADC, and the critical passive components necessary for optimum performance.

The EVAL-ADAQ4001PMDZ and the EVAL-ADAQ4003PMDZ on-board components include the following:

-  The :adi:`ADR4550` high precision, buffered band gap, 5.0 V voltage reference (see Figure 25)
-  An optional :adi:`ADA4898-1` high voltage, low noise, low distortion, unity-gain stable, high speed op amp (see Figure 26)
-  An optional :adi:`AD8251` programmable gain in-amp (see Figure 26)
-  The :adi:`LT5400-4` quad matched, low drift, resistor network

Note that J1 and J2 on the EVAL-ADAQ4001PMDZ and the EVAL-ADAQ4003PMDZ provide low noise analog signal sources.

.. tip::

   The datasheet provides a full description and complete specifications of the :adi:`ADAQ4001` / :adi:`ADAQ4003`. Consult it in conjunction with this user guide when using the :adi:`EVAL-ADAQ4001FMCZ <eval-adaq40xx>` / :adi:`EVAL-ADAQ4003FMCZ <eval-adaq40xx>`.


FIXME

.. important::

   INSERT BOARD PHOTO HERE


FIXME

Quick Start Guide
-----------------

Loading Image on SD Card
~~~~~~~~~~~~~~~~~~~~~~~~

To boot the Zedboard and control the :adi:`EVAL-AD3552R`, you will need to install ADI Kuiper Linux on an SD card. Complete instructions, including where to download the SD card image, how to write it to the SD card, and how to configure the system are provided on the :doc:`Kuiper Linux page </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`.

Configuring the SD Card
~~~~~~~~~~~~~~~~~~~~~~~

Follow the configuration procedure under **Configuring the SD Card for FPGA Projects** on the :doc:`Kuiper Linux </wiki-migration/resources/tools-software/linux-software/kuiper-linux>` page. Copy the following files onto the boot directory to configure the SD card:

-  **uImage** file for Zynq
-  **BOOT.BIN** specific to your :adi:`EVAL-AD3552R` + ZedBoard
-  **devicetree.dtb** for Zynq specific to your :adi:`EVAL-AD3552R` + ZedBoard

Setting up the Hardware
~~~~~~~~~~~~~~~~~~~~~~~

You will need to:

-  Get the `ZedBoard <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`__.


|zedboard.png|

-  Insert the SD-CARD into the SD Card Interface Connector (J12).
   \* Connect the :adi:`EVAL-AD3552R` board into the ZedBoard FMC connector.
   \* Connect USB UART J14 (Micro USB) to your host PC.
   \* Plug your ethernet cable into the RJ45 ethernet connector(J11).
   \* Plug the Power Supply into the 12V Power input connector (J20) (DO NOT turn the device on).
   \* Set the jumpers as seen in the below picture:

   |jumpers_boot_sd_zedboard.jpg|

.. tip::

   Before executing the below steps, make sure that VADJ jumper is set to 1.8V.


\* Connect the oscilloscope probes to the SMB connectors.
   \* Turn it on.
   \* Wait ~30 seconds for the “DONE” LED to turn blue. This is near the DISP1.

::

   {{  resources:eval:user-guides:dac:ad3552r_eval_zed:setup_diagram_eval_ad3552r.jpg?800 }}

.. esd-warning::


Application Software (both locally and remotely on the FPGA)
------------------------------------------------------------

Hardware Connection
~~~~~~~~~~~~~~~~~~~

The Libiio is a library used for interfacing with IIO devices and is required to be installed on your computer.

.. admonition:: Download
   :class: download

   Download and Install the latest :git-libiio:`Libiio package <releases>` on your machine.


To be able to connect your device, the software must be able to create a context. The context creation in the software depends on the backend used to connect to the device as well as the platform where the :adi:`EVAL-AD3552R` is attached. The Zedboard running ADI Kuiper Linux is currently the only platform supported for the :adi:`EVAL-AD3552R`. The user needs to supply a **URI** which will be used in the context creation.

The :doc:`iio_info </wiki-migration/resources/tools-software/linux-software/libiio/iio_info>` command is a part of the libIIO package that reports all IIO attributes.

| Upon installation, simply enter the command on the terminal command line to access it.

For FPGA(Zedboard) Direct Local Access:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   iio_info

For Windows machine connected to an FPGA(Zedboard):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   iio_info -u ip:<ip address of your ip>

Example:

-  If your Zedboard has the IP address 169.254.92.202, you have to use *iio_info -u ip::169.254.92.202* as your URI

.. note::

   Do note that the Windows machine and the FPGA board should be connected to the same network for the machine to detect the device.


IIO Oscilloscope
~~~~~~~~~~~~~~~~

.. important::

   Make sure to download/update to the latest version of IIO-Oscilloscope found on this link\ :git-iio-oscilloscope:`releases\`


-  Once done with the installation or an update of the latest IIO-Oscilloscope, open the application. The user needs to supply a URI which will be used in the context creation of the IIO Oscilloscope and the instructions can be seen in the previous section.
-  Press refresh to display available IIO Devices and press connect.

|iio_connect.png|

-  Select the desired input source for the AD3552R device (Available options for AD3552R-EVAL are ramp_input and dma_input).

|input_source_selection_ad3552r.jpg|

.. important::

   Even if the input source is set to ramp_input the steps regarding the DAC Data Management tab have to be followed.


-  Select the desired input source for the AD3552R device.



|output_range_selection_ad3552r.jpg|

.. warning::

   Make sure you don't try to read/write the output_range attribute when the stream_status is in start_stream or start_stream_synced.


-  From the DAC Data Manager Window select the output channels of the DAC and enable the cyclic buffer.
-  Load an example file from the IIO Oscilloscope/lib/osc/waveforms folder.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/dac/ad3552r_eval_zed/dac_data_management_ad3552r.jpg
   :alt: dac_data_management_ad3552r.jpg
   :align: center
   :width: 700px

-  Click on the load button.
-  Select the stream_status IIO Attribute and start the stream.

|stream_status_iio_ad3552r.jpg|

.. important::

   Please note that for the AD3552R-EVAL board, the start_stream_synced feature is not supported.


-  After the stream_status has been written and the input source is set to dma_input you should see the following capture on the oscilloscope:



|captured_data_ad3552r.jpg|

PyADI-IIO
~~~~~~~~~

| :doc:`PyADI-IIO </wiki-migration/resources/tools-software/linux-software/pyadi-iio>` is a Python abstraction module for ADI hardware with IIO drivers to make them easier to use. This module provides device-specific APIs built on top of the current libIIO Python bindings. These interfaces try to match the driver naming as much as possible without the need to understand the complexities of libIIO and IIO.
| Follow the step-by-step procedure on how to install, configure, and set up PYADI-IIO and install the necessary packages/modules needed by referring to this :doc:`link </wiki-migration/resources/tools-software/linux-software/pyadi-iio>`.

Running the example
^^^^^^^^^^^^^^^^^^^

.. admonition:: Download
   :class: download

   Github link for the Python sample script: :git-pyadi-iio:`AD3552R-EVAL Python Example <examples/ad3552r_example.py>`


After installing and configuring PYADI-IIO on your machine, you are now ready to run Python script examples. In our case, run the **ad3552r_example.py** found in the examples folder.

::

   D:\pyadi-iio>export PYTHONPATH=D:/pyadi-iio/ 
   D:\pyadi-iio>python examples/ad3552r_example.py ip:your_board_ip

Press enter and you will get these readings:

::

   $ python examples/ad3552r_example.py ip:your_board_ip
   uri: ip:your_board_ip
   sample rate: 16666667
   Sample data min: 0
   Sample data max: 64712
   output_range:dac: -10/+10V
   input_source:dac: dma_input

The following window will pop up:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/dac/ad3552r_eval_zed/python_plot_ad3552r.jpg
   :alt: python_plot_ad3552r.jpg
   :align: center
   :width: 700px

Schematic, PCB Layout, Bill of Materials
========================================

.. admonition:: Download
   :class: download

   
   -  `EVAL-AD3552RFMC1Z <https://wiki.analog.com/_media/resources/eval/eval-ad3552rfmc1z.pdf>`__
   -  `EVAL-AD3552RFMC2Z <https://wiki.analog.com/_media/resources/eval/eval-ad3552rfmc2z.pdf>`__
   -  `EVAL-AD3552RFMCxZ Gerber Files <https://wiki.analog.com/_media/resources/eval/eval_ad3552rfmcxz_gerber_files.zip>`__
   -  `EVAL-AD3552RFMC1Z Bill of Materials <https://wiki.analog.com/_media/resources/eval/eval-ad3552rfmc1z.xlsx>`__
   -  `EVAL-AD3552RFMC2Z Bill of Materials <https://wiki.analog.com/_media/resources/eval/eval-ad3552rfmc2z.xlsx>`__
   


Reference Demos & Software
--------------------------

-  :git-pyadi-iio:`PyADI-IIO sources for the EVAL-AD3552R board. <examples/ad3552r_example.py>`
-  :doc:`Dual Channel, 16-Bit, 33 MUPS, Multispan, Multi-IO SPI DAC Linux device driver. </wiki-migration/resources/tools-software/linux-drivers/iio-dac/axi-ad3552r>`
-  :doc:`AXI-AD3552R HDL IP. </wiki-migration/resources/fpga/docs/axi_ad3552r>`
-  `pyADI-IIO <https://github.com/analogdevicesinc/pyadi-iio>`__
-  :doc:`PyADI-IIO Installation Guide </wiki-migration/resources/tools-software/linux-software/pyadi-iio>`
-  :doc:`IIO Oscilloscope Installation Guide </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`
-  :doc:`Kuiper Linux </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`

.. |zedboard.png| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/AD777x-ARDZ/zedboard.png
   :width: 600px
.. |jumpers_boot_sd_zedboard.jpg| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dac/ad3552r_eval_zed/jumpers_boot_sd_zedboard.jpg
   :width: 400px
.. |iio_connect.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dac/ad3552r_eval_zed/iio_connect.png
   :width: 700px
.. |input_source_selection_ad3552r.jpg| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dac/ad3552r_eval_zed/input_source_selection_ad3552r.jpg
   :width: 700px
.. |output_range_selection_ad3552r.jpg| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dac/ad3552r_eval_zed/output_range_selection_ad3552r.jpg
   :width: 700px
.. |stream_status_iio_ad3552r.jpg| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dac/ad3552r_eval_zed/stream_status_iio_ad3552r.jpg
.. |captured_data_ad3552r.jpg| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dac/ad3552r_eval_zed/captured_data_ad3552r.jpg
