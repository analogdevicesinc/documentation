Power System Management on Linux Tutorial
=========================================

Introduction
------------

| The goal of this tutorial is to equip the reader with a collection of hardware and software tools for working with Power System Management devices, and more generally, devices that fall under the Linux hardware monitoring kernel API (HWMON) framework.
| The tutorial will focus on using standard tools and simple examples that can be used for debug and development.
| Also note that the tutorial is geared toward Linux-based systems, in contrast to bare-metal, no-OS applications. A great resource for learning about this use case is the `Linduino to PSM adapter shield <ad>:adi:`dc2294a>`__`. The instructions for this board go over how to run several examples on the Linduino (A clone of the Arduino UNO).

Videos
------

|

.. note::

   This video includes installation and configuration of Kuiper Linux, as well as building and installing the development branch of the libiio with HWMON support. The video will be re-done (and re-hosted on the CftL YouTube channel) once these features are merged to master and included in a Kuiper release.

   | |youtube>mR9V8uN390M|


| ==== Materials ====

-  Raspberry Pi 4; 2G, 4G, or 8G version. (3B, 3B Plus will work, but you will want the 4 :-) )
-  5V USB-C wall adapter for Raspberry Pi (micro USB for model 3)
-  :adi:`DC1962C "PowerStick" PSM Demo Board <https://www.analog.com/dc1962c>`
-  Electrical connection hardware (choose one):

   -  12x 15cm socket-to-socket jumpers such as `these from Schmartboard <https://schmartboard.com/wire-jumpers/female-jumpers/5-inch/>`__
   -  <<Future RPi to Pmod, QuikEval, PSM adapter>>

-  16GB (or larger) Class 10 (or faster) micro-SD card
-  User interface setup (choose one):

   -  HDMI monitor, keyboard, mouse plugged directly into Raspberry Pi
   -  Host Windows/Linux/Mac computer on same network as Raspberry Pi

-  Multimeters `7-Function Cen Tech <https://www.harborfreight.com/7-function-digital-multimeter-63759.html>`__ or equivalent

| 

Hardware Setup: Linux / Raspberry Pi
------------------------------------

| Follow the directions for downloading and burning the ADI Kuiper Linux image to the SD card:
| :doc:`Kuiper Linux </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`
| Add the following line to config.txt:

::

   dtoverlay=rpi-dc1962c

| 
| Make the fllowing connections between the DC1962C and the Raspberry Pi, following the pin mapping in Figure 1 and corresponding photo in Figure 2.
|

.. note::

   Pin mapping diagram


.. container:: centeralign

   Figure 1. Pin Mapping Diagram


| |image1|

.. container:: centeralign

   Figure 2. Connections with Discrete Wires


|

.. note::

   Update photo when production boards arrive

   | |image2|
   
   .. container:: centeralign

      Figure 3. Connections with DesignSpark adapter

   
   |


Toolbox Item: i2cdetect
-----------------------

When bringing up I2C devices on the Raspberry Pi (or any other processor / operating system, for that matter), it's helpful to know if devices are connected properly. The i2c-detect utility will scan all addresses on a partc I2c-detect is part of the I2C-tools package, which is pre-installed in Kuiper Linux. (It can be installed with apt-get install i2c-tools on Debian systems). The `i2c-detect man page <https://manpages.debian.org/unstable/i2c-tools/i2cdetect.8.en.html>`__ describes all options. Run:

::

   i2cdetect -y 1

| And observe the output as shown in Figure X.

.. note::

   Re-take screenshot with other EEPROMs on experimenter setup disabled (0x50-0x53)


   |image3|

   .. container:: centeralign

      Figure 4. Scanning I2C Bus 1 with i2c-detect

   


The LTC2974, LTC2977, and LTC3880 are at I2C addresses 0x32, 0x33, and 0x30, respectively. i2c-detect reports "UU" for these addresses because these devices are controlled from kernelspace, and users cannot access them directly. The onboard 24AA02 EEPROM is not associated with a driver. The upper nibble of the i2c address is 0x5, and the lower 3 bits select banks within the device. Externally, addresses 0x50 to 0x57 are acknowledged.
| Note that no data transfer actually occurs, the i2c-detect command is simply testing which devices acknowledge, then a stop condition is issued.
| ==== Toolbox Item: LM Sensors utilities ====

.. note::

   ToDo: add issue to Kuiper repo - add lm-sensors

   
   ::
   
      sudo apt-get install lm-sensors
   


::

   sensors

Toolbox Item: HWMON Python library
----------------------------------

::

   sudo pip3 install hwmon

(run through some of the examples)

::

   from hwmon import Hwmon
   sensors = Hwmon.HW()
   sensors.print_data()

Toolbox Item: IIO Utilities
---------------------------

Yup, this really works!

.. note::

   ToDo: Remove when merged to master and included in Kuiper release The libiio master branch now includes HWMON support, but is not included in the latest Kuiper release. It needs to be installed manually - but fear not, It's easy:

   
   ::
   
      git clone https://github.com/analogdevicesinc/libiio.git
      cd libiio
      git checkout master
      mkdir build && cd build && cmake -DWITH_SYSTEMD=ON -DWITH_HWMON=ON -DWITH_EXAMPLES=ON ../ && make && sudo make install
      sudo reboot
   
   |


| iio_info
| IIO Oscilloscope
| Hopefully PyADI-IIO in the not too distant future

Toolbox Item: pmbus_dpsm utilities
----------------------------------

When you need to dig in deeper, use cases, noting that you have to remove the device tree overlay in order to use userspace functions.

Putting it all together: A Run-time Logging Application
-------------------------------------------------------

Put together a simple python script to periodically log data from the power stick over time, and save to a local file. Show how this can be used to detect anomalies, trends toward higher operating temperatures, and other diagnostic stuff.

Show both a python HWMON example running locally, and a libiio based example that can run either locally or remotely.

Conclusion
----------

| 
| Existing PSM tools are the workhorse of system design and bringup. The Linux HWMON drivers and utilities are additional tools available for run-time debug and monitoring. (obviously this conclusion needs work...)

.. |youtube>mR9V8uN390M| image:: https://wiki.analog.com/_media/youtube>mR9V8uN390M
.. |image1| image:: https://wiki.analog.com/_media/university/labs/software/psm_hwmon_linux_tutorial/rpi_power_stick_jumpers.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/university/labs/software/psm_hwmon_linux_tutorial/rpi_adapter_power_stick.jpg
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/university/labs/software/psm_hwmon_linux_tutorial/i2c-detect_drivers_enabled.png
   :width: 400px
