-- ADXL317 Quick Start User Guide --
====================================

Device Overview
---------------

The :adi:`adxl317` is a 3-axis, 4kHz bandwidth accelerometer, capable of sensing a full-scale range of ±16 *g*, with 14 bits resolution. This sensor is well suited for wideband active noise control (ANC) applications, featuring very low latency from the moment of acceleration to the transmission of digital output data, even in noisy scenarios. The ADXL317 is designed to interface directly with the AD2425W A2B transceiver, or with any other I2S capable A2B transceiver, microcontroller or SDP.

The ADXL317 reports positive acceleration when it is accelerated in the direction of the sensing axes shown in Figure 1.

.. image:: https://wiki.analog.com/_media/resources/quick-start/xl-sensigaxes.png
   :align: center
   :width: 200px

.. container:: center lo

   **Figure 1:** Sensing axis.


Gravity, which is a constant +1 *g* acceleration force, also factors into the overall response of the ADXL317. Figure 2 shows the output response to gravity. The user must be careful to account for gravity, because it can affect the output of one or more of the sensor axes.

.. image:: https://wiki.analog.com/_media/resources/quick-start/xl-orientation2gravity.png
   :align: center
   :width: 500px

.. container:: center lo

   **Figure 2:** Acceleration response with respect to gravity.


The ADXL317 is supplied in a small, thin, 5 mm × 5 mm × 1.45 mm, 32-pin LFCSP package. The device is qualified for use in automotive applications over the entire operating temperature range of –40°C to +125°C.

Application Circuit
-------------------

The ADXL317 has a single power input pin, VCC, which operates at a nominal voltage of 3.3 V. An internal regulator steps this voltage down to 1.8 V, accessible via VDD pin. The VCC and VDD pin must be properly bypassed, as shown in Figure 3, to remove ac fluctuations from the power supply. All its logic inputs and outputs support only 1.8V logic. This device has no internal clock, thus, clock must be supplied externally and must always be running at a rate of either 3.072 MHz or 6.144 MHz for the device to operate properly.

The figure bellow shows the recommended application circuit for this device.

.. image:: https://wiki.analog.com/_media/resources/quick-start/xl317_basic_config3.png
   :align: center
   :width: 500px

.. container:: center lo

   **Figure 3:** Recommended application circuit. ALT_ADDR may be grounded or connected to VDD. The exposed pad on the bottom of the package must be connected to ground.


The ADXL317 counts with two digital interfaces i2C and I2S. In both cases, the ADXL317 operates as a slave device, receiving commands and responding with requested data. These two ports operate independently and use separate pins. Therefore, these ports can be used simultaneously.

I2C for device configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I2C is used to configure the ADXL317 but it also provides access to the acceleration data only at the standard 100 kHz data transfer rate. Refer to the :adi:`ADXL317 datasheet <media/en/technical-documentation/data-sheets/ADXL317.pdf>` for timing specifications and a command sequence.

The two I2C lines, SCL (Pin 10) and SDA (Pin 11), each require a pull-up resistor (Rp) to VDD. The value of these resistors is dependent on bus capacitance. Refer to the `UM10204 I2 C-Bus Specification and User Manual, Rev. 6—4 April 2014 <https://www.nxp.com/docs/en/user-guide/UM10204.pdf>`__, chapter 7, section 1 (Pull-up resistor sizing) when selecting pull-up resistor values. The exposed pad on the bottom of the package must be connected to ground.

I2S/TDM for data streaming
~~~~~~~~~~~~~~~~~~~~~~~~~~

I2S/TDM is used for synchronous high-speed data streaming (not for user configuration) and consist of a 4-wire interface, comprising one continuous serial clock (BCLK), one synchronization signal (SYNC), and two serial data channels (DTX0 and DTX1), see Figure 3. It supports four packet formats, depending on the input clock frequency and system requirements:

-  3.072 MHz clock:

   -  32-bit I2S/TDM2 (two data pins)

      -  16-bit TDM4

-  6.144 MHz clock:

   -  32-bit TDM4

      -  16-bit TDM8.

