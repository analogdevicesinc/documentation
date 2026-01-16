.. _cn0566_lab2:

Lab 2: Steering Angle
=====================

Training Objective
------------------

In this lab, we’ll explore the relationship between the element to element
phase shift and the resulting electrical steering angle.

Instructions
------------

1. Open the file “cn0566_gui.py” in the Thonny IDE (This guide uses the Thonny
   IDE, but the file should run on other IDEs as well) 

   .. figure:: steeringangle_1.png

2. Press the green ``Run`` button 

   .. figure:: steeringangle_2.png

3. You’ll see the FFT (amplitude vs. frequency) of the HB100 source as received
   by the Phaser’s array: 

   .. figure:: steeringangle_3.png

4. By adjusting the “Steering Angle” slider bar, you can change the phase values
   of each element.

5. Move the HB100 to an angle of about 30 deg. The protractor, can help you
   point this somewhat accurately. Just place it on top of the Raspberry Pi, and
   move the arrow to 30 deg. 

   .. figure:: steeringangle_5.png

6. Now slide the “Steering Angle” to find the phase delta that produces the
   maximum FFT amplitude.

7. **What phase delta do you observe that produces the maximum FFT amplitude?**

8. Now click on the “Rectangular Plot” tab

   .. figure:: steeringangle_8.png

9. This plots the peak FFT amplitude vs the selected steering angle

10. Move the Steering Angle slider bar again.

11. **Does the amplitude move in a predictable way? What do you think is happening?**
