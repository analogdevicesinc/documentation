.. warning::

   These pages are not updated anymore. Documentation has been moved to :git-lnxdsp-adi-meta:`wiki\`


Configuring Peripherals for the ADSP-SC5xx When Using Linux and SHARC Applications
==================================================================================

| 
| ==== Default Peripheral allocation between SHARCs and ARM ==== By default all peripherals are allocated to the ARM. In order to access a peripheral it is necessary for the pinmux for the peripheral to be configured correctly. The pinmux should only be configured by a single core and by default this is handled by the ARM, which is the booting core.
| Peripheral allocation is controlled by the device tree source file. The device tree source files are located in the Linux source repo in the /arch/arm/boot/dts folder. For the SC594 EZKIT there are two devicetree source files, a generic one for the device family named sc59x.dtsi and a board specific one named sc594-som-ezkit.dts.

For Linkport0 for example there will be an entry in both files. The sc594.dtsi file contains:

::

     lp0: linkport@0 {
         compatible = "linkport0";
         interrupt-parent = <&gic>;
         interrupts = <GIC_SPI 117 IRQ_TYPE_LEVEL_HIGH>,
                      <GIC_SPI 118 IRQ_TYPE_LEVEL_HIGH>;
         clock-div = <1>;
         status = "disabled";
     };

The sc594-som-ezkit.dts contains the following entry which overrides the above status and enables the linkport:

::

     &lp0 {
         pinctrl-names = "default";
         pinctrl-0 = <&lp0_default>;
         status = "okay";
     };

Allocating a peripheral to SHARC
--------------------------------

Allocating a peripheral to SHARC requires changes to the devicetree source file specific to the board. The ARM core is still required to configure the pinmux but should otherwise not interact with the peripheral. For example allocating Linkport0 to the SHARC requires the following changes to sc594-som-ezkit.dts file. First disable Linkport0 in the devicetree:

::

     &lp0 {
         pinctrl-names = "default";
         pinctrl-0 = <&lp0_default>;
         status = "disabled";
     };

Next it is necessary to specify the required pinmux for Linkport0. For any peripherals not used by linux this is handled by the icc driver.:

::

     &pinctrl0 {
         icc {
             icc_default: icc0@0 {
                 adi,group = "lp0grp";
                 adi,function = "lp0";
             };
         };
     };

Lastly the the pincontrol just created needs to be passed into the icc which will then set up the pinmux for Linkport0 use and ensure the pins are reserved. The driver does not interact with the peripheral itself thereby reserving it for the SHARC:

::

     &icc0 {
         pinctrl-names = "default";
         pinctrl-0 = <&icc_default>;
         status = "okay";
     };

The pinmux for Linkport0 is then configured at boot by Linux and can be used by a SHARC core without Linux accessing the device or the pins for any other purpose.
