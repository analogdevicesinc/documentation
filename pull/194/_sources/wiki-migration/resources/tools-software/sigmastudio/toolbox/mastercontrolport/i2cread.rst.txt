I2C Read (ADAU145X)
===================

| :doc:`Click here to return to the Master Control Port section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/mastercontrolport>`
| There are two different versions of I2C Read module.

-  I2C Periodic Read
-  I2C Read with external Trigger

I2C Periodic Read
-----------------

The 'I2C Periodic Read' block reads a particular sub address from any I2C slave periodically and sends the value read in the output pin.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mastercontrolport/i2cperiodicread.jpg
   :align: center

| 
| ====Output Pins====

+-----------------+------------------------------------+----------------------------+
| Name            | Format [int/dec] - [control/audio] | Function Description       |
+=================+====================================+============================+
| Pin 0: I2C Data | decimal - control                  | Outputs data read over I2C |
+-----------------+------------------------------------+----------------------------+

| 
| ====Configuration==== Click on the configure button to configure the parameters for I2C read.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mastercontrolport/i2creadwindow.jpg
   :align: center

Create Multiple instances for monitoring multiple slaves/ multiple sub address from same slave.

| 
| ====GUI Control====

+----------------------+---------------+---------------------------------+----------------------------------------------------------+
| GUI Control Name     | Default Value | Range                           | Function Description                                     |
+======================+===============+=================================+==========================================================+
| Bitrate              | 400 kHz       | 20 - 400 kHz                    | I2C Speed                                                |
+----------------------+---------------+---------------------------------+----------------------------------------------------------+
| Device Address       | 0             | 0 – 127                         | I2C Slave Device Address                                 |
+----------------------+---------------+---------------------------------+----------------------------------------------------------+
| Data Length          | 4             | 1-4                             | Length of the data to be read                            |
+----------------------+---------------+---------------------------------+----------------------------------------------------------+
| Sub-Address Bytes    | 2             | 1-4                             | Length of the sub address                                |
+----------------------+---------------+---------------------------------+----------------------------------------------------------+
| Read Interval        | 1 ms          | 1 - 1000 ms                     | Interval between 2 consecutive I2C Read                  |
+----------------------+---------------+---------------------------------+----------------------------------------------------------+
| Read Address         | 0             | 0 to Pow(2, Address Length) - 1 | Sub- address of the slave to be read                     |
+----------------------+---------------+---------------------------------+----------------------------------------------------------+
| Initial Output Value | 0             | -2147483648 to 2147483647       | Value in the output pin till the first read is complete. |
+----------------------+---------------+---------------------------------+----------------------------------------------------------+

| 
| ===== I2C Read with external Trigger ===== The 'I2C Read with external Trigger' block reads a particular sub address from any I2C slave when a rising edge is detected in the input pin.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mastercontrolport/i2cperiodicread.jpg
   :align: center

| 
| ====Input Pins====

+----------------+------------------------------------+--------------------------------------------+
| Name           | Format [int/dec] - [control/audio] | Function Description                       |
+================+====================================+============================================+
| Pin 0: Trigger | decimal - control                  | Rising edge in this signal initiates read. |
+----------------+------------------------------------+--------------------------------------------+

| 
| ====Output Pins====

+-----------------+------------------------------------+----------------------------+
| Name            | Format [int/dec] - [control/audio] | Function Description       |
+=================+====================================+============================+
| Pin 0: I2C Data | decimal - control                  | Outputs data read over I2C |
+-----------------+------------------------------------+----------------------------+

| 
| ====Configuration==== Click on the configure button to configure the parameters for I2C read.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mastercontrolport/i2creadwindow2.jpg
   :align: center

Create Multiple instances for monitoring multiple slaves/ multiple sub address from same slave.

| 
| ====GUI Control====

+----------------------+---------------+---------------------------------+----------------------------------------------------------+
| GUI Control Name     | Default Value | Range                           | Function Description                                     |
+======================+===============+=================================+==========================================================+
| Bitrate              | 400 kHz       | 20 - 400 kHz                    | I2C Speed                                                |
+----------------------+---------------+---------------------------------+----------------------------------------------------------+
| Device Address       | 0             | 0 – 127                         | I2C Slave Device Address                                 |
+----------------------+---------------+---------------------------------+----------------------------------------------------------+
| Data Length          | 4             | 1-4                             | Length of the data to be read                            |
+----------------------+---------------+---------------------------------+----------------------------------------------------------+
| Sub-Address Bytes    | 2             | 1-4                             | Length of the sub address                                |
+----------------------+---------------+---------------------------------+----------------------------------------------------------+
| Read Address         | 0             | 0 to Pow(2, Address Length) - 1 | Sub- address of the slave to be read                     |
+----------------------+---------------+---------------------------------+----------------------------------------------------------+
| Initial Output Value | 0             | -2147483648 to 2147483647       | Value in the output pin till the first read is complete. |
+----------------------+---------------+---------------------------------+----------------------------------------------------------+
