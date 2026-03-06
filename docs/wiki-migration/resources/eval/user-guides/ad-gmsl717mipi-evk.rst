AD-GMSL717MIPI-EVK
==================

|

.. important::

   **Notice:** This page has been fully migrated to GitHub.io and is no longer maintained on the Wiki. Please refer to the GitHub link below for the most current and accurate information.

   | https://analogdevicesinc.github.io/documentation/solutions/reference-designs/ad-gmsl717mipi-evk/index.html
   | If you would like to contribute updates to this document, please submit your suggestions via a Pull Request on the GitHub page.
   | Thank you for your understanding, and we apologize for any inconvenience this transition may cause.
   


Overview
--------

The **AD-GMSL717MIPI-EVK** allows connecting a wide range of cameras with 15-pin MIPI CSI-2 ribbon cable interfaces to Analog Devices’ MAX96717 GMSL2 serializer, enabling connectivity to processing systems which have GMSL2 receive interfaces. Due to its compact form-factor and mounting holes, the board can be easily and securely integrated into vision systems with various requirements in terms of size, shape, and mobility. A detachable extension allows mounting on tripods with 1/4”-20 mounts.

|image1| |image2|

| 
| ==== Features ====

-  1 x MIPI CSI (2 x lanes) 15-pin ribbon cable connector
-  4 x MFP pins routed to the ribbon cable connector
-  1 x FAKRA coaxial cable connector
-  Implements Power over Cable (PoC)
-  Mounting holes for easy and secure attach of all Raspberry Pi cameras form factors
-  Open-source reference software for all supported camera types targeting a range of compute platforms such as Nvidia SoCs, Raspberry Pi, and AMD SoCs

Applications
------------

-  High-Resolution Camera Systems
-  Autonomous Guided Vehicles
-  Advanced Driver Assistance Systems (ADAS)

| 
| ===== Software Development ===== The GMSL Linux kernel drivers, the complete Linux distributions for the supported processing platforms, and software user guides can be found on the `Analog Devices GMSL GitHub repository <https://github.com/analogdevicesinc/gmsl>`__.

| 
| ==== Resources ====

-  :adi:`MAX96717 Product Page <MAX96717>`
-  :adi:`MAX20049 Product Page <MAX20049>`

| 
| ===== Support =====

.. hint::

   For questions and more information, please contact us on the **Analog Devices Engineer Zone**.

   
   -  :ez:`EngineerZone Linux Support <linux-software-drivers>`
   -  :adi:`GMSL-Related Technical Support <en/support.html>`
   


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmsl717mipi-evk/ad-gmsl717mipi-evk_block_diagram.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmsl717mipi-evk_angle-evaluation-board-web.png
   :width: 400px
