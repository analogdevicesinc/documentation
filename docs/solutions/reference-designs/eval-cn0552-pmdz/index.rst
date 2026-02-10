.. _eval-cn0552-pmdz:

Capacitance to Digital Converter with Extended Range

Overview
--------

The :adi:`EVAL-CN0552-PMDZ <CN0552>` is a
`PMOD <https://reference.digilentinc.com/pmod/start>`__ 
form-factor evaluation board for the :adi:`AD7746`, a high
resolution, Σ-Δ capacitance-to-digital converter (CDC). The
architecture features inherent high resolution (24-bit no
missing codes, up to 21-bit effective resolution), high
linearity (±0.01%), and high accuracy (±4 fF factory 
calibrated).

.. figure:: actual_hardware.jpg
   :align: center
   :width: 400px

   EVAL-CN0552-PMDZ

The :adi:`CN0552` has two capacitive inputs with each channel that
can be configured as single-ended or differential. The capacitance
input range is ±4.096 pF at a maximum bulk capacitance of 17 pF 
but is capable of extending up to ±50 pF with a maximum bulk 
capacitance of 200 pF which can be balanced by a
programmable on-chip, digital-to-capacitance converter (CAPDAC).

.. figure:: cn0552_block_diagram.png
   :align: center

   CN0552 Block Diagram

The output data rate is adjustable from 9.1 sps to 90.9 sps, with the
16.1 sps setting providing strong rejection of both 50 Hz and 60 Hz
power line noise. The CDC also provides temperature measurement 
with a resolution of 0.1°C and accuracy of ±2° C for temperature
compensation and system calibration.

The CN0552 is compatible with I2C PMOD platform boards, with an I/O
voltage from 2.7 V to 5.5 V.

.. figure:: i2c_con.png
   :align: center

   I2C Connection

Features
--------

- Interfaces to single or differential floating sensors

- Resolution down to 4aF (that is, up to 21 ENOB)

- Accuracy: 4fF

- Linearity: 0.01%

- Common mode (not changing) capacitance up to 17 pF

- Full-scale (changing) capacitance range: ±4 pF

- Tolerant of parasitic capacitance to ground up to 60 pF

- Update rate: 10 Hz to 90 Hz

- Simultaneous 50 Hz and 60 Hz rejection at 16Hz

Connectors and Configuration
----------------------------

By default, the :adi:`EVAL-CN0552-PMDZ <CN0552>` is
configured to be controlled and power from the PMOD connector
using standard connections.

CN0552 Inputs/Outputs Connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All the analog and digital input/output pins available on the
EVAL-CN0552-PMDZ are brought out to two(2) separate 8 row 0.1“ through
holes through connectors P8 and P13.

============ ====== ============= ======
Connector P8        Connector P13       
------------ ------ ------------- ------
Description  Pin(s) Description   Pin(s)
============ ====== ============= ======
EXCA         1      GND           1
EXCB         2      VDD           2
EXC_EXTENDED 3      GND           3
REFIN_POS    4      VIN_NEG       4
REFIN_NEG    5      VIN_POS       5
GND          6      GND           6
CIN1_NEG     7      CIN2_NEG      7
CIN1_POS     8      CIN2_POS      8
============ ====== ============= ======

Digital Communications
~~~~~~~~~~~~~~~~~~~~~~

The Digital communication on the EVAL-CN0552-PMDZ is accomplished using
a new standard I2C PMOD port.

============ ======
Connector P2       
------------ ------
Description  Pin(s)
============ ======
INT          6
RST          5
SCL          4
SDA          3
GND          2
IOVDD        1
============ ======

Solder Jumpers
~~~~~~~~~~~~~~

Eight solder jumpers are available at the bottom of the board, if you
want to change the operating modes. See the schematic for more details.

.. figure:: eval-cn0552-pmdztop.png
   :align: center

