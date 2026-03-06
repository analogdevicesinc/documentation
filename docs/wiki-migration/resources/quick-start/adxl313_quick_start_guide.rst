-- ADXL313 Quick Start User Guide --
====================================

DEVICE OVERVIEW
---------------

The :adi:`adxl313` is a 3-axis, low *g* accelerometer capable of sensing a full-scale range of up to ±4 *g*, with 13 bits resolution. The ADXL313 reports positive acceleration when it is accelerated in the direction of the sensing axes shown in Figure 1.

.. image:: https://wiki.analog.com/_media/resources/quick-start/xl-sensigaxes.png
   :align: center
   :width: 300px

Gravity, which is a constant +1 *g* acceleration force, also factors into the overall response of the ADXL313. Figure 2 shows the output response to gravity. The user must be careful to account for gravity, because it can affect the output of one or more of the sensor axes.

.. image:: https://wiki.analog.com/_media/resources/quick-start/xl-orientation2gravity.png
   :align: center
   :width: 800px

The ADXL313 is supplied in a small, thin 5 mm × 5 mm × 1.45 mm, 32-lead LFCSP package and is pin compatible with the ADXL312 accelerometer device. Refer to the ADXL313 data sheet for the recommended printed circuit board land pattern.

SERIAL COMMUNICATIONS CONFIGURATION
-----------------------------------

SPI:
~~~~

The ADXL313 accepts commands via either the I2C or the SPI standard communication protocols. The SPI interface is compatible with either 3-wire or 4-wire configurations. Figure 3 shows the recommended electrical connections for 4-wire SPI. When using the 3-wire SPI configuration, disconnect the SDO pin.

.. image:: https://wiki.analog.com/_media/resources/quick-start/xl313-4wirespi.png
   :align: center
   :width: 400px

The recommended power supply decoupling capacitor values are: Cs = 1uF (tantalum) and Cio = 0.1uF (ceramic), both placed as close as possible to the ADXL313 sensor.

The ADXL313 is always configured as a slave device, the maximum clock speed is 5Mhz and the timing scheme follows clock polarity (CPOL)=1 and clock phase (CPHA)=1. For the microcontroller, these settings are normally stored in the control registers. Refer to the :adi:`ADXL313 datasheet <media/en/technical-documentation/data-sheets/ADXL313.pdf>` for timing specifications and a command sequence.

I2C:
~~~~

Figure 4 shows the recommended electrical connection for I2C communications (SDO/ALT ADDRESSS pin connected to GND). The 7-bit I2C address for the device is 0x53, followed by the R/W bit. The user can select an alternate I2C address by connecting the SDO/ALT ADDRESS pin to the VDD I/O pin, in which case the 7-bit I2C address is 0x1D, followed by the R/W bit.

.. image:: https://wiki.analog.com/_media/resources/quick-start/xl313-i2c.png
   :align: center
   :width: 400px

External pull-up resistors, Rp, are necessary for proper I2C operation. Refer to the `UM10204 I2 C-Bus Specification and User Manual, Rev. 6—4 April 2014 <https://www.nxp.com/docs/en/user-guide/UM10204.pdf>`__, chapter 7, section 1 (Pull-up resistor sizing) when selecting pull-up resistor values.

The ADXL313 support standard (100 kHz) and fast (400 kHz) data transfer modes. Refer to the :adi:`ADXL313 datasheet <media/en/technical-documentation/data-sheets/ADXL313.pdf>` for timing specifications and a command sequence.

INITIALIZATION
--------------

When powered, the ADXL313 is in Standby mode by default. It is recommended to confirm the validity of a communication sequence by reading the DEVID_0 register (Address 0x00). The DEVID_0 register is read-only, and contains the value 0xAD, identifying Analog Devices, Inc. as the device manufacturer. If the data read from DEVID is not 0xAD, it indicates that either the physical connection or command sequence is incorrect. Alternatively, you can confirm that the device under test is the ADXL313 by reading the PARTID register (0x02). This register is also read-only and should return the value 0xCB (to be interpreted as an octal value that corresponds to 313).

The flow diagram bellow shows an example of the simplest initialization routine for synchronous data acquisition at the default Output Data Rate (ODR) of 100Hz, using DATA_READY interrupt mapped to INT1 pin:

.. image:: https://wiki.analog.com/_media/resources/quick-start/xl313-initseq.png
   :align: center
   :width: 600px

The DATA_READY interrupt signal indicates that all three axes of acceleration data have been updated in the data registers. It is latched high when new data is ready. Use the low-to-high transition to trigger action on an interrupt service routine. Data is read from the DATAX0, DATAX1, DATAY0, DATAY1, DATAZ0, and DATAZ1 registers (0x32 to 0x37). To ensure data coherency, use multibyte reads to retrieve data from the ADXL313. The DATA_READY interrupt is cleared once the data is read. The interrupt behavior, latch high or latch low, can be configured through the DATA_FORMAT register. Refer to the ADXL313 data sheet for details.

.. tip::

   Always make that the ADXL313 is in Standby mode first before configuring any register.


DATA FORMAT
^^^^^^^^^^^

The ADXL313 registers length is 8 bits, while its acceleration in full resolution is 13 bits. Thus the acceleration data of each axis is stored in two registers. For example, for X-axis DATAX0 is the low byte register and DATAX1 is the high byte register. Once acceleration data is acquired from data registers, the user must reconstruct the data as a 16-bits word length.

In this case, in full resolution, the upper four bits are sign bits (see Figure bellow).

.. image:: https://wiki.analog.com/_media/resources/quick-start/xl-dataconstruction.png
   :align: center
   :width: 400px

In programming language this will be equivalent to:

::

   X_16bits = DATAX1 << 8 | DATAX0;

with X_16bits a variable defined as uint16.

Also make sure to zero the unwanted MSB (14th to 16th bit) by doing:

::

   X_raw  = X_16bits & 0x1FFF;

where **X_raw** is uint16 that contains actual acceleration information formatted as **two's complement**.

The two's complement function can be implemented with the following code:

::

   int twos_complement(uint16_t value, int bits){
       int val = 0;
       val = (int) value;
       if (val & (1 << (bits-1))){
           val -= 1 << bits;
       }
       return val;
   }

For this example, the argument **value** will be X_raw and the argument **bits** will be 13 (full resolution).

To calculate the acceleration value in units of *g*, multiply the two's complement value obtained times the Scale Factor (1/sensitivity, units: [g]/LSB) at the given range and resolution. For this example, the Scale Factor is 4 [g]/ 1024 LSB which is equal to 3.9[m\ *g*]/LSB.

In code this is:

::

   X_g = (twos_complement(X_raw,13))*0.0039;

where **X_g** is the X-axis acceleration in units of *g*.

.. tip::

   Always review the :adi:`ADXL313 datasheet <media/en/technical-documentation/data-sheets/ADXL313.pdf>` for detailed information

