|

.. important::

   THIS IS A TEMPLATE.

   
   THE GOAL IS TO CREATE A DOCUMENT CUSTOMERS WILL USE WHEN GETTING THEIR CFTL UP AND RUNNING, SO THEY DON'T ASK YOU SO MANY QUESTIONS. IT'S DESIGNED TO HELP YOU GET STARTED WRITING YOUR HARDWARE USER GUIDE.
   
   ALL OF THE CONTENT IS PLACEHOLDER INFORMATION, SO YOU WILL NEED TO POPULATE RELEVANT INFORMATION TO YOUR CFTL. SOME(OR SEVERAL) OF THE SECTION HEADERS MAY NOT APPLY TO YOU, SIMPLY REMOVE THEM. ALSO I MAY NOT HAVE CAPTURED EVERYTHING RELATIVE TO YOUR BOARD, SO ADDING INFORMATION IS ACCEPTABLE.
   
   DON'T FORGET TO CREATE A MEDIA FOLDER SPECIFIC TO YOUR CN NUMBER FOR ANY IMAGES, FILES, OR DOCUMENTS YOU WISH TO INCLUDE. THIS WILL HELP US KEEP THE WIKI ORGANIZED AND ENSURE YOUR CONTENT DOESN'T GET REMOVED.


EVAL-CN0xxx-ARDZ User Guide
===========================

:adi:`CN0xxx` Copy the first couple of paragraphs from the CN here. Ensure to hyper link products used. For examples :adi:`adr3433` and :adi:`ad7124-8`.

| Add in any other details you want as well.
| **<<ADD in a PICTURE>>** of the circuit block diagram, hardware image, or functional diagram. Please be sure to make the proper directory for images and other files related to this CN. If you need help doing so, please look online at Doku Wiki tutorials or ask someone who has done it before.

Input and Output Connections and Configurations
-----------------------------------------------

Add any and all connectors and options that customers can configure or interface with. analog inputs/outputs connectors digital inputs/outputs connectors jumper configurations (for analog and digital signals) etc.

Explain pinouts, provide part numbers for sensors you used, any tables for input/output configurations, and anything else a user needs to know when setting up the hardware

I/O Connector #1 (P?)
~~~~~~~~~~~~~~~~~~~~~

Place your 1st analog or digital connector in this section. Typically analog inputs are first and then flow to the digital next.

Jumper Selection
^^^^^^^^^^^^^^^^

This could be a requirement for the input range or something, just make sure you provide details on how to use the I/O connector.

I/O Connector #2 (P?)
~~~~~~~~~~~~~~~~~~~~~

Place your 2nd analog or digital connector in this section. Typically analog inputs are first and then flow to the digital next.

Jumper Configuration
^^^^^^^^^^^^^^^^^^^^

This could be a requirement for the input range or something, just make sure you provide details on how to use the I/O connector.

I/O Connector #3 (P?)
~~~~~~~~~~~~~~~~~~~~~

Place your 2nd analog or digital connector in this section. Typically analog inputs are first and then flow to the digital next.

.. _jumper-configuration-1:

Jumper Configuration
^^^^^^^^^^^^^^^^^^^^

This could be a requirement for the input range or something, just make sure you provide details on how to use the I/O connector.

Other Remaining Analog/Digital Input/output Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Your board may be more or less complicated, so just ensure that you talked about everything that a customer would want to know about and change.

LED Indicators
~~~~~~~~~~~~~~

Does your board have LEDs, buzzer, or other easy to read indicators? If yes what do they indicate? Power good? Data transfer? Faults? Alarms? Tell your customer what they mean.

Switches and Buttons
~~~~~~~~~~~~~~~~~~~~

Are there any switches or reset buttons, describe them.

Host Processor Connector
~~~~~~~~~~~~~~~~~~~~~~~~

FMC, Arduino, RPI, PMOD, SDP, Other pinout of the

Chip Select
^^^^^^^^^^^

If you have a selectable digital communication signal make mention of that

Power Supply Considerations and Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

How is your board powered? What is the voltage and current needed? Do you need a separate supply? Is it USB? Are there any configuration options that need to be talked about.

Device Driver Support
---------------------

There are two device driver solutions that are provided for controlling the **EVAL-CN0552-PMDZ** using the no-OS device driver on the **EVAL-ADICUP3029** platform and Linux device driver on the **Raspberry Pi** platform.

-  **EVAL-ADICUP3029**

   -  The ADICUP3029 example application uses the :doc:`AD7746 no-OS driver </wiki-migration/resources/tools-software/uc-drivers/ad7746>` and emulates the Linux IIO framework through the `tinyiiod daemon library <https://github.com/analogdevicesinc/libtinyiiod>`__. The application communicates with the host computer via the serial backend, over a USB-UART physical connection. This facilitates rapid application development on a host computer, independent from embedded code development.

