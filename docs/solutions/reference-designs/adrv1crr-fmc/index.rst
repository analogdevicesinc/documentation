.. imported from: https://wiki.analog.com/resources/eval/user-guides/pzsdr/carriers/fmc

.. _adrv1crr-fmc:

ADRV1CRR-FMC Carrier
======================

The :adi:`ADRV1CRR-FMC` is an FMC (FPGA Mezzanine Card) carrier board for the
PicoZed SDR System-On-Module (SOM) platform. It provides FMC connectivity along
with Ethernet, USB, HDMI, camera, SFP+, and PMOD interfaces for prototyping and
evaluation. The carrier is designed for use with the
:ref:`ADRV9361-Z7035 <adrv9361-z7035>` and :ref:`ADRV9364-Z7020 <adrv9364-z7020>`
RF SOMs.

Compatible SOMs
---------------

ADRV9361-Z7035
~~~~~~~~~~~~~~

The :ref:`ADRV9361-Z7035 <adrv9361-z7035>` is fully compatible with the FMC
carrier. All carrier functionality is supported, including Ethernet, USB, PMOD
interfaces, HDMI output, camera input, SFP+, FMC connector, push buttons, LEDs,
and slide switches.

ADRV9364-Z7020
~~~~~~~~~~~~~~

The :ref:`ADRV9364-Z7020 <adrv9364-z7020>` is partially compatible with the FMC
carrier. Due to the fewer available user I/Os on the Zynq XC7Z020, not all
carrier functionality is supported.

**Supported features:**

- Ethernet
- USB
- PMOD1 and PMOD_MIO
- Push buttons 1, 2, 3
- LED 0

**Unsupported features:**

- HDMI output
- Camera input
- PMOD0 (pins 0 and 1 are connected)
- SFP+
- LEDs 1, 2, 3
- Slide switches
- Push button 0
- FMC connector

.. note::

   For the ADRV9364-Z7020, the :ref:`ADRV1CRR-BOB <adrv1crr-bob>` breakout
   carrier is recommended instead.

External Reference Clock
-------------------------

.. figure:: pzsdr_ext_clk.png
   :align: center
   :width: 600

   External reference clock configuration via J1

An external reference clock can be supplied via the J1 connector on the carrier.
To switch the clock source, the
:git-linux:`zynq-adrv9361-z7035.dtsi <arch/arm/boot/dts/xilinx/zynq-adrv9361-z7035.dtsi>`
device tree file must be modified:

.. code-block:: dts

   clocks {
       xo_40mhz_fixed_clk: clock@0 {
           #clock-cells = <0>;
           compatible = "fixed-clock";
           clock-frequency = <40000000>; /* Set to external clock frequency */
           clock-output-names = "XO_40MHz";
       };

       ad9361_clkin: clock@1 {
           #clock-cells = <0>;
           compatible = "gpio-gate-clock";
           clocks = <&xo_40mhz_fixed_clk>;
           enable-gpios = <&gpio0 105 1>; /* 0 = onboard XO, 1 = external J1 */
           clock-output-names = "ad9361_ext_refclk";
       };
   };

Configuration steps:

#. Update the ``clock-frequency`` property with the exact frequency of the
   external clock.
#. Set ``enable-gpios = <&gpio0 105 1>`` to select the external clock via J1
   (use ``0`` for the onboard oscillator).
#. Rebuild and install the modified device tree on the target.

Schematics and Design Files
----------------------------

.. admonition:: Download

   Rev C design files for the :adi:`ADRV1CRR-FMC` carrier:

   - :download:`Rev C Schematic (PDF) <02_039799c_top.pdf>`
   - :download:`Rev C BOM (XLSX) <05_039799-c.xlsx>`
   - :download:`Rev C Gerbers (ZIP) <038799c.zip>`
   - :download:`Rev C Allegro Board File (ZIP) <08_039799c.zip>`
   - :download:`Letter of Volatility (PDF) <letter_of_volatility_adrv1-fmc.pdf>`

More Information
----------------

- :ref:`ADRV9361-Z7035 User Guide <adrv9361-z7035>`
- :ref:`ADRV9364-Z7020 User Guide <adrv9364-z7020>`
- :ref:`ADRV1CRR-BOB Breakout Carrier <adrv1crr-bob>`
- :adi:`ADRV1CRR-FMC Product Page <ADRV1CRR-FMC>`

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.

.. esd-warning::
