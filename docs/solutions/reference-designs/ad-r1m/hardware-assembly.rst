.. _ad-r1m-hardware-assembly:

Hardware Assembly Guide
=======================

This guide covers the complete assembly process for the AD-R1M Open Mobile Robot Platform.

Bill of Materials
-----------------

:download:`Download BOM (CSV) <res/BOM.csv>`

.. list-table:: AD-R1M Bill of Materials
   :name: table-bom
   :header-rows: 1
   :widths: 8 5 20 35 32

   * - Ref
     - Qty
     - P/N
     - Description
     - Link
   * - 3D1
     - 4
     - N/A
     - 16 mm caster raiser
     -
   * - 3D2
     - 2
     - N/A
     - Motor mounts
     -
   * - 3D3
     - 2
     - N/A
     - 3D printed camera mount brackets
     -
   * - 3D4
     - 1
     - N/A
     - 3D printed camera housing
     -
   * - 3D5
     - 2
     - N/A
     - Wheel assembly
     -
   * - 3D6
     - 1
     - N/A
     - Electronics sub-assemblies mounting plate
     -
   * - 3D7
     - 1
     - N/A
     - 3D Printed Front Panel
     -
   * - ADI1
     - 2
     - QSH5718-51-28-101-10K
     - NEMA 23 stepper motor 55Ncm, 2.8A
     - .. image:: res/qsh5718-51-28-101-10k.jpg
          :width: 80px

       :adi:`qsh5718`
   * - ADI2
     - 1
     - EVAL-ADTF3175
     - Time-of-Flight depth camera
     - .. image:: res/eval_adtf3175.png
          :width: 80px

       :adi:`EVAL-ADTF3175`
   * - ADI3
     - 1
     - ADRD3161
     - Motor Control PCB
     - .. image:: res/adrd3161.jpg
          :width: 80px

       :adi:`ADRD3161-01Z`
   * - ADI4
     - 1
     - ADRD5161
     - Battery Management System
     - .. image:: res/adrd5161.png
          :width: 80px

       :adi:`ADRD5161-01Z`
   * - ADI5
     - 1
     - ADRD4161
     - Compute Carrier
     - .. image:: res/adrd4161_board.jpg
          :width: 80px

       :adi:`ADRD4161-01Z`
   * - ADI6
     - 1
     - N/A
     - Battery Holder
     -
   * - E1
     - 1
     - RPi 5
     - Raspberry Pi 5 SBC
     -
   * - E2
     - 1
     - IND16-12B-C
     - Status LED
     -
   * - E3
     - 1
     - 82-4151.1000
     - SPDT Button
     -
   * - E4
     - 1
     - 82-4151.1123
     - SPDT Button
     -
   * - M1
     - 6
     - FA-093W201N05S01
     - Angle bracket
     -
   * - M2
     - 6
     - A-094411M4
     - Panel holder
     -
   * - M3
     - 1
     - K2020-I5 KRAFTBERG
     - 340mm Aluminum 20X20 profile
     -
   * - M4
     - 2
     - K2040-I5 KRAFTBERG
     - 530mm Aluminum 20X40 profile
     -
   * - M5
     - 1
     - K2040-I5 KRAFTBERG
     - 340mm Aluminum 20X40 profile
     -
   * - M6
     - 12
     - M5X8/D912-A4
     - Screw
     -
   * - M7
     - 28
     - FA-096215
     - M5 Profile nut
     -
   * - M8
     - 4
     - JDPE-0501-1001
     - Casters
     -
   * - M9
     - 8
     - B5X25/BN3
     - M5 25mm screw
     -
   * - M10
     - 8
     - B5/BN715
     - 5mm washer
     -
   * - M11
     - 8
     - B5X10/BN3
     - M5 10mm screw
     -
   * - M12
     - 8
     - B5/BN161
     - M5 nut lock
     -
   * - M13
     - 2
     - B4X8/BN3
     - M4 x 8 HEX
     -
   * - M14
     - 2
     - B4/BN1074
     - M4 Washer
     -
   * - M15
     - 8
     - M3X15/DR213
     - Standoff TFF
     -
   * - M16
     - 4
     - M3X20/DR113
     - Standoff TFM
     -
   * - M17
     - 8
     - M3X25/DR213
     - Standoff TFF
     -
   * - M18
     - 16
     - M3X5/D7985
     - Screw
     -
   * - M19
     - 16
     - B3X5/BN610
     - HEX Screw
     -
   * - M20
     - 8
     - B5X16/BN3
     - M5 x 16 screw
     -

Tools Required
--------------

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Tool
     - Purpose
   * - Tape measure
     - Measuring frame dimensions and diagonals
   * - Allen Key set
     - Tightening hex screws
   * - Pliers
     - General assembly
   * - Crimping tools
     - Wire harness assembly

Frame Assembly
--------------

Step 1: Base Frame
^^^^^^^^^^^^^^^^^^

