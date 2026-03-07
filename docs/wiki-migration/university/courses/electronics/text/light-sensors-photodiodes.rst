Photodiodes and other Light Sensors
===================================

**By James Bryant**

This article has been written to answer a number of questions that the author has encountered, as an analog applications engineer, concerning the characteristics of photosensors and photosensor interface circuitry - both for AC and DC applications. Except inasmuch as they all use photosensors and their interface circuitry, it is not about digital photography, spectrophotometry, optical signalling, security systems, robotics or any other system depending on photosensors - it is just about the interface from an optical to an electronic signal. The main text discusses the way that most photocells work in not too demanding applications - the copious footnotes mention second- and third-order effects which may sometimes be important but can usually be checked and then ignored.

For the purposes of this article light consists of electromagnetic radiation in the visible (wavelengths approximately 400-800 nm), near infrared\ :sup:`[1]` (IR-A: 800-1400 nm or perhaps a little beyond) and near ultra-violet\ :sup:`[1]` (UV-A: 320-400 nm or, again, perhaps a little beyond) regions. Not all light sensors respond to all wavelengths in this range and it is important, when choosing one, to be aware of how its sensitivity varies with wavelength.

We shall mostly discuss photodiodes, as they are the cheapest light sensors, and generally the easiest to use, but there are several other light sensors of which analog engineers should be aware.

Vacuum Photocells
-----------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/cphotodio_f1.jpg
   :align: center
   :width: 500px

.. container:: centeralign

   Fig 1A The Phototube - the first Photosensor


The first such sensor was the "phototube" or "photo-electric cell" (Fig 1A) which consists of a photo-sensitive cathode in a vacuum (or, sometimes, very low-pressure gas) tube which when illuminated emits electrons which move to a positively biased anode, allowing a current to flow which is proportional to the light intensity. Simple vacuum photocells are rarely used today, but photomulipliers, which use secondary emission from multiple electrodes (dynodes) at stepped potentials (Fig 1B) to multiply each electron from a photocathode by up to 160 dB, are essential photosensors in nuclear and particle physics, astronomy, medical imaging, motion picture film scanning, radar countermeasures, and the high-end image scanners known as drum scanners. Their combination of high gain, low noise, very fast response, and large light collection area cannot presently be matched by any solid-state circuitry and photomultipliers are an application of vacuum-tube technology which is still at the forefront of valuable electronic techniques. The technology is also used in night vision devices.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/cphotodio_f2.jpg
   :align: center
   :width: 500px

.. container:: centeralign

   Fig 1B Photomultiplier - Simplified Diagram and an actual Device


Photoresistors
--------------

Another type of light sensor uses the variation of electrical resistance with illumination exhibited by some materials (the most usual are Cadmium Sulphide [CdS]and Cadmium Selenide/Sulphide [Cd\ :sub:`2`\ SeS]) to make "photoresistors\ :sup:`[2]`". Until recently such photoresistors were the commonest form of photosensor despite their slow response to changing light input, but the combined effects of lower photodiode prices and legal limitations on the use of cadmium because of its toxicity\ :sup:`[3]` have reduced their use in recent years.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/cphotodio_f3.jpg
   :align: center
   :width: 250px

.. container:: centeralign

   Fig 2 Inexpensive CdS Photoresistor


Photoresistors are still commonly used in combination with a variable light source (originally an incandescent bulb - now almost invariably an LED) as isolated variable resistors\ :sup:`[4]` - since they are resistors they are not polarized (they may be connected either way round) and will work with alternating current.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/cphotodio_f4.jpg
   :align: center
   :width: 500px

.. container:: centeralign

   Fig 3 Photoresistor Gain Control


Photoresistors using more exotic materials (lead sulphide [PbS], indium antimonide [InSb] and copper doped germanium) are invaluable and at present unreplaceable as photodetectors in the mid- and far-infrared.

The conductance\ :sup:`[5]` of a photoresistor is proportional to the intensity of the light falling on it. This means that the current in a photoresistor having a fixed voltage across it is proportional to the incident light (the constant of proportionality will vary with the wavelength and the device temperature - read the data sheet\ :sup:`[6]` of the device for details).

In addition to their photoresistance there is also a very high (megohms or tens of megohms) "leakage" or "dark resistance" in parallel with it which allows a very small current to flow when the device is not illuminated. With some CdS devices this dark resistance can depend on whether or not the device has been illuminated within the last few hours, or even days, making such photoresistors unsuitable for very high precision measurement since their leakage depends on their recent illumination history.

Photodiodes & Phototransistors
------------------------------

The majority of this article concerns photodiodes. A semiconductor diode is a crystalline piece of semiconductor material containing a p-n junction with connections to the P and N regions - its operation is discussed in Appendix A. All semiconductor diodes are, to some extent, photodiodes, but some are much more sensitive than others.

