.. _ad-acevsecrdset-sl:

AD-ACEVSECRDSET-SL
==================

Type 2 EVSE 3.6 kW Charging Cable
""""""""""""""""""""""""""""""""""

Introduction
------------

The :adi:`AD-ACEVSECRDSET-SL <ad-bct2ade9113-sl>` is  a complete Type 2 EVSE 3.6kW
charging cable solution, providing a reference design intended for evaluation
and prototyping of EV charging systems.

The system includes the :adi:`ADE9113` 3-channel isolated sigma-delta (Σ-Δ) ADC
for voltage and current measurement on the single-phase power input and
measurement of the relay voltage for solder contacts detection and relay
state of health. Safe operation is enabled by the inclusion of a 6mA DC / 30mA rms RCD.
Detection of overvoltage, undervoltage, overcurrent, overtemperature, and EV diode
presence are also available.

The :adi:`MAX32655` ultralow power ARM® Cortex®-M4 processor
implements the logic for system control and communication with the EV over the
control pilot interface. A programming and debugging interface are included.
The MAX32655 Bluetooth 5.2 interface enables connectivity to external devices.

The design is accompanied by an open-source software stack and reference
applications, enabling custom software development to start from a proven
implementation validated to meet the applicable standards. The system is
designed to meet the IEC61851 and IEC62752 standards.

.. figure:: ad-acevsecrdset-sl_angle.jpg
    :align: center
    :width: 600 px

    AD-ACEVSECRDSET-SL Type 2 EVSE Cordset Evaluation Kit

Features
---------

- Complete reference design for Type 2 EVSE Cordset (IC-CPD)
- Power level from 2.3kW up to 3.6kW (at 230V)
- Designed to meet the applicable standards: IEC61851, IEC62752
- Incorporates a 6mA DC/30mA rms RCD and a control pilot circuit
- Relay soldered contacts detection
- Upstream and downstream PE detection
- Overtemperature detection
- Integrated isolation
- Reduced component count for cost optimization
- Bluetooth 5.2 interface for connectivity to external devices
- Open-source software stack to enable custom firmware development

Applications
------------

- EV Charging

Block Diagram
-------------

.. figure:: block_diagram_new.png

    AD-ACEVSECRDSET-SL Simplified Block Diagram

Specifications
--------------

+-------------------------------------+--------------------------------------+
| Electrical Specs                    |                                      |
+=====================================+======================================+
| Power                               | 3.6kW                                |
+-------------------------------------+--------------------------------------+
| Input voltage                       | 230V +/-15% or 120V +/-15%           |
+-------------------------------------+--------------------------------------+
| Input current                       | 16A                                  |
+-------------------------------------+--------------------------------------+
| Input frequency                     | 50Hz / 60Hz                          |
+-------------------------------------+--------------------------------------+
| Output voltage                      | 230V +/-15% or 120V +/-15%           |
+-------------------------------------+--------------------------------------+
| Output current                      | 10A/16A                              |
+-------------------------------------+--------------------------------------+
| Output frequency                    | 50Hz / 60Hz                          |
+-------------------------------------+--------------------------------------+
| **Operating Conditions**                                                   |
+-------------------------------------+--------------------------------------+
| Operating temperature               | -25°C to +45°C                       |
+-------------------------------------+--------------------------------------+
| Residual current device             | 6mA DC / 30mA rms                    |
+-------------------------------------+--------------------------------------+
| **Safety Features**                                                        |
+-------------------------------------+--------------------------------------+
| Overvoltage category                | II                                   |
+-------------------------------------+--------------------------------------+
| Protection features                 | Relay soldered contacts detection    |
|                                     +--------------------------------------+
|                                     | Overvoltage                          |
|                                     +--------------------------------------+
|                                     | Undervoltage                         |
|                                     +--------------------------------------+
|                                     | Overcurrent                          |
|                                     +--------------------------------------+
|                                     | Overtemperature                      |
+-------------------------------------+--------------------------------------+
| Other features                      | Integrated isolation                 |
|                                     +--------------------------------------+
|                                     | Diode detection                      |
|                                     +--------------------------------------+
|                                     | Upstream and downstream PE detection |
+-------------------------------------+--------------------------------------+
| **User Interface & Control**                                               |
+-------------------------------------+--------------------------------------+
| Communication                       | Bluetooth 5.2                        |
+-------------------------------------+--------------------------------------+
| Status Indicators                   | LEDs                                 |
+-------------------------------------+--------------------------------------+
| Debugging                           | RS-232                               |
+-------------------------------------+--------------------------------------+
| Designed to the following standards |                                      |
|                                     | IEC 61851, IEC 62752                 |
+-------------------------------------+--------------------------------------+

System Setup
------------

.. toctree::
   :titlesonly:
   :glob:

   */index

Additional Information and Useful Links
---------------------------------------

- :adi:`AD-ACEVSECRDSET-SL Product Page <ad-bct2ade9113-sl>`
- :adi:`MAX32655 Product Page <MAX32655>`
- :adi:`ADE9113 Product Page <ADE9113>`
- :adi:`ADA4523-1 Product Page <ADA4523-1>`
- :adi:`ADT75 Product Page <ADT75>`
- :adi:`MAX20457 Product Page <MAX20457>`
- :adi:`LT8330 Product Page <LT8330>`

Software Resources
------------------

- :git-no-OS:`Link to the project source code <projects/ad-acevsecrdset-sl>`

Design and Integration Files
----------------------------

.. admonition:: Download

    :download:`AD-ACEVSECRDSET-SL Design & Integration Files (Rev E) <ad-acevsecrdset-sl_design_support_package_rev._e.zip>`

    - Schematics
    - PCB Layout
    - Bill of Materials
    - Allegro Project

Help and Support
----------------

For questions and more information, please visit the :ez:`/`.
