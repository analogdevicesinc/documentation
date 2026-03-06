SHARC Audio Module
==================

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/sam-logo.png
   :align: right
   :width: 300px

Welcome! The :adi:`SHARC® Audio Module Platform <design-center/evaluation-hardware-and-software/evaluation-boards-kits/sharc-audio-module.html>` is an expandable hardware/software platform enabling project prototyping, development and deployment of audio applications including effects processors, multi-channel audio systems, MIDI synthesizers, and many other DSP-based audio projects.

The centerpiece of the SHARC Audio Module is `Analog Devices' <http://analog.com>`__ high-performance :adi:`sharc` :adi:`ADSP-SC589 <sc58x>`. Combining two 450 MHz floating point DSP cores, a 450MHz ARM® Cortex®-A5 core and an FFT/IFFT accelerator with a massive amount of on-board I/O, the ADSP-SC589 is a remarkable engine for audio processing.

The SHARC Audio Module features two 2Gbit DDR3 memories, 512Mbit SPI flash, a UART (for MIDI & more), and a :adi:`sigmadsp` 96 kHz, 24-bit audio codec. A variety of I/O is provided, including 1/8" stereo jacks, S/PDIF, Gigabit Ethernet, USB OTG & HS as well as Analog Devices' revolutionary :adi:`A2B multi channel audio interface <a2b>`. In addition, on the underside of the board are two expansion connectors (60 pin 0.100 pitch) with access to most of the signals available on the board. Please see the :doc:`Hardware Overview </wiki-migration/resources/tools-software/sharc-audio-module/hardware/main-board>` section for more information.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/hardware/sam-main-board-top.png
   :align: left
   :width: 300px

While the SHARC Audio Module can be used as a self-contained product, it is designed for custom expansion. Analog Devices has developed expansion boards: a :doc:`Audio Project Fin </wiki-migration/resources/tools-software/sharc-audio-module/hardware/audioproj-fin>` that plugs directly onto the main SHARC Audio Module, and a :doc:`Class-D Amplifier module </wiki-migration/resources/tools-software/sharc-audio-module/hardware/class-d>` that connects over the A\ :sup:`2`\ B® bus.

In addition, there are several leading developers and board designers that provide a variety of software and hardware platforms for you to expand the SHARC Audio Module platform. Since all of the major functions and GPIO of the board can be accessed via the two multi-pin connectors, you can easily design and build your own expander. Documentation for these connectors can be found in the :doc:`SHARC Audio Module Hardware Reference Manual </wiki-migration/resources/tools-software/sharc-audio-module/hardware/main-board>`.


--------------

SHARC Audio Module Daughter Boards
----------------------------------

The SHARC Audio Module main board can be expanded using the A\ :sup:`2`\ B interface or the expansion interface. **Fins** are any extender boards that plug directly onto the SHARC Audio Module main board expansion connector. Below is a list of currently supported daughter boards for the SHARC Audio Module main board.

+----------+----------------------------------------------------------------------------------------------+---------------------+----------------------------------------------+
|          | Name                                                                                         | Connection Type     | Main Functionality                           |
+==========+==============================================================================================+=====================+==============================================+
| |image3| | :doc:`Audio Project Fin </wiki-migration/resources/tools-software/sharc-audio-module/hardware/audioproj-fin>`  | Expansion Connector | MIDI In / Out / Thru DIN connectors          |
|          |                                                                                              |                     | POTs                                         |
|          |                                                                                              |                     | push buttons                                 |
|          |                                                                                              |                     | 1/4" stereo input/output                     |
+----------+----------------------------------------------------------------------------------------------+---------------------+----------------------------------------------+
| |image4| | :doc:`Class-D Amplifier Module </wiki-migration/resources/tools-software/sharc-audio-module/hardware/class-d>` | A2B interface       | 2 SSM3582 high efficiency Class-D amplifiers |
+----------+----------------------------------------------------------------------------------------------+---------------------+----------------------------------------------+


--------------

.. important::

   All information contained throughout these wiki pages corresponds to version 2.x of the Bare Metal SDK release.


Documentation
-------------

This guide is structured as follows:

-  :doc:`Getting Started and Support </wiki-migration/resources/tools-software/sharc-audio-module/gettingstarted>` - Provides all the steps to download/install all necessary software to get up and running with your 1st SHARC Audio Module example. It will also help with support and getting familiar with CrossCore Embedded Studio.
-  :doc:`Bare Metal Framework </wiki-migration/resources/tools-software/sharc-audio-module/baremetal>` - Provides all documentation about the bare metal framework and how to use it, as well as multiple helpful tutorials.
-  :doc:`Hardware Reference </wiki-migration/resources/tools-software/sharc-audio-module/hardware>` - Provides full documentation for the SHARC Audio Module hardware as well as the various daughter cards that connect using the expansion interface or A\ :sup:`2`\ B bus.
-  :doc:`Faust and the SHARC Audio Module </wiki-migration/resources/tools-software/sharc-audio-module/faust>` - Provides details about the Faust language and how it integrates with the SHARC Audio Module.
-  :doc:`MicroPython for the SHARC Audio Module </wiki-migration/resources/tools-software/sharc-audio-module/micropython>` - Provides examples and tutorials about how to use MicroPython on the SHARC Audio Module.
-  :doc:`New and Experimental things for the SHARC Audio Module </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects>` - Provides examples and tutorials about how to set up and run some new and emerging features of the SHARC Audio Module.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/hardware/sam-diy-angle.png
   :width: 100px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/hardware/sam-class-d-angle.png
   :width: 100px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/hardware/sam-diy-angle.png
   :width: 100px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/hardware/sam-class-d-angle.png
   :width: 100px
