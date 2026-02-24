.. _ad-fmcomms2-ebz-filter-wizard:

AD9361 Filter Design Wizard
=============================

The AD9361 Filter Design Wizard is a MATLAB App which can be used to design
transmitter and receiver FIR filters, taking into account the magnitude and
phase response from other analog and digital stages in the filter chain.

With this wizard, users can:

- Choose correct digital filters to use for receive and transmit
- Design the programmable FIR filters, get the filter coefficients and save
  them in a ``.ftr`` file, which can be directly loaded into the hardware
- Examine the independent response of each filter, and the composite response
  of all the filters, including both digital and analog filters

Signal Path Overview
--------------------

Transmit Path
~~~~~~~~~~~~~

The TX signal path consists of digital and analog sections separated by the
DAC. Before the DAC, there are four digital filters: a programmable poly-phase
FIR filter (PROG TX FIR) which can interpolate by a factor of 1, 2, or 4
(or be bypassed), and three fixed-coefficient digital filters (HB1, HB2,
HB3/INT3) that can be individually enabled.

.. figure:: software/txfilter.png
   :align: center

   AD9361 transmit filter chain

After the DAC, two low-pass analog filters complete the signal path.

Receive Path
~~~~~~~~~~~~

The RX signal path has two low-pass analog filters before the ADC, followed
by three fixed-coefficient digital filters (HB3/DEC3, HB2, HB1) and a
programmable poly-phase FIR filter (PROG RX FIR) which can decimate by a
factor of 1, 2, or 4 (or be bypassed).

.. figure:: software/rxfilter.png
   :align: center

   AD9361 receive filter chain

Using the MATLAB App
--------------------

After launching the MATLAB App, a drop-down list in "Device Settings" includes
default parameter profiles for several widely used LTE applications.

.. list-table:: LTE Specification Presets
   :header-rows: 1

   * - LTE Bandwidth (MHz)
     - Occupied RF BW (MHz)
     - Sample Rate (MSPS)
   * - 1.4
     - 1.08
     - 1.92
   * - 3
     - 2.7
     - 3.84
   * - 5
     - 4.5
     - 7.68
   * - 10
     - 9
     - 15.36
   * - 15
     - 13.5
     - 23.04
   * - 20
     - 18
     - 30.72

.. list-table:: AD9361 Filter Settings
   :header-rows: 1

   * - Sample Rate (MSPS)
     - Fpass (MHz)
     - Fstop (MHz)
     - Apass (dB)
     - Astop (dB)
   * - 1.92
     - 0.54
     - 0.66
     - 0.1
     - 80
   * - 3.84
     - 1.35
     - 1.65
     - 0.1
     - 80
   * - 7.68
     - 2.25
     - 2.75
     - 0.1
     - 80
   * - 15.36
     - 4.5
     - 5.5
     - 0.1
     - 80
   * - 23.04
     - 6.75
     - 8.25
     - 0.1
     - 80
   * - 30.72
     - 9
     - 11
     - 0.1
     - 80

.. note::

   The LTE Release-8 physical layer specification supports 105 different
   bandwidth options (not just the 6 shown above). Occupied RF Bandwidth
   from 1.08 MHz to 19.8 MHz with 180 kHz steps complies with the spec.

Basic Workflow
~~~~~~~~~~~~~~

.. figure:: software/1start.png
   :align: center

   MATLAB App startup with LTE preset selection

#. Select a preset profile (e.g., "LTE10 (Rx & Tx)") from the drop-down list.
   All parameters are filled automatically.

   .. figure:: software/2basic.png
      :align: center

      Parameter settings for LTE10

#. Click **Design Filter** to start the design. The magnitude plot displays
   with Fpass, Fstop, Apass and Astop highlighted.

   .. figure:: software/3basicdesign.png
      :align: center

      Filter design results with magnitude plot

#. Use the **FVTool** buttons to launch the MATLAB Filter Visualization Tool
   for detailed analysis:

   - Magnitude response of half-band filters and HB + designed FIR filter

   .. figure:: software/fvtooldatarate.png
      :align: center

      Half-band and composite filter response

   - Magnitude response of the designed FIR only (with phase, group delay,
     impulse response, and poles/zeros available via toolbar)

   .. figure:: software/6fironly.png
      :align: center

      FIR-only magnitude response

   - Overall group delay on passband with variance calculation

   .. figure:: software/5fvt2.png
      :align: center

      Group delay analysis

   - Full frequency band magnitude response

   .. figure:: software/4fvt1.png
      :align: center

      Full band magnitude response

Saving Results
~~~~~~~~~~~~~~

**Save to Workspace**: Saves the filter object and data structure to the MATLAB
workspace for use with other MATLAB functions or Simulink models.

.. figure:: software/7save2ws.png
   :align: center

   Save to workspace option