Assemble the frame using aluminum profiles and angle brackets. Ensure a rectangular
shape by measuring the diagonals. Use 2 angle brackets to connect two K2040 profiles.
Place 4 "M2" holders 30mm from the interior and 2 in the middle of the 530mm profiles.

.. list-table::
   :widths: 50 50

   * - .. list-table:: Parts Required
          :header-rows: 1
          :widths: 10 8 25 57

          * - Ref
            - Qty
            - P/N
            - Description
          * - M1
            - 6
            - FA-093W201N05S01
            - Angle bracket
          * - M2
            - 6
            - A-094411M4
            - Panel holder
          * - M3
            - 1
            - K2020-I5 KRAFTBERG
            - 340mm Aluminum 20X20 profile
          * - M4
            - 2
            - K2040-I5 KRAFTBERG
            - 530mm Aluminum 20X40 profile
          * - M5
            - 1
            - K2040-I5 KRAFTBERG
            - 340mm Aluminum 20X40 profile
          * - M6
            - 12
            - M5X8/D912-A4
            - Screw
          * - M7
            - 12
            - FA-096215
            - M5 Profile nut

     - .. figure:: res/assembly/image2.jpeg
          :width: 100%

          Assembled base frame

Step 2: Caster Wheels
^^^^^^^^^^^^^^^^^^^^^

Attach the caster wheels using the 3D printed 16mm caster raisers (3D1).

.. list-table::
   :widths: 50 50

   * - .. list-table:: Parts Required
          :header-rows: 1
          :widths: 10 8 25 57

          * - Ref
            - Qty
            - P/N
            - Description
          * - M8
            - 4
            - JDPE-0501-1001
            - Casters
          * - 3D1
            - 4
            - N/A
            - 16 mm caster raiser
          * - M7
            - 8
            - FA-096215
            - M5 profile nut
          * - M9
            - 8
            - B5X25/BN3
            - M5 25mm screw
          * - M10
            - 8
            - B5/BN715
            - 5mm washer

     - .. figure:: res/assembly/image3.jpeg
          :width: 100%

          Caster wheel installation

Step 3: Motor Mounts
^^^^^^^^^^^^^^^^^^^^

Install the motor mounts (3D2) in the center of the 530mm longitudinal profiles.

.. list-table::
   :widths: 50 50

   * - .. list-table:: Parts Required
          :header-rows: 1
          :widths: 10 8 25 57

          * - Ref
            - Qty
            - P/N
            - Description
          * - 3D2
            - 2
            - N/A
            - Motor mounts
          * - M7
            - 8
            - FA-096215
            - M5 profile nut
          * - M11
            - 8
            - B5X10/BN3
            - M5 10mm screw

     - .. figure:: res/assembly/image4.jpeg
          :width: 100%

          Motor mount placement

Step 4: Motors
^^^^^^^^^^^^^^

Install the NEMA 23 stepper motors onto the motor mounts.

.. list-table::
   :widths: 50 50

   * - .. list-table:: Parts Required
          :header-rows: 1
          :widths: 10 8 25 57

          * - Ref
            - Qty
            - P/N
            - Description
          * - M20
            - 8
            - B5X16/BN3
            - M5 x 16 screw
          * - M12
            - 8
            - B5/BN161
            - M5 nut lock
          * - ADI1
            - 2
            - QSH5718-51-28-101-10K
            - NEMA 23 stepper motor

     - .. figure:: res/assembly/image5.png
          :width: 100%

          Motor installation

Step 5: Camera Mount
^^^^^^^^^^^^^^^^^^^^

Install camera mounts 116.5mm from the side, 135.5mm from camera position.
Camera mounts and housing are 3D printed.

.. list-table::
   :widths: 50 50

   * - .. list-table:: Parts Required
          :header-rows: 1
          :widths: 10 8 25 57

          * - Ref
            - Qty
            - P/N
            - Description
          * - M13
            - 2
            - B4X8/BN3
            - M4 x 8 HEX
          * - M14
            - 2
            - B4/BN1074
            - M4 Washer
          * - 3D3
            - 2
            - N/A
            - Camera mount brackets
          * - 3D4
            - 1
            - N/A
            - Camera housing
          * - ADI2
            - 1
            - EVAL-ADTF3175
            - ToF depth camera

     - .. figure:: res/assembly/image6.jpeg
          :width: 100%

          Camera and mount assembly

Step 6: Wheel Assembly
^^^^^^^^^^^^^^^^^^^^^^

Install the wheel assemblies on the motor shafts.

.. list-table:: Parts Required
   :header-rows: 1
   :widths: 15 10 20 55

   * - Ref
     - Qty
     - P/N
     - Description
   * - 3D5
     - 2
     - N/A
     - Wheel assembly

Electronics Assembly
--------------------

Step 1: Board Spacers
^^^^^^^^^^^^^^^^^^^^^

