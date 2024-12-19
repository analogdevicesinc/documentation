.. _petalinux system-user:

Device Tree Modifications with system-user.dtsi
===============================================
One of the simplest ways to customize or extend a device tree in a ADI Petalinux
project is to use the system-user.dtsi file, included as part of *meta-user*.

During its device tree recipe, *meta-adi* will automatically re-append the
system-user.dtsi file to end of the device tree, allowing the ability to add
new nodes and customize existing nodes to meet the application.  This is an
ideal solution when leveraging an existing reference design, and making minor
modifications for evaluation and test.

Procedure
---------
The following procedure describes how to leverage the system-user.dtsi file.
This assumes the project has been configured with *meta-adi* and utilizes one of
the existing device trees provided by the ADI kernel, as described in the
*meta-adi* readme file.

This hypothetical example modifies the configuration of the
zynqmp-zcu102-rev10-ad9081-m8-l4 device tree with the following adjustments:

* Change the AD9081 DAC frequency to 6.2GHz
* Update the Tx Channel 0 Shift to 400MHz
* Delete the LPM Mode Enable property on the Rx Xcvr node
* Add another channel to the HMC7044 to support an ADF4378
* Add a ADF4378 to SPI1, using CS Line 1

.. warning::
    The device tree contents in this example a just hypothetical to illustrate
    various actions that can be performed in system-user.dtsi.  These in no way
    likely represent a valid AD9081 configuration.

To apply these changes, the
``<project>/project-spec/meta-user/recipes-bsp/device-tree/files/system-user.dtsi``
file was modified as follows:

.. code-block:: dts
    :caption: system-user.dtsi

    /include/ "system-conf.dtsi"

    /* Update the DAC frequency */
    &trx0_ad9081 {
        adi,tx-dacs {
            adi,dac-frequency-hz = /bits/ 64 <6200000000>;
        };
    };
    /* Update the Channel 0 shift */
    &ad9081_dac0 {
        adi,nco-frequency-shift-hz = /bits/ 64 <400000000>;
    };
    /* Remove the LPM Enable directive */
    &axi_ad9081_adxcvr_rx {
        /delete-property/ adi,use-lpm-enable;
    };
    /* Add another clock channel to the HMC7044 for the ADF4378.
    Channel 1 is not used in the original device tree
    */
    &hmc7044 {
        hmc7044_c1: channel@1 {
        reg = <1>;
        adi,extended-name = "ADF4378_REFCLK";
        adi,divider = <12>;
        adi,driver-mode = <HMC7044_DRIVER_MODE_LVDS>;
        };
    };
    /* Add a ADF4378 to SPI1, CS1 */
    &spi1 {
        adf4378: adf4378@1 {
            #address-cells = <1>;
            #size-cells = <0>;
            #clock-cells = <1>;

            compatible = "adi,adf4378";
            reg = <1>; /* CS 1*/
            spi-max-frequency = <10000000>;
            clocks = <&hmc7044 1>;
            clock-names = "ref_in";
        };
    };

Once system-user.dtsi has been modified, the project may be built as normal
using the standard ``petalinux-build`` command.  To verify the changes, the most
concrete way is to inspect the resulting device tree binary created.

The final dtb file will be in the ``images/linux`` folder of the project. To
decompile the dtb file, run the following.
*This assumes the shell is at the project root, and out_check.dts is the desired
output filename*

``dtc -I dtb -O dts images/linux/system.dtb > out_check.dts``

out_check.dtb can be searched to confirm the incorporated changes. A subset of
incorporated changes verified below:

.. code-block:: dts
    :emphasize-lines: 4

    adi,tx-dacs {
        #size-cells = <0x00>;
        #address-cells = <0x01>;
        adi,dac_frequency-hz = <0x01 0x718c7e00>;

.. code-block:: dts
    :emphasize-lines: 4

    dac@0 {
        reg = <0x00>;
        adi,crossbar-select = <0x28>;
        adi,nco-frequency-shift-hz = <0x00 0x17d78400>;
        phandle = <0xa5>;
    };

.. code-block:: dts
    :emphasize-lines: 1,3

    channel@1 {
        reg = <0x01>;
        adi,extended-name = "ADF4378_REFCLK";
        adi,divider = <0x0c>;
        adi,driver-mode = <0x02>;
        phandle = <0xb8>;
    };

