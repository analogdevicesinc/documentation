Numeric Formats
===============

| :doc:`Click here to return to the Using Sigma Studio page </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio>`

Audio data at the serial inputs and outputs is formatted as 24 bit, signed, integer values. SigmaDSP cores, however, use numeric formats with more than 24 bits for intermediate values, coefficients, and parameters to provide additional headroom and precision. The numeric format has increased in the more powerful DSP core architectures.

To represent non-integer values, all of the SigmaDSP architectures use fixed-point numeric formats (rather than the more common floating point) to maximize the precision needed for audio signal processing. Fixed-point numbers are simply formatted as **A.B**, where A is the number of bits to the left of the decimal point (the integer part) and B is the number of bits to the right of the decimal point (the fractional part).

The combined value A.B is in 2's complement format enabling both positive and negative values. For more information on two's complement representations, please read the comprehensive article on Wikipedia here: `Two's complement <https://en.wikipedia.org/wiki/Two%27s_complement>`__

.. note::

   The AD194x, ADAU176x, ADAU177x, ADAU1781, and ADAU144x processors use 28 bit coefficients, and the ADAU145x processors use 32 bit coefficients.


32 bit Architectures
--------------------

In 32 bit SigmaDSP architectures, audio is represented with A = 8 and B = 24, resulting in a 8.24 bit number. However, control signals and index table values generally require an integer representation, and are therefore represented as A = 32 and B = 0 for a 32.0 value with no fractional part.

32.0 (Integer) Format
~~~~~~~~~~~~~~~~~~~~~

Signals that are in integer format follow standard binary rules for representation.

::

   0b = 0, 1b = 1, 10b = 2, 11b = 3, 100b = 4, et cetera.

32.0 formatted numbers range from (2^31)-1 to -(2^31). Including zero padding, positive integers in the DSP are represented as follows:

::

   0000 0000 0000 0000 0000 0000 0000 0000 = 0
   0000 0000 0000 0000 0000 0000 0000 0001 = 1
   0000 0000 0000 0000 0000 0000 0000 0010 = 2
   0000 0000 0000 0000 0000 0000 0000 0011 = 3
   0000 0000 0000 0000 0000 0000 0000 0100 = 4
   ...
   0000 0000 1000 0000 0000 0000 0000 0000 = 8,388,608 (0 dBFS for 24 bit audio represented in 32.0 format)
   ...
   0111 1111 1111 1111 1111 1111 1111 1111 = 2,147,483,647 (2^31 - 1)

32-bit negative integers are represented in two's complement as follows:

::

   1000 0000 0000 0000 0000 0000 0000 = -2,147,483,648 (2^31)
   ...
   1111 1111 1111 1111 1111 1111 1100 = -4
   1111 1111 1111 1111 1111 1111 1101 = -3
   1111 1111 1111 1111 1111 1111 1110 = -2
   1111 1111 1111 1111 1111 1111 1111 = -1

In general, negative integers are not used in SigmaStudio or SigmaDSP algorithms.

As mentioned, the serial ports and DACs are use 24 bit, signed integer values. Avoid mapping a 32.0 formatted value to an audio output.

8.24 (Decimal) Format
~~~~~~~~~~~~~~~~~~~~~

Audio, unlike control signals, is formatted intuitively as a decimal value in the range of 1 to -1. If a full-scale audio signal with a peak amplitude of 1 has -3 dB of gain applied, it should have an amplitude of approximately 0.707. If -6 dB of gain is applied, the signal has an amplitude of 0.5.

A full scale 24-bit input signal has a positive peak value in common 24 bit, 2's complement representation of:

::

   1000 0000 0000 0000 0000 0000 = 2^23 - 1 = 0dBFS

If we add 8 bits of headroom (MSB zero padding), the 32-bit representation becomes:

::

   0000 0000 1000 0000 0000 0000 0000 0000 = 2^23 - 1 LSB = 0dBFS (A=0, B=2^23 - 1)

The negative peak of a full-scale signal becomes:

::

   1111 1111 1000 0000 0000 0000 0000 0000 = -2^23 + 1 LSB (A=-1, B=2^23 - 1)

