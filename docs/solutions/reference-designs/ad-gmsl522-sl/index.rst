AD-GMSL522-SL
=============

GMSL Carrier Board
""""""""""""""""""

Overview
--------

.. figure:: ad-viper-sl_angle.jpg
   :width: 400 px
   :align: left

   AD-GMSL522-SL GMSL Board

The :adi:`AD-GMSL522-SL` is a
:adi:`Gigabit Multimedia Serial Link(GMSL) <en/solutions/gigabit-mulitimedia-serial-link.html>`-enabled
NVIDIA Jetson Xavier NX-based hardware and software solution that allows for
prototyping with GMSL technology. This solution creates a scalable, user
friendly, GMSL platform for receiving and transmitting data over GMSL. It
supports two forms of camera input – either straight CSI data coming through a
SAMTEC connector from a GMSL evaluation kit, or via camera modules using GMSL2
or GMSL1 technology to connect to the on-board :adi:`MAX96724` via
COAX connectors. The package also includes software tools to enable
development of GMSL applications. Among these tools are modified L4T kernels
that support certain camera modules and documentation that allows any user to
update these kernels for their specific hardware needs. The design also
incorporates the MAX96724GTN/VY+ Quad tunneling GMSL2/1 to CSI-2 deserializer
and MAX96717GTJ/VY+ CSI-2 to GMSL2 serializer and provides a reliable platform
to evaluate high-bandwidth GMSL.

Features
--------

- Hardware solution that bridges the gap between GMSL2 technology and the NVIDIA Jetson
- On-board MAX96724 that allows 4x GMSL2/1 camera inputs that allows for camera module bring-up, debug, and video streaming
- On-board MAX96717 that can be used for camera emulation and head-unit debug
- Enables development of GMSL applications with NVIDIA Jetson SoC
- SAMTEC connector that allows connection of any GMSL DPHY EV Kit to the NVIDIA Jetson
- Additional inputs: USB, Ethernet, PCIe, and microSD card

Applications
------------

- ADAS Camera Solutions
- Sensor Fusion ECU
- Driver and Occupant Monitoring
- In-cabin Infotainment

System Architecture
---------------------

.. figure:: ad-gmsl522-sl_block_diagram.png
   :width: 600 px

   AD-GMSL522-SL Simplified Block Diagram

Specifications
-----------------

.. csv-table::
   :file: specifications.csv

Software Development
--------------------

The GMSL Linux kernel drivers, the complete Linux distributions for the supported
processing platforms, and software user guides can be found on the
:git-gmsl:`Analog Devices GMSL GitHub repository </>`.

User Guides
-----------

Get complete access to hardware components, design files, and procedure on
how to setup and use the AD-GMSL522-SL Carrier Board:

.. toctree::
   :titlesonly:
   :maxdepth: 1
   :glob:

   */index

Resources
---------

- :adi:`MAX96724 Product Page <MAX96724>`
- :adi:`MAX96717 Product Page <MAX96717>`
- :adi:`MAX20313 Product Page <MAX20313>`
- :adi:`AD9394 Product Page <AD9394>`
- :adi:`AD7291 Product Page <AD7291>`
- :adi:`MAX2008 Product Page <MAX2008>`
- :adi:`ADM1177 Product Page <ADM1177>`
- :adi:`MAX25206 Product Page <MAX25206>`
- :adi:`LTC3303 Product Page <LTC3303>`

Support
-------

For questions and more information, please contact us on the :ez:`/`.

- :ez:`EngineerZone Linux Support <linux-software-drivers>`
- :adi:`GMSL-Related Technical Support <en/support.html>`

