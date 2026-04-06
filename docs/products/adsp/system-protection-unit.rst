.. _adsp system-protection-unit:

System Protection Unit (SPU)
============================

Introduction
------------

This page describes the System Protection Unit (SPU) on ADSP-SC5xx platforms,
which is responsible for controlling access to shared system resources
(peripherals, DMA, memory, etc) by different system bus masters (ARM core,
SHARC cores, MDMA).

The information contained in this page is from the
:adi:`ADSP-SC5xx Hardware Reference Manual <media/en/dsp-documentation/processor-manuals/SC58x-2158x-hrm.pdf>`,
Chapter 43.

Overview
--------

The SPU protects a system from multiple bus masters from causing conflicts over
peripherals, and keeps access to system components fixed to particular bus
masters. It does this in 2 ways:

- Write-Protect access to certain Memory-Mapped Registers (MMRs) against
  selected bus masters.
- Global Lock Mechanism to simultaneously & dynamically protect many peripheral
  configuration registers.
- Exception Signal to indicate blocked accesses

In addition, a user can configure access protection for the SPU's own
write-protection registers.

The SPU is a critical configuration resource for systems which intend to
leverage peripherals via the SHARC cores. Proper configuration of the SPU
should generate an SPU exception when a core (Arm or SHARC) tries to access a
peripheral that has already been allocated to a different core.

Write-Protect Configuration
---------------------------

The configuration of the SPU's Write Protection roughly begins with setting the
Write Protect register corresponding to the peripheral to protect.

Each of these registers protects a particular peripheral from write accesses by
certain bus masters:

.. figure:: images/spu-wp-regs.jpg
   :align: center
   :alt: SPU Write Protect registers overview

   SPU Write Protect Registers [1]_

Access is prevented by system bus masters whose bitfields are masked in the
corresponding Write Protect register:

.. figure:: images/spu-wp-access.jpg
   :align: center
   :alt: SPU Write Protect access control

   SPU Write Protect Access Control [2]_

The Write Protect Registers are all formatted the same. Each register is
associated with a particular peripheral, and contains Write Protect Enable bits
corresponding to either Core Masters (CM) or System Masters (SM) such as
DMA, PCIe, or debug interfaces.

.. figure:: images/spu-wp-reg-n.jpg
   :align: center
   :alt: SPU Write Protect register format

   SPU_WP Register Format [3]_

These registers each have bitfields which correspond to system bus masters
which should be prevented from writing the peripheral.

.. table:: SPU_WP Core (CM) and System Master (SM) Bits
   :width: 100%
   :widths: auto
   :align: left

   +------------+----------+-----------------------------+
   | Bit Number | Bit Name | Description                 |
   +============+==========+=============================+
   | 0          | CM_WP[0] | ARM Core 0                  |
   +------------+----------+-----------------------------+
   | 1          | CM_WP[1] | SHARC Core 1                |
   +------------+----------+-----------------------------+
   | 2          | CM_WP[2] | SHARC Core 2                |
   +------------+----------+-----------------------------+
   | 15         | SM_WP[0] | PCIe                        |
   +------------+----------+-----------------------------+
   | 16         | SM_WP[1] | DBG                         |
   +------------+----------+-----------------------------+
   | 17         | SM_WP[2] | Embedded Trace Router (ETR) |
   +------------+----------+-----------------------------+
   | 18         | SM_WP[3] | Enhanced Bandwidth MDMA     |
   +------------+----------+-----------------------------+

Consult the SPU chapter of the
:adi:`Hardware Reference Manual <media/en/dsp-documentation/processor-manuals/SC58x-2158x-hrm.pdf>`
for the index of the WP registers corresponding to each peripheral.

Current Linux Support Status
----------------------------

Currently, the DSP Linux kernel has support instrumented within the various
peripheral drivers for the SPU.

The drivers call back to functions defined in
:git-linux:`arch/arm/mach-sc5xx/spu.c <adsp-6.12.0-y:arch/arm/mach-sc5xx/spu.c>`.

.. code-block:: c

   #include <linux/export.h>
   #include <linux/types.h>

   void set_spu_securep_msec(uint16_t n, bool msec)
   {
     (void)n;
     (void)msec;
   }
   EXPORT_SYMBOL(set_spu_securep_msec);

Currently, these functions are stubs which do not actually configure the SPU.
The ADI DSP Linux kernel and accompanying examples are designed with the intent
that the ARM core owns and allocates most of the system's peripherals.
The accompanying SHARC examples leverage peripherals minimally to prevent
contention with the ARM for system resources.

SPU support is currently being worked on as an addition to the ADSP Linux kernel
(`PR #3133 <https://github.com/analogdevicesinc/linux/issues/3133>`_).
Systems where SHARC cores boot their own applications prior to Linux/ARM will
not be supported due to contention with Linux for system resources
(peripherals, interrupts, DMA, shared L2 memory, etc.). For these systems,
system resources must be carefully managed by the developer to avoid conflicts
with the understanding that Linux/ARM will own the SPU configuration
and all system resources allocated in the devicetree.

References
----------

.. [1]
   ADSP-SC5xx Hardware Reference Manual, Chapter 43, Figure 43-1 (SPU Write Protect Registers),
   Analog Devices, Inc. https://www.analog.com/media/en/dsp-documentation/processor-manuals/SC58x-2158x-hrm.pdf

.. [2]
   ADSP-SC5xx Hardware Reference Manual, Chapter 43, Figure 43-2 (SPU Write Protect Access Control),
   Analog Devices, Inc. https://www.analog.com/media/en/dsp-documentation/processor-manuals/SC58x-2158x-hrm.pdf

.. [3]
   ADSP-SC5xx Hardware Reference Manual, Chapter 43, Figure 43-3 (SPU_WP Register Format),
   Analog Devices, Inc. https://www.analog.com/media/en/dsp-documentation/processor-manuals/SC58x-2158x-hrm.pdf
