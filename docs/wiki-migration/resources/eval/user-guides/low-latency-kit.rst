Precision Low Latency Development Kit User Guide
================================================

| The :adi:`CN0577` is a 15 MSPS, 2 ppm linear data acquisition system with a medium impedance of 1.1 kΩ, easy to drive input, and is designed to provide analog front end and FMC digital interface for the :adi:`LTC2387-18` use successive approximation register (SAR) ADC. Unlike in existing FMC boards where the ADC encodes signals coming from the FPGA, the :adi:`CN0577` utilizes a sophisticated driver circuitry that allow analog inputs to be sampled and digitized directly by the LTC2387-18, without added noise or latency. This solution includes an on-board reference oscillator and a retiming circuit to minimize signal-to-noise ratio (SNR) degradation due to the FPGA additive jitter.
| The circuit is in FPGA FMC form factor, powered either from the FMC platform board or an external supply. The digital interface uses serial low voltage differential signaling (LVDS), minimizing the input/output requirements, and enabling easy integration with other FPGA designs. A separate data clock output eases the timing requirements of the host FPGA, thereby, allowing this board to be used conveniently within single-board systems or standalone operations. Additionally, this reference design includes a digital bus switch that offers power-down mode to reduce power consumption when some functions are unused.
| This board is also complete with Linux drivers and IIO software available to configure, read, and set analog input/output signals. These enable easy integration of both hardware and software to different applications.
| <<ADD in a PICTURE>> of the circuit block diagram, hardware image, or functional diagram. |image1|
| ===== Connectors and Jumper Configurations ===== Add any and all connectors and options that customers can talk to or configure. Explain pinouts, provide part numbers for sensors you used, any third party equipment you connected so customers can replicate the setup which you tested & verified on.
| ===== Power Supply Considerations and Configuration =====
| ===== Digital Interface =====
| ===== Analog Input =====
| ===== Power Supply Considerations and Configuration =====
| ===== System Setup =====

Equipment Required
------------------

**Hardware**
~~~~~~~~~~~~

-  EVAL-CN0577-FMCZ Circuit Evaluation Board
-  FPGA development board (such as ZedBoard)
-  Interposer board
-  12 V power supply
-  Host PC
-  16 GB or larger micro SD card
-  LAN cable
-  SMA cables
-  XLR cable
-  USB cable
-  Audio Precision audio analyzer for SNR,THD, SFDR analysis
-  Precision dc source/calibrator for noise test (Krohn-Hite 523 or similar)

**Software**

-  Analog Devices Kuiper Linux image

**Documentation**

-  :adi:`cn0577` Circuit Note

System Test Setup
-----------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0577/cn0577_test_setup.png
   :align: center
   :width: 600px

.. container:: center

   *<fc #c0c0c0>Figure x. EVAL-CN0577-FMCZ System Test Setup for SNR,THD, and SFDR Analysis</fc>*


Running the System
------------------

To set up the complete system, follow these steps:

-  Download and install the CN0577 evaluation board software on the PC.
-  Load the Analog Devices Kuiper Linux image onto the micro SD card.
-  Place the micro SD card into the ZedBoard.
-  Connect EVAL-CN0577-FMCZ to the ZedBoard through the FMC pin connector.
-  Connect the 12 V power supply jack on the ZedBoard.
-  Plug in the LAN cable from the ZedBoard to the PC.
-  Connect the EVAL-CN0577-FMCZ to the interposer board using the SMA cables.
-  Connect the interposer board to the Audio Precision audio analyzer through the XLR cable.
-  Connect the ground of the EVAL-CN0577-FMCZ to the Audio Precision audio analyzer.
-  Connect the Audio Precision audio analyzer USB cable to PC.
-  Run the CN0577 software and capture the resulting ADC data and FFT data.

Software Setup
^^^^^^^^^^^^^^

For the device to run, the SD card should be loaded with Analog Devices Kuiper Linux, a distribution based on Raspbian from the Raspberry Pi Foundation. It incorporates Linux device drivers for ADI products as well as tools and other software products designed and created with ease of use in mind. The reasoning behind creating this distribution is to minimize the barriers to integrating ADI hardware devices into a Linux-based embedded system.

Access to the embedded system can be through ​a remote PC connected ​either via LAN cable or Wi-Fi. ​

Downloading and Flashing Kuiper Linux Image on SD Card
------------------------------------------------------

