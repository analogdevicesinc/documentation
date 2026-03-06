Dealing with non-Quadrature Signals
===================================

This may seem to be a puzzling topic to some — the radio is quadrature — how can a signal be non-quadrature?

The answer involves a little math, so the reader is expected to understand :doc:`fundamental of quadrature signals </wiki-migration/resources/eval/user-guides/ad-fmcomms1-ebz/math>`. In the basic sense, quadrature signals can be broken down into two orthogonal components or source (modulated) sinusoids. Real or non-quadrature signals are technically a subset of quadrature when the components are in-phase or one of the components is zero. This is easy to observe spectrally since real-valued signals are conjugate symmetric in frequency. By only using quadrature, sometimes referred to as complex, a signal can we place information uniquely on a single sideband.

Creating and Transmitting a "real" signal
=========================================

Transmitting a "real" signal isn't a problem. It's either:

-  sending in-phase (or identical) I & Q signals
-  sending just I or Q

Sending the same signal on I and Q
----------------------------------

In IIO-Scope, we can create a real signal by playing the same tone, at the same frequency, same magnitude out the DDSes all the same time.

.. image:: https://wiki.analog.com/_media/university/tools/pluto/users/dds-real.png
   :width: 400px

Euler says that this should generate an equal-sized tone on each side of the LO, and we can check this by putting the part into digital loopback mode (anything that we send out the Tx, is sent to the Rx) by going to the advanced tab, under the Built-in Self Test (BIST) tab:

.. image:: https://wiki.analog.com/_media/university/tools/pluto/users/loopback.png
   :align: center
   :width: 500px

