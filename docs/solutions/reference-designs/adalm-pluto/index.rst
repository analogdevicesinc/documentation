.. _adalm-pluto:

ADALM-PLUTO
===========

Active Learning Module - PlutoSDR

Introduction
------------

The :adi:`ADALM-PLUTO` (PlutoSDR) is an easy-to-use tool from Analog Devices Inc. (ADI)
designed to introduce the fundamentals of Software Defined Radio (SDR). It enables students,
engineers, and hobbyists to explore radio frequency concepts through hands-on learning with
portable lab equipment that can be taken anywhere.

The PlutoSDR is a pocket-sized learning module that generates or measures RF analog signals
from 325 to 3800 MHz, at up to 61.44 Mega Samples per Second (MSPS) with a 20 MHz bandwidth.
Based on the :adi:`AD9363` RF Agile Transceiver, the module is entirely self-contained and
USB-powered, making it an ideal platform for both education and prototyping.

Whether you're a student learning the basics of RF communications, a software developer
building SDR applications, or a hardware enthusiast customizing designs, the ADALM-PLUTO
provides a versatile platform for radio frequency exploration and development.

.. figure:: pluto_in_hand.png
   :align: center
   :width: 400px

   ADALM-PLUTO Active Learning Module

Features
--------

- Complete Software Defined Radio learning platform
- Based on :adi:`AD9363` RF Agile Transceiver
- Frequency range: 325 MHz to 3800 MHz
- Sample rate: Up to 61.44 MSPS
- Bandwidth: 20 MHz
- One receive and one transmit channel (full duplex capable)
- USB-powered (no external power required)
- Pocket-sized portable design
- Cross-platform support (Windows, Linux, macOS)
- Compatible with MATLAB, Simulink, GNU Radio, and custom applications
- Mass storage mode with configuration files
- Open-source firmware and HDL design files
- Customizable and hackable platform

Applications
------------

- RF and wireless communications education
- Software Defined Radio prototyping
- Algorithm development and testing
- Wireless system design and validation
- Signal processing experimentation
- RF measurement and analysis
- Amateur radio and hobbyist projects
- IoT and wireless sensor development
- Custom wireless protocol development

Specifications
--------------

+------------------------------------------+------------------------------------------+
| **RF Performance**                                                                  |
+------------------------------------------+------------------------------------------+
| RF Transceiver                           | :adi:`AD9363`                            |
+------------------------------------------+------------------------------------------+
| Frequency Range                          | 325 MHz to 3800 MHz                      |
+------------------------------------------+------------------------------------------+
| Sample Rate                              | Up to 61.44 MSPS                         |
+------------------------------------------+------------------------------------------+
| Bandwidth                                | 20 MHz                                   |
+------------------------------------------+------------------------------------------+
| Receive Channels                         | 1                                        |
+------------------------------------------+------------------------------------------+
| Transmit Channels                        | 1                                        |
+------------------------------------------+------------------------------------------+
| Full Duplex                              | Yes                                      |
+------------------------------------------+------------------------------------------+
| **System Interface**                                                                |
+------------------------------------------+------------------------------------------+
| Host Interface                           | USB 2.0 (Hi-Speed)                       |
+------------------------------------------+------------------------------------------+
| Power Supply                             | USB-powered (5V)                         |
+------------------------------------------+------------------------------------------+
| FPGA                                     | Xilinx Zynq Z-7010                       |
+------------------------------------------+------------------------------------------+
| **Software Support**                                                                |
+------------------------------------------+------------------------------------------+
| Operating Systems                        | Windows, Linux, macOS                    |
+------------------------------------------+------------------------------------------+
| Software Frameworks                      | MATLAB, Simulink, GNU Radio,             |
|                                          | IIO Oscilloscope, SDRangel, SDR#         |
+------------------------------------------+------------------------------------------+
| Programming Languages                    | C, C++, C#, Python                       |
+------------------------------------------+------------------------------------------+
| Embedded Platforms                       | Raspberry Pi, Beaglebone, 96boards       |
+------------------------------------------+------------------------------------------+

Target Users
------------