In order to control the **EVAL-CN0577-RPIZ**, you will need to install ADI Kuiper Linux on an SD card. Complete instructions, including where to download the SD card image, how to write it to the SD card, and how to configure the system are provided at :doc:`Kuiper Images </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`. Write the image and follow the system configuration procedure.

.. image:: https://wiki.analog.com/_media/university/labs/software/iio_intro_toolbox/command_prompt.png
   :align: center
   :width: 400px

Configuring the SD Card for the CN0577
--------------------------------------

For the Linux kernel to identify the device connected to the expansion header, update the device tree overlay. A **Device Tree Overlay** contains information about additional connected hardware, the EVAL-CN0577-FMCZ for this case. The overlay file is already included in the SD card and just needs to be matched to the EVAL-CN0577-FMCZ.

Follow the Hardware Configuration procedure under **Preparing the Image: Raspberry Pi** in the :doc:`Kuiper Images </wiki-migration/resources/tools-software/linux-software/kuiper-linux>` page, substituting the following lines in **config.txt**:

This brings up the file in the terminal. Scroll down until the line that begins with "dtoverlay" is found; then, whatever it currently is, change it to:

::

   dtoverlay=rpi-cn0577

Save the file by Ctrl + X command. Reboot the system by typing on the command prompt:

::

   analog@analog:~$ sudo reboot

Graphical User Interface(GUI) and Example Python Scripts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are two main tools which a user has the option to interact with the EVAL-CN0577-FMCZ.

-  IIO Oscilloscope
-  Python (via Pyadi-iio)

Software Control and Diagnostics via IIO Oscilloscope
-----------------------------------------------------

TheEVAL-CN0577-FMCZ can be evaluated using IIO Oscilloscope. Customers can use the CN0511 plug-in tab, debug tab, and the DMM tab. Various controls and diagnostics are available in these plug-ins.

CN0577 IIO Oscilloscope Plug-in
"""""""""""""""""""""""""""""""

| 

Pyadi-IIO
---------

| :doc:`PyADI-IIO </wiki-migration/resources/tools-software/linux-software/pyadi-iio>` is a python abstraction module for ADI hardware with IIO drivers to make them easier to use. This module provides device-specific APIs built on top of the current libIIO python bindings. These interfaces try to match the driver naming as much as possible without the need to understand the complexities of libIIO and IIO.

Installation of Latest Lib-IIO and Other Requirements Needed to Run the Example
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

In order to run the current Python example a few additional steps need to occur.

.. important::

   
   Step 1: Installation of the latest
   
   ::
   
      git clone https://github.com/analogdevicesinc/libad9166-iio
   
   ::
   
      cd libad9166-iio
   
   ::
   
      cmake ./CMakeLists.txt
   
   ::
   
      make
   
   ::
   
      sudo make install
   
   ::
   
      cd bindings/python
   
   ::
   
      sudo pip install -r requirements_dev.txt
   
   ::
   
      cmake ./CMakeLists.txt
   
   ::
   
      sudo make
   
   ::
   
      sudo make install
   
   Step 2: Clone the latest pyadi-iio from github
   
   ::
   
      git clone https://github.com/analogdevicesinc/pyadi-iio
   
   Step 3: Installation of libatlas-base-dev linux packages
   
   ::
   
      sudo apt-get install libatlas-base-dev 
   
   Then choose 'Y' if were asked to continue.
   
   .. note::

      Enter the password “analog” whenever asked for it during the installation process

   


After all these requirements has been loaded in the Raspberry Pi, example found in ~/home/analog/pyadi-iio/examples for CN0511 can now be executed.

Running the Example
"""""""""""""""""""

This demo uses a PyADI-IIO example script. This scripts will show the single-tone frequency with calibrated output power in dBm. - -

Schematic, PCB Layout, Bill of Materials
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Download
   :class: download

   
   :adi:`EVAL-CN0xxx-ARDZ Design & Integration Files <cn0xxx-designsupport>`
   
   -  Schematics
   -  PCB Layout
   -  Bill of Materials
   -  Allegro Project
   -  <ADD other things specific to your project if desired>
   


Additional Information and Useful Links
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   * 

Reference Demos & Software
==========================

::

   * 

Hardware Registration
^^^^^^^^^^^^^^^^^^^^^

.. tip::

   Receive software update notifications, documentation updates, view the latest videos, and more when you register your hardware. `Register <https://form.analog.com/Form_Pages/FeedBack/EVAL-CN0577-FMCZ?&v=RevD>`__ to receive all these great benefits and more!


// End of Document //

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0577/cn0577_simplified_block_diagram.png
   :width: 600px
