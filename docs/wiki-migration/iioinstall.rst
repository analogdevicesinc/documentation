Helpful Links and Tips for Installing All Things IIO Based
==========================================================

Sometimes it can be difficult to navigate all of the documentation to install the IIO based library or device that you want. This site is a compilation of various tips and links to help you with that installation.

--------------

**Windows Installation**

-  **Install the** :git-plutosdr-m2k-drivers-win:`PlutoSDR driver <releases>`. Download the latest PlutoSDR-M2k-USB-Drivers.exe file.
-  **Install the** :git-libiio:`libiio <releases/latest>` **Library**. Download the latest libiio-xxxxx-windows-setup.exe file.
-  **Install** :git-iio-oscilloscope:`IIO-Scope <releases>`. Download the latest adi-osc-setup.exe file.
-  \*\* GNU Radio Installation (optional) \*\*

   -  Download the most recent "radioconda-Windows-x86_64.exe" Radioconda install package here: https://github.com/ryanvolz/radioconda
   -  Update Radioconda to the latest version of PYADI-IIO

      -  Delete Radioconda's "adi" folder in radioconda/lib/site-packages
      -  Git clone :git-pyadi-iio>`__ (using a program like "Tortoise GIT")
      -  Copy the "adi" folder in that cloned PYADI-IIO repo to radioconda:`pyadi-iio <lib/site-packages

   -  Test the GNU Radio Installation

      -  Open GNU Radio Companion and place a "Python Module" block
      -  Open that block in an editor and type:
      -

      |image1|

         -  Sometimes it is necessary to included the path to the cloned pyadi-iio directory (as shown in the image above)

--------------

**Linux (Ubuntu 24 was used)**

-  \*\* Install `libiio <https://github.com/analogdevicesinc/libiio/releases/latest>`:\*\*

   -  Pick your Linux distribution from the list :git-libiio:`here <releases/latest>`.
   -  Or install from source

      -  :git-libiio:`README_BUILD`.md
      -  But change the git clone line to:

         -  git clone https://github.com/analogdevicesinc/libiio.git --branch libiio-v0
         -  libiio-v0 is always the latest, stable, branch. This command as of (Sept 2024) will install libiio v0.25
         -  If you run into any errors with install, try repeating that command with sudo

-  **Install PYADI-IIO** (from source is recommended but not always necessary)

   -  https://analogdevicesinc.github.io/pyadi-iio/guides/quick.html

-  **libad9361-iio library** : You will need the https://github.com/analogdevicesinc/libad9361-iio library.

   -  Instructions for building it are :doc:`here </wiki-migration/resources/eval/user-guides/ad-fmcomms5-ebz/multi-chip-sync>`.

-  **IIO-Scope:** Linux users will need to build from `source <https://github.com/analogdevicesinc/iio-oscilloscope>`_. Build instructions are :doc:`here </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`. You can skip the build of libiio and libad9361-iio steps, since you already did that.
-  **Install GNU Radio** (optional): https://wiki.gnuradio.org/index.php/UbuntuInstall

--------------

**ADI-Kuiper Linux** (instructions for Raspberry Pi 4 are given):

-  **Download ADI-Kuiper Linux** here: :doc:`kuiper-linux </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`

   -  Write ADI-Kuiper-full.img to an SD card
   -  Windows users can use Win32 Disk Imager. Writing img files to an SD card will work even on computers with bitlocker or where normally writing to an SD card is encrypted.

-  **Install SD Card** into Raspberry Pi, and boot up. First boot may take a few minutes extra
-  **If you are using the Phaser (CN0566)**, or if you just want to enable some extra features, follow this Phaser :doc:`quickstart </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0566/quickstart>`
-  \*\* GNU Radio Installation (optional) \*\*

   -  The June 2024 version of ADI-Kuiper Linux contains GNU Radio 3.8.2
   -  If you need to update to GNU Radio 3.10, you can try this:
   -  Remove GRC3.8.2 by: sudo apt remove gnuradio
   -  Install GRC3.10 by following https://wiki.gnuradio.org/index.php?title=LinuxInstall#From_Source

      -  Make sure to install these dependencies (Focal Fossa): https://wiki.gnuradio.org/index.php?title=UbuntuInstall#Install_Dependencies
      -  Then install Volk
      -  Then follow the instructions to install GNU Radio. **BUT** use (sudo) git checkout maint-3.10

--------------

.. important::

   If you run into any questions, please ask on this Support Forum: :ez:`ez>adieducation/university-program/f/q-a <adieducation/university-program/f/q-a>`


.

.. |image1| image:: https://wiki.analog.com/_media/grc_windows_test.png
   :width: 400px