-  **Raspberry Pi**

   -  The :doc:`Linux driver </wiki-migration/resources/tools-software/linux-drivers/iio-cdc/ad7745>` uses the Industrial Input/Output (IIO) framework, greatly simplifying the development of application code via the cross-platform Libiio library, which is written in C and includes bindings for Python, MATLAB, C#, and other languages. Application code can run directly on the platform board, communicating with the device over the local backend, or from a remote host over the network or USB backends.

System Setup Using ADICUP3029
-----------------------------

The \*\* EVAL-CN0552-PMDZ \*\* can be used with :doc:`ADICUP3029 </wiki-migration/resources/eval/user-guides/eval-adicup3029>`. Here is a video on how to use the CN0552 with the ADICUP3029:

.. container:: center round box


|youtube>6yjW-1EjQ0I|

Demo Requirements
~~~~~~~~~~~~~~~~~

The following is the list of items needed in order to replicate this demo.

-  \*\* Hardware \*\*

   -  :adi:`EVAL-ADICUP3029`
   -  :adi:`EVAL-CN0552-PMDZ <CN0552>`
   -  Two 2pF ceramic capacitors
   -  Micro-USB to USB Cable
   -  PC or Laptop with USB Port

-  \*\* Software \*\*

   -  :git-no-OS:`ADuCM3029_demo_cn0552.hex <releases/download/Latest/cn0552.zip>`

.. note::

   
   There are two basic ways to program the ADICUP3029 with the software for the CN0552.
   
   -  Dragging and Dropping the .Hex to the Daplink drive
   
      -  Using the drag and drop method, the software is going to be a version that Analog Devices creates for testing and evaluation purposes. This is the **EASIEST** way to get started with the reference design.
   
   -  Building, Compiling, and Debugging using CCES
   
      -  Importing the project into :adi:`CrossCore Embedded Studio <en/design-center/evaluation-hardware-and-software/software/adswt-cces.html>` is going to allow you to change parameters and customize the software to your application, but will be a bit more advanced and will require you to download the CrossCore toolchain.
   


.. admonition:: Download
   :class: download

   
   The software for the **ADICUP3029_CN0552** demo can be found here:
   
   Prebuilt CN0552 Hex File
   
   -  :git-no-OS:`ADuCM3029_demo_cn0552.hex <releases/download/Latest/cn0552.zip>`
   
   Complete CN0552 Source Files
   
   -  :git-no-OS:`ADuCM3029_demo_cn0552 Source Code <projects/cn0552>`
   


Setting up the Hardware
~~~~~~~~~~~~~~~~~~~~~~~

-  Connect **EVAL-CN0552-PMDZ** board at connector **P9** of the **EVAL-ADICUP3029**.
-  Connect a micro-USB cable to the P10 connector of the EVAL-ADICUP3029 and connect it to a computer. The final setup should look similar to the picture below.

|pmod-toadicup.png|

.. container:: center

   *<fc>Figure 5. Hardware Setup</fc>*


-  Make sure the following switches are as shown from the table below.



|switch_config.png|

.. container:: center

   
   *<fc>Figure 6. Switch Confuguration</fc>*


-  From your PC, open My Computer and look for the DAPLINK drive, if you see this then the drivers are complete and correct.



|image1|

.. container:: center

   
   *<fc>Figure 7. DAPLINK Drive</fc>*


-  Simply extract the provided zip file. Once extracted, you will see the pre-built hex file for the CN0552 demo. Then drag and drop this Hex file to the DAPLINK drive and your ADICUP3029 board will be programmed. The DS2 (red) LED will blink rapidly.
-  The DS2 will stop blinking and will stay ON once the programming is done.
-  For demo purposes, place a 2 pF capacitor between the EXCA pin and the CIN1(+) pin on the PMOD board. This will be your first channel. Then, place another 2 pF capacitor between EXCB pin and the CIN2(+) pin on the PMOD board. This will be your second channel.

System Setup Using Raspberry Pi
-------------------------------

The \*\* EVAL-CN0552-PMDZ \*\* can be used with a Raspberry Pi.

.. _demo-requirements-1:

Demo Requirements
~~~~~~~~~~~~~~~~~

The following is a list of items needed in order to replicate this demo.

-  **Hardware**

   -  :adi:`EVAL-CN0552-PMDZ <CN0552>`
   -  :adi:`PMOD to Raspberry Pi Adapter (PMD-RPI-INTZ) <PMD-RPI-INTZ>`
   -  Raspberry PI Zero, Zero W, 3B+, or 4
   -  16GB (or larger) Class 10 (or faster) micro-SD card
   -  5Vdc, 2.5A power supply with micro USB connector (USB-C power supply for Raspberry Pi 4)
   -  User interface setup (choose one):

      -  HDMI monitor, keyboard, mouse plugged directly into Raspberry Pi
      -  Host Windows/Linux/Mac computer on the same network as Raspberry Pi

