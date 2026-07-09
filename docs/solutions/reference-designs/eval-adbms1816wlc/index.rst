.. _eval-adbms1816wlc:

EVAL-ADBMS1816WLC
=================

E2/E3W BMS Extension Board

Overview
--------

.. figure:: eval-adbms1816wlc_board.png
   :width: 600 px

   EVAL-ADBMS1816WLC Board

The :adi:`EVAL-ADBMS1816WLC` is an expansion and evaluation platform 
designed to work in conjunction with the :adi:`AD-BMSE2E3WLC-48V` Baseboard, 
providing additional cell-monitoring capability for battery packs used 
in Electric 2-Wheeler (E2W), Electric 3-Wheeler (E3W), 
and Light Electric Vehicle (LEV) applications.  

The board is built around the :adi:`ADBMS1816W <ADBMS1816>` battery-monitoring IC, 
which enables precise measurement of battery cell voltages 
as part of the :adi:`AD-BMSE2E3WLC-SL` reference design.

Designed for seamless integration, the EVAL-ADBMS1816WLC Daughter Board 
connects to the AD-BMSE2E3WLC-48V Baseboard through isoSPI communication, 
supporting scalable and daisy-chain-ready battery management architectures.  

The board includes Arduino-compatible headers and dedicated cell connectors, 
that simplify hardware setup and system expansion. 

When combined with the AD-BMSE2E3WLC software ecosystem, firmware examples, 
and GUI tools, the daughter board enables real-time cell-voltage monitoring, 
diagnostics, data visualization, and rapid evaluation of battery management algorithms 
for a wide range of rechargeable battery chemistries and energy-storage applications. 

Features
--------

**Wide Range BMS System**

 - can handle from 36V to 48V, can operate up to 100A

**Battery Chemistry Compatibility**

 - Supports multiple battery chemistries: Ni-MH, Li-ion, LiFePO4, Sodium-ion

**System Integration**

 - Can be used with Arduino-based microcontroller board
 - Plug-and-play integration

**Monitoring Capabilities**

 - Cell voltage accuracy: ±3.0mV
 - Temperature monitoring: Up to 8 sensors
 - SOC/SOH Coulomb counting
 - High-side and low-side current sensing

**Connectivity and Software**

 - Daisy-chaining ready for multi-board configurations 
 - With comprehensive GUI that is compatible with any PC/laptop 
   and enables real-time battery monitoring and diagnostics

Applications
------------

 - Medium to High Performance Electric and Hybrid 2-and 3-Wheeler Vehicles
 - Light Electric Vehicles
 - BMS Battery Research and Development
 - Adaptive Battery Type System Monitoring
 - Portable Energy Storage Systems

System Architecture
-------------------

.. figure:: eval-adbms1816wlc-block_diagram.png
   :width: 800 px

   EVAL-ADBMS1816WLC Simplified Block Diagram

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
how to use the EVAL-ADBMS1816WLC reference design:

   .. toctree::
      :titlesonly:
      :glob:

      */index

Resources
---------

 - :adi:`ADBMS1816W Data Sheet </media/en/technical-documentation/data-sheets/adbms1816w.pdf>`

Design & Integration Files
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Download

      :adi:`EVAL-ADBMS1816WLC Design Support Package <media/en/reference-design-documentation/design-integration-files/eval-adbms1816wlc-designsupport.zip>`

      * Schematic
      * PCB Layout
      * Bill of Materials
      * Allegro Project

Help and Support
----------------

For questions and more information, please visit the :ez:`EngineerZone Support Community </>`.
