EVAL-ADT7420-PMDZ System Setup with MAX32655FTHR and MAX32650FTHR
=================================================================

The :adi:`EVAL-ADT7420-PMDZ` can be used with the MAX32655FTHR and MAX32650FTHR.

Demo Requirements
-----------------

The following is the list of items needed in order to replicate this demo.

-  \*\* Hardware \*\*

   -  `MAX32655FTHR <https://www.maximintegrated.com/MAX32655FTHR>`__ or
   -  `MAX32650FTHR <https://www.maximintegrated.com/MAX32650FTHR>`__ with `MAX32625PICO <https://www.maximintegrated.com/MAX32625PICO>`__
   -  :adi:`FTHR-PMD-INTZ`
   -  :adi:`EVAL-ADT7420-PMDZ`
   -  Micro-USB to USB Cable
   -  10-pin ribbon cable
   -  PC or Laptop with USB Port

-  \*\* Software \*\*

   -  For MAX32655FTHR,

      -  Pre-built hex file "adt7420_max32655fthr.hex" in `adt7420_max3265xfthr.zip <https://wiki.analog.com/_media/resources/eval/user-guides/maximfthr/adt7420_max3265xfthr.zip>`__
      -  PuTTY or other similar software

   -  For MAX32650FTHR,

      -  Maxim Micros SDK `swpart=SFW0010820A <https://www.maximintegrated.com/en/design/software-description.html/swpart=SFW0010820A>`__
      -  Pre-built elf file "adt7420_max32650fthr.elf" in `adt7420_max3265xfthr.zip <https://wiki.analog.com/_media/resources/eval/user-guides/maximfthr/adt7420_max3265xfthr.zip>`__

MAX32655FTHR
------------

1. Connect **MAX32655FTHR** with the **FTHR-PMOD-INTZ**. Note that MAXIM feather board should have stacking headers for feather board where the interposer board will be connected.

2. Connect \*\* EVAL-ADT7420-PMDZ \*\* to the \*\* FTHR-PMOD-INTZ \*\*.

================= ==============
EVAL-ADT7420-PMDZ FTHR-PMOD-INTZ
================= ==============
pin 1 and 2       SCL_PMOD
pin 3 and 4       SDA_PMOD
pin 5 and 6       GND
pin 7 and 8       VCCY_I2C
================= ==============

The final setup should look similar shown in Figure 1.


|image1|

.. container:: center

   *<fc>Figure 1. Hardware Setup </fc>*


3. Power up the **MAX32655FTHR** by connecting it to your laptop using micro-USB

4. Open the file explorer. Drag-and-drop the pre-built hex file to the DAPLINK. If the transfer was not completed, update the firmware for the DAPLINK. Follow the steps here: https://github.com/MaximIntegrated/max32625pico-firmware-images/

5. Open PuTTY or other similar software. Check the Device Manager to set correct COM for the MAX32655FTHR. Set baud rate to **57600**.

The expected output viewed in the PuTTY is shown in Figure 2.


|image2|

.. container:: center

   *<fc>Figure 2. Expected Output </fc>*


MAX32650FTHR
------------

1. Using a 10-pin ribbon cable, connect the **MAX32625PICO** to the **MAX32650FTHR**. Connect **MAX32650FTHR** to the **FTHR-PMOD-INTZ**.

2. Connect \*\* EVAL-ADT7420-PMDZ \*\* to the \*\* FTHR-PMOD-INTZ \*\*.

================= ==============
EVAL-ADT7420-PMDZ FTHR-PMOD-INTZ
================= ==============
pin 1 and 2       SCL_PMOD
pin 3 and 4       SDA_PMOD
pin 5 and 6       GND
pin 7 and 8       VCCY_I2C
================= ==============

The final setup should look similar shown in Figure 3.


|image3|

.. container:: center

   *<fc>Figure 3. Hardware Setup </fc>*


3. Power up the **MAX32650FTHR** by connecting it to your laptop using micro-USB. Connect **MAX32625PICO** to your laptop as well.

4. Place the pre-built elf file in your current CMD path folder.

5. Run the following in your command terminal:

::

   C:\MaximSDK\Tools\OpenOCD\openocd.exe -s C:\MaximSDK\Tools\OpenOCD\scripts -f interface\cmsis-dap.cfg -f target\max32650.cfg -c "program adt7420_max32650fthr.elf verify exit"

6. Open PuTTY or other similar software. Set baud rate to **57600**.

The expected output viewed in the PuTTY is shown in Figure 4.


|image4|

.. container:: center

   *<fc>Figure 4. Expected Output </fc>*


// End of Document //

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/maximfthr/adt7420_max32655fthr.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/maximfthr/adt7420_max32655.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/maximfthr/adt7420_max32650fthr.jpg
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/maximfthr/adt7420_max32650.png
   :width: 600px
