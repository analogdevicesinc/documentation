Power Measurement
=================

Binary and source: `Pluto Power App <https://wiki.analog.com/_media/university/tools/pluto/users/debug.zip>`__

This application is a command line utility that uses Pluto in loopback mode (TX and RX LO are equal) to take power measurements. The application only utilizes the DDSs in full-scale ranges, but the DDS frequency, transceiver LO, transceiver RX/TX gain, and transceiver sample rates, are all configurable.

Since Pluto is not an instrument the power measurement can only be considered relatively and is provided in only dB, and continuously averaged over runtime.

Power is measured purely as the squared RMS of the time domain received samples

| :math:`P = 20 \times log10( RMS(x_N \times conj(x_N))^2 )` :
| where :math:`x_N` is the receive complex samples of length N. In the case of this application N is 2^20 samples.

Usage
-----

Note that **ALL** parameters must be set besides -h (help) of course.

::

   C:\Work\App>power2.exe -h
   Usage:
           power -d 10000 -t -10 -r 10

   Measure power from DDS at a specific frequency in loopback

   Options:
           -h, --help
                           Show this help and quit.
           -d, --dds
                           Set DDS tone frequency in Hz.
           -t, --tx
                           Set RX gain in dB.
           -r, --rx
                           Set TX gain in dB.
           -l, --lo
                           Set LO frequency in GHz.            <------------- Typo, should be Hz
           -f, --fs
                           Set sampling frequency in MHz.      <------------- Typo, should be Hz

.. warning::

   When running tests with amplifiers do not exceed 2dBm on the receiver input.