**Students & Educators**
  Ideal for learning RF concepts using MATLAB, Simulink, GNU Radio, or custom programming
  environments on Windows, Linux, Mac, or embedded platforms like Raspberry Pi and Beaglebone.

**Software Developers**
  Develop and test SDR applications using high-level frameworks or custom code. Move from
  prototype to production by embedding algorithms into custom products.

**HDL & Embedded Developers**
  Customize HDL designs and modify embedded software to enable extended capabilities such as
  standalone tracking stations, wireless protocols, or custom signal processing.

**Hardware Enthusiasts**
  Modify PCB designs, connect to GPIO interfaces, and explore multi-device synchronization
  for advanced applications.

Getting Started
---------------

When connected to a computer, the ADALM-PLUTO appears as a Mass Storage Device containing:

- **info.html** - Getting started guide
- **config.txt** - Device configuration file
- **LICENSE.html** - Licensing information

For comprehensive documentation on using the ADALM-PLUTO, please visit:

- :dokuwiki:`PlutoSDR User Guide <university/tools/pluto/users>`
- :dokuwiki:`Drivers & Software Installation <university/tools/pluto/users/drivers>`
- :dokuwiki:`Quick Start Guides <university/tools/pluto/users/quick_start>`

Software Support
----------------

The ADALM-PLUTO is supported by a wide range of software tools and frameworks:

**MATLAB & Simulink**
  - :mw:`Communications Toolbox Support Package for ADALM-PLUTO Radio <help/supportpkg/plutoradio/>`
  - Algorithm development and hardware-in-the-loop testing
  - Seamless transition from simulation to hardware

**GNU Radio**
  - Native gr-iio support
  - :dokuwiki:`GQRX Receiver <university/tools/pluto/users/gqrx>`
  - Custom flowgraph development

**IIO Oscilloscope**
  - :dokuwiki:`Linux measurement and visualization tool <resources/tools-software/linux-software/iio_oscilloscope>`
  - Real-time signal monitoring
  - Device configuration and control

**Python**
  - :dokuwiki:`pyadi-iio library <resources/tools-software/linux-software/pyadi-iio>`
  - libiio Python bindings
  - Rapid prototyping and automation

**Other Frameworks**
  - SDRangel - Qt5/OpenGL SDR frontend
  - SDR# - Windows SDR receiver
  - SoapySDR - Cross-platform abstraction layer
  - Custom C/C++/C# applications

Hardware Resources
------------------

- :dokuwiki:`Hardware Overview <university/tools/pluto/users/hardware>`
- :dokuwiki:`Antenna Selection & Configuration <university/tools/pluto/users/antennas>`
- :dokuwiki:`Temperature Management <university/tools/pluto/users/temperature>`
- :dokuwiki:`Customization Guide <university/tools/pluto/users/customizing>`
- :dokuwiki:`Firmware Upgrade <university/tools/pluto/users/firmware>`

Firmware & HDL
--------------

The ADALM-PLUTO platform is fully open-source, enabling advanced customization:

- :dokuwiki:`Firmware Source Code <university/tools/pluto/devs/embedded_code>`
- :dokuwiki:`HDL Reference Design <university/tools/pluto/devs/fpga>`
- :dokuwiki:`Building Firmware from Source <university/tools/pluto/devs/building_the_image>`
- :git-hdl:`HDL Project Repository <projects/pluto>`

Additional Resources
--------------------

- :adi:`ADALM-PLUTO Product Page <ADALM-PLUTO>`
- :adi:`AD9363 Product Page <AD9363>`
- :dokuwiki:`PlutoSDR Wiki <university/tools/pluto>`
- :dokuwiki:`Programming Examples <university/tools/pluto/users/examples>`
- :ez:`EngineerZone Support </>`

Help and Support
----------------

For questions and more information, please visit:

- :dokuwiki:`PlutoSDR Help & Support <university/tools/pluto/help_support>`
- :ez:`EngineerZone Community </>`

Warning
-------

.. esd-warning::

   The ADALM-PLUTO contains ESD-sensitive components. Electrostatic discharge up to
   4000V can cause permanent damage without proper ESD precautions. Always use proper
   grounding and anti-static procedures when handling the device.
