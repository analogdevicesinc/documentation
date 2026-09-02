.. _ad5766:

EVAL-AD5766-SDZ
===============================================================================

16-Channel, 16-Bit Voltage Output denseDAC

.. image:: images/ad5767_chip.png
      :width: 200
      :align: left

Overview
-------------------------------------------------------------------------------

The :adi:`AD5766`/:adi:`AD5767` are 16-channel, 16-/12-bit, voltage output
digital-to-analog converters (DAC). The DACs generate output voltage ranges
from an external 2.5 V reference. Depending on the span selected, the
mid-point of the output span can be adjusted allowing for a minimum output
voltage as low as -20 V or a maximum output voltage of up to +14 V.

The :adi:`AD5766`/:adi:`AD5767` have integrated output buffers which can sink
or source up to 20 mA. This makes the devices suitable for Indium Phosphide
Mach Zehnder Modulator (InP-MZM) biasing applications.

The part incorporates a power-on reset circuit that ensures that the DAC
outputs power up to 0 V and remain at this level until the output range of the
DAC is configured. The outputs of all DACs are updated through register
configuration, with the added functionality of user-selectable DAC channels to
be simultaneously updated.

The :adi:`AD5766`/:adi:`AD5767` require four power supplies. AVCC is the analog
supply for the low voltage DAC circuitry. AVDD and AVSS are the positive and
negative high voltage power supplies for the output amplifiers. A VLOGIC supply
pin is provided to set the logic levels for the digital interface pins.

The devices utilize a versatile 4-wire serial interface that operates at clock
rates of up to 50 MHz for write mode and up to 10 MHz for readback and
daisy-chain mode, and is compatible with SPI, QSPI, MICROWIRE, and DSP
interface standards.

Features:

- Complete 16-channel, 12/16-bit DACs
- 8 software-programmable output ranges
- Integrated reference buffers
- Channel monitoring multiplexer
- 1.8 V logic compatibility
- Integrated DAC output buffers

Applications:

- Mach Zehnder Modulator Bias Control
- Analog Output Modules
- Process Control
- Optical Networking
- Instrumentation
- Industrial Automation
- Data acquisition systems

.. image:: images/eval-ad5766-sd2z.png
   :align: center
   :width: 400

.. toctree::
   :hidden:

   user-guide
   prerequisites
   quickstart/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

To better understand the :adi:`AD5766` / :adi:`AD5767`, we recommend to use
the :adi:`EVAL-AD5766/67-SD2Z <EVAL-AD5766>` evaluation board.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`ad5766 user-guide` - what you need to know about the
      evaluation board
   #. :ref:`ad5766 prerequisites` - what you need to get started with the setup
   #. :ref:`ad5766 quickstart`:

      #. Using the :ref:`ZedBoard <ad5766 zed>`

#. Design with the AD5766/AD5767

   - :ref:`ad5766 block-diagram`

     - :adi:`AD5766 product page <AD5766>`
     - :adi:`AD5767 product page <AD5767>`

   - Resources for designing a custom AD5766/AD5767-based platform software

     - :external+hdl:ref:`HDL reference design <ad5766_sdz>`
     - :external+no-OS:doc:`No-OS example project <projects/dac/ad5766-sdz>`
     - :git-hdl:`HDL project <projects/ad5766_sdz>`
     - :git-no-OS:`No-OS project <projects/ad5766-sdz>`
     - :git-no-OS:`No-OS driver <drivers/dac/ad5766>`
     - :git-linux:`Linux driver <drivers/iio/dac/ad5766.c>`

#. :ref:`Help and Support <help-and-support>`

.. _ad5766 block-diagram:

Block Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/ad5766_block_diagram.png
   :align: center

More Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :external+hdl:ref:`ADI Reference Designs HDL User Guide <user_guide>`
- :adi:`AD5766 Product Page <AD5766>`
- :adi:`AD5767 Product Page <AD5767>`

Support
-------------------------------------------------------------------------------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.