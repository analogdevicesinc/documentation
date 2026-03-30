# Beamforming

```{image} resources/overview.svg
:width: 400px
:align: right
```

In this pilot you will learn how to construct a two-channel digital beamformer using the **ADALM-PLUTO SDR** as the front-end.  
The basic concept is simple: two receive channels (two antennas) sample the same incident wavefront; by applying a relative phase shift between the two channels you can steer or focus the reception in a particular direction (or measure direction-of-arrival).  

We’ll replicate the key hardware setup, demonstrate digital phase shifting in Python, and show how to use the collected data to steer or detect signal direction.

```{toctree}
:maxdepth: 1
Beamforming Theory <bf_theory>
Beamforming Pilot Setup <bf_setup>
Beamforming Pilot Walkthrough <bf_practical>
```

**Further Reading:**
- {ez}`How to Construct a Beamformer with the ADALM-PLUTO <ez-blogs/b/engineerzone-spotlight/posts/how-to-construct-a-beamformer-with-the-adalm-pluto>`  
- {ez}`Turn Pluto into a Phased Array Beamformer <ez-blogs/b/engineerzone-spotlight/posts/turn-pluto-into-a-phased-array-beamformer>`  
- {ez}`Building a Monopulse Signal Tracker with ADALM-PLUTO <ez-blogs/b/engineerzone-spotlight/posts/building-a-monopulse-signal-tracker-with-adalm-pluto>`

```{clear-content}
```
```{note}
For questions or help with the Pluto SDR, please visit:
{ez}`adieducation/university-program`
```


