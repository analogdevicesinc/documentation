.. _ad7606c_remotecontrol:

AD7606B/C ACE Remote Control
==============================

By using `ACE Remote Control
<https://wiki.analog.com/resources/tools-software/ace/remotecontrol>`_,
AD7606B and AD7606C plug-ins can be automated to perform several evaluation
activities across the different analog input ranges, bandwidth modes,
channels, etc. Different example scripts are given in the MATLAB examples
section.

Without hardware, the
:adi:`AD7606x Family software model <en/products/ad7606b.html#product-tools>`
can be used to try different configurations for both AD7606C and AD7606B:
sampling rate, RC filtering, oversampling, calibration; and analyze frequency
response, noise performance, interface timing or power consumption, among
others.

All the below features can also be tested using the
:ref:`AD7606 Mbed IIO Application <ad7606_mbed_iio_application>`, which
uses No-OS drivers and interfaces with SDP-K1 or STM32 Nucleo boards.

Getting Started
---------------

Hardware
~~~~~~~~

- :adi:`SDP-H1 Controller board
  <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-sdp-h1.html>`
  and its 12 V DC wall adapter
- :adi:`AD7606C Evaluation Board
  <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad7606c-18.html>`
  or an equivalent board with any of the following ADCs:

  - AD7606B
  - AD7606C-18
  - AD7606C-16

Software
~~~~~~~~

- :adi:`ACE software
  <en/design-center/evaluation-hardware-and-software/ace-software.html>`
- AD7606B or AD7606C ACE plugin — downloadable from within ACE through the
  plug-in manager section
- A MATLAB or Python environment

ACE Environment
---------------

Refer to the
:adi:`AD7606C Evaluation Board user guide
<media/en/technical-documentation/user-guides/eval-ad7606c-fmcz-ug-1870.pdf>`
for instructions on powering the board and setting up the ACE plugin. Ensure
the plugin is functional and the device responds to plugin interaction before
proceeding.

Setting up Communication with ACE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Open ACE, then go to **Settings**.
- Go to the **IPC Server** tab and ensure that it is enabled and a port is
  allocated.

.. image:: images/ace_ipc_server_settings.png
   :align: center

Recording Macros
----------------

Start recording macros as explained on the `Recording a macro
<https://wiki.analog.com/software-tools/ace/recording-macros>`_ page.

Editing Macros in MATLAB
-------------------------

The code generated in the previous section can be imported into MATLAB and
used to set the exact configuration loaded during macro recording. To give
ACE an extra layer of flexibility, the ``execute_macro`` function can be
edited to perform repetitive tasks. For example, an 'AD7606C configuration'
macro can be easily recorded with the macro recording tool to fully configure
the AD7606C device: mode, range, OSR, reference, data interface, throughput,
etc.

.. image:: images/ace_execute_macro.jpg
   :align: center
   :width: 400

In order to automate operations:

- Each of the parameters used (strings) can be replaced by variables managed
  in the main code. These variables would then be input parameters to the
  function, along with ``Client``.
- Several macros can be recorded, each used as a function. The
  ``execute_macro`` function can be renamed to a more intuitive name.

Explore each of the following MATLAB scripts to see different functions
created to automate tests, e.g.: ``configure_ad7606c()``, ``run_capture()``,
``get_config()``, etc.

