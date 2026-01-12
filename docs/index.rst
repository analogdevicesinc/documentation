System Level Documentation
==========================

.. attention::

   Work-in-progress, not all content available at the
   `wiki <https://wiki.analog.com/resources/eval/user-guides/>`_
   has been imported yet.

Welcome to Analog Devices' System Level Documentation, your comprehensive resource
for prototyping and development with ADI products. This documentation provides
a complete ecosystem of hardware, HDL reference designs, software drivers,
libraries, and applications to accelerate your path from concept to production.

The Ecosystem Approach
-------------------------------------------------------------------------------

ADI takes an **ecosystem approach** to development, providing all the building
blocks you need at every layer of the stack:

- **Hardware** - Best-in-class ADCs, DACs, transceivers, sensors, and signal chain components
- **HDL** - FPGA reference designs and reusable IP cores (JESD204, SPI Engine, DMA)
- **Drivers** - Linux IIO kernel drivers and bare-metal firmware for microcontrollers
- **Libraries** - Hardware abstraction (libiio) with multiple backends (local, network, USB, serial)
- **Language Bindings** - Python (pyadi-iio), MATLAB, and C/C++ interfaces
- **Applications** - GUI tools (Scopy, IIO Oscilloscope) and complete Linux distributions (Kuiper Linux)

Rather than reinventing the wheel, we integrate with established open-source
ecosystems like the Linux kernel, Python scientific computing, and MATLAB,
allowing you to focus on your application while relying on proven infrastructure.

**New to the ecosystem?** Start with the :doc:`Ecosystem Overview </overview/index>`
to understand how all the pieces fit together, or jump directly to a
:doc:`workflow example </overview/workflows>` that matches your use case.

What You'll Find Here
-------------------------------------------------------------------------------

This documentation covers everything from individual device drivers to complete
reference designs, organized to help you find what you need quickly. Whether
you're building a high-speed FPGA-based data acquisition system, a low-power
embedded sensor, or a Raspberry Pi prototyping platform, we have the resources
to get you started.

Contents
-------------------------------------------------------------------------------

.. toctree::
   :caption: Ecosystem Overview
   :maxdepth: 2

   overview/index

.. toctree::
   :caption: Product Categories
   :maxdepth: 2
   :glob:

   products/*/index

.. toctree::
   :caption: Kuiper & Linux Kernel
   :maxdepth: 2
   :glob:

   linux/*/index

.. toctree::
   :caption: Software
   :maxdepth: 1
   :glob:

   software/*/index

.. toctree::
   :caption: Devices
   :maxdepth: 2
   :glob:

   tools/*/index

.. toctree::
   :caption: Apps & Solutions
   :maxdepth: 4
   :glob:

   solutions/*/index

.. toctree::
   :caption: University Program
   :maxdepth: 4

   university/index

.. toctree::
   :caption: Learning
   :maxdepth: 4

   learning/index

.. toctree::
   :caption: Contributing and Guidelines
   :maxdepth: 4
   :glob:

   contributing/*

