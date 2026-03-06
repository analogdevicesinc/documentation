Conda Packages
==============

.. image:: https://wiki.analog.com/_media/university/tools/python-conda.png
   :alt: https://www.geekpills.com/operating-system/linux/how-to-install-anaconda-on-ubuntu-18-04
   :width: 400px

Conda and Anaconda are cross-platform package-management tools that generally focus around python but can support any language or package generally.

Available packages/libraries:

-  libiio
-  libm2k
-  libsmu
-  pyadi-iio

To get started with the Conda packages Anaconda needs to be installed first. Please follow the `official documentation from Anaconda <https://docs.anaconda.com/anaconda/install/>`__. For Windows users, we recommend installing for individual users as global installs seem to not install shortcuts for easy access.

Once you have Anaconda installed the packages need to be built and installed. First, activate conda:

-  For Windows users launch Anaconda Prompt from your start menu
-  For macOS users by default conda is added to your path
-  Linux users activate conda in your shell based on how you installed it

From your open shell/command prompt run the following based on what packages you want to be installed.

Install
-------

ADI authored packages are provided through the conda-forge channel. Therefore, all packages should be installed as:

::

   conda install -c conda-forge <package name>

libm2k
------

Install libm2k+python bindings:

::

   conda install -c conda-forge libm2k

Once installed you can call libm2k from python. A quick test from a python terminal:

::

   >> import libm2k
   >> ctx=libm2k.m2kOpen()
   >> ctx.getUri()
   'usb:2.3.4'

libsmu
------

Install libsmu+python bindings:

::

   conda install -c conda-forge libsmu

Once installed you can call pysmu from python. A quick test, with m1k board connected to USB port, from a python terminal:

::

   >> from pysmu import Session
   >> session = Session()
   >> devx = session.devices[0]
   >> devx.serial
   '2031205050485230313530303830313'
   >> devx.fwver
   '2.17'
   >> devx.hwver
   'F'
