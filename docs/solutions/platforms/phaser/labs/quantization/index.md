# Quantization Sidelobes

Quantization sidelobes are analogous to quantization error in a data converter. These sidelobes can appear, for certain steering angles, if our phase steps are too large.  More information is in this excellent lecture by Bob Broughton here:

```{video} https://www.youtube.com/watch?v=51O5FLVZE4c
:align: left
```

```{clear-content}
```
___

## Quantization Sidelobes Lab
In this lab, we will change the phase step size and observe the formation of quantization sidelobes.

1. In the Phaser GUI, select “Lab 6:  Quantization”
2. In the “Config” tab, set the steering angle to 15 deg

```{image} qGUI1.svg
:width: 600px
:align: center
```

3. Click on the Gain tab and select a taper—we don’t want any sidelobes!   
   1. (Blackman is the pre-programmed default for this lab)
4. Move the HB100 in an arc around the Phaser.

```{image} rotate.svg
:width: 600px
:align: center
```

5. Keep the HB100 pointed at Phaser, and move at a smooth/consistent speed
   1. With practice, it may look like this:

```{image} scan.svg
:width: 600px
:align: center
```

6. Our Blackman taper should have suppressed all the sidelobes.  So we are just seeing the true mainlobe at 15
7. Now, in the “Bits” tab:  slide “Phase Shift Bits” to 2.  This produces 90 deg phase steps (instead of the 2.8 deg phase steps that we normally have with the ADAR1000)
8. Repeat moving the HB100 in an arc.  

```{image} qGUI2.svg
:width: 600px
:align: center
```

9.  Do you see any new sidelobes?  


```{clear-content}
```
```{note}
For questions or help with the Phaser, please visit:
{ez}`adieducation/university-program`
```


