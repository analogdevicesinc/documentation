Changing the VCXO frequency and updating the default RF Transceiver Profile
===========================================================================

Changing the VCXO frequency
---------------------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9528_fbl.png
   :align: center
   :width: 400px

The ADRV9009, ADRV9008-1, ADRV9008-2, AD9371, AD9375 evaluation boards contains an on-board VCXO (Voltage Controlled Crystal Oscillator) as well as the AD9528 chip responsible for the device clock and SYSREF signal generation and distribution. With the hardware configuration provided on the evaluation board, a user can generate device clock frequencies such as 122.88MHz, 153.6MHz, 184.32MHz, 245.76MHz, and 307.2MHz. There are limitations with the default hardware configuration in the scenario where a user desired device frequencies are not related to the on-board 122.88MHz VCXO by a rational fraction. Examples of such device clock frequency are: 125MHz, 133.33MHz, 250MHz and 266.66MHz. The document below outlines these limitations as well as explains how they can be overcome with an AD9371 evaluation board hardware modification. Pretty much the same things also apply for all the other devices listed above.

-  :ez:`Evaluation-board-vcxo-selection <wide-band-rf-transceivers/design-support-ad9371/w/documents/10080/ad9371-evaluation-board-vcxo-selection>`

This page is supposed to be a system level addition to the aforementioned document with some extra tips and tricks.

Rational
--------

Some reasons why someone would change the onboard VCXO:

-  Being able to generate device clocks which are not a rational fraction of the default 122.88MHz VCXO. For example realize 50, 100, 200 MSPS baseband rates instead of 61.44, 122.88, 245.76 MSPS.
-  Being able to synchronize the VCXO via AD9528 PLL1 with a reference which is not a rational fraction of the default 122.88MHz VCXO. For example with an external 10MHz reference clock, instead of an 30.72MHz reference.
-  Testing a better or worse clock jitter, stability VCXO.

Procedure
---------

In the following example procedure the VCXO is changed to 80MHz to achieve 240, 200, 120, 100 MSPS baseband rates. In general, more common would be to use a 125MHz VCXO instead.

Physically replace the onboard VCXO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

   If you just want to test things without VCXO, there is the option to bypass the VCXO and PLL1 and directly feed an external clock into the AD9528 via the REF_CLK_IN SMA which is typically used to feed the external reference for PLL1. Some resistors and caps need to be flipped. Check the Eval board schematics for more details. In such case you would bypass PLL1 and use differential input.

   
   ::
   
      &clk0_ad9528 {  
          /* PLL1 config */
          adi,pll1-bypass-enable;
          adi,osc-in-diff-enable;
      }
   


Adjust the adi,vcxo-freq device tree property with the used VCXO frequency in Hz
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

   Please see here as well: :doc:`AD9528 Low Jitter Clock Generator Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ad9528>`


::

   &clk0_ad9528 {
       adi,vcxo-freq = <80000000>;
   }

Plan the distribution clock
~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are basically two configuration options. In both examples described below the distribution clock is set to 1200MHz. So each AD9528 output channel can be set to 1200MHz / N where N = 1..256.

Manual configuration
^^^^^^^^^^^^^^^^^^^^

Manual configuration requires to understand the math behind the PLL.

Please also see:

-  :adi:`AD9528 data sheet <static/imported-files/data_sheets/AD9528.pdf>`
-  :adi:`AD9528 Evaluation Board Software <eval-ad9528>`
-  :doc:`Clock Generation and Distribution Evaluation Software User Guide </wiki-migration/resources/eval/csg-evalsoftware-user-guide>`

