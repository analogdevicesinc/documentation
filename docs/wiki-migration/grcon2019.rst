GRCon 2019 Workshops
====================

For those attending the PlutoSDR workshop at GRCon 2019, hosted by ADI, thanks. In order to make your experience better (less installing software while others are using the hardware) please have the following software installed on your machine:

-  **libIIO library:**

   -  Packages for Linux and Windows are available here: :git-libiio:`releases/latest`
   -  For macOS users select the PKG closest to your version of macOS for **libiio v0.17**. :git-libiio:`High Sierra 10.13.6 <releases/download/v0.17/libiio-0.17.g5bdc242-darwin-10.13.6.pkg>` or :git-libiio:`Sierra 10.12.6 <releases/download/v0.17/libiio-0.17.g5bdc242-darwin-10.12.6.pkg>`. Mojave will work fine with the High Sierra release.
   -  Source available here: https://github.com/analogdevicesinc/libiio. If you want to build from source, feel free; master works fine.
   -  Documentation: :doc:`What is libiio? </wiki-migration/resources/tools-software/linux-software/libiio>`

-  **libad9361-iio library**

   -  For linux users only, you will need the https://github.com/analogdevicesinc/libad9361-iio library.
   -  :git-libad9361-iio:`For macOS users <releases/download/v0.2/libad9361-0.2.pkg>`
   -  Instructions for building it are :doc:`here </wiki-migration/resources/eval/user-guides/ad-fmcomms5-ebz/multi-chip-sync>`.

-  **IIO-Scope:**

   -  Windows installers are available here: :git-iio-oscilloscope:`releases`
   -  Linux users will need to build from source: https://github.com/analogdevicesinc/iio-oscilloscope. Build instructions are :doc:`here </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`. You can skip the build of libiio and libad9361-iio steps, since you already did that.
   -  macOS users use brew. ``brew install tfcollins/homebrew-formulae/i-i-o-oscilloscope``

      -  To launch IIO-Scope run this from a terminal: ``osc``

   -  Documentation: :doc:`IIO Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`

-  **GNU Radio with IIO support:**

   -  A prebuilt binary for Windows users is available here: https://github.com/tfcollins/GNURadio_Windows_Build_Scripts/releases/tag/1.5.0

      -  If you need the Windows version of GNU Radio, you likely need the Windows driver from :git-plutosdr-m2k-drivers-win:`releases/latest`.

   -  Installation instructions for Linux users are here: :doc:`GNU Radio </wiki-migration/resources/tools-software/linux-software/gnuradio>`
   -  For macOS GNU Radio and gr-iio can be installed from macports

.. warning::

   Those installing on Linux do not use GNU Radio 3.8


The Workshops are on Wednesday and Thursday. If you would like to come by the booth, and check out things with your hardware on Monday or Tuesday during the expo hours, it would be appreciated.

.. important::

   If you run into any questions while downloading, or building, please ask on the Pluto Support Forum at ADI's :ez:`Engineerzone <university-program>`, where all workshop developers answer questions


.

Slides and Labs
===============

Sessions

-  `PlutoSDR Workshop Labs <https://github.com/sdrforengineers/LabGuides/tree/master/grcon2019>`_
-  `PlutoSDR Workshop Slides <https://wiki.analog.com/_media/adiplutoworkshop_grcon2019.pdf>`_
