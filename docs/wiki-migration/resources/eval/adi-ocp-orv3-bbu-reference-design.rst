ADI OCP ORV3 BBU Reference Design
=================================

Overview
--------

This reference design shares an overview about the Analog Devices' proprietary solution for the OCP ORV3 Battery Back-up Unit reference design, leveraging the company's array of resources, including power converters, controllers, power and battery management products, microcontrollers, high-performance supervisors, and more. The webpage will offer a brief summary and explanation of a battery backup unit, outlining its application in data center scenarios.

What is OCP?
------------

The **Open Compute Project**, abbreviated as **OCP**, is an organization that facilitates the sharing of designs and best practices for data center products among various companies, including Meta, IBM, Intel, Google, Microsoft, HP, Nokia, and more. OCP originated internally at Facebook HQ as **"Project Freedom"** in 2009.

BBU Specification
-----------------

What is a Battery Back-up Unit?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image1| Designed for deployment on a BBU Shelf within a data center rack, a **Battery Back-up Unit (BBU)** serves the purpose of supplying DC power to system loads in the event of sudden power interruptions. OCP has established a set of design requirements and specifications for the BBU reference design standard.

As an illustration, a key requirement for an individual BBU module is its ability to deliver a **backup power of 3kW** for a duration of 4 minutes and a **charging power of 250W** over a period ranging from three to six hours.

To see additional details regarding the established BBU standard specifications, please refer to the following link:

-  `Open Rack/SpecsAndDesigns <https://www.opencompute.org/wiki/Open_Rack/SpecsAndDesigns>`_

Single BBU module
^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/eval/bbu_module.png
   :align: right
   :width: 200px

-  3kW for 4 minutes
-  250W charging power
-  Internal cooling
-  Enhanced fault detection
-  Dual disconnect, battery, and backplane
-  Interchangeable 11S6P Li-ion battery pack
-  BMS with advanced SOC and SOH technology

.. image:: https://wiki.analog.com/_media/resources/eval/bbu_module_1.jpg
   :align: right
   :width: 200px

Battery Back-up Unit (BBU Shelf)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  5+1 redundant backplane power
-  Up to 18kW DC power to the system backplane
-  4 minutes of full power delivery

Block Diagram
-------------

The block diagram comprises of the main power converter, :adi:`LT8228`, functioning as a bidirectional controller for the BBU's charging and discharging processes. Additionally, to augment the backup power available during battery discharging, the power converter design incorporates the multiphase expander, :adi:`LT8551`. The combined operation of **LT8228** and **LT8551** enhances the backup **discharging power** to **3kW** and the **charging power** to **250W**.

To serve as the battery management system device for the BBU, :adi:`ADBMS6948` has been introduced. Paired with its dedicated microcontroller, :adi:`MAX32625`, it has the capability to provide comprehensive routine maintenance and monitoring of the BBU's battery stack.

With regards to power system and fault monitoring, the power management IC, :adi:`LTC2971`, was employed in conjunction with :adi:`MAX32690`, acting as the primary microcontroller and brain of the BBU. **MAX32690** is responsible for logic control, communications, housekeeping, and fault handling within the BBU.

.. image:: https://wiki.analog.com/_media/resources/eval/bbu_block_diagram.svg
   :align: center

Graphical User Interface
------------------------

A graphical user interface has been created to offer a visual logical sequence of operations for the device, ensuring a meticulously planned execution of housekeeping and protection tasks. The GUI also plays a pivotal role in facilitating well-organized and object-oriented monitoring, reading, and providing easy access for customers.

The graphical user interface (GUI) for the BBU module is divided into various sections, each offering crucial information to the user. The following details the functions of each section:

-   Module operation status indicator
-   Module internal temperature readings
-   Module fault indicator table
-   Fan speed indicator (in rpm)
-   Power Converter metrics information
-   Cells information (voltage and temperature)

The GUI only allows the display of one module at a time, and users have the flexibility to select which specific module's data they want to view on the interface.

.. image:: https://wiki.analog.com/_media/resources/eval/bbu_gui.jpg
   :align: center

More Information
----------------

Technical Articles
~~~~~~~~~~~~~~~~~~

A comprehensive five-part technical article series about the BBU reference design will be published on Analog Dialogue, commencing in December 2023. Stay tuned for the release of the articles, and links to each installment will be provided.

-  :adi:`Smart Battery Backup for Uninterrupted Energy Part 1: Electrical and Mechanical Design - December 2023 <en/analog-dialogue/articles/smart-battery-backup-for-uninterrupted-energy-part1.html#>`
-  :adi:`Smart Battery Backup for Uninterrupted Energy Part 2: BBU Microcontroller Functions and Operations - February 2024 <en/analog-dialogue/articles/smart-battery-backup-for-uninterrupted-energy-part-2.html>`
-  :adi:`Smart Battery Backup for Uninterrupted Energy Part 3: Battery Management System - March 2024 <en/analog-dialogue/articles/smart-battery-backup-for-uninterrupted-energy-part3.html>`
-  :adi:`Smart Battery Backup for Uninterrupted Energy Part 4: BBU Shelf Operation - April 2024 <en/analog-dialogue/articles/smart-battery-backup-for-uninterrupted-energy-part4.html>`
-  :adi:`Smart Battery Backup for Uninterrupted Energy Part 5: Auxiliary Power System - May 2024 <en/analog-dialogue/articles/smart-battery-backup-for-uninterrupted-energy-part5.html>`

External Webinar
~~~~~~~~~~~~~~~~

Feel free to watch this :ez:`Webinar <webinar/c/e/561>` which talks about the complete design journey for the company's BBU Reference design which meets the OCP ORV3 specification for data centers.

Support
~~~~~~~

Analog Devices can provide online support for anyone using any components used on the reference design through posting a question on the :ez:`EngineerZone <power>`. Feel free to click on this :ez:`link <power/f/q-a/p/addpost>` to redirect you to the "Ask a question" page.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/bbu_orv3_architecture.jpg
   :width: 350px
