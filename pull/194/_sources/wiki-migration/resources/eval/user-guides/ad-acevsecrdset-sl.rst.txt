AD-ACEVSECRDSET-SL User Guide
=============================

|

.. important::

   **Notice:** This page has been fully migrated to GitHub.io and is no longer maintained on the Wiki. Please refer to the GitHub link below for the most current and accurate information.

   | https://analogdevicesinc.github.io/documentation/solutions/reference-designs/ad-acevsecrdset-sl/index.html
   | If you would like to contribute updates to this document, please submit your suggestions via a Pull Request on the GitHub page.
   | Thank you for your understanding, and we apologize for any inconvenience this transition may cause.
   


Introduction
------------

| The :adi:`AD-ACEVSECRDSET-SL <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/ad-bct2ade9113-sl.html>` is a complete Type 2 EVSE 3.6 kW charging cable solution, providing a reference design intended for evaluation and prototyping of EV charging systems.
| |image1|

| The system includes the :adi:`ADE9113` 3-channel isolated sigma-delta (Σ-Δ) ADC for voltage and current measurement on the single-phase power input and measurement of the relay voltage for solder contacts detection and relay state of health. Safe operation is enabled by the inclusion of a 6 mA DC / 30 mA rms RCD. Detection of overvoltage, undervoltage, overcurrent, overtemperature and EV diode presence are also available.
| The :adi:`MAX32655` ultralow power ARM® Cortex®-M4 processor implements the logic for system control and communication with the EV over the control pilot interface. A programming and debugging interface are included. The MAX32655 Bluetooth 5.2 interface enables connectivity to external devices.
| The design is accompanied by an open-source software stack and reference applications, enabling custom software development to start from a proven implementation validated to meet the applicable standards. The system is designed to meet the IEC61851 and IEC62752 standards.
| ===== Features =====

-  Complete reference design for Type 2 EVSE Cordset (IC-CPD)
-  Power level from 2.3 kW up to 3.6 kW (at 230 V)
-  Designed to meet the applicable standards - IEC61851, IEC62752
-  Incorporates a 6 mA DC/30 mA rms RCD and a control pilot circuit
-  Relay soldered contacts detection
-  Upstream and downstream PE detection.
-  Overtemperature detection
-  Integrated isolation
-  Reduced component count for cost optimization
-  Bluetooth 5.2 interface for connectivity to external devices
-  Open-source software stack to enable custom firmware development

Applications
------------

-  EV Charging

Block Diagram
-------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/block_diagram_new.png
   :align: center
   :width: 800px

Specifications
--------------

.. container:: center

   
   =================================== ====================================
   Electrical Specs                    
   =================================== ====================================
   Power                               3.6 kW
   Input voltage                       230V +/-15% or 120V +/-15%
   Input current                       16 A
   Input frequency                     50 Hz / 60 Hz
   Output voltage                      230 V +/-15% or 120V +/-15%
   Output current                      10 A/16 A
   Output frequency                    50 Hz / 60 Hz
   Operating Conditions                
   Operating temperature               -25°C to +45°C
   Residual current device             6mA DC / 30 mA rms
   Safety Features                     
   Overvoltage category                II
   Protection features                 Relay soldered contacts detection
   \                                   Overvoltage
   \                                   Undervoltage
   \                                   Overcurrent
   \                                   Overtemperature
   Other features                      Integrated isolation
   \                                   Diode detection
   \                                   Upstream and downstream PE detection
   User Interface & Control            
   Communication                       Bluetooth 5.2
   Status Indicators                   LEDs
   Debugging                           RS-232
   Designed to the following standards 
   \                                   IEC 61851, IEC 62752
   =================================== ====================================
   


| 
| ===== System Setup =====

.. tip::

   For Hardware & Software Setup instructions, please check out the following pages:

   
   -  :doc:`AD-ACEVSECRDSET-SL Hardware User Guide </wiki-migration/resources/eval/user-guides/ad-acevsecrdset-sl/hardware>`
   
   -  :doc:`AD-ACEVSECRDSET-SL Software User Guide </wiki-migration/resources/eval/user-guides/ad-acevsecrdset-sl/software>`
   


--------------

Additional Information and Useful Links
---------------------------------------

-  :adi:`AD-ACEVSECRDSET-SL Product Page <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/ad-bct2ade9113-sl.html>`
-  :adi:`MAX32655 Product Page <MAX32655>`
-  :adi:`ADE9113 Product Page <ADE9113>`
-  :adi:`ADA4523-1 Product Page <ADA4523-1>`
-  :adi:`ADT75 Product Page <ADT75>`
-  :adi:`MAX20457 Product Page <MAX20457>`
-  :adi:`LT8330 Product Page <LT8330>`

--------------

Software Resources
------------------

-  :git-no-OS:`Link to the project source code <projects/ad-acevsecrdset-sl>`

--------------

Design and Integration Files
----------------------------

.. admonition:: Download
   :class: download

   `AD-ACEVSECRDSET-SL Design & Integration Files <https://wiki.analog.com/_media/resources/eval/user-guides/ad-acevsecrdset-sl/ad-acevsecrdset-sl_design_support_package_rev._e.zip>`_

   
   -  Schematics
   -  PCB Layout
   -  Bill of Materials
   -  Allegro Project
   


--------------

Registration
------------

.. tip::

   Receive software update notifications, documentation updates, view the latest videos, and more when you register your hardware. `Register <https://form.analog.com/Form_Pages/FeedBack/AD-ACEVSECRDSET-SL>`_ to receive all these great benefits and more!


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bct2ade9113-sl_angle.jpg
   :width: 400px
