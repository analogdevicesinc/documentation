AD-FMComms1-EBZ : Using the reference design
============================================

.. important::

   Analog Devices uses six designations to inform our customers where a semiconductor product is in its :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`. From emerging innovations to products which have been in production for twenty years, we understand that insight into life cycle status is important. Device life cycles are tracked on their individual product pages on `analog.com <adi>>`__, and should always be consulted before making any design decisions.

   
   This particular articl/edocument/design has been retired or deprecated, which means it is no longer maintained or actively updated, even though the devices themselves may be **Recommended for New Designs** or in **Production**. This page is here for historical/reference purposes only.



The reference design is a combination of hardware (the FMComms1 Card + the FPGA base platform), the HDL, and the software that is either running on the Microblaze, or ARM Cores.

In all the demos that we support, Linux is a large piece.

Linux Device Drivers
--------------------

-  :doc:`AD9523-1: Low Jitter Clock Generator with 14 LVPECL/LVDS/HSTL/29 LVCMOS Outputs </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ad9523>`
-  :doc:`ADF4351: Wideband Synthesizer with Integrated VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf4350>`
-  :doc:`AD8366: DC to 600 MHz, Dual-Digital Variable Gain Amplifiers </wiki-migration/resources/tools-software/linux-drivers/iio-amplifiers/ad8366>`
-  :doc:`AD9643: 14-Bit, 170/210/250 MSPS, 1.8 V Dual Analog-to-Digital Converter (ADC) </wiki-migration/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
-  :doc:`AD9122: Dual, 16-Bit, 1200 MSPS, TxDAC+® Digital-to-Analog Converter </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`

Booting Linux
-------------

Normally, when the Linux image is booted, it will search both the LPC and HPC FMC slots for 2 cards. (the same reference design supports MIMO, as a single card). You should see something like this in the kernel log message - which indicates that a single card is plugged into the LPC FMC connector.

::

   # **dmesg**
   [snip]
   at24 0-0051: 256 byte 24c02 EEPROM, writable, 1 bytes/write
   spi-xcomm: probe of 1-0058 failed with error -5
   at24 1-0050: 256 byte 24c02 EEPROM, writable, 1 bytes/write
   cf_axi_adc 7c820000.cf-ad9643-core-lpc: Device Tree Probing 'cf-ad9643-core-lpc'
   platform 7c820000.cf-ad9643-core-lpc: Driver cf_axi_adc requests probe deferral
   cf_axi_adc 7c800000.cf-ad9643-core-hpc: Device Tree Probing 'cf-ad9643-core-hpc'
   platform 7c800000.cf-ad9643-core-hpc: Driver cf_axi_adc requests probe deferral
   **cf_axi_fft_core 7ee00000.axi-fft: Device Tree Probing 'axi-fft'**
   **cf_axi_fft_core 7ee00000.axi-fft: ADI-FFT (0x10061) at 0x7EE00000 mapped to 0xf0160000, DMA-1, DMA-0 probed**
   **ad9548 spi0.2: Rev. 0xC6 probed**
   **ad9523 spi0.3: probed ad9523-lpc**
   cf_axi_dds 7a020000.cf-ad9122-core-lpc: Device Tree Probing 'cf-ad9122-core-lpc'
   platform 7a020000.cf-ad9122-core-lpc: Driver cf_axi_dds requests probe deferral
   cf_axi_dds 7a000000.cf-ad9122-core-hpc: Device Tree Probing 'cf-ad9122-core-hpc'
   platform 7a000000.cf-ad9122-core-hpc: Driver cf_axi_dds requests probe deferral
   TCP: cubic registered
   NET: Registered protocol family 17
   **cf_axi_adc 7c820000.cf-ad9643-core-lpc: Device Tree Probing 'cf-ad9643-core-lpc'**
   **-------ooooooooooo|oooooooooo---- DCO 0x91**
   **cf_axi_adc 7c820000.cf-ad9643-core-lpc: ADI AIM (0x10061) at 0x7C820000 mapped to 0xf0180000, DMA-0 probed ADC AD9643 as MASTER**
   cf_axi_adc 7c800000.cf-ad9643-core-hpc: Device Tree Probing 'cf-ad9643-core-hpc'
   platform 7c800000.cf-ad9643-core-hpc: Driver cf_axi_adc requests probe deferral
   **cf_axi_dds 7a020000.cf-ad9122-core-lpc: Device Tree Probing 'cf-ad9122-core-lpc'**
   **-o|o DCI 2**
   **cf_axi_dds 7a020000.cf-ad9122-core-lpc: Analog Devices CF_AXI_DDS_DDS MASTER (0x10061) at 0x7A020000 mapped to 0xf01a0000, probed DDS AD9122**
   cf_axi_dds 7a000000.cf-ad9122-core-hpc: Device Tree Probing 'cf-ad9122-core-hpc'
   platform 7a000000.cf-ad9122-core-hpc: Driver cf_axi_dds requests probe deferral
   cf_axi_adc 7c800000.cf-ad9643-core-hpc: Device Tree Probing 'cf-ad9643-core-hpc'
   platform 7c800000.cf-ad9643-core-hpc: Driver cf_axi_adc requests probe deferral
   cf_axi_dds 7a000000.cf-ad9122-core-hpc: Device Tree Probing 'cf-ad9122-core-hpc'
   platform 7a000000.cf-ad9122-core-hpc: Driver cf_axi_dds requests probe deferral
   cf_axi_adc 7c800000.cf-ad9643-core-hpc: Device Tree Probing 'cf-ad9643-core-hpc'
   platform 7c800000.cf-ad9643-core-hpc: Driver cf_axi_adc requests probe deferral

