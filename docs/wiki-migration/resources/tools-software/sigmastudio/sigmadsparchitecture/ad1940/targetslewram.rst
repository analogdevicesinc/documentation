Target Slew Ram
===============

:doc:`Click here to return to the AD1940 Architecture page </wiki-migration/resources/tools-software/sigmastudio/sigmadsparchitecture/ad1940>`

Target/Slew RAM is a hardware-optimized function that allows volume or other parameter level changes to ramp to subsequent levels without audible clicks/pops.

| In audio systems, abrupt changes in volume position or other parameters produce unpredictable noises. See the sample schematic below showing possible real-time changes that can produce clicks/pops:
| |targetslew1.png|

| This noise arises from an audio signal getting scaled by a step function, which causes an unwanted response. The step function contains an impulse (Dirac delta function d(k)). It can be shown that the impulse d(k) is a frequency-limited white noise. This noise is unwanted in all audio applications. See below for a graphic representation of this signal noise caused by the step function:
| |targetslew2.png|

There are a couple of possible solutions to consider for this noise problem:

-  We can continuously write an incremented value to the DSP until we reach the desired value. Problems:

   -  Microcontroller-intensive
   -  Difficult to write because of timing and slope-shape considerations.

-  We can use target/slew RAM to automatically do the required ramping with one simple command without the need to mute the DSP. Below is the result:

| 
| |targetslew3.png|

SigmaStudio’s volume control and mux blocks both use the slew RAM to cleanly ramp volume from one level to another. Thus for the all the volume control cells, you have the option of using target/slew RAM as your algorithm to prevent the noise inherent in switching levels.

There are 4 types of slope that can be used with the target/slew RAM:

-  Linear -- fixed step size.
-  Constant dB -- uses instantaneous slew value to calculate the next step size. In dB, it is constant up and down.
-  RC-type -- Uses the difference between target and current values to calculate step size.
-  Constant -- values change linearly, in a fixed number of steps.

| For details, see the AD1940/1941 Volume Control Algorithms page.
| |targetslew4.png|

Although target/slew RAM is useful for eliminating unwanted noise, there are some drawbacks:

-  We are forced to write the values using the safeload registers.
-  We cannot read back from the target/slew RAM to verify the written value.
-  We can perform this functionality in software, although that will take possibly scarce program RAM (MIPS) and wouldn't be optimized.
-  Limited number: the 1940 currently has 64 target/slew RAM locations, which should be used only when a parameter or set of parameters is going to get modified at runtime in the final application.

.. |targetslew1.png| image:: https://wiki.analog.com/_media/targetslew1.png
.. |targetslew2.png| image:: https://wiki.analog.com/_media/targetslew2.png
.. |targetslew3.png| image:: https://wiki.analog.com/_media/targetslew3.png
.. |targetslew4.png| image:: https://wiki.analog.com/_media/targetslew4.png
