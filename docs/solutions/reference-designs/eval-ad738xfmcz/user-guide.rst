.. _eval-ad738xfmcz user-guide:

User Guide
===============================================================================

Hardware guide
--------------

For detailed evaluation board hardware information including power
supplies, jumper/link configurations, connectors, and test points,
refer to the board-specific user guides:

- :ref:`eval-ad7380-4fmcz` (for AD7380-4, AD7381-4, AD7389-4)
- :ref:`eval-ad7386fmcz` (for AD7386, AD7387, AD7388, AD4684, AD4685)
- `EVAL-AD7380FMCZ/AD7381FMCZ User Guide (UG-1304) <https://www.analog.com/media/en/technical-documentation/user-guides/eval-ad7380fmcz-7381fmcz-ug-1304.pdf>`_ (for AD7380, AD7381, AD4680, AD4681)
- `EVAL-AD7386-4FMCZ User Guide (UG-2168) <https://www.analog.com/media/en/technical-documentation/user-guides/eval-ad7386-4-ug-2168.pdf>`_ (for AD7386-4 family)

Analog Inputs
~~~~~~~~~~~~~

The AD738x family offers three analog input types depending on the
device variant:

- **Differential inputs**: The :adi:`AD7380`, :adi:`AD7381`,
  :adi:`AD4680`, :adi:`AD4681`, :adi:`AD7380-4`, :adi:`AD7389-4`,
  and :adi:`AD7381-4` provide differential analog input channels.
  The differential input signals should be connected to the
  corresponding AINx+/AINx- pins on the evaluation board.

- **Pseudo-differential inputs**: The :adi:`AD7383`,
  :adi:`AD7384`, :adi:`AD4682`, and :adi:`AD4683` provide
  pseudo-differential analog input channels.

- **Single-ended inputs**: The :adi:`AD7386`, :adi:`AD7387`,
  :adi:`AD7388`, :adi:`AD4684`, and :adi:`AD4685` provide
  single-ended analog input channels (AINA, AINB for dual
  devices; AINA, AINB, AINC, AIND for quad devices).

The absolute input voltage range is determined by the reference
voltage (internal 2.5 V or external up to 3.3 V). An internal
precharge buffer on each analog input reduces input current
requirements.

For testing purposes, a signal generator can be connected to the
analog inputs using the SMA connectors on the evaluation board.
For optimal performance, use a low noise, low distortion signal
source.

HDL Design Description
----------------------

In the :dokuwiki:`ADI Reference Designs HDL User Guide <resources/fpga/docs/hdl>`
can be found an in-depth presentation and instructions about the HDL design in
general.

The reference design uses the standard :dokuwiki:`SPI Engine Framework <resources/fpga/peripherals/spi_engine>`
with an integrated pulse generator, which will provide the required conversion
rate for the ADC.

In order to build the HDL design the user has to go through the following steps:

-  Confirm that you have the right tools (the reference design requires Vivado 2018.3)
-  Clone the HDL GitHub repository (the project is located at :git-hdl:`projects/ad738x_fmc`)
-  Build the project (see :dokuwiki:`Building HDL <resources/fpga/docs/build>`)

HDL Downloads
-------------

.. admonition:: Download
   :class: download

   
   -  :git-hdl:`ad738x HDL Project. <projects/ad738x_fmc>`
   

No-OS Downloads
---------------

.. admonition:: Download
   :class: download

   
   -  :git-no-OS:`ad738x No-OS Project <projects/ad738x_fmcz>`
   
