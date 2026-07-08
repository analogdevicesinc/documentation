.. _adbmse2e3wlc-48v:

AD-BMSE2E3WLC-48V
=================

48V Battery Monitor for E2/E3W Applications

Overview
--------

.. figure:: ad-bmse2e3wlc-48v_baseboard.png
   :width: 600 px

   AD-BMSE2E3WLC-48V Board

The **AD-BMSE2E3WLC-48V** is the baseboard of the
AD-BMSE2E3WLC-SL Solution Kit, developed to simplify the evaluation and
development of Battery Management Systems (BMS) for Electric 2-Wheeler
(E2W), Electric 3-Wheeler (E3W), Light Electric Vehicle (LEV), and
energy storage applications. 

Operating over a battery voltage range of **36V to 48V** and 
supporting currents up to **100A**, the board integrates battery monitoring, 
current sensing, power-path control, communication interfaces, 
and MCU connectivity into a single platform.

When paired with the **EVAL-ADBMS1816WLC Daughter Board**, it enables
high-accuracy cell voltage measurement, temperature monitoring, SOC/SOH
estimation, and battery protection functions required for modern
electric mobility systems.

Built around the automotive-grade :adi:`ADBMS1816W <ADBMS1816>` battery monitoring IC,
the AD-BMSE2E3WLC-48V Baseboard supports multiple battery chemistries,
including Li-ion, LiFePO4, Ni-MH, and Sodium-ion batteries. Its
MCU-agnostic architecture, Arduino-compatible headers, FeatherWing
connector, and isoSPI communication interface provide flexibility for
integration into centralized, distributed, or modular BMS architectures.

The platform also includes charge and discharge control circuitry,
high-side and low-side current sensing, daisy-chain capability for
higher cell-count systems, and compatibility with open-source firmware
and GUI software for real-time monitoring, diagnostics, visualization,
and rapid prototyping of BMS applications.

Features
--------

**Wide Range BMS System**

 - can operate from 36V to 96V, can handle up to 100A

**Battery Chemistry Compatibility**

 - Supports multiple battery chemistries: Ni-MH, Li-ion, LiFePO4,
   Sodium-ion, and others

**System Integration**

 - Plug-and-play integration
 - MCU-agnostic design for easy integration into existing systems
 - Flexible topology support: Centralized, Distributed, and Modular
   configurations

**Monitoring Capabilities**

 - Cell voltage accuracy: ±3.0mV
 - Temperature monitoring: Up to 8 sensors
 - SOC/SOH Coulomb counting
 - High-side and low-side current sensing

**Vehicle State Management**

 - E2W/E3W vehicle state condition readiness
 - Support for Driving, Charging, Parking, and Fault states

**Connectivity and Software**

 - Daisy-chaining ready for multi-board configurations
 - Comprehensive GUI compatible with any PC/laptop
 - Integrated firmware and GUI software suite
 - Real-time monitoring, diagnostics, and data plotting capabilities
 - Open-source BMS example codes provided

Applications
------------

 - Medium to High Performance Electric and Hybrid 2-Wheeler and 3-Wheeler Vehicles
 - Light Electric Vehicles
 - BMS Battery Research and Development
 - Adaptive Battery Type System Monitoring
 - Portable Energy Storage Systems

System Architecture
-------------------

.. figure:: ad-bmse2e3wlc-48v_block_diagram.png
   :width: 600 px

   AD-BMSE2E3WLC-48V Simplified Block Diagram

Specifications
--------------

+----------------------+-------+---------+-------+------+------------------+
| **Parameter**        | Min   | Typical | Max   | Unit | **Notes**        |
+======================+=======+=========+=======+======+==================+
| **ADBMS1816W Cell    |       |         |       |      |                  |
| Monitor**            |       |         |       |      |                  |
+----------------------+-------+---------+-------+------+------------------+
| VREG Supply          | 4.5   | 5       | 5.5   | V    |                  |
+----------------------+-------+---------+-------+------+------------------+
| VREF1, VREF2         | 3     | -       | 3.3   | V    | Supply to        |
|                      |       |         |       |      | internal ADCs    |
+----------------------+-------+---------+-------+------+------------------+
| VRES/VDD             | 4.5   | 5       | 5.5   | V    |                  |
+----------------------+-------+---------+-------+------+------------------+
| Operating            | -40   | -       | 125   | °C   |                  |
| Temperature          |       |         |       |      |                  |
+----------------------+-------+---------+-------+------+------------------+
| CPIN Input Range     | -2.5  | -       | 5.5   | V    |                  |
+----------------------+-------+---------+-------+------+------------------+
| Cell Count           | 1     | -       | 32    | -    | Minimum 17 cells |
|                      |       |         |       |      | to initiate      |
|                      |       |         |       |      | daisy chain      |
+----------------------+-------+---------+-------+------+------------------+
| Drive Voltage Range  | -0.3  | -       | 6     | V    | Relative to each |
|                      |       |         |       |      | cell monitor V-  |
+----------------------+-------+---------+-------+------+------------------+
| VP Range             | 16    | -       | 80    | V    |                  |
+----------------------+-------+---------+-------+------+------------------+
| VREG Pack Monitor    | 4.5   | 5       | 5.5   | V    |                  |
+----------------------+-------+---------+-------+------+------------------+

User Guides
-----------

Proceed to the following pages for detailed information on 
how to use and evaluate the AD-BMSE2E3WLC-48V reference design:

   .. toctree::
      :titlesonly:
      :glob:

      */index

Resources
---------

 - :adi:`ADBMS1816 Data Sheet <media/en/technical-documentation/data-sheets/adbms1816w.pdf>`
 - :adi:`ADBMS1816 Product Page <adbms1816>`
 - :adi:`LTC7000 Product Page <ltc7000>`

Design & Integration Files
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Download

      :adi:`AD-BMSE2E3WLC-48V Design Support Package <media/en/reference-design-documentation/design-integration-files/ad-bmse2e3wlc-48v-designsupport.zip>`

      * Schematic
      * PCB Layout
      * Bill of Materials
      * Allegro Project

Help and Support
----------------

For questions and more information, please visit the :ez:`EngineerZone Support Community </>`.