By looking at the digital loopback time and frequency domain of the signal we are sending, we can see even after 300 years, the math holds up. (The time domain signal looks like only one (green = ``I`` ), since the other channel (red = ``Q``) is exactly the same and behind it.

============================ =================================
Digital Loopback Time Domain Digital Loopback Frequency Domain
============================ =================================
|image1|                     |image2|
============================ =================================

Sending only I or only Q
------------------------

You can achieve the same result mathematically by only sending I or Q (and sending zeros on the other channel). Here we set the magnitude on Q to -99 (or -Infinity).

.. image:: https://wiki.analog.com/_media/university/tools/pluto/users/i_only.png
   :width: 400px

The rest of the tests are the same as the above. Take note that even though we are sending the same magnitude of I as before, the power in the signal is less (the peaks in the FFT drop), since we are sending half the power, (only I, no Q).

============================ =================================
Digital Loopback Time Domain Digital Loopback Frequency Domain
============================ =================================
|image3|                     |image4|
============================ =================================

Sending the data
----------------

We can send that out the RF, by disabling loopback and setting the Rx and Tx LO to the same value. The results shown during the receiving section are RF loopback (The BIST Loopback setting is set to ``Disable``, and the Rx and Tx SMA connectors are connected via an SMA cable, which is referred to as "Analog Loopback").

Receiving a "real" signal
=========================

Receiving is where things can be more complicated. Most (all) integrated transceivers include some sort of Quadrature tracking corrections which try to ensure the signals are correct, and any imperfections in the chip or external circuitry (balun, non-differential traces, etc) are removed.

While the frequency domain plot looks the same, we can see that the amplitude is jumping up and down by a few dB (which is impossible to show in a static picture like this).

+-------------------------------------------------------------------+


| Analog Loopback, Frequency Domain, ACG On, Quadrature tracking On |

+===+
| |image5|                                                          |
+---+

It's easier to look at this in the time domain. Here the amplitude difference between I & Q is random based on the random difference between the phase of the Rx and Tx PLL. This is indeed completely random and will change any time either PLL settings are touched. Moving one LO to a different setting, and back again, will change this phase offset (which manifest itself as a magnitude difference between I and Q).

+--------------------------------------------------------------------------+


| Analog Loopback, Time Domain, I & Q Data, ACG On, Quadrature tracking On |

+===+
| |image6|                                                                 |
+---+

You can change this magnitude difference digitally by post-processing the sampled data, by using the Phase Rotation control in IIO oscilloscope. It doesn't change the phase relationship between I and Q, but it does change the effective sample time relative to the PLL, and therefore changes their relative magnitude. By changing this, you can effectively make either of the I or Q zero, and only receive the signal the other (Q or I), indicating that the received signal is "real" (all information can be received just on one signal channel, and it has no phase or quadrature information.

+------------------------------------------+


| Analog Loopback, Time Domain, I & Q Data |

+===+
| |image7|                                 |
+---+

The easiest way to ignore these things is to look at the overall magnitude of the signal ie - set up a math equation in IIO-Scope with ``ssqrtf((voltage0*voltage0)+(voltage1*voltage1))*((voltage0 > 0)-(voltage0 < 0))``. This is the equivalent the :math:`sign(I) \times sqrtI^2 + Q^2` . This will ensure that any I/Q magnitude difference doesn't affect the investigation.

============== ==================
I / Q Rotation I, Q, and mag data
============== ==================
0

|image8|

50 degrees

|image9|

70 degrees

|image10|

mag only

|image11|

============== ==================

You can see from the data (and the math) that we can rotate I/Q and it doesn't change the overall attitude of the signal. It's sometimes difficult to see the ``I`` (green), ``Q`` (red), and ``Mag`` (blue) since they may by hidden (behind) other channels.

By capturing 1048576 samples (or at 3MSPS, 349525.333 us) you can see what looks like some weird sort of steps. These perturbations are caused by two state machines inside the AD9363 fighting against each other. (1) Automatic Gain Control (ACG) and (2) Quadrature tracking corrections.

+--------------------------------------------------------------------------+


| Analog Loopback, Time Domain, I & Q Data, ACG On, Quadrature tracking On |

+===+
| |image12|                                                                |
+---+

Here the green signal is the ``I``, and the blue is the overall magnitude. Since, during this run, the ``I`` was showing most the perturbations, and it is small compared to Q, the overall magnitude does not change that much, but it does have undesired step changes, that can be easily fixed when we understand what is happening.

The first step is to understand that the ACG is reacting to magnitude changes caused by the Quadrature tracking corrections. Turning the ACG to manual mode can help isolate the effects of the IQ Correction. Here is a picture of the same setup with the ACG set to manual mode.

+---------------------------------------------------------------------------+


| Analog Loopback, Time Domain, I & Q Data, ACG Off, Quadrature tracking On |

+===+
| |image13|                                                                 |
+---+

Here we can see multiple times where the Quadrature tracking corrections are trying to suppress what it believes is an image until it gives up, resets, and starts over. This results in what appears to be amplitude errors in the signal.

.. important::

   The problem statement is simple - there is no way for a Quadrature tracking correction algorithm to understand if a "real" signal is being sent, or if in fact something is quadrature, is an image, and needs to be suppressed. The only thing that understands that is the sentient being between the chair and the keyboard.


Removing issues.
================

Turning Quadrature tracking off
-------------------------------

The easiest way to remove this error is to simply turn off Quadrature tracking corrections.

.. image:: https://wiki.analog.com/_media/university/tools/pluto/users/tracking_off.png
   :align: center
   :width: 100px

This will resolve the set changes in magnitude in either I or Q

.. image:: https://wiki.analog.com/_media/university/tools/pluto/users/fixed.png
   :align: center
   :width: 700px

Offset Tuning
-------------

Here when Rx and Tx PLL are the same, we can see the Quadrature tracking issue.

.. image:: https://wiki.analog.com/_media/university/tools/pluto/users/0khz_offset.png
   :align: center
   :width: 600px

Moving 1 kHz off (with Quadrature tracking On), makes the magnitude look like (which is the correct, expected result - constant magnitude over time):

.. image:: https://wiki.analog.com/_media/university/tools/pluto/users/mag_1khz_offset.png
   :align: center
   :width: 700px

It's expected there may be "waves" in the magnitude, as we are sending sinusoidal signals, and sampling at an offset will cause low-frequency aliasing. The best thing to do is to look at the signal with Quadrature tracking On and Off to see if it makes a difference. (all tests were taken with ACG turned off, so we are isolating one (Quadrature tracking) issue).

====== ======================= ======================
offset Quadrature Tracking Off Quadrature Tracking On
====== ======================= ======================
0 Hz   |image14|

|image15|

5 Hz   |image16|

|image17|

10 Hz  |image18|

|image19|

20 Hz  |image20|

|image21|

====== ======================= ======================

Conclusion
==========

You can see from this that as long as you are off by 10 Hz or more, the Quadrature tracking feature works properly. In most systems, it's pretty rare to see this in the wild - as, at 2.4 GHz, a sub 10 Hz offset would be better than 4 parts per billion (or 0.004 ppm) offset. Unless you have a great reference clock, and spend some time tuning the system, and are lucky - you should never run into this.

It is quite easy to connect Rx to Tx and see this on the same unit - since the reference offset is 0 between Tx and Rx.

IIO Attributes
--------------

The IIO attributes that were used above are:``# **iio_attr -a -c ad9361-phy RX_LO frequency**
dev 'ad9361-phy', channel 'altvoltage0' (output), id 'RX_LO', attr 'frequency', value '435000000'
# **iio_attr -a -c ad9361-phy TX_LO frequency**
dev 'ad9361-phy', channel 'altvoltage1' (output), id 'TX_LO', attr 'frequency', value '435000000'
#  **iio_attr  -D  ad9361-phy loopback**
dev 'ad9361-phy', debug attr 'loopback', value :'0'
# **iio_attr -c ad9361-phy voltage0 gain_control_mode**
dev 'ad9361-phy', channel 'voltage0' (input), attr 'gain_control_mode', value 'manual'
# **iio_attr -c ad9361-phy voltage0 quadrature_tracking_en**
dev 'ad9361-phy', channel 'voltage0' (input), attr 'quadrature_tracking_en', value '1'``

UHD
---

For those using a National Instruments USRP Radio, this can be controlled via ``set_rx_iq_balance()`` method.

SDRangel
--------

`SDRAngel <https://github.com/f4exb/sdrangel>`__ also can turn on/off Quadrature tracking with it's Hardware control buttons.

.. image:: https://wiki.analog.com/_media/university/tools/pluto/users/sdrangel_controls.png

-  ``RFDC`` : RF DC Correction tracking
-  ``BBDC`` : BaseBand DC Correction tracking
-  ``IQ`` : Quadrature tracking

Scope
-----

This issue will exist on all integrated devices which have some sort of Quadrature tracking feature, including all hardware based on ADI and `other manufactures <https://github.com/f4exb/sdrangel/issues/378#issuecomment-513012883>`__. It's not something specific to the ADALM-PLUTO, or the AD9363.

.. |image1| image:: https://wiki.analog.com/_media/university/tools/pluto/users/dds_lookback_time.png
   :width: 450px
.. |image2| image:: https://wiki.analog.com/_media/university/tools/pluto/users/dds_loopback.png
   :width: 450px
.. |image3| image:: https://wiki.analog.com/_media/university/tools/pluto/users/dds_loopback_time_i.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/university/tools/pluto/users/dds_looback_i.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/university/tools/pluto/users/rf_lo_same.png
   :width: 700px
.. |image6| image:: https://wiki.analog.com/_media/university/tools/pluto/users/lo_same_time.png
   :width: 700px
.. |image7| image:: https://wiki.analog.com/_media/university/tools/pluto/users/rx_rot.png
   :width: 300px
.. |image8| image:: https://wiki.analog.com/_media/university/tools/pluto/users/lo_same_time_0_offset.png
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/university/tools/pluto/users/lo_same_time_52_offset.png
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/university/tools/pluto/users/lo_same_time_77offset.png
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/university/tools/pluto/users/lo_same_time_mag_only.png
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/university/tools/pluto/users/acg_q_on.png
   :width: 700px
.. |image13| image:: https://wiki.analog.com/_media/university/tools/pluto/users/off_iq_on.png
   :width: 600px
.. |image14| image:: https://wiki.analog.com/_media/university/tools/pluto/users/0hz_offset_iq_off.png
   :width: 400px
.. |image15| image:: https://wiki.analog.com/_media/university/tools/pluto/users/0hz_offset_iq_on.png
   :width: 400px
.. |image16| image:: https://wiki.analog.com/_media/university/tools/pluto/users/5hz_offset_iq_off.png
   :width: 400px
.. |image17| image:: https://wiki.analog.com/_media/university/tools/pluto/users/5hz_offset_iq_on.png
   :width: 400px
.. |image18| image:: https://wiki.analog.com/_media/university/tools/pluto/users/10hz_offset_iq_off.png
   :width: 400px
.. |image19| image:: https://wiki.analog.com/_media/university/tools/pluto/users/10hz_offset_iq_on.png
   :width: 400px
.. |image20| image:: https://wiki.analog.com/_media/university/tools/pluto/users/20hz_offset_iq_off.png
   :width: 400px
.. |image21| image:: https://wiki.analog.com/_media/university/tools/pluto/users/20hz_offset_iq_on.png
   :width: 400px
