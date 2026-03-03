Software Configuration and Setup
=================================

This section provides guidance on configuring and running the software
components of the High-Performance Analog Meets AI demonstration.

Overview
--------

The demonstration consists of two main software components:

1. **Holoscan Modulation Classification Application** - A real-time AI-powered
   modulation classification system built with NVIDIA Holoscan SDK
2. **Data Visualization Dashboard** - A Python-based Dash application for
   monitoring and analyzing classification results

Holoscan Modulation Classification Application
----------------------------------------------

Description
~~~~~~~~~~~

This application performs real-time modulation classification on incoming data
using MATLAB-generated CUDA code. It processes signals from ADRV9009 devices and
classifies them into one of eight modulation schemes:

- BPSK (Binary Phase Shift Keying)
- QPSK (Quadrature Phase Shift Keying)
- 8PSK (8-Phase Shift Keying)
- 16QAM (16-Quadrature Amplitude Modulation)
- 64QAM (64-Quadrature Amplitude Modulation)
- PAM4 (4-Pulse Amplitude Modulation)
- GFSK (Gaussian Frequency Shift Keying)
- CPFSK (Continuous Phase Frequency Shift Keying)

Key Components
~~~~~~~~~~~~~~

**Holohub application**: The Holohub application and IIO operators
   - Example applications:
     https://github.com/nvidia-holoscan/holohub/tree/main/applications/iio
   - Generic operators:
     https://github.com/nvidia-holoscan/holohub/tree/main/operators/iio_controller

There are 5 operators (each with its own Python binding) that can read/write IIO
attributes, read/write IIO buffers and configure the initial setup for a
device/system. This demonstration uses the buffer read operator in order to read
from the 2 ADRV9009 devices. After that, the matlab module (that needs to be
compiled beforehand) will call the classification function that returns the
modulation and confidence level. This will be printed to the output file from
where the python dash app will read and display the information.

Configuration
~~~~~~~~~~~~~

1. **Network Configuration**

   Update IP addresses in main.cpp for your ADRV9009 devices:

   .. code-block:: cpp

      // Configure IIO buffer read for Talise device at IP 10.43.1.10 auto
      iio_rx_1 = make_operator<ops::IIOBufferRead>("iio_rx_1",
                                        Arg("ctx") =
                                        std::string("ip:10.43.1.10"), Arg("dev")
                                        = std::string("axi-adrv9009-rx-hpc"), //
                                        ... other parameters

2. **Output Configuration**

   Modify the YAML file to set output file paths:

   .. code-block:: yaml

      matlab:
        out_file: "modulation_results.txt"

3. **Channel Configuration**

   The application is configured for 8 channels (4 I/Q pairs):

   .. code-block:: cpp

      std::vector<std::string> channel_names = {
          "voltage0_i", "voltage0_q", "voltage1_i", "voltage1_q", "voltage2_i",
          "voltage2_q", "voltage3_i", "voltage3_q"
      };

Building and Running
~~~~~~~~~~~~~~~~~~~~

1. **Build the Application**

   .. shell::

      ~/holohub $build iio

2. **Run the Application**

   .. shell::

      ~/holohub $run iio

The application will:

- Connect to the specified ADRV9009 devices
- Continuously read data samples (8192 samples per buffer, but it is
  configurable from the code)
- Process data through the MATLAB classification model
- Output results to ``modulation_results.txt`` and ``modulation_results1.txt``

Data Visualization Dashboard
----------------------------

Location
~~~~~~~~

The visualization script is located at:
:git-pyadi-iio:`raw+afpop:jupiter_modulation/examples/plot_identification_data.py`

Description
~~~~~~~~~~~

This Python application provides a web-based dashboard for monitoring and
analyzing the modulation classification results in real-time. It features:

- Real-time confusion matrices
- Constellation diagrams
- Time-domain waveform plots
- Classification accuracy metrics
- Interactive modulation selection

Key Features
~~~~~~~~~~~~

**Real-time Monitoring**
   - Reads results from Holoscan output files every 3 seconds
   - Updates visualizations dynamically
   - Tracks classification performance over time

**Modulation Control**
   - Manual modulation selection or automatic random switching
   - Real-time transmission to connected SDR devices
   - Supports all 8 modulation schemes

**Signal Visualization**
   - Constellation diagrams showing I/Q relationships
   - Time-domain waveforms (I and Q components)
   - Interactive plots with hover information

Prerequisites
~~~~~~~~~~~~~

Install required Python packages:

.. shell::

   $pip3 install dash plotly pandas scipy scikit-learn numpy pyadi-iio

Hardware Requirements
~~~~~~~~~~~~~~~~~~~~~

The dashboard expects the following hardware setup:

- **4 ADRV9002 devices** for signal transmission (IPs: 192.168.0.15-18)
- **2 ADRV9009ZU11eg devices** for signal reception (configured in Holoscan app)
- **Modulated data files** in ``modulated_data/`` directory

Configuration
~~~~~~~~~~~~~

1. **File Paths**

   Update file paths to match your Holoscan output location:

   .. code-block:: python

      file_path =
      '/home/analog/git/holohub/build/matlab_classify_modulator/modulation_results.txt'
      file_path1 =
      '/home/analog/git/holohub/build/matlab_classify_modulator/modulation_results1.txt'

2. **SDR Configuration**

   Configure SDR devices with appropriate IP addresses and stream profiles:

   .. code-block:: python

      sdr = adi.adrv9002(uri="ip:192.168.0.15")
      sdr.write_stream_profile("lte_40_lvds_api_68_14_10.stream",
      "lte_40_lvds_api_68_14_10.json")

3. **Modulated Data**

   Ensure modulated data files are available in the ``modulated_data/``
   directory:

   - mod_BPSK.mat
   - mod_QPSK.mat
   - mod_8PSK.mat
   - mod_16QAM.mat
   - mod_64QAM.mat
   - mod_PAM4.mat
   - mod_GFSK.mat
   - mod_CPFSK.mat

Running the Dashboard
~~~~~~~~~~~~~~~~~~~~~

1. **Start the Holoscan Application**

   Ensure the Holoscan modulation classification application is running and
   generating output files.

2. **Launch the Dashboard**

   .. shell::

      $python3 plot_identification_data.py

3. **Access the Web Interface**

   Open a web browser and navigate to ``http://localhost:8050``

Usage Workflow
~~~~~~~~~~~~~~

1. **Select Modulation**: Use the dropdown to choose a specific modulation or
   select "Random" for automatic switching
2. **Monitor Classification**: Observe real-time classification results for both
   ADRV9009 devices
3. **Analyze Performance**: Review confusion matrices and accuracy metrics
4. **Examine Signals**: Study constellation diagrams and time-domain waveforms

Support and Resources
---------------------

For additional support and documentation:

- **Holoscan SDK Documentation**: https://docs.nvidia.com/holoscan/
- **PyADI-IIO Documentation**: :external+pyadi-iio:doc:`index`
