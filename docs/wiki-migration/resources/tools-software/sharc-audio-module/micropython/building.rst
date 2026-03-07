Tutorial: Building MicroPython with CrossCore Embedded Studio
=============================================================

MicroPython is an open-source software. You can build MicroPython yourself from the source code using CrossCore Embedded Studio(CCES). Either the Windows version or Linux version of CCES will work.

Make sure you have CCES installed, as well as a desktop version of Python 3.

Windows user: please download that from `Python official website <https://www.python.org/downloads/>`_. The folder containing the Python executable needs to be added to PATH. This is an option that can be enabled during installation, or you can add it manually later after the installation.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/micropython/py372_install.png

Also, please download `Git for Windows <https://gitforwindows.org/>`_ since the Makefile used for building MicroPython executes commands like 'mkdir' and 'rm'.

Linux user: you may install Python 3 from your distribution's software repository, and no extra configuration should be necessary after installation.

Start by cloning the GitHub repository of MicroPython: https://github.com/analogdevicesinc/micropython.git, you can use `Git for Windows <https://git-scm.com/download/win>`_ or `GitHub Desktop <https://desktop.github.com/>`_ to do that. Note that MicroPython relies on external repositories so cloning should be done recursively.

After cloning that onto your local computer, open the project located inside ``ports/sc5xx`` using CCES:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/micropython/open_project.png

After opening the project, build it normally using the build command.

.. note::

   If you see an error saying python could not be found, check the executable name of your Python, sometimes it is called ``python3``, sometimes it is simply ``python``. Change the executable name accordingly inside ``py/mkenv.mk``\


Now MicroPython should be built inside the folder ``ports/sc5xx/build-sam``.

Optionally, users can generate a loader file that can be flashed into the SPI Flash(This only works with Windows version, replace firmware with the path to your binary):

::

   "C:\Analog Devices\CrossCore Embedded Studio 2.8.1\elfloader.exe" -proc ADSP-SC589 -core0=firmware -init "C:\Analog Devices\CrossCore Embedded Studio 2.8.1\SHARC\ldr\ezkitSC589_initcode_core0_v10" -b SPI -f BINARY -Width 8 -bcode 0x1 -o micropython.ldr

--------------

`Using MicroPython with Bare Metal Framework#..micropython|MicroPython Overview#.new-module|Creating a New MicroPython Module <https://wiki.analog.com/_media/navigation SHARC Audio Module#.bmsdk>`_
