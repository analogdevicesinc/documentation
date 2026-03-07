How to build a radio with the M2k
=================================

Background
----------

In order to be able to process radio signals with ADALM2000 is necessary a receiver that can convert the incoming RF signal to a lower intermediate frequency. The FM signal, centered on a carrier frequency with high values, is reduced to an intermediate value, called IF, through a downconverter receiver. The receiver built for the m2k-radio has a basic radio architecture with four main components: Antenna, Low noise amplifier, Mixer and a Local oscillator. These 3 main parts need additional components (usually some filters) in order to work well together and receive signals in certain desired bandwidths.


|image1|

.. container:: centeralign

   Figure 1. Block Schematic of the M2k Receiver


-  **Low noise amplifie\ r**: Because antennas are sources of weak signal, it is necessary to amplify the signal received through it but is also important to keep the noise level as low as possible. For this purpose, is used a low noise amplifier which amplifies a low power signal without introducing additional noise. As FM radio has a 200kHz bandwidth, from 88.1 to 108.1 MHz is important to use an LNA with a bandwidth that includes these frequencies.
-  **Mixer**: A well-suited IC component for RF to IF down-conversion applications is the AD831 Low Distortion Mixer. It consists of a mixer core, a limiting amplifier, a low noise output amplifier, and a bias circuit. The mixer produces a high-level output at IFP and IFN—consisting of the sum and difference frequencies of the RF and LO inputs.
-  **Local Oscillator**: The Local oscillator of this receiver can be implemented using ADF4351 component. This is a wideband synthesizer with integrated VCO which allows implementation of fractional-N or integer-N phase-locked loop (PLL) frequency synthesizers when used with an external loop filter and external reference frequency. The optimum LO frequency and power can be software programmed on the ADF4351.

Hardware setup:
---------------

EVAL boards interconnection
~~~~~~~~~~~~~~~~~~~~~~~~~~~

For building a first prototype, it is possible to find each block in the form of an EVAL-board which has all the necessary components already integrated and is ready to be easily used in the project. The blocks are interconnected with SMA connectors. The filters between the blocks can be used to reduce the unwanted frequencies so the acquired signal is at a better quality.


|image2|

.. container:: centeralign

   Figure 2. EVAL Boards


Power Supplies
~~~~~~~~~~~~~~

The last thing necessary, from a hardware point of view, is the power supply. Using an external supply and some voltage regulators is possible to implement an easy solution. In this case, with a 12V supply and simple voltage regulators together with their bypass capacitors you can implement the 5V and 9V supplies needed for the boards.

.. image:: https://wiki.analog.com/_media/university/tools/adalm2000/supplies.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3. Power Supplies schematic


   |image3|

.. container:: centeralign

   Figure 4. Power Supplies breadboard connections


The outputs of the regulators should be connected on the corresponding VCC pins/pads of each board (5V for LNA and PLL, 9V for the mixer).

Connections to M2k
~~~~~~~~~~~~~~~~~~

::

     1+ - AD831 IFout
   1- - AD831 GND (outer part of the SMA connector)
     2+ -
     2- -
     W1 –  
     DIO0 - ADF4351 CLK
     DIO1 - ADF4351 DATA
     DIO2 - ADF4351 LE
     DIO3 - ADF4351 MUXOUT

     |image4|

.. container:: centeralign

   Figure 5. M2k Pinout


   |image5|

.. container:: centeralign

   Figure 6. M2k Radio Receiver


Software
--------

GNU Radio is a free and open-source software development toolkit that provides signal processing blocks to implement software radios. GNU Radio Companion (GRC) is a graphical tool for creating signal flow graphs and generating flow-graph source code. GNU Radio can be extended with own functionality and blocks using OutOfTreeModules. gr-m2k is a module containing blocks for interfacing with ADALM2000.

Creating a flowgraph in GRC, using GNU Radio 3.8, is an easy and fast solution. There are two possible approaches:

-  Creating a new out-of-tree module. Please check the available OutOfTreeModules `documentation <https://wiki.gnuradio.org/index.php/OutOfTreeModules#Tools_and_resources_at_my_disposal>`_
-  Integrating the ADF4350 block with gr-m2k

All steps for integrating ADF4350 with gr-m2k will be further explained.

ADF4350 block
~~~~~~~~~~~~~

Controlling the radio implies controlling the output voltage frequency of ADF4350. A GRC block, integrated with M2k blocks, that controls the frequency can be created. no-OS provides a driver for ADF4350 that simplifies the work. This driver communicates using SPI. In the following steps we are going to create a GRC block for gr-m2k that uses libm2k communication segment integrated with no-OS drivers.

-  Install libm2k. Instructions can be found :doc:`here </wiki-migration/university/tools/m2k/libm2k/libm2k>`.
-  Compile the gr-m2k blocks for your PC. Check the steps :doc:`here </wiki-migration/university/tools/m2k/libm2k/gr-m2k>`.
-  Download the ADF4350 driver from :git-no-OS:`no-OS page <drivers/frequency/adf4350>`.

The steps to implement a GRC block:

-  Create the inclusion header
-  Create the implementation class

   -  Add the driver
   -  Implement the class

-  Create python bindings
-  Create the GRC component

Project structure:

-  gr-m2k

   -  grc

      -  m2k_adf4350_sink.block.yml

   -  include/m2k

      -  adf4350_sink.h

   -  lib

      -  drivers

         -  adf4350.h
         -  adf4350.c
         -  spi.h

      -  adf4350_sink_impl.h
      -  adf4350_sink_impl.cc

   -  swig

      -  m2k_swig.i

