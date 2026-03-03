.. _jupiter-sdr known-issues:

Jupiter SDR - known issues
==========================

Jupiter SDR known issues when used with
:external+adi-kuiper-gen:doc:`2023_r2 Patch1 Kuiper image <index>`

#. IIO buffer size limited to 131072 samples when USB 3 interface is
   used to stream data to a host

#. USB 3 and Gigabit Ethernet interfaces throughput is currently limited
   by :ref:`libiio v0.26 <libiio>`
   implementation. The throughputs will significantly improve once
   libiio v1.0 will be realeaed.

#. IIO Oscilloscope profile generator (latest libadrv9002-iio) supports
   v68.10.1 API while 2023_r3 Patch1 comes with v68.14.10 API;
   :ref:`Generate a custom device profile using TES <ad-jupiter-ebz profile-generation>`

#. Multi chip synchronization support is not included in the 2023_r2
   Patch1 Kuiper release. Please visit
   :ref:`multi-chip synchronization page <ad-jupiter-ebz mcs-setup>`
   to check available support.

#. :adi:`ADRV9002` CMOS interface not implemented
