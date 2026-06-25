.. _ad-jupiter-ebz mcs-setup:

Jupiter_SDR MCS Setup
=====================

Hardware requirements
---------------------

.. figure:: images/jupiter_sdr_2x_system_sync.svg
   :align: center
   :width: 800px

- 1x Main machine running Linux - it’s goal is to control and process data from
  others, through Ethernet(ssh)
- 2x jupiter_sdr + USB C Power supply (5V/3A, 9V/3A) if PoE is not available.
- 2x SD card(min 32G) for jupiter_sdr
- 1x Synchrona + ADD-ON Voltage Translation Board + 12V Power Supply
- 1x Ethernet Switch/Router
- 3x Ethernet cables
- 3x Micro-USB (UART)
- 9x SMA cables

  - 4x SMA cables of same length and type for > 6GHz (splitter to Jupiter_sdr
    Rx)
  - 4x SMA cables for of same length and type for > 6GHz (synchrona to jupiter)
  - 1x SMA cable (Jupiter_sdr Tx to splitter input)

.. important::
    We chose to use Synchrona for clock and MCS requests. If you have
    a different sync setup the constraints are:

     #. Clocks, MCS 6 pulse train or MCS requests should be generated from the
        same source for both systems

         *2x 30.72 MHz, (LVPECL)*

         *2x MCS pulse, at request (LVPECL)*

     #. The trace length should be equal for all mcs and clock paths, from
        reference to the systems inputs. This is if you can afford to delay the
        MCS in regard to the clock, otherwise the MCS cables should be longer
        than the clock ones.

.. _ad-jupiter-ebz mcs-setup prebuild-files:

MCS prebuild files
------------------

The boot partition files for the MCS sync example and the device tree overlays
for Synchrona can be built from the following sources:

- :external+hdl:ref:`Jupiter SDR HDL Reference Design <jupiter_sdr>` -- build
  the FPGA bitstream
- :ref:`linux-kernel zynqmp` -- build the Linux kernel (Image) and the
  device tree (system.dtb) using
  :git-linux:`zynqmp-jupiter-sdr-rx2tx2.dts <2026_R1:arch/arm64/boot/dts/xilinx/zynqmp-jupiter-sdr-rx2tx2.dts>`,
  which enables the ``ssi-sync-gpios`` required for MCS synchronization
- :external+hdl:ref:`build_boot_bin` -- generate the BOOT.BIN

