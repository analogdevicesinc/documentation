# Direct LIBIIO Access of the PlutoSDR

Pluto runs a Linux operating system, so you can use standard Linux commands to navigate the file system, manage processes, and configure settings. You can also run custom scripts or install additional software on Pluto if needed.

ADI use [IIO](https://www.kernel.org/doc/html/v6.1/driver-api/iio/index.html) to interface with the Pluto hardware. IIO provides a powerful and flexible way to control Pluto's features and access its data. You can use the IIO command line tools or write custom scripts using the IIO API to interact with Pluto and perform various tasks such as configuring the radio settings, streaming data, or processing signals.

Let's explore these commands now.  In the previous section, we detailed how to connect to Pluto via SSH or through the serial COM port.  Use one of those methods now to access the Pluto command line shell.  Remember the username is root, password is analog.

```{image} resources/pluto_ssh.png
:width: 800px
:align: center
```  

From the shell you can use libiio userspace command line tools such as `iio_info` to get information about the available devices and channels on Pluto, or `iio_attr` to read and write attributes of the devices. You can also use the IIO API in your own scripts or applications to control Pluto and access its data.

| Tool           | Purpose                   |
| -------------- | ------------------------- |
| `iio_info`     | List devices and contexts |
| `iio_attr`     | Read/write attributes     |
| `iio_readdev`  | Capture samples           |
| `iio_writedev` | Transmit samples          |
| `iio_reg`      | Register access           |
| `iio_monitor`  | Buffer monitoring         |
| `iio_genxml`   | Generate XML context      |


Lets try using `iio_info` to get information about the available devices and channels on Pluto, you can run the following command in the SSH terminal:

```bash
iio_info -s
```

The **-s** is asking libIIO to show the available contexts. Think of a contexts as a list of libIIO interfaces. These interfaces allow the caller to read / write attributes and buffer data from Pluto.  

You should see something like this:

```{code-block} bash 

Available contexts:
        0: 192.168.2.1 (Analog Devices PlutoSDR Rev.C (Z7010-AD9363A)), serial=10447318ac0f000911002700454e18a382 [ip:pluto.local]
        1: fe80::205:f7ff:feee:7a05%usb0 (Analog Devices PlutoSDR Rev.C (Z7010-AD9363A)), serial=10447318ac0f000911002700454e18a382 [ip:pluto.local]
        2: (cf-ad9361-dds-core-lpc,xadc,cf-ad9361-lpc,one-bit-adc-dac,ad9361-phy,adi-iio-fakedev on Analog Devices PlutoSDR Rev.C (Z7010/AD9363)) [local:]
```

What does it all mean?
- The first two contexts (0 and 1) are the same Pluto device, but accessed via different interfaces (IP and local). You can use either of these contexts to access Pluto's features and data.
- The third context (2) is a local context that provides access to the various devices and  channels on Pluto. This context is useful for advanced users who want to access specific features or data on Pluto.

We have context information, how do we use it? 

```bash
iio_info -u ip:192.168.2.1
```

This command is asking libIIO to show the available devices and channels on Pluto, accessed via the IP interface. You should see a list of devices and channels that are available on Pluto, along with their attributes and capabilities. The -u is asking libIIO to use the specified URI to access Pluto. In this case, we are using the IP address of Pluto to access it over the network.

It will respond with a list of devices and channels that are available on Pluto, along with their attributes and capabilities. You can use this information to configure Pluto and access its features and data:

```{code-block} bash
:class: scrollable

iio_info version: 0.26 (git tag:v0.26)
Libiio version: 0.26 (git tag: v0.26) backends: local xml ip usb serial
IIO context created with network backend.
Backend version: 0.26 (git tag: v0.26)
Backend description string: 192.168.2.1 Linux (none) 6.1.0-gf3da30df6004 #5 SMP PREEMPT Tue Oct 15 10:50:00 CEST 2024 armv7l
IIO context has 9 attributes:
        hw_model: Analog Devices PlutoSDR Rev.C (Z7010-AD9363A)
        hw_model_variant: 1
        hw_serial: 10447318ac0f000911002700454e18a382
        fw_version: v0.39
        ad9361-phy,xo_correction: 40000120
        ad9361-phy,model: ad9363a
        local,kernel: 6.1.0-gf3da30df6004
        uri: ip:192.168.2.1
        ip,ip-addr: 192.168.2.1
IIO context has 6 devices:
        iio:device0: ad9361-phy
                9 channels found:
                        altvoltage1: TX_LO (output)
                        9 channel-specific attributes found:
                                attr  0: external value: 0
                                attr  1: fastlock_load value: 0
                                attr  2: fastlock_recall ERROR: Invalid argument (22)
                                attr  3: fastlock_save value: 0 215,88,82,189,206,82,94,233,207,203,99,239,203,206,73,239
                                attr  4: fastlock_store value: 0
                                attr  5: frequency value: 2450000000
                                attr  6: frequency_available value: [325000000 1 3800000000]
                                attr  7: label value: TX_LO
                                attr  8: powerdown value: 0
                        voltage0:  (input)
                        15 channel-specific attributes found:
                                attr  0: bb_dc_offset_tracking_en value: 1
                                attr  1: filter_fir_en value: 0
                                attr  2: gain_control_mode value: slow_attack
                                attr  3: gain_control_mode_available value: manual fast_attack slow_attack hybrid
                                attr  4: hardwaregain value: 71.000000 dB
                                attr  5: hardwaregain_available value: [-3 1 71]
                                attr  6: quadrature_tracking_en value: 1
                                attr  7: rf_bandwidth value: 18000000
                                attr  8: rf_bandwidth_available value: [200000 1 56000000]
                                attr  9: rf_dc_offset_tracking_en value: 1
                                attr 10: rf_port_select value: A_BALANCED
                                attr 11: rf_port_select_available value: A_BALANCED B_BALANCED C_BALANCED A_N A_P B_N B_P C_N C_P TX_MONITOR1 TX_MONITOR2 TX_MONITOR1_2
                                attr 12: rssi value: 112.25 dB
                                attr 13: sampling_frequency value: 30720000
                                attr 14: sampling_frequency_available value: [2083333 1 61440000]
                        voltage3:  (output)
                        8 channel-specific attributes found:
                                attr  0: filter_fir_en value: 0
                                attr  1: raw value: 306
                                attr  2: rf_bandwidth value: 18000000
                                attr  3: rf_bandwidth_available value: [200000 1 40000000]
                                attr  4: rf_port_select_available value: A B
                                attr  5: sampling_frequency value: 30720000
                                attr  6: sampling_frequency_available value: [2083333 1 61440000]
                                attr  7: scale value: 1.000000
                        altvoltage0: RX_LO (output)
                        9 channel-specific attributes found:
                                attr  0: external value: 0
                                attr  1: fastlock_load value: 0
                                attr  2: fastlock_recall ERROR: Invalid argument (22)
                                attr  3: fastlock_save value: 0 255,178,121,233,249,175,232,179,114,253,43,174,163,139,51,216
                                attr  4: fastlock_store value: 0
                                attr  5: frequency value: 2399999998
                                attr  6: frequency_available value: [325000000 1 3800000000]
                                attr  7: label value: RX_LO
                                attr  8: powerdown value: 0
                        voltage2:  (output)
                        8 channel-specific attributes found:
                                attr  0: filter_fir_en value: 0
                                attr  1: raw value: 306
                                attr  2: rf_bandwidth value: 18000000
                                attr  3: rf_bandwidth_available value: [200000 1 40000000]
                                attr  4: rf_port_select_available value: A B
                                attr  5: sampling_frequency value: 30720000
                                attr  6: sampling_frequency_available value: [2083333 1 61440000]
                                attr  7: scale value: 1.000000
                        temp0:  (input)
                        1 channel-specific attributes found:
                                attr  0: input value: 35088
                        voltage0:  (output)
                        10 channel-specific attributes found:
                                attr  0: filter_fir_en value: 0
                                attr  1: hardwaregain value: -10.000000 dB
                                attr  2: hardwaregain_available value: [-89.750000 0.250000 0.000000]
                                attr  3: rf_bandwidth value: 18000000
                                attr  4: rf_bandwidth_available value: [200000 1 40000000]
                                attr  5: rf_port_select value: A
                                attr  6: rf_port_select_available value: A B
                                attr  7: rssi value: 0.00 dB
                                attr  8: sampling_frequency value: 30720000
                                attr  9: sampling_frequency_available value: [2083333 1 61440000]
                        voltage2:  (input)
                        13 channel-specific attributes found:
                                attr  0: bb_dc_offset_tracking_en value: 1
                                attr  1: filter_fir_en value: 0
                                attr  2: gain_control_mode_available value: manual fast_attack slow_attack hybrid
                                attr  3: offset value: 57
                                attr  4: quadrature_tracking_en value: 1
                                attr  5: raw value: 402
                                attr  6: rf_bandwidth value: 18000000
                                attr  7: rf_bandwidth_available value: [200000 1 56000000]
                                attr  8: rf_dc_offset_tracking_en value: 1
                                attr  9: rf_port_select_available value: A_BALANCED B_BALANCED C_BALANCED A_N A_P B_N B_P C_N C_P TX_MONITOR1 TX_MONITOR2 TX_MONITOR1_2
                                attr 10: sampling_frequency value: 30720000
                                attr 11: sampling_frequency_available value: [2083333 1 61440000]
                                attr 12: scale value: 0.305250
                        out:  (input, WARN:iio_channel_get_type()=UNKNOWN)
                        1 channel-specific attributes found:
                                attr  0: voltage_filter_fir_en value: 0
                19 device-specific attributes found:
                                attr  0: calib_mode value: auto
                                attr  1: calib_mode_available value: auto manual manual_tx_quad tx_quad rf_dc_offs rssi_gain_step
                                attr  2: dcxo_tune_coarse ERROR: No such device (19)
                                attr  3: dcxo_tune_coarse_available value: [0 0 0]
                                attr  4: dcxo_tune_fine ERROR: No such device (19)
                                attr  5: dcxo_tune_fine_available value: [0 0 0]
                                attr  6: ensm_mode value: fdd
                                attr  7: ensm_mode_available value: sleep wait alert fdd pinctrl pinctrl_fdd_indep
                                attr  8: filter_fir_config value: FIR Rx: 0,0 Tx: 0,0
                                attr  9: gain_table_config value: <gaintable AD9361 type=FULL dest=3 start=1300000000 end=4000000000>
-3, 0x00, 0x00, 0x20
-3, 0x00, 0x00, 0x00
-3, 0x00, 0x00, 0x00
-2, 0x00, 0x01, 0x00
-1, 0x00, 0x02, 0x00
0, 0x00, 0x03, 0x00
1, 0x00, 0x04, 0x00
2, 0x00, 0x05, 0x00
3, 0x01, 0x03, 0x20
4, 0x01, 0x04, 0x00
5, 0x01, 0x05, 0x00
6, 0x01, 0x06, 0x00
7, 0x01, 0x07, 0x00
8, 0x01, 0x08, 0x00
9, 0x01, 0x09, 0x00
10, 0x01, 0x0A, 0x00
11, 0x01, 0x0B, 0x00
12, 0x01, 0x0C, 0x00
13, 0x01, 0x0D, 0x00
14, 0x01, 0x0E, 0x00
15, 0x02, 0x09, 0x20
16, 0x02, 0x0A, 0x00
17, 0x02, 0x0B, 0x00
18, 0x02, 0x0C, 0x00
19, 0x02, 0x0D, 0x00
20, 0x02, 0x0E, 0x00
21, 0x02, 0x0F, 0x00
22, 0x02, 0x10, 0x00
23, 0x02, 0x2B, 0x20
24, 0x02, 0x2C, 0x00
25, 0x04, 0x27, 0x20
26, 0x04, 0x28, 0x00
27, 0x04, 0x29, 0x00
28, 0x04, 0x2A, 0x00
29, 0x04, 0x2B, 0x00
30, 0x24, 0x21, 0x20
31, 0x24, 0x22, 0x00
32, 0x44, 0x20, 0x20
33, 0x44, 0x21, 0x00
34, 0x44, 0x22, 0x00
35, 0x44, 0x23, 0x00
36, 0x44, 0x24, 0x00
37, 0x44, 0x25, 0x00
38, 0x44, 0x26, 0x00
39, 0x44, 0x27, 0x00
40, 0x44, 0x28, 0x00
41, 0x44, 0x29, 0x00
42, 0x44, 0x2A, 0x00
43, 0x44, 0x2B, 0x00
44, 0x44, 0x2C, 0x00
45, 0x44, 0x2D, 0x00
46, 0x44, 0x2E, 0x00
47, 0x44, 0x2F, 0x00
48, 0x44, 0x30, 0x00
49, 0x44, 0x31, 0x00
50, 0x64, 0x2E, 0x20
51, 0x64, 0x2F, 0x00
52, 0x64, 0x30, 0x00
53, 0x64, 0x31, 0x00
54, 0x64, 0x32, 0x00
55, 0x64, 0x33, 0x00
56, 0x64, 0x34, 0x00
57, 0x64, 0x35, 0x00
58, 0x64, 0x36, 0x00
59, 0x64, 0x37, 0x00
60, 0x64, 0x38, 0x00
61, 0x65, 0x38, 0x20
62, 0x66, 0x38, 0x20
63, 0x67, 0x38, 0x20
64, 0x68, 0x38, 0x20
65, 0x69, 0x38, 0x20
66, 0x6A, 0x38, 0x20
67, 0x6B, 0x38, 0x20
68, 0x6C, 0x38, 0x20
69, 0x6D, 0x38, 0x20
70, 0x6E, 0x38, 0x20
71, 0x6F, 0x38, 0x20
</gaintable>
                                attr 10: multichip_sync ERROR: Permission denied (13)
                                attr 11: rssi_gain_step_error value: lna_error: 0 0 0 0
mixer_error: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
gain_step_calib_reg_val: 0 0 0 0 0
                                attr 12: rx_path_rates value: BBPLL:983040001 ADC:245760000 R2:122880000 R1:61440000 RF:30720000 RXSAMP:30720000
                                attr 13: trx_rate_governor value: nominal
                                attr 14: trx_rate_governor_available value: nominal highest_osr
                                attr 15: tx_path_rates value: BBPLL:983040001 DAC:122880000 T2:122880000 T1:61440000 TF:30720000 TXSAMP:30720000
                                attr 16: waiting_for_supplier value: 0
                                attr 17: xo_correction value: 40000120
                                attr 18: xo_correction_available value: [39992120 1 40008120]
                180 debug attributes found:
                                debug attr  0: digital_tune value: 0
                                debug attr  1: calibration_switch_control value: 0
                                debug attr  2: multichip_sync value: 0
                                debug attr  3: gaininfo_rx2 ERROR: Resource temporarily unavailable (11)
                                debug attr  4: gaininfo_rx1 value: 71 76 0 0 0 0 0 0
                                debug attr  5: bist_timing_analysis value: 0
                                debug attr  6: gpo_set value: 0
                                debug attr  7: bist_tone value: 0
                                debug attr  8: bist_prbs value: 0
                                debug attr  9: loopback value: 0
                                debug attr 10: initialize value: 0
                                debug attr 11: adi,bb-clk-change-dig-tune-enable value: 0
                                debug attr 12: adi,axi-half-dac-rate-enable value: 0
                                debug attr 13: adi,txmon-2-lo-cm value: 48
                                debug attr 14: adi,txmon-1-lo-cm value: 48
                                debug attr 15: adi,txmon-2-front-end-gain value: 2
                                debug attr 16: adi,txmon-1-front-end-gain value: 2
                                debug attr 17: adi,txmon-duration value: 8192
                                debug attr 18: adi,txmon-delay value: 511
                                debug attr 19: adi,txmon-one-shot-mode-enable value: 0
                                debug attr 20: adi,txmon-dc-tracking-enable value: 0
                                debug attr 21: adi,txmon-high-gain value: 24
                                debug attr 22: adi,txmon-low-gain value: 0
                                debug attr 23: adi,txmon-low-high-thresh value: 37000
                                debug attr 24: adi,gpo3-tx-delay-us value: 0
                                debug attr 25: adi,gpo3-rx-delay-us value: 0
                                debug attr 26: adi,gpo2-tx-delay-us value: 0
                                debug attr 27: adi,gpo2-rx-delay-us value: 0
                                debug attr 28: adi,gpo1-tx-delay-us value: 0
                                debug attr 29: adi,gpo1-rx-delay-us value: 0
                                debug attr 30: adi,gpo0-tx-delay-us value: 0
                                debug attr 31: adi,gpo0-rx-delay-us value: 0
                                debug attr 32: adi,gpo3-slave-tx-enable value: 0
                                debug attr 33: adi,gpo3-slave-rx-enable value: 0
                                debug attr 34: adi,gpo2-slave-tx-enable value: 0
                                debug attr 35: adi,gpo2-slave-rx-enable value: 0
                                debug attr 36: adi,gpo1-slave-tx-enable value: 0
                                debug attr 37: adi,gpo1-slave-rx-enable value: 0
                                debug attr 38: adi,gpo0-slave-tx-enable value: 0
                                debug attr 39: adi,gpo0-slave-rx-enable value: 0
                                debug attr 40: adi,gpo3-inactive-state-high-enable value: 0
                                debug attr 41: adi,gpo2-inactive-state-high-enable value: 0
                                debug attr 42: adi,gpo1-inactive-state-high-enable value: 0
                                debug attr 43: adi,gpo0-inactive-state-high-enable value: 0
                                debug attr 44: adi,gpo-manual-mode-enable-mask value: 0
                                debug attr 45: adi,gpo-manual-mode-enable value: 0
                                debug attr 46: adi,aux-dac2-tx-delay-us value: 0
                                debug attr 47: adi,aux-dac2-rx-delay-us value: 0
                                debug attr 48: adi,aux-dac2-active-in-alert-enable value: 0
                                debug attr 49: adi,aux-dac2-active-in-tx-enable value: 0
                                debug attr 50: adi,aux-dac2-active-in-rx-enable value: 0
                                debug attr 51: adi,aux-dac2-default-value-mV value: 0
                                debug attr 52: adi,aux-dac1-tx-delay-us value: 0
                                debug attr 53: adi,aux-dac1-rx-delay-us value: 0
                                debug attr 54: adi,aux-dac1-active-in-alert-enable value: 0
                                debug attr 55: adi,aux-dac1-active-in-tx-enable value: 0
                                debug attr 56: adi,aux-dac1-active-in-rx-enable value: 0
                                debug attr 57: adi,aux-dac1-default-value-mV value: 0
                                debug attr 58: adi,aux-dac-manual-mode-enable value: 1
                                debug attr 59: adi,aux-adc-decimation value: 256
                                debug attr 60: adi,aux-adc-rate value: 40000000
                                debug attr 61: adi,temp-sense-decimation value: 256
                                debug attr 62: adi,temp-sense-periodic-measurement-enable value: 1
                                debug attr 63: adi,temp-sense-offset-signed value: 206
                                debug attr 64: adi,temp-sense-measurement-interval-ms value: 1000
                                debug attr 65: adi,elna-gaintable-all-index-enable value: 0
                                debug attr 66: adi,elna-rx2-gpo1-control-enable value: 0
                                debug attr 67: adi,elna-rx1-gpo0-control-enable value: 0
                                debug attr 68: adi,elna-bypass-loss-mdB value: 0
                                debug attr 69: adi,elna-gain-mdB value: 0
                                debug attr 70: adi,elna-settling-delay-ns value: 0
                                debug attr 71: adi,ctrl-outs-enable-mask value: 255
                                debug attr 72: adi,ctrl-outs-index value: 0
                                debug attr 73: adi,rssi-duration value: 1000
                                debug attr 74: adi,rssi-wait value: 1
                                debug attr 75: adi,rssi-delay value: 1
                                debug attr 76: adi,rssi-unit-is-rx-samples-enable value: 0
                                debug attr 77: adi,rssi-restart-mode value: 3
                                debug attr 78: adi,fagc-adc-large-overload-inc-steps value: 2
                                debug attr 79: adi,fagc-power-measurement-duration-in-state5 value: 64
                                debug attr 80: adi,fagc-rst-gla-if-en-agc-pulled-high-mode value: 0
                                debug attr 81: adi,fagc-rst-gla-en-agc-pulled-high-enable value: 0
                                debug attr 82: adi,fagc-rst-gla-large-lmt-overload-enable value: 1
                                debug attr 83: adi,fagc-rst-gla-large-adc-overload-enable value: 1
                                debug attr 84: adi,fagc-energy-lost-stronger-sig-gain-lock-exit-cnt value: 8
                                debug attr 85: adi,fagc-rst-gla-engergy-lost-sig-thresh-below-ll value: 10
                                debug attr 86: adi,fagc-rst-gla-engergy-lost-goto-optim-gain-enable value: 1
                                debug attr 87: adi,fagc-rst-gla-engergy-lost-sig-thresh-exceeded-enable value: 1
                                debug attr 88: adi,fagc-rst-gla-stronger-sig-thresh-above-ll value: 10
                                debug attr 89: adi,fagc-optimized-gain-offset value: 5
                                debug attr 90: adi,fagc-rst-gla-stronger-sig-thresh-exceeded-enable value: 1
                                debug attr 91: adi,fagc-use-last-lock-level-for-set-gain-enable value: 1
                                debug attr 92: adi,fagc-gain-index-type-after-exit-rx-mode value: 0
                                debug attr 93: adi,fagc-gain-increase-after-gain-lock-enable value: 0
                                debug attr 94: adi,fagc-final-overrange-count value: 3
                                debug attr 95: adi,fagc-lmt-final-settling-steps value: 1
                                debug attr 96: adi,fagc-lpf-final-settling-steps value: 1
                                debug attr 97: adi,fagc-lock-level-gain-increase-upper-limit value: 5
                                debug attr 98: adi,fagc-lock-level-lmt-gain-increase-enable value: 1
                                debug attr 99: adi,fagc-lp-thresh-increment-steps value: 1
                                debug attr 100: adi,fagc-lp-thresh-increment-time value: 5
                                debug attr 101: adi,fagc-allow-agc-gain-increase-enable value: 0
                                debug attr 102: adi,fagc-state-wait-time-ns value: 260
                                debug attr 103: adi,fagc-dec-pow-measurement-duration value: 64
                                debug attr 104: adi,agc-immed-gain-change-if-large-lmt-overload-enable value: 0
                                debug attr 105: adi,agc-immed-gain-change-if-large-adc-overload-enable value: 0
                                debug attr 106: adi,agc-gain-update-interval-us value: 1000
                                debug attr 107: adi,agc-sync-for-gain-counter-enable value: 0
                                debug attr 108: adi,agc-dig-gain-step-size value: 4
                                debug attr 109: adi,agc-dig-saturation-exceed-counter value: 3
                                debug attr 110: adi,agc-lmt-overload-large-inc-steps value: 2
                                debug attr 111: adi,agc-lmt-overload-small-exceed-counter value: 10
                                debug attr 112: adi,agc-lmt-overload-large-exceed-counter value: 10
                                debug attr 113: adi,agc-adc-lmt-small-overload-prevent-gain-inc-enable value: 0
                                debug attr 114: adi,agc-adc-large-overload-inc-steps value: 2
                                debug attr 115: adi,agc-adc-large-overload-exceed-counter value: 10
                                debug attr 116: adi,agc-adc-small-overload-exceed-counter value: 10
                                debug attr 117: adi,agc-dig-sat-ovrg-enable value: 0
                                debug attr 118: adi,agc-outer-thresh-low-inc-steps value: 2
                                debug attr 119: adi,agc-outer-thresh-low value: 18
                                debug attr 120: adi,agc-inner-thresh-low-inc-steps value: 1
                                debug attr 121: adi,agc-inner-thresh-low value: 12
                                debug attr 122: adi,agc-inner-thresh-high-dec-steps value: 1
                                debug attr 123: adi,agc-inner-thresh-high value: 10
                                debug attr 124: adi,agc-outer-thresh-high-dec-steps value: 2
                                debug attr 125: adi,agc-outer-thresh-high value: 5
                                debug attr 126: adi,agc-attack-delay-extra-margin-us value: 1
                                debug attr 127: adi,mgc-split-table-ctrl-inp-gain-mode value: 0
                                debug attr 128: adi,mgc-dec-gain-step value: 2
                                debug attr 129: adi,mgc-inc-gain-step value: 2
                                debug attr 130: adi,mgc-rx2-ctrl-inp-enable value: 0
                                debug attr 131: adi,mgc-rx1-ctrl-inp-enable value: 0
                                debug attr 132: adi,gc-use-rx-fir-out-for-dec-pwr-meas-enable value: 0
                                debug attr 133: adi,gc-max-dig-gain value: 15
                                debug attr 134: adi,gc-dig-gain-enable value: 0
                                debug attr 135: adi,gc-low-power-thresh value: 24
                                debug attr 136: adi,gc-dec-pow-measurement-duration value: 8192
                                debug attr 137: adi,gc-lmt-overload-low-thresh value: 704
                                debug attr 138: adi,gc-lmt-overload-high-thresh value: 800
                                debug attr 139: adi,gc-adc-large-overload-thresh value: 58
                                debug attr 140: adi,gc-adc-small-overload-thresh value: 47
                                debug attr 141: adi,gc-adc-ovr-sample-size value: 4
                                debug attr 142: adi,gc-rx2-mode value: 2
                                debug attr 143: adi,gc-rx1-mode value: 2
                                debug attr 144: adi,update-tx-gain-in-alert-enable value: 0
                                debug attr 145: adi,tx-attenuation-mdB value: 10000
                                debug attr 146: adi,rf-tx-bandwidth-hz value: 18000000
                                debug attr 147: adi,rf-rx-bandwidth-hz value: 18000000
                                debug attr 148: adi,qec-tracking-slow-mode-enable value: 0
                                debug attr 149: adi,dc-offset-count-low-range value: 50
                                debug attr 150: adi,dc-offset-count-high-range value: 40
                                debug attr 151: adi,dc-offset-attenuation-low-range value: 5
                                debug attr 152: adi,dc-offset-attenuation-high-range value: 6
                                debug attr 153: adi,dc-offset-tracking-update-event-mask value: 5
                                debug attr 154: adi,clk-output-mode-select value: 0
                                debug attr 155: adi,tx-lo-powerdown-managed-enable value: 1
                                debug attr 156: adi,trx-synthesizer-target-fref-overwrite-hz value: 80008000
                                debug attr 157: adi,rx1-rx2-phase-inversion-enable value: 0
                                debug attr 158: adi,tx-rf-port-input-select-lock-enable value: 1
                                debug attr 159: adi,rx-rf-port-input-select-lock-enable value: 1
                                debug attr 160: adi,tx-rf-port-input-select value: 0
                                debug attr 161: adi,rx-rf-port-input-select value: 0
                                debug attr 162: adi,split-gain-table-mode-enable value: 0
                                debug attr 163: adi,1rx-1tx-mode-use-tx-num value: 1
                                debug attr 164: adi,1rx-1tx-mode-use-rx-num value: 1
                                debug attr 165: adi,2rx-2tx-mode-enable value: 0
                                debug attr 166: adi,digital-interface-tune-fir-disable value: 1
                                debug attr 167: adi,digital-interface-tune-skip-mode value: 0
                                debug attr 168: adi,tx-fastlock-pincontrol-enable value: 0
                                debug attr 169: adi,rx-fastlock-pincontrol-enable value: 0
                                debug attr 170: adi,rx-fastlock-delay-ns value: 0
                                debug attr 171: adi,tx-fastlock-delay-ns value: 0
                                debug attr 172: adi,tdd-skip-vco-cal-enable value: 0
                                debug attr 173: adi,tdd-use-dual-synth-mode-enable value: 0
                                debug attr 174: adi,debug-mode-enable value: 0
                                debug attr 175: adi,ensm-enable-txnrx-control-enable value: 0
                                debug attr 176: adi,ensm-enable-pin-pulse-mode-enable value: 0
                                debug attr 177: adi,frequency-division-duplex-independent-mode-enable value: 0
                                debug attr 178: adi,frequency-division-duplex-mode-enable value: 1
                                debug attr 179: direct_reg_access value: 0x0
                No trigger on this device
        iio:device1: xadc
                10 channels found:
                        voltage5: vccoddr (input)
                        3 channel-specific attributes found:
                                attr  0: label value: vccoddr
                                attr  1: raw value: 1824
                                attr  2: scale value: 0.732421875
                        voltage0: vccint (input)
                        3 channel-specific attributes found:
                                attr  0: label value: vccint
                                attr  1: raw value: 1359
                                attr  2: scale value: 0.732421875
                        voltage4: vccpaux (input)
                        3 channel-specific attributes found:
                                attr  0: label value: vccpaux
                                attr  1: raw value: 2441
                                attr  2: scale value: 0.732421875
                        temp0:  (input)
                        3 channel-specific attributes found:
                                attr  0: offset value: -2219
                                attr  1: raw value: 2625
                                attr  2: scale value: 123.040771484
                        voltage7: vrefn (input)
                        3 channel-specific attributes found:
                                attr  0: label value: vrefn
                                attr  1: raw value: -13
                                attr  2: scale value: 0.732421875
                        voltage1: vccaux (input)
                        3 channel-specific attributes found:
                                attr  0: label value: vccaux
                                attr  1: raw value: 2440
                                attr  2: scale value: 0.732421875
                        voltage2: vccbram (input)
                        3 channel-specific attributes found:
                                attr  0: label value: vccbram
                                attr  1: raw value: 1358
                                attr  2: scale value: 0.732421875
                        voltage3: vccpint (input)
                        3 channel-specific attributes found:
                                attr  0: label value: vccpint
                                attr  1: raw value: 1362
                                attr  2: scale value: 0.732421875
                        voltage8:  (input)
                        2 channel-specific attributes found:
                                attr  0: raw value: 3288
                                attr  1: scale value: 0.244140625
                        voltage6: vrefp (input)
                        3 channel-specific attributes found:
                                attr  0: label value: vrefp
                                attr  1: raw value: 1686
                                attr  2: scale value: 0.732421875
                2 device-specific attributes found:
                                attr  0: sampling_frequency value: 961538
                                attr  1: waiting_for_supplier value: 0
                No trigger on this device
        iio:device2: one-bit-adc-dac
                2 channels found:
                        voltage0:  (input)
                        2 channel-specific attributes found:
                                attr  0: label value: muxout
                                attr  1: raw value: 0
                        voltage0:  (output)
                        2 channel-specific attributes found:
                                attr  0: label value: phaser_enable
                                attr  1: raw value: 0
                1 device-specific attributes found:
                                attr  0: waiting_for_supplier value: 0
                No trigger on this device
        iio:device3: cf-ad9361-dds-core-lpc (buffer capable)
                6 channels found:
                        voltage0:  (output, index: 0, format: le:S16/16>>0)
                        4 channel-specific attributes found:
                                attr  0: calibphase value: 0.000000
                                attr  1: calibscale value: 1.000000
                                attr  2: sampling_frequency value: 30720000
                                attr  3: sampling_frequency_available value: 30720000 3840000
                        voltage1:  (output, index: 1, format: le:S16/16>>0)
                        4 channel-specific attributes found:
                                attr  0: calibphase value: 0.000000
                                attr  1: calibscale value: 1.000000
                                attr  2: sampling_frequency value: 30720000
                                attr  3: sampling_frequency_available value: 30720000 3840000
                        altvoltage3: TX1_Q_F2 (output)
                        6 channel-specific attributes found:
                                attr  0: frequency value: 9279985
                                attr  1: label value: TX1_Q_F2
                                attr  2: phase value: 0
                                attr  3: raw value: 1
                                attr  4: sampling_frequency value: 30720000
                                attr  5: scale value: 0.000000
                        altvoltage1: TX1_I_F2 (output)
                        6 channel-specific attributes found:
                                attr  0: frequency value: 9279985
                                attr  1: label value: TX1_I_F2
                                attr  2: phase value: 90000
                                attr  3: raw value: 1
                                attr  4: sampling_frequency value: 30720000
                                attr  5: scale value: 0.000000
                        altvoltage0: TX1_I_F1 (output)
                        6 channel-specific attributes found:
                                attr  0: frequency value: 9279985
                                attr  1: label value: TX1_I_F1
                                attr  2: phase value: 90000
                                attr  3: raw value: 1
                                attr  4: sampling_frequency value: 30720000
                                attr  5: scale value: 0.000000
                        altvoltage2: TX1_Q_F1 (output)
                        6 channel-specific attributes found:
                                attr  0: frequency value: 9279985
                                attr  1: label value: TX1_Q_F1
                                attr  2: phase value: 0
                                attr  3: raw value: 1
                                attr  4: sampling_frequency value: 30720000
                                attr  5: scale value: 0.000000
                3 device-specific attributes found:
                                attr  0: sync_start_enable value: arm
                                attr  1: sync_start_enable_available value: arm
                                attr  2: waiting_for_supplier value: 0
                3 buffer-specific attributes found:
                                attr  0: data_available value: 0
                                attr  1: direction value: out
                                attr  2: length_align_bytes value: 8
                1 debug attributes found:
                                debug attr  0: direct_reg_access value: 0x90262
                No trigger on this device
        iio:device4: cf-ad9361-lpc (buffer capable)
                2 channels found:
                        voltage0:  (input, index: 0, format: le:S12/16>>0)
                        6 channel-specific attributes found:
                                attr  0: calibbias value: 0
                                attr  1: calibphase value: 0.000000
                                attr  2: calibscale value: 1.000000
                                attr  3: samples_pps ERROR: No such device (19)
                                attr  4: sampling_frequency value: 30720000
                                attr  5: sampling_frequency_available value: 30720000 3840000
                        voltage1:  (input, index: 1, format: le:S12/16>>0)
                        6 channel-specific attributes found:
                                attr  0: calibbias value: 0
                                attr  1: calibphase value: 0.000000
                                attr  2: calibscale value: 1.000000
                                attr  3: samples_pps ERROR: No such device (19)
                                attr  4: sampling_frequency value: 30720000
                                attr  5: sampling_frequency_available value: 30720000 3840000
                3 device-specific attributes found:
                                attr  0: sync_start_enable value: disarm
                                attr  1: sync_start_enable_available value: arm
                                attr  2: waiting_for_supplier value: 0
                3 buffer-specific attributes found:
                                attr  0: data_available value: 0
                                attr  1: direction value: in
                                attr  2: length_align_bytes value: 8
                2 debug attributes found:
                                debug attr  0: pseudorandom_err_check value: CH0 : PN9 : Out of Sync : PN Error
CH1 : PN9 : Out of Sync : PN Error
                                debug attr  1: direct_reg_access value: 0x0
                No trigger on this device
        iio:device5: adi-iio-fakedev (label: iio-axi-tdd-0)
                3 channels found:
                        channel2:  (output, WARN:iio_channel_get_type()=UNKNOWN)
                        6 channel-specific attributes found:
                                attr  0: enable value: 0
                                attr  1: off_ms value: 0.000000
                                attr  2: off_raw value: 0
                                attr  3: on_ms value: 0.000000
                                attr  4: on_raw value: 0
                                attr  5: polarity value: 0
                        channel0:  (output, WARN:iio_channel_get_type()=UNKNOWN)
                        6 channel-specific attributes found:
                                attr  0: enable value: 0
                                attr  1: off_ms value: 0.000000
                                attr  2: off_raw value: 0
                                attr  3: on_ms value: 0.000000
                                attr  4: on_raw value: 0
                                attr  5: polarity value: 0
                        channel1:  (output, WARN:iio_channel_get_type()=UNKNOWN)
                        6 channel-specific attributes found:
                                attr  0: enable value: 0
                                attr  1: off_ms value: 0.000000
                                attr  2: off_raw value: 0
                                attr  3: on_ms value: 0.000000
                                attr  4: on_raw value: 0
                                attr  5: polarity value: 0
                18 device-specific attributes found:
                                attr  0: burst_count value: 0
                                attr  1: core_id value: 0
                                attr  2: enable value: 0
                                attr  3: frame_length_ms value: 0.000000
                                attr  4: frame_length_raw value: 0
                                attr  5: internal_sync_period_ms value: 0.000000
                                attr  6: internal_sync_period_raw value: 0
                                attr  7: magic value: 0x5444444e
                                attr  8: scratch value: 0x00000000
                                attr  9: startup_delay_ms value: 0.000000
                                attr 10: startup_delay_raw value: 0
                                attr 11: state value: 0
                                attr 12: sync_external value: 0
                                attr 13: sync_internal value: 0
                                attr 14: sync_reset value: 0
                                attr 15: sync_soft ERROR: Permission denied (13)
                                attr 16: version value: 2.00.b
                                attr 17: waiting_for_supplier value: 0
                No trigger on this device
```

There is a lot to digest above, but key point to note:
 - There are 6 IIO devices found:
    1) iio:device0: ad9361-phy (Main SDR control)
    2) iio:device1: xadc (On chip [Xilinx] low speed ADC)
    3) iio:device2: one-bit-adc-dac (GPIO Devices)
    4) iio:device3: cf-ad9361-dds-core-lpc (DDS Engine, buffer capable)
    5) iio:device4: cf-ad9361-lpc ( Main SDR data, buffer capable)
    6) iio:device5: adi-iio-fakedev (label: iio-axi-tdd-0)
  
