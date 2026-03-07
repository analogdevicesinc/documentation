.. warning::

   \ **This software uses an older version of libsmu / pysmu and is no longer recommended for use.**

   
   :doc:`ALICE Desktop 1.3 </wiki-migration/university/tools/m1k/alice/desk-top-users-guide>` is now recommended.


.. admonition:: Download
   :class: download

   Download Windows installer here:

   
   -  `Latest release for 32 bit Python 2.7 <https://wiki.analog.com/_media/university/tools/alice-1.0-32bit-setup.zip>`_
   -  `Latest release for 64 bit Python 2.7 <https://wiki.analog.com/_media/university/tools/alice-1.0-64bit-setup.zip>`_
   


ALM1000 ALICE Software Suite
============================

ALICE (Active Learning Interface for Circuits and Electronics) is a open source suite of Python applications, which provides a user interface for visualizing and manipulating signals while exploring circuits and electronics systems attached to the affordable Analog Devices' :adi:`ADALM1000`

The use of Python affords a cross-platform (Windows, Linux, OS X) set of accessible tools for initial interactive explorations. **Python 2.7 and the numpy extension module must be installed on the user's computer before installing the ALICE tools.** These programs are written for Python 2.7 and will not run on Python 3.

Interfaces for DC, AC, Time Domain and Frequency Domain analysis make exploring system behaviors across a wide range of signal amplitudes, frequencies, or phases a trivial exercise. It includes interfaces for :

-  :doc:`Active Learning Interface (for) Circuits (and) Electronics </wiki-migration/university/tools/m1k/alice/users-guide>`
-  :doc:`ALM1000 DC Volt Meter User Guide </wiki-migration/university/tools/m1k/alice/voltmeter-users-guide>`
-  :doc:`ALM1000 DC Meter-Source User Guide </wiki-migration/university/tools/m1k/alice/meter-source-users-guide>`
-  :doc:`ALM1000 DC Ohmmeter User Guide </wiki-migration/university/tools/m1k/alice/ohmmeter-users-guide>`
-  :doc:`ALM1000 Strip Chart Recorder Tool User Guide </wiki-migration/university/tools/m1k/alice/stripchart-users-guide>`
-  :doc:`ALICE Oscilloscope User Guide </wiki-migration/university/tools/m1k/alice/users-guide>`
-  :doc:`ALICE-SA Spectrum Analyzer User Guide </wiki-migration/university/tools/m1k/alice/sa-users-guide>`
-  :doc:`ALICE-VVM Vector Voltmeter - Impedance Analyzer - RLC Meter User Guide </wiki-migration/university/tools/m1k/alice/vvm-users-guide>`

.. image:: https://wiki.analog.com/_media/university/tools/alice1_userguide_f1.png
   :align: center
   :width: 500px

Download
========

The release contains multiple Python programs that allow the tool set to be deployed on systems that run Windows. The installer assumes that `Python 2.7 <https://www.python.org/downloads/>`_ ( 32 bit or 64 bit binary versions depending on user's computer ) sub version 8 or higher along with any required add-on modules ( `numpy <http://www.scipy.org/scipylib/download.html>`_ for all programs as of Feb 11 2016 ) have already been installed on the user's computer. The installer also presumes that it will be located in the C:\\Python27 directory tree. The installer will place the current version of the libpysmu.pyd ALM1000 interface library in the C:\\Python27\\DLLs directory.

The latest release of the ALICE tool set Windows installer for 32 bit Python is available for download from `HERE <https://wiki.analog.com/_media/university/tools/alice-1.0-32bit-setup.zip>`_ and 64 bit Python `HERE <https://wiki.analog.com/_media/university/tools/alice-1.0-64bit-setup.zip>`_. Extract the .exe setup file from the .zip archive. Run the alice-1.0-XXbit-setup.exe installer program. The programs open and save info and data to various files in the installation directory. Because of user permission issues with some installations of Windows you may need to install the software in a directory other than the default "Program Files". C:\\Python27\\ would be a good second choice.

The installer adds desktop icons for each tool in the suite.

The typical list of files that a release contains:

-  :doc:`alice-1.0.pyw </wiki-migration/university/tools/m1k/alice/users-guide>`
-  :doc:`alice-SA-1.0.pyw </wiki-migration/university/tools/m1k/alice/sa-users-guide>`
-  :doc:`alice-VVM-1.0.pyw </wiki-migration/university/tools/m1k/alice/vvm-users-guide>`
-  :doc:`dc-meter-source-tool.pyw </wiki-migration/university/tools/m1k/alice/meter-source-users-guide>`
-  meter-source-dac-slider.pyw
-  :doc:`ohm-meter-tool.pyw </wiki-migration/university/tools/m1k/alice/ohmmeter-users-guide>`
-  ohm-meter-vdiv.pyw
-  :doc:`strip-chart-tool.pyw </wiki-migration/university/tools/m1k/alice/stripchart-users-guide>`
-  :doc:`volt-meter-tool.pyw </wiki-migration/university/tools/m1k/alice/voltmeter-users-guide>`
-  libpysmu.pyd
-  Various icon files

Manually installing libpysmu and ALICE Python source
====================================================

The latest release of the ALICE tool set Python source files is available for download from `HERE <https://wiki.analog.com/_media/university/tools/alice-1.0.zip>`_.

To manually install on Windows the libpysmu.pyd from `libpysmu.pyd (64 bit) <https://ci.appveyor.com/api/projects/analogdevicesinc/libsmu/artifacts/libpysmu.pyd?branch=master&job=Platform%3A%20x64>`_ `libpysmu.pyd (32 bit) <https://ci.appveyor.com/api/projects/analogdevicesinc/libsmu/artifacts/libpysmu.pyd?branch=master&job=Platform%3A%20x86>`_ must be placed in the C:\\Python27\\DLLs directory. Desk-top short cuts to the various programs will need to be added manually.

OS X and Linux users will currently have to compile their own version of libpysmu.so from the libsmu source in :git-libsmu>`__. The command to make things, is just ``make python``. You will also need the development version of python installed (``apt-get install python2.7-dev``).

Raspberry Pi users with Raspbian need to have the Jessie distribution installed which includes the most up to date versions of gcc ( 4.9.2 ) and libusb-1.0-0-dev (``apt-get install libusb-1.0-0-dev libudev-dev``). As with other Linux OS the command to make things, is just ``make python``. You will also need the development version of python installed (``apt-get install python2.7-dev``).

Manually installing numpy Python extension
==========================================

For Linux users, numpy might already be part of your Python 2.7 distribution. Otherwise you can download and install numpy through the software :`GitHub <package manager on your particular version of Linux.

For Windows users, there are Windows binary installers that can be downloaded from `SourceForge <https://sourceforge.net/projects/numpy/files/NumPy/1.10.2>`. The latest version may or may not have a Windows binary so you may need to look back one or two version releases to find a Windows binary. As of this writing the newest version with a binary is numpy-1.10.2-win32-superpack-python2.7.exe 2015-12-14. Be sure to download the version for Python 2.7! Note that the developers have only created a Windows binary for 32 bit Python 2.7. Users more familiar with building from source code can download the source archive and use the setup scripts to install ( build ) numpy for their 64 bit version of Python.