- Synchrona device tree overlay:

  .. important::

     The device tree overlay below needs to be updated for the ``hdl_2026_r1``
     release.

  .. collapsible:: rpi-ad9545-hmc7044.dts

     .. code-block:: dts

        /dts-v1/;

        / {
            compatible = "brcm,bcm2835\0brcm,bcm2709\0brcm,bcm2711";

            fragment@0 {
                target-path = "/";

                __overlay__ {

                    ref_clk_2 {
                        compatible = "fixed-clock";
                        #clock-cells = <0x01>;
                        clock-frequency = <0x989680>;
                        clock-output-names = "Ref-B";
                        phandle = <0x02>;
                    };

                    ref_clk_3 {
                        compatible = "fixed-clock";
                        #clock-cells = <0x01>;
                        clock-frequency = <0x01>;
                        clock-output-names = "Ref-BB";
                        phandle = <0x03>;
                    };

                    ref_m1_clk {
                        compatible = "fixed-clock";
                        #clock-cells = <0x01>;
                        clock-frequency = <0x2faf080>;
                        clock-output-names = "Ref-M1";
                        phandle = <0x04>;
                    };

                    hmc_ref_clk_0 {
                        compatible = "fixed-clock";
                        #clock-cells = <0x01>;
                        clock-frequency = <0x249f000>;
                        clock-output-names = "HMC-REF_CLKIN0";
                        phandle = <0x06>;
                    };

                    hmc_ref_clk_1 {
                        compatible = "fixed-clock";
                        #clock-cells = <0x01>;
                        clock-frequency = <0x249f000>;
                        clock-output-names = "HMC-REF_CLKIN1";
                        phandle = <0x07>;
                    };

                    hmc_ref_clk_3 {
                        compatible = "fixed-clock";
                        #clock-cells = <0x01>;
                        clock-frequency = <0x249f000>;
                        clock-output-names = "HMC-REF_CLKIN3";
                        phandle = <0x08>;
                    };
                };
            };

            fragment@1 {
                target = <0xffffffff>;

                __overlay__ {
                    status = "disabled";
                };
            };

            fragment@2 {
                target = <0xffffffff>;

                __overlay__ {
                    status = "disabled";
                };
            };

            fragment@3 {
                target = <0xffffffff>;

                __overlay__ {

                    gpio_overrides {
                        phandle = <0x01>;

                        pin-25-reset-high {
                            pins = "gpio25";
                            function = "gpio_out";
                            bias-pull-up;
                            output-high;
                            export;
                        };

                        pin-5-reset-low {
                            pins = "gpio5";
                            function = "gpio_out";
                            bias-pull-down;
                        };

                        pin-6-vcxo-select {
                            pins = "gpio6";
                            function = "gpio_out";
                            export;
                            bias-pull-up;
                            output-high;
                        };

                        pin-32-red_led {
                            pins = "gpio12";
                            function = "gpio_out";
                            bias-pull-up;
                            output-high;
                            export;
                        };

                        pin-36-green_led {
                            pins = "gpio16";
                            function = "gpio_out";
                            bias-pull-up;
                            export;
                        };

                        pin-16-sync-en {
                            pins = "gpio23";
                            function = "gpio_out";
                            bias-pull-down;
                            export;
                        };
                    };
                };
            };

            fragment@4 {
                target = <0xffffffff>;

                __overlay__ {
                    compatible = "brcm,bcm2835-spi";
                    #address-cells = <0x01>;
                    #size-cells = <0x00>;
                    status = "okay";

                    ad9545@0 {
                        compatible = "adi,ad9545";
                        reg = <0x00>;
                        #address-cells = <0x01>;
                        #size-cells = <0x00>;
                        pinctrl-0 = <0x01>;
                        pinctrl-names = "default";
                        adi,ref-crystal;
                        adi,ref-frequency-hz = <0x2ee0000>;
                        spi-max-frequency = <0xf4240>;
                        clock-names = "Ref-B\0Ref-BB\0Ref-M1";
                        clocks = <0x02 0x02 0x03 0x03 0x04 0x01>;
                        #clock-cells = <0x02>;
                        assigned-clocks = <0x05 0x02 0x00 0x05 0x01 0x00
                                           0x05 0x01 0x01 0x05 0x00 0x00
                                           0x05 0x00 0x02 0x05 0x00 0x06
                                           0x05 0x00 0x08 0x05 0x03 0x00>;
                        assigned-clock-rates = <0x2710 0x53724e00 0x60216000
                                                0x989680 0x989680 0x249f000
                                                0x989680 0x30d40>;
                        assigned-clock-nshot = <0x00 0x00 0x00 0x00
                                                0x00 0x00 0x01 0x00>;
                        phandle = <0x05>;

                        aux-tdc-clk@0 {
                            reg = <0x00>;
                            adi,pin-nr = <0x01>;
                        };

                        aux-dpll@0 {
                            reg = <0x00>;
                            adi,compensation-source = <0x04>;
                            adi,aux-dpll-bw-mhz = <0xc350>;
                        };

                        ref-input-clk@2 {
                            reg = <0x02>;
                            adi,single-ended-mode = <0x00>;
                            adi,r-divider-ratio = <0x32>;
                            adi,ref-dtol-pbb = <0x989680>;
                            adi,ref-monitor-hysteresis-pbb = <0x155cc>;
                            adi,ref-validation-timer-ms = <0x0a>;
                            adi,freq-lock-threshold-ps = <0x7d0>;
                            adi,phase-lock-threshold-ps = <0x7d0>;
                            adi,freq-lock-fill-rate = <0x14>;
                            adi,freq-lock-drain-rate = <0x14>;
                            adi,phase-lock-fill-rate = <0x14>;
                            adi,phase-lock-drain-rate = <0x14>;
                        };

                        ref-input-clk@3 {
                            reg = <0x03>;
                            adi,single-ended-mode = <0x02>;
                            adi,r-divider-ratio = <0x01>;
                            adi,ref-dtol-pbb = <0x186a0>;
                            adi,ref-monitor-hysteresis-pbb = <0x30d4>;
                            adi,ref-validation-timer-ms = <0x3e8>;
                            adi,freq-lock-threshold-ps = <0x7d0>;
                            adi,phase-lock-threshold-ps = <0x7d0>;
                            adi,freq-lock-fill-rate = <0x64>;
                            adi,freq-lock-drain-rate = <0x0a>;
                            adi,phase-lock-fill-rate = <0x64>;
                            adi,phase-lock-drain-rate = <0x0a>;
                        };

                        aux-nco-clk@0 {
                            reg = <0x00>;
                            adi,freq-lock-threshold-ps = <0xffffff>;
                            adi,phase-lock-threshold-ps = <0xffffff>;
                        };

                        pll-clk@0 {
                            reg = <0x00>;
                            #address-cells = <0x01>;
                            #size-cells = <0x00>;
                            phandle = <0x09>;
                            adi,pll-slew-rate-limit-ps = <0x5f5e100>;

                            profile@0 {
                                reg = <0x00>;
                                adi,pll-source = <0x03>;
                                adi,profile-priority = <0x05>;
                                adi,pll-loop-bandwidth-uhz = <0xc350>;
                                adi,fast-acq-excess-bw = <0x08>;
                                adi,fast-acq-timeout-ms = <0x2710>;
                                adi,fast-acq-lock-settle-ms = <0x3e8>;
                            };

                            profile@1 {
                                reg = <0x01>;
                                adi,pll-source = <0x02>;
                                adi,profile-priority = <0x0f>;
                                adi,pll-loop-bandwidth-uhz = <0xbebc200>;
                            };
                        };

                        pll-clk@1 {
                            reg = <0x01>;
                            #address-cells = <0x01>;
                            #size-cells = <0x00>;
                            phandle = <0x0a>;
                            adi,pll-slew-rate-limit-ps = <0x5f5e100>;

                            profile@0 {
                                reg = <0x00>;
                                adi,pll-source = <0x03>;
                                adi,profile-priority = <0x05>;
                                adi,pll-loop-bandwidth-uhz = <0xc350>;
                                adi,fast-acq-excess-bw = <0x08>;
                                adi,fast-acq-timeout-ms = <0x2710>;
                                adi,fast-acq-lock-settle-ms = <0x3e8>;
                            };

                            profile@1 {
                                reg = <0x01>;
                                adi,pll-source = <0x02>;
                                adi,profile-priority = <0x0f>;
                                adi,pll-loop-bandwidth-uhz = <0xbebc200>;
                            };
                        };

                        output-clk@0 {
                            reg = <0x00>;
                            adi,output-mode = <0x00>;
                            adi,current-source-microamp = <0x3a98>;
                        };

                        output-clk@2 {
                            reg = <0x02>;
                            adi,output-mode = <0x00>;
                            adi,current-source-microamp = <0x3a98>;
                        };

                        output-clk@6 {
                            reg = <0x06>;
                            adi,output-mode = <0x00>;
                            adi,current-source-microamp = <0x3a98>;
                        };

                        output-clk@8 {
                            reg = <0x08>;
                            adi,output-mode = <0x00>;
                            adi,current-source-microamp = <0x3a98>;
                        };
                    };

                    hmc7044@1 {
                        reg = <0x01>;
                        #address-cells = <0x01>;
                        #size-cells = <0x00>;
                        #clock-cells = <0x01>;
                        compatible = "adi,hmc7044";
                        spi-max-frequency = <0xf4240>;
                        adi,pll1-clkin-frequencies = <0x249f000 0x249f000
                                                      0x249f000 0x249f000>;
                        adi,pll1-ref-prio-ctrl = <0xff>;
                        adi,pll1-ref-autorevert-enable;
                        adi,pll1-loop-bandwidth-hz = <0xc8>;
                        adi,clkin0-buffer-mode = <0x07>;
                        adi,clkin1-buffer-mode = <0x07>;
                        adi,clkin2-buffer-mode = <0x07>;
                        adi,clkin3-buffer-mode = <0x07>;
                        clocks = <0x06 0x00 0x07 0x00 0x05 0x00 0x06
                                  0x08 0x00 0x05 0x00 0x08>;
                        clock-names = "clkin0\0clkin1\0clkin2\0clkin3\0sync_clk";
                        adi,vcxo-frequency = <0x7530000>;
                        adi,pll2-output-frequency = <0x927c0000>;
                        adi,sysref-timer-divider = <0xf00>;
                        adi,pulse-generator-mode = <0x01>;
                        adi,oscin-buffer-mode = <0x15>;
                        adi,sync-pin-mode = <0x01>;
                        adi,gpi-controls = <0x00 0x00 0x00 0x00>;
                        adi,gpo-controls = <0x1f 0x2b 0x00 0x00>;
                        clock-output-names = "HMC7044_OUT0\0HMC7044_OUT1\0HMC7044_OUT2\0HMC7044_OUT3\0HMC7044_OUT4\0HMC7044_OUT5\0HMC7044_OUT6\0HMC7044_OUT7\0HMC7044_OUT8\0HMC7044_OUT9\0HMC7044_OUT10\0HMC7044_OUT11\0HMC7044_OUT12\0HMC7044_OUT13";
                        phandle = <0x0b>;

                        channel@0 {
                            reg = <0x00>;
                            adi,extended-name = "HMC7044_CLKOUT0_CH11";
                            adi,divider = <0x50>;
                            adi,driver-mode = <0x01>;
                            adi,output-mux-mode = <0x00>;
                            adi,fine-analog-delay = <0x00>;
                            adi,coarse-digital-delay = <0x00>;
                            adi,disable;
                        };

                        channel@1 {
                            reg = <0x01>;
                            adi,extended-name = "HMC7044_CLKOUT1_CH12";
                            adi,divider = <0x50>;
                            adi,driver-mode = <0x01>;
                            adi,output-mux-mode = <0x00>;
                            adi,fine-analog-delay = <0x00>;
                            adi,coarse-digital-delay = <0x00>;
                            adi,disable;
                        };

                        channel@2 {
                            reg = <0x02>;
                            adi,extended-name = "HMC7044_CLKOUT2_CH14";
                            adi,divider = <0x50>;
                            adi,driver-mode = <0x01>;
                            adi,output-mux-mode = <0x00>;
                            adi,fine-analog-delay = <0x00>;
                            adi,coarse-digital-delay = <0x00>;
                            adi,disable;
                        };

                        channel@3 {
                            reg = <0x03>;
                            adi,extended-name = "HMC7044_CLKOUT3_CH13";
                            adi,divider = <0x50>;
                            adi,driver-mode = <0x01>;
                            adi,output-mux-mode = <0x00>;
                            adi,fine-analog-delay = <0x00>;
                            adi,coarse-digital-delay = <0x00>;
                            adi,disable;
                        };

                        channel@4 {
                            reg = <0x04>;
                            adi,extended-name = "HMC7044_CLKOUT4_CH8";
                            adi,divider = <0xf00>;
                            adi,driver-mode = <0x03>;
                            adi,output-mux-mode = <0x00>;
                            adi,fine-analog-delay = <0x00>;
                            adi,coarse-digital-delay = <0x08>;
                            adi,driver-impedance-mode = <0x01>;
                        };

                        channel@5 {
                            reg = <0x05>;
                            adi,extended-name = "HMC7044_CLKOUT5_CH10";
                            adi,divider = <0x50>;
                            adi,driver-mode = <0x01>;
                            adi,output-mux-mode = <0x00>;
                            adi,fine-analog-delay = <0x00>;
                            adi,coarse-digital-delay = <0x03>;
                        };

                        channel@6 {
                            reg = <0x06>;
                            adi,extended-name = "HMC7044_CLKOUT6_CH6";
                            adi,divider = <0xf00>;
                            adi,driver-mode = <0x03>;
                            adi,output-mux-mode = <0x00>;
                            adi,fine-analog-delay = <0x00>;
                            adi,coarse-digital-delay = <0x00>;
                            adi,driver-impedance-mode = <0x00>;
                            adi,disable;
                        };

                        channel@7 {
                            reg = <0x07>;
                            adi,extended-name = "HMC7044_CLKOUT7_CH4";
                            adi,divider = <0xf00>;
                            adi,driver-mode = <0x03>;
                            adi,driver-impedance-mode = <0x01>;
                            adi,startup-mode-dynamic-enable;
                            adi,high-performance-mode-disable;
                            adi,force-mute-enable;
                            adi,dynamic-driver-enable;
                            adi,coarse-digital-delay = <0x10>;
                        };

                        channel@8 {
                            reg = <0x08>;
                            adi,extended-name = "HMC7044_CLKOUT8_CH1";
                            adi,divider = <0xf00>;
                            adi,driver-mode = <0x03>;
                            adi,driver-impedance-mode = <0x01>;
                            adi,startup-mode-dynamic-enable;
                            adi,high-performance-mode-disable;
                            adi,force-mute-enable;
                            adi,dynamic-driver-enable;
                            adi,coarse-digital-delay = <0x10>;
                        };

                        channel@9 {
                            reg = <0x09>;
                            adi,extended-name = "HMC7044_CLKOUT9_CH2";
                            adi,divider = <0x50>;
                            adi,driver-mode = <0x01>;
                            adi,output-mux-mode = <0x00>;
                            adi,fine-analog-delay = <0x00>;
                            adi,coarse-digital-delay = <0x04>;
                        };

                        channel@10 {
                            reg = <0x0a>;
                            adi,extended-name = "HMC7044_CLKOUT10_CH3";
                            adi,divider = <0x50>;
                            adi,driver-mode = <0x01>;
                            adi,output-mux-mode = <0x00>;
                            adi,fine-analog-delay = <0x00>;
                            adi,coarse-digital-delay = <0x00>;
                        };

                        channel@11 {
                            reg = <0x0b>;
                            adi,extended-name = "HMC7044_CLKOUT11_CH5";
                            adi,divider = <0xf00>;
                            adi,driver-mode = <0x03>;
                            adi,driver-impedance-mode = <0x01>;
                            adi,startup-mode-dynamic-enable;
                            adi,high-performance-mode-disable;
                            adi,force-mute-enable;
                            adi,dynamic-driver-enable;
                            adi,coarse-digital-delay = <0x10>;
                        };

                        channel@12 {
                            reg = <0x0c>;
                            adi,extended-name = "HMC7044_CLKOUT12_CH9";
                            adi,divider = <0x50>;
                            adi,driver-mode = <0x01>;
                            adi,output-mux-mode = <0x00>;
                            adi,fine-analog-delay = <0x00>;
                            adi,coarse-digital-delay = <0x00>;
                        };

                        channel@13 {
                            reg = <0x0d>;
                            adi,extended-name = "HMC7044_CLKOUT13_CH7";
                            adi,divider = <0xf00>;
                            adi,driver-mode = <0x03>;
                            adi,driver-impedance-mode = <0x01>;
                            adi,startup-mode-dynamic-enable;
                            adi,high-performance-mode-disable;
                            adi,force-mute-enable;
                            adi,dynamic-driver-enable;
                            adi,disable;
                        };
                    };
                };
            };

            fragment@5 {
                target-path = "/";

                __overlay__ {

                    power_ctrl {
                        compatible = "gpio-poweroff";
                        gpios = <0xffffffff 0x15 0x11>;
                        input;
                        force;
                        phandle = <0x0c>;
                    };
                };
            };

            fragment@6 {
                target-path = "/soc";

                __overlay__ {

                    shutdown_button@3 {
                        compatible = "gpio-keys";
                        status = "okay";
                        phandle = <0x0d>;

                        shutdown {
                            label = "shutdown";
                            linux,code = <0x74>;
                            gpios = <0xffffffff 0x14 0x11>;
                            debounce-interval = <0x64>;
                            phandle = <0x0e>;
                        };
                    };
                };
            };

            fragment@7 {
                target = <0xffffffff>;

                __overlay__ {
                    compatible = "brcm,bcm2711-i2c";
                    status = "okay";
                    #address-cells = <0x01>;
                    #size-cells = <0x00>;

                    adt7422@48 {
                        compatible = "adi,adt7422";
                        reg = <0x48>;
                    };
                };
            };

            __symbols__ {
                ref_clk2 = "/fragment@0/__overlay__/ref_clk_2";
                ref_clk3 = "/fragment@0/__overlay__/ref_clk_3";
                ref_m1 = "/fragment@0/__overlay__/ref_m1_clk";
                hmc_ref_clk0 = "/fragment@0/__overlay__/hmc_ref_clk_0";
                hmc_ref_clk1 = "/fragment@0/__overlay__/hmc_ref_clk_1";
                hmc_ref_clk3 = "/fragment@0/__overlay__/hmc_ref_clk_3";
                gpio_overrides = "/fragment@3/__overlay__/gpio_overrides";
                ad9545_clock = "/fragment@4/__overlay__/ad9545@0";
                ad9545_apll0 = "/fragment@4/__overlay__/ad9545@0/pll-clk@0";
                ad9545_apll1 = "/fragment@4/__overlay__/ad9545@0/pll-clk@1";
                hmc7044_fmc = "/fragment@4/__overlay__/hmc7044@1";
                power_ctrl = "/fragment@5/__overlay__/power_ctrl";
                shutdown_button = "/fragment@6/__overlay__/shutdown_button@3";
                button = "/fragment@6/__overlay__/shutdown_button@3/shutdown";
            };

            __fixups__ {
                spidev0 = "/fragment@1:target:0";
                spidev1 = "/fragment@2:target:0";
                gpio = "/fragment@3:target:0\0/fragment@5/__overlay__/power_ctrl:gpios:0\0/fragment@6/__overlay__/shutdown_button@3/shutdown:gpios:0";
                spi0 = "/fragment@4:target:0";
                i2c1 = "/fragment@7:target:0";
            };

            __local_fixups__ {

                fragment@4 {

                    __overlay__ {

                        ad9545@0 {
                            pinctrl-0 = <0x00>;
                            clocks = <0x00 0x08 0x10>;
                            assigned-clocks = <0x00 0x0c 0x18 0x24
                                               0x30 0x3c 0x48 0x54>;
                        };

                        hmc7044@1 {
                            clocks = <0x00 0x08 0x10 0x1c 0x24>;
                        };
                    };
                };
            };
        };

  To compile the overlay:

  .. code-block:: bash

     dtc -@ -I dts -O dtb -o rpi-ad9545-hmc7044.dtbo rpi-ad9545-hmc7044.dts

