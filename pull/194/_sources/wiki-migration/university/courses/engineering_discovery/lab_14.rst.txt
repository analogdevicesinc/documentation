Push-Pull Class B and Class AB Amplifiers
=========================================

.. image:: https://wiki.analog.com/_media/analogTV>Video  Here
   :alt: analogTV>Video  Here
   :align: right

Introduction
------------

We learned that the conduction angle of a Class A amplifier is 360 degrees, meaning that the amplifying element is conducting current throughout the entire cycle of a sine wave that is being amplified. We saw that Class A amplifiers offer reasonable linearity, but have poor performance with respect to efficiency. We are now going to look at push-pull Class B and Class AB amplifiers, which are comprised of devices with conduction angles less than 360 degrees. These amplifiers can be made to be more efficient than Class A amplifiers, but suffer from a particularly undesirable form of distortion known as *crossover distortion*. We will investigate crossover distortion and some commonly-used methods to ameliorate it as we progress through the lab.

An ideal Class B amplifier has a conduction angle of 180 degrees, or one half-cycle of a sine wave. This type of amplifier therefore requires two amplifying elements to produce a full sine wave at its output. One of the elements conducts for the positive portion of the signal being amplified and the other conducts for the negative portion of the signal. For a sine wave, the positive portion of the signal is the positive 180 degree half-cycle of the waveform and the negative portion of the signal is the negative 180 degree half-cycle of the waveform. This is where the definition of the 180 degree conduction angle originates. An amplifier that uses two amplifying elements in this type of arrangement is often referred to as a *push-pull* Class B amplifier because one device pushes current into the load and the other pulls current from the load. Push-pull Class B amplifiers made with BJTs can be constructed using a NPN transistor for one element and a PNP transistor for the other element or with two of the same type of transistor. The NPN/PNP design is often called *complementary*, and requires the use of two complementary transistors that are well matched in their I\ :sub:`C` vs. V\ :sub:`BE` characteristics.

As we know, a BJT requires a V\ :sub:`BE` of approximately 0.7 V in order to operate in its forward active region. If we are designing the positive half-cycle section of a complementary push-pull Class B amplifier with a NPN BJT, we could connect the emitter to ground and drive the base directly. In this case the input voltage would have to rise to at least 0.5 V to 0.6 V just to begin to turn the transistor on. When the input was substantially less than this, the transistor would be off and no significant emitter or collector current would flow. This situation produces a *dead zone* on the amplifier input, meaning that the output is essentially "dead" until the input signal rises above 0.5 V to 0.6 V. We get a similar dead zone when we attach the PNP BJT for the negative half-cycle of the sine wave, producing an overall dead zone of +/- 0.5 V to 0.6 V on the amplifier input, meaning that the amplifier output is dead when the input signal is inside of this range. It is not completely correct to describe this type of amplifier as Class B, therefore, since no current flows in the devices in their dead zones, and this situation produces a conduction angle of less than 180 degrees. This undesirable type of distortion happens when the sine wave is *crossing over* from positive to negative, or negative to positive, and is appropriately called *crossover distortion*. Crossover distortion in a BJT-based push-pull Class B amplifier is generally unacceptable because it is so large, so we need to find ways to minimize it. The most common way is to provide a small amount of bias to each transistor such that they are just barely on when the signal crosses over from negative to positive or positive to negative. If we were to bias each transistor such that it is perfectly on the verge of conducting with no input signal applied, we would have something as close to a perfect push-pull Class B amplifier as we could achieve since the conduction angle for each device would be very close to 180 degrees. In other words, an extremely small input voltage would cause one of the transistors to go from the non-conducting state to the conducting state. Real transistors do not have a perfectly abrupt transition between non-conducting and conducting states, however, so we cannot achieve perfect Class B operation even with the bias added. The best solution is to bias each transistor such that it is conducting a small amount with no input signal applied. Because we are adding a small amount of bias in addition to what is required to overcome the base-emitter drop, the resulting amplifier is called a *Class AB* amplifier because it has a small amount of Class A bias in it to reduce the crossover distortion.

