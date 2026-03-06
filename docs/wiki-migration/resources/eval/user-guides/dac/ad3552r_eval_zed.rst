EVAL-AD3552R Evaluation Board on ZedBoard User Guide
====================================================

**Evaluation Board for the AD3552R, 16-Bit, 2-Channel, Current Output DAC**


|eval-ad3552rfmcxztop-web.gif|

Features
--------

-  Full featured evaluation board for the :adi:`AD3552R`
-  Available in two transimpedance amplifier options
-  Selectable transimpedance gain
-  On-board or external power supply
-  On-board or external voltage reference
-  Clock and trigger inputs for external synchronization
-  Is supported on `ZedBoard <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`__

Evaluation Kit Contents
-----------------------

-  :adi:`EVAL-AD3552R`

Hardware Required
-----------------

-  16GB (or larger) Class 10 (or faster) micro-SD card
-  `ZedBoard <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`__ Rev D or later board
-  12Vdc, 3A power supply
-  Micro-USB cable
-  Ethernet cable
-  An oscilloscope( In this demo ADALM 2000 is used)
-  User interface setup (choose one):

   -  HDMI monitor, keyboard, and mouse plugged directly into the Zedboard
   -  Host Windows/Linux/Mac computer on the same network as the Zedboard

Software Required
-----------------

-  You need a Host PC (Windows or Linux)
-  A UART terminal (Putty/Tera Term/Minicom, etc.), Baud rate 115200 (8N1)
-  IIO Scope Download
-  :doc:`Kuiper Linux Image </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`

General Description
-------------------

| The EVAL-AD3552RFMCxZ is an evaluation board for the AD3552R ultrafast 16-bit precision DAC. The board is available in two variants: EVAL-AD3552RFMC1Z is optimized for high speed, intended to reproduce dynamic specifications shown in the datasheet; EVAL-AD3552RFMC2Z is optimized for DC precision and has a much lower bandwidth, intended to reproduce DC electrical specifications shown in the datasheet. The difference between these boards is the transimpedance amplifier and its corresponding feedback capacitor.
|

.. tip::

   For more informations about hardware specifications, see the :doc:`EVAL-AD3552R Evaluation Board User Guide </wiki-migration/resources/eval/user-guides/dac/eval-ad3552r>` page.


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

.. important::

   At the moment the AD3552R-EVB is not yet supported in the latest Kuiper Image so these `boot files <https://wiki.analog.com/_media/resources/eval/user-guides/dac/ad3552r/ad3552r-boot-files-2025-02-27.zip>`__ should be used.


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

| |iio_connect.png|

-  Once connected it is possible to set voltage raw values as below:

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-drivers/iio-dac/ad3552r/output_raw_1_.png
   :alt: output_raw_1\_.png
   :align: center
   :width: 700px

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

|

.. important::

   Cyclic mode is actually not enabled by defualt, please edit the file **examples/ad3552r_example.py** and set:

   | dev.tx_cyclic_buffer = True
   


::

   D:\pyadi-iio>export PYTHONPATH=D:/pyadi-iio/ 
   D:\pyadi-iio>python examples/ad3552r_example.py ip:your_board_ip

Press enter and you will get these readings:

::

   $ python examples/ad3552r_example.py ip:your_board_ip
   uri: ip:your_board_ip
   sample rate: 33333333
   Sample data min: 1
   Sample data max: 65534

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

.. |eval-ad3552rfmcxztop-web.gif| image:: https://wiki.analog.com/_media/resources/eval/eval-ad3552rfmcxztop-web.gif
   :width: 400px
.. |zedboard.png| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/AD777x-ARDZ/zedboard.png
   :width: 600px
.. |jumpers_boot_sd_zedboard.jpg| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dac/ad3552r_eval_zed/jumpers_boot_sd_zedboard.jpg
   :width: 400px
.. |iio_connect.png| image:: https://wiki.analog.com/_media/resources/tools-software/linux-drivers/iio-dac/ad3552r/iio_connect.png
   :width: 700px
