HowTo: observe the FM band with an AD9361-equipped board
========================================================

About FM radio
--------------

**FM band:**

-  In Europe and Africa: 87.5 MHz to 107.9 MHz
-  In America: 87.9 MHz to 107.9 MHz
-  In Japan: 76.0 MHz to 90 MHz

**FM channels:**

-  either 200 kHz wide, with a frequency deviation limited to 150 kHz total,
-  or 100 kHz wide, with a frequency deviation limited to 75 KHz total.

The sysfs interface
-------------------

It is possible to configure the AD9361 chip directly from sysfs. The interesting files are located in **/sys/bus/iio/devices/iio:deviceX** where X is the number of the device whose name is **ad9361-phy**:

::

   root@linaro-ubuntu-desktop:~# cat /sys/bus/iio/devices/iio:device1/name
   ad9361-phy

This directory contains several files, some of which can be used to read raw values from the hardware, while others are used to configure the ad9361 chip.

::

   root@linaro-ubuntu-desktop:~# ls /sys/bus/iio/devices/iio:device1
   calib_mode                              in_voltage_rf_dc_offset_tracking_en
   calib_mode_available                    in_voltage_rf_port_select_available
   dcxo_tune_coarse                        in_voltage_sampling_frequency
   dcxo_tune_fine                          name
   dev                                     out_altvoltage0_RX_LO_frequency
   ensm_mode                               out_altvoltage1_TX_LO_frequency
   ensm_mode_available                     out_voltage0_hardwaregain
   filter_fir_config                       out_voltage0_rf_port_select
   in_out_voltage_filter_fir_en            out_voltage1_hardwaregain
   in_temp0_input                          out_voltage1_rf_port_select
   in_voltage0_gain_control_mode           out_voltage2_raw
   in_voltage0_hardwaregain                out_voltage2_scale
   in_voltage0_rf_port_select              out_voltage3_raw
   in_voltage0_rssi                        out_voltage3_scale
   in_voltage1_gain_control_mode           out_voltage_filter_fir_en
   in_voltage1_hardwaregain                out_voltage_rf_bandwidth
   in_voltage1_rf_port_select              out_voltage_rf_port_select_available
   in_voltage1_rssi                        out_voltage_sampling_frequency
   in_voltage2_offset                      power
   in_voltage2_raw                         rx_path_rates
   in_voltage2_scale                       subsystem
   in_voltage_bb_dc_offset_tracking_en     trx_rate_governor
   in_voltage_filter_fir_en                trx_rate_governor_available
   in_voltage_gain_control_mode_available  tx_path_rates
   in_voltage_quadrature_tracking_en       uevent
   in_voltage_rf_bandwidth

The program we will use, :doc:`IIO Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`, use the sysfs interface to configure the ad9361, and use the special character device /dev/iio:device1 to read the raw values.

Equipment used
--------------

This test has been realized with a `Zed board <http://zedboard.org/content/overview>`_, coupled with a :adi:`ad-fmcomms3-ebz` module.

.. image:: https://wiki.analog.com/_media/resources/tools-software/board2.jpg
   :width: 300px

Monitoring the FM band
----------------------

We will monitor the most used FM band, from 87.5 MHz to 107.9 MHz. The :doc:`IIO Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>` can be configured like this:

.. image:: https://wiki.analog.com/_media/resources/tools-software/capture4.png
   :width: 300px

-  **RX LO Frequency**: the base frequency at which the hardware will be tuned. Set to 87.4 MHz (and not 87.5, since 87.5 is the middle of a 200 KHz channel);
-  **RF Baudwidth**: the size of the band you want to capture. Here, we want at least a band of 107.9 - 87.5 = 20.4 MHz
-  **Sampling rate**: the number of samples you want to capture (in millions per second). Here we set this to 22, so that we get a resolution of approximatively one hertz.

Lanch a capture, and you will be able to see peaks in the frequency domain:

.. image:: https://wiki.analog.com/_media/resources/tools-software/capture3.png
   :width: 300px

In this screenshot, it is clearly possible to identify several channels: at 95.5 MHz, 96.3 MHz, 97.5 MHz, 98.4 MHz among other frequencies.

Playback
--------

To verify if those frequencies actually correspond to something, we can use the **iio_fm_radio** tool. But first, it is necessary to change the gain control:

::

   echo fast_attack > /sys/bus/iio/devices/iio:device1/in_voltage1_gain_control_mode

Then, the **iio_fm_radio_play** tool will playback the desired channel on the speaker of the HDMI monitor:

::

   iio_fm_radio_play 95.5

To directly get access to the audio waveform data the **iio_fm_radio** tool can be used. This tool outputs the audio data (in 16-bit mono at 48kHz) on standard output from where it can be taken and further processed. E.g. the following command plays back the stream on the headphone jack of the ZED board.

::

   iio_fm_radio 95.5 | aplay -D default:CARD=ADAU1761 -r 48000 -f S16
