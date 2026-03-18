.. _ad9467_fmc_250ebz user-guide:

User guide
===============================================================================

The complete evaluation board documentation can be found at
:adi:`AD9467-FMC-250EBZ product page <EVAL-AD9467>`.

Hardware guide
-------------------------------------------------------------------------------

Power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The power supply comes from the FMC connector, given by the FPGA carrier board.

.. warning::
   The recommended VADJ value for each FPGA carrier can be found in the
   corresponding README.md file :git-hdl:`here <projects/ad9467_fmc>`.

Clock configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AD9467-FMC-250EBZ supports three clock configuration options:

**Default clock input (J201)**

- Transformer-coupled, 50 Ω terminated, AC-coupled input
- Accepts single-ended sine wave inputs
- Requires external clock source (250 MHz)

**Crystal oscillator (Y200)**

- Low phase noise oscillator from Vectron (VCC6-QCD-250M000)
- Requires hardware modifications:
  - Install C205 and C206
  - Remove C202
  - Set Jumper P200 to "On" position

**AD9517-4 clock generator**

- Programmable clock generator with SPI interface
- Supports LVPECL or LVDS output
- Requires hardware modifications:

  - For LVPECL: Populate C304, C305
  - For LVDS: Populate C306, C307
  - Remove C209 and C210 to disconnect default clock path
  - Add C300, C301

Results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For testing we used an input signal with a frequency of 1 MHz and 3V amplitude

.. image:: ./images/scopy_in_sig.png

.. include-template:: ../common/using-iio-osc.rst.jinja

   has_linux: true
   iio_show_frequency_domain: true
   iio_show_time_domain: true
   iio_show_data_capture: true
   iio_frequency_domain_image: ./images/iio_fft.png
   iio_time_domain_image: ./images/iio_waveform.png

.. Schematic, PCB Layout, Bill of Materials
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   The archive from ADI contains the following:

   - :download:`Schematics <resources/ad9467_schematic.pdf>`
   - :download:`Bill of Materials <resources/ad9467_bom.xls>`
   - :download:`Gerber Files <resources/ad9467_gerber_files.zip>`

  .. important::

   C302 and C303 are not installed as indicated in the Schematic and BOM.

Software guide
-------------------------------------------------------------------------------

The evaluation board is supported with the Libiio library. This library is
cross-platform (Windows, Linux, Mac) with language bindings for C, C#, Python,
MATLAB, and others. One easy example that can be used with it is:

- :dokuwiki:`IIO Oscilloscope <resources/tools-software/linux-software/iio_oscilloscope>`

Reference designs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :external+hdl:ref:`AD9467_FMC HDL reference design <ad9467_fmc>`

Additional resources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :adi:`AD9467 datasheet <media/en/technical-documentation/data-sheets/ad9467.pdf>`
- :adi:`AN-835: Understanding ADC Testing and Evaluation <en/resources/app-notes/an-835.html>`
- :dokuwiki:`ADI SPI Application Note <resources/technical-guides/adispi>`
