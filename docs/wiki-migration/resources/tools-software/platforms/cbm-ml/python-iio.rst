Python Support For CBM Development Platform
===========================================

|https://www.python.org/static/community_logos/python-logo-inkscape.svg|

Python support for the CBM development system is provided in two layers, both of which are built on top of the various IIO drivers and :doc:`libIIO </wiki-migration/resources/tools-software/linux-software/libiio>`. The two layers are:

-  **The python libIIO bindings** which are simply a pythonic interface into the C library itself. This is recommended for users comfortable with libIIO and its API, or if you need more advanced control.
-  **pyadi-iio** which is a module built on top of the libIIO python bindings with class-specific implementations of specific parts and platforms. pyadi-iio greatly simplifies much of the libIIO complexities especially around buffer management, connectivity, and data interpretation.

Getting Started
===============

Depending on the choice you make above you will need more or fewer components to get going. Since pyadi-iio requires libIIO and its python bindings, it will be a subset of pyadi-iio requirements. To get started follow these guides to get libIIO, its bindings, and optionally pyadi-iio as well.

-   :git-libiio:`libIIO and its python bindings <README_BUILD.md>`
-  :doc:`pyadi-iio </wiki-migration/resources/tools-software/linux-software/pyadi-iio>`

Getting Data Into Python
========================

For the sake of simplicity and avoiding the complexity of interpreting data from libIIO directly, we will discuss only using pyadi-iio here. pyadi-iio is always recommended first since its classes have been verified to specific devices and the interpreted data is always in the correct format.

Python can be used remotely on a desktop/laptop or on the development system itself running Linux. Only the selection of the context is needed to switch between the two. This is done through the URI. Here is an example:

.. code:: python

   # Import the module
   import adi
   # Connect to the device when on-board
   dev = adi.<Class Name>(uri="local:")
   # Connect to the device when remote
   dev = adi.<Class Name>(uri="ip:<ip of board>")
   # Enable desired channels
   dev.rx_enabled_channels = [0, 1]
   # Pull data
   data = dev.rx()
   # data will be a list of numpy arrays of size 2.
   ....
   # More python fun

.. |https://www.python.org/static/community_logos/python-logo-inkscape.svg| image:: https://www.python.org/static/community_logos/python-logo-inkscape.svg
   :width: 500px
   :target: https://www.python.org/static/community_logos/python-logo-inkscape.svg
