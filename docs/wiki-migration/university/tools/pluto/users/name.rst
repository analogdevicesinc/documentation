Why "Pluto"
===========

Just like `Pluto <https://en.wikipedia.org/wiki/Pluto>`__ (the celestial body) is a `Dwarf Planet <https://en.wikipedia.org/wiki/Dwarf_planet>`__, (resembling a small planet but lacking certain technical criteria that are required for it to be classed as such), the PlutoSDR is an active learning module resembling a `software defined radio <https://en.wikipedia.org/wiki/Software-defined_radio>`__, but it lacks some of the the performance/technical criteria for it to be classified as such (in our opinion).

While it is a great learning tool for the first experience of a communications class, or SDR class, the PlutoSDR is not meant as a replacement or an alternative for various professional Software Defined Radios (SDR) that are available (some of which are listed `online <https://en.wikipedia.org/wiki/List_of_software-defined_radios>`__) - it was designed to provide RF/SDR functionality for students, and hit a price point affordable for students [1]_; as a result - there are limitations to the PlutoSDR that every user should be aware of, to understand and ensure they can work around them.

System Issues
-------------

Temperature Range
-----------------

The temperature range that the PlutoSDR has been tested in is 10°C to 40°C. While this is nominal for classrooms world wide - it is not robust enough for units to be used in a commercial setting, where temperature extremes are often found. This is more of an issue of the system level design, the case, and the qualification that was done. The devices that are inside the PlutoSDR are typically specified for 0°C to 70°C, or −40°C to +85°C.

This can easily be overcome with more verification, and ensuring that all parts meet the temperature specifications of the particular application.

Digital Issues
--------------

USB 2.0
~~~~~~~

`USB 2.0 <https://en.wikipedia.org/wiki/USB#USB_2.0>`__ is a 480 Mb/s half-duplex serial protocol.

-  Assuming 100% utilization, 480 Mb/s would be 60 MB/s.
-  According to a USB-IF chairman, "*at least 10-15% of the stated peak 60 MB/s (480 Mb/s) of Hi-Speed USB goes to overhead — the communication protocol between the card and the peripheral.*"  [2]_, that would bring things down to ~50 MB/s.
-  There are Control Transfers, Interrupt Transfers, Isochronous Transfers, and Bulk Transfers. We use bulk, but you can't turn off the others, so you loose another 10% overhead, this brings things down to ~45 MB/s.
-  Since it is half duplex, that would be ~22.5 MB/s for transmission, and ~22.5 MB/s for reception.
-  Since each sample is two bytes (12-bit samples), that would be ~11 MSPS.

What we actually achieve with the PlutoSDR is closer to 7.5 - 12 MSPS, but this depends on the USB host, and what other traffic is happening. This is about 65% to 100% of the theoretical rate, meaning that most depends on the host, but there still may be optimizations to be done. This is much slower than Gigabit or 10G Ethernet, USB 3.0 (5 Gbps, full duplex) or PCIe (4 Gbps per lane) solutions, which are available in various commercial offerings.

USB 2.0 could easily be upgraded to a different interface, (with additional devices) depending on what the specific application needs.

However, it should be noted that the PlutoSDR has alot of internal memory (512MBytes), which can be used to locally store data. For example with 128 MB (32 MSamples), at a data rate of 30.72 MSPS (LTE20), that can store 1.04166 Seconds of RF information. Since LTE frame has an overall length of 10 ms, that would be 104 frames. If you are interested in understanding LTE, and creating your own decoder, 100+ continuous frames is plenty for that exercise. This is known as burst mode.

Burst mode enables you to buffer a set of contiguous samples without losing samples inside a burst. This forces lost samples to be between bursts. Since you can control the length of the burst this also controls the latency in the system.

FPGA Size
~~~~~~~~~

The FPGA inside the PlutoSDR (as part of the Xilinx Zynq 7010) is quite small.

=============== ====
Attribute       size
=============== ====
Logic Cells (K) 28
Block RAM (Mb)  2.1
DSP Slices      80
=============== ====

The default design, which uses some of the FPGA for :

-  implementation of the CMOS interface
-  I/Q rotation (if you need it)
-  DDS (for multi-tone generation on the transmit side), and
-  an additional by 8 interpolation/decimation so the sample rate of the PlutoSDR can be 8 times lower (65.104166 kSPS) than the minimum sample rate of the AD9363 (520.833kSPS) [3]_.

A typical utilization report is below. If you do not need some of the above logic, it can be turned off, and you can re-use the FPGA for your custom logic.

.. image:: https://wiki.analog.com/_media/pluto_utilization.jpg
   :alt: pluto_utilization.jpg
   :align: center
   :width: 425px
   :height: 337px

The additional decimation and interpolation filters use 20 DSP slices each (40 in total). The optional DDS uses 20 DSP slices, and the optional 2 x 2 matrix multiply (sometimes used for IQ correction, or phase rotation) are 2 per channel, and the DC filter is 1 per channel.

