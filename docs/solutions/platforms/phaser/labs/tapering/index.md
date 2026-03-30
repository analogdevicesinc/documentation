# Sidelobes and Tapering

When we formed the beam, we saw that we got the main lobe in the direction we wanted--which is good! But we also get a bunch of sidelobes.  These come from the sinc pattern of how all the elements get added up and yielded the array factor equation.

But the problem with sidelobes is they end up pointing our antenna in unintended directions.  For example, let's assume that the signal we want is coming directly from mechanical boresight, shown as the orange arrow in this figure.

```{image} sidelobes.svg
:width: 400px
:align: right
```


But we also have an interferer, or jammer, coming from the gray arrow.  And let's just say that the jammer lines up perfectly with the first sidelobe.  Remember, that first sidelobe is only 13 dB down from the peak of our main lobe.  It means that we will pick up the signal we want, but we will also pick up the jammer, attenuated only by 13 dB.  And we won’t be able to tell which is the signal and which is the jammer.  We’ll think that everything is coming from the direction that we set our main lobe to.  So that’s the problem, and it’s a very big problem.  

The most common method to deal with sidelobes is to use amplitude tapering across the array elements.  To better understand tapering, first consider a square wave signal, in the time domain, that goes from -1 to +1.  This looks like a boxcar, or a rectangular, waveform.  And in antenna terms we’d call it “uniform illumination."

```{image} windowing.svg
:alt: E Field Windowing
:width: 800px
:align: center
```

If you took the fourier transform of that time domain square wave you would end up with a sin(x)/x function (the middle graph).  Taking 20 LOG of that will give you the signal power, and that graph yields the familiar main lobe, and a bunch of sidelobes.  Note that the first sidelobe at -13dB down from the peak lobe--just like we get when we measured the first sidelobe of our antenna pattern.

And if we make the pulse wider in the time domain, the main lobe in the spectrum becomes more narrow, the sidelobes crowd in, but the sidelobe levels remain the same.  Which should also remind you of something we did in our lab:  where we changed the number of elements.

To control those sidelobes on a rectangular FFT, we’ll commonly apply a window function. Though windowing brings some loss to the peak and broadening of the main lobe.  

```{image} WindowFunctions.svg
:alt: Windowing Profiles
:width: 800px
:align: center
```

So we start with Boxcar, and we see that the first sidelobe is only 13 dBc down from the peak, but it has the narrowest main lobe.  Then we can apply a windowing function to that.  And there are many windowing functions to choose from, but as an example, here are Hanning and Blackman.  Hanning brings the first sidelobe down to -30 dBc.  And Blackman has the lowest sidelobes, but you can clearly see it has the widest main lobe.

So that analysis was all for the square wave signal in the time domain.  But it’s basically the same in the spatial domain.  If we have a uniformly illuminated antenna pattern, then we get sidelobes.  But if we window that antenna pattern, then we reduce the sidelobes. In antenna terms windowing is “tapering” the power at each element down from the center toward the edge of the antenna.  However, this also has the undesirable effect of broadening the main lobe--just like a Blackman window will broaden the responses in an FFT.

```{image} tapering.svg
:alt: Antenna Tapering
:width: 600px
:align: center
```
*Figures from “Phased Array Antenna Patterns—Part 3: Sidelobes and Tapering”*

So tapering presents an interesting dilemma:  We taper to reduce the sidelobes.  But as we taper, we are widening the beam and reducing the gain of the main lobe. But the reason we go to the expense of large arrays is to get narrow beams and high gains.  So tapering works against us, and becomes an interesting engineering tradeoff that we can explore with the Phaser kit.  

## Tapering Lab

1.  In the Phaser GUI, select “Lab 3: Tapering”
2.  Press “Copy Plot to Memory”, then try one of the tapering profile buttons.

```{image} TaperingGUI.svg
:alt: Antenna Tapering
:width: 600px
:align: center
```

3.  What is the impact to sidelobe level, beamwidth, and peak gain?
4.  Select “Symmetric Taper” and invent your own profile! 
   * Can you make a “better” taper?



You can find a video walkthrough of this lab here:

```{video} https://www.youtube.com/watch?v=be_5D4eNtCY
:align: left
```

```{clear-content}
```
```{note}
For questions or help with the Phaser, please visit:
{ez}`adieducation/university-program`
```
