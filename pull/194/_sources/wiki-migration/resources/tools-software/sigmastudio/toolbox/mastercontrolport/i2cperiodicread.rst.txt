I2C Periodic Read
=================

:doc:`Click here to return to the Master Control Port section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/mastercontrolport>`

The 'I2C Periodic Read' block reads a particular sub address from any I2C slave periodically and sends the value read in the output pin.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mastercontrolport/i2cread.jpg
   :align: center
   :width: 80px

Click on the configure button to configure the parameters for I2C read.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mastercontrolport/i2creadwindow.jpg
   :align: center

Create Multiple instances for monitoring multiple slaves/ multiple sub address from same slave.

GUI Control
-----------

+------------------+---------------+---------------------------------+-----------------------------------------+
| GUI Control Name | Default Value | Range                           | Function Description                    |
+==================+===============+=================================+=========================================+
| Bitrate          | 400 kHz       | 20 - 400 kHz                    | I2C Speed                               |
+------------------+---------------+---------------------------------+-----------------------------------------+
| Device Address   | 0             | 0 – 127                         | I2C Slave Device Address                |
+------------------+---------------+---------------------------------+-----------------------------------------+
| Read Address     | 0             | 0 to Pow(2, Address Length) - 1 | Sub- address of the slave to be read    |
+------------------+---------------+---------------------------------+-----------------------------------------+
| Address Length   | 2             | 1-4                             | Length of the sub address               |
+------------------+---------------+---------------------------------+-----------------------------------------+
| Data Length      | 4             | 1-4                             | Length of the data to be read           |
+------------------+---------------+---------------------------------+-----------------------------------------+
| Read Interval    | 1 ms          | 1 - 1000 ms                     | Interval between 2 consecutive I2C Read |
+------------------+---------------+---------------------------------+-----------------------------------------+