::

   &clk0_ad9528 { 
       /* Manual divider configuration /
           adi,vcxo-freq = <80000000>;
       adi,pll2-vco-div-m1 = <3>;
       adi,pll2-n2-div = <15>;
       adi,pll2-r1-div = <1>; 
   }

Automatic configuration
^^^^^^^^^^^^^^^^^^^^^^^

Or to use the device driver automatic configuration. This way you only need to specify the ``adi,pll2-m1-frequency``

::

   &clk0_ad9528 { 
           adi,vcxo-freq = <80000000>;
       * Valid ranges based on VCO locking range:
       *   1150.000 MHz - 1341.666 MHz
       *    862.500 MHz - 1006.250 MHz
       *    690.000 MHz -  805.000 MHz
       */
       
           adi,pll2-m1-frequency = <1200000000>;
   }

Updating the default RF Transceiver Profile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now that we know we can generate output clocks such as 80MHz (N=15) 100MHz (N=12) or 120MHz (N=10) we need to create a RF transceiver profile using:

-  :doc:`MATLAB Profile Generator for AD9371 </wiki-migration/resources/eval/user-guides/mykonos/software/filters>`
-  :adi:`MATLAB Filter Wizard / Profile Generator for ADRV9009 <media/en/evaluation-boards-kits/evaluation-software/ADRV9008-x-ADRV9009-profile-config-tool-filter-wizard-v2.4.zip>`

This procedure is not going to describe this process, however once the profile is generated the user has to choose a ``Device Clock`` by selecting a possible Ref Clk Divider. In theory the RF Transceiver can handle all offered options, while typically higher rates are better from a phase noise point of view. But the baseband processor (FPGA) has lots of constrains as well. So practically these limitations must be taken into account as well before making a decision.

.. note::

   It’s a bit out of scope to cover capabilities and constrains of all FPGA vendor architectures. (Xilinx GTX, GTH, GTY type transceivers with their CPLLs and QPLLs or Intel ATX PLL, FPLL, CDR PLL, etc.)


But a good value from various perspectives (such as deterministic latency and link clock) is to choose ``Lane rate / 40``.

Some typical example below, where TX and ORX run at the same baseband rate, and RX is ½ TX rate.

