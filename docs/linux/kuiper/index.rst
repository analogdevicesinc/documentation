.. _kuiper:

Kuiper
======

.. note::

   This page provides an overview of Kuiper Linux within the ADI software
   ecosystem. For complete build instructions, configuration options, and
   detailed guides, see the
   :external+adi-kuiper-gen:doc:`the dedicated Kuiper documentation <index>`

Kuiper is a specialized Debian-based Linux distribution designed specifically
for Analog Devices hardware and evaluation boards. It provides a complete,
ready-to-use environment with ADI libraries, tools, and applications
pre-configured for seamless hardware integration.

Rather than manually installing and configuring individual ADI software
components, Kuiper delivers a cohesive development platform that eliminates
setup complexity and gets you running immediately.

Integration with ADI Software Ecosystem
----------------------------------------

Kuiper brings together the key components of ADI's software stack into a
single, optimized distribution:

**Core Libraries (Optional)**

- **LibIIO**: Hardware abstraction layer for IIO devices
- **PyADI-IIO**: Python interfaces for rapid prototyping and development
- **Libm2k**: ADALM2000 support for mixed-signal analysis

**Development Applications (Optional)**

- **IIO Oscilloscope**: Real-time data visualization and device control
- **Scopy**: Advanced signal analysis and generation platform
- **GNU Radio**: Software-defined radio development framework

**System Integration**

- Pre-configured boot files for Raspberry Pi, Xilinx, and Intel platforms
- Optimized ARM device configurations
- Desktop environment with VNC access (optional)

Build Configurations
--------------------

Kuiper offers flexible build configurations to match your specific needs:

**Basic Image**
   Essential system with boot files and core utilities. Perfect for headless
   applications and custom development.

**Full Image**
   Complete development environment with desktop, all ADI libraries, and
   development tools. Ideal for evaluation and comprehensive development work.

**Custom Image**
   Configurable combination of components tailored for production deployments
   or specialized applications.

Use Cases
---------

**Evaluation and Prototyping**
   Quick setup for testing ADI evaluation boards without manual configuration

**Software-Defined Radio Development**
   Pre-configured GNU Radio environment with ADI hardware support

**Educational Environments**
   Complete learning platform with all tools and examples ready to use

**Production Prototyping**
   Customizable base system for embedded applications

Getting Started
---------------

**Quick Start**
   Download pre-built images from
   :git-adi-kuiper-gen:`GitHub Actions <actions/workflows/kuiper2_0-build.yml+>`

**Custom Builds**
   Build your own configured image using
   :git-adi-kuiper-gen:`adi-kuiper-gen </>`

**Prerequisites**
   Ubuntu 22.04 + Docker for building custom images

Hardware Support
----------------

- **Raspberry Pi**: All models with ARM processors
- **Xilinx Zynq**: Development boards and custom designs
- **Intel/Altera**: FPGA development platforms
- **ADI Evaluation Boards**: ADALM-PLUTO, ADALM2000, FMComms series, and more

Resources
---------

- **Source Code**: :git-adi-kuiper-gen:`adi-kuiper-gen </>`
- **Pre-built Images**: :git-adi-kuiper-gen:`GitHub Actions
  <actions/workflows/kuiper2_0-build.yml+>`
- **Issues and Bug Reports**: :git-adi-kuiper-gen:`GitHub Issues <issues+>`
- **Community Discussion**: :ez:`Linux Software Drivers Forum
  <linux-software-drivers>`