Place the board spacers on the electronics mounting plate.

.. list-table::
   :widths: 40 60

   * - .. list-table:: Parts Required
          :header-rows: 1
          :widths: 12 10 28 50

          * - Ref
            - Qty
            - P/N
            - Description
          * - 3D6
            - 1
            - N/A
            - Electronics mounting plate
          * - M15
            - 8
            - M3X15/DR213
            - Standoff TFF
          * - M16
            - 4
            - M3X20/DR113
            - Standoff TFM
          * - M17
            - 4
            - M3X25/DR213
            - Standoff TFF
          * - M18
            - 16
            - M3X5/D7985
            - Screw

     - .. list-table::
          :widths: 50 50

          * - .. figure:: res/assembly/image7.png
                 :width: 100%

                 Spacer layout (top view)

            - .. figure:: res/assembly/image8.png
                 :width: 100%

                 Spacer layout (side view)

.. figure:: res/assembly/image23.png
   :width: 350px
   :align: center

   Standoff detail view

Step 2: PCB Installation
^^^^^^^^^^^^^^^^^^^^^^^^

Install the PCB sub-assemblies. The BMS board mounts above the battery holder
on 4x M3X25 standoffs.

.. list-table::
   :widths: 40 60

   * - .. list-table:: Parts Required
          :header-rows: 1
          :widths: 12 10 28 50

          * - Ref
            - Qty
            - P/N
            - Description
          * - M19
            - 16
            - B3X5/BN610
            - HEX Screw
          * - M17
            - 4
            - M3X25/DR213
            - Standoff TFF
          * - ADI3
            - 1
            - ADRD3161
            - Motor Control PCB
          * - ADI4
            - 1
            - ADRD5161
            - BMS
          * - ADI5
            - 1
            - ADRD4161
            - Compute Carrier
          * - ADI6
            - 1
            - N/A
            - Battery Holder
          * - E1
            - 1
            - RPi 5
            - Raspberry Pi 5 SBC

     - .. figure:: res/assembly/image9.png
          :width: 100%

          Complete electronics assembly

Control Panel
-------------

.. list-table::
   :widths: 40 60

   * - .. list-table:: Parts Required
          :header-rows: 1
          :widths: 12 10 28 50

          * - Ref
            - Qty
            - P/N
            - Description
          * - E2
            - 1
            - IND16-12B-C
            - Status LED
          * - E3
            - 1
            - 82-4151.1000
            - SPDT Button
          * - E4
            - 1
            - 82-4151.1123
            - SPDT Button
          * - 3D7
            - 1
            - N/A
            - 3D Printed Front Panel

     - .. list-table::
          :widths: 50 50

          * - .. figure:: res/assembly/image10.png

                 Front panel layout

            - .. figure:: res/assembly/image11.png

                 Panel with components

Wiring Harness
--------------

.. figure:: res/assembly/image12.jpeg
   :width: 600px
   :align: center

   Main wiring diagram

Wiring Overview
^^^^^^^^^^^^^^^

.. list-table::
   :widths: 50 50

   * - .. figure:: res/assembly/image13.png

          System wiring overview

     - .. figure:: res/assembly/image14.png

          Connection routing

.. figure:: res/assembly/image15.png
   :width: 400px
   :align: center

   Wire bundle organization

.. figure:: res/assembly/image16.jpeg
   :width: 300px
   :align: center

   Completed wiring harness

Wire Assemblies
^^^^^^^^^^^^^^^

**CAN Bus Cable**

Twisted pair + GND with Molex Micro-Fit 3.0 **43025-0400** connectors on both ends.

.. figure:: res/assembly/image17.png
   :width: 500px
   :align: center

   CAN bus cable assembly

**Motor Encoder Cable**

Wire assembly with Molex Micro-Fit 3.0 **43025-0800** connector on the motor
control board side. See ADRD3161 documentation for details.

.. figure:: res/assembly/image18.jpeg
   :width: 450px
   :align: center

   Motor encoder cable pinout

**Battery Balancing Cable**

4-wire assembly with JST **XHP-4** connectors on both ends.

.. list-table::
   :widths: 60 40

   * - .. figure:: res/assembly/image19.png

          Battery balancing cable schematic

     - .. figure:: res/assembly/image20.jpeg
          :width: 560px

          Completed cable

**Power Cables**

- 2.5mm wires with bootlace ferrule
- 450mm length from BMS to motor control board (2 pairs)

.. figure:: res/assembly/image21.png
   :width: 500px
   :align: center

   Power distribution diagram

.. list-table::
   :widths: 50 50

   * - .. figure:: res/assembly/image22.png

          Wire gauge reference

     - .. figure:: res/assembly/image24.png

          Power cable routing

.. list-table::
   :widths: 50 50

   * - .. figure:: res/assembly/image25.png

          Terminal connection detail

     - .. figure:: res/assembly/image26.png

          Completed power connections