You can also check the status of things with:

::

   # **cd /sys/bus/iio/devices/**
   # **grep "" iio\:device*/name**
   iio:device0/name:ad8366-lpc
   iio:device1/name:ad9523-lpc
   iio:device2/name:adf4351-rx-lpc
   iio:device3/name:adf4351-tx-lpc
   iio:device4/name:cf-ad9643-core-lpc
   iio:device5/name:cf-ad9122-core-lp

Those are the devices that the Linux kernel found.

Running the demo
----------------

It's a simple matter of configuring the ethernet on the FPGA platform:

::

   # **ifconfig eth0 192.168.1.2 up**
   # **ifconfig eth0**
   eth0      Link encap:Ethernet  HWaddr 00:0A:35:69:1C:00  
             inet addr:192.168.1.2  Bcast:192.168.1.255  Mask:255.255.255.0
             UP BROADCAST RUNNING  MTU:1500  Metric:1
             RX packets:11 errors:0 dropped:0 overruns:0 frame:0
             TX packets:1 errors:0 dropped:0 overruns:0 carrier:0
             collisions:0 txqueuelen:1000 
             RX bytes:3506 (3.4 KiB)  TX bytes:322 (322.0 B)
             Interrupt:10 Memory:40e00000-40e0ffff 

(or by running the udhcpc client)

and then ensuring that the your host PC is attached to the same subnet as the FPGA platform.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/scope.png
   :width: 400px

From here you can look at things in the time domain, frequency domain, and control the various "knobs" in the platform.

To find the various "knobs", they are in the ``sysfs`` directory.

::

   # **cd /sys/devices/axi.0/40800000.i2c/i2c-0/0-0059/spi_master/spi0/spi0.3/iio:device2**
   # **ls**
   dev
   name
   out_altvoltage0_ZD_OUTPUT_frequency
   out_altvoltage0_ZD_OUTPUT_phase
   out_altvoltage0_ZD_OUTPUT_raw
   out_altvoltage0_clk_src_vcxo_en
   out_altvoltage1_DAC_CLK_frequency
   out_altvoltage1_DAC_CLK_phase
   out_altvoltage1_DAC_CLK_raw
   out_altvoltage1_clk_src_vcxo_en
   out_altvoltage2_ADC_CLK_frequency
   out_altvoltage2_ADC_CLK_phase
   out_altvoltage2_ADC_CLK_raw
   out_altvoltage2_clk_src_vcxo_en
   out_altvoltage3_clk_src_vcxo_en
   out_altvoltage4_DAC_REF_CLK_frequency
   out_altvoltage4_DAC_REF_CLK_phase
   out_altvoltage4_DAC_REF_CLK_raw
   out_altvoltage4_clk_src_vco2_en
   out_altvoltage5_TX_LO_REF_CLK_frequency
   out_altvoltage5_TX_LO_REF_CLK_phase
   out_altvoltage5_TX_LO_REF_CLK_raw
   out_altvoltage5_clk_src_vco2_en
   out_altvoltage6_DAC_DCO_CLK_frequency
   out_altvoltage6_DAC_DCO_CLK_phase
   out_altvoltage6_DAC_DCO_CLK_raw
   out_altvoltage6_clk_src_vco2_en
   out_altvoltage7_clk_src_vco2_en
   out_altvoltage8_ADC_SYNC_CLK_frequency
   out_altvoltage8_ADC_SYNC_CLK_phase
   out_altvoltage8_ADC_SYNC_CLK_raw
   out_altvoltage8_clk_src_vco2_en
   out_altvoltage9_RX_LO_REF_CLK_frequency
   out_altvoltage9_RX_LO_REF_CLK_phase
   out_altvoltage9_RX_LO_REF_CLK_raw
   out_altvoltage9_clk_src_vco2_en
   status
   store_eeprom
   subsystem
   sync
   uevent
   vco1_frequency
   vco2_frequency
   vco_frequency_available

