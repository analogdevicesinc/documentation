.. _eval-ad469x-ltspice-transient-sims:

Transient simulations with AD469x LTspice model
===============================================================================

The AD469x LTspice model supports transient simulations to
evaluate the following aspects of analog front-end performance:

- **Transient glitches**: How the ADC responds to short-duration
  voltage variations at analog inputs and the effectiveness of
  kickback filters in mitigation.
- **Acquisition time**: The duration required for accurate signal
  capture and stable digital output conversion.
- **Channel sequencing**: Proper operation when processing multiple
  analog input channels sequentially.
- **AFE settling performance**: How quickly the analog front-end
  settles and minimizes measurement errors.

Schematic setup
-------------------------------------------------------------------------------

Operating conditions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure the following operating conditions in the schematic:

- **AVDD**: voltage supply for the analog section.
- **VDD**: voltage supply for other specific circuit blocks.
- **Voltage REF**: the reference voltage used in the circuit.
- **Analog input voltages**: the inputs to the ADC.

AFE parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure the analog front-end parameters:

- **Kickback filter**: a filter used to minimize any voltage spikes
  or glitches during the ADC conversion process.
- **Resistor and capacitor values**: these components contribute to
  the AFE's overall performance.

Sampling dynamics and timing delay
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure the timing delays for proper sampling behavior:

.. code-block:: spice

   .param reset_delay 1u
   .param cnv_delay = reset_delay + 50u

Configure channel sequencing parameters:

.. code-block:: spice

   .param num_sequences = 16
   .param num_channels = 2

Simulation parameters
-------------------------------------------------------------------------------

Set up the transient simulation using the following SPICE
directives:

.. code-block:: spice

   .tran 0 {tstop} {tstart}
   .param tstart = cnv_delay - tstart_buffer
   .param tstop = cnv_delay + (t_cnv * num_samples) + tstop_buffer
   .param tstart_buffer t_cnv
   .param tstop_buffer t_cnv

Analyzing settling performance
-------------------------------------------------------------------------------

Simulation setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Verify all parameters match ADC specifications and AFE
   circuitry requirements.
#. Define values in LTspice simulation command; confirm alignment
   with settling time needs.
#. Execute simulation via the **Run** button; results display in
   terminal or real-time.

Settling error measurements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Locate the ``in0_err`` and ``in1_err`` outlets after simulation
   completion.
#. Place the probe on the ``in0_err`` and ``in1_err`` outlets to
   measure the settling error in volts.
#. Wait for the settling tails in ``in0_err`` and ``in1_err`` to
   reach a steady-state value.

Sample circuit
-------------------------------------------------------------------------------

A sample transient simulation circuit is available for download:
:dokuwiki:`ad4696_transient.zip <resources/quick-start/ad469x-ltspice-user-guide/transient-sims?do=export_code>`