Note that 32-bit I2S/TDM2 mode requires two data pins, whereas the other three modes require only one. For all package formats, the frame frequency is 48kHz.

.. important::

   The ADXL317 clock frequency have some tolerance, but the frame frequency must respect the number of bits per frame required for each package format. For example, if clock frequency used is 3MHz, and the device is configured for 16-bit TDM4 format, each frame must contain exactly 64 clock periods (64-bits). Therefor, the frame frequency will be 3MHz/64bits = 46.875 kHz.


===== Initialization =====

There are a few tips that we recommend when initializing the ADXL317:

.. container:: hi

   \ **1)**\


After the part is powered up (VCC = 3.3V), wait 1ms before attempting to read/write its register map.

.. container:: hi

   \ **2)**\


After the startup time has passed (1ms), confirm the validity of a I2C communication sequence by reading the DEVID_ID0 register (Address 0x00). The DEVID register is read-only, and contains the value 0x22. If the data read from DEVID_ID0 is not 0x22, it indicates that either the physical connection or command sequence is incorrect.

.. container:: hi

   \ **3)**\


All attempts to write to any of the device writeable registers are ignored until the proper key is written to the USER_REG_KEY register (Address 0x80). This protects the device from entering into an unexpected state during potential transient activity on the I2C bus. To unlock all writeable registers complete the following procedure:

-  Write 0xBC to the USER_REG_KEY register (Address 0x80).
-  Write 0x43 to the USER_REG_KEY register (Address 0x80).

After writing these two values, all writeable registers are unlocked and can be written to as normal. The two writes must be performed using two separate, single-byte writes. A multibyte write cannot be used.

.. container:: hi

   \ **4)**\


Each axis has its own digital output filter stage (CIC filter, low pass IIR filter and high pass filter). By default all axis are configured for the higher bandwidth setting (4kHz). Modify the filters settings to adjust your needs.

.. container:: hi

   \ **5)**\


I2S/TDM package format, clock rate, frame shape and data output pin can be configured by writing on the I2S_CFG0, I2S_CFG1, and CLOCK_RATE register. The Figure 4 shows an example of the timing diagram for the following registers configuration: I2S_CFG0 = 0x91, I2S_CFG1 = 0x01 and CLOCK_RATE = 0x01. This configuration results on a 3.072MHz 16-bits TDM4 package format, with data transmission beginning on the falling edge of SYNC, and SYNC asserted for one BCLK cycle only.

.. image:: https://wiki.analog.com/_media/resources/quick-start/xl317_tdm4_2.png
   :align: center
   :width: 600px

.. container:: center lo

   **Figure 4:** Timing diagram for I2S_CFG0 = 0x91, I2S_CFG1 = 0x01 and CLOCK_RATE = 0x01.


Data format
-----------

For either I2C or I2S/TDM, the acceleration data on each axis is transmitted in two's complement, left justified, 14-bits resolution format.

When using I2C, the acceleration data of each axis is stored in two 8-bits registers. For example, for X-axis X_DATA_LO is the low byte register and X_DATA_HI is the high byte register. The user must reconstruct the data as a 16-bits word length. The two less significant bits (LSB) are always zero.

In programming language this will be equivalent to:

::

   X_16bits = X_DATA_HI << 8 | X_DATA_LO;

with X_16bits a variable defined as uint16.

To convert X_16bits from left justified to right justified:

::

   X_raw  = (X_16bits >> 2) & 0x3FFF;

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

In this case, the argument **value** will be X_raw and the argument **bits** will be 14.

To calculate the acceleration value in units of *g*, multiply the two's complement value obtained times the Scale Factor (1/sensitivity, units: [g]/LSB) at the given filter configuration. For example, if the filters are set to 4kHz bandwidth, the Scale Factor is 1.8[m\ *g*]/LSB.

In code this is:

::

   X_g = (twos_complement(X_raw,14))*0.0018;

where **X_g** is the X-axis acceleration in units of *g*.

.. tip::

   Always review the :adi:`ADXL317 datasheet <media/en/technical-documentation/data-sheets/ADXL317.pdf>` for detailed information

