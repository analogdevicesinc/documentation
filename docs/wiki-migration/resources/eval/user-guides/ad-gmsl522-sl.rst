AD-GMSL522-SL: GMSL Carrier Board
=================================

|

.. important::

   We are in the process of migrating our documentation to GitHub Pages.

   | The latest version of this page can be found at https://analogdevicesinc.github.io/documentation/solutions/reference-designs/ad-gmsl522-sl/index.html


Overview
--------

| The **AD-GMSL522-SL** is a :adi:`Gigabit Multimedia Serial Link (GMSL) <en/solutions/gigabit-mulitimedia-serial-link.html>`-enabled NVIDIA Jetson Xavier NX-based hardware and software solution that allows for prototyping with GMSL technology. This solution creates a scalable, user friendly, GMSL platform for receiving and transmitting data over GMSL. It supports two forms of camera input -- either straight CSI data coming through a SAMTEC connector from a GMSL evaluation kit, or via camera modules using GMSL2 or GMSL1 technology to connect to the on-board :adi:`MAX96724` via COAX connectors. The package also includes software tools to enable development of GMSL applications. Among these tools are modified L4T kernels that support certain camera modules and documentation that allows any user to update these kernels for their specific hardware needs. The design also incorporates the MAX96724GTN/VY+ Quad tunneling GMSL2/1 to CSI-2 deserializer and MAX96717GTJ/VY+ CSI-2 to GMSL2 serializer and provides a reliable platform to evaluate high-bandwidth GMSL.
| |image1|

--------------

Features
~~~~~~~~

-  Hardware solution that bridges the gap between GMSL2 technology and the NVIDIA Jetson
-  On-board MAX96724 that allows 4x GMSL2/1 camera inputs that allows for camera module bring-up, debug, and video streaming
-  On-board MAX96717 that can be used for camera emulation and head-unit debug
-  Enables development of GMSL applications with NVIDIA Jetson SoC
-  SAMTEC connector that allows connection of any GMSL DPHY EV Kit to the NVIDIA Jetson
-  Additional inputs: USB, Ethernet, PCIe, and microSD card

--------------

Applications
~~~~~~~~~~~~

-  ADAS Camera Solutions
-  Sensor Fusion ECU
-  Driver and Occupant Monitoring
-  In-cabin Infotainment

--------------

System Architecture
~~~~~~~~~~~~~~~~~~~

| 
| |image2|

--------------

Specifications
~~~~~~~~~~~~~~