-  TX : FC=\ **240** MSPS, M=\ **4**, L=\ **4**, N’=16, S=1:

   -  Lane Rate = (M x S x N' x 10/8 x FC)/L = **4800Mbit/s**

-  RX : FC=\ **120** MSPS, M=\ **4**, L=\ **2**, N’=16, S=1:

   -  Lane Rate = (M x S x N' x 10/8 x FC)/L = **4800Mbit/s**

-  ORX: FC=\ **240** MSPS, M=\ **2**, L=\ **2**, N’=16, S=1:

   -  Lane Rate = (M x S x N' x 10/8 x FC)/L = **4800Mbit/s**

| 
| **So here Device Clock == FMC Clock = Lane rate / 40 = 120 MHz would be a perfect match. We choose 120MHz in this configuration.**

Once we have changed the clock chip distribution clock, we must also update the default transceiver profile, which is configured for initial setup. Failure to do so can result in the transceiver device driver asking for a clock tree which is not achievable since the AD9528 clock chip driver dynamically controls the output divider but not the PLL2 VCO and distribution clock.

The MATLAB Filter Wizard / Profile Generator generates a XML style output file. It’s pretty easy to understand and can be easily matched to the Linux device tree properties. Besides single key value pairs there are also signed filter coefficients which must be converted to an array style. It’s important to know that signed values must be put in braces. Everything that differs in value must be updated.

Below you cab find a quick and dirty bash script, which allows you to extract the filter arrays:

.. code:: bash

   #!/bin/bash

   while IFS='' read -r line || [[/-n_"$line"|-n_"$line"]]; do
       if [[/$line_==_*"filter"*|$line_==_*"filter"*]]; then
           echo
           start="1"
       fi
       if [[/$line_==_*"adc-profile"*"num"*|$line_==_*"adc-profile"*"num"*]] || [[/$line_==_*"adcprofile"*"num"*|$line_==_*"adcprofile"*"num"*]]; then
           echo
           start="1"
       fi
       if [[/$line_==_*"</"*|"*]]; then
           echo
           start="0"
       fi

       if [ "$start" == "1" ];then
           echo -n "(`echo $line | xargs`) "
       fi
   done < "$1"

In the example below we don’t change things directly in the provided default device trees. In fact there are several which recursively include them. Instead we create a new file (zynq-zc706-adv7511-adrv9371-vcxo80.dts), place it in the same folder, and we include the default dts file. Then we reference the devicetree phandles and either overwrite or delete properties. This way we only handle changes which matters and don't end up maintaining a complete new file.

=============== ===============================================
\               Devicetrees can be found or must be placed here
=============== ===============================================
ZYNQ & SoC FPGA linux/arch/arm/boot/dts/
ZYNQMP          linux/arch/arm64/boot/dts/xilinx/
=============== ===============================================

| Instructions to build and deploy your new/modified devicetree can be found here:

-  :doc:`Building the Zynq Linux kernel and devicetrees from source </wiki-migration/resources/tools-software/linux-build/generic/zynq>`
-  :doc:`Building the ZynqMP / MPSoC Linux kernel and devicetrees from source </wiki-migration/resources/tools-software/linux-build/generic/zynqmp>`

The complete **zynq-zc706-adv7511-adrv9371-vcxo80.dts** file would look like this:

::

   #include "zynq-zc706-adv7511-adrv9371.dts"

   &clk0_ad9528 {
           adi,vcxo-freq = <80000000>;

           /*
            * Valid ranges based on VCO locking range:
            *   1150.000 MHz - 1341.666 MHz
            *    862.500 MHz - 1006.250 MHz
            *    690.000 MHz -  805.000 MHz
            */
           adi,pll2-m1-frequency = <1200000000>;

           /* Manual divider configuration /
           /delete-proptery/ adi,pll2-ndiv-a-cnt;
           /delete-proptery/ adi,pll2-ndiv-b-cnt;
           /delete-proptery/ adi,pll2-vco-div-m1;
           /delete-proptery/ adi,pll2-n2-div;
           /delete-proptery/ adi,pll2-r1-div;

           /* PLL1 config */
           adi,pll1-feedback-div = <8>; /* 10 MHz Reference */
   };

   &trx0_ad9371 {
       adi,clocks-clk-pll-vco-freq_khz = <9600000>;
       adi,clocks-device-clock_khz = <120000>;

           adi,obs-settings-obs-rx-channels-enable = <3>; /* Disable Sniffer Profile */

       adi,rx-profile-iq-rate_khz = <120000>;
       adi,rx-profile-rf-bandwidth_hz = <80000000>;
       adi,rx-profile-rx-fir-gain_db = <(0)>;
       adi,rx-profile-rx-fir-num-fir-coefs = <48>;
       adi,rx-profile-rx-fir-coefs = /bits/ 16 <(0)(0)(1)(2)(-3)(-10)(12)(28)(-33)(-71)(81)(154)(-174)(-305)(343)(561)(-635)(-989)(1155)(1750)(-2330)(-4059)(4644)(16559)(16559)(4644)(-4059)(-2330)(1750)(1155)(-989)(-635)(561)(343)(-305)(-174)(154)(81)(-71)(-33)(28)(12)(-10)(-3)(2)(1)(0)(0)>;
       adi,rx-profile-custom-adc-profile = /bits/ 16  <(574)(382)(201)(98)(1280)(342)(1553)(180)(1285)(67)(784)(33)(48)(38)(23)(189)>;

       adi,obs-profile-iq-rate_khz = <240000>;
       adi,obs-profile-rf-bandwidth_hz = <160000000>;
       adi,obs-profile-rx-bbf-3db-corner_khz = <80000>;
       adi,obs-profile-rx-fir-gain_db = <6>;
       adi,obs-profile-rx-fir-num-fir-coefs = <24>;
       adi,obs-profile-rx-fir-coefs = /bits/ 16 <(-51)(-107)(90)(-29)(-72)(128)(-11)(-279)(178)(-46)(-2343)(21563)(-2343)(-46)(178)(-279)(-11)(128)(-72)(-29)(90)(-107)(-51)(0)>;
       adi,obs-profile-custom-adc-profile = /bits/ 16 <(499)(386)(201)(98)(1280)(534)(1741)(601)(1423)(456)(857)(27)(48)(38)(25)(205)>;
       adi,obs-settings-custom-loopback-adc-profile = /bits/ 16  <(581)(379)(201)(98)(1280)(304)(1544)(157)(1288)(59)(787)(34)(48)(39)(23)(189)>;

       adi,tx-profile-dac-div = <1>;
       adi,tx-profile-iq-rate_khz = <240000>;
       adi,tx-profile-rf-bandwidth_hz = <160000000>;
       adi,tx-profile-tx-bbf-3db-corner_khz = <80000>;
       adi,tx-profile-tx-dac-3db-corner_khz = <160000>;
       adi,tx-profile-tx-fir-gain_db = <6>;
       adi,tx-profile-tx-fir-num-fir-coefs = <16>;
       adi,tx-profile-tx-fir-coefs = /bits/ 16 <(-48)(290)(-51)(-251)(577)(167)(-3254)(21872)(-3254)(167)(577)(-251)(-51)(290)(-48)(0)>;
   };

Modifying the JESD204 configuration example for ADRV9009-ZU11EG
---------------------------------------------------------------

HDL
~~~

If the desired design has other configuration than the default one, you will have to do some modifications to the HDL and devicetree. First of all, the project has to be parametrized in order for this flow to work. A quick check for the **MAX_TX/RX/RX_OS_NUM_OF_LANES** variable into the **common/adrv9009zu11eg_bd.tcl** file would ensure that: :git-hdl:`common/adrv9009zu11eg_bd.tcl <projects/adrv9009zu11eg/common/adrv9009zu11eg_bd.tcl>`

If the condition above is valid, you can jump to the last step from the HDL section. Then, the AXI_XCVR IP has to be configured with the MAX_TX/RX/RX_OS_NUM_OF_LANES instead of TX/RX/RX_OS_NUM_OF_LANES. Check for the ad_xcvrconn function call and use it with a partial lane map as in this example:

::

   ad_xcvrcon  util_adrv9009_som_xcvr axi_adrv9009_som_tx_xcvr axi_adrv9009_som_tx_jesd {0 1 2 3 4 5 6 7} core_clk_a {} $MAX_TX_NUM_OF_LANES {0 1 4 5}

What this does is it gives the util the maximum number of lanes, but only binds the one in the partial lane map (the last list given as a parameter). For the lane map (the first list given as a parameter) it needs to contain all the lanes. The order might be different, depending on the hardware configuration and FMC connections.

After doing all the modifications mentioned above, you can just run:

::

   make TX_JESD_L=4

ADRV9009 Transceiver Evaluation Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After figuring out the HDL, download the transceiver evaluation software from this page, form the **ADRV9008/ADRV9009 Evaluation Software with GUI for Evaluation Board** section:

:adi:`en/design-center/landing-pages/001/transceiver-evaluation-software`.html

The image below contains the first page of the configuration panel. Here you will have to set the device to adrv9009, the desired device clock frequency, the channels that you want to enable and the profile for each of these channels.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/talise3.png
   :alt: talise3.png

Move to the JESD204b Setup tab. Here you can choose what lanes do you want to use in the design, but please keep in mind that the lanes must correspond to the ones picked in HDL.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/talise4.png
   :alt: talise4.png

Now, from the top left corner click Tools, then Create Script and then Init .c Files. If everything goes well you will be welcomed by a success message and you will have a .c file that contains values corresponding the devicetree setup.

Devicetree
~~~~~~~~~~

First, create a new dts file that contains in its name the number of lanes that you are using (ex: zynqmp-adrv9009-zu11eg-tx-l4.dts). Then include the devicetree file that was usually used. Now all that is left to do is overwrite the jesd parameters that are different, according to the .c file generated by the evaluation software. Here is an example for :git-linux:`adrv9009-zu11eg-tx-l4.dts <arch/arm64/boot/dts/xilinx/zynqmp-adrv9009-zu11eg-tx-l4.dts>`:

::

   #include "zynqmp-adrv9009-zu11eg-revb-adrv2crr-fmc-revb-jesd204-fsm.dts"
   &spi0 {
       trx0_adrv9009: adrv9009-phy@0 {
           /* JESD204 */

           /* JESD204 OBS */
           adi,jesd204-framer-b-m = <4>;

           /* JESD204 TX */
           adi,jesd204-deframer-a-deserializer-lanes-enabled = <0x03>;
       };
       trx1_adrv9009: adrv9009-phy-b@1 {
           /* JESD204 */

           /* JESD204 OBS */
           adi,jesd204-framer-b-m = <4>;

           /* JESD204 TX */
           adi,jesd204-deframer-a-deserializer-lanes-enabled = <0x03>;
       };
   };

Here are overwritten the parameters accountable for tx number of lanes and rx_os number of converters (because TX and RX_OS share the same clock => it is recommended to use the same M)

Troubleshooting
---------------

Requesting device clock failed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   ad9371 spi32766.1: Requesting device clock 120000000 failed got 122880000

If you see something like this in your kernel startup messages (dmesg) this indicates that the clock chip distribution clock was not properly set. Check the clock chip (AD9528/HMC7044/etc.) device tree properties.

::

   adrv9009 spi1.0: Requesting device clock 200000000 failed got 187500000

In this particular case the HMC7044 or HMC7043 is used as clock provider. The VCO frequency pas properly set to 3000MHz, from an 100MHz VCXO. However the HMC7044 output divider supports even divide ratios from 2 to 4094. The supported odd divide ratios are 1, 3, and 5. All even and odd divide ratios have 50.0% duty cycle. So in this case a odd divider of 15 is required which the HMC7044 can't support. So the device driver rounded up to 16, which lead to this error. A workaround in this case is to use an VCO of 2800 MHz instead.

Requesting [deframer|framer] lanerate failed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   adrv9009 spi1.1: adrv9009_probe : enter
   adrv9009 spi1.1: Request deframer lanerate 4800000 kHz failed (-22)
   adrv9009 spi1.1: Request deframer lanerate 4800000 kHz failed (-22)
   adrv9009: probe of spi1.1 failed with error -22 

::

   adrv9009 spi1.0: adrv9009_probe : enter
   adrv9009 spi1.0: Request framer lanerate 8000000 kHz failed (-22)
   adrv9009 spi1.0: Request framer lanerate 8000000 kHz failed (-22)
   adrv9009: probe of spi1.0 failed with error -22

Depending on the FPGA gigabit transceiver architecture GTX, GTH, GTY, etc. and the PLL used the VCO tuning ranges might not fit the requested rate. In this case ‘’Request [deframer|framer] lanerate” error is printed. And the driver probe errors with -EINVAL (-22).

For example GTX QPLL actually have two none overlapping frequency bands with a hole in the middle. GTH and GTY do have two QPLLs with slightly different VCO min/max.

-  To avoid these issues increasing/decreasing the number of Lanes used can be useful.
-  Often increasing the QPLL/CPLL reference frequency from lanerate/40 to lanerate/20 can help with that error as well.
-  Switching from QPLL0 to QPLL1 might help as well.
-  Or using CPLL for both links can help, but only in case both links require the same rate.
-  Sometimes the requested value is just a bit out of the specified range. Hacking the driver to exceed the limits might work, but is **not recommended!**

.. code:: c

   index e425c12..81e86e9 100644
   --- a/drivers/iio/jesd204/xilinx_transceiver.c
   +++ b/drivers/iio/jesd204/xilinx_transceiver.c
   @@ -6,7 +6,7 @@
     * Licensed under the GPL-2.
     *
     */
   -
   +#define DEBUG
   #include <linux/device.h>
   #include <linux/fpga/adi-axi-common.h>
   #include <linux/kernel.h>
   @@ -408,7 +408,7 @@ int xilinx_xcvr_calc_qpll_config(struct xilinx_xcvr *xcvr,
                   N = N_gtx2;
                   vco0_min = 5930000;
                   vco0_max = 8000000;
   -               vco1_min = 9800000;
   +               vco1_min = 9600000; /* FIXME: 9800000 */
                   vco1_max = 12500000;
                   break;
           case XILINX_XCVR_TYPE_US_GTH3:
   @@ -424,10 +424,10 @@ int xilinx_xcvr_calc_qpll_config(struct xilinx_xcvr *xcvr,
                   return -EINVAL;
           }

   -       if (AXI_PCORE_VER_MAJOR(xcvr->version) > 0x10)
   -               xilinx_xcvr_setup_qpll_vco_range(xcvr,
   -                                                &vco0_min, &vco0_max,
   -                                                &vco1_min, &vco1_max);
   +//     if (AXI_PCORE_VER_MAJOR(xcvr->version) > 0x10)
   +//             xilinx_xcvr_setup_qpll_vco_range(xcvr,
   +//                                              &vco0_min, &vco0_max,
   +//                                              &vco1_min, &vco1_max);

           for (m = 1; m <= 4; m++) {
                   for (d = 1; d <= 16; d <<= 1) {

ARM Mailbox Busy. Command not executed in MYKONOS_sendArmCommand()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   ERROR: 256: ARM Mailbox Busy. Command not executed in MYKONOS_sendArmCommand()
   ERROR: 256: ARM Mailbox Busy. Command not executed in MYKONOS_sendArmCommand()
   ad9371 spi0.1: ARM Mailbox Busy. Command not executed in MYKONOS_sendArmCommand()
   (256)
   ERROR: 256: ARM Mailbox Busy. Command not executed in MYKONOS_sendArmCommand()
   ERROR: 256: ARM Mailbox Busy. Command not executed in MYKONOS_sendArmCommand()
   ad9371 spi0.1: ARM Mailbox Busy. Command not executed in MYKONOS_sendArmCommand()
   (256)
   ad9371: probe of spi0.1 failed with error -14

This indicates an ARM firmware internal error. Which can be caused by some erroneous or incomplete profile. Please double check all the settings in the devicetree.

ERROR: 321: Tx Profile IQrate and filter settings are not possible with current CLKPLL frequency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   adrv9009 spi1.0: ERROR: 321: Tx Profile IQrate and filter settings are not possible with current CLKPLL frequency

This error originates here::git-linux:`drivers/iio/adc/talise/talise.c <drivers/iio/adc/talise/talise.c#L2230]>`

And typically means that either the profile wizard created an invalid profile or that an typo was introduced in the device tree.

In one particular case the issue was with the **adi,dig-clocks-clk-pll-hs-div** property. A new profile required 2.0 instead of 2.5.

In the device tree we use the enum values:

-  :git-linux:`talise_types.h <drivers/iio/adc/talise/talise_types.h#L28>`

So for hs-div=2.0 must use a value of **0** and NOT 2!

*adi,dig-clocks-clk-pll-hs-div = <0>;*

ERROR: 64: CLKPLL VCO frequency exceeded max(9.216Ghz) in VCO divider /1.5 case ()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Can be caused by an invalid filter wizard profile. Please see answer here: :ez:`Changing the VCXO 80 MHz ad9375 <linux-software-drivers/f/q-a/555532/qec-init/450766>`