Setup
-----

Since Synchrona provides the reference clock for the Jupiter SDR boards, it
must be configured and running before powering up the Jupiter SDRs.

.. _ad-jupiter-ebz mcs-setup setting-synchrona:

Setting Synchrona for MCS setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Power up the system/Wait for it to boot(1min).

#. Using a UART terminal, read the IP address of the Pi(synchrona). Enter
   ifconfig

#. Copy the device-tree rpi-ad9545-hmc7044.dtbo on the synchrona SD card via scp
   (or locally on a different machine) on the boot partition in /boot/overlays.
   :red:`Loading the devicetree object in the GUI might get the`
   :red:`desired frequency but it will not wait for a synq request`.

#. Reboot Synchrona

#. To check if the configuration was set, after reboot, you can enter in a
   browser enter the IP address. In the GUI that will open in browser, log in
   with User “admin”, pass: “analog”

   The **Advanced** and **Debug** tabs should look like the following images
   after the device tree is loaded.

   .. tab-set::

      .. tab-item:: Before loading the device tree

         .. figure:: images/synchrona_advanced_tab_init.png
            :align: center

            Advanced tab before loading the device tree

         .. figure:: images/synchrona_debug_tab_init.png
            :align: center

            Debug tab before loading the device tree

      .. tab-item:: After loading the device tree

         .. figure:: images/synchrona_advanced_tab_devicetree_loaded.png
            :align: center

            Advanced tab after loading the device tree

         .. figure:: images/synchrona_debug_tab_devicetree_loaded.png
            :align: center

            Debug tab after loading the device tree

   .. warning::

      If the configuration does not match the images above, follow these steps:

      #. In the **Advanced** tab, in the **Input Priority** section, drag the
         TCXO to the top of the list using the three-line handle on the right
         side.
      #. Click **Reload Config**.
      #. Press **OK** in the warning dialog if it appears.
      #. Reboot the Synchrona.
      #. After reboot, refresh the web page in your browser.