For the purposes of simplified analysis we can model a photodiode as an ideal (non-photosensitive) diode in parallel with a light-dependent current source. This current source is quite linear - the current is more or less proportional to the incident light over a range of 1000:1 or better - but the range of wavelengths to which it is sensitive depends on the material of which the diode is made.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/cphotodio_f5.jpg
   :align: center
   :width: 500px

.. container:: centeralign

   Fig 4 An Ideal Diode.


.. container:: centeralign

   (Its reverse leakage current is too small to be evident.)


An ideal diode with reverse bias (i.e. its anode is negative with respect to its cathode) acts as an insulator, but has a small temperature dependent leakage current, largely independent of the reverse bias voltage\ :sup:`[7]`, which doubles with every 10°C increase in the device temperature. There is also a small capacitance in parallel with the diode, which decreases as the reverse bias increases.

With forward bias (anode positive) the diode current increases exponentially with voltage (see Appendix A for the equations), but from a practical point of view the current is too small to matter until a "threshold" or "knee" voltage is reached. This voltage depends on the diode material and can vary from 200 mV for silicon Schottky diodes to some 4 V for blue LEDs using gallium nitride - normal silicon diodes have a threshold around 700 mV. The threshold voltage decreases with increasing device temperature, and the parallel capacitance of a forward biased diode increases with the bias voltage.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/cphotodio_f6.jpg
   :align: center
   :width: 500px

.. container:: centeralign

   Fig 5 Ideal Semiconductor Photodiode


