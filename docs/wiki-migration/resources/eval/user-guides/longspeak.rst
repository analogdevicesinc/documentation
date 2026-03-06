ADAR3003,3002 (Longs Peak) ANALOG BEAMFORMER
============================================

(UNDER CONSTRUCTION)
====================

GENERAL DESCRIPTION
===================

Main RFICs
----------

ADAR3002: 17–21 GHz, 4-Channel, Dual Beam Ka Band Receive Beamformer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ADAR3003: 27-31 GHz, 4-Channel, Ka Band Transmit Beamformer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Peripheral ICs
--------------

RF Detector Block
~~~~~~~~~~~~~~~~~

::

   * 

Power Generation
~~~~~~~~~~~~~~~~

::

   * 

Control & Monitoring
~~~~~~~~~~~~~~~~~~~~

::

   * 

--------------

REQUIREMENTS
============

Documents
---------

::

   * 
   * Rev. A design:
     * 
   * Rev. B/C design:
     * 

Hardware
--------

::

   * 

Suggested Test Equipment
------------------------

-  40GHz RF Signal Generator
-  40GHz Spectrum Analyzer
-  40GHz Vector Network Analyzer
-  Thermal Camera (optional)
-  Oscilloscope (optional)
-  RF Power Meter (optional)

Software/Digital Control
------------------------

PMOD Control
~~~~~~~~~~~~

Software
~~~~~~~~

--------------

BOARD DESIGN
============

Power Supply
------------

The ADAR1000-EVAL1Z board must be powered from the included power supply with a voltage level of 12V. There is an on-board power management tree which generates the required voltage rails for all of the associated parts.

RF Input and Output Signals
---------------------------

Digital Signals
---------------

PMOD Pinout
^^^^^^^^^^^

SPI Control
^^^^^^^^^^^

EVALUATION
==========

Hardware Setup
--------------

Mechanical Parts
~~~~~~~~~~~~~~~~

Mechanical Assembly
~~~~~~~~~~~~~~~~~~~

Test Setup Assembly
~~~~~~~~~~~~~~~~~~~

Board Power Control
-------------------

Powerup Procedure
^^^^^^^^^^^^^^^^^

Powerdown Procedure
^^^^^^^^^^^^^^^^^^^

Software Control
----------------

::

   * 

Recommended ADAR3003/3002 Initialization Sequences
==================================================

<WRAP note>

Max Gain & 0° Phase
-------------------

Disable
-------

Tx Enable (Reduced Power)
-------------------------

Longs Peak Board Cell & Channel Maps
====================================

Cell Map
--------

Channel Map
-----------

Channel Map (Back of Board)
---------------------------