We can lower the crossover distortion if we bias the input voltage up at least 0.7 V on the positive half-cycle section and down at least 0.7 V on the negative half-cycle section of a complementary push-pull Class AB amplifier. By doing this to each section we can cancel out most of the ill effects incurred due to the V\ :sub:`BE` voltage drop. This can be accomplished are by using another transistor or diode to provide the V\ :sub:`BE` voltage drop, using a resistive voltage divider (not usually done for reasons we will see later), or some other equivalent means. Diodes and transistors that are used to shift the DC levels of signals are called *level shifters*.

Class AB amplifiers are often used as amplifier output stages in emitter-follower and common-emitter configurations. The common-emitter Class AB stage is used in rail-to-rail operational amplifier (op-amp) stages in order to allow the output voltage to swing very close to the power supply voltages. In this lab we will first build a push-pull class B common-emitter amplifier comprised of one NPN and one PNP transistor and use this to illustrate the large crossover distortion that is produced without transistor biasing. We then add biasing and observe how doing this significantly reduces the crossover distortion. In the "Theory" section we consider the problem of *thermal runaway* that can arise in the bias circuits of these amplifiers and how to minimize the likelihood of it happening. Providing a thermally stable, well-positioned bias point can be the most challenging part of a Class AB amplifier design.

Objective
---------

To study and understand push-pull Class B amplifiers constructed with BJTs as the amplifying elements and view the characteristic crossover distortion associated with them. To see how using level shifters to add a small amount of bias to the Class B amplifier sections to produce a push-pull Class AB amplifier can significantly reduce crossover distortion. To understand how the crossover distortion mechanism differs from other distortion mechanisms, and gets worse as a percentage of signal amplitude as the output signal gets smaller. To understand how thermal runaway can occur in Class AB amplifiers and investigate techniques to prevent it. Following completion of this lab you should be able to explain the basic operation of push-pull Class B and Class AB amplifiers that use BJTs as the amplifying elements, describe crossover distortion, explain how and why it happens, and how it differs from distortion caused by other mechanisms, describe what level shifters do, and explain what can cause thermal runaway in Class AB amplifiers, why it can be dangerous, and how it can be prevented.

Materials and Apparatus
-----------------------

-  Data sheet handout for the 2N3904 NPN transistor
-  Data sheet handout for the 2N3906 PNP transistor
-  Computer running PixelPulse software
-  Analog Devices ADALM1000 (M1K)
-  Solderless breadboard and jumper wires from the ADALP2000 Analog Parts Kit
-  (2) 2N3904 NPN transistor from the ADALP2000 Analog Parts Kit
-  (2) 2N3906 PNP transistor from the ADALP2000 Analog Parts Kit
-  (4) 1.1 Ω resistor from the ADALP2000 Analog Parts Kit
-  (1) 100 Ω resistor from the ADALP2000 Analog Parts Kit
-  (2) 1.0 KΩ resistor from the ADALP2000 Analog Parts Kit

Procedure
---------

-  Construct the following circuit on the solderless breadboard\


|lab_14_image_1.png|

-  Refer to the illustration below for one way to install the components in the solderless breadboard\

|lab_14_assembly_image_1.png|

-  Run PixelPulse and plug in the M1K using the supplied USB cable
-  Update M1K firmware, if necessary
-  Set up the M1K to source voltage/measure current on Channel A and measure voltage on Channel B
-  Set up Channel A source waveform for a 50 Hz “Sine” output that swings between 0.5 V and of 4.5 V
-  Observe the output voltage at the connection between the two emitters on Channel B and observe the large amount of crossover distortion that is present in the output signal as shown in the image below\

|lab_14_image_2.png|

-  Construct the following circuit on the solderless breadboard\

|lab_14_image_3.png|

-  Refer to the illustration below for one way to install the components in the solderless breadboard\

|lab_14_assembly_image_2.png|