If your Synchrona does not boot or you need a fresh SD card for synchrona, you
should re-image the SD card with the image from the bottom of this section, or
check if there is a newer version on :ref:`ad-syncrhona14-ebz`

- Write the image to an SD card, 16 G or above. Using your favourite tool

- Insert the freshly written SD card into the Synchrona’s raspberry Pi and power
  up the system

- After boot, configure the following in the serial terminal:

  - Make sure in the /boot/config.txt there the below line pointing to the
    Synchrona devicetree overlay.

     .. code-block::

        dtoverlay=rpi-ad9545-hmc7044.dtbo

- By default, the IP is static. 192.168… . So, if needed you can enable the dhcp
  by running the enable_dhcp.sh script:

 .. code-block::

    root@analog:~# cd /root/linux_image_ADI-scripts/
    root@analog:/linux_image_ADI-scripts# ./enable_dhcp.sh
    root@analog:/linux_image_ADI-scripts# reboot

After reboot, start from :ref:`ad-jupiter-ebz mcs-setup setting-synchrona` point
2. above.

More info on :ref:`ad-syncrhona14-ebz`

None of the jumpers should be connected on Synchrona’s ADD-ON board

.. figure:: images/ad-synchrona14-ebz2_top-1000.jpg
   :align: center
   :width: 800px

