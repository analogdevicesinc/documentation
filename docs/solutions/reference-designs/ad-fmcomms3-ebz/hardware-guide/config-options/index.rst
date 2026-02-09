.. _ad-fmcomms3-ebz hardware-guide config-options:

FMCOMMS3 Configuration Options
==============================

The AD-FMCOMMS3 has almost no configuration options for normal use. If
you find that this platform does meet your RF performance goals, you
should check out the
:dokuwiki:`ad-fmcomms2-ebz <resources/eval/user-guides/ad-fmcomms2-ebz>`
board, which can be tuned with external baluns.

Changing the external clock
---------------------------

The :adi:`AD-FMCOMMS2-EBZ` and :adi:`AD-FMCOMMS3-EBZ` are both 
clocked from a 40.000000 MHz Epson crystal. If you want to run from 
a external source, you need to remove Y101, populate C113 (0.1uF Cap),
and provide a low jitter clock source into J105 (SMA connector). If 
you provide anything but a 40.000000 MHz input, you are required to 
change the ``clock-frequency`` setting in the device tree.

<source /arch/arm/boot/dts/adi-fmcomms2.dtsi:clocks{} c linux/master>

To change the frequency follow 
:dokuwiki:`this guide <resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_2014r2#build_the_devicetree_fcmomms2345>`
on how to build the devicetree binary file (make sure you modify the
``clock-frequency`` attribute first.)