An illuminated photodiode contains an ideal diode and a light dependent current source (and some voltage variable capacitance). The photocurrent is KL where K is a constant depending on the photodiode and the light wavelength(s) and L is the light intensity (note that K is a characteristic of the particular photodiode, it is not k, which is Boltzmann's constant - 1.3806E-23 JK\ :sup:`-1`). If the photodiode is open-circuit or loaded only with a very high resistance the anode will be sufficiently positive for the photo current to flow in the diode and the voltage across the photodiode will be proportional to the logarithm of the light intensity. It is possible to measure this behaviour using an electrometer op-amp with very low bias current such as the AD549 (I\ :sub:`b` ˜ 40 fA) but photodiodes are rarely used in exactly this way.

There are two practical modes of photodiode operation - photoconductive mode and photovoltaic mode.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/cphotodio_f7.jpg
   :align: center
   :width: 500px

.. container:: centeralign

   Fig 6 Photodiode in Photoconductive Mode


If the photodiode is reverse biased its current will be the sum of its leakage and its photocurrent and its capacitance will be lower than when it is forward biased - which is convenient when measuring HF modulated light. The associated circuitry is designed to amplify this current. This is the photoconductive mode of operation. (It is possible to amplify the photocurrent of an unbiased photodiode by injecting it into an op-amp summing junction but its capacitance is slightly higher in this "photovoltaic current mode".)

Not only are diodes light sensitive - most transistors, which, after all, also contain P-N junctions, are photosensitive as well. Half a century ago it was well-known to amateur electronic experimenters that if the black paint was removed from the glass package of the Mullard\ :sup:`[8]` OC71 germanium transistor it became light sensitive - in fact it had almost exactly the same characteristics as the OCP71 phototransistor which cost five times as much! Few people bought the more expensive part until eventually Mullard redesigned the package of the OC71 so that removing the paint still did not allow light to reach the transistor structure.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/cphotodio_f8.jpg
   :align: center
   :width: 500px

.. container:: centeralign

   Fig 7 Phototransistor


A phototransistor is a transistor with its base-collector junction deliberately made more strongly light sensitive. Often it has no external base connection. The photocurrent of the diode flows in the base-emitter circuit and is amplified by the transistor current gain, ß. The sensitivity of a phototransistor is therefore ß (~30-200) times greater than that of a similar diode. However the switching times of phototransistors with an unconnected base are slow (typical phototransistors have rise and fall times of the order of 10-20 µs, and the fastest only 500-1000 ns). They are always used in the photoconductive mode described above, and may be convenient when a single photosensing device is required to operate a relay. If the base connection is available, connecting a resistor from base to emitter reduces photosensitivity and increases the turn-on threshold, but does improve desaturation time and therefore speeds up the transistor turn-off.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/cphotodio_f9.jpg
   :align: center
   :width: 500px

.. container:: centeralign

   Fig 8 Photodiode used in (Photovoltaic) Voltage Mode


If a photodiode is shunted with a resistor, chosen so that when the maximum expected\ :sup:`[9]` photocurrent flows in it the voltage is 20% below the threshold voltage of the diode, the circuit will have an output voltage proportional to the incident light and output impedance equal to the value of the resistor (shunted by the diode capacitance). With this photovoltaic configuration the associated circuitry is voltage driven.

If we go to the websites of the major electronic component distributors we find that the cheapest photodiodes cost some 15¢ and are infra-red (IR) sensitive silicon with a threshold voltage of about 700 mV whereas the cheapest LEDs are under 4¢ and have a threshold 2-5 times larger. These inexpensive LEDs are sensitive to visible light, and are, in many cases, as sensitive as purpose-made photocells when used as such. Of course purpose-made photodiodes are characterised and tested for photodiode specifications and are likely to have faster response times than LEDs - but LEDs are not hard to characterise, can be selected for specific spectral characteristics, and can often serve a dual purpose in a system, acting both as an indicator light and an ambient light meter, or an optical transmitter and receiver. The ATMega328 microcontroller used in the Arduino (and Analog Devices' ADuC7023 and many of their other analog microcontrollers including their latest\ :sup:`[10]` the ADuCM320) have some ports which can be configured both as digit input/outputs and very high impedance analog-digital converter (ADC) inputs. An LED and two resistors on such ports allows a single pin both to control an indicator lamp and to measure ambient illumination.

LEDs used as photodiodes are insensitive to wavelengths longer than their own peak output wavelength. Of course if they are encapsulated in coloured plastic their response will be affected by this, but LEDs in clear plastic\ :sup:`[11]` often, but by no means always (check the device you intend to use), have quite a broad response to wavelengths shorter than their own\ :sup:`[12]`. Silicon photodiodes are more sensitive in the near IR down to 1000 nm and less sensitive to visible wavelengths\ :sup:`[13]`.

Single coloured LEDs are simple diodes and have more or less monochromatic light output\ :sup:`[14]` and, of course, multi-coloured LEDs are simply arrays of two or more single coloured ones. White LEDs are made in several different ways and are quite complex. Most of them act as photodiodes, but their characteristics will probably be more complex too - this is not to say that they cannot be used as photodiodes, but a warning that their spectral sensitivities, and their electronic characteristics, may need to be checked carefully when doing so. It should go without saying that complex devices containing LEDs plus other circuits\ :sup:`[15]` are unsuitable for use as photodiodes.

Appendix B contains a brief discussion of the photocell measurement techniques which allow simple characterization of an LED as a photodiode.

**Lab Activity:** :doc:`LEDs as light sensors </wiki-migration/university/courses/electronics/electronics-lab-led-sensor>`

Photocell Applications
----------------------

In this section we shall discuss the interface between a photosensor and its associated electronics. There are really just two photocell applications - light measurement, and the reception of modulated light.

When we measure light we may be measuring its intensity, or we may simply be detecting if it is present. We have seen that photodiodes have photocurrent and photoresistors have conductance proportional to the light falling on them (in this section we shall not discuss varying spectral sensitivity). If we measure the photocurrent (in the case of the photoresistor with a defined bias voltage) we can measure the incident light.

For photometry (lux meters, exposure meters, closed-loop light control systems, etc.) we may wish to do this accurately, for many photocell applications we simply need to know if light is present or not - although, almost always, "present" really means present above some low ambient level. If the light that we are detecting is the output of an LED, and other light may be present, it is usually better to modulate the LED output and discriminate between the modulated light and background illumination. We shall discuss this later.

The classical photodetector uses a photocell (photodiode in current mode or photoresistor), in series with a resistor, R\ :sub:`s` , and a transistor. The resistor is chosen such that when the light intensity is large enough the transistor is switched on or off.

The transistor may be a bipolar junction transistor (BJT), a Darlington transistor, or a MOSFET. In the past BJTs were often used as being cheaper than MOSFETs but this no longer the case and the best choice actually is a MOSFET. Its output may be a relay, or a resistor with a logic output taken from the drain/collector, or an open-circuit drain/collector intended for "wired-OR" logic connection. It is possible to either use N-channel/NPN or P-channel/PNP devices, but since the circuitry involved is exactly the same for both, with the exception of polarity reversal, all the examples and calculations in this article assume the use of N-channel/NPN devices.

It is quite difficult to write an algorithm to determine the value of R\ :sub:`s`, which is why it is often determined by experiment (or even adjusted with a potentiometer in each individual system!) This is because it is generally hard to predict the light intensity at the photocell in a given system, and in many cases it is also hard to determine the photocell's sensitivity to the actual colour of light used.

The threshold voltage, V\ :sub:`th`, of a transistor is the input voltage (gate-source or base-emitter) at which its output (drain or collector) starts to conduct. Different manufacturers use different symbols (V\ :sub:`gs(th)`, V\ :sub:`gs0`, etc.). Values of threshold current for "starts to conduct" will vary from device to device but since small changes of input voltage in this region produce large changes in output current it does not usually matter very much for our calculations what value of threshold current is chosen.

A BJT turns on when its base-emitter voltage is about 700 mV, a bipolar Darlington transistor at around 1300 mV, and a small-signal MOSFET will usually have V\ :sub:`th` in the range 900-2400 mV (RTFDS\ :sup:`6)` High voltage MOSFETs may have higher values but are not often used in photocell circuitry.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/cphotodio_f10.jpg
   :align: center
   :width: 500px

|

.. container:: centeralign

   Fig 9 Classical Photodetector - Transistor conducts when light is present


   | (Diagram shows the possible devices which might be used)


The commoner arrangement has the transistor conduct in the presence of light, turning on a relay load or producing logic 0 on an N-channel/NPN drain/collector. The voltage drop across R\ :sub:`s` must be equal to V\ :sub:`th` when I\ :sub:`t` (the photocell current at the switching threshold) flows in it. With a photodiode I\ :sub:`t` is more or less independent of its bias voltage, so

:math:`R_s = V_th / I_t` [1]

but with a photoresistor

:math:`I_t = ( V_s - V_th ) / R_t` [2]

or

:math:`I_t = ( V_s - V_th ) G_t` [3]

where V\ :sub:`s` is the supply voltage and R\ :sub:`t` is the threshold resistance (or G\ :sub:`t` is the threshold conductance) of the photoresistor. This gives a value of R\ :sub:`s` defined by the equations

:math:`R_s = V_th R_t / ( V_s - V_th )` [4]

or

:math:`R_s = V_th / G_t ( V_s - V_th )` [5]

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/cphotodio_f11.jpg
   :align: center
   :width: 500px

|

.. container:: centeralign

   Fig 10 Classical Inverting Photodetector - Transistor conducts when light is not present


   | (Diagram shows the possible devices which might be used)


The other arrangement (the inverting photodetector) has the transistor turned off in the presence of light, turning off a relay load or producing logic 1 on an N-channel/NPN drain/collector. In this case the voltage drop across R\ :sub:`s` must be equal to (V\ :sub:`s`-V\ :sub:`th`) when I\ :sub:`t` (the photocell current at the switching threshold) flows in it. Again the photodiode equation is simple

:math:`R_s< = ( V_s - V_th ) / I_t` [6]

but with a photoresistor

:math:`I_t = V_th / R_t` [7]

or

:math:`I_t = V_th G_t` [8]

where V\ :sub:`s` is the supply voltage and R\ :sub:`t` is the threshold resistance (or G\ :sub:`t` is the threshold conductance) of the photoresistor. This gives a value of R\ :sub:`s` defined by the equations

:math:`R_s = ( Vs - V_th ) R_t / V_th` [9]

or

:math:`\displaystyle R_s = \frac{ Vs-V_th }{G_t} V_th` [10]

A photodiode working in photovoltaic mode will also act as a photodetector. Its shunt resistor R\ :sub:`s` is selected so that when I\ :sub:`t` flows in it the voltage is the V\ :sub:`th` of the device it is driving.

:math:`R_s = V_th /I_t` [11]

Obviously the photodiode material selected for this application must have a conduction threshold voltage which is larger then V\ :sub:`th`. This usually means that a photodiode used in this way will not be a silicon device\ :sup:`[16]`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/cphotodio_f12.jpg
   :align: center
   :width: 500px

|

.. container:: centeralign

   Fig 11 Photodetector using a Photodiode in Photovoltaic Mode

   | V\ :sub:`th(Photodiode)` > V\ :sub:`th(Transistor)`
   | (Diagram shows the possible devices which might be used - it does not work with a photoresistor.)


If a bipolar device - a BJT or even a Darlington - is used in any of the circuits in Figs 9-11 its minimum base current when the load is turned fully on should be no more than 20% of I\ :sub:`t`. If the collector load resistance (resistor or relay) is R\ :sub:`L` and the supply V\ :sub:`s` the collector current will be V\ :sub:`s`/R\ :sub:`L`, and the minimum base current, I\ :sub:`b(min)`, V\ :sub:`s`/ßR\ :sub:`L` where ß is the current gain of the bipolar device. So

:math:`I_t = 5V_s /ßR_L` and therefore :math:`R_L = 5V_s /ßI_t` [12]

otherwise the base current required to switch the bipolar device may be too large for the network formed by the photocell and R\ :sub:`s` to supply. If the load is a relay and it is not possible to use a relay with a sufficiently large R\ :sub:`L` the bipolar device should be replaced with a MOSFET. (It is reasonable to assume that the worst case minimum ß of a simple BJT is 30, and that of a small-signal Darlington is 500.)

The problem with all these circuits is that if the light value is close to the threshold the transistor acts as a (fairly) linear amplifier and produces small changes in output in response to electrical or optical noise. If the optical part of the system has a large light change and no delays close to the threshold this is unlikely to be a problem - but otherwise a different circuit is necessary.

The simplest circuit uses a Schmitt trigger input logic gate. These are logic circuits with analog positive feedback on their input stages such that as the input voltage on a logic input increases from zero there is no change of logic output until the input is (very roughly) around 50-60% of the supply voltage when the output changes its logic state. Many logic gates have a linear region where they act as (poor quality) amplifiers but these devices switch very quickly from one state to the other when the input reaches a threshold value. If the input is now reduced the output does not change back until the input has reduced by approximately 30% of the supply voltage. (Note that these values vary quite widely with device types, the supply voltage used, and even from device to device - these devices have excellent hysteresis but are not precision level sensors.)

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/cphotodio_f13.jpg
   :align: center
   :width: 500px

|

.. container:: centeralign

   Fig 12 Photodetectors with Hysteresis


   | (This diagram shows the possible input device configurations and an optional relay driver.)


Such Schmitt input logic gates are available with supply ranges between 2 V and 18 V (no single part has this wide a range - but parts are available that may be used with any supply from 3 V to 18 V). They are available in traditional DIL and SOT packages with 4 or 6 gates in a package (the "4000 Series" 4093 and 40106 for example) or as single or dual buffers or inverters in a tiny SO-23 package for as little as 6 cents in large quantities (the Toshiba TC4S584F and many others).

The range of threshold voltages for different supplies will be given on the data sheet and can be used in equations [1] [4] [5] [6] [9] [10] & [11] to calculate suitable values of R\ :sub:`s`.

These Schmitt gates are inexpensive, convenient and easy to use - but not very accurate. Nevertheless they are accurate enough for many light threshold sensing operations and are probably the ideal choice for the majority of non measuring light sensing applications. We could replace one with a Schmitt trigger built from discrete components but this would cost more, use more components and board area, and almost certainly consume more power. The output of these Schmitt input gates is a logic level (some of them are inverters, some are buffers - make sure you know which you are using - the one shown in Fig 12 is a non-inverting buffer). If relay operation is required drive it with a MOSFET connected to the Schmitt output. This is also shown as an option in Fig 12.

Where we need greater accuracy a comparator (or an ADC - see below) is necessary. A comparator is a device with two inputs and a logic output\ :sup:`[17]`. The output indicates which of the two inputs is more positive than the other, so if we connect a photocell in series with a resistance across a voltage V\ :sub:`s` and the centre tap to one input of a comparator and a voltage reference (V\ :sub:`ref`) to the other the logic will indicate quite precisely whether or not the signal voltage in the photocell circuit is larger or smaller than the voltage reference. With suitable calibration this allows us to make accurate light comparisons. A comparator may also be driven by a photodiode working in the photovoltaic mode.

Comparators sometimes have built-in hysteresis and can almost always have hysteresis added by simple additional circuitry. Fig 13 shows this done with two resistors (which may be omitted if hysteresis is not needed). The articles referred to in the footnote\ :sup:`[17]` discuss the correct resistor values and other issues concerning comparators in more detail.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/cphotodio_f14.jpg
   :align: center
   :width: 500px

|

.. container:: centeralign

   Fig 13 Accurate Photodetector using a Comparator

   | (Diagram shows the possible configurations which might be used)


The equations relating the photocell characteristics, V\ :sub:`ref`, and R\ :sub:`s` are very similar to Equations [1] - [10] except that V\ :sub:`th` becomes the reference voltage V\ :sub:`ref`.

The best way to measure a range of photocell outputs accurately is with an analog interface circuit, either using an operational amplifier, or driving a suitable analog-digital converter (ADC) directly from a photocell.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/cphotodio_f15.jpg
   :align: center
   :width: 500px

.. container:: centeralign

   Fig 14 Voltage Output Photodiode Circuits


The outputs of the photodiode circuits in Fig 14 are voltages, proportional to incident light, which may be amplified by an operational amplifier or sent directly to the input of an ADC with a large enough Z\ :sub:`in` that it does not load the circuit driving it.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/cphotodio_f16.jpg
   :align: center
   :width: 400px

.. container:: centeralign

   Fig 15 Voltage Output Photoresistor Circuits (non-linear)


The voltage outputs of the photoresistor circuits in Fig 15, while quite predictable, are not simply proportional to incident light and require linearization - which is one reason why it is better to use photodiodes than photoresistors.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/cphotodio_f17.jpg
   :align: center
   :width: 500px

.. container:: centeralign

   Fig 16 Simplified Diagram of a Switched Capacitor ADC Input


The input of many, if not most, ADCs contains switched capacitors which draw high frequency (HF) currents. The input should therefore have a small capacitor to ground very close to the ADC to ensure that these HF currents flow to local ground and not to the photocell, buffer amplifier or elsewhere in the system\ :sup:`[18]`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/cphotodio_f18.jpg
   :align: center
   :width: 500px

.. container:: centeralign

   Fig 17 Decoupling an ADC's Analog Inputs


Read the ADC data sheet and any application notes for discussion of suitable values and their effect on the performance of the ADC and of the system where it is used.

The best interface between a photodiode and an op-amp is a current to voltage converter, which works with a photoresistor as well, provided the photoresistor bias voltage is maintained constant. This is shown in Fig 18.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/cphotodio_f19.jpg
   :align: center
   :width: 500px

.. container:: centeralign

   Fig 18 Driving a Current-Voltage Converter from a Photocell


The current from the photocell flows into the summing junction at the op-amp's inverting input. Negative feedback works to maintain the same voltage on the inverting and non-inverting inputs, so the output voltage on R\ :sub:`fb` causes the current in it to be equal to the photocell current. Obviously this circuit requires an op-amp with bias current much less than the photocurrent, which is why such circuits usually use FET input op-amps.

If we wish to measure AC photocurrent but are not interested in the DC or randomly varying photocurrent due to ambient light there are two possible techniques. The simplest is to limit the gain of the amplifier in Fig 18 by reducing R\ :sub:`fb` so that the amplifier will not be overdriven by the largest possible AC + DC photocurrent the system is expected to encounter. The AC component of the signal is then capacitively coupled to a second amplifier with sufficient gain for the application.

Or we can connect the photocell in series with a suitable inductor which will ground the DC component of its signal. We then connect the AC signal to an amplifier. If the signal bandwidth is narrow the inductor can be shunted with a capacitor to make a parallel-tuned LC circuit of suitable Q to give narrow bandwidth and high in-band gain. If a tuned circuit is used it should drive a voltage amplifier with high input impedance so as not to degrade the Q. This amplifier should not drive an inductive load or the interaction of the load and the feedback ("Miller") capacitance may cause instability.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/cphotodio_f20.jpg
   :align: center
   :width: 400px

.. container:: centeralign

   Fig 19 Narrow Band Tuned Circuit Photocell Load with AC Amplifier


If an untuned inductor is used as a simple high AC/low DC impedance the variation of impedance with frequency can be avoided by using an AC current-voltage converter (transimpedance amplifier) rather than a voltage amplifier. This effectively short-circuits the inductor at AC (which is why it does not work with a tuned circuit) as the AC current from the photocell flows to the virtual ground of the amplifier inverting input.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/cphotodio_f21.jpg
   :align: center
   :width: 400px

.. container:: centeralign

   Fig 20 Inductive Photocell Load with AC Current-Voltage Converter


Inductors for the applications in Figs 19 & 20 must be chosen so that they can carry the maximum expected photocurrent without saturation - this is unlikely to be a problem, but should not be overlooked.

Photodetectors using a modulated signal source, which I mentioned earlier in this article, can detect the modulation using one of the above amplifier schemes and some sort of frequency detector. There is plenty of tone detection software available if the signal is digitized, but the simple NE567 PLL IC, first manufactured nearly forty years ago by Signetics and still available from a number of manufacturers, (prefixes vary, but the 567 is constant) is all that is needed for this application.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/cphotodio_f022.jpg
   :align: center
   :width: 400px

.. container:: centeralign

   Fig 21 Tone Detector for Modulated Beam Systems using a 567 PLL


The values of C1 and C2 in the above diagram depend on the tone frequency to be detected. For more detail consult the 567 data sheet, but with AC input = 200 mV rms the tone frequency F is determined by C1 and the detection bandwidth by C2. The equations are:

:math:`\displaystyle F = \frac{1}{2}.42 C1` [13]

:math:`\displaystyle BW = 1070sqrt(\frac{1}{5}FC) %` [14]

(BW is calculated as a percentage of F.)

There are innumerable other applications of photosensors, but this article is intended only to discuss their characteristics and how to use them, not to consider the systems where they are used.

| James Bryant
| Calshot - England
| August 2014

**Return to** :doc:`Previous Chapter </wiki-migration/university/courses/electronics/text/chapter-7>`

**Go to** :doc:`Next Chapter </wiki-migration/university/courses/electronics/text/chapter-8>`

**Return to** :doc:`Table of Contents </wiki-migration/university/courses/electronics/text/electronics-toc>`

APPENDIX A - Semiconductor Diodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In a semiconductor P-N junction mobile electrons (conduction-band electrons) from the N region diffuse into the P region and "recombine" with the holes there, causing the region around the junction to be depleted of charge carriers and, effectively, an insulator. This process is limited because the positive donor ions in the N region (left behind by the diffusing electrons) and the negative acceptor ions in the P region (produced when the holes are filled) cause an electric field across the depletion zone which prevents further electron diffusion. At room temperature the potential caused by this mechanism is approximately 700 mV for simple silicon junctions, 300 mV for germanium diodes, 200 mV for silicon Schottky diodes, and between 1.8 V (IR & red) and 4 V (blue & UV) for LEDs of different colours.

If a negative external bias voltage (often called *reverse bias*) is applied to the P region it reinforces the depletion zone, which remains an insulator, but a positive bias voltage (*forward bias*) allows recombination to continue and a current flows in the junction. The equation\ :sup:`[19]` relating this current (*I*) to the bias voltage (V) is

$\\displaystyle I = I_se^{-v/\\frac{kT}{q}} - 1 $ [15]

where *I*\ :sub:`s` is the "scale current" or "reverse bias saturation current", k is Boltzmann's constant (1.3806E-23 JK\ :sup:`-1`), T is the absolute temperature, and q is the electron charge (-1.602E-19 C).

:math:`kT/q` is not the only term in the equation which is temperature dependent - the scale current, *I*\ :sub:`s`, doubles for every 10°C temperature increase as well.

With negative (reverse) bias (i.e. -V is positive and the electron charge is negative, so the exponent is large and negative) the exponential term is very small and :math:`I approx -I_s` . However the reverse current of most diodes is actually much larger than the scale current due to manufacturing imperfections in the P-N junction, so the equation is not very accurate with real diodes and reverse bias - nevertheless the total reverse current normally behaves in much the same way as the scale current in that it is substantially constant with bias voltage and doubles for every 10°C temperature increase. (Of course, if the reverse bias approaches or exceeds the diode's breakdown voltage its behaviour becomes much more complex - we shall not discuss such behaviour in this article.)

Since the exponent is so much larger than 1 the equation for the forward current can be simplified to

$\\displaystyle I = I_s e^{-v/\\frac{kT}{q}} $ [16]

The forward current is therefore exponentially related to the forward voltage - quite small voltage changes produce large current changes. In practice this means that the voltage drop across a normal small diode or LED at operating currents between 50 µA and 20 mA will increase with current but will remain reasonably close to the potential in the depletion zone as mentioned above, i.e. 700 mV for simple silicon junctions, 300 mV for germanium diodes, 200 mV for silicon schottky diodes, and between 1.8 V (IR & red) and 4 V (blue & UV) for LEDs of different colours. At high currents, of course, the ohmic resistance of the semiconductor and its connections increases the voltage expected for a given current above that predicted by the equation.

APPENDIX B - Measuring Photodiodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The basic principle of measuring a photodiode's characteristics is to expose it to a known light intensity at a number of different wavelengths, measure the photocurrent at each wavelength and plot a response curve. This is easily done if you have access to an expensive spectrophotometer, but otherwise it is quite hard to obtain an accurate tuneable light source.

But some photocells are quite well characterized and it is possible to compare the response of an unknown photocell with the response of a well-characterized one to the same light sources. It is cheap and easy to obtain high intensity LEDs of a variety of colours from UV to IR and some manufacturers' data sheets have very good characterization of their LEDs' spectra. If we obtain a well-characterized (in terms of spectral variation of sensitivity, not necessarily of absolute sensitivity) photocell covering the range of wavelengths we are interested in, and choose six or seven 5mm LEDs with peak wavelengths reasonably evenly distributed across this range we can perform quite a good spectral and sensitivity analysis of the performance of an unknown photodiode by comparing its response to that of a photodiode of known characteristics under standard conditions.

If the calibration and tested photocells are both in 5mm packages too this is easily done: drill a 5mm hole in a small piece of ebony, black ABS, carbon fibre block or other dark material. Insert the LEDs in turn at one end and the photocells at the other and make your comparisons. If your photodiode under test is some other diameter try and find a calibration photodiode of the same diameter and drill an appropriate diameter hole 10 mm deep into a co-axial 10 mm deep 5mm LED hole.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/cphotodio_f28.jpg
   :align: center
   :width: 400px

.. container:: centeralign

   Fig 22 Test Jigs for using LEDs to make Photocell Measurements


In addition to measurement of spectral sensitivity it may be advisable to measure leakage current, threshold voltage and, possibly, switching speed. All can be done with a mid-range DVM, a fast pulse generator, an LED known to have fast switching time, and a 100 MHz oscilloscope. The procedures are left as an exercise for the student.

Foot Notes
~~~~~~~~~~

| [1]The International Commission on Illumination (CIE) recommends the division of infrared & ultraviolet radiation into the following six bands:
| **Infrared**
| • IR-A: 700 nm – 1400 nm (215 THz – 430 THz)
| • IR-B: 1400 nm – 3000 nm (100 THz – 215 THz)
| • IR-C: 3000 nm – 1 mm (300 GHz – 100 THz)
| **Ultraviolet**
| • UV-A: 315 nm – 400 nm (750 THz – 950 THz)
| (Subdivided into UV-A1 (315 nm – 340 nm) & UV-A2 (340 nm – 400 nm)
| • UV-B: 280 nm – 315 nm (950 THz – 1070 THz)
| • UV-C: 100 nm – 280 nm (1070 THz – 3000 THz)
| [2]The characteristics of photoresistors are discussed in some detail on the Selco Products website at
| http://www.selcoproducts.com/pdfs/CdS-Photocells%20Catalog.pdf

[3]There are a number of ROHS compliant CdS & Cd2SeS photocells but many older types are not compliant.

[4]The same arrangement was once used for digital isolators as well, but today these almost always use photodiodes or phototransistors.

| [5]The electrical conductance of a conductor is the ease with which an electric current passes through that conductor. The (commoner) inverse quantity is its resistance - the opposition to the passage of an electric current. The official SI unit of conductance is the Siemens (S) but the older name, “mho”, and symbol (Ʊ) are still quite widely used because the older symbol is less likely to be confused with the symbol for a second (s). The unit of resistance is the ohm (Ω). The relationships between voltage (V), current (I), resistance (R) and conductance (G) are:-
| :math:`R = V/I` :math:`G = I/V` :math:`G = 1/R`

| [6] Read the Friendly Data Sheet (RTFDS). The RAQ on this topic can be found at
| http:*www.analog.com/static/imported-files/rarely_asked_questions/RAQ_caveat.pdf
  and the longer discussions at
  http:*\ www.analog.com/static/imported-files/rarely_asked_questions/moreInfo_raq_datasheet.html
| http:*www.analog.com/static/imported-files/rarely_asked_questions/moreInfo_raq_opAmpNoise.html
  http:*\ www.analog.com/static/imported-files/rarely_asked_questions/moreInfo_raq_opampbiasCurrents.html
| http://www.analog.com/static/imported-files/rarely_asked_questions/moreInfo_raq_dcSpecs.html

[7]Sometimes there is a very high resistance in parallel with the current sources so that there is a slight change of leakage with applied voltage, but the effect is generally negligible.

[8]Mullard was a company manufacturing thermionic valves ("tubes") in England in the 1920s. It became part of Philips in 1927 but continued to use the Mullard brand name for its valves and (from the 1950s) semiconductors until the 1980s.

[9]Or, in some circumstances, maximum wanted – i.e. the maximum possible light may sometimes (quite often) be greater than we need to measure so diode conduction at high light levels is unimportant.

[10]August 2014

[11]Plastic that appears clear to the eye may not transmit wavelengths outside the visible spectrum (UV or IR). If this matters in your application read the data sheet (or, if necessary, perform a simple experiment or two) to discover if this is the case.

[12]I have done some on-line research on this and obtained conflicting "facts". There seems to be little doubt that some LEDs have quite wide spectral sensitivity as a photodiode, and that others are sensitive in quite a narrow band (not Gaussian - there's a fairly abrupt transition at lower frequencies [longer wavelength] and more gradual roll off as the wavelength decreases). I suspect that modern high intensity LEDs have a wider bandwidth but have only a few home measurements to support this hypothesis.

I intend to make more measurements and will modify this footnote when I have done so. Please email me [A] if you are getting tired of waiting, or, [B] if you have good spectral response measurements on one or more types of LED.

[13]The RAQ 45"Glass Diodes May See the Light – and Hum" mentions the photosensitivity of small glass silicon diodes such as the 1N914/1N4148. In bright sunlight these have photocurrent of the order of 10 nA, but when illuminated by a nearby (30 cm/1 foot) 60W incandescent bulb the photocurrent is about 30 nA and there is, very roughly, about 2 nA rms 100 Hz ripple on it, thus demonstrating their greater sensitivity in the near infra-red - and the approximate 100 Hz light modulation of a 60W incandescent bulb.

[14]The output spectrum of a simple LED is not a single narrow line like the spectral lines in a gas discharge but a rather wider (but still relatively narrow – bandwidth a few percent of the peak) band of wavelengths with a Gaussian distribution around the nominal peak wavelength.

[15]A simple integral series resistor in an LED does not affect its use as a photodiode - but most other built-in circuitry does. This includes current limiters with active devices, diode bridges, integral dimmers and flashers.

[16]A silicon photodiode with a threshold of 700 mV used in this way may be able to drive an exceptionally low threshold MOSFET or a Schmitt input gate using a very low supply voltage.

| [17]A discussion of comparator characteristics is in the article accompanying RAQ 11 "Comparators & Op Amps – May They Never Meet (or Good Advice from Mr. Punch)"
| http://www.analog.com/en/all-operational-amplifiers-op-amps/operational-amplifiers-op-amps/product/raq_jbryant_comparators_opamps_may_issue11/resources/faq.html?display=popup .
| The article is at
| http://www.analog.com/static/imported-files/rarely_asked_questions/op-AmpsAsComparatorsv1.ppt .
| It is possible to use an operational amplifier as a comparator but there are problems, which are also discussed in this article. Despite being written to discuss a particular application problem, it is a useful short background note on the properties and uses of comparators.

| [18]Read RAQ 22 on ADC inputs.
| http://www.analog.com/static/imported-files/rarely_asked_questions/RAQ_highfrequency.pdf

[19]This equation is often written with respect to the bias being on the N region, in which case the polarity of V is reversed and the equation becomes :math:`\displaystyle I = I_s e^{v/\frac{kT}{q}}-1`