Setting up Jupiter SDR
~~~~~~~~~~~~~~~~~~~~~~

#.  Write the latest Kuiper image on the SD cards
    :external+kuiper:doc:`Kuiper images <index>`

#.  Build the boot files (Image, system.dtb, BOOT.BIN and boot.scr) as described
    in the :ref:`MCS prebuild files <ad-jupiter-ebz mcs-setup prebuild-files>`
    section and copy them on the boot partition of the SD cards.

#.  Make sure the Synchrona reference clock is connected and running.

#.  Insert the SD cards and power up the Jupiter SDRs.

#.  You need all 4 machines (Main, Jupiter SDR, Synchrona) in the same LAN
    network, even if a DHCP server is not present

#.  Using a UART terminal, read the IP addresses of the Jupiter SDRs and
    Synchrona by entering ``ifconfig`` in their UART console.

#.  On the main Linux machine, make sure you have installed python3, libiio and
    pyadi-iio, more info in :ref:`ad-jupiter-ebz mcs-setup prepare-python-tests`
    section.

#.  Enter in the folder examples/adrv9002_mcs_sync and run
    ``python3 jupiter_sync.py``.

.. _ad-jupiter-ebz mcs-setup connecting-synchrona:

Connecting Jupiter SDR with Synchrona
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: images/jupitersdr_front1.png
   :align: center
   :width: 800px

