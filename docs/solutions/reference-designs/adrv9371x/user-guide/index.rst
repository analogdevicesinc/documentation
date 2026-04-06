User Guide
================================================================================

.. toctree::
   :hidden:

   ad9371_osc_main
   ad9371_plugin
   ad9371_advanced_plugin
   filters
   basic_iq_datafiles

IIO Oscilloscope
--------------------------------------------------------------------------------

The :git-iio-oscilloscope:`ADI IIO Oscilloscope <>`  is a cross platform GUI
application, which demonstrates how to interface different evaluation boards
from within a Linux system. The application supports plotting of the captured
data in four different modes (time domain, frequency domain, constellation and
cross-correlation). The application also allows to view and modify several
settings of the evaluation board's devices.

To learn how to use the IIO Oscilloscope with the :adi:`AD9371`, check out the
following pages:

- :doc:`/solutions/reference-designs/adrv9371x/user-guide/ad9371_osc_main`
- :doc:`/solutions/reference-designs/adrv9371x/user-guide/ad9371_plugin`
- :doc:`/solutions/reference-designs/adrv9371x/user-guide/ad9371_advanced_plugin`

MATLAB Support
--------------------------------------------------------------------------------

MATLAB support is provided through the
:doc:`/software/matlab/transceiver-toolbox/index`, with unique classes for
transmit and receive functionality. The :adi:`AD9371` can be controlled via
MATLAB using example scripts which are available as part of the
:git-TransceiverToolbox:`Transceiver Toolbox <>`. The toolbox can either be
manually downloaded from the Releases section of the GitHub page, or downloaded
and installed via MATLAB Add-On Explorer. MATLAB is used to exercise the board
through :doc:`LibIIO </software/libiio/index>` objects and provide higher level
application functionality.

Additionally, a :doc:`Filter Design Wizard</solutions/reference-designs/adrv9371x/user-guide/filters>`
can used to design the transmitter and receiver FIR filters for the AD9371
product family.