.. TODO: uncomment when ad7606x-matlab-example-code.zip is available
.. MATLAB Examples
.. ---------------
..
.. .. important::
..
..    Copyright © 2020 by Analog Devices, Inc. All rights reserved. This
..    software is proprietary to Analog Devices, Inc. and its licensors. This
..    software is provided on an "as is" basis without any representations,
..    warranties, guarantees or liability of any kind. Use of the software is
..    subject to the terms and conditions of the `Clear BSD License
..    <https://spdx.org/licenses/BSD-3-Clause-Clear.html>`_.
..
.. .. admonition:: Download
..    :class: download
..
..    `ad7606x-matlab-example-code.zip
..    <https://wiki.analog.com/_media/resources/tools-software/ace/ad7606x-matlab-example-code.zip>`_
..
.. The following variables are used across the different examples to define the
.. AD7606C configuration:
..
.. .. list-table::
..    :header-rows: 1
..    :widths: 25 75
..
..    * - Variable
..      - Description
..    * - ``generic``
..      - Either ``AD7606B``, ``AD7606C-18`` or ``AD7606C-16``, depending on
..        the hardware used
..    * - ``mode``
..      - ``True`` = Software mode; ``False`` = Hardware mode
..    * - ``range``
..      - ``range=3`` → ±10 V Single Ended Range (see register summary in
..        datasheet)
..    * - ``ref_sel``
..      - ``True`` = Internal Reference; ``False`` = External reference
..    * - ``par_serb``
..      - ``True`` = Parallel Interface; ``False`` = Serial Interface
..    * - ``throughput``
..      - Sample frequency in kSPS
..    * - ``no_samples``
..      - Number of samples in each dataset
..    * - ``OSR``
..      - Oversampling Ratio = 2\ :sup:`OSR`
..    * - ``sdo_lines``
..      - Number of SDO lines (serial interface only)
..    * - ``graph``
..      - Either ``'histogram'``, ``'waveform'``, or ``'FFT'``
..
.. Oversampling Benefits
.. ~~~~~~~~~~~~~~~~~~~~~
..
.. Oversampling increases noise performance at the expense of reduced throughput
.. rate. This can be seen through DC histograms. To validate the oversampling
.. feature:
..
.. - Tie the inputs Vx+ and Vx− together, to AGND.
.. - Start ACE and navigate to the **Analysis** tab.
.. - Store the ``OversamplingSweep.m`` file in your ``C:\`` drive.
.. - Open ``OversamplingSweep.m`` in MATLAB and run it.
..
.. The script runs through all possible oversampling ratios and shows the
.. histogram of codes for all channels.
..
.. .. image:: images/ace_ad7606_oversampling_histogram.png
..    :align: center
..    :width: 1000
..
.. .. warning::
..
..    This validation method is not valid for Unipolar single-ended ranges (0
..    to 5 V, 0 to 10 V, and 0 to 12.5 V) because tying the inputs to AGND may
..    saturate the ADC. Tie them to a DC level instead.
..
.. .. note::
..
..    To visualize a Waveform or FFT instead of the Histogram, modify the
..    script and assign the ``graph`` variable with either ``'waveform'`` or
..    ``'FFT'``. Make sure the correct columns are loaded after the
..    ``readtable`` function by exploring the .csv files.
..
.. Offset Calibration
.. ~~~~~~~~~~~~~~~~~~
..
.. AD7606B and AD7606C have on-chip offset calibration that eliminates any
.. offset caused externally, for example due to a mismatch in external
.. resistors.
..
.. .. image:: images/ace_ad7606_offset_cal_setup.png
..    :align: center
..    :width: 400
..
.. To validate offset calibration:
..
.. - Place the required external front-end resistors and/or caps (e.g. RC
..   filter).
.. - Tie the evaluation board inputs Vx+ and Vx− together, to AGND, or the
..   expected 0 V level.
.. - Start ACE and navigate to the **Analysis** tab.
.. - Store the ``OffsetCalibration.m`` file in your ``C:\`` drive.
.. - Open ``OffsetCalibration.m`` in MATLAB and run it.
..
.. The script displays the data gathered before and after offset calibration.
..
.. .. image:: images/ace_ad7606_offset_cal_histogram.png
..    :align: center
..    :width: 800
..
.. .. warning::
..
..    This validation method is not valid for Unipolar single-ended ranges (0
..    to 5 V, 0 to 10 V, and 0 to 12.5 V) because tying the inputs to AGND may
..    saturate the ADC. Tie them to a DC level instead.
..
.. .. note::
..
..    To visualize a Waveform or FFT instead of the Histogram, modify the
..    script and assign the ``graph`` variable with either ``'waveform'`` or
..    ``'FFT'``.
..
.. Gain Calibration
.. ~~~~~~~~~~~~~~~~
..
.. AD7606B and AD7606C have on-chip gain calibration that eliminates gain
.. errors caused by external resistors.
..
.. .. image:: images/ace_ad7606_gain_cal_setup.png
..    :align: center
..    :width: 400
..
.. To validate gain calibration:
..
.. - Place the required external front-end resistors and/or caps (e.g. RC
..   filter) on one channel.
.. - Connect a sine wave signal to the desired channel inputs Vx+ and Vx−.
.. - Start ACE and navigate to the **Analysis** tab.
.. - Store the ``GainCalibration.m`` file in your ``C:\`` drive.
.. - Open ``GainCalibration.m`` in MATLAB.
.. - Look up the ``ch_num`` variable and update it with the channel number that
..   has the external resistors.
.. - Look up the ``Rfilter`` variable and update it with the resistor value
..   used (in Ω).
.. - Run the script.
..
.. The script displays the data gathered before and after gain calibration. The
.. example below shows the same signal on two channels: CH1 has no resistors in
.. front of the AD7606C-16, while CH8 has a 10 kΩ resistor in front of both
.. V8+ and V8−. The two subplots show CH8 attenuated due to the external
.. resistor (left) and the ADC output after gain calibration. CH1 is shown for
.. reference.
..
.. .. image:: images/ace_ad7606_gain_cal_waveform.png
..    :align: center
..    :width: 1400
..
.. .. warning::
..
..    Gain calibration is not available for Unipolar single-ended ranges (0 to
..    5 V, 0 to 10 V, and 0 to 12.5 V).
..
.. Phase Calibration
.. ~~~~~~~~~~~~~~~~~
..
.. An RC filter affects not only gain but also phase, due to its time constant.
.. To validate the phase calibration feature:
..
.. - Place the required external RC filter on one channel.
.. - Connect a sine wave signal to the desired channel inputs Vx+ and Vx−, and
..   to at least one more channel without an RC filter.
.. - Start ACE and navigate to the **Analysis** tab.
.. - Store the ``PhaseCalibration.m`` file in your ``C:\`` drive.
.. - Open ``PhaseCalibration.m`` in MATLAB, look up the ``ch_num`` variable
..   and update it with the channel number that has the external RC filter.
.. - Run the script.
..
.. Open Circuit Detection
.. ~~~~~~~~~~~~~~~~~~~~~~
..
.. AD7606B and AD7606C have on-chip Open Circuit Detection, capable of
.. detecting a disconnected analog input signal. A resistor (RPD > 20 kΩ) in
.. parallel with the input source is required, as shown in the diagram:
..
.. .. image:: images/ace_ad7606_open_circuit_schematic.png
..    :align: center
..    :width: 400
..
.. There are two modes of operation: automatic and manual.
..
.. To validate **Automatic Open Circuit Detection**:
..
.. - *(Optional)* Place the required external RC filter through the provided
..   placeholders (check the board schematic).
.. - Populate the RPD resistor on one channel through the provided placeholders
..   (check the board schematic).
.. - Connect a sine wave or DC signal to the desired channel's Vx+ and Vx−
..   test points (or P8/P10 connectors).
.. - Start ACE and navigate to the **Analysis** tab.
.. - Store the ``OpenCircuitAutoMode.m`` file in your ``C:\`` drive.
.. - Open ``OpenCircuitAutoMode.m`` in MATLAB.
.. - Look up the ``ch_num`` and ``queue`` variables and update them with the
..   channel under test and a queue size greater than 5.
.. - Run the script.
..
.. The script continuously gathers and plots ADC data on the figure window
.. (overwriting each time). If the source signal is disconnected from the
.. board's input, the script stops and shows the last dataset. Observe how the
.. ADC output drops to near zero and MATLAB's Command Window displays:
..
.. *Channel Disconnected*
..
.. To verify **Manual Mode**, follow the same steps but run
.. ``OpenCircuitManualMode.m`` instead. After some time, disconnect the analog
.. input signal. When the ADC output code drops below a certain threshold (see
.. flowchart in the datasheet), the script changes the PGA common mode. If the
.. ADC output code varies, as shown in the graph below, the analog input has
.. been disconnected and the *Channel Disconnected* message appears.
..
.. .. image:: images/ace_ad7606_open_circuit_manual_triggered.png
..    :align: center
..    :width: 400
..
.. However, if the analog input signal amplitude is lowered below the threshold,
.. the script will still trigger. The PGA common mode will change, but the ADC
.. output remains unaltered. In that case the script determines the input was
.. not disconnected and continues running until the inputs are indeed
.. disconnected.
..
.. .. image:: images/ace_ad7606_open_circuit_manual_connected.png
..    :align: center
..    :width: 400
..
.. .. important::
..
..    Open Circuit Detection only works on bipolar input ranges and Vx− must
..    be tied to ground.

.. tip::

   Feel free to consult
   :ez:`Analog Devices Engineer-Zone <data_converters/precision_adcs>`
   for additional support.
