:doc:`Click here to return to the A2B Raspberry Pi User Guide homepage </wiki-migration/resources/tools-software/a2bv2/a2braspberrypi>`

DTS Overlay
===========

The Raspberry Pi 4 Model B uses the `bcm2711-rpi-4-b.dts <https://github.com/raspberrypi/linux/blob/rpi-5.15.y/arch/arm/boot/dts/bcm2711-rpi-4-b.dts>`__ file to configure its peripherals. To interface the AD242x with the Raspberry Pi, additional configuration is required in an overlay file, which must then be added to the kernel.

The overlay file rpi-ad242x-overlay.dts is provided below to enable the Codec on the Raspberry Pi:

::

   #include <dt-bindings/clock/bcm2835.h>

   /*
     * Device tree overlay - AD242X Transceivers
    */

    /dts-v1/;
    /plugin/;
    / {
        compatible = "brcm,bcm2711";

        fragment@0 {
            target = <&sound>;
            __overlay__ {
                compatible = "simple-audio-card";
                simple-audio-card,name = "ad242x";
                status="okay";
                capture_link: simple-audio-card,dai-link@0 {
                    format = "i2s";
                    r_cpu_dai: cpu {
                        sound-dai = <&i2s>;
                        // TDM slot configuration for stereo
                        dai-tdm-slot-num = <2>;
                        dai-tdm-slot-width = <32>;
                    };

                    r_codec_dai: codec {
                        sound-dai = <&codec_in>;
                    };
                };

                playback_link: simple-audio-card,dai-link@1 {
                    format = "i2s";
                    p_cpu_dai: cpu {
                        sound-dai = <&i2s>;
                        // TDM slot configuration for stereo
                        dai-tdm-slot-num = <2>;
                        dai-tdm-slot-width = <32>;
                    };
                    p_codec_dai: codec {
                        sound-dai = <&codec_out>;
                    };
                };
            };
        };

        fragment@1 {
            target-path = "/";
            __overlay__ {
                codec_out: spdif-transmitter {
                    #address-cells = <0>;
                    #size-cells = <0>;
                    #sound-dai-cells = <0>;
                    compatible = "linux,spdif-dit";
                    status = "okay";
                };
                codec_in: spdif-receiver {
                    #address-cells = <0>;
                    #size-cells = <0>;
                    #sound-dai-cells = <0>;
                    compatible = "linux,spdif-dir";
                    status = "okay";
                };
            };
        };

        fragment@2 {
            target = <&i2s>;
            __overlay__ {
                #sound-dai-cells = <0>;
                status = "okay";
            };
        };
    };

To integrate the AD242x Codec with the Raspberry Pi, follow these steps:

| **Compile the Overlay File:**
| This overlay is based on the reference from `i2smaster.dts <https://github.com/AkiyukiOkayasu/RaspberryPi_I2S_Master/blob/master/i2smaster.dts>`__. Compile the overlay file using the following command: ``dtc -@ -H epapr -O dtb -o rpi-ad242x.dtbo -Wno-unit_address_vs_reg rpi-ad242x-overlay.dts``

| **Copy the Overlay File:**
| Copy the compiled overlay file to the /boot/overlays folder:``sudo cp rpi-ad242x.dtbo /boot/overlays/``

| **Update the Configuration File:**
| Edit the /boot/config.txt file to enable the necessary hardware interfaces. Add or uncomment the following lines: ``dtparam=i2s=on
  dtoverlay=rpi-ad242x``

Save the changes and reboot the Raspberry Pi to apply them.

| **Check the Loaded Module:**
| Ensure that the required module is loaded by running: ``lsmod | grep snd_soc_simple_card``

**PREV :** :doc:`Building the Kernel and Running Application </wiki-migration/resources/tools-software/a2bv2/a2braspberrypi/buildingkernel>` **NEXT :** :doc:`Migrating Latest A2B stack </wiki-migration/resources/tools-software/a2bv2/a2braspberrypi/migratinga2bstack>`