**Create the inclusion header**

Create *adf4350_sink.h* in gr-m2k/include/m2k.

Add this file in the corresponding CMake file.

::

     install(FILES
     ...
     adf4350_sink.h
     DESTINATION ${GR_INCLUDE_DIR}/m2k)

In the make function add as parameters the URI and all attributes from the adf4350_init_param structure (23 attributes) found in the driver. This way they could be change from GRC without hard coding them.

**Create the implementation class**

In this part we are going to integrate libm2k with a no-OS driver. For more information please check this :doc:`link </wiki-migration/university/tools/m2k/libm2k/digital_communication>`.

Create *adf4350_sink_impl.h* and *adf4350_sink_impl.cc* in gr-m2k/lib. Create a drives directory in gr-m2k/lib and add the ADF4350 driver. Add both source files in the corresponding CMake file.

::

     list(APPEND m2k_sources
     ...
     adf4350_sink_impl.cc
     drivers/adf4350.c)

Create a header called *spi.h* and include the SPI header of libm2k:

::

     //spi.h
     #include <libm2k/tools/spi.hpp>

ADF4350 block will receive a message from a QT GUI block. The message contains the value of the frequency. The adf4350_sink_impl class has to implement the class constructor and a method (*write_attribute*) that will receive the message and will communicate with the chip in order to set its output frequency.

In the source file (*adf4350_sink_impl.cc*) include the SPI extra header of libm2k (*<libm2k/tools/spi_extra.hpp>*). In the constructor open the context and initialize m2k_spi_init structure :

::

     libm2k::contexts::M2k *context = analog_in_source_impl::get_context(uri);
     m2k_spi_init m2KSpiInit;
     m2KSpiInit.clock = 0;
     m2KSpiInit.mosi = 1;
     m2KSpiInit.miso = 7;
     m2KSpiInit.bit_numbering = MSB;
     m2KSpiInit.context = context;

Initialize the adf4350 structure with the given parameters. The first parameter, spi_init_param, should contain these values:

::

     {
         1000000,
         2,
         SPI_MODE_0,
         (void*)&m2KSpiInit
     }

*write_attribute* function is supposed to:

-  receive the message
-  convert it into a number
-  pass the value to the driver, in order to set the output frequency of ADF4350

::

     pmt::pmt_t key;
     
     if (!is_pair(pdu)) {
         throw std::runtime_error("Message not a pair!\n");
     }
     
     key = pmt::car(pdu);
     std::string skey = pmt::symbol_to_string(key);
     
     if (skey == "frequency") {
         long long frequency;
         pmt::pmt_t freq = pmt::cdr(pdu);
         std::string sfreq = pmt::symbol_to_string(freq);
         frequency = std::stoll(sfreq);
         adf4350_out_altvoltage0_frequency(d_adf4350_device, frequency);
         std::cout << "ADF4350: PLL 0 frequency = " << frequency << "Hz." << std::endl;
     }

**Create python bindings**

In swig directory is a file called *m2k_swig.i*. Include the block's header in this file:

::

    %{
    ...
    #include "m2k/adf4350_sink.h"
    %}
    
    ...
    %include "m2k/adf4350_sink.h"
    
    ...
    GR_SWIG_BLOCK_MAGIC2(m2k, adf4350_sink);

**Create the GRC component**

GNU Radio 3.8 uses yml files for creating GRC blocks. Create a file *m2k_adf4350_sink.block.yml* in the *grc* directory. This file will describe how the GRC block should look like. Add all parameters using the following format:

-   id: <key>

::

         label: <name>
         dtype: <type>
         default: <value>
         hide: part  # optional

This block is a sink for messages, not streams. To specify this create the following tag:

::

     inputs:
   *   domain: message
           id: msg
           optional: false

**Build the new created block**

::

     cd build
     cmake ..
     make
     sudo make install
     cd ../..
     sudo ldconfig

The source code can be found on the gr-m2k :git-gr-m2k>`__. In order to build it, make sure to enable digital option (cmake -DDIGITAL=ON ..).

GNURadio-Companion Flowgraph
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/:`github page <university/tools/m2k/tutorials/m2k_fm.png

The file `m2k_fm.zip <https://wiki.analog.com/_media/university/tools/m2k/tutorials/m2k_fm.zip>` contains the gnuradio flowgraph. The gnuradio flowgraph acquires the data from the M2K and sets the ADF4350 PLL frequency. When changing the PLL frequency slider, the gnuradio ADF4350 block that we just written, encodes SPI messages to the PLL in order to change the frequency that is fed into the mixer. The data acquired from the mixer is captured by the M2k using GNURadio. The flow then shifts the frequency by a smaller offset in the "offset" slider. The offset slider allows fine tuning of the signal before it gets demodulated by the WBFM receiver block. Eventually the data is sent to an audio sink which plays back the radio in the speakers.

This project was presented in GRCon 2019. Slides are available `here <https://www.gnuradio.org/grcon/grcon19/presentations/Building_a_radio_with_M2K_and_spare_parts/>`_

.. |image1| image:: https://wiki.analog.com/_media/university/tools/adalm2000/block.png
   :width: 700px
.. |image2| image:: https://wiki.analog.com/_media/university/tools/adalm2000/eval.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/university/tools/adalm2000/power_supplies.png
   :width: 900px
.. |image4| image:: https://wiki.analog.com/_media/university/tools/adalm2000/pinout.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/university/tools/adalm2000/final_circ.png
   :width: 800px
