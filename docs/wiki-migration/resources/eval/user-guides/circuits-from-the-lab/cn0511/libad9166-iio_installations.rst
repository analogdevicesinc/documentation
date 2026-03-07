Installation of Latest Lib-IIO Needed to Run the Example for CN0511
===================================================================

.. important::

   
   -  Line script to be copied are those found after the '$' symbol
   -  Enter the password "analog" whenever asked for it during the installation process
   
   ::
   
      [sudo] password for analog: analog
   


--------------

After the reboot, open command prompt or terminal again to clone the libad9166-iio from Github

Go to libad9166-iio directory

::

   analog@analog:~$ cd /usr/local/src/libad9166-iio 

Install the libad9166-iio

::

   analog@analog:/usr/local/src/libad9166-iio $ sudo cmake ./CMakeLists.txt

::

   analog@analog:/usr/local/src/libad9166-iio $ sudo make

::

   analog@analog:~/libad9166-iio $ sudo make install

Go to python directory

::

   analog@analog:~/libad9166-iio $ cd bindings/python

Install the requirements under this folder

::

   analog@analog:~/python $ sudo pip install -r requirements_dev.txt

::

   analog@analog:~/python $ cmake ./CMakeLists.txt

::

   analog@analog:~/python $ sudo make

::

   analog@analog:~/python $ sudo make install

--------------