-  **Software**

   -  :doc:`Kuiper Linux Image </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`

Loading Image on SD Card
~~~~~~~~~~~~~~~~~~~~~~~~

In order to boot the Raspberry Pi and control the **EVAL-CN0552-PMDZ**, you will need to install ADI Kuiper Linux on an SD card. Complete instructions, including where to download the SD card image, how to write it to the SD card, and how to configure the system are provided on the :doc:`Kuiper Linux page </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`.

Configuring the SD Card
~~~~~~~~~~~~~~~~~~~~~~~

Follow the configuration procedure under **Configuring the SD Card for Raspberry Pi Projects** on the :doc:`Kuiper Linux </wiki-migration/resources/tools-software/linux-software/kuiper-linux>` page, substituting the following lines in **config.txt**:

::

   dtoverlay=rpi-cn0552

.. _setting-up-the-hardware-1:

Setting up the Hardware
~~~~~~~~~~~~~~~~~~~~~~~

To set up the circuit for evaluation, consider the following steps:

-  Connect the P9 of the **PMOD to Raspberry Pi Interposer** board at the male header GPIO pin connector of the **Raspberry Pi** as shown below.


|image2|

-  Connect the \*\* :adi:`EVAL-CN0552-PMDZ <CN0552>` \*\* on the PMOD to Raspberry Pi Interposer board either via Port P3 or P4.

|image3|

-  Burn the SD card with the proper ADI Kuiper Linux image. Insert the burned SD card on the designated slot on the RPi.
-  Connect the system to a monitor using an HDMI cable through the mini HDMI connector on the RPi.
-  Connect a USB keyboard and mouse to the RPi through the USB ports.
-  Power on the RPi board by plugging in a 5V power supply with a micro-USB connector. The final setup should look similar to the picture below.

::

   {{ :resources:eval:user-guides:circuits-from-the-lab:cn0552:overall_setup.png?600 | }}

Application Software (both ADICUP3029 and Raspberry Pi)
-------------------------------------------------------

Hardware Connection
~~~~~~~~~~~~~~~~~~~

The Libiio is a library used for interfacing with IIO devices and is required to be installed on your computer.

.. admonition:: Download
   :class: download

   Download and Install the latest :git-libiio:`Libiio package <releases>` on your machine.


To be able to connect your device, the software must be able to create a context. The context creation in the software depends on the backend used to connect to the device as well as the platform where the EVAL-CN0552-PMDZ is attached. Two platforms are currently supported for the CN0552: Raspberry Pi using the ADI Kuiper Linux and the ADICUP3029 running the no-OS AD7746 demo project. The user needs to supply a **URI** which will be used in the context creation.

The :doc:`iio_info </wiki-migration/resources/tools-software/linux-software/libiio/iio_info>` command is a part of the libIIO package that reports all IIO attributes.


| Upon installation, simply enter the command on the terminal command line to access it.

For RPI Direct Local Access:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   iio_info

For Windows machine connected to Raspberry Pi:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   iio_info -u ip:<ip address of your ip>

Example:

-  If your Raspberry Pi has the IP address 192.168.1.7, you have to use *iio_info -u ip::192.168.1.7* as your URI

.. note::

   Do note that the Windows machine and the RPI board should be connected to the same network in order for the machine to detect the device.


For Windows machine connected to ADICUP3029:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   iio_info -u serial:<serial port>

Examples:

-  In a Windows machine, you can check the port of your ADICUP3029 via Device Manager in the Ports (COM & LPT) section. If your device is in COM4, you have to use *iio_info -u serial:COM4* as your URI.
-  In a Unix-based machine, you will see it under the /dev/ directory in this format "ttyUSBn", where n is a number depending on how many serial USB devices attached. If you see that your device is ttyUSB0, you have to use serial:/dev/ttyUSB0 as your URI.

IIO Commands
~~~~~~~~~~~~

There are different commands that can be used to manage and control the device being used. The :doc:`iio_attr </wiki-migration/resources/tools-software/linux-software/libiio/iio_attr>` command reads and writes IIO attributes.

::

   analog@analog:~$ iio_attr [OPTION]...

Example:

-  To look at the context attributes, enter this code on the terminal:

::

   analog@analog:~$ iio_attr -a -C

|

| The :doc:`iio_reg </wiki-migration/resources/tools-software/linux-software/libiio/iio_reg>` command reads or writes SPI or I2C registers in an IIO device. This is generally not needed for end applications, but can be useful in debugging drivers. Note that you need to specify a context using the *-u* qualifier when you are not directly accessing the device via RPI or when you are using the ADICUP3029 platform.

