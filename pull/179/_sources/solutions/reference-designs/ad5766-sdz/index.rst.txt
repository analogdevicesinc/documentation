.. _ad5766-sdz:

AD5766-SDZ User Guide
=====================

Introduction
------------

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

Applications
~~~~~~~~~~~~

- Mach Zehnder Modulator Bias Control
- Analog Output Modules
- Process Control

Supported Devices
-----------------

- :adi:`AD5766`
- :adi:`AD5767`

Supported Carriers
------------------

- `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__

HDL Reference Design
--------------------

Block Diagram
~~~~~~~~~~~~~

.. figure:: ad5766_sdz_analog.png
   :align: center

   AD5766-SDZ analog section block diagram

.. figure:: ad5766_sdz_logic.png
   :align: center

   AD5766-SDZ logic section block diagram

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`projects/ad5766_sdz`

HDL Documentation
~~~~~~~~~~~~~~~~~

- `AD5766-SDZ HDL project <https://analogdevicesinc.github.io/hdl/projects/ad5766_sdz/index.html>`__

Building the HDL Project
~~~~~~~~~~~~~~~~~~~~~~~~

The design is built upon ADI's generic HDL reference design framework. ADI
does not distribute pre-built bitstream files, so the project must be built
from source. Clone the HDL repository and, with the correct tools installed,
navigate to the project directory and run ``make``:

.. code-block:: bash

   cd hdl/projects/ad5766_sdz/zed
   make

A comprehensive build guide is available in the
`HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__.

Software Support
----------------

Linux Device Driver
~~~~~~~~~~~~~~~~~~~

- :git-linux:`drivers/iio/dac/ad5766.c`

No-OS Driver
~~~~~~~~~~~~~

The AD5766 No-OS driver provides a platform-independent software layer for
controlling the :adi:`AD5766`/:adi:`AD5767` DACs from bare-metal applications.

Source code:

- :git-no-OS:`drivers/dac/ad5766`
- :git-no-OS:`projects/ad5766-sdz`

More Information
----------------

- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__
- :adi:`AD5766 Product Page <AD5766>`
- :adi:`AD5767 Product Page <AD5767>`

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.
