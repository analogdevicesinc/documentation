Software-Defined Radio Workshops
================================

For those attending the PlutoSDR workshop, hosted by ADI, MathWorks and RichardsonRFPD. In order to make your experience better (less installing software while others are using the hardware) please have the following software installed on your machine:

All attendees should have received instructions to install `MATLAB <https://www.mathworks.com//campaigns/products/trials.html?prodcode=CM>`_. If not, please use this `this link <https://www.mathworks.com//campaigns/products/trials.html?prodcode=CM>`_ and then install the `support package <https://www.mathworks.com//hardware-support/adalm-pluto-radio.html>`_. You will also need some additional software from ADI. Please install libIIO, libad9361, and IIO-Scope based on your operating system:

-  **Windows**

   -  **The** :git-plutosdr-m2k-drivers-win:`PlutoSDR driver <releases>`. Download the latest PlutoSDR-M2k-USB-Drivers.exe file.
   -  **The** :git-libiio:`libiio <releases/latest>` **Library**. Download the latest libiio-xxxxx-windows-setup.exe file.
   -  :git-iio-oscilloscope:`IIO-Scope <releases>`. Download the latest adi-osc-setup.exe file.

-  **Linux**

   -  **The** :git-libiio:`libiio <releases/latest>` **Library** : Pick your Linux distribution from the list :git-libiio:`here <releases/latest>`.

      -  Source available here: https://github.com/analogdevicesinc/libiio. If you want to build from source, feel free; master works fine.

   -  **libad9361-iio library** : You will need the https://github.com/analogdevicesinc/libad9361-iio library.

      -  Instructions for building it are :doc:`here </wiki-migration/resources/eval/user-guides/ad-fmcomms5-ebz/multi-chip-sync>`.

   -  **IIO-Scope:** Linux users will need to build from `source <https://github.com/analogdevicesinc/iio-oscilloscope>`_. Build instructions are :doc:`here </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`. You can skip the build of libiio and libad9361-iio steps, since you already did that.

-  **MAC**

   -  **The** :git-libiio:`libiio <releases/latest>` **Library** : Select the PKG closest to your version of macOS for **libiio v0.17**. :git-libiio:`High Sierra 10.13.6 <releases/download/v0.17/libiio-0.17.g5bdc242-darwin-10.13.6.pkg>` or :git-libiio:`Sierra 10.12.6 <releases/download/v0.17/libiio-0.17.g5bdc242-darwin-10.12.6.pkg>`. Mojave will work fine with the High Sierra release.
   -  **The** :git-libad9361-iio:`libad9361 <releases/latest>` **Library** : :git-libad9361-iio:`macOS Version <releases/download/v0.2/libad9361-0.2.pkg>`
   -  **IIO-Scope:** use brew. ``brew install tfcollins/homebrew-formulae/i-i-o-oscilloscope``

      -  To launch IIO-Scope run this from a terminal: ``osc``

.. important::

   For macOS you must use libiio v0.17 since the binaries for libad9361 was built against that release. If you have already built IIO-Scope with a newer release, the libraries must be downgraded first then IIO-Scope should be built again


Additionally, the instructions for installing RF Blockset Models for Analog Devices RF Transceivers can be found `here <https://wiki.analog.com/university/tools/rfblkset_mdls_install>`_.

**Documentation**:

-  :doc:`What is libiio? </wiki-migration/resources/tools-software/linux-software/libiio>`
-  Documentation: :doc:`IIO Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`

If you would like to come by the earlier in the morning before 9am, and check out things with your hardware, it would be appreciated.

.. important::

   If you run into any questions while downloading, or building, please ask on the Pluto Support Forum here: :ez:`ez>adieducation/university-program/f/q-a <adieducation/university-program/f/q-a>`


.

Labs
====

Lab files and lab documents: `seminar.zip <https://wiki.analog.com/_media/seminar.zip>`_

Slides
======

`Baltimore/Natick <https://wiki.analog.com/_media/richardsonmathworksseminars.pdf>`_