Each device has channels and attributes that can be read or written to using the libIIO userspace tools. 

To read the current frequency of the TX_LO channel on the ad9361-phy device, you can use the following command:

```bash 
iio_attr -u ip:192.168.2.1 -c ad9361-phy altvoltage1 frequency
2450000000
```

Lets break that command down:
- `iio_attr`: This is the command-line tool used to read or write attributes of IIO devices.
- `-u ip:192.168.2.1`: This is the context. -u specifies and exact URI.
- `-c ad9361-phy`: This specifies the device.
- `altvoltage1`: This specifies the channel 
- `frequency`: This is the attribute we want to read

To write a value to an attribute, you can use the same command but with the `-w` flag and the value you want to write. For example, to set the frequency of the TX_LO channel to 2.5 GHz, you can use:

```bash
iio_attr -u ip:192.168.2.1 -c ad9361-phy altvoltage1 frequency -w 2500000000
```
This will set the frequency of the TX_LO channel to 2.5 GHz. You can verify that the value has been set correctly by reading the attribute again.

Using the userspace tools is one way to interact with IIO devices. You can also use the system file system to read and write attributes directly.

All the IIO supported IIO devices can be found under `/sys/bus/iio/devices/`. Each device will have a directory named `iio:deviceX` where X is the device number. Inside each device directory, you will find files representing the channels and attributes of that device. You can read and write to these files to interact with the device. For example, to read the frequency of the TX_LO channel on the ad9361-phy device, you can use the following command:    

```bash 
cat /sys/bus/iio/devices/iio:device0/out_altvoltage1_TX_LO_frequency
2450000000
```     
To write a value to the same attribute, you can use:

```bash
echo 2500000000 > /sys/bus/iio/devices/iio:device0/out_altvoltage1_TX_LO_frequency
```

You've seen a couple of examples of how to read and write attributes using both the libIIO tools and the sysfs interface. There are many more attributes available for each device, and you can explore them using the `iio_attr` command or by looking at the files in the sysfs directory.

In the next section, we will look at how to use the libIIO API to interact with the devices programmatically.


```{clear-content}
```
```{note}
For questions or help with the Pluto SDR, please visit:
{ez}`adieducation/university-program`
```
