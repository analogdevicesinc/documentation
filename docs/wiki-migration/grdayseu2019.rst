European GNU Radio Days 2019 Workshops
======================================

For those attending the :adi:`PlutoSDR` workshop at European GNU Radio Days 2019, hosted by ADI, thanks. In order to make your experience better (less installing software while others are using the hardware) please have the following software installed on your machine:

-  **libIIO library:**

   -  Packages for Linux and Windows are available here: :git-libiio:`releases/latest`
   -  Source available here: https://github.com/analogdevicesinc/libiio. If you want to build from source, feel free; master works fine.
   -  Documentation: :doc:`What is libiio? </wiki-migration/resources/tools-software/linux-software/libiio>`

-  **libad9361-iio library**

   -  for linux users only, you will need the https://github.com/analogdevicesinc/libad9361-iio library.
   -  Instructions for building it are :doc:`here </wiki-migration/resources/eval/user-guides/ad-fmcomms5-ebz/multi-chip-sync>`.

-  **IIO-Scope:**

   -  Windows installers are available here: :git-iio-oscilloscope:`releases`
   -  Linux users will need to build from source: https://github.com/analogdevicesinc/iio-oscilloscope. Build instructions are :doc:`here </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`. You can skip the build of libiio and libad9361-iio steps, since you already did that.
   -  Documentation: :doc:`IIO Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`

-  **GNU Radio with IIO support:**

   -  A prebuilt binary for Windows users is available here: https://ci.appveyor.com/api/buildjobs/3cigr6q3sb6tb7li/artifacts/gnuradio_3_7_11_iiosupport.msi

      -  If you need the Windows version of GNU Radio, you likely need the Windows driver from :git-plutosdr-m2k-drivers-win:`releases/latest`.

   -  Installation instructions for Linux users are here: :doc:`GNU Radio </wiki-migration/resources/tools-software/linux-software/gnuradio>`

.. important::

   If you run into any questions while downloading, or building, please ask on the Pluto Support Forum at ADI's :ez:`Engineerzone <university-program>`, where all workshop developers answer questions


.

Slides and Labs
===============

`Pluto Labs <https://wiki.analog.com/_media/plutotutorial.zip>`_
