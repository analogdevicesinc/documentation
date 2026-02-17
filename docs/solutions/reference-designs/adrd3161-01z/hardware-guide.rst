ADRD3161-01Z Hardware Guide
===========================

.. figure:: res/adrd3161-01z-annotated.lfs.svg
   :align: center
   :width: 40em

   ADRD3161-01Z Motor Control board

========== ========= ==================================================================
Annotation Component Function
========== ========= ==================================================================
1          P10       DC power connection, 9 - 70 V
2          P3        :ref:`Motor windings connection <adrd3161_winding_connections>`
3          P8, P9    :ref:`CAN bus connections <adrd3161_cable_can>` (daisy-chainable)
4          P7        TMC9660 debug port
5          P6        MAX32662 debug port
6          DS3       :ref:`FAULT LED (CiA 303-3) <adrd3161_status_leds>`
7          DS2       :ref:`RUN LED (CiA 303-3) <adrd3161_status_leds>`
8          S1, S3    :ref:`Reset switches <adrd3161_reset_switches>`
9          S2        :ref:`Address selection switch <adrd3161_address_selection>`
10         P16       :ref:`Encoder cable <adrd3161_cable_encoder>` connection
========== ========= ==================================================================

.. _adrd3161_winding_connections:

Motor winding connections
-------------------------

.. warning::

   Wire colors are not standard and vary between motors.
   These tables reflect the wiring of Trinamic motors.
   Check your motor's datasheet!

.. tab-set::

   .. tab-item::  Stepper

        =========== ========== ========
        Motor phase Wire color Terminal
        =========== ========== ========
        A+          Black      UX1
        A-          Green      VX2
        B+          Red        WY1
        B-          Blue       Y2
        =========== ========== ========

   .. tab-item:: Brushless DC

        =========== ========== ========
        Motor phase Wire color Terminal
        =========== ========== ========
        U           Yellow     UX1
        V           Red        VX2
        W           Black      WY1
        =========== ========== ========

   .. tab-item:: Brushed DC

        =========== ========== ========
        Motor phase Wire color Terminal
        =========== ========== ========
        M+          Red        UX1
        M-          Black      VX2
        =========== ========== ========

.. _adrd3161_status_leds:

Status LEDs
-----------

The LEDs on the board signal the CANopen status according to CiA 303-3.

.. table:: CiA 303-3 RUN LED patterns

   ==================== ==========================================
   RUN LED (Blue, DS2)  CANopen NMT state
   ==================== ==========================================
   Solid on             OPERATIONAL
   Blinking 2.5 Hz      PRE-OPERATIONAL
   Single flash         STOPPED
   Flickering 10 Hz     AutoBaud/LSS *(not currently implemented)*
   ==================== ==========================================

.. table:: CiA 303-3 ERR LED patterns

   ================== ================================================
   ERR LED (Red, DS3) CANopen error state
   ================== ================================================
   Off                No error
   Single flash       Warning limit reached: too many CAN error frames
   Double flash       Error Control Event
   Triple flash       Sync timeout
   Flickering 10 Hz   AutoBaud/LSS *(not currently implemented)*
   Solid on           CAN bus off: **needs board reset**
   ================== ================================================

.. _adrd3161_reset_switches:

Reset switches
--------------

Switches RST_TMC and RST_MCU reset the TMC9660 motor drive and MAX32662 application processor, respectively. Press them in the order: RST_TMC, RST_MCU to do a full board reset.

.. _adrd3161_address_selection:

Address selection switch
------------------------

The boards' CANopen node IDs can be configured using the DIP switch S2. The CANopen node ID is ``0x10`` + the binary value of the DIP switches. Assigning node IDs via CANopen LSS is not supported yet. Most CAN messages sent and received by a specific device will have the lower 7 bits set to the node ID, allowing for easy identification when monitoring the bus:

=============== =============== ================
Switch position CANopen node ID CAN frame IDs
=============== =============== ================
 𜹥 (111)        0x17 (default)  ``x17``, ``x97``
 𜹵 (110)        0x16            ``x16``, ``x96``
 𜹩 (101)        0x15            ``x15``, ``x95``
 𜹹 (100)        0x14            ``x14``, ``x94``
 𜹦 (011)        0x13            ``x13``, ``x93``
 𜹶 (010)        0x12            ``x12``, ``x92``
 𜹪 (001)        0x11            ``x11``, ``x91``
 𜹺 (000)        0x10            ``x10``, ``x90``
=============== =============== ================

.. _adrd3161_cable_encoder:

Encoder cable
-------------

Header P16 provides 5V power to encoders and has isolated inputs corresponding to ABN and Digital Hall encoders.

Depending on the used motor and its wiring, you may need to customize the encoder cable. Some examples:

.. tab-set::

   .. tab-item:: ADI Trinamic ABN (Default)

      Encoder cable for ADI Trinamic ABN encoders, such as the
      :adi:`ADI Trinamic TMCS <en/product-category/motor-encoders.html>` series, and the builtin encoders on
      :adi:`ADI Trinamic QSH <en/product-category/stepper-motors.html>` series stepper motors.

      .. image:: res/cable-encoder-stepper.lfs.svg
      .. .. wireviz:: res/cable-encoder-stepper.wireviz.yaml

   .. tab-item:: BLDC with Hall
      
      Encoder cable for a generic BLDC with Digital Hall sensor configuration, with no special encoder connector, such as the
      :adi:`ADI Trinamic QBL <en/product-category/bldc-brushless-dc-motors.html>` series.


      .. image:: res/cable-encoder-bldc.lfs.svg
      .. .. wireviz:: res/cable-encoder-bldc.wireviz.yaml

   .. tab-item:: BLDC with Hall, VESC-like connector

      Encoder cable for using a Digital Hall sensor with a VESC-like encoder connector (6-pin JST PH), such as the
      `REV-21-1650 <https://revrobotics.eu/rev-21-1650/>`_.

      .. image:: res/cable-encoder-bldc-vesc.lfs.svg
      .. .. wireviz:: res/cable-encoder-bldc-vesc.wireviz.yaml

   .. tab-item:: BLDC with Hall & ADI Trinamic ABN

      Encoder cable for using both an ADI Trinamic ABN encoder and a Digital Hall sensor.

      .. image:: res/cable-encoder-bldc-abn.lfs.svg
      .. .. wireviz:: res/cable-encoder-bldc-abn.wireviz.yaml

.. _adrd3161_cable_can:

CAN cable
---------

The ADRDx161 board family communicates via CAN bus. The two headers P8, P9 allow for daisy-chaining CAN devices.

.. image:: res/cable-can.lfs.svg
.. .. wireviz:: res/cable-can.wireviz.yaml

.. _adrd3161_design_files:

Design support files
--------------------

A design support package consisting of the board schematic, layout, assembly and fabrication files, and more, can be downloaded from the :adi:`ADRD3161-01Z` page. If you intend to build your own board from scratch, follow the :doc:`production-guide` for the necessary first-time programming steps.
