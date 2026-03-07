Introduction
============

This page describes the steps required to build and use the RTC on the ADSP-SC589 EZ-board(ADSP-SC584 and ADSP-SC573 don't support RTC). The Real Time Clock (RTC) serves two purposes: to keep accurate time/date information and to provide wake up alarms (both during runtime and while sleeping). Since the RTC can be externally powered and clocked independently of the processor it can remain running even when the rest of the system is turned off.

Hardware Required
-----------------

An ADSP-SC589 EZ-Board v1.1 and above

Software Configuration
----------------------

Configure Linux Kernel
~~~~~~~~~~~~~~~~~~~~~~

Enable RTC support:

::

   Device Drivers  --->
       [*] Real Time Clock  --->
           <*>   ADI On-Chip RTC v2

Configure Packages
~~~~~~~~~~~~~~~~~~

Add the rtc-test program in the filesystem images, it's enabled in adsp-sc5xx-full image by default.

::

   vim build/conf/local.conf
   IMAGE_INSTALL_append = "rtc-test"

Example
-------

Users just need to run rtc_test command on board to test rtc. Results as shown below:

::

   # rtc_test
   0. open and release
   opened '/dev/rtc0': fd = 3
   1. ioctl RTC_UIE_ON
   2. RTC read 5 times
   RTC read 1
   RTC read 2
   RTC read 3
   RTC read 4
   RTC read 5
   3. ioctl RTC_UIE_OFF
   4. Get RTC Time
   Current RTC date/time is 24-4-76, 22:48:15
   5. Set RTC Time
   Set Current RTC date/time to 31-5-104, 02:30:00
   Get RTC time
   Current RTC date/time is 31-5-104, 02:30:00
   6. Set alarm Time
   7. Get alarm Time
   Alarm time now set to 02:30:50
   Waiting 50 seconds for alarm...
   random: nonblocking pool is initialized
    Okay. Alarm rang.
   Current RTC date/time is 31-5-104, 02:30:50
   8. ioctl RTC_AIE_OFF
   8.5 test sleep 10
   Current RTC date/time is 31-5-104, 02:31:00
   Current RTC date/time is 31-5-104, 02:31:00
   RTC Tests done !

--------------

**Back to** :doc:`Kernel Features and Device Drivers for ADSP-SC5xx Yocto Linux </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/start>`
