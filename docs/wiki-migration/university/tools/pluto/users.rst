ADALM-PLUTO for End Users
=========================

.. image:: https://wiki.analog.com/_media/university/tools/pluto/pluto_in_hand.png
   :align: right
   :width: 200px

Everyone using Pluto should read these pages. They will demonstrate how to interact with RF signals with MATLAB, Simulink, GNU Radio or custom C, C++, C#, or Python code on a host (x86) or embedded (Raspberry Pi, Beaglebone, 96boards.org, etc.) platform over USB. As you can see, we have lots of examples with MATLAB and Simulink, as we find that a very powerful environment, and a path to a releasable radio (you can take your algorithms, and easily embed them into a custom product).

Contents
--------

.. container:: hide

   Make sure all things are in ./users


-  :doc:`Introduction to the Hardware </wiki-migration/university/tools/pluto/users/intro>`

   -  :doc:`What's with the name? </wiki-migration/university/tools/pluto/users/name>` *PlutoSDR?*
   -  :doc:`Understanding the Internals </wiki-migration/university/tools/pluto/users/understanding>`
   -  :doc:`How hot? </wiki-migration/university/tools/pluto/users/temp>`
   -  :doc:`How Far, How fast? </wiki-migration/university/tools/pluto/users/far_fast>`

      -  :doc:`RF Output </wiki-migration/university/tools/pluto/users/transmit>`

         -  :doc:`Phase Noise & Accuracy </wiki-migration/university/tools/pluto/users/phase_noise>`

      -  :doc:`RF Input </wiki-migration/university/tools/pluto/users/receive>`

         -  :doc:`Receiver Sensitivity </wiki-migration/university/tools/pluto/users/receiver_sensitivity>`
         -  :doc:`Dealing with Non-Quadrature signals </wiki-migration/university/tools/pluto/users/non_quad>`

   -  :doc:`Antennas </wiki-migration/university/tools/pluto/users/antennas>`
   -  `Letter of Volatility <https://wiki.analog.com/_media/./users/letter_of_volatility_pluto.pdf>`__

-  :doc:`Quick Start </wiki-migration/university/tools/pluto/users/quick_start>`
-  Intro to the Software. Installing Device Drivers on:

   -  :doc:`Windows </wiki-migration/university/tools/pluto/drivers/windows>`
   -  :doc:`Linux </wiki-migration/university/tools/pluto/drivers/linux>`
   -  :doc:`MAC </wiki-migration/university/tools/pluto/drivers/osx>`

-  Upgrading the the ADALM-PLUTO :doc:`Firmware </wiki-migration/university/tools/pluto/users/firmware>` .
-  :doc:`Calibrating </wiki-migration/university/tools/pluto/users/calibration>` the ADALM-PLUTO.
-  :doc:`Customizing </wiki-migration/university/tools/pluto/users/customizing>` the ADALM-PLUTO.
-  Once the driver are configured and set up, you can interact with the :adi:`ADALM-PLUTO` Active Learning Module from:

   -  :doc:`IIO oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`
   -  `gqrx <http://gqrx.dk/>`__, an open source software defined radio receiver (SDR) powered by the GNU Radio
   -  `Official support for MATLAB and Simulink <https://www.mathworks.com/hardware-support/adalm-pluto-radio.html>`__
   -  :doc:`MATLAB IIO Bindings </wiki-migration/resources/tools-software/linux-software/libiio/clients/matlab_simulink>`
   -  :doc:`GNU Radio </wiki-migration/resources/tools-software/linux-software/gnuradio>`
   -  `SDRangel <https://github.com/f4exb/sdrangel>`__, an Open Source Qt5 / OpenGL 3.0+ SDR and signal analyzer frontend to various hardware.
   -  `SDR# <https://airspy.com/download/>`__. The PlutoSDR frontend for SDRsharp can be found here: `sdrsharp-plutosdr <https://github.com/Manawyrm/sdrsharp-plutosdr>`__
   -  `SoapySDR <https://github.com/pothosware/SoapySDR>`__. The Soapy SDR plugin for PlutoSDR can be found here: `SoapyPlutoSDR <https://github.com/jocover/SoapyPlutoSDR>`__
   -  `Access and control of PlutoSDR hardware using python bindings to libiio <https://github.com/radiosd/PlutoSdr>`__
   -  :doc:`Python Interfaces </wiki-migration/resources/tools-software/linux-software/pyadi-iio>`
   -  :doc:`C Examples </wiki-migration/university/tools/pluto/controlling_the_transceiver_and_transferring_data>`

-  `accessories <https://wiki.analog.com/accessories>`__
-  `asee_papers <https://wiki.analog.com/asee_papers>`__