This can easily be overcome by using a different `Zynq <https://www.xilinx.com//support/documentation/selection-guides/zynq-7000-product-selection-guide.pdf>`__ device - we picked the one in the smallest pin count, to make layout easier, to hit the price point we needed. Going to a larger device, larger package, will impact size, and cost.

RF Issues
---------

Oscillator
~~~~~~~~~~

The oscillator on the PlutoSDR is a specific version of the Rakon RXO3225M 40.000 MHz (Custom PN : :ez:`509336 <cfs-file/__key/telligent-evolution-components-attachments/00-323-00-00-00-03-22-63/attachment.pdf>`, :ez:`thread <fpga/f/q-a/86600/what-is-the-crystal-used-on-the-ad-fmcomms5-ebz>`) that meets the jitter requirements of the AD936x family. However, it has a frequency stability of ±25 ppm (voltage, temperature, drift plus initial accuracy).

You may think that this is really bad (and it is), but:

-  it can be corrected digitally by programming the XO frequency. If you notice that it is 39.987654 MHz (down to Hz resolution), you can tell the system this, and the LO frequency and sample rates will be updated to reflect this. By monitoring this frequency offset, this can be updated on the fly.
-  most receivers do have a frequency compensation correction algorithm, since the remote transmitter is not likely to be the same as your local device anyway - you just need to make sure your compensation algorithm can cope with a wide number.
-  loopback, being your own transmitter and receiver - the offsets in frequency and sample rates will be the same on both channels of a single device. It should be noted - there still will be random phase offsets between the Tx and Rx LOs, but they should be exactly the same frequency.

This can easily be overcome by using a different oscillator (which may impact cost).

Tuning Range
~~~~~~~~~~~~

The tuning range of the :adi:`AD9363` found inside the PlutoSDR is specified by LO center frequencies between 325 and 3800 MHz. While this is more than a decade of tuning range, and does cover many interesting bands in the `US <https://www.ntia.doc.gov/files/ntia/publications/january_2016_spectrum_wall_chart.pdf>`__, `Europe <https://docdb.cept.org/download/3543>`__, `Australia <http://www.acma.gov.au/webwr/radcomm/frequency_planning/spectrum_plan/aust_rf_spectrum_plan.doc>`__, `Japan <http://www.tele.soumu.go.jp/e/adm/freq/search/share/plan.htm>`__ it's not quite as broad as the :adi:`AD9361` or :adi:`AD9364` which has a tuning range of 70 to 6000 MHz, nearly two decades!

This can easily be overcome by swapping the AD9363 to the AD9364 or the AD9361, as the pinouts of the devices are nearly identical, but it will impact cost. Some users have noted success in :doc:`telling the PlutoSDR </wiki-migration/university/tools/pluto/users/customizing>` it has a AD9364 inside, which seems to work.

RF Shielding
~~~~~~~~~~~~

There is no RF shielding inside the PlutoSDR. That means placing a strong transmitter close to it (like your cellphone) may impact the results for any frequency that the PlutoSDR is tuned to.

This can easily be overcome by adding RF shielding, but it would impact cost, and size.

RF Filtering
~~~~~~~~~~~~

There is no preselect, or output filters on the PlutoSDR. What comes out of the AD9363 is what comes out of the SMA connector. What comes into the antenna is what is provided to the AD9363 pins.

The RF transmitter in the AD9363 does output a moderate 3rd harmonic of the LO frequency. This will be fairly low if your LO is at 3 GHz (where the 3rd harmonic would be 9 GHz, outside the range of the balun used for the differential to single ended conversion in the PlutoSDR). However - if the LO is at 500 MHz, the third harmonic would be 1500 MHz, entirely within the range. If you are transmitting an RF signal at 500 MHz, you will also (inadvertently) be broadcasting at 1500 MHz as well.

This can easily be overcome by adding specific preselect or output filters. Depending on the tuning range you want to do, it can complicate things pretty drastically, and also depends what sort of antenna you are using. (Antennas are also filters).

RF Performance
~~~~~~~~~~~~~~

While the RF performance of the :adi:`AD9363` is adequate for many RF applications, it does not match the specifications from other higher performance devices, like the :adi:`AD9361`, :adi:`AD9364`, :adi:`AD9371` which are found in other commercial SDR devices.

The PlutoSDR does exceed the performance of many devices in the same class, but is not meant to be the best SDR possible.

We do exceed the datasheet specifications on the devices we have tested, and this should not be an issue for many applications.

.. [1]
   less than a price of a good texbook

.. [2]
   `USB#Transmission_rates <https://en.wikipedia.org/wiki/USB#Transmission_rates>`__

.. [3]
   minimum sample rate of the AD9363 ADC is 25 MSPS, the max decimation factor is 48 (3 \* 2 \* 2 \* 4) 48; 25 MSPS ÷ 48 is 520833.33 SPS