::

   analog@analog:~$ iio_reg -u <context> <device> <register> [<value>]

Example:

-  To to read the device ID (register = 0x02) of an AD7746 interfaced via RPI from a Windows machine, enter the following code on the terminal:

::

   iio_reg -u ip:<ip address> ad7746 0x02

| 

IIO Oscilloscope
~~~~~~~~~~~~~~~~

.. important::

   Make sure to download/update to the latest version of IIO-Oscilloscope found on this link\ :git-iio-oscilloscope:`releases\`


-  Once done with the installation or an update of the latest IIO-Oscilloscope, open the application. The user needs to supply a URI which will be used in the context creation of the IIO Oscilloscope and the instructions can be seen from the previous section.
-  Press refresh to display available IIO Devices, once ad7746 appeared, press connect.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0552/osc.png
   :alt: AD7746 Oscilloscope Configuration
   :align: center
   :width: 200px

Debug Panel
^^^^^^^^^^^

Below is the Debug panel of AD7746 wherein you can directly access the attributes of the device.


|AD7746 Debug Panel|

DMM Panel
^^^^^^^^^

Access the DMM panel to see the instantaneous reading of the input capacitances and the device temperature.


|AD7746 DMM Panel|

PyADI-IIO
~~~~~~~~~

| :doc:`PyADI-IIO </wiki-migration/resources/tools-software/linux-software/pyadi-iio>` is a python abstraction module for ADI hardware with IIO drivers to make them easier to use. This module provides device-specific APIs built on top of the current libIIO python bindings. These interfaces try to match the driver naming as much as possible without the need to understand the complexities of libIIO and IIO.
| Follow the step-by-step procedure on how to install, configure, and set up PYADI-IIO and install the necessary packages/modules needed by referring to this :doc:`link </wiki-migration/resources/tools-software/linux-software/pyadi-iio>`.

Running the example
^^^^^^^^^^^^^^^^^^^

After installing and configuring PYADI-IIO in your machine, you are now ready to run python script examples. In our case, run the **ad7746.py** found in the examples folder.

<code> D:\\pyadi-iio>python examples/ad7746.py </code>

Press enter and you will get these readings.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0552/python_script.png
   :alt: python_script.png
   :width: 500px

.. admonition:: Download
   :class: download

   Github link for the python sample script: :git-pyadi-iio:`CN0511 Python Example <examples/cn0511_example.py>`


Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download
   :class: download

   
   :adi:`EVAL-CN0xxx-ARDZ Design & Integration Files <cn0xxx-designsupport>`
   
   -  Schematics
   -  PCB Layout
   -  Bill of Materials
   -  Allegro Project
   -  <ADD other things specific to your project if desired>
   


Additional Information and Useful Links
---------------------------------------

-  :git-EVAL-ADICUP3029:`CN0414 Demo Software <projects/ADuCM3029_demo_cn0414>`
-  :adi:`CN0414 Circuit Note Page <CN0414>`
-  :adi:`CN0414 Design Support Package <CN0414-DesignSupport>`
-  :adi:`AD4111 Product Page <AD4111>`
-  :adi:`AD5700-1 Product Page <AD5700-1>`
-  :adi:`ADUM5411 Product Page <ADUM5411>`
-  :adi:`ADUM3151 Product Page <ADUM3151>`
-  :adi:`ADP2441 Product Page <ADP2441>`
-  :adi:`ADG704 Product Page <ADG704>`

Reference Demos & Software
--------------------------

-  :git-pyadi-iio>`__
-  `AD9166 IIO <https::`pyADI-IIO </github.com/analogdevicesinc/libad9166-iio>`
-  :doc:`PyADI-IIO Installation Guide </wiki-migration/resources/tools-software/linux-software/pyadi-iio>`
-  :doc:`IIO Oscilloscope Installation Guide </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`
-  :doc:`Kuiper Linux </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`

Hardware Registration
---------------------

.. tip::

   Receive software update notifications, documentation updates, view the latest videos, and more when you register your hardware. `Register <https://form.analog.com/Form_Pages/FeedBack/EVAL-CN0511-RPIZ?&v=RevD>`__ to receive all these great benefits and more!


// End of Document //

.. |youtube>6yjW-1EjQ0I| image:: https://wiki.analog.com/_media/youtube>6yjW-1EjQ0I
.. |pmod-toadicup.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0552/pmod-toadicup.png
   :width: 900px
.. |switch_config.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0552/switch_config.png
   :width: 900px
.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0552/daplink.jpg
   :width: 300px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0552/interposer.png
   :width: 500px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0552/pmod-interposer.png
   :width: 300px
.. |AD7746 Debug Panel| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0552/debug_panel.png
   :width: 400px
.. |AD7746 DMM Panel| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0552/dmm_readings.png
   :width: 400px
