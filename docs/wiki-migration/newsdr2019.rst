Software-Defined Radio Workshops
================================

For those attending the PlutoSDR workshop at `NewSDR <https://www.eventbrite.com/e/newsdr-hands-on-session-with-the-pluto-sdr-tickets-61166067354>`__, hosted by Analog Devices, in order to make your experience better (less installing software while others are using the hardware) please have the following software installed on your machine:

Please install libIIO, libad9361, and IIO-Scope based on your operating system:

-  **Windows**

   -  **The** :git-plutosdr-m2k-drivers-win:`PlutoSDR driver <releases>` is available here: :git-plutosdr-m2k-drivers-win:`PlutoSDR-USB-Drivers.exe <releases/download/v0.7/PlutoSDR-M2k-USB-Drivers.exe>`
   -  **The** :git-libiio:`libiio <releases/latest>` **Library** : :git-libiio:`Windows-setup.exe <releases/download/v0.18/libiio-0.18.g4e22517-Windows-setup.exe>`
   -  :git-iio-oscilloscope:`IIO-Scope <releases>` : :git-iio-oscilloscope:`OSC-setup.exe <releases/download/v0.10-master/adi-osc-setup.exe>`

-  **Linux**

   -  **The** :git-libiio:`libiio <releases/latest>` **Library** : Pick your Linux distribution from the list :git-libiio:`here <releases/latest>`.

      -  Source available here: https://github.com/analogdevicesinc/libiio. If you want to build from source, feel free; master works fine.

   -  **libad9361-iio library** : You will need the https://github.com/analogdevicesinc/libad9361-iio library.

      -  Instructions for building it are :doc:`here </wiki-migration/resources/eval/user-guides/ad-fmcomms5-ebz/multi-chip-sync>`.

   -  **IIO-Scope:** Linux users will need to build from `source <https://github.com/analogdevicesinc/iio-oscilloscope>`__. Build instructions are :doc:`here </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`. You can skip the build of libiio and libad9361-iio steps, since you already did that.

-  **MAC**

   -  **The** :git-libiio:`libiio <releases/latest>` **Library** : Select the PKG closest to your version of macOS. :git-libiio:`High Sierra 10.13.6 <releases/download/v0.17/libiio-0.17.g5bdc242-darwin-10.13.6.pkg>` or :git-libiio:`Sierra 10.12.6 <releases/download/v0.17/libiio-0.17.g5bdc242-darwin-10.12.6.pkg>`
   -  **The** :git-libiio:`libad9361 <releases/latest>` **Library** : :git-libad9361-iio:`macOS Version <releases/download/v0.2/libad9361-0.2.pkg>`
   -  **IIO-Scope:** use brew. ``brew install tfcollins/homebrew-formulae/i-i-o-oscilloscope``

Additionally, the instructions for installing RF Blockset Models for Analog Devices RF Transceivers can be found `here <https://wiki.analog.com/university/tools/rfblkset_mdls_install>`__.

**Documentation**:

-  :doc:`What is libiio? </wiki-migration/resources/tools-software/linux-software/libiio>`
-  Documentation: :doc:`IIO Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`

If you would like to come by the earlier in the evening before 6pm, and check out things with your hardware, it would be appreciated.

.. important::

   If you run into any questions while downloading, or building, please ask on the Pluto Support Forum at ADI's :ez:`Engineerzone <university-program>`, where all workshop developers answer questions


.

Optional
--------

To use things in `MATLAB <https://www.mathworks.com//campaigns/products/trials.html?prodcode=CM>`__. Install MATLAB and Communications Toolbox using `this link <https://www.mathworks.com//campaigns/products/trials.html?prodcode=CM>`__ and then install the `support package <https://www.mathworks.com//hardware-support/adalm-pluto-radio.html>`__.

Labs
====

Lab files and lab documents: `seminar.zip <https://wiki.analog.com/_media/seminar.zip>`__