.. figure:: images/synchrona_front.jpg
   :align: center
   :width: 800px

============= =========== ====== ========= ========
Synchrona SMA Jupiter SMA Signal Frequency Standard
============= =========== ====== ========= ========
ch9_p         Ref Clk     Clock  30.72 MHz LVPECL
ch10_p        Ref Clk     Clock  30.72 MHz LVPECL
ch5_p         MCS         MCS    640 KHz   CMOS
ch8_p         MCS         MCS    640 KHz   CMOS
============= =========== ====== ========= ========

.. caution::

    ch9_n and ch10_n must have 50 ohm SMA terminations.

.. figure:: images/sma-termination.jpg
   :align: center
   :width: 800px

Configuring Synchrona in a 4 Jupiter SDR syncronization setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Not all channels can be used, some channels have the option for sync request,
others don’t. Below is a table with the possible sync scheme, sine channels
require soldering components on Synchrona. More info on
:ref:`ad-syncrhona14-ebz`

============= =========== ====== ========= ========
Synchrona SMA Jupiter SMA Signal Frequency Standard
============= =========== ====== ========= ========
ch1_p         MCS         MCS    640 KHz   CMOS
ch2_p         Ref Clk     Clock  30.72 MHz LVPECL
ch3_p         Ref Clk     Clock  30.72 MHz LVPECL
ch4_p         MCS         MCS    640 KHz   CMOS
ch5_p         MCS         MCS    640 KHz   CMOS
ch6_p         Ref Clk     -      30.72 MHz -
ch7_p         Ref Clk     -      30.72 MHz -
ch8           MCS         MCS    640 KHz   CMOS
ch9_p         Ref Clk     Clock  30.72 MHz LVPECL
ch10_p        Ref Clk     Clock  30.72 MHz LVPECL
============= =========== ====== ========= ========

