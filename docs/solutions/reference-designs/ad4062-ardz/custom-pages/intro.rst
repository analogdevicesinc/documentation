:orphan: 

Introduction
============

Welcome to the documentation for the :adi:`AD4060` and :adi:`AD4062` precision
analog-to-digital converters (ADCs) and their evaluation ecosystem. This guide
provides complete information on hardware evaluation, firmware development,
Linux kernel integration, and FPGA design for these advanced 2 MSPS SAR ADCs
with I3C digital interface.

About the AD4060 and AD4062
---------------------------

The :adi:`AD4060` and :adi:`AD4062` are compact, low-power successive
approximation register (SAR) analog-to-digital converters featuring an I3C
digital interface. These devices are part of Analog Devices' Easy Drive SAR ADC
family, designed to simplify precision measurement applications while minimizing
power consumption.

**What is I3C?**

I3C (Improved Inter-Integrated Circuit) is a modern serial communication
protocol that combines the simplicity of I²C with the speed of SPI. Key
advantages include:

* **Lower pin count:** Only 2 wires (SDA and SCL) for communication
* **Higher throughput:** Up to 12.5 MHz data rate
* **Multi-device support:** Multiple devices on a single bus with dynamic addressing
* **In-Band Interrupts (IBI):** Devices can signal the host without dedicated interrupt lines
* **Hot-join:** Devices can be added to the bus during operation
* **Backwards compatibility:** Can coexist with legacy I²C devices

For the AD4060/AD4062, I3C enables efficient data acquisition while minimizing
board complexity and power consumption.

Evaluation Ecosystem
--------------------

This documentation covers the complete evaluation ecosystem for the AD4060 and
AD4062:

**Hardware:**

* **EVAL-AD4060-ARDZ / EVAL-AD4062-ARDZ** - Arduino Uno Shield-compatible
  evaluation boards with on-board signal conditioning, voltage reference, and
  power management
* **Supported carriers:**

  - STM32 Nucleo boards (NUCLEO-H503RB, NUCLEO-H563ZI) for bare-metal evaluation
  - AMD Xilinx Zynq-7000 SoC (Cora Z7S) for Linux evaluation
  - Intel Cyclone V SoC (DE10-Nano) for Linux evaluation

**Firmware:**

* **no-OS (bare-metal):** Portable C drivers and example projects for
  microcontrollers, with TinyIIO support for remote control via libiio
* **Linux kernel:** Full-featured IIO driver with support for triggers, events,
  buffered acquisition, and GPIO control

**FPGA Design:**

* **HDL project:** Reference design implementing I3C controller with DMA support
  for high-throughput data acquisition on Zynq-7000 and Cyclone V SoCs

**Software Tools:**

* **libiio:** Cross-platform library for interfacing with IIO devices
* **IIO Oscilloscope:** GUI application for waveform visualization and analysis
* **Scopy:** Advanced signal analysis and debugging tool
* **pyadi-iio:** Python bindings for rapid prototyping and automation

Target Audience
---------------

This documentation is designed for:

* **System designers** evaluating the AD4060/AD4062 for precision measurement applications
* **Firmware engineers** developing bare-metal applications on microcontrollers
* **Linux developers** integrating the devices into embedded Linux systems
* **FPGA designers** implementing custom I3C interfaces or modifying the reference design
* **Application engineers** using the evaluation boards for rapid prototyping

How to Use This Documentation
------------------------------

This guide is organized into distinct sections that can be read independently
or sequentially:

1. **Evaluation Board** - Start here if you've just received the hardware and
   want to get up and running quickly. Covers hardware setup, firmware flashing,
   and basic usage with GUI tools.

2. **Linux IIO Driver** - For embedded Linux developers. Describes the kernel
   driver architecture, devicetree configuration, and all supported features
   including buffered acquisition, events, and GPIO control.

3. **no-OS Driver and Projects** - For bare-metal firmware developers. Explains
   the driver API, TinyIIO layer, and example projects for STM32 platforms.

4. **HDL Design** - For FPGA developers. Documents the I3C controller
   implementation, AXI interfaces, and integration with the Analog Devices
   HDL framework.

5. **Software Tools** - Reference guide for libiio command-line tools and
   usage examples.

**Recommended Reading Paths:**

* **Quick evaluation:** Read sections 1 and 5 to evaluate using pre-built
  firmware and GUI tools
* **Linux integration:** Read sections 1, 2, 4, and 5 for complete Linux
  integration
* **Bare-metal development:** Read sections 1, 3, and 5 for microcontroller
  implementation
* **Custom FPGA design:** Read all sections for complete system understanding

Getting Help
------------

For technical questions and support:

* **Product pages:** :adi:`AD4060`, :adi:`AD4062`
* **Evaluation boards:** :adi:`EVAL-AD4060-ARDZ`, :adi:`EVAL-AD4062-ARDZ`
* **Support community:** :ez:`EngineerZone <reference-designs>`
* **Datasheets:**
  :adi:`AD4060 datasheet <media/en/technical-documentation/data-sheets/ad4060.pdf>`,
  :adi:`AD4062 datasheet <media/en/technical-documentation/data-sheets/ad4062.pdf>`