You can ``echo`` or ``cat`` into these files to change the various options.

::

   # **cat out_altvoltage1_DAC_CLK_frequency**
   491520000
   # **echo 500000000 > out_altvoltage1_DAC_CLK_frequency**
   # **cat out_altvoltage1_DAC_CLK_frequency**
   983040000
   # **echo 400000000 > out_altvoltage1_DAC_CLK_frequency**
   # **cat out_altvoltage1_DAC_CLK_frequency**
   491520000

Just like if you were trying to program the part with specific frequencies, there are only so many options you can pick, so it attempts to pick the "closest" option.

FMC FRU EEPROM Utility
----------------------

The FRU EEPROM responds to I2C Slave address 0x51.

Dump FRU Board Information
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      # **fru_dump -i /sys/bus/i2c/devices/0-0051/eeprom -b**
      read 256 bytes from /sys/bus/i2c/devices/0-0051/eeprom
      Date of Man  : Tue Sep 18 16:30:00 2012
      Manufacture  : Analog Devices
      Product Name : FMC Comms 1
      Serial Number: D836081
      Part Number  : AD-FMCOMMS1-EBZ
      Board Rev    : B
   


Dump FRU Power Information
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      # **fru_dump -i /sys/bus/i2c/devices/0-0051/eeprom -p**
      read 256 bytes from /sys/bus/i2c/devices/0-0051/eeprom
      DC Load
        Output number: 0 (P1 VADJ)
        Nominal Volts:         2500 (mV)
        minimum voltage:       1800 (mV)
        maximum voltage:       2500 (mV)
        Ripple and Noise pk-pk 0000 (mV)
        Minimum current load   0000 (mA)
        Maximum current load   0000 (mA)
      DC Load
        Output number: 1 (P1 3P3V)
        Nominal Volts:         3300 (mV)
        minimum voltage:       2970 (mV)
        maximum voltage:       3630 (mV)
        Ripple and Noise pk-pk 0000 (mV)
        Minimum current load   0000 (mA)
        Maximum current load   3000 (mA)
      DC Load
        Output number: 2 (P1 12P0V)
        Nominal Volts:         12000 (mV)
        minimum voltage:       10800 (mV)
        maximum voltage:       13200 (mV)
        Ripple and Noise pk-pk 0000 (mV)
        Minimum current load   0000 (mA)
        Maximum current load   1000 (mA)
      DC Output
        Output Number: 3 (P1 VIO_B_M2C)
        Nominal volts:              0 (mV)
        Maximum negative deviation: 0 (mV)
        Maximum positive deviation: 0 (mV)
        Ripple and Noise pk-pk:     0 (mV)
        Minimum current draw:       0 (mA)
        Maximum current draw:       0 (mA)
      DC Output
        Output Number: 4 (P1 VREF_A_M2C)
        Nominal volts:              0 (mV)
        Maximum negative deviation: 0 (mV)
        Maximum positive deviation: 0 (mV)
        Ripple and Noise pk-pk:     0 (mV)
        Minimum current draw:       0 (mA)
        Maximum current draw:       0 (mA)
      DC Output
        Output Number: 5 (P1 VREF_B_M2C)
        Nominal volts:              0 (mV)
        Maximum negative deviation: 0 (mV)
        Maximum positive deviation: 0 (mV)
        Ripple and Noise pk-pk:     0 (mV)
        Minimum current draw:       0 (mA)
        Maximum current draw:       0 (mA)
   


Dump FRU Connector Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      # **fru_dump -i /sys/bus/i2c/devices/0-0051/eeprom -c**
      read 256 bytes from /sys/bus/i2c/devices/0-0051/eeprom
      Single Width Card
      P1 is LPC
      P1 Bank A Signals needed 68
      P1 Bank B Signals needed 0
      P1 GBT Transceivers needed 0
      Max JTAG Clock 0
   


AD-FMCOMMS1-EBZ Calibration EEPROM Utility
------------------------------------------

The Calibration EEPROM responds to I2C Slave address 0x55.

Query best match calibration set for a given Frequency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      # **xcomm_cal -f 2400 -s /sys/bus/i2c/devices/0-0055/eeprom**
   
      --- Best match ENTRY 1 ---
      Calibration Frequency:  2400 MHz
      DAC I Phase Adjust:             357
      DAC Q Phase Adjust:             0
      DAC I Offset:           214
      DAC Q Offset:           25
      DAC I Full Scale Adj:   401
      DAC Q Full Scale Adj:   401
      ADC I Offset:           -2
      ADC Q Offset:           -34
      ADC I Gain Adj: 32853
      ADC Q Gain Adj: 32768
   

