FMComms3 Configuration Options
==============================

The AD-FMCOMMS3 has almost no configuration options for normal use. If you find that this platform does meet your RF performance goals, you should check out the `ad-fmcomms2-ebz <https://wiki.analog.com/../../ad-fmcomms2-ebz>`__ board, which can be tuned with external baluns.

Changing the external clock
---------------------------

The AD-FMCOMMS2-EBZ and AD-FMCOMMS3-EBZ are both clocked from a 40.000000 MHz Epson crystal. If you want to run from a external source, you need to remove Y101, populate C113 (0.1uF Cap), and provide a low jitter clock source into J105 (SMA connector). If you provide anything but a 40.000000 MHz input, you are required to change the ``clock-frequency`` setting in the device tree.

<source /arch/arm/boot/dts/adi-fmcomms2.dtsi:clocks{} c linux/master>

To change the frequency follow `this guide <https://wiki.analog.com/[[/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_2014r2>`__ on how to build the devicetree binary file (make sure you modify the ``clock-frequency`` attribute first.
