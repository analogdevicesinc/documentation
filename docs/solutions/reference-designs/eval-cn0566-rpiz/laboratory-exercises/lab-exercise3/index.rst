.. _cn0566_lab3:

Lab 3: Phased Array Antenna Patterns
====================================

Part 1: Array Factor and Beamwidth
----------------------------------

Training Objective
~~~~~~~~~~~~~~~~~~

In this lab, we will directly observe the array factor equation. And then
observe how the beamwidth changes with steering angle.

Instructions
~~~~~~~~~~~~

1. In the Phaser GUI, select ``Lab 2: Array Factor``.

   .. figure:: arrayantennapatterns_1.png

2. Slowly move the HB100 in a half-circle around the array and observe the
   changes.

3. **Does the main lobe’s beamwidth remain constant as you move the RF source?**

4. In the Phaser GUI, select ``Polar Plot``. 

   .. figure:: arrayantennapatterns_2.png

5. This is the same data, just displayed on a polar grid.

6. **Slowly move the HB100 in a half-circle around the array and observe the
   changes again**

Part 2: Array Factor Measurements
---------------------------------

Training Objective
~~~~~~~~~~~~~~~~~~

In this lab, we will make measurements on the array pattern and compare to the
theoretical values.

Recall that the array factor of a uniform, equally weighted (constant
amplitude), linear array is given by: 

.. figure:: arrayantennapatterns_3.png

And plotting this for various numbers of array elements (N) gives:

.. figure:: arrayantennapatterns_4.png

From this, we can make some measurements on the array:

1. Halfpower Beam Width (HPBW):  Main lobe beamwidth, measured 3dB down from peak
2. First Null Beam Width (FNBW):  Spacing between main lobe nulls
3. First Sidelobe Amplitude:  Difference in amplitude (measured in dBc) from the main lobe 
   to the first sidelobe on either side of the main lobe.
4. Peak Amplitude:  signal strength of the main lobe (measured in dBFS for our lab)

.. figure:: arrayantennapatterns_5.png

From the array factor equation, with a frequency of 10.3GHz and element to
element (d) spacing of 14mm, we can calculate the HPBW and FNBW for various
numbers of elements: 

.. figure:: arrayantennapatterns_6.png

Let’s measure this now and see how close we are to these calculated values.

Instructions
~~~~~~~~~~~~

1. In the Phaser GUI, select ``Lab 2: Array Factor``

  .. figure:: arrayantennapatterns_7.png

2. Move the HB100 to the mechanical boresight location (i.e., directly facing
   the array)

3. Record the following: 

  .. figure:: arrayantennapatterns_8.png

4. **How do the HPBW and FNBW values compare with the calculated values?**

5. In the Phaser GUI, select the ``Gain`` tab

6. Click the Rx1_Gain button to disable that channel.

7. Do the same for Rx2, Rx7, and Rx8. We now have a 4 element array.

  .. figure:: arrayantennapatterns_9.png

8. Repeat the beamwidth measurements and compare to the calculated values
   and to the N=8 values. 

  .. figure:: arrayantennapatterns_10.png

Part 3: Measuring the Actual Antenna Pattern
--------------------------------------------

Training Objective
~~~~~~~~~~~~~~~~~~

In this lab, we’ll make a simple measurement like what you would do in an
antenna chamber. It certainly won’t be perfect, but you’ll experience the
process and then we’ll measure the sidelobe levels and see how they compare to
the electrical scan method.

Instructions
~~~~~~~~~~~~

1. In the Phaser GUI, select ``Lab 2: Array Factor``.

2. In the ``Config`` tab, select ``Signal vs Time`` from ``Mode Selection``. This
   plots the peak amplitude vs. time.

   .. figure:: arrayantennapatterns_11.png

3. Now rotate the HB100 in a radius around the Phaser board. Keep the HB100
   pointed at Phaser! 
   
   .. figure::arrayantennapatterns_12.png

4. Start at the left position (-90 deg), and move around to the right position
   (+90 deg)

5. Keep a smooth, consistent speed.

6. Practice a few times, then try time it so that one smooth rotation covers the
   entire graph span.

7. With practice, it may look like this: 

  .. figure:: arrayantennapatterns_13.png

8. Ok, so we can’t really get angular measurements from this (we can never
   rotate it perfectly). **But we can get accurate lobe amplitudes. Compare these
   amplitudes to your earlier measurements. How close are they?**

9. **Repeat the process, but change the “Steering Angle” from 0 deg to 30 deg**.
