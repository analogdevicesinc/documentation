Lab 3: Phased Array Antenna Patterns
====================================

--------------

Part 1: Array Factor and Beamwidth
----------------------------------

Training Objective
~~~~~~~~~~~~~~~~~~

| In this lab, we will directly observe the array factor equation. And then observe how the beamwidth changes with steering angle.
| ==== Instructions ==== 1- In the Phaser GUI, select “Lab 2: Array Factor” |image1|
| 2- Slowly move the HB100 in a half-circle around the array and observe the changes

**3- Does the main lobe’s beamwidth remain constant as you move the RF source?**

| 4- In the Phaser GUI, select “Polar Plot” |image2|
| 5- This is the same data, just displayed on a polar grid

| **6- Slowly move the HB100 in a half-circle around the array and observe the changes again**
| ----

Part 2: Array Factor Measurements
---------------------------------

.. _training-objective-1:

Training Objective
~~~~~~~~~~~~~~~~~~

| In this lab, we will make measurements on the array pattern and compare to the theoretical values.
| Recall that the array factor of a uniform, equally weighted (constant amplitude), linear array is given by: |image3|
| And plotting this for various numbers of array elements (N) gives: |image4|
| From this, we can make some measurements on the array:

::

   -Halfpower Beam Width (HPBW):  Main lobe beamwidth, measured 3dB down from peak
   -First Null Beam Width (FNBW):  Spacing between main lobe nulls
   -First Sidelobe Amplitude:  Difference in amplitude (measured in dBc) from the main lobe to the first sidelobe on either side of the main lobe.
   -Peak Amplitude:  signal strength of the main lobe (measured in dBFS for our lab)

| |image5|
| From the array factor equation, with a frequency of 10.3GHz and element to element (d) spacing of 14mm, we can calculate the HPBW and FNBW for various numbers of elements: |image6|
| Let’s measure this now and see how close we are to these calculated values.
| ==== Instructions ==== 1- In the Phaser GUI, select “Lab 2: Array Factor” |image7|
| 2- Move the HB100 to the mechanical boresight location (i.e. directly facing the array)

| 3- Record the following: |image8|
| **4- How do the HPBW and FNBW values compare with the calculated values?**

5- In the Phaser GUI, select the “Gain” tab

6- Click the Rx1_Gain button to disable that channel.

| 7- Do the same for Rx2, Rx7, and Rx8. We now have a 4 element array! |image9|
| **8- Repeat the beamwidth measurements and compare to the calculated values and to the N=8 values.** |image10|
| ===== Part 3: Measuring the Actual Antenna Pattern =====

.. _training-objective-2:

Training Objective
~~~~~~~~~~~~~~~~~~

| In this lab, we’ll make a simple measurement like what you would do in an antenna chamber. It certainly won’t be perfect, but you’ll experience the process and then we’ll measure the sidelobe levels and see how they compare to the electrical scan method.
| ==== Instructions ==== 1- In the Phaser GUI, select “Lab 2: Array Factor”

| 2- In the “Config” tab, select “Signal vs Time” from “Mode Selection”. This plots the peak amplitude vs time. |image11|
| 3- Now rotate the HB100 in a radius around the Phaser board –keep the HB100 pointed at Phaser! |image12|
| 4- Start at the left position (-90 deg), and move around to the right position (+90 deg)

5- Keep a smooth, consistent speed!

6- Practice a few times, then try time it so that one smooth rotation covers the entire graph span

| 7- With practice, it may look like this: |image13|
| 8- Ok, so we can’t really get angular measurements from this (we can never rotate it perfectly). **But we can get accurate lobe amplitudes. Compare these amplitudes to your earlier measurements. How close are they?**

9- **Repeat the process, but change the “Steering Angle” from 0 deg to 30 deg**

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/arrayantennapatterns_1.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/arrayantennapatterns_2.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/arrayantennapatterns_3.png
   :width: 200px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/arrayantennapatterns_4.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/arrayantennapatterns_5.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/arrayantennapatterns_6.png
   :width: 300px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/arrayantennapatterns_7.png
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/arrayantennapatterns_8.png
   :width: 600px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/arrayantennapatterns_9.png
   :width: 600px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/arrayantennapatterns_10.png
   :width: 600px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/arrayantennapatterns_11.png
   :width: 600px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/arrayantennapatterns_12.png
   :width: 600px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/arrayantennapatterns_13.png
   :width: 600px
