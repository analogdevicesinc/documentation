# Finding the Element to Element Phase Shift


##  How to Steer an “Electronically Steerable Array”

Phased arrays are more accurately called “electronically steerable arrays”, or ESAs.  A good first activity for any ESA is to steer it.  So how do we electronically steer an antenna array? The short answer is we form the beam by setting a delay per element and then adding all the elements together. In order to understand how to set this delay, first consider an RF signal that is striking our 8-element Phaser receive array:

```{image} steering_array.svg
:width: 500px
:align: center
```

Based on the direction of arrival (DOA) of the RF signal to the array, each element will see the signal at some slightly different time.  You can see that that delay will be smaller if the signal moved directly over the array (called the broadside or mechanical boresight direction). And the delay will be larger as the signal moves toward either horizon of the array.  So the delay that we pick will set the steering angle for our array to optimally add all the elements together.  Conversely, signals arriving from other angles will then have a greatly reduced gain. 

 
So how do we choose the exact delay we want, to steer the array to a particular angle?  If you just turn our setup on its side, you’ll see an equivalent view of it here:

```{image} steering_angle.svg
:width: 700px
:align: center
```

You can see that we now have a right triangle whose hypotenuse is the incoming wavefront.  The distance between elements is “d” (14mm for the Phaser board).  And the angle from mechanical boresight is called theta.  And if we form another right triangle with the wavefront and theta, we can calculate L, which is the incremental propagation distance between elements.  We can do some simple math to show that the time delay between when the wavefront strikes one element to when it strikes the neighboring element is:

```{image} deltaT.svg
:width: 200px
:align: center
```

And we can convert that time delay into a phase shift if we multiply by 2 Pi f, where f is the frequency of the incoming signal. 

```{image} delta_phase.svg
:width: 120px
:align: center
```

So if we shift each element from its neighbor by that amount, then we will steer the antenna in the direction of “theta.”  Here’s an example of how that would work for a 30 deg steering angle (theta), at a frequency of 10.3 GHz:

```{image} steering_example.svg
:alt: 
:width: 600px
:align: center
```

So that’s the basic idea of how we can electronically steer the receive array of Phaser.  Now, let’s try it out!


## Steering Angle Lab with Phaser

In this lab, we’ll explore the relationship between the element to element phase shift and the resulting electrical steering angle

### Instructions

```{image} gui.svg
:alt: GUI
:width: 300px
:align: right
```

* Open the file “phaser_gui.py” in the Thonny IDE (This guide uses the Thonny IDE, but the file should run on other IDEs as well)
* Press the green "Run" button
* In the middle of the GUI, at the bottom, select "Lab 1: Steering Angle"
* You’ll see the FFT (amplitude vs frequency) of the HB100 source as received by the Phaser’s array:

```{image} fft.svg
:alt: FFT
:width: 400px
:align: center
```

```{image} setup.svg
:alt: Picture of Lab Setup
:width: 400px
:align: right
```

* By adjusting the “Steering Angle” slider bar, you can change the phase values of each element.
* Move the HB100 to an angle of about 30 deg. If you have a protractor, that can help you point this somewhat accurately. 

* Now slide the “Steering Angle” bar to find the phase delta that produces the maximum FFT amplitude.
* What phase delta do you observe that produces the maximum FFT amplitude?


* Now click on the “Rectangular Plot” tab

```{image} rect_plot.svg
:alt: FFT
:width: 700px
:align: center
```

* This plots the peak FFT amplitude vs the selected steering angle
* Move the Steering Angle slider bar again.
* Does the amplitude move in a predictable way? What do you think is happening?


For a video walkthrough of this lab, see the second half of this video:

```{video} https://www.youtube.com/watch?v=5bqsyF1zhR8
:align: left
```
```{clear-content}
```




```{clear-content}
```
```{note}
For questions or help with the Phaser, please visit:
{ez}`adieducation/university-program`
```