-  Set up Channel A source waveform for a 50 Hz “Sine” output that swings between 1.0 V and of 4.0 V
-  Observe the output voltage at the connection between the two emitters on Channel B and observe how the crossover distortion has been significantly improved due to the addition of the level shifting transistors, connected as diodes
-  Estimate the voltage loss factor due to the voltage divider formed between the amplifier output resistance and the load resistance
-  Increase the input voltage amplitude to swing between 0.5 V and 4.5 V and observe the output waveform clipping that occurs due to the headroom loss incurred by the level shifters

Theory
------

In the lab we observed the serious crossover distortion in a BJT-based push-pull Class B amplifier that occurs due to the required ≈ 0.7 V V\ :sub:`BE` bias voltage. The clear solution to this problem was to add just enough DC bias voltage such that each transistor is slightly conducting collector current with no signal applied to the amplifier input. This solution works quite well, but has a few drawbacks, one of which is the potential for thermal runaway.

Thermal runaway is a form of positive feedback, sometimes referred to as a self-reinforcing feedback loop, in which a change in a system operating condition pushes the system away from a desired stable point instead of toward a stable point. Stable systems are designed using *negative feedback* in which changes in the system operating conditions push the system back toward its desired stable state. A simple example of a naturally-occurring negative feedback system is the system that regulates the amount of light that enters the eye by controlling the diameter of the iris diaphragm. When the light entering the eye increases beyond the ideal amount, the iris diaphragm decreases in diameter until the light reaches its ideal level. Similarly, when the light entering the eye decreases below the ideal level, the iris diaphragm increases until the light reaches its ideal level. Thus, negative feedback drives the system to *decrease* the error between an ideal condition and the actual condition. Positive feedback systems do just the opposite of negative feedback systems. A simple example of thermal runaway is what can can occur in carbon composition resistors that have negative temperature coefficients (NTC), that is, the resistances of these resistors decrease with temperature. As a NTC resistor heats up its resistance decreases, causing it to draw more current, which further decreases its resistance, causing it to draw even more current, and so on. If not limited by something, this process can continue until the resistor overheats and destroys itself.

Thermal runaway in BJT-based push-pull Class AB amplifiers occurs due to the negative temperature of the base-emitter voltage V\ :sub:`BE`. The V\ :sub:`BE` temperature coefficient is typically about -2 mV/°C. The worst bias arrangements for Class AB amplifiers with respect to thermal runaway are those that use bias voltages that are relatively fixed over temperature. A resistive voltage divider network provides bias voltages that are relatively fixed with temperature, and this is why they are not widely used as Class AB amplifier bias circuits. The following schematic illustrates a simple resistive voltage divider bias circuit that could be used to bias a BJT-based Class AB amplifier.\


|lab_14_image_4.png|

The resistor values would be chosen such that R\ :sub:`B1` = R\ :sub:`B4` and R\ :sub:`B2` = R\ :sub:`B3`. A potentiometer could also be placed between the two bases with a slightly different arrangement to provide an adjustable bias. In the schematic above the input signal would be applied between R\ :sub:`B2` and R\ :sub:`B3`. When properly designed, the voltage between the two bases would be equal to 2V\ :sub:`BE`\ (on) where V\ :sub:`BE`\ (on) is defined as the base-emitter voltage at which each transistor begins to conduct. The thermal runaway problem with fixed bias can now be addressed. As the base-emitter junction temperature increases, due to self-heating as well as potential ambient temperature increase, the base-emitter voltage would decrease by -2 mV/°C if it were not fixed by the resistive bias network. The collector current and base-emitter voltage have an exponential relationship, which must be obeyed. Since the base-emitter voltages are not allowed to decrease due to the fixed bias voltages provided by the voltage divider, the collector current increases instead according to the exponential dependence of I\ :sub:`C` on V\ :sub:`BE`. This arrangement presents an exponential dependence of collector current on temperature. As the collector current increases the base-emitter junction temperature increases, further increasing the collector current. Much as was the case in the carbon composition resistor, we have an unstable self-reinforcing feedback loop in the amplifier which produces thermal runaway, and will eventually destroy the transistors. Fortunately, there are a number of better biasing schemes that can be used to avoid thermal runaway.

