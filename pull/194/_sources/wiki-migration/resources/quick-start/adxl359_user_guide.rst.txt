-- ADXL359 User Guide --
========================

| *Useful links:
  ADXL359* :adi:`product page <adxl359>` *\|* :adi:`datasheet <media/en/technical-documentation/data-sheets/adxl359.pdf>`\ *.
  *
| ===== Device Overview ===== The :adi:`adxl359` is a low noise density, low 0 g offset drift, low power, 3-axis accelerometer with selectable measurement range (10g, 20g, and 40g). The ADXL359 offers industrial leading noise, minimal offset drift over temperature, and long-term stability, enabling precision applications with minimal calibration.

The low drift, low noise, and low power ADXL359 enables accurate tilt measurement in an environment with high vibration, such as airborne IMUs. The low noise over higher frequencies is ideal for wireless condition monitoring.

The ADXL359 multifunction pin names may be referenced only by their relevant function for either the SPI or limited I2C interface.

.. image:: https://wiki.analog.com/_media/resources/quick-start/cc-14-2_adxl359.png
   :align: center
   :width: 400px

Evaluation Board Overview
-------------------------

The EVAL-ADXL359Z is an evaluation board that allows quick evaluation of the performance of the ADXL359 low noise, low power accelerometer. This board is ideal for evaluation the ADXL359 in existing systems because the stiffness and small size of the board minimize the effect of the board on both the system and acceleration measurements. Full details about the ADXL359 are available in the ADXL359 datasheet.

Evaluation Board Hardware
-------------------------

The EVAL-ADXL359Z allows users to access the individual connections of the ADXL359 and includes decoupling capacitors for the supplies, a few discrete resistors that provide isolation on the V1P8ANA and V1P8DIG pins, and two 6-pin headers. Refer to the ADXL359 datasheet for more details on the specific pin definitions. The power supplies for the ADXL359 are decoupled using multiple 0.1 μF ceramic (0603) capacitors.

The EVAL-ADXL359Z uses two 6-pin headers to provide access to all pins. Header P1 provides access to VDDIO, VDD (which connects to the ADXL359 VSUPPLY pin), VSS/VSSIO (supply common connection), INT1, INT2, DRDY, as shown below.

.. image:: https://wiki.analog.com/_media/resources/quick-start/header_p1.png
   :align: center
   :width: 200px

Header P2 provides access to V1P8ANA, V1p8DIG, MISO/ASEL, /CS/SCL, SCLK/VSSIO, and MOIS/SDA, as shown below.

.. image:: https://wiki.analog.com/_media/resources/quick-start/header_p2.png
   :align: center
   :width: 200px

The vias or headers allow the evaluation board to attach to either a prototyping breadboard or a printed circuit board (PCB) in an existing user system. Four holes are provided in the corners of the evaluation board for mechanical attachment of the evaluation boards in many applications. An external host processor is required for communication to the ADXL359.

The dimensions of the evaluation board are 0.8 in x 0.8 in.

Circuit Description
-------------------

The ADXL359 has two power modes. It can be powered either by integrated, low dropout (LDO) regulators or by external user supplied 1.8 V regulated supplies. Refer to the ADXL359 datasheet for more information.

Handling Considerations
-----------------------

The EVAL-ADXL359Z is not reverse polarity protected. Reversion any of the supply connections, including the VSS and the VSSIO pins, can cause damage to the ADXL359.

Dropping the evaluation boards on a hard surface can generate several thousand g of acceleration, which can exceed the ADXL359 datasheet absolute maximum limits.

Evaluation Board Schematic
--------------------------

.. image:: https://wiki.analog.com/_media/resources/quick-start/schematic.png
   :align: center
   :width: 600px