Notes that moving a leading '1' to the left or right will double or halve the value, respectively.

::

   0000 0000 0000 0000 0000 0000 0000 =  0.0
   0000 0010 0000 0000 0000 0000 0000 =  0.25
   0000 0100 0000 0000 0000 0000 0000 =  0.5
   0000 1000 0000 0000 0000 0000 0000 =  1.0 (0 dBFS)
   0001 0000 0000 0000 0000 0000 0000 =  2.0
   0010 0000 0000 0000 0000 0000 0000 =  4.0
   0111 1111 1111 1111 1111 1111 1111 =  (16.0 - 1 LSB) = max value

Similarly, for negative numbers:

::

   1000 0000 0000 0000 0000 0000 0000 =  -16.0 = min value
   1110 0000 0000 0000 0000 0000 0000 =  -4.0
   1111 0000 0000 0000 0000 0000 0000 =  -1.0
   1111 1000 0000 0000 0000 0000 0000 =  -1.0
   1111 1100 0000 0000 0000 0000 0000 =  -0.5
   1111 1110 0000 0000 0000 0000 0000 =  -0.25
   1111 1111 1111 1111 1111 1111 1111 =  (1 LSB below 0.0)

When outputting to the serial ports or DACs, signals will saturate at 0 dBFS. This means any signal with a peak exceeding 1.0 in 5.23 format will be clipped to full-scale on the outputs.

The ADAU176x, ADAU177x, and ADAU1781 processors use a 28 bit value, and the ADAU145x processors use a 32 bit value

.. _bit-architectures-1:

28 bit architectures
--------------------

In 28 bit SigmaDSP architectures, audio is represented with A = 5 and B = 23, resulting in a 5.23 bit number. However, control signals and index table values generally require an integer representation, and are therefore represented as A = 28 and B = 0 for a 28.0 value with no fractional part.

.. _integer-format-1:

28.0 (Integer) Format
~~~~~~~~~~~~~~~~~~~~~

Signals that are in integer format follow standard binary rules for representation.

::

   0b = 0, 1b = 1, 10b = 2, 11b = 3, 100b = 4, et cetera.

28.0 formatted numbers range from (2^27)-1 to -(2^27). Including zero padding, positive integers in the DSP are represented as follows:

::

   0000 0000 0000 0000 0000 0000 0000 = 0
   0000 0000 0000 0000 0000 0000 0001 = 1
   0000 0000 0000 0000 0000 0000 0010 = 2
   0000 0000 0000 0000 0000 0000 0011 = 3
   0000 0000 0000 0000 0000 0000 0100 = 4
   ...
   0000 1000 0000 0000 0000 0000 0000 = 8388608 (0 dB full scale represented in 28.0 format)
   ...
   0111 1111 1111 1111 1111 1111 1111 = 134217727 (2^27 - 1)

28-bit negative integers are represented in two's complement as follows:

::

   1000 0000 0000 0000 0000 0000 0000 = -134217728 (2^27)
   ...
   1111 1111 1111 1111 1111 1111 1100 = -4
   1111 1111 1111 1111 1111 1111 1101 = -3
   1111 1111 1111 1111 1111 1111 1110 = -2
   1111 1111 1111 1111 1111 1111 1111 = -1

In general, negative integers are not used in SigmaStudio or SigmaDSP algorithms.

As mentioned, the serial ports and DACs are 24 bit integer values. In 28 bit architectures, the 24 least significant bit signals map to 0 dBFS. The four extra MSBs added for processing headroom are ignored. This means any signal exceeding 8388608 in 28.0 format will be limited to full-scale on the outputs. This clipping operation is one of the reasons negative 28 bit integers are avoided.

.. _decimal-format-1:

5.23 (Decimal) Format
~~~~~~~~~~~~~~~~~~~~~

Audio, unlike control signals, is formatted intuitively as a decimal value in the range of 1 to -1. If a full-scale audio signal with a peak amplitude of 1 has -3 dB of gain applied, it should have an amplitude of approximately 0.707. If -6 dB of gain is applied, the signal has an amplitude of 0.5.