+-----------------------+-----------------------+-----------------------+
| Description and       | Solder Jumper         | Default Position      |
| default connection    |                       |                       |
+=======================+=======================+=======================+
| ADC SDA connection    | P1                    | Shorted               |
| (pull-up SDA to VDD)  |                       |                       |
+-----------------------+-----------------------+-----------------------+
| ADC SCL connection    | P7                    | Shorted               |
| (pull-up SCL to VDD)  |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Extended Excitation   | P14                   | Shorted               |
| Enable (connect A1    |                       |                       |
| OUT to P8 pin 3)      |                       |                       |
+-----------------------+-----------------------+-----------------------+
| ADC REFIN(-)          | P3                    | Open                  |
| connection (connect   |                       |                       |
| GND and P8 pin 5)     |                       |                       |
+-----------------------+-----------------------+-----------------------+
| ADC REFIN(+)          | P9                    | Open                  |
| connection (connect   |                       |                       |
| GND and P8 pin 4)     |                       |                       |
+-----------------------+-----------------------+-----------------------+
| ADC CIN1(-)           | P4                    | Open                  |
| connection (connect   |                       |                       |
| GND to P8 pin 7)      |                       |                       |
+-----------------------+-----------------------+-----------------------+
| ADC CIN1(+)           | P10                   | Open                  |
| connection (connect   |                       |                       |
| GND to P8 pin 8)      |                       |                       |
+-----------------------+-----------------------+-----------------------+
| ADC CIN2(-)           | P5                    | Open                  |
| connection (connect   |                       |                       |
| GND to P13 pin 7)     |                       |                       |
+-----------------------+-----------------------+-----------------------+
| ADC CIN1(+)           | P11                   | Open                  |
| connection (connect   |                       |                       |
| GND to P13 pin 8)     |                       |                       |
+-----------------------+-----------------------+-----------------------+
| ADC VIN(-) connection | P6                    | Open                  |
| (connect GND to P13   |                       |                       |
| pin 4)                |                       |                       |
+-----------------------+-----------------------+-----------------------+
| ADC VIN(+) connection | P12                   | Open                  |
| (connect GND to P13   |                       |                       |
| pin 5)                |                       |                       |
+-----------------------+-----------------------+-----------------------+

Test Points
~~~~~~~~~~~

Also, four test points are available to probe the I2C interface.

Device Driver Support
---------------------

There are two device driver solutions that are provided for controlling
the :adi:`EVAL-CN0552-PMDZ <CN0552>` using the no-OS device driver on
the :adi:`EVAL-ADICUP3029` platform and Linux device driver on the 
**Raspberry Pi** platform.

#. **EVAL-ADICUP3029**

 - The ADICUP3029 example application uses the 
   :dokuwiki:`AD7746 no-OS driver <resources/tools-software/uc-drivers/ad7746>`
   and emulates the Linux IIO framework through the 
   :git-libtinyiiod:`tinyiiod daemon library <+>`. The
   application communicates with the host computer via the serial
   backend, over a USB-UART physical connection. This facilitates rapid
   application development on a host computer, independent from embedded
   code development.

#. **Raspberry Pi**

 - The 
   :dokuwiki:`Linux driver <resources/tools-software/linux-drivers/iio-cdc/ad7745>`
   uses the Industrial Input/Output (IIO) framework, greatly simplifying
   the development of application code via the cross-platform Libiio
   library, which is written in C and includes bindings for Python,
   MATLAB, C#, and other languages. Application code can run directly on
   the platform board, communicating with the device over the local
   backend, or from a remote host over the network or USB backends.

Similarly, utility software such as iio_info, IIO Oscilloscope,
PyADI-IIO, and etc. can be used for both the EVAL-CN0552-PMDZ on
Raspberry PI and on ADICUP3029.

General Setup Using ADICUP3029
------------------------------

The :adi:`EVAL-CN0552-PMDZ <CN0552>` can be used with
:dokuwiki:`ADICUP3029 <resources/eval/user-guides/eval-adicup3029>`.
Here is a video on how to use the CN0552 with the ADICUP3029:

