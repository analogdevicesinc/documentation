GRCon 2021 Workshops
====================

ADI always is happy to support the GNU Radio community with not only `Sponsorship <https://events.gnuradio.org/event/8/page/5-sponsors>`_, presentations and the PlutoSDR Workshop.

Presentations
-------------

libIIO and the new mainline module gr-iio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Abstract <https://events.gnuradio.org/event/8/contributions/62/>`_


|youtube>Qx8uFhumgGM|

gr-genalyzer, a new OOT module to characterize data converter performance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Abstract <https://events.gnuradio.org/event/8/contributions/30/>`_


|youtube>ef30VPIx-LM|

A new Linux kernel subsystem for JESD204 RF Transceiver Systems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Abstract <https://events.gnuradio.org/event/8/contributions/63/>`_


|youtube>2s940fttDco|

Implementing OFDM Radar & DOA on DirectRF Platforms using IIO and GNURadio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Abstract <https://events.gnuradio.org/event/8/contributions/130/>`_


|youtube>BaRgx5ehdOw|

pyadi-jif: JESD204 tools for mere mortals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Abstract <https://events.gnuradio.org/event/8/contributions/61/>`_


|youtube>BaRgx5ehdOw|

Workshop
~~~~~~~~

For those attending the PlutoSDR workshop at GRCon 2021, hosted by ADI, thanks. In order to make your experience better (less installing software while others are using the hardware) please have the following software installed on your machine:

-  **libIIO library:**

   -  Packages for Linux and Windows are available here: :git-libiio:`releases/latest`
   -  For macOS users select the tar closest to your version of macOS for **libiio v0.23**.
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

   -  Installation instructions for Linux users are here: :doc:`GNU Radio </wiki-migration/resources/tools-software/linux-software/gnuradio>`
   -  For macOS GNU Radio and gr-iio can be installed from macports

.. important::

   If you run into any questions while downloading, or building, please ask on the Pluto Support Forum at ADI's :ez:`Engineerzone <university-program>`, where all workshop developers answer questions


.

Slides and Labs
---------------

Sessions

-  `PlutoSDR Workshop Labs <https://github.com/sdrforengineers/LabGuides/tree/master/grcon2020>`_
-  `PlutoSDR Workshop Slides <https://wiki.analog.com/_media/plutoworkshop.pdf>`_

.. |youtube>Qx8uFhumgGM| image:: https://wiki.analog.com/_media/youtube>Qx8uFhumgGM
.. |youtube>ef30VPIx-LM| image:: https://wiki.analog.com/_media/youtube>ef30VPIx-LM
.. |youtube>2s940fttDco| image:: https://wiki.analog.com/_media/youtube>2s940fttDco
.. |youtube>BaRgx5ehdOw| image:: https://wiki.analog.com/_media/youtube>BaRgx5ehdOw
