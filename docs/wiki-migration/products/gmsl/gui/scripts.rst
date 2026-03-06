Scripts
=======

The GMSL GUI offers scripting capabilities to allow you to fully program the GMSL link without any need of an additional processor. Out GUI tools generate scripts in specific formats that are understood by the GUI but can be interpreted and converted into any other type of format.

.. important::

   GMSL scripting uses 8-bit address notation for I2C communication. This may differ from other vendors who use 7-bit address notation.


--------------

TXT Format (\*.txt)
-------------------

The format specification is as follows; inputs are all in hex WITHOUT the leading “0x”. Examples of this format can be observed in the Log Window(s).

To **read** a 16-bit register address the command is: <code> RIB <I2C_address> <Register_Address> <number of bytes> </code>

.. container:: hi

   Example:


To **read** I2C address 0x80 register 0x0001 1 byte, enter the following: <code> RIB 80 01 1 </code>

| 
| To **write** a 16-bit register address the command is: <code> WIB <I2C_address> <Register_Address> <value> </code>

.. container:: hi

   Example:


To **write** I2C address 0x80 register 0x0038 to value 0x12, enter the following: <code> WIB 80 38 12 </code>

| 
| Delays are also supported with the format being: <code> delay <time in ms> </code>

.. container:: hi

   Example:


To enter a delay of 10 ms, enter the following: <code> delay 10 </code>

--------------

CSV Format (\*.csv)
-------------------

This format supports writing of registers that have 16-bit register address values. All hex values MUST have the “0x” preceding the value.

The format is comma delimited: <code> <i2c Address>,<register address>,<value> </code>

.. container:: hi

   Example:


To write I2C address 0x90, register 0x013E, to value 0xC4: <code> 0x90,0x13E,0xC4 </code>

| 
| This \*.csv format also allows performing a read-modify-write operations: <code> <i2c Address + 1>,<register address>,<value>,<mask> </code>

.. container:: hi

   Example:


To do a read-modify-write operation setting bit 0 = 0 and bit 1 = 1 (where you only need to modify to lower two bits): <code> 0x91,0x13E,0x02,0x03 </code> The mask 0x03 = 0b00000011 indicates to only modify bits 0 and 1.

| 
| Delays are also supported with the format being: <code> delay <time in ms> </code>

.. container:: hi

   Example:


To enter a delay of 10 ms, enter the following: <code> delay 10 </code>

--------------

CPP Format (\*.cpp)
-------------------

This selection ONLY supports writing of registers that have either 8-bit or 16-bit register address values. All hex values MUST have the “0x” preceding the value.

The first hex value can be either:

-  0x00 which designates a delays and the following byte is the delay in milliseconds.
-  A number indicating the number of bytes to following this one on the line from the file.

| 
| When the first byte is 0x00, the delay format is: <code> 0x00,<delay in ms> </code>

.. container:: hi

   Example:


To enter a delay of 5 ms, enter the following: <code> 0x00,0x05 </code>

| 
| When the first byte is not 0x00, it will typically be 0x04 for 16-bit addressing (or 0x03 for 8-bit addressing). The second byte is the I2C address, the third (and fourth byte for 16-bit) is the register address, and the last byte is the value to be written.

The format is as follows: <code> <number of bytes>,<i2c address>,<upper byte reg addr>,<lower byte reg addr>,<value> </code>

.. container:: hi

   Example:


To write I2C address 0x90, register 0x013E, to value 0xC4: <code> 0x04,0x90,0x01,0x3E,0xC4 </code>

| 
| This \*.cpp format also allows performing a read-modify-write operations: <code> <number of bytes>,<i2c address + 1>,<upper byte reg addr>,<lower byte reg addr>,<value>,<mask> </code>

.. container:: hi

   Example:


To do a read-modify-write operation setting bit 0 = 0 and bit 1 = 1 (where you only need to modify to lower two bits): <code> 0x04,0x90,0x01,0x3E,0x02,0x03 </code> The mask 0x03 = 0b00000011 indicates to only modify bits 0 and 1.