.. caution::

    Each negative pair of a clock must have 50 ohm SMA termination mounted.

.. _ad-jupiter-ebz mcs-setup prepare-python-tests:

Prepare and run Python tests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We recommend that you have git installed on your machine. Because we need a
specific branch of the development repo.

.. code-block::

   sudo apt install git

You also need to have `libiio <https://github.com/analogdevicesinc/libiio>`__
and `pyadi-iio <https://github.com/analogdevicesinc/pyadi-iio>`__ installes, as
described below Install the required tools

.. code-block::

   sudo apt-get update
   sudo apt install git
   sudo apt-get install build-essential
   sudo apt-get install libxml2-dev libzstd-dev bison flex libcdk5-dev cmake
   sudo apt-get install libaio-dev libusb-1.0-0-dev
   sudo apt-get install libserialport-dev libavahi-client-dev
   sudo apt-get install doxygen graphviz
   sudo apt-get install python3 python3-pip python3-setuptools
   apt install python3.10-venv
   pip install paramiko
   pip install matplotlib

Clone libiio, use v0.25.

.. code-block::

   git clone https://github.com/analogdevicesinc/libiio.git
   git checkout  v0.25
   cd libiio
   mkdir build
   cd build
   cmake ../ -DCPP_BINDINGS=ON -DPYTHON_BINDINGS=ON
   make -j$(nproc)
   sudo make install
   cd ../..

