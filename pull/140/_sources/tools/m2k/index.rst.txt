.. _m2k:

ADALM2000
=========

.. toctree::
   :hidden:
   :glob:

   */index
   *

The :adi:`ADALM2000` (M2K) Active Learning Module is an affordable
USB-powered data acquisition module that takes the capabilities of the
:adi:`ADALM1000` (M1K) Active Learning Module to the next level.
With 12-bit ADCs (at 100MSPS) and DACs (at 150MSPS), the ADALM2000 with the
:dokuwiki:`Scopy </m2k/scopy>` software, brings the power of high performance lab
equipment to the palm of your hand, enabling electrical engineering students and
hobbyists to explore signals and systems into the tens of MHz without the cost
and bulk associated with traditional lab gear. The ADALM2000, when coupled with
Analog Devices' :external+scopy:doc:`Scopy <index>` graphical application
software running on a computer, provides the user with the following high
performance instrumentation:

-  Two-channel oscilloscope with differential inputs
-  Two-channel arbitrary function generator
-  16-channel digital logic analyzer (3.3V CMOS and 1.8V or 5V tolerant,
   100MS/s)
-  16-channel pattern generator (3.3V CMOS, 100MS/s)
-  16-channel virtual digital I/O
-  Two input/output digital trigger signals for linking multiple instruments
   (3.3V CMOS)
-  Two-channel voltmeter (AC, DC, ±25V)
-  Network analyzer – Bode, Nyquist, Nichols transfer diagrams of a circuit.
   Range: 1Hz to 10MHz
-  Spectrum Analyzer – power spectrum and spectral measurements (noise floor,
   SFDR, SNR, THD, etc.)
-  Digital Bus Analyzers (SPI, I²C, UART, Parallel)
-  Two programmable power supplies (0…+5V , 0…-5V)

Introduction
------------

ADALM2000 is a portable lab. It's more than the combinations of a few parts, but
to understand the capabilities of the unit, you must understand the fundamental
operation of each part inside the unit. Depending on who you are, and what you
want to do, you may have different needs, and different wants. It's expected
that many people will stop when they solve their immediate problem and don't
want to go any deeper into the stack. There are 3 main categories of users:

#. :ref:`ADALM2000 Users & Students <m2k users>`:

   -  ADALM2000 users normally interact with real world analog signals using
      :external+scopy:doc:`Scopy <index>` or
      :dokuwiki:`Alice </university/tools/m2k/alice/users-guide-m2k>`
   -  Everyone should read this section, as it describes the device, and
      describes how to get the drivers and host software installed properly.

#. ADALM2000 Application Developers:

   -  Want to write their application interface for the ADALM2000 to run on the
      PC, but do not need to modify the ADALM2000 firmware or need to know the
      details on the ADALM2000's inner workings
   -  Use :dokuwiki:`scopy's scripting ability </m2k/scopy/scripting-guide>`.
      Write scripts in javascript and then call scopy via the command line.
   -  Use :ref:`libm2k` to write
      C++/C#/Python applications that capture and generate data from the host
      PC.

#. :ref:`ADALM2000 Firmware Developers <m2k devs>`:

   -  normally write custom software or HDL (for the FPGA) that run directly on
      the ADALM2000 device. This may put the ADALM2000 in different modes, and
      support different external USB devices (including LAN (via USB), or WiFi
      (vs USB)), extending the capabilities of the device. This includes all the
      information to compile HDL projects, compile kernels, change to custom USB
      PID/VID and/or run custom user space applications.

It's expected that most people will work their way down through each section,
reading and skimming most of the content. The content is in a constant state of
improvement, so if you do have a question, please ask at
:ez:`EngineerZone <community/university-program>`,
or check the :ref:`help and support <m2k help_support>` page.

.. esd-warning::
