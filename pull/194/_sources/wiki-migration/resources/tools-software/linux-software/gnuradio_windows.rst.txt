GNU Radio with IIO for Windows
==============================


.. note::

   See `wiki/common <https://wiki.analog.com/wiki/common#retired>`_


Analog Devices provides a Windows binary installer for GNU Radio with support for IIO based devices like ADALM-Pluto, FMComms2/3/4/5, and other devices. Windows is not a primary platform for GNU Radio and is not thoroughly tested, and support through the GNU Radio community is limited. For users looking to build custom out-of-tree modules, it is recommended to do so with GNU Radio on a Linux based system.

.. important::

   This old binary was removed, since we don't want people to go down a path that no one will get any support on. If you need it, build it from source.


Licensing
---------

The `scripts <https://github.com/tfcollins/GNURadio_Windows_Build_Scripts/>`_ used to build the MSI's are released under the GPLv3 and are based on existing work by `GCN Development <https://github.com/gnieboer/GNURadio_Windows_Build_Scripts>`_. The resulting MSI's are also GPLv3 compatible, see `here <http://www.gcndevelopment.com/gnuradio>`_ for details and access to all modifications to original source code. All patches are released under the same license as the original package.

Please see `here <http://www.gcndevelopment.com/gnuradio/downloads.htm>`_ for links to original source and binaries of gnuradio and it's required dependencies. The dependencies specific to gr-iio blocks are:

-  :git-libiio>`__
-  `libad9361 <https::`libiio </github.com/analogdevicesinc/libad9361-iio>`

Installer Build Process
-----------------------

The entire build process is detailed here `README <https://github.com/tfcollins/GNURadio_Windows_Build_Scripts/blob/maint/README.md>`_, and requires elevated privileges in Windows. Analog Devices does not provide support for this build process. If you wish to build the installer you are on your own.

Support
-------

This installer is provided with only support for questions relating to the gr-iio blocks specifically and the driver software associated with libiio.

-  Questions relating to the ADALM-Pluto should be asked in :ez:`Virtual Classroom for ADI University Program <community/university-program>`.
-  Questions relating to other Analog Devices IIO supported devices should be asked in the :ez:`Linux forums <community/linux-device-drivers/linux-software-drivers>`.

.. warning::

   While both the community and Analog Devices provide best efforts for support, no one has any obligation to provide maintenance or support for any of the Software distributed or found on this site. Just as you are free to use any of the software you find on this site (under that software package's license), you are free use an alternative, which may include commercial/deterministic support.

   
   We reserves the right to change anything (source code, circuits, schematics, forum content, policies, procedures, etc) at any time without notice, but is under no obligation to do so.