**Coefficients to ftr File**: Saves the FIR coefficients in a format compatible
with the :doc:`IIO Oscilloscope </software/iio-oscilloscope/index>`.

.. figure:: software/fig7.png
   :align: center

   Coefficient export option

.. figure:: software/8savecoeff.png
   :align: center

   File save dialog

.. note::

   Both the Transmit and Receive filters must be designed before the
   "Coefficients to ftr File" button becomes available.

Target Connection (Zynq)
~~~~~~~~~~~~~~~~~~~~~~~~~

The wizard can connect directly to Zynq-based platforms to read clock settings
and upload filter coefficients.

.. figure:: software/13connecttozynq.png
   :align: center

   Connect to target

.. figure:: software/14readclock.png
   :align: center

   Read clock settings from target

.. figure:: software/15tozynq.png
   :align: center

   Upload coefficients to target

Advanced Functions
------------------

Enable the **Advanced** option for additional controls:

.. figure:: software/9advanced.png
   :align: center

   Advanced options

Phase Equalization
~~~~~~~~~~~~~~~~~~

Reduces passband group delay variance caused by analog and digital filters.

.. figure:: software/10targetdelay.png
   :align: center

   Phase equalization option

.. figure:: software/10pheq.png
   :align: center

   Results with phase equalization (group delay variance reduced from
   16.6 ns to 1.52 ns)

External FIR Implementation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For users who want to implement the FIR filter on FPGA rather than on the
AD9361, disable the **Use Internal FIR** option. The design file then performs
a minimum-order design without the AD9361 tap count constraint.

.. figure:: software/11usefir.png
   :align: center

   External FIR option

HDL code can be generated using the **Generate HDL** button, which calls the
MATLAB ``fdhdltool`` function.

.. figure:: software/12createhdl.png
   :align: center

   HDL generation dialog

Using MATLAB Functions
----------------------

Users can also employ MATLAB functions directly from the command window:

.. code-block:: matlab

   output = design_filter(input)

The input structure contains:

- ``Rdata`` - input/output sample data rate (Hz)
- ``FIR`` - FIR interpolation/decimation factor
- ``PLL_mult`` - PLL multiplication
- ``Fpass`` - passband frequency (Hz)
- ``Fstop`` - stopband frequency (Hz)
- ``Apass`` - max ripple allowed in passband (dB)
- ``Astop`` - min attenuation in stopband (dB)
- ``FIRdBmin`` - min rejection that FIR is required to have (dB)
- ``phEQ`` - Phase Equalization on (not -1) / off (-1)
- ``int_FIR`` - Use AD9361 FIR on (1) / off (0)
- ``wnom`` - analog cutoff frequency (Hz)

The output structure contains:

- ``firtaps`` - fixed point FIR coefficients
- ``filter`` - system object for visualization
- ``delay`` - actual delay used in phase equalization

Example: Tx LTE-5
~~~~~~~~~~~~~~~~~~

.. code-block:: matlab

   >> input = ad9361_settings.tx.LTE5;
   >> output = design_filter(input);

   % Inspect individual filter stages
   TFIR = output.Hmd;
   Hm1 = output.Hm1;

   % Visualize HB1 response
   hfvt1 = fvtool(Hm1, ...
       'FrequencyRange', 'Specify freq. vector', ...
       'FrequencyVector', linspace(0, 122.88e6/2, 2048), ...
       'Fs', 122.88e6, ...
       'ShowReference', 'off', 'Color', 'White');

.. figure:: software/HB1.png
   :align: center

   HB1 filter response

C/C++ Source Code
-----------------

For users wishing to deploy or embed this filter designer into their own C/C++
source, two options are available:

#. **GPL licensed C version**: Part of the
   `libad9361-iio <https://github.com/analogdevicesinc/libad9361-iio>`__
   library, includes all necessary source to generate filter coefficients.

#. **MATLAB Coder version**: The
   `ad936x-filter-wizard <https://github.com/analogdevicesinc/ad936x-filter-wizard>`__
   repository (codegen-support branch) provides a MATLAB source enhanced for
   code generation. Required MATLAB toolboxes: MATLAB, Signal Processing
   Toolbox, Fixed-Point Designer, and MATLAB Coder.

Source Code
-----------

- `AD936x Filter Wizard (GitHub) <https://github.com/analogdevicesinc/ad936x-filter-wizard>`__
- `Design function <https://github.com/analogdevicesinc/ad936x-filter-wizard/blob/master/design_filter.m>`__
- `Internal design function <https://github.com/analogdevicesinc/ad936x-filter-wizard/blob/master/internal_design_filter.m>`__

Support
-------

If you have any questions about these scripts/tools, please ask on the
:ez:`Linux Software Drivers Forum <linux-software-drivers>`.