If we replace R\ :sub:`B2` and R\ :sub:`B3` with forward biased diodes, or transistors configured as diodes, we can cancel out the effects of the negative V\ :sub:`BE` temperature to a great degree as long as the current vs. voltage characteristics of these devices are well matched to those of the transistors in the amplifier and the temperature of all devices are very close. This is what we did in the lab when we added the transistors connected as diodes to the Class B amplifier to change it to a Class AB amplifier. A further improvement can be made to the circuit by converting the transistors connected as diodes to emitter follower stages, providing a high input impedance to the amplifier. This type of arrangement is commonly called a *diamond* stage. We can follow the bias voltage in the upper signal path as going up a V\ :sub:`BE` drop in the diode and down a V\ :sub:`BE` drop in the upper NPN transistor. Similarly, for the lower signal path we go down a V\ :sub:`BE` drop in the diode and up a V\ :sub:`BE` drop in the PNP transistor. Sometimes, however, this thermal compensation may not be enough to entirely avoid thermal runaway, since devices are not perfectly matched, and temperatures can vary between devices. A heat sink, if available, can be used to help equalize the temperature among all of the devices if all of the devices are thermally connected to it. Another technique that is often used is to place small resistors in series with the emitters of the amplifier transistors. Doing this produces negative feedback in the same was as discussed in the "Class A NPN Common-Emitter Amplifier" lab. This is why we placed the two 1.1 Ω resistors in series with the emitters of the two transistors.

Crossover distortion is worse than other types of distortion since it is not reduced as a percentage of signal amplitude as the signal amplitude is reduced. Other distortion mechanisms produce harmonic distortion (distortion of the shape of a sine wave from its ideal shape) that scale with amplitude over a wide dynamic range, giving a rather constant percentage of harmonic distortion as the signal amplitude is varied. Crossover distortion, on the other hand, does not decrease with signal amplitude -- the dead zones stay the same -- so the distortion percentage in a signal actually increases as its amplitude decreases. Fortunately, negative feedback is often provided around amplifiers with push-pull Class AB output stages, which significantly reduces signal distortions. Clearly, the amplifiers themselves should be designed to produce minimal crossover distortion without the negative feedback.

Observations and Conclusions
----------------------------

-  Ideal Class B amplifiers have conduction angles of 180 degrees
-  Two Class B amplifiers are required to amplify a sine wave -- one for each half-cycle of the sine wave
-  Two Class B amplifiers configured such that one amplifies the positive half-cycle and the other amplifies the negative half-cycle are commonly referred to as push-pull Class B amplifiers
-  Push-pull Class B amplifiers can be designed using two of the same type of transistors or two complementary transistors
-  Class B amplifiers produce significant crossover distortion, which is highly undesirable
-  A small amount of bias can be added to a Class B amplifier to form a Class AB amplifier, which has considerably less crossover distortion than a Class B amplifier
-  Single Class AB amplifiers can be combined to form push-pull Class AB amplifiers
-  Adding bias can produce thermal runaway, and avoiding the use of fixed bias sources can help avoid thermal runaway
-  Diodes, transistors connected as diodes, and emitter follower stages can be used to implement bias that has temperature compensation that reduces the likelihood of thermal runaway
-  In order to minimize the likelihood of thermal runaway, all devices should be kept at the same temperature; one way to implement this is to thermally connect all devices to the same heat sink
-  Small resistors can be placed in series with the emitters of Class AB emitter-follower amplifier stages in order to provide negative feedback in the bias circuit that can help prevent thermal runaway

**Return to** :doc:`Engineering Discovery Index </wiki-migration/university/courses/engineering_discovery>`

.. |lab_14_image_1.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_14_image_1.png
   :width: 800px
.. |lab_14_assembly_image_1.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_14_assembly_image_1.png
   :width: 1000px
.. |lab_14_image_2.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_14_image_2.png
   :width: 1000px
.. |lab_14_image_3.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_14_image_3.png
   :width: 800px
.. |lab_14_assembly_image_2.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_14_assembly_image_2.png
   :width: 1000px
.. |lab_14_image_4.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_14_image_4.png
   :width: 200px