.. image:: https://img.youtube.com/vi/6yjW-1EjQ0I/maxresdefault.jpg
    :width: 600px
    :target: https://www.youtube.com/watch?v=6yjW-1EjQ0I

Demo Requirements
~~~~~~~~~~~~~~~~~

The following is the list of items needed in order to replicate this
demo.

- **Hardware**

  - :adi:`EVAL-ADICUP3029 <EVAL-ADICUP3029>`

  - :adi:`EVAL-CN0552-PMDZ <CN0552>`

  - Two 2 pF ceramic capacitors

  - Micro-USB to USB Cable

  - PC or Laptop with USB Port

- **Software**

  There are two basic ways to program the ADICUP3029 with the software for
  the CN0552.

  #. Dragging and Dropping the .Hex to the Daplink drive

  #. Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version
that Analog Devices creates for testing and evaluation purposes. This is
the EASIEST way to get started with the reference design.

Importing the project into CrossCore is going to allow you to change
parameters and customize the software to fit your needs, but will be a
bit more advanced and will require you to download the CrossCore
toolchain.

The software for the **ADICUP3029_CN0552** demo can be found here:

.. admonition:: Download
    
    Prebuilt CN0552 Hex File
    
     - :download:`ADuCM3029_demo_cn0552.hex <ADuCM3029_demo_cn0552.hex>`

    Complete CN0552 Source Files

     - :git-no-oS:`ADuCM3029_demo_cn0552 Source Code <projects/cn0552>`

To build the project from the source, follow the instructions in the
:git-no-oS:`no-os wiki <wiki+>`.

Setting up the Hardware
~~~~~~~~~~~~~~~~~~~~~~~

#. Connect **EVAL-CN0552-PMDZ** board at connector **P9** of the
   **EVAL-ADICUP3029**.

#. Connect a micro-USB cable to the P10 connector of the EVAL-ADICUP3029
   and connect it to a computer. The final setup should look similar to
   the picture below.

   .. figure:: pmod-toadicup.png
      :align: center
      
      Hardware Setup

#. Make sure the following switches are as shown from the table below.

   .. figure:: switch_config.png
      :align: center
      
      Switch Confuguration

#. From your PC, open My Computer and look for the DAPLINK drive, if you
   see this then the drivers are complete and correct.

   .. figure:: daplink.jpg
      :align: center
      :width: 400px
      :height: 400px
      
      DAPLINK Drive

#. Simply extract the provided zip file. Once extracted, you will see
   the pre-built hex file for the CN0552 demo. Then drag and drop this
   Hex file to the DAPLINK drive and your ADICUP3029 board will be
   programmed. The DS2 (red) LED will blink rapidly.

#. The DS2 will stop blinking and will stay ON once the programming is
   done.

#. For demo purposes, place a 2 pF capacitor between the EXCA pin and
   the CIN1(+) pin on the PMOD board. This will be your first channel.
   Then, place another 2 pF capacitor between EXCB pin and the CIN2(+)
   pin on the PMOD board. This will be your second channel.

General Setup Using Raspberry Pi
--------------------------------

The :adi:`EVAL-CN0552-PMDZ <CN0552>` can be used with a Raspberry Pi.

Demo Requirements
~~~~~~~~~~~~~~~~~

The following is a list of items needed in order to replicate this demo.

- **Hardware**

  - :adi:`EVAL-CN0552-PMDZ <CN0552>`

  - :adi:`PMOD to Raspberry Pi Adapter (PMD-RPI-INTZ) <PMD-RPI-INTZ>`

  - Raspberry PI Zero, Zero W, 3B+, or 4

  - 16 GB (or larger) Class 10 (or faster) micro-SD card

  - 5 Vdc, 2.5 A power supply with micro USB connector (USB-C power 
    supply for Raspberry Pi 4)

  - User interface setup (choose one):

    - HDMI monitor, keyboard, mouse plugged directly into Raspberry Pi

    - Host Windows/Linux/Mac computer on the same network as Raspberry
      Pi

