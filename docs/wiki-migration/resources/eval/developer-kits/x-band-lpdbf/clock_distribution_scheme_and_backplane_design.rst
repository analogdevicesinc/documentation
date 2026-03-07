Clock Distribution Scheme and Backplane Design
==============================================

Overview
--------

One of the main features of the Marlin platform is the ability to operate up to 8 tiles synchronously with one FPGA. This operation comes with many challenges, as the :adi:`AD9106`, :adi:`AD9083`, and :adi:`ADF5356` all operate on different reference clock frequency levels. Therefore, care has to be taken to make sure all clock signals to like chips are distributed appropriately across each tile to ensure signal integrity, isolation, and noise reduction. A combination of fanout buffers and clock distributors are used to create a scheme for single-tile and multi-tile use.

Key IC: LTC6953
---------------

The key IC that enables the clock distribution scheme for the Marlin platform is the :adi:`LTC6953`. This chip is a high performance, ultralow jitter, JESD204B/C clock distribution IC. It has the ability to output up to 11 general purpose clock outputs or 5 JESD204B/C subclass 1 device clock/SYSREF pairs plus 1 general purpose output. The LTC6953 comes with :adi:`EZSync <media/en/technical-documentation/product-selector-card/4pb_clocking.pdf>` or ParallelSync capabilities, which allow for multi-device synchronization. The Marlin platform utilizes an adaptation of the ParallelSync Multichip Synchronization scheme that is outlined in pages 20-21 of the part :adi:`datasheet <media/en/technical-documentation/data-sheets/ltc6953.pdf>`.

In the ParallelSync Multichip Synchronization scheme, two distributors are used to distribute the reference clock signal and EZS_SRQ signals, respectively. The frequency of the LTC6953 output clock signals are dictated by the frequency of the reference clock, which in the case of Marlin is 250 MHz provided from an external signal generator. The output signals from the LTC6953 can therefore be any divisor of 250 MHz. The :adi:`AD9083` supports multi-devices synchronization through the differential SYSREF, TRIG, and SYNCINB input pins, which are all sent by the LTC6953.

The clock signals necessary for each chip vary based on the part specifications. Below is a table that contains the frequencies of the necessary clock signals for each part.

Clock Distribution Scheme
-------------------------

Before delving into multi-tile clock distribution, it is important to establish clock distribution to the different chips on the tile itself. Below is a block diagram illustrating the distribution of clock signals within one tile.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_singletileclocking.png
   :width: 600px

**Figure 1: Single Tile Clock Distribution**

The on-tile LTC6953 takes in a 250 MHz reference clock signal from an external signal generator. When being operated in single-tile mode, the LTC6953 supplies the SYSREF, JRXJESD, and REFCLK signals directly to the FPGA. The AD9083 requires the SYSREF, TRIG, and SYNCINB signals to operate in multi-chip synchronization, and so those signals are sent to the chip from the on-tile LTC6953. Additionally, all of the follower chips (AD9106, AD9083, and ADF5356) need a reference clock signal which are all sent directly sent from the on-tile LTC6953 as well. Note that all the frequencies are a divisor of 250 MHz, which is the reference clock signal that is sent to the LTC6953 from the external signal generator. This is to abide with the reference distribution divider and DDEL settings for ParallelSync that are listed in Table 9 on page 21 of the part datasheet. One advantage of the LTC6953 is that in SYSREF generation mode, there are methods via control bits to shutdown as much circuitry as possible while maintaining the correct timing relationship between the SYSREF outputs and the clock outputs. The ParallelSync configuration also allows for improved jitter performance when devices are cascaded. The tighter restrictions with the control of the REF and EZS_SRQ signals that are mentioned in the datasheet are accounted for in the backplane clock scheme. Below is the block diagram illustrating the backplane clock distribution scheme for multi-tile enablement.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_multitileclocking.png
   :width: 600px

**Figure 2: Multi-tile Clock Distribution Scheme**

The reference clocks signals to each tile have to be synchronized. To do this, an EZSync signal must be utilized. The EZSync signal is sent from the FPGA to the first of 2 backplane LTC6953 chips. This signal ensures that all reference clock signals are synchronized, both to all eight tiles as well as the backplane :adi:`ADCLK854`, which distributes the SYSREF request (EZS_SRQ) to all eight tiles.

The ADCLK854 is a low-power clock fanout buffer capable of up to 12 LVDS (1.2GHz) or 24 CMOS (250MHz) signal outputs. This chip is used in three places in the multi-tile clocking scheme. The first use is for distributing the EZS_SRQ signals as mentioned before. The EZS_SRQ signals are distributed all eight tiles and also to the second backplane LTC6953 which interfaces with the FPGA. The other two uses of the ADCLK854 are for supplying the TRIG and SYNCINB signals that are distributed to the on-tile AD9083 chips straight from the FPGA. Using the clock buffer for distribution of these signals allows for isolation and reduces any chance of compromising signal integrity.

The second LTC6953 takes in the REFCLK and EZS_SRQ signals from the respective clock distribution chips and sends the JRXJESD, REFCLK, and SYSREF signals to the FPGA.

All in all, the clock distribution scheme is designed to enable the user to utilize both single-tile and multi-tile functionalities. It is essential for the successful operation of the platform and has been optimized to consume the least power possible as well.
