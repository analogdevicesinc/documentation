GRCon 2018 Workshops
====================

For those attending the PlutoSDR workshop at GRCon 2018, hosted by ADI, thanks. In order to make your experience better (less installing software while others are using the hardware) please have the following software installed on your machine:

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

.. warning::

   Those installing on Linux use the **attr-block** branch of gr-iio. This contains the new IIO Attribute blocks needed for the labs


The Workshops are on Tuesday. If you would like to come by the booth, and check out things with your hardware on Monday during the expo hours, it would be appreciated. Also - attending Michael Hennerich's discussion on *ARM PlutoSDR With Custom Applications* Monday afternoon is highly recommended.

.. important::

   If you run into any questions while downloading, or building, please ask on the Pluto Support Forum at ADI's :ez:`Engineerzone <university-program>`, where all workshop developers answer questions


.

Slides and Labs
===============

Sessions

-  `PlutoSDR session <https://github.com/sdrforengineers/LabGuides/tree/master/grcon2018>`_
