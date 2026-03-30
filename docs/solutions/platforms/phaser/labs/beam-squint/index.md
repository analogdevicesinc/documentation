# Beam Squint

```{image} triangle.svg
:width: 400px
:align: right
```


Recall that in an electronically steerable array, there are two ways to represent the delay between adjacent antenna elements:

1.  It can be represented as a time delay:

```{image} eq1.svg
:width: 120px
:align: center
```


1.  It can be represented as a phase shift:

```{image} eq2.svg
:width: 170px
:align: center
```

Note that the phase shift is a function of the instantaneous frequency.  If that frequency changes, then the phase shift applied to the elements would also need to change.  If the phase shift cannot change, perhaps due to a wideband signal, then an effective variation in time delay is placed on the array at those frequencies.  It means that, for different frequencies, the steering angle will change.  This change in steering angle is called "beam squint."  

At mechanical boresight (a steering angle of 0 deg), there is no phase shift applied, and therefore no potential for a beam squint issue.  However, as the array is steered away from mechanical boresight, the effect of beam squint becomes more significant.  Therefore, the beam squint is both a function of frequency and steering angle.  This [article](https://www.analog.com/en/analog-dialogue/articles/phased-array-antenna-patterns-part2.html) provides a summarized equation as follows:

```{image} eq4.svg
:width: 300px
:align: center
```

For example, if we have a carrier frequency of 10.5GHz, and a peak frequency deviation of 500MHz, then the beam will move off the intended 45 degree beam angle by 3 degrees. That’s not really a problem if the HPBW is 25 degrees, as is the case for our 4 element setup.  But for a large antenna with, say, 1 degree beam width, the received power will be down by many dB at the band edge.

## Beam Squint Lab

Since our HB100 frequency source is fixed, for this lab, we will instead change the frequency at which the steering angle is calculated.  This will appear as the “Beam Calculated at” frequency. Both methods are equivalent. Its easier to change the calculated frequency in our lab. It also avoids other changes in the antenna pattern that would come from a new frequency, so we end up with a more straightforward comparison.

1. Set the RF source (HB100) to an angle of about 50 degrees
2. In the Phaser GUI, select “Lab 5: Beam Squint”

```{image} squint1.svg
:width: 600px
:align: center
```

3. Click “Copy Plot to Memory”
4. Record the peak angle (you can also turn on “Show Peak Angle” under “Plot Options” tab)
5. Change the “Signal BW” slider bar to 500 MHz
6. Record the new peak angle. Does the difference between the two peaks match our ~3° calculation?

```{image} squint2.svg
:width: 600px
:align: center
```

7. Try other **signal bandwidths** and observe the effect.
8. Try other **steering angles** and observe the effect.

You can find a video walkthrough of this lab here:

```{video} https://www.youtube.com/watch?v=LYVD014ClZI
:align: left
```

```{clear-content}
```
```{note}
For questions or help with the Phaser, please visit:
{ez}`adieducation/university-program`
```
