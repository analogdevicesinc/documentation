.. _jupiter-sdr knownissues:

Jupiter SDR - known issues
==========================

Jupiter SDR known issues when used with 
:dokuwiki:`2023_r2 Patch1 Kuiper image: <resources/tools-software/linux-software/adi-kuiper_images/release_notes>`

#. IIO buffer size limited to 131072 samples when USB 3 interface is
   used to stream data to a host

#. USB 3 and Gigabit Ethernet interfaces throughput is currently limited
   by 
   :dokuwiki:`libiio v0.26 <resources/eval/user-guides/ad-fmcdaq2-ebz/software/linux/applications/libiio>`
   implementation. The throughputs will significantly improve once
   libiio v1.0 will be realeaed.

#. IIO Oscilloscope profile generator (latest libadrv9002-iio) supports
   v68.10.1 API while 2023_r3 Patch1 comes with v68.14.10 API; 
   :dokuwiki:`Generate a custom device profile using TES <resources/eval/user-guides/jupiter-sdr/profile_generation_using_tes>`

#. Multi chip synchronization support is not included in the 2023_r2
   Patch1 Kuiper release. Please visit 
   :dokuwiki:`multi-chip synchronization page <resources/eval/user-guides/jupiter_sdr/mcs>`
   to check available support.

#. :adi:`ADRV9002` CMOS interface not implemented
