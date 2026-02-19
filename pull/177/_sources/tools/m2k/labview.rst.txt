.. _m2k labview:

Using With LabVIEW
""""""""""""""""""

The ADALM2000 (M2K) can be controlled in LabVIEW. Controlling M2K is provided
through a set of bindings for libm2k.

The C++ API reference is available on
`here <https://analogdevicesinc.github.io/libm2k/index.html>`__.

The LabVIEW VI documentation is available on
`here <https://analogdevicesinc.github.io/libm2k-labview/index.html>`__.

Releases
========

Always use the latest release VI Package from the
:git-libm2k-labview:`releases/latest+`.

Installing
==========

The first step is to install libm2k using the Windows system installer. Go to
:git-libm2k:`libm2k release page <releases/latest+>` or use
the `nightly builds <https://ci.appveyor.com/project/analogdevicesinc/libm2k>`__.

The LabVIEW wrapper is available only starting from official version v0.4.0.

In the libm2k system installer, check the "Install wrapper for LabVIEW bindings"
box. The base library and the wrapper will be installed in your system.

Download the latest ADALM2000 VI Package from the Release section on the
following page:
:git-libm2k-labview:`ADALM2000 LabVIEW repository </>`.
Load the VIP package in the VI Package Manager, install the package.
After that, there will be a new palette, named Analog Devices -> ADALM2000,
in LabVIEW.

Windows Support
---------------

After checking the "Install wrapper for LabVIEW bindings" box, the system
installer will install libm2k.dll and libm2k_lv.dll in your Windows system.
If libm2k_lv does not appear in the system path, the LabVIEW bindings will
not find the exposed methods and will not work.

In the VI Package Manager, you should load the .vip package and then install
it.

.. image:: install-vipackage.png

.. note::

   The VI Package was tested on version 2015 and 2020 of LabVIEW on
   Windows.

.. note::

   As this is still under development, bugs might arise.

.. note::

   Not every libm2k method is supported yet, but may be added
   in the future.

Support
=======

For support questions please post them on EngineerZone under the
:ez:`Virtual Classroom Forum <adieducation/university-program>`.

If you find any bugs please report them on the
:git-libm2k:`libm2k issues tracker <issues+>`.

Examples and LabVIEW palette
============================

The ADALM2000 palette can be found under the "Analog Devices" category.

.. image:: pallette-preview.png

This contains the following subpalettes:

- **AnalogIn** - VIs for ADC control
- **AnalogOut** - VIs for DAC control
- **Digital** - VIs for the Digital pins control
- **Power Supply** - Vis for the ADALM2000 power supplies
- **Examples** - A few examples on how the VIs can be used.

And the following VIs:

- **Close.vi** - Will destroy the currently open libm2k context
- **Instrument Handler.vi** - Will create a libm2k context
- **Search ADALM2000.vi** - Will search the currently available ADALM2000 and
  return a list of URIs.

