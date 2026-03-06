Digital Interface Timing Verification
=====================================

.. important::

   Analog Devices uses six designations to inform our customers where a semiconductor product is in its :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`. From emerging innovations to products which have been in production for twenty years, we understand that insight into life cycle status is important. Device life cycles are tracked on their individual product pages on `analog.com <adi>>`__, and should always be consulted before making any design decisions.

   
   This particular articl/edocument/design has been retired or deprecated, which means it is no longer maintained or actively updated, even though the devices themselves may be **Recommended for New Designs** or in **Production**. This page is here for historical/reference purposes only.

 Both the :adi:`AD9122` and the :adi:`AD9643` have very tight FPGA <-> converter digital interface timing requirements. Ensuring that things work over voltage, temperature with different PCB carrier boards is a challenge. To meet this challenge, we use the on-chip verification of both the ADC and the DAC to ensure that good data is sent and received.

The way that this is done is to send a known sequence, and then verify it on the other end. If things don't work, adjust the timing, and try again.

AD9122
------

The AD9122 provides timing verification via it's on-chip sample error detection (SED) circuitry. The SED circuitry compares the input data samples captured at the digital input pins with a set of comparison values loaded over the SPI interface. Differences between the captured values and the comparison values are detected and stored.

The SED circuitry operates on a data set made up of four 16-bit input words, denoted as I0, Q0, I1, and Q1 (loaded over SPI to registers:

-  ``0x68`` I0 LSBs, ``0x69`` I0 MSBs
-  ``0x6A`` Q0 LSBs, ``0x6B`` Q0 MSBs
-  ``0x6C`` I1 LSBs, ``0x6D`` I1 MSBs
-  ``0x6E`` Q1 LSBs, ``0x6F`` Q1 MSBs

The SED has three flag bits (Register 0x67, Bit 5, Bit 1, and Bit 0) that indicate the results of the input sample comparisons. The SED also provides registers that indicate which input data bits experienced errors (Register 0x70 through Register 0x73). These bits are latched and indicate the accumulated errors detected until cleared.

-  ``0x70`` I LSBs ``0x71`` I MSBs SED Errors Detected,
-  ``0x72`` Q LSBs ``0x73`` Q MSBs SED Errors Detected

With this, we can load (over SPI) a predetermined pattern, enable the SED functionality, and then start sending the data over the high speed digital interface. If an error is detected, we know we need to adjust DCI.

"Adjusting DCI" is setting a programmable delay associated with the DCI (Data Clock Input).

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/ad9122_dci.png
   :width: 400px

The delay shifts (delays) the clock with respect to all the data pins. There are four programmable delay options (from 350 ps to 925 ps of delay). This additional delay can be added to improve timing margins in some systems, and we have found is almost always necessary.

Note that this does not resolve data pin to data pin issues. These must still be resolved inside the FPGA.

System level software (in this case the Linux, or no-OS drivers), sets up the SED (in both the HDL and in the DAC) lets it run, and then changes the DCI delay to ensure proper operation.

AD9643
------

The :adi:`AD9643` makes reference to a local Test mode register (0x0D), having the ability to generate a varity of sequences:

-  midscale short
-  positive FS
-  negative FS
-  alternating checkerboard
-  PN long sequence
-  PN short sequence
-  one/zero word toggle

In this case, we normally use one of the PN sequences, which is `LSFR <https://en.wikipedia.org/wiki/Linear_feedback_shift_register>`__ or `PRBS <https://en.wikipedia.org/wiki/Pseudorandom_binary_sequence>`__. Although in :adi:`Application Note 877 <an877>` it indicates that the long PN sequence is a PN23 and the short is PN9, both complying with `ITU 0.150 <http://www.itu.int/rec/T-REC-O.150-199210-S/en>`__, they are not on the AD9643. The actual polynomial is:

:math:`Long == x^16 + x^6`

:math:`Short == x^8 + x^6 + x^0`

The verilog for this is included in the project, in the ``cf_lib\edk\pcores\axi_adc_2c_v1_00_a\hdl\verilog\cf_pnmon.v`` file. We use these sequences to generate a sequence of words that does not repeat, and that we know exactly what it will be. This way, we can verify the proper timing of the digital data from the ADC to the FPGA.

When we find that the data does not match, we adjust the DCO (Data Clock Output) delay of the ADC. There is a SPI register (0x017) which sets a fine delay in the output latch relative to when the internal output registers are strobed. The output latch is changed to compensate for any external setup and hold time issues resulting from ADC/FPGA timing issues. The range of this delay can be between 100 ps and 3200 ps.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/ad9643_dco.png
   :width: 500px

Again, this is done largely in software (Linux and NO-OS). The PN test mode is turned on in both the ADC and inside the HDL, and the software monitors things, until things look robust.

As always - if you have any questions - feel free to ask in the :ez:`support forums <community/fpga>`