- **Software**

  - :external+adi-kuiper-gen:doc:`index`

Loading Image on SD Card
~~~~~~~~~~~~~~~~~~~~~~~~

In order to control the :adi:`EVAL-CN0552-PMDZ <CN0552>` from the
Raspberry Pi, you will need to install ADI Kuiper Linux on an SD card.
Complete instructions, including where to download the SD card image,
how to write it to the SD card, and how to configure the system are
provided at :external+adi-kuiper-gen:doc:`index`.
Write the image and follow the system configuration procedure.

Configuring the SD Card
~~~~~~~~~~~~~~~~~~~~~~~

Follow the Hardware Configuration procedure under **Preparing the 
Image: Raspberry Pi** in the :external+adi-kuiper-gen:doc:`index`
page, substituting the following lines in **config.txt**:

.. code-block::

   dtoverlay=rpi-cn0552

Setting up the Hardware
~~~~~~~~~~~~~~~~~~~~~~~

To set up the circuit for evaluation, consider the following steps:

#. Connect the P9 of the **PMOD to Raspberry Pi Interposer** board at
   the male header GPIO pin connector of the **Raspberry Pi** as shown
   below.

   .. figure:: interposer.png
      :align: center

#. Connect the :adi:`EVAL-CN0552-PMDZ <CN0552>` on
   the PMOD to Raspberry Pi Interposer board either via Port P3 or P4.

   .. figure:: pmod-interposer.png
      :align: center

#. Burn the SD card with the proper ADI Kuiper Linux image. Insert the
   burned SD card on the designated slot on the RPi.

#. Connect the system to a monitor using an HDMI cable through the mini
   HDMI connector on the RPi.

#. Connect a USB keyboard and mouse to the RPi through the USB ports.

#. Power on the RPi board by plugging in a 5 V power supply with a
   micro-USB connector. The final setup should look similar to the
   picture below.

   .. figure:: overall_setup.png
      :align: center

Software (both ADICUP3029 and Raspberry Pi)
-------------------------------------------

Connection
~~~~~~~~~~

To be able to connect your device, the software must be able to create a
context. The context creation in the software depends on the backend
used to connect to the device as well as the platform where the
EVAL-CN0552-PMDZ is attached. Two platforms are currently supported for
the CN0552: Raspberry Pi using the ADI Kuiper Linux and the ADICUP3029
running the no-OS AD7746 demo project. The user needs to supply a URI
which will be used in the context creation.

The Libiio is a library for interfacing with IIO devices.

.. admonition:: Download
    
    Install the 
    :git-libiio:`Libiio package <releases+>`
    on your machine.

The
:dokuwiki:`iio_info <resources/tools-software/linux-software/libiio/iio_info>`
command is a part of the libIIO package that reports all IIO attributes.

Upon installation, simply enter the command on the terminal command line
to access it.

For RPI Direct Local Access:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

   iio_info

For Windows machine connected to Raspberry Pi:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

   iio_info -u ip:<ip address of your ip>

Example:

 - If your Raspberry Pi has the IP address 192.168.1.7, you have to use
   *iio_info -u ip::192.168.1.7* as your URI

.. note::
    
    Do note that the Windows machine and the RPI board should be 
    connected to the same network in order for the machine to 
    detect the device.

For Windows machine connected to ADICUP3029:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

   iio_info -u serial:<serial port>

Examples:

 - In a Windows machine, you can check the port of your ADICUP3029 via
   Device Manager in the Ports (COM & LPT) section. If your device is in
   COM4, you have to use *iio_info -u serial:COM4* as your URI.

 - In a Unix-based machine, you will see it under the /dev/ directory in
   this format “ttyUSBn”, where n is a number depending on how many
   serial USB devices attached. If you see that your device is ttyUSB0,
   you have to use serial:/dev/ttyUSB0 as your URI.