Clone and install pyadi-iio, use tfcollins/jupiter-sync brnach. The below
example was runed on Ubuntu 22.4, which requires a virtual environment.

.. code-block::

   git clone https://github.com/analogdevicesinc/pyadi-iio.git
   cd pyadi-iio
   git checkout tfcollins/jupiter-sync
   python3 -m venv venv
   sudo apt install python3.10-venv
   source venv/bin/activate
   pip install -e .

Go to the example jupiter scripts folder and edit, using your desired editor,
jupiter_sync.py. Add the ip addr of the Synchrona and of the Jupiters to sync.

.. code-block::

   cd examples/adrv9002_mcs_sync
   vim jupiter_sync.py

The script can synchronize from 1 up to 4 Jupiters. At this moment, the limit
comes from Synchrona’s available outputs.

.. code-block::

   synchrona_ip = "192.168.0.1"
   device_ips = ["192.168.0.2", "192.168.0.3", "192.168.0.4", "192.168.0.5"]

Call the script

.. code-block::

   python3 ./jupiter_sync.py

Expected results
~~~~~~~~~~~~~~~~~~~~

.. code-block::

   DEBUG:adi.adrv9002_multi:Creating primary device: ip:192.168.0.2
   DEBUG:adi.adrv9002_multi:Creating secondary device: ip:192.168.0.3
   DEBUG:adi.adrv9002_multi:Creating secondary device: ip:192.168.0.4
   DEBUG:adi.adrv9002_multi:Creating secondary device: ip:192.168.0.5
   Loading profiles
   DEBUG:adi.adrv9002_multi:Setting profile_config on ip:192.168.0.2
   DEBUG:adi.adrv9002_multi:Setting profile_config on ip:192.168.0.3
   DEBUG:adi.adrv9002_multi:Setting profile_config on ip:192.168.0.4
   DEBUG:adi.adrv9002_multi:Setting profile_config on ip:192.168.0.5

   Waiting for 6 pulses
   Requesting sysref
   Waiting for MCS done on ip:192.168.0.2
   ARM rx DMA and DDS cores
   Mute DAC data sources
   ARM RX/TX transfer paths
   Configure DDSs
   Set DDS as DAC data source
   Enable Rx channels and define buffer size
   Issue Sync pulse
   Capture data


A window with a python plot will appear.

.. figure:: images/mcs_result.png
   :align: center
   :width: 800px


Description of key aspects
--------------------------

MCS process
~~~~~~~~~~~

jupiter_sdr signal chain description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The clock and MCS requests, generated by Synchrona, are driving the
Jupiter_SDRs. The 6 MCS pulses required by adrv9002, are generated in HDL and
have characteristics defined in software by the user.

The MCS procedure is not enough to synchronize the systems.

After MCS we will have synchronized clocks and LOs. Each Rx channel has in
independent SSI reference clock driving the data path up to a DMA. Meaning, for
this e.g. to synchronize a reception, we have to synchronize 4 DMAs across 2
systems. This is done with a sync_req from Synchrona. The sync_request will
generate a trigger pulse in the HDL MCS sync logic, dedicated for the
transmission steps. Which will release the armed Rx DMAS on the start_sync DMA
feature/signal.

The Tx receives the same trigger signal, which releases the cores from the armed
state.

Notes
-----

- SSI - source synchronous interface

- MCS - Multi Chip Synchronization

Tips
----

If you can connect the systems to a LAN which has DHCP server, it is recommended
to do so. Otherwise, you can use a switch and set static IPs.

If you get a static IP and are expecting one from your network, call script:

.. code-block::

   ./enable_dhcp.sh

Same for Jupiter and Synchrona, see Synchrona setup above.

If you need a static IP, you can set the system for a desired IP by calling:

.. code-block::

    enable_static_ip.sh 192.168.1.100 eth0

Resources
---------

- :git-pyadi-iio:`pyadi-iio/tree/tfcollins/jupiter-sync/examples/adrv9002_mcs_sync <tfcollins/jupiter-sync:examples/adrv9002_mcs_sync>`
