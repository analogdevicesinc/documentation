.. _eval-ad6676 user-guide:

User guide
===============================================================================

.. image:: images/Eval-AD6676.jpg
   :align: center
   :width: 500

Hardware guide
-------------------------------------------------------------------------------

Power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The power supply comes from the FMC connector, given by the FPGA carrier
board. The :adi:`EVAL-AD6676` evaluation board uses an on-board LDO
regulator powered through the FMC interface to generate the required
**1.1V** and **2.5V** supply domains for the :adi:`AD6676`.

The board requires **VADJ set to 2.5V**. The VADJ configuration can be
found in the README.md file at: :git-hdl:`projects/ad6676evb/zc706`.

Clock configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clock source selection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On the FMC card, choose between the available CLKIN sources:

#. **On-board 200 MHz XO** (default) — R95 and R100 installed
#. **External clock via J5** — remove R95 and R100

The ADC clock frequency (FADC) operates between 2.0 GHz to 3.2 GHz
when using an external synthesizer, or 2.925 GHz to 3.2 GHz when using
the internal synthesizer.

Clock routing options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On the FMC card, choose between the available clock routing options:

#. **PECL comparator** (default) — C35, C47, C48 installed (C38, C45,
   C46 uninstalled); CLKIN is routed through a PECL-output comparator
   that drives the AD6676 clock inputs.
#. **Direct RF via ceramic balun** — install C38, C45, C46 and remove
   C35, C47, C48.

JESD204B reference and device clocks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The JESD204B interface operates with the following clock relationships:

- **Lane rate**: 4 Gbps
- **Reference clock**: 200 MHz (lane rate / 20)
- **Device clock**: 100 MHz (lane rate / 40)
- **ADC clock (FADC)**: 3200 MHz

RF and data interfaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`AD6676` is a highly integrated IF subsystem that can digitize
radio frequency (RF) bands up to 160 MHz in width centered on an
intermediate frequency (IF) of 70 MHz to 450 MHz.

- **High instantaneous dynamic range**

  - Noise figure (NF) as low as 13 dB
  - Noise spectral density (NSD) as low as −159 dBFS/Hz
  - IIP3 up to 36 dBm with spurious tones <−97 dBFS

- **Tunable band-pass Σ-Δ analog-to-digital converter (ADC)**

  - 70 MHz to 450 MHz IF center frequency
  - 2.0 GSPS to 3.2 GSPS ADC clock rate
  - 16-bit I/Q rate up to 266 MSPS

- **On-chip digital signal processing**

  - NCO and quadrature digital downconverter (QDDC)
  - Selectable decimation factor of 12, 16, 24, and 32

- **Automatic gain control (AGC) support**

  - On-chip attenuator with 27 dB span in 1 dB steps

- **Data interface**: Single or dual lane JESD204B, subclass 1

  - M=2 converters, S=1 sample per frame, NP=16 bits
  - L=2 lanes: F=2 octets per frame
  - L=1 lane: F=4 octets per frame
  - 8B10B encoding

- **Control interface**: SPI interface for setup and control

Analog input
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connect the IF signal to the SMA connector on the evaluation board.
The :adi:`AD6676` contains a 50 Ω input attenuator programmable in
1 dB steps with a range from 0 to −27 dB.

.. Schematic, PCB Layout, Bill of Materials
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. Design files for the :adi:`EVAL-AD6676` evaluation board:

.. - `AD6676 Evaluation Board Schematic (PDF) <https://wiki.analog.com/_media/resources/eval/user-guides/13039d_sch.pdf>`_
.. - `AD6676 Evaluation Board Gerber Files (ZIP) <https://wiki.analog.com/_media/resources/eval/user-guides/13039d_gerber.zip>`_
.. - `AD6676 Evaluation Board BOM (XLS) <https://wiki.analog.com/_media/resources/eval/user-guides/13039d_bom.xls>`_

IBIS models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. - `AD6676 IBIS Model (ZIP) <https://wiki.analog.com/_media/resources/eval/user-guides/ad6676_ibis.zip>`_

- AD6676 IBIS AMI Model — email highspeed.converters@analog.com to request

Software guide
-------------------------------------------------------------------------------

The :adi:`EVAL-AD6676` evaluation board is supported with the
:git-libiio:`libiio library </>`. This library is cross-platform
(Windows, Linux, Mac) with language bindings for C, C#, Python, MATLAB,
and others.

.. include-template:: ../common/using-iio-osc.rst.jinja

   has_linux: true
   has_no_os: true
   has_local_connection: true
   show_linux_connection_image: true
   linux_connection_image: images/conection_ad6676.png
   iio_has_plugin: false
   iio_show_data_capture: true
   iio_show_time_domain: true
   iio_time_domain_image: images/ad6676_iio_timedomain.png
   iio_show_frequency_domain: true
   iio_frequency_domain_image: images/ad6676_iio_freqdomain.png

.. include-template:: ../common/using-scopy.rst.jinja

   scopy_has_plugin: false

PyADI-IIO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:git-pyadi-iio:`PyADI-IIO </>` is a Python abstraction module for ADI
hardware with IIO drivers. An :adi:`AD6676` example can be found
:git-pyadi-iio:`here </examples/ad6676.py>`.

Linux driver
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. seealso::
   :external+linux:doc:`AD6676 Linux device driver <drivers/iio-adc/ad6676>`

No-OS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. seealso::
   :external+no-OS:doc:`AD6676 no-OS Project <projects/adc/ad6676-ebz>`
