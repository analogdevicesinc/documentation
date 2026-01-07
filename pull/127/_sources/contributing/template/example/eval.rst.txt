:orphan:

.. _template eval:

EVAL-XXX-XXX
============
.. Add an image and the overview description of the board.

.. image:: placeholder.svg
   :align: right

The :adi:`EVAL-AD4050-ARDZ` and :adi:`EVAL-AD4052-ARDZ` evaluation boards enable
quick and easy evaluation of the performance and features of the
:adi:`AD4050` or the :adi:`AD4052`, respectively [CONTINUE]...

Overview
--------
.. This section outlines the key points of the evaluation board, aiding the user
   in choosing an appropriate solution (bare-metal, Linux, FPGA, soft core, etc.).

This section provides a general overview on the evaluation board, all supported
carriers, firmware and software.

The following carriers are supported, followed by the target firmware:

.. list-table::

   * - Carrier
     - no-OS
     - Linux
   * - NUCLEO-ABC
     - ✓
     -
   * - Cora Z7S
     -
     - ✓
   * - DE10-Nano
     -
     - ✓
   * - SDP-K1 [#]_
     - ✓
     -

.. [#] Some informative footnote.

Features
~~~~~~~~
..
   Quick features overview for users (don't dive deep on details yet).

* Full featured evaluation boards for the :adi:`AD4050` and :adi:`AD4052` with
  a USB power solution.
* Single differential channel and common-mode input available through SMA
  connectors.
* PC software (ACE plugin/:ref:`iio-oscilloscope`) for control and data analysis
  of the time and frequency domains.
* Compatible with other Arduino form factor controller boards.

Evaluation board kit contents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
..
   What comes on the box?

* EVAL-AD4050-ARDZ/EVAL-AD4052-ARDZ evaluation board.

Equipment needed
~~~~~~~~~~~~~~~~~
..
   Overview of the required equipment, generic to all carriers.

* Host PC.
* One of the supported carriers.
* Precision signal source with SMA cable.

Hardware
~~~~~~~~
..
   Overview of the hardware, generic to all carries.

The evaluation board is connected to the Arduino Uno compatible headers of the
carrier.

When powering from the carrier, ensure the JP2 jumper is to the +5V position and
power on the carrier board.

When powering from an external power supply, ensure the JP2 jumper is set to the
VIN position, power on the carrier board, and provide power to VIN
(according to the carrier board user guide).

For more information about hardware specifications, see the
:adi:`EVAL-AD4050-ARDZ`/:adi:`EVAL-AD4052-ARDZ`
evaluation board pages, in particular, the user guide
and design support files.

User Guide
----------

.. This section contains all guides aimed at users.
   Start with the most plug-and-play solution, then gradually delve deeper into
   the technical aspects. Additionally, link to generic tutorials and pages,
   such as the :ref:`libiio`.

   Below is a hardcoded/dummy rendered toctree for illustrative purposes. In your doc, however, use a toctree like:

   .. toctree:
      :titlesonly:
      :glob:

      user/*

   Note: if you store the files in the `eval` folder or some subfolder like
   "users" above depends on the complexity of the eval.
   If the part(s) under evaluation are simple enough and there isn't content for
   additional pages, you shall include the guide here directly, without creating
   a new file.

* Introduction to the hardware
* Quick start on no-OS Systems
* Quick start on Linux Systems
* Customizing

Developer Overview
------------------
..
   This section should contain all the technical details that a developer may
   want to know.
   Start summarizing all the source code that exist, linking to the proper
   documentation.
   Do not copy-and-paste/duplicate content, if the information already
   exists in the HDL doc, do not add the same information here.
   And if some no-OS driver information is missing from the part no-OS driver
   page, add there instead.

This chapter summarizes all source code and related documentation of the
evaluation board.

To work with the source code, you should have prior knowledge on software
development and HDL design (for the FPGA).
We provide pointers to introductory guides, although their scope is limited to
topics that particularly relate to our codebase and do not replace the full
documentation of the tools used.

Drivers
~~~~~~~

The drivers source code are available at:

.. list-table::

   * - Firmware
     - Source code
     - Documentation
   * - no-OS
     - :git-no-OS:`drivers/adc/ad405x`
     - :external+no-OS:doc:`doc <drivers/adc/ad405x>`
   * - Linux
     - :git-linux:`staging/ad4052:drivers/iio/adc/ad4052.c`
     - :ref:`doc <linux ad4052>`

The no-OS driver is divided into a core driver and a tinyIIO layer to be used
with :ref:`libiio`.
The Linux driver is always exposed via the :ref:`iio`.

To get started with no-OS drivers, checkout :external+no-OS:doc:`drivers_guide`,
and for Linux drivers the :ref:`linux-kernel` page.

Projects
~~~~~~~~

The source code for baremetal projects can be found at:

.. list-table::

   * - Carrier
     - Firmware
     - Project
     - Documentation
   * - NUCLEO-H503RB
     - no-OS
     - :git-no-OS:`ad405x:projects/ad405x`
     - ``EXAMPLE :external+no-OS:doc:`docs <projects/ad405x>```
   * - NUCLEO-H563ZI
     - no-OS
     - :git-no-OS:`ad405x:projects/ad405x`
     - ``EXAMPLE :external+no-OS:doc:`docs <projects/ad405x>```
   * - SDP-K1
     - precision-converters-firmware
     - :git-precision-converters-firmware:`projects/ad405x_iio`
     - :external+precision-converters-firmware:doc:`docs <source/projects/ad405x_iio/ad405x_iio>`
   * - CoraZ7S
     - Linux
     - \-
     - \-
   * - DE10-Nano
     - Linux
     - \-
     - \-

For the no-OS project, the basic examples use only the core driver, while the
iio example uses the tinyIIO layer to expose the device to :ref:`libiio`.

The precision-converters-firmware project also expose the device to :ref:`libiio`,
differentiating only on the target carrier.

Since the Linux driver exposes the device via the :ref:`iio`, no project is
required to leverage the device on Linux targets
(CoraZ7S and DE10-Nano).

Follow :dokuwiki:`no-OS projects <resources/no-os/build>` and
:external+precision-converters-firmware:doc:`precision-converters-firmware projects <source/build/project_build>`
to comprehend the project structure for each.

Linux devicetrees
~~~~~~~~~~~~~~~~~

For the carriers targeting Linux, the devicetrees are available at:

.. list-table::

   * - Carrier
     - Devicetree
   * - Cora Z7S
     - :git-linux:`zynq-coraz7s-ad4052.dts <staging/ad4052:arch/arm/boot/dts/xilinx/zynq-coraz7s-ad4052.dts>`
   * - DE10-Nano
     - \-

HDL reference design
~~~~~~~~~~~~~~~~~~~~

The DE10-Nano and Cora Z7s use the FPGA to instantiate the controllers to
interface the evaluation board.

The source code is available at
:git-hdl:`ad4052:projects/ad4052_ardz`
and documented at
:external+hdl:ref:`ad4052_ardz`.

Get start with the HDL reference design reading the :external+hdl:ref:`user_guide`.

Software & Bindings
~~~~~~~~~~~~~~~~~~~

Using any IIO or TinyIIO driver layer, the device can be interacted through
:ref:`libiio`, language bindings on top of libiio and the :ref:`iio-oscilloscope`
GUI.

For the Python language a class abstraction of the device is available at
:git-pyadi-iio:`adi/ad405x.py`
(:external+pyadi-iio:doc:`class doc <devices/adi.ad405x>`),
with an example at
:git-pyadi-iio:`examples/ad4052_example.py`

Developer Guide
---------------

.. This section is similar to the User Guides, but focused on developers!

   If there are no guides, you can remove this section and rename
   the previous from "Developers Overview" to just "Developer".

   Analogous to before, below is a hardcoded/fake rendered toctree for illustrative purposes.
   In your doc, however, use a toctree like:

   .. toctree:
      :titlesonly:
      :glob:

      devs/*

* Schematics
* Detailed performance
* Changing modes during runtime

Help and Support
----------------
..
   This is the most generic section, but you can still add help/support
   information related to your particular eval.

For questions and more information, please visit the
:ez:`EngineerZone Support Community <reference-designs>`.

.. esd-warning::
