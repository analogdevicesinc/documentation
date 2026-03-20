.. _cn0511-software-req:

Software Requirements
=====================

Following the instructions below will allow you to install the latest version of libIIO and other requirements needed to run the example for CN0511. 
This is necessary because the latest version of libIIO contains the necessary support for AD9166, which is the main component of CN0511.

.. important::

   -  This set of instructions will soon go away when the next version of Kuiper Linux is released
   -  Line script to be copied are those found after the '$' symbol
   -  Enter the password "analog" whenever asked for it during the
      installation process

   ::

      [sudo] password for analog: analog

----

Libad9166-iio Installation 
--------------------------

1. After the reboot, open command prompt or terminal again to clone the
   libad9166-iio from GitHub.

   ::

       analog@analog:~$ git clone https://github.com/analogdevicesinc/libad9166-iio

2. Go to the libad9166-iio directory.

   ::

      analog@analog:~$ cd libad9166-iio

3. Install the libad9166-iio and its dependencies by running the following commands:

   ::

      analog@analog:~/libad9166-iio $ cmake ./CMakeLists.txt

   ::

      analog@analog:~/libad9166-iio $ make

   ::

      analog@analog:~/libad9166-iio $ sudo make install

4. Go to the Python directory.

   ::

      analog@analog:~/libad9166-iio $ cd bindings/python

5. Install the other requirements needed for CN0511 libad9166-iio example project by running the following commands:

   ::

      analog@analog:~/libad9166-iio/bindings/python $ sudo pip install -r requirements_dev.txt

   ::

      analog@analog:~/python $ sudo pip install -r requirements_dev.txt

   ::

      analog@analog:~/python $ cmake ./CMakeLists.txt

   ::

      analog@analog:~/python $ sudo make

   ::

      analog@analog:~/python $ sudo make install

----

Pyadi-iio Installation
----------------------

1. Enter the following commands to install pyadi-iio from GitHub:

   ::

      analog@analog:~ $ sudo python -m pip install git+https://github.com/analogdevicesinc/pyadi-iio/

   ::

      analog@analog:~$ git clone https://github.com/analogdevicesinc/pyadi-iio

2. Install the libatlas-base-dev and linux packages by running the following command:

   ::

      analog@analog:~$ sudo apt-get install libatlas-base-dev linux packages

3. Then, choose 'Y' if were asked to continue.

After all these requirements has been loaded in the Raspberry Pi, the example
found in ~/home/analog/pyadi-iio/examples for CN0511 can now be run.