A full scale 24-bit input signal has a positive peak value in common 24 bit, 2's complement representation of:

::

   1000 0000 0000 0000 0000 0000 = 2^23 - 1 = 0dBFS

If we add 4 bits of headroom (MSB zero padding), the 28-bit representation becomes:

::

   0000 1000 0000 0000 0000 0000 0000 = 2^23 - 1 = 0dBFS (A=0, B=2^23 - 1)

The negative peak of a full-scale signal becomes:

::

   1111 1000 0000 0000 0000 0000 0000 (A=-1, B=2^23 - 1)

Moving the leading '1' to the left or right will double or halve the value, respectively.

::

   0000 0000 0000 0000 0000 0000 0000 =  0.0
   0000 0010 0000 0000 0000 0000 0000 =  0.25
   0000 0100 0000 0000 0000 0000 0000 =  0.5
   0000 1000 0000 0000 0000 0000 0000 =  1.0 (0 dBFS)
   0001 0000 0000 0000 0000 0000 0000 =  2.0
   0010 0000 0000 0000 0000 0000 0000 =  4.0
   0111 1111 1111 1111 1111 1111 1111 =  (16.0 - 1 LSB)

Similarly, for negative numbers:

::

   1000 0000 0000 0000 0000 0000 0000 =  -16.0
   1110 0000 0000 0000 0000 0000 0000 =  -4.0
   1111 0000 0000 0000 0000 0000 0000 =  -1.0
   1111 1000 0000 0000 0000 0000 0000 =  -1.0
   1111 1100 0000 0000 0000 0000 0000 =  -0.5
   1111 1110 0000 0000 0000 0000 0000 =  -0.25
   1111 1111 1111 1111 1111 1111 1111 =  (1 LSB below 0.0)

When outputting to the serial ports or DACs, signals will saturate at 0 dBFS. This means any signal with a peak exceeding 1.0 in 5.23 format will be limited to full-scale on the outputs.

As mentioned, the serial ports and DACs are 24 bit integer values. The 24 least significant bits (the fractional portion = B) map to 0 dBFS. The four integer bits (A) are ignored.

5.19 (Hardware Readback) Format
-------------------------------

Some cells in SigmaStudio may use slightly different number formats. For example, since the hardware-based DSP readback registers in the ADAU1701 only have 24 bits, the lower 4 bits from the 5.23 signal are truncated and the number is represented in 5.19 format.

So, a full-scale signal that was represented in 5.23 format as

::

   0000 1000 0000 0000 0000 0000 0000

| would have its lower 4 bits truncated for 5.19 representation:

::

   0000 1000 0000 0000 0000 0000

The result is that very small amplitude signals will be truncated and therefore cannot be read back from the DSP on the older generation of SigmaDSP cores.

Newer cores, such as the ADAU1761 and ADAU144x, have full 5.23 readback capabilities implemented in software.

Decibel Conversion
------------------

Concept for dB conversion:

-  Count the number of leading 0s (minus 4) and multiply by 6; this is the integer part of the dB scale.
-  Use the bits after the leading 1 to linearly interpolate between the 6 dB points.

|numericpic1.png|

In order to get a linear value into a hex/binary number that can be written to the SigmaDSP, and vice versa, it is important to understand number conversions.

The actual level parameters that you need to write are only the last 28 bits, and this value is simply a linear gain value. Using -40 dB as an example, convert this value to a linear value using the standard dB equation:

::

   20log10 (x/1) = -40dB      x = .01

Take this linear value and multiply by 223 in order to get the decimal representation of the value in hex, because it is a 5.23 value.

::

   .01 * 223 = 83886.08.  

Now take the integer part of this result and convert 83886 to hex, and you will get 0x00147AE.

The output of some blocks is a 5.19 number. The formula to determine the dB-output value from the readback value is the following:

::

   dB_value = 96.32959861 * (readback_value / 219 - 1)

.. |numericpic1.png| image:: https://wiki.analog.com/_media/numericpic1.png
