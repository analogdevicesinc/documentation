Building Pixelpulse2
====================

Linux
-----

To build from source on Linux with an appropriate C++ compiler and libraries:

-  Install LibUSB

   -  On debian installations that would be something like:

::

   pi@raspberrypi:/home/pi/git# **sudo apt-get install libusb-1.0-0-dev libudev-dev**

-  Install Qt5.4

   -  On debian installations that would be something like:

::

   pi@raspberrypi:/home/pi/git# **sudo apt-get install qtbase5-dev qtdeclarative5-dev**

-  Check out PixelPulse2:

::

   git clone --recursive https:%%//%%github.com/analogdevicesinc/pixelpulse2

-  Go into that directory, and make a build directory.
-  make the project using CMake

::

   pi@raspberrypi:/home/pi# **cd pixelpulse2**
   pi@raspberrypi:/home/pi/pixelpulse2# **mkdir build**
   pi@raspberrypi:/home/pi/pixelpulse2# **cd build**
   pi@raspberrypi:/home/pi/pixelpulse2/build# cmake ../
   pi@raspberrypi:/home/pi/pixelpulse2/build# make
