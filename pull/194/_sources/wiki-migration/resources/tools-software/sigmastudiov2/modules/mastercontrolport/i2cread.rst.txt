:doc:`Click here to return to the Master Control Port page </wiki-migration/resources/tools-software/sigmastudiov2/modules/mastercontrolport>`

I2C Read
========

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mastercontrolport/i2c_read_ssp.jpg
   :alt: i2c_read_ssp.jpg

| 
| ===== Description =====
| There are two different versions of I2C Read module.

-  I2C Periodic Read
-  I2C Read with external Trigger

| The **'I2C Periodic Read'** block reads a particular sub address from any I2C slave periodically and sends the value read in the output pin.
| The **'I2C Read with external Trigger'** block reads a particular sub address from any I2C slave when a rising edge is detected in the input pin.
| ===== Usage =====
| Click on the Settings button to configure the parameters for I2C read.
| |i2c_read_wndw_ssp.jpg|
| Create Multiple instances for monitoring multiple slaves/ multiple sub address from same slave.
| ===== Targets Supported =====

======== ========== ===================== ============= ================
Name     ADSP-214xx ADSP-215xx/ADSP-SC5xx ADAU145x/146x ADSP-218xx/SC8xx
======== ========== ===================== ============= ================
I2C Read NA         NA                    S             NA
======== ========== ===================== ============= ================

| 
| ===== Pins =====
| ====Input Pins====

======= ======= ==========================================
Name    Type    Description
======= ======= ==========================================
Trigger Control Rising edge in this signal initiates read.
======= ======= ==========================================

| 
| ====Output Pins====

======================== ======= ==========================
Name                     Type    Description
======================== ======= ==========================
Output<fc #ff0000>X</fc> Control Outputs data read over I2C
======================== ======= ==========================

| 
| ===== Configurable Parameters =====

+---------------------------------------------+---------------+---------------------------------+----------------------------------------------------------+
| GUI Control Name                            | Default Value | Range                           | Function Description                                     |
+=============================================+===============+=================================+==========================================================+
| I2CBitrate                                  | 400 kHz       | 20 - 400 kHz                    | I2C Speed                                                |
+---------------------------------------------+---------------+---------------------------------+----------------------------------------------------------+
| I2CDeviceAddress                            | 0             | 0 – 127                         | I2C Slave Device Address                                 |
+---------------------------------------------+---------------+---------------------------------+----------------------------------------------------------+
| I2CDeviceAddressBits                        | 8-Bit         | 8-Bit/7-Bit                     | 7 or 8 bit i2c address                                   |
+---------------------------------------------+---------------+---------------------------------+----------------------------------------------------------+
| I2CDeviceAddressFormat                      | Hex           | Hex/Dec                         | Address format                                           |
+---------------------------------------------+---------------+---------------------------------+----------------------------------------------------------+
| DataLength                                  | 4             | 1-4                             | Length of the data to be read                            |
+---------------------------------------------+---------------+---------------------------------+----------------------------------------------------------+
| SubAddressBytes                             | 2             | 1-4                             | Length of the sub address                                |
+---------------------------------------------+---------------+---------------------------------+----------------------------------------------------------+
| ReadAddress_Output<fc #ff0000>X</fc>        | 0             | 0 to Pow(2, Address Length) - 1 | Sub- address of the slave to be read                     |
+---------------------------------------------+---------------+---------------------------------+----------------------------------------------------------+
| InitialOutputValue_Output<fc #ff0000>X</fc> | 0             | -2147483648 to 2147483647       | Value in the output pin till the first read is complete. |
+---------------------------------------------+---------------+---------------------------------+----------------------------------------------------------+

| 
| Note: <fc #ff0000>X</fc> indicates the channel number

DSP Parameters
--------------

| 
| Not applicable
| ===== DSP Parameter Computation =====
| Not applicable

.. |i2c_read_wndw_ssp.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mastercontrolport/i2c_read_wndw_ssp.jpg
