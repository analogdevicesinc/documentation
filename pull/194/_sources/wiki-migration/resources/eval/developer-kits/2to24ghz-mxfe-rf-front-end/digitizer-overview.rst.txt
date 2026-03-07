Digitizer Overview
==================

The :adi:`AD9082` or :adi:`AD9081` (“MxFE”) are ideal digitizers for this wideband RF front end due to their high level of integration, performance, and RF sampling rates. The MxFE’s high instantaneous and analog input bandwidth enable RF sampling up to 8GHz, providing architectural and frequency planning flexibility at the system level. They also have highly configurable, on-chip DSP capabilities (DDC/DUC channelizers, NCOs, and programmable FIR filters) as well as four DAC channels and two-to-four ADCs for use in multi-channel systems.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/mxfevariants.png
   :align: center
   :width: 800px

The ADI Frequency Planning Utility tool was used to determine the optimal :adi:`AD9082` ADC sample rate, IF sampling frequency, and IF bandwidth. A 6GSPS ADC rate allows for maximum instantaneous bandwidth (IBW) and complete avoidance of HD2 aliasing in-band for a 1GHz signal bandwidth centered at 4.5GHz (2nd Nyquist). The figure below illustrates this.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/freqfoldinggraphic.png
   :align: center
   :width: 600px

|

.. important::

   The receiver and transmitter front ends described in this CN use a frequency plan designed using the :adi:`AD9082`, specifically with 6GSPS and 12GSPS ADC and DAC sample rates, respectively. However, the RF components themselves are wideband enough to allow for flexibility in the frequency plan and filtering, which can be adjusted to work with the lower ADC sample rates.


   | The :adi:`ADF4377` integrated PLL/VCO is an ideal choice for generating the MxFE sample clock. The [adi>ADF4377]] can generate a clean, low-jitter clock from 800MHz up to 12.8GHz, and it's differential outputs are capable of directly driving the MxFE clock pins.

|