IIO Commands
~~~~~~~~~~~~

There are different commands that can be used to manage the device being
used. The
:dokuwiki:`iio_attr <resources/tools-software/linux-software/libiio/iio_attr>`
command reads and writes IIO attributes.

.. code-block::

   analog@analog:~$ iio_attr [OPTION]...

Example:

 - To look at the context attributes, enter this code on the terminal:

    .. code-block::
        
        analog@analog:~$ iio_attr -a -C

The
:dokuwiki:`iio_reg <resources/tools-software/linux-software/libiio/iio_reg>`
command reads or writes SPI or I2C registers in an IIO device. This is
generally not needed for end applications, but can be useful in
debugging drivers. Note that you need to specify a context using the
*-u* qualifier when you are not directly accessing the device via RPI or
when you are using the ADICUP3029 platform.

.. code-block::

   analog@analog:~$ iio_reg -u <context> <device> <register> [<value>]

Example:

 - To to read the device ID (register = 0x02) of an AD7746 interfaced via
   RPI from a Windows machine, enter the following code on the terminal:

    .. code-block::
        
        iio_reg -u ip: ad7746 0x02

IIO Oscilloscope
~~~~~~~~~~~~~~~~

.. important:: 
    
    Make sure to download/update to the latest version of 
    IIO-Oscilloscope found on this 
    :git-iio-oscilloscope:`link <releases+>`.

#. Once done with the installation or an update of the latest
   IIO-Oscilloscope, open the application. The user needs to supply a
   URI which will be used in the context creation of the IIO
   Oscilloscope and the instructions can be seen from the previous
   section.

#. Press refresh to display available IIO Devices, once ad7746 appeared,
   press connect.

   .. figure:: osc.png
      :align: center


Debug Panel
^^^^^^^^^^^

Below is the Debug panel of :adi:`AD7746` wherein you can directly 
access the attributes of the device.

.. figure:: debug_panel.png
   :align: center

DMM Panel
^^^^^^^^^

Access the DMM panel to see the instantaneous reading of the input
capacitances and the device temperature.

.. figure:: dmm_readings.png
   :align: center

PyADI-IIO
~~~~~~~~~

:ref:`pyadi-iio`
is a python abstraction module for ADI hardware with IIO drivers to make
them easier to use. This module provides device-specific APIs built on
top of the current libIIO python bindings. These interfaces try to match
the driver naming as much as possible without the need to understand the
complexities of libIIO and IIO.

Follow the step-by-step procedure on how to install, configure, and set
up PYADI-IIO and install the necessary packages/modules needed by
referring to this :ref:`pyadi-iio`.

Running the example
^^^^^^^^^^^^^^^^^^^

After installing and configuring PYADI-IIO in your machine, you are now
ready to run python script examples. In our case, run the **ad7746.py**
found in the examples folder.

.. code-block::

    D:\pyadi-iio>python examples/ad7746.py 

Press enter and you will get these readings.

.. figure:: python_script.png
   :align: center

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download
   
   :download:`EVAL-CN0552-PMDZ Design & Integration Files <cn0552-DesignSupport.zip>`
   
    - Schematic
    - PCB Layout
    - Bill of Materials
    - Allegro Project

Additional Information and Useful Links
---------------------------------------

 - :adi:`AD7746 Product Page <AD7746>`

 - :adi:`AN-1585 Application Note <technical-documentation/application-notes/AN-1585.pdf>`

Reference Demos & Software
--------------------------

 - :git-no-OS:`CN0552 No-OS Build Instruction Guide <wiki+>`

 - :git-no-OS:`CN0552 No-OS Device Drivers <projects/cn0552>`

 - :external+adi-kuiper-gen:doc:`index`

Registration
------------

Receive software update notifications, documentation updates, view the
latest videos, and more when you register your hardware.
`Register <https://my.analog.com/en/app/registration/hardware/EVAL-CN0552-PMDZ?&v=Rev%20B>`__
to receive all these great benefits and more!