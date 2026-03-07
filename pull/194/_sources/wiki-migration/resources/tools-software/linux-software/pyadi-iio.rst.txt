.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/pyadi-iio_logo_600.png
   :align: center
   :width: 400px

pyadi-iio: Device Specific Python Interfaces For IIO Drivers
============================================================

To simplify the use of different devices a python package was created interface with the different IIO drivers. The module pyadi-iio, provides device-specific APIs built on top of the current libIIO python bindings. These interfaces try to match the driver naming as much as possible without the need to understand the complexities of libIIO and IIO. In general, if you are familiar with python this is a great starting point for using different ADI parts and can even run on some ADI development systems as well.

Basic Installation
------------------

There are three steps required to setup PyADI-IIO:

-  Download and Install LibIIO
-  Download and Install Python
-  Install the PyADI-IIO bindings

Windows Installation
~~~~~~~~~~~~~~~~~~~~

-  Download and install the latest release of LibIIO

.. admonition:: Download
   :class: download

   
   :git-libiio:`LibIIO <releases>`


-  Download and install Python

.. admonition:: Download
   :class: download

   
   `Python for Windows <https://www.python.org/downloads/windows/>`_


-  Install the libIIO bindings through pip.\ ``pip install pylibiio``
-  Install the PyADI-IIO through pip.\ ``pip install pyadi-iio``
-  If you need to Update/Overwrite your PyADI-IIO through pip, use the following command.\ ``pip install -U pyadi-iio``

Linux Installation
~~~~~~~~~~~~~~~~~~

-  It is recommended that Linux users build libiio from :git-libiio:`the build instructions <README_BUILD.md>`

   -  Note that since v0.19 libiio requires :git-libiio:`cmake <README_BUILD.md>` flags to enable the python bindings during installation.

-  Make sure you have at least Python 3.6 or newer installed
-  Install the libIIO bindings through pip.\ ``pip install pylibiio
     * Make sure you are using the Python 3 version of pip. That might be pip3.``
-  Install the PyADI-IIO through pip.\ ``pip install pyadi-iio
     * Make sure you are using the Python 3 version of pip. That might be pip3.``

Mac OS Installation
~~~~~~~~~~~~~~~~~~~

-  It is recommended that Mac OS users build libiio from :git-libiio:`the build instructions <README_BUILD.md>`

   -  Note that since v0.19 libiio requires :git-libiio:`cmake <README_BUILD.md>` flags to enable the python bindings during installation.

-  Make sure you have at least Python 3.6 or newer installed
-  Install the libIIO bindings through pip.\ ``pip install pylibiio``
-  Install the PyADI-IIO through pip.\ ``pip install pyadi-iio``

Examples
--------

Devices specific examples are available in the :git-pyadi-iio:`source repo <examples>`, and the `sphinx doc <https://analogdevicesinc.github.io/pyadi-iio/>`_, but here is the basic idea

.. code:: python

   # Import library
   import adi
   # Create radio object
   sdr = adi.Pluto()
   # Configure properties
   sdr.rx_rf_bandwidth = 4000000
   # Get data
   data = sdr.rx()

Supported Devices/Parts
-----------------------

See :git-pyadi-iio:`repo readme <supported_parts.md>` for supported hardware.

Support
-------

Documentation
~~~~~~~~~~~~~

-  All PyADI-IIO documentation is available on `GitHub <https://analogdevicesinc.github.io/pyadi-iio>`_.

Other Useful Links
~~~~~~~~~~~~~~~~~~

-  :git-pyadi-iio>`__
-  `PyPi <https::`Source </pypi.org/project/pyadi-iio>`

Support Questions
~~~~~~~~~~~~~~~~~

Please direct support question or enhancement requests to the :ez:`Software Interface Tools Forums on EngineerZone <sw-interface-tools>`

*End of Document*