.. container:: center round box

   
   +--------------------------------------------------------------+----------------------------------------------------------------+
   | <fc #6495ed>\ **MAX96724 Interfaces to Jetson SOM**\ </fc>   |                                                                |
   +--------------------------------------------------------------+----------------------------------------------------------------+
   | **Interface**                                                | **Detailed Description**                                       |
   +--------------------------------------------------------------+----------------------------------------------------------------+
   | 2x I2C                                                       | 1x I2C, and 1x I2C PT. 400 kbps speeds                         |
   +--------------------------------------------------------------+----------------------------------------------------------------+
   | GPIO Signals                                                 | MFP0, MFP1, MFP4, MFP5, PWDNB                                  |
   +--------------------------------------------------------------+----------------------------------------------------------------+
   | MIPI CSI-2                                                   | CSI-2 v1.3                                                     |
   |                                                              | DPHY v1.2                                                      |
   +--------------------------------------------------------------+----------------------------------------------------------------+
   | <fc #6495ed>\ **CSI SAMTEC Interfaces to Jetson SOM**\ </fc> |                                                                |
   +--------------------------------------------------------------+----------------------------------------------------------------+
   | 2x I2C                                                       | 1x I2C, and 1x I2C PT. 400 kbps speeds                         |
   +--------------------------------------------------------------+----------------------------------------------------------------+
   | GPIO Signals                                                 | ERRB, FSYNC0, RESET, LOCK                                      |
   +--------------------------------------------------------------+----------------------------------------------------------------+
   | Oscillator                                                   | Configurable speed oscillator signal between 15 MHz and 40 MHz |
   +--------------------------------------------------------------+----------------------------------------------------------------+
   | 1x SPI                                                       | 25 MHz Serial Peripheral Interface (SPI).                      |
   |                                                              | Non-standard SPI used for GMSL devices                         |
   +--------------------------------------------------------------+----------------------------------------------------------------+
   | CSI-2 v1.3                                                   | 4x2, 2x4 CSI-2 DPHY v1.2                                       |
   +--------------------------------------------------------------+----------------------------------------------------------------+
   | Power                                                        | 12 V, 5 V, 1.8 V                                               |
   +--------------------------------------------------------------+----------------------------------------------------------------+
   | <fc #6495ed>\ **GMSL Inputs**\ </fc>                         |                                                                |
   +--------------------------------------------------------------+----------------------------------------------------------------+
   | 4x High Speed COAX Connector                                 | 59S2AQ-40MT5-Z_1                                               |
   +--------------------------------------------------------------+----------------------------------------------------------------+
   | GMSL2                                                        | 3 Gbps, 6 Gbps, COAX                                           |
   +--------------------------------------------------------------+----------------------------------------------------------------+
   | Protocol                                                     | GMSL1/2                                                        |
   +--------------------------------------------------------------+----------------------------------------------------------------+
   | PoC                                                          | 5 V, 8 V, 12 V                                                 |
   +--------------------------------------------------------------+----------------------------------------------------------------+
   | <fc #6495ed>\ **GMSL Output**\ </fc>                         |                                                                |
   +--------------------------------------------------------------+----------------------------------------------------------------+
   | 1x High Speed COAX Connector                                 | 59S2AQ-40MT5-Z_1                                               |
   +--------------------------------------------------------------+----------------------------------------------------------------+
   | GMSL2/3                                                      | 3 Gbps, 6 Gbps, 12 Gbps, COAX                                  |
   +--------------------------------------------------------------+----------------------------------------------------------------+
   | Protocol                                                     | GMSL1/2/3                                                      |
   +--------------------------------------------------------------+----------------------------------------------------------------+
   | <fc #6495ed>\ **Display Outputs**\ </fc>                     |                                                                |
   +--------------------------------------------------------------+----------------------------------------------------------------+
   | HDMI 2.0a/b                                                  | Up to 6 Gbps, 4Kp60                                            |
   +--------------------------------------------------------------+----------------------------------------------------------------+
   | <fc #6495ed>\ **Other Interfaces**\ </fc>                    |                                                                |
   +--------------------------------------------------------------+----------------------------------------------------------------+
   | PCIe Gen 3/4                                                 | 1x1 Gen3 + 1x4 Gen4                                            |
   +--------------------------------------------------------------+----------------------------------------------------------------+
   | USB                                                          | 4x USB 3.1 Type A                                              |
   +--------------------------------------------------------------+----------------------------------------------------------------+
   | Micro USB Input                                              | USB 2.0                                                        |
   +--------------------------------------------------------------+----------------------------------------------------------------+
   | Ethernet                                                     | 10/100/1000 BASE-T Ethernet with PoE                           |
   +--------------------------------------------------------------+----------------------------------------------------------------+
   | Power                                                        | 12 V Power Barrel Jack Input                                   |
   +--------------------------------------------------------------+----------------------------------------------------------------+
   


--------------

| 
| =====Software Development===== The GMSL Linux kernel drivers, the complete Linux distributions for the supported processing platforms, and software user guides can be found on the `Analog Devices GMSL GitHub repository <https://github.com/analogdevicesinc/gmsl>`__.
| ----

System Setup and Evaluation
---------------------------

.. tip::

   Get complete access to hardware components, design files, and procedure on how to setup and use the AD-GMSL522-SL Carrier Board:

   
   -  :doc:`AD-GMSL522-SL Getting Started Guide </wiki-migration/resources/eval/user-guides/ad-gmsl522-sl/getting-started>`
   -  :doc:`AD-GMSL522-SL Hardware Guide </wiki-migration/resources/eval/user-guides/ad-gmsl522-sl/hardware>`
   -  :doc:`GMSL522 Labs -- Follow Along Guides </wiki-migration/resources/eval/user-guides/ad-gmsl522-sl/gmsl522-labs-follow-along-guides>`
   


--------------

Resources
---------

-  :adi:`MAX96724 Product Page <MAX96724>`
-  :adi:`MAX96717 Product Page <MAX96717>`
-  :adi:`MAX20313 Product Page <MAX20313>`
-  :adi:`AD9394 Product Page <AD9394>`
-  :adi:`AD7291 Product Page <AD7291>`
-  :adi:`MAX2008 Product Page <MAX2008>`
-  :adi:`ADM1177 Product Page <ADM1177>`
-  :adi:`MAX25206 Product Page <MAX25206>`
-  :adi:`LTC3303 Product Page <LTC3303>`

--------------

Support
-------

.. hint::

   For questions and more information, please contact us on the **Analog Devices Engineer Zone**.

   
   -  :ez:`EngineerZone Linux Support <linux-software-drivers>`
   -  :adi:`GMSL-Related Technical Support <en/support.html>`
   


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-viper-sl/ad-viper-sl_angle.jpg
   :width: 500px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmsl522-sl/ad-gmsl522-sl_block_diagram.png
   :width: 800px
