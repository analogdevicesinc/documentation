Filament - Unified DSP/AI Data Extraction Platform
==================================================

Overview
--------

.. figure:: general-diagram.png
   :align: center

   Filament Platform Overview

Filament is a multimarket software and hardware platform developed by Analog Devices
to enable DSP/AI capabilities with ADI data converters. It provides a unified programming interface
for building portable, scalable, and efficient DSP/AI pipelines across various industries such as:

- Communications
- Medical
- Automation
- Electronic Test and Measurement

Key Features
------------

- Unified access to ADI data converters
- Scalable architecture for edge AI workloads
- Software-defined features and applications
- High-speed data interfaces (JESD204x, Ethernet, PCIe, USB)
- GPU/CPU acceleration for DSP/AI processing
- Cloud and PC connectivity

System Architecture
-------------------

.. figure:: software-architecture.png
   :align: center

   Filament System Architecture

The Filament platform is composed of the following layers:

**Hardware Components**

- MxFE (Mixed-Signal Front End): AD9986 (4Tx, 2Rx)
- DADI (Data Adaptation Digital Interface): Based on Stratix 10 FPGA
- GPU: e.g., NVIDIA RTX A6000
- Client PC: Windows-based GUI for control and analysis

**Software Stack**

.. figure:: unified-sw-stack.png
   :align: center

   Filament Software Stack

- Control Plane: Manages configuration and communication with converters via SPI/I2C
- Data Plane: Handles high-speed data extraction and processing (e.g., JESD to Ethernet conversion)
- Algorithm Library: Includes DDC, DUC, PSD, EVM, AI/ML modules
- GUI & APIs: C++, CUDA, Python interfaces for application development

Use Case: 5G VSA/VSG
---------------------

Vector Signal Generator (VSG)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Custom signals are generated on the GPU and transmitted via DAC in real-time.

Vector Signal Analyzer (VSA)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: vsa-setup.png
   :align: center

   VSA Setup Diagram

- Full DSP chain implemented on GPU for high-speed parallel processing:
  - Phase Tracking
  - Frame Sync
  - DDC + Decimation
  - Channel Estimation
  - Equalization
  - EVM Calculation

Demonstration Setups
---------------------

Case I: External Signal Source
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Uses Agilent MXG N5182A VSG to feed signal into ADC.

.. figure:: 5g-source.png

- EVM and spectral analysis performed on Windows PC.

Case II: DAC-to-ADC Loopback
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Demonstrates internal signal generation and loopback.
- Achieves high EVM performance (e.g., -49.4 dB).

Hardware Blocks
---------------

**Block 1: MxFE**

- AD9986 (4Tx, 2Rx)
- DAC0 to ADC1 loopback (Case II)
- External feed from MXG to ADC0 (Case I)

.. figure:: MxFE.png

**Block 2: DADI**

- Stratix 10 FPGA
- Optical Ethernet port to GPU NIC
- Supports up to 100 Gbps × 2 lanes

.. figure:: block2.png

**Block 3: GPU**

- Receives JESD data via Ethernet
- Executes DSP/AI workloads

.. figure:: block3.png

**Block 4: Windows PC**

- GUI for visualization and analysis
- Displays EVM results for both cases

.. figure:: block4.png

Getting Started
------------------

1. Connect Hardware: MxFE, DADI, GPU, and Client PC
2. Install Software: ADI SDK, GUI, and required drivers
3. Configure Use Case: Select VSA or VSG mode
4. Run Analysis: Use GUI to visualize EVM, spectrum, and constellation

Performance Highlights
----------------------

- Optical Ethernet supports up to 100 Gbps × 2 lanes
- GPU acceleration enables real-time DSP/AI workloads
- EVM performance:

  - Case I: ~-43.1 dB
  - Case II: ~-49.4 dB

Benefits
--------

- Faster development and time-to-market
- Hardware reuse and scalability
- Compact system design (no USB adapters needed)
- Easy integration of new applications and algorithms

Troubleshooting Tips
--------------------

- Ensure all firmware and drivers are up to date.
- Verify JESD synchronization and Ethernet link status.
- Use diagnostic tools in the GUI for signal integrity checks.

Additional Resources
--------------------

- ADI SDK Documentation
- JESD204x Interface Guides
- GPU Programming APIs (CUDA, Python)
