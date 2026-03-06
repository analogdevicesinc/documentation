Current Steering Digital-to-Analog Converters
=============================================

.. container:: centeralign

   Douglas A. Mercer


1 DIGITAL-TO-ANALOG CONVERTER BASICS
------------------------------------

Real-world analog signals such as temperature, pressure, sound, or images are routinely converted to a digital representation that can be easily processed in modern digital systems. In many systems, this digital information must be converted back to an analog form to perform some real-world function. The circuits that perform this step are digital-to-analog converters (DACs),and their outputs are used to drive a variety of devices. Loudspeakers, video displays, motors, mechanical servos, radio frequency (RF) transmitters, and temperature controls are just a few diverse examples. DACs are often incorporated into digital systems in which real-world signals are digitized by analog-to-digital converters (ADCs), processed, and then converted back to analog form by DACs. In these systems, the performance required of the DACs will be influenced by the capabilities and requirements of the other components in the system.

A DAC produces a quantized (discrete step) analog output in response to a binary digital input code. The transfer function for an example 3 bit DAC is shown in Figure 1. The digital input may be TTL, ECL, CMOS, or LVDS, while the analog output may be either a voltage or a current. To generate the output, a reference quantity (either a voltage or a current) is divided into binary and/or linear fractions. Then the digital input drives switches that combine an appropriate number of these fractions to produce the output. The number and size of the fractions reflect the number of possible digital input codes, which is a function of converter resolution or the number of bits (N) in the input code. For N bits, there are 2\ :sup:`N` possible codes. The analog output of the DAC output is the digital fraction represented as the ratio of the digital input code divided by 2\ :sup:`N` times the analog reference value.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/figure1.png
   :align: center
   :width: 620px

.. container:: centeralign

   Figure 1, 3 Bit DAC transfer function.


.. image:: https://wiki.analog.com/_media/university/courses/tutorials/equation1.png
   :align: center
   :width: 150px

| where
| Ao is the analog output
| Di is the digital input code
| N is the number of digital input bits (resolution)
| Ref is the reference value (full-scale)

Analog signals are continuous time-domain signals with infinite resolution and possibly infinite bandwidth. However, the DAC's output is a signal constructed from discrete values (quantization) generated at uniform, but finite, time intervals (sampling). In other words, the DAC output attempts to represent an analog signal with one that features finite resolution and bandwidth. Quantization and sampling impose fundamental, yet predictable, limits on DAC performance. Quantization determines the maximum dynamic range of the converter and results in quantization error or noise in the output. Sampling determines the maximum bandwidth of the DAC output signal according to Nyquist criteria. The Nyquist theory states that the signal frequency (that is, the DAC output) must be less than or equal to one-half the sampling frequency to prevent sampling images from occurring in the frequency band of the DAC output. In an ideal DAC, the analog outputs are exactly one least significant bit (LSB) apart, where one LSB is the full-scale analog output amplitude divided by 2\ :sup:`N`, and N is the DAC resolution expressed in number of bits. In addition, DAC operation is also affected by nonideal effects beyond those dictated by quantization and sampling. These errors are characterized by a number of AC and DC performance specifications that determine the converter's static and dynamic performance.

A number of factors affect static or DC performance. Gain error is the deviation of the slope of the converter's transfer function from that of the ideal transfer function (see Figure 1). Offset error is the deviation of the DAC output from that of the ideal transfer function when gain error is zero. Offset error is thus constant for all input codes. Differential nonlinearity (DNL) is the deviation of the actual step size at each input code from the ideal 1-LSB step. DNL errors can result in additive noise and spurs beyond quantization effects. Integral nonlinearity (INL) is the deviation of the actual output voltage from the ideal output voltage on a straight line drawn between the end points of the transfer function. INL is calculated after offset and gain errors are removed. INL error can also result in additive harmonics and spurs in the output. A DAC is monotonic if its output increases or remains the same for an increment in the digital input code. Conversely, a DAC is nonmonotonic if the output decreases for an increment in the digital code.

There are a number of time-domain specifications often provided for DACs. Settling time is defined as the time for the analog output to settle to a value within its specified error limits in response to a step change in the digital input. Glitch is the amount of charge injected into the converter output from the inputs when they change state. Output noise from digital feed-through can be caused by high-frequency logic signals leaking through to the converter's output.

Frequency-domain or AC performance can be characterized by a number of parameters, such as spurious-free dynamic range (SFDR), total harmonic distortion (THD), and signal-to-noise ratio (SNR). Another parameter, THD + N, is the ratio of the rms sum of the harmonics plus noise to the amplitude of the fundamental.

1.1 COMMON D/A ARCHITECTURES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Conceptually, the simplest DACs use a binary-weighted architecture, where N binary-weighted elements (current sources, resistors, or capacitors) are combined to provide an analog output (N = DAC resolution). Digital decoding circuits are minimized, but the difference or scale factor between the most significant bit (MSB) and the LSB-weighted elements increase with increasing resolution, making accurate matching difficult. High-resolution D/As using this architecture are difficult to manufacture and are sensitive to mismatch errors.

1.2 VOLTAGE DIVIDER
~~~~~~~~~~~~~~~~~~~

The voltage divider architecture, shown in Figure 2, consists of 2\ :sup:`N` equal value resistors, simplifying matching compared with the binary-weighted approach. All the resistors are of equal value, so the input must be decoded. The output is determined by decoding 1 of 2\ :sup:`N` switches to tap into a particular location on the resistor string. This architecture has the advantage of being completely monotonic, voltage output, and low glitch (as only two switches operate during each code transition). It is also linear if all the resistors are of equal value. A related current-output architecture uses 2\ :sup:`N` equal current sources connected in parallel between a supply voltage and an output node where the currents are summed. The major disadvantage of this architecture is the large number or resistors or current sources required for higher resolutions. This becomes prohibitive in terms of size (and matching) for resolutions above about 8 bits. Nevertheless, while not practical for higher resolutions, these architectures (known as “fully decoded”) are often used as building blocks for high-resolution “segmented” DACs.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/figure2.png
   :align: center
   :width: 620px

.. container:: centeralign

   Figure 2 The voltage divider architecture, equal value resistors.


1.3 SEGMENTED DACS
~~~~~~~~~~~~~~~~~~

Segmented architectures, where the full resolution of the converter is spread across two or more sub-DACs, can be used for both current-and voltage-output DACs. The voltage across the decoded resistor in a resistor string divider circuit can be further subdivided to build a voltage-segmented DAC. This subdivision can be achieved through a second voltage divider circuit or with even a different architecture, as shown in Figure 3. The output of the overall DAC remains monotonic as long as the individual segments are monotonic and the offsets of the two buffer amplifiers in Figure 3 are less than one LSB. Monotonicity is easy to achieve because the individual segments have lower resolution. Segmentation has the added benefit of reducing the number of resistors (or current sources)required to achieve a given resolution, allowing smaller die sizes. Thus, it is common for high-resolution DACs to be segmented. Overall linearity is still determined by the matching of individual elements.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/figure3.png
   :align: center
   :width: 620px

.. container:: centeralign

   Figure 3 Monotonicity is easily achieved because the individual segments have lower resolution.


1.4 R-2R LADDER DACS
~~~~~~~~~~~~~~~~~~~~

The R-2R, or ladder, architecture simplifies resistor-matching requirements since only two resistor values are required in a 2:1 ratio. The R-2R architecture can be used as a voltage-or current-mode DAC. Most R-2R current-mode architectures are based on the circuit shown in Figure 4a. An external reference is applied to the Vref pin. The R-2R ladder divides the input current into binary-weighted currents. These currents are steered to node 1 or node 2 depending on the digital input. The current-output node is often connected to an op amp configured as a current-to-voltage converter. For matching reasons, the op-amp feedback resistor is usually included on the DAC chip. The switches are always at ground potential, and their voltage rating does not affect the reference voltage rating. If the switches are designed to carry current in either direction, a variable or ac signal may be used as the reference, resulting in a multiplying DAC. The input impedance of Vref is constant and equal to R. The disadvantages of this architecture include the inversion introduced by the op amp requiring both positive and negative power supplies, and the complicated stabilization of the op amp, as the DAC output impedance, seen at node 1, varies with digital input. Current mode operation also results in higher glitch, since the switches connect directly to the output. Voltage-mode R-2R DACs switch resistors between Vref and ground. The reference voltage is applied to node 1. Each rung on the ladder provides a binary-scaled value with the output taken as the cumulative voltage at the end of the ladder as shown in Figure 4b. The output voltage has constant impedance, simplifying amplifier stabilization. A positive reference voltage will provide a positive output, so single supply operation is possible. Glitch generated by switch capacitance is minimized. The drawback is that the reference input impedance varies widely, so a low-impedance reference must be used. Also, the switches operate from ground to Vref , restricting the allowed range of the reference.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/figure4.png
   :align: center
   :width: 620px

.. container:: centeralign

   Figure 4 The R-R2 architecture: (a) current-mode and (b) voltage-mode.


For high-resolution DACs, it is common to combine a R-2R ladder architecture with a fully decoded DAC in a segmented architecture. For example, the 16 bit AD7546 was one of the first DACs to use a fully decoded 4 bit resistor string combined with a 12 bit R-2R. The 65,536 output levels were divided down into 16 groups of 4096 steps. The 4 bit section is monotonic by design, so the 12 bit R-2R D/A determines the overall monotonicity. Matching and trimming is much easier than for a full 16 bit DAC. Segmentation reduces the overall number of resistors and simplifies trimming for higher resolution DACs.

1.5 DELTA-SIGMA ARCHITECTURE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A delta-sigma architecture (also called oversampling) can be used for DACs where linearity is preferred over bandwidth (for example, in audio DACs). The architecture consists of a digital interpolation filter, sigma-delta modulator and a 1 bit DAC, shown in Figure 5. The interpolation filter accepts an input data stream at a low rate and inserts zeros to increase the overall number of words in a particular time period, thus increasing the sampling rate of the D/A. The filter interpolates to assign values to the inserted words so that the noise in the output spectrum is concentrated at high frequency. This has the effect of pushing noise out of band, thus reducing the in-band noise and increasing the resolution. The modulator acts as a low-pass filter to the signal, converting it to a high-speed bit stream that is fed into a 1 bit DAC. Depending on the average number of ones or zeros in the bit stream, the DAC output will lie between the positive and negative reference voltages. Very high linearity can be achieved from the 1 bit DAC, which is theoretically perfectly linear. A major part of the converter uses digital circuits, so the chip area and power consumption can be kept small.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/figure5.png
   :align: center
   :width: 620px

.. container:: centeralign

   FIGURE 5 Delta-sigma architecture, output bandwidth . sample rate.


1.6 MANUFACTURING PROCESSES
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Architecture is not the sole contributor to DAC performance. DACs are made up from a combination of switches, resistors, amplifiers, and logic. Building a monolithic DAC in a bipolar process can provide good device matching, which yields good DC performance. However, device scaling is difficult, so a R-2R architecture is required for higher resolution. Also, this approach typically consumes higher power and it cannot be integrated easily with digital signal processing. CMOS processes are ideal for making high-density low-power logic and switches, but are less suitable for amplifiers. CMOS processes are often preferred for DACs requiring low power and small packages. For a DAC implemented in a CMOS process, scaling issues are simplified, so there is no need for an R-2R network and its drawbacks. Moreover, CMOS allows integration of digital signal processing and still offers good device matching for 12 bit linearity. But calibration is often required for higher resolution.

2 CURRENT MODE DACS IN CMOS
---------------------------

Submicron CMOS technologies have become the process of choice for high sample rate switched current digital to analog converter design [1–9]. Switching speeds of submicron gate length MOS transistors have allowed sample rates of many hundreds of MHz and at the extreme beyond a giga-sample-per-second. Unlike switched capacitor circuits used in many ADCs, which require mixed-signal process variants with high-quality poly-poly or metal-metal capacitors, switched current DACs can make use of the standard CMOS processes. The designs have marched down the process generations from 0.8 to 0.18 µm and beyond. There are certain common features of these designs that have become givens. Because of this, it is important to note that many of the best circuit techniques are protected intellectual property and special care should be taken when developing a commercial product. The data converter area is a mine field of patents.

Almost universally, DACs with resolutions from 8 to 16 bits are split into two or more segments. The MSB segment is nearly always made from unit-weighted elements and is thermometer-coded. The number of bits in the MSB segment can vary from as few as 4 bits to as many as 8 bits, with 5 and 6 bits being the slightly more common choice. The rest of the bits may be binary coded but are often further segmented into a thermometer-coded intermediate significant bit (ISB) section and a LSB binary-coded section. A notable exception to the use of thermometer coding is proposed in Ref.[10]. Here competitive performance is achieved using unit elements but combined and switched in binary fashion. It also seems that P-channel metal oxide semiconductor (PMOS) currents and switches are used more often than N-channel metal oxide semiconductor (NMOS) currents, especially when the next circuit block in the signal chain does not reside on the same die as the DAC. Using PMOS devices on a standard twin-well process on P-type wafers provides the opportunity to isolate the back gates of the devices and bias them at some potential other than a power supply or ground. Within a system with only positive power supplies, PMOS provides the convenience of having the output load referenced to ground as well. Newer triple well processes have become available in deep submicron, which provide the ability to isolate the NMOS devices but poorer 1/f noise performance, as well as needing positive supply referred output loads, has limited the appeal of going with NMOS currents. Depicted in Figure 6 is the basic structure of a typical CMOS DAC [1,8]. This example provides 14 bits of overall resolution. The five MSBs are composed of 31 unit-weighted elements and are thermometer-coded. Each unit element consists of a cascoded PMOS current source and a PMOS differential current switch pair. The remaining nine bits of the DAC are further segmented into four thermometer-decoded intermediate bits with the five LSBs being binary coded. Because just five of the MSBs are thermometer-coded, leaving 9 bits remaining, the inclusion of the thermometer coding for the 4 intermediate bits helps insure these 9 bits have sufficient INL and DNL accuracy for the overall resolution of the DAC.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/figure6.png
   :align: center
   :width: 620px

.. container:: centeralign

   FIGURE 6 Basic structure of typical CMOS current mode DAC.


2.1 POWER DISSIPATION
~~~~~~~~~~~~~~~~~~~~~

Power or supply current in a CMOS switch current DAC can be divided into three categories. The first comes from the digital logic and clock section and often directly scales with the sample frequency and the data pattern. CMOS has the advantage that the design will benefit from advances in process and supply voltage scaling. By way of illustration, the digital logic portion of DAC in Ref. [1] consumes 60 µA/MSPS at 5 V, up to a reported 125 MSPS maximum. A slightly more optimized logic block AQ2 of a low-power design in Ref. [8] consumes 56 µA/MSPS at 3.3 V, up to a 200 MSPS maximum. At the same time, the CMOS logic can be operated from 1.8 V and the current drops to less than half at 22 µA/MSPS while the maximum frequency drops by one-half to 100 MSPS. This process and supply voltage scaling results in a 86% reduction in the digital power consumed. The DAC in Ref.[10] takes this one step further by eliminating the binary to thermometer decoding logic in favor of using the binary code directly. This lower power binary coding approach can be used when 10 bit performance levels are sufficient for the target application.

The second and third supply current categories are analog in nature. The full-scale output current is the major single contributor to the current in the analog supply. A popular output current for many designs is 20 mA because it provides 1 V signal swings in 50 ohm systems. An obvious place to trade-off power for signal amplitude is to lower the full-scale current. The third part of the analog supply current is overhead and comes from the bandgap reference and various bias circuits. Inclusion of these bias circuits can have a direct effect on the spurious performance of the DAC (SFDR). For example, with an analog supply overhead current of 5 mA in addition to the 20 mA full-scale output, the DAC in Ref.[1] does not include a cascode in the PMOS current sources and achieves 61 dBc at Fout = 10 MHz. Whereas a similar DAC in Ref. [31] includes a cascode and has SFDR = 73 dBc, an improvement of 12 dB over the DAC in Ref. [1]. The addition of the cascode bias circuit increases the analog supply overhead current by 7 mA to a total of 12 mA. The challenge in power-efficient designs is to implement these performance-enhancing parts of the circuit while using a minimum of current. In the example from Ref. [8], two levels of cascode are included in a total analog supply current of 2.5 mA in addition to the reduced 2 mA full-scale output while maintaining an SFDR = 78 dBc at 10 MHz. In some cases, this overhead current can be made to at least partially scale with the full-scale output. Designs such as these often make use of mixed voltage process options to allow the analog sections to be powered from higher supply voltages than the digital decoding logic and provide larger voltage swings on the output.

2.2 STATIC ERRORS AND MATCHING
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Device matching in CMOS processes has been studied and is well documented starting with the often cited work by Pelgrom in Ref. [11]. By taking advantage of statistical averaging, layout techniques and random switching order, accuracy of up to 14 bits has been reported in Ref. [6]. The PMOS devices, which made up the main current sources in previous designs in 0.6 µmCMOS such as Ref. [1], which operate from a 5V power supply, are sized to provide sufficient yield to 12 bit linearity without calibration. An important aspect of design for good current source matching is the level of V\ :sub:`gs` - V\ :sub:`T` at which the devices operate. The larger this gate overdrive the less effect the random variations in V\ :sub:`T` have on the current sources. With the available headroom a 5 V supply affords, it is possible to size the transistors with a generous V\ :sub:`gs` - V\ :sub:`T` of around 600 mV in the 0.6 µm process. As the supply voltage shrinks such as in a 0.35 µm 3.3 V design [32] the V\ :sub:`gs` -V\ :sub:`T`\ is reduced to approximately 450 mV. For the DAC in Ref. [8], which can operate from 1.8 V, the V\ :sub:`gs` - V\ :sub:`T`\ is further reduced to 250 mV. It is also important to point out that the value of V\ :sub:`T` has scaled by 260 mV in these examples going from the 0.6 µm process (V\ :sub:`T` = 935 mV) to the 0.18 µm process (V\ :sub:`T` = 675 mV).

Table 1 lists the untrimmed DNL and INL normalized to 14 bit level LSBs for various reported designs. It can be seen that the number of unit currents used for the MSB segment has a strong effect on the resulting linearity.

The use of statistical averaging across a large collection of smaller devices will result in improved matching performance. There are a number of approaches to how to arrange the current sources and the individual devices that compose them. Figure 7 shows one possible floor plan where each unit cell includes the output switch pair, current source, possibly with a cascode, along with the final re-timing latch and final decoding logic gate [2]. These unit cells are arranged in a two-dimensional array or matrix. The area required by the extra devices in each unit cell increases the distance between current source devices. This results in an accuracy disadvantage as we can see from Table 1. The two examples in Refs.[2,12] each use 256 unit elements for the 8 MSBs; however, there is nearly a factor of 10 difference in the reported linearity. Another issue with a matrix configuration such as this is that it forces distributing the final latch clock and the row, column data lines through cells, and may result in undesired coupling into the analog output and current-source bias nodes.

Another possible floor plan more or less used by the rest of the examples in Table 1 is shown in Figure 8. Here the circuit blocks are arranged by functional block. All the data latches and binary to thermometer decode logic are placed together in one block. The output switches are arranged in a single row with the analog currents entering on one side and the switch gate drive signals entering on the other. By placing all the current source devices close together, the best matching can be achieved. Clock and data routing can be kept away from the analog output and current-source bias nodes.

**TABLE 1 Segmentation Comparison**

========= ============ ================= ========== ==========
Reference Segmentation Process Node (µm) 14 Bit DNL 14 Bit INL
========= ============ ================= ========== ==========
[1]       5–4–3        0.6               +4.0 LSB   -3.6 LSB
[8]       5–4–5        0.18              -2.6 LSB   +3.0 LSB
[5]       6–8          0.18              -0.7 LSB   -1.2 LSB
[2]       8–2          0.35              -1.6 LSB   -3.6 LSB
[12]      8–6          0.5               +0.15 LSB  +0.3 LSB
========= ============ ================= ========== ==========

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/figure7.png
   :align: center
   :width: 620px

.. container:: centeralign

   Figure 7 Row–column floor plan.


The individual devices, which make up the unit current sources in the matrix, can be broken up and distributed around the matrix to cancel out process-induced gradients across the array. Figure 9a and 9b show two possible layout techniques to minimize matching errors in the current sources. The individual transistors, which make up each cell in the matrix, consists of two gate stripes sharing common source and drain diffusions, thus minimizing the overall area. Often included, but not shown here, are rows of dummy devices around the periphery. This insures that the local environment is uniform when the polygates are patterned. In the examples shown, the 64 elements of the 8×8 matrix are combined into eight current sources. In Figure 9a, the units are combined along diagonals of the matrix as proposed (by Reynolds) in Ref. [23]. This is a simple interconnect method and requires the fewest number of metal layers because each combination of elements has at least two members on an edge and all interior cells are adjacent to another member of their group.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/figure8.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 8 Floor plan arranged by functional block.


.. image:: https://wiki.analog.com/_media/university/courses/tutorials/figure9.png
   :align: center
   :width: 620px

.. container:: centeralign

   FIGURE 9 (a) Unit devices arranged along diagonals and (b) Unit devices arranged around common centroid.


In Figure 9b, the units are combined around a common centroid where the average distance from the center of the matrix is the same for all eight combinations. A number of minor variations on this basic concept have been proposed in Ref.[12]. This is a more complex interconnect method and requires a larger number of metal layers. Many of the combinations are land locked so to speak with no members on an edge of the matrix.

In order to insure optimal differential linearity the carry from an MSB to the sum of the remaining LSBs should be addressed. For low resolution LSB segments (4 to 5 bits) individual transistors in the matrix could be combined in a binary fashion to generate the desired current values. For higher resolution LSB segments, a popular way to accomplish this is by subdividing an extra MSB unit current source to provide the remaining lower bits of the DAC. This insures that the current from the total of all the LSBs closely matches the MSBs. A current-splitting array of transistors (sub-DAC) can be used in place of a single cascode device as used in an MSB cell. For example, a 9 bit sub-DAC splitter could be further segmented into a 4 bit thermometer-coded upper segment and with binary-weighted elements for the five LSBs. The current splitter gate rail could be driven by a control loop separate from that of the MSB cascodes as shown in Figure 10 [28], closing the loop on the drain of the current source. In this way, all the main MSB unit current source operating points now match even though the effective cascodes, MP1 for the MSBs and MP2 for the LSBs, have potentially different V\ :sub:`gs` operating points.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/figure10.png
   :align: center
   :width: 620px

.. container:: centeralign

   FIGURE 10 Further splitting an MSB unit to generate LSBs.


2.3 SELF-CALIBRATION
~~~~~~~~~~~~~~~~~~~~

To achieve even higher accuracy or to increase yields with less layout area, trimming or calibration techniques are often used as in the literature [4,8,13,20,22]. There are two basic approaches to implementing self-calibration, foreground, and background. A converter, which is foreground-calibrated, must be taken off line and not used while being calibrated because as each current source is measured, it is removed from the output. In background calibration, an additional current source is used to replace each current source as it is calibrated. This allows the DAC to be in use while being continuously calibrated. However, the operation of removing and replacing current sources from the output could cause extra disturbances. The calibration clock may operate synchronous or asynchronous to the main DAC clock.

There are also two basic approaches to storing the correction factors for the individual current sources. One technique, as proposed in Ref. [13], is shown in Figure 11. In this figure, a correction voltage is stored on the gate capacitance of a MOS transistor MN1. In calibration mode, MN1 is diode connected through S2 and the gate will settle to a value such that the sum of Im and the current in MN1 will equal Iref . In normal operation S1 switches the current to the output and switch S2 is opened holding the voltage on C\ :sub:`gs`, the gate of MN1. In the process of opening switch S2, a small error charge may be dumped onto C\ :sub:`gs` so care must be taken in how S2 is implemented. A dynamic technique such as this needs to be constantly refreshed and lends itself to background calibration. There is also a minimum clock rate requirement and the calibration will be lost if the clock is turned off during power saving modes.

There are certain systematic sources of error in this technique. The operating conditions of trim device MN1 and the devices in the main current source Im potentially vary between the calibration and normal operation modes. The V\ :sub:`ds` of the devices is set equal to the V\ :sub:`gs` of MN1 while in calibration (Figure 11a). However, while in normal operation (Figure 11b), the V\ :sub:`ds` is set by whatever circuitry is connected to the terminal OUT. This could be a cascode device or the output switches of the DAC. Because of the finite output impedance of the current source devices, the current that results in the operating mode will be different than that flowing in the calibration configuration. Each cell is slightly different and the amount of adjustment needed, i.e., the gate voltage of MN1, will be different. The change in current between calibration and operation modes will depend on the level of the adjustment. This will limit the accuracy of the calibrated result. In order to maximize the headroom in designing current sources, the devices are often biased such that the V\ :sub:`ds` is marginally larger than the V\ :sub:`dsat` of the device. In this configuration, the V\ :sub:`ds` of MN1 and Im must be equal to the V\ :sub:`gs` of MN1 when in calibration.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/figure11.png
   :align: center
   :width: 620px

.. container:: centeralign

   FIGURE 11 Dynamic storage correction.


Static storage of a digital correction value as used in Refs. [4,8] does not need to be refreshed and would lend itself to foreground calibration. In this approach, shown in Figure 12, the unit element to be calibrated, inside the dashed box, is measured against a master reference current and the difference adjusted as close to zero as possible through the successive approximation register (SAR) logic. A

CAL DAC injects a small correction current in parallel with the main current source at the drain of MP1. The switches, which redirect the current either to the output node or the calibration hardware, act as the cascode devices and thus fix the drain voltage of the main current source device, MP1, to be the same, within the matching of the V\ :sub:`gs` of the two cascode switches, in both cases [27]. This can result in a much more accurate calibration. The additional circuitry used for the calibration is not clocked during normal operation and does not consume power or inject noise into the main signal path. The calibration algorithm in its first cycle calibrates the master current from MP7 to be the same as MSB current segment number 1 with its calibration DAC set to mid-scale. This in effect trims out any systematic offsets from either the NMOS mirror (MN1–4) or the voltage comparator. The trim range of the CAL DAC used to adjust the master Iref (not shown in Figure 12) is twice that of the other CAL DACs to allow for these offsets. In the second cycle, MSB current number 1 is trimmed against the now adjusted master current. This readjustment must be done because, as just indicated, the master current CAL DAC step size is twice that of all other CAL DACs and may result in a systematic difference between the value of MSB number 1 and the other MSBs. In the following cycles, the remaining MSB currents are adjusted in sequence to equal the master current. The configuration of the 6 bit calibration DAC is shown in Figure 13. The weight of MSB current MP1 is equal to 512 14 bit LSBs. A current equal to 16 LSBs is generated by the combination of MP2 and the splitting devices. From the typical raw DNL values from Table 1, we see a typical DNL of around than 3 LSB. Providing a trim range of ±8LSB or ±1.5% is sufficient to cover the worst-case matching errors. MP2 operates in the linear region and serves as a degeneration resistance for the devices in the splitting array. These devices are weighted as shown totaling 63 units.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/figure12.png
   :align: center
   :width: 620px

.. container:: centeralign

   Figure 12 Static digital storage correction.


.. image:: https://wiki.analog.com/_media/university/courses/tutorials/figure13.png
   :align: center
   :width: 620px

.. container:: centeralign

   Figure 13 6 Bit resolution calibration DAC.


Each unit is equal to approximately one-fourth of the 14 bit main DAC LSB. To keep the area of the splitting array small and insure monotonicity at the 6 bit level, the top two bits are thermometer-coded and generated from 3 equal 16× fractions. Switches are configured to direct the currents to either the drain of MP1 increasing the output current of the cell or discarded to a return current node common to all calibration DACs. The voltage to which the discarded currents is returned is forced to be approximately equal to the drain of MP1 by a buffer amplifier, which is driven from the same cascode bias used in the cascode for MP1. This insures that the splitting action is unaffected by how the switches are set.

2.4 FINITE OUTPUT IMPEDANCE
~~~~~~~~~~~~~~~~~~~~~~~~~~~

An INL mechanism that results from the use of a switched multiple current source architecture is code-dependent output impedance (Figure 14a). As the number of current source elements is switched to the output, the resistance Rsw of that element's current source appears in parallel with the load resistor RL. As the number of elements turned on increases, the effective output impedance of the DAC in total decreases. The varying impedance in parallel with the load resistor results in a nonlinear output voltage across the load. For cases where Rsw is much larger than RL, the maximum single-ended INL error with respect to the full-scale voltage (IFS × RL) can be approximated using the following formula:

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/equation2.png
   :align: center
   :width: 200px

| where
| Iunit is the magnitude of the unit current source
| RL is the load impedance
| Nu is the number of unit current elements
| Rsw is the impedance of a unit current source
| |image1|

.. container:: centeralign

   Figure 14 Code-dependent output impedance.


What we actually need to know is Rsw to design the DAC unit element. This formula can be rearranged to give us the required Rsw for a given overall DAC resolution and 1/2 LSB INL error:

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/equation3.png
   :align: center
   :width: 200px

| where
| RL is the load impedance
| Nu is the number of unit current elements
| NR is the number of bits for the overall DAC
| While it is true that switch output resistance requirements are greatly reduced for fully differential output configurations, as pointed out in Ref.[14], it is important to design the output switches and their gate voltages so as to keep the output switches in saturation. This maximizes the attenuation of the output swing seen at the common source nodes of the differential switches. The small signal attenuation of the switches is given by the ratio of the device gm to gds. Typical values of this ratio can be in the range of 20 to 50.

The parasitic capacitances shown in Figure 14b reduce the current source impedance as the output frequency increases [21]. As indicated in the figure, one or more cascode stages can be included to improve low-frequency output impedance, and extend the frequency range over which the current source output impedance is acceptable. The simulated output impedance versus frequency for an example unit cell in a standard 0.18 µm CMOS process is shown in Figure 15. The triangle curve is for the total of the drain to gate and drain to bulk junction capacitance of switches MP1 and MP2, which always appear on the output nodes independent of whether the switch is off or on. The other three curves are the impedance seen when the switch is on (excluding the fixed drain capacitance). The circle is for the case where the main current source devices connect directly to the switch pair. The square curve includes one cascode and the x curve includes two levels of cascode. For the two cascoded cases, the drain capacitance dominates the impedance until the DC resistance is reached. We can use the same INL formula to gauge at what frequency the distortion will cross the required specification level. Again for differential output configurations, the even order distortion terms are greatly attenuated. At some point, the unavoidable nonlinearity of the drain to bulk junction capacitance will dominate.

Early work on a 16 bit DAC in BiCMOS in Ref.[18] pointed out that high-frequency operation requires not only that the switch common source node capacitance be small but also linear. A switch

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/figure15.gif
   :align: center
   :width: 620px

.. container:: centeralign

   Figure 15 Unit cell output impedance versus frequency.


unit element will see an attenuated output signal on the switch common source node, and any nonlinear back gate capacitance, depicted as C1 in Figure 14b, on this node will produce odd order output distortion. Tying the switch and cascode transistors' back gates to the supply reduces nonlinear capacitances, but for a large array, the total nonlinear capacitance can be significant. The input of a unity-gain level shifting amplifier can be connected to the switch common source node and used to drive the back gate of the switches and cascode [4]. The nonlinear back gate capacitances now see the signal on both plates, thereby bootstrapping the well capacitances and leaving small linear parasitic capacitances. The amplifier's dc level shift should set high to minimize the switch's nonlinear capacitance.

2.5 SIMILARITIES BETWEEN DAC AND FLASH ADC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The thermometer-coded segments of a switched current DAC are very much analogous to the full parallel flash ADC. The complexity and hardware of both double for each bit of resolution. In the ADC, the distribution of the analog input signal to the comparators with matched delays is much the same as the collection and combining of the individual unit current outputs of the DAC. Also, as in the Flash ADC where the delays in the clock distribution to the individual comparators must be tightly matched, the clock distribution network driving the final stage of re-timing latches in the DAC is equally important.

One possible approach to this is propagation delay matching [4] illustrated in Figure 16a. Here if we assume that each cell has the same delay. and the delay along the clock distribution line from bottom cell 1 to top cell n is d1 and the delay along the output signal line is d2 then the sample timing is preserved if d1 = d2.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/figure16.png
   :align: center
   :width: 620px

.. container:: centeralign

   Figure 16 Signal distribution by (a) propagation matching and (b) constant wavefront matching.


Binary tree distribution structures are often used to match these delays as well as done in Ref. [5] for a DAC with a 1.4 Gsample/s clock rate. This results in a constant wavefront as illustrated in Figure 16b. The clock distribution tree is arranged to have equal lengths from the driver to each cell. Likewise the output collection tree is arranged with equal length from each cell to the output pad(s). The clock tree delay does not need to match the output tree delay. The physical placement of the unit cells in the layout is an important consideration and geometric shuffling of the placement is often used to breakup any linear gradients in the cell delay . (Figure 16)that might be present [33].

2.6 DIGITAL DATA PATTERN-DEPENDENT NOISE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The observation was made in Ref.[15] that noise generated by the data passing through the digital logic portions, specifically the thermometer decode section, of a DAC can cause spurious tones and distortion in the analog output. The U.S. patent [24] teaches us that it is possible to concentrate this noise at the clock frequency Fs or Fs/2. This is accomplished by including a shadow or mirror data path with a one-to-one correspondence to the main data path. This shadow data path is driven by a data pattern is such a way that for each node in the main data path that does not change value at a given clock transition the corresponding node in the shadow path does. Likewise, when a node in the main path does change the corresponding shadow node does not change. This makes the sum total of all nodes changing at each clock transition constant and independent of the data pattern.

An example of this technique in an oversampled switched current audio DAC is proposed in Ref.[19]. In this approach, a dummy data shift register creates constant local digital edge activity on the supply, ground, and substrate. NMOS switch devices, driven by full rail swings, are used to switch the cascoded PMOS current sources. The use of the dummy data to drive dummy switch devices balances the switching activity injected into the output stage thus minimizing the demodulation of out-of-band noise into the base band.

A similar notion, referred to as modified mismatch shaping (MMS), is proposed in Ref.[16]. The idea is to set the number of elements or cells switching per clock period to a constant. This turns the errors caused by nonideal element dynamics into a dc offset and energy at Fs/2. An oversampling converter is assumed, where the maximum output bandwidth is reduced. The choice of what fraction of the total number elements to set the constant to is problematic and the optimum is a function of the nature of the signals being converted, however. In any case, the constant can never be set to more than one-half the number of elements. This limits either the maximum amplitude or the maximum output frequency to only one-half of what it would have been otherwise. Therefore, we conclude that, for a Nyquist rate converter, to make use of this constant element switching concept, we will need twice as many elements.

2.7 DATA-DEPENDENT CLOCK LOADING
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As pointed out in the previous section, due to the mixed-signal nature of a DAC, digital data activity on the die will cause interference in the analog and clock sections of the device. This becomes an important performance issue as the output signal power is reduced or the frequency of the reconstructed output increases. A special case of data pattern-dependent interference comes from the varying load seen by the final clock buffer, which drives the final rank of re-timing latches in the DAC [7]. The now popular six-transistor latch topology first used in Ref. [1] is shown in Figure 17 [24]. True and complements of the data are provided to inputs at D and DB and are allowed to change only when Clock is low, i.e., NMOS transistors MN1,2 are off. When a rising edge transition occurs on the Clock input, the value of D is passed to Q and DB is passed to QB. When the Clock signal transitions back to a low state, falling edge, and MN1,2 turn off, the state of Q and QB is held by the positive feedback around the weak inverters.

An example of this effect is shown in Figure 18. The effect is made more pronounced in this simulation for clarity by using a relatively weak clock buffer. The simulated time when the rising edge of the clock signal crosses mid supply, 1.8 V in this case, is plotted for the case of a single latch when the input data is not changing and when the input data is changing. This simulation shows a 4 pSec difference between the x curve when the data does not change and the square curve when the data does change. Given the finite strength of the final clock buffer, the effect is magnified when a large number of latches are driven by the same common clock buffer and is proportional to the number of latches, which change their state. In the case of thermometer-coded data, the number of unit MSB cells switching is proportional to the absolute value of the rate of change of the reconstructed output waveform. The time-shift of the output samples is thus proportional to this rate-of-change and so results in odd-order distortions, mainly third order. A strong clock buffer can be used, which minimizes the time differences thus the effect of the data-dependent clock loading is most prominent at high-output frequencies.

We can get a workable solution by taking the shadow or mirror data paths concept of Ref. [25] and combining it with what we concluded from Ref. [16] and realize that by doubling the number of latches by simply adding the seconds a mirror path for each original latch and driving the mirror latch in such a way as to cause it to change state only when the main data latch does not. One way this mirror data can be generated is shown in Figure 19 [29]. By combining the main data signal with a clock signal at F\ :sub:`clock`/2, or one-half the main clock rate, with an exclusive OR gate the mirror data signal is created such that it changes only when the main data does not. By doubling the number of latches, we have doubled the load on the clock driver, but it is now independent of the incoming data pattern.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/figure17.png
   :align: center
   :width: 620px

.. container:: centeralign

   Figure 17 Final latch circuit.


.. image:: https://wiki.analog.com/_media/university/courses/tutorials/figure18.gif
   :align: center
   :width: 520px

.. container:: centeralign

   Figure 18 Normalized clock buffer crossing point.


Additional power is consumed to generate and distribute the F\ :sub:`clock`/2 signal. Some of this F\ :sub:`clock`/2 energy may leak onto the main F\ :sub:`clock` signal and cause spurious outputs centered around F\ :sub:`clock`/2.

A more area-and power-efficient solution, which addresses this problem is shown in Figure 20 [8,30]. The top portion, which includes transistors MN1,2 and INV1,2, is the standard latch from Figure 17. The bottom portion is the compensating load, which provides, through NMOS transistors MN3,4, a load that varies in a way opposite to the load provided by MN1,2.

The gate current that the buffer driving CLK needs to supply to transistor MN1 is a function of the relative voltage levels present at input D and output Q. If the voltage on D is the same as on Q a slightly smaller amount of charge is needed to turn on MN1 than if D is not equal to Q. MN3 shares its drain connection with MN1 at input D, but the source is connected to the output of INV6. The voltage on the output of INV6 will be opposite INV1 because the input of INV6 is connected to the output of INV3, an inverted version of output QB. INV6 is a gated inverter and the output will be in a high impedance state when CLK is high and will be driven high or low when CLK is low.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/figure19.png
   :align: center
   :width: 620px

.. container:: centeralign

   Figure 19 Constant clock load data path.


.. image:: https://wiki.analog.com/_media/university/courses/tutorials/figure20.png
   :align: center
   :width: 620px

.. container:: centeralign

   Figure 20 Constant clock load latch.


It can be seen that, for all possible combinations of the inputs and state of the latch, of the four switches MN1,2,3,4, the first will have high to low across source to drain (S-D), the second will have low to high across S-D, the third will have high to high across S-D, and the fourth will have low to low across S-D. Therefore, as far as the charge that is needed to be supplied by the clock driver to turn on these four switches, it should be invariant with the data pattern. There is no energy at F\ :sub:`clock`/2 and actually the supply current in INV5,6 has energy at 2F\ :sub:`clock`.

Shortly after the CLK line goes high, the latch formed by cross-connected INV1 and INV2 will have regenerated, making the signals levels across S-D of MN1,2 the same and INV5,6 will now be in tri-state, equalizing the voltages across S-D of MN3,4. When CLK returns low MN1–4 turn off and INV5,6 come out of tri-state and the cycle is ready to repeat. It is necessary to balance the relative strengths of the weak inverters INV1,2, used in the latch, with the gated inverters INV5,6 to insure data-independent loading on the clock driver. Gated inverters INV5,6 are sized such that their delay entering into tri-state is about the same as the regeneration time of the INV1,2 latch.

2.8 SWITCH GATE DRIVE
~~~~~~~~~~~~~~~~~~~~~

The differential output switch pair (MP1,MP2; Figure 21) could be driven directly with full supply rail swing outputs of the CMOS logic, the Q, QB nodes in Figure 17 or Figure 20. This would be the lowest power solution. However, it is well known that for the best SFDR performance, the crossing point for the gate drive signals of the output current switch pair needs to be optimized [1,2]. The circuit that drives the differential switch should ensure that both switches are never completely off at the same time so that the current from the current source is always flowing at a constant value. This minimizes the excursion of the voltage on the switch common source node, Cs, during a transition. Any current lost to parasitic capacitor C1 causes output distortions. The disturbance on Cs should be symmetric around the nominal DC value as indicated in Figure 21. To the extent that the disturbance cannot be completely eliminated, as pointed out earlier, it is important that C1 be minimized [21]. It is also important to point out that it is not necessary to bring the gates of the switch devices any higher than the voltage on the common source node Cs, when turning off the device (V\ :sub:`gs` = 0). This reduces any feed through of the gate drive signals to the outputs or the common source node.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/figure21.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 21 Differential current switch.


Another source of dynamic error relates back to the fact that a small attenuated amount of the output signal leaks through the gds of the differential switch onto node Cs. The amplitude of the signal seen at node Cs is typically about 1/20 that seen at outputs IA and IB or 50 mV for a 1 V swing at the output. Each switch element turns on at a different point in the transfer function and as a result will have a different wave shape on node Cs. In Figure 22a, the complementary outputs IA and IB are shown. Referring to Figure 21, node Cs will have the attenuated version of IA when MP1 is on and the attenuated version of IB when MP2 is on. In Figure 22b, we see what the signal on

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/figure22.gif
   :align: center
   :width: 520px

.. container:: centeralign

   Figure 22 Common source node waveforms.


Cs will look like when a switch element is near the lower end of the transfer function. Similarly, for Figure 22c, we see the signal on Cs when a switch element is near the top of the transfer function.

In Figure 20, note that the point at which MP1 and MP2 switch is determined by the crossing point of gate drive signals G1, G2 with respect to the value of node Cs. If the relative value of Cs is modulated by the output swing and where in the transfer function the switch element is, the actual time point when the switches change will also be a function of the output swing and their position in the transfer function. This will result in a signal-dependent timing error seen in the output. As indicated in Figure 22b, MP1 switches from on to off when Cs is at its low point and MP1 switches from off to on when Cs is near the high point. For the case shown in Figure 22c, just the opposite happens. The amount of timing error depends on the magnitude of the signal on Cs and the rise/fall time of the gate drive signals.

Simulation results of an example case is shown in Figure 23, where the normalized zero crossing point of the differential output voltage at IA, IB is shown for three cases. The horizontal axis is 5 pSec per division and the vertical axis spans 1 mV. The three curves are for cases where the difference between IA and IB when the switch flips is -333 mV, 0 V, and +333 mV. For these three cases, the node Cs has shifted its nominal value by a total of 32 mV or approximately 1/20 of the output. We see a shift in time of 4 pSec, which results from a differential slew rate on the gate drive signals G1,G2 of 125 pSec/V in this simulation. This could be a significant source of error when generating high-frequency outputs.

The circuit, which produces the appropriate signals at the gates, is shown in Figure 24. The full supply rail swing outputs from the final latch, Q,QB (Figure 20), are used to turn on and off NMOS devices MN1–4, which connect the two outputs G1 and G2 to either the node, which sets the output common mode level or the VSB bias node. The output common mode level is most often ground but in this example circuit can be adjusted, external to the die, to accommodate interfacing to other circuits, which may require that the common mode voltage be as much as 1.2 V or more such as a mixer or modulator. The amount of output shift can be traded off with increasing or decreasing the analog supply voltage. The VSB node is driven to a voltage approximately the V\ :sub:`gs` of the output switches above the output common mode level.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/figure23.gif
   :align: center
   :width: 460px

.. container:: centeralign

   Figure 23 Switch timing delay versus output swing.


.. image:: https://wiki.analog.com/_media/university/courses/tutorials/figure24.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 24 Output switch gate driver.


For each transition of the data, a large narrow spike of current is drawn from the VSB node by device MN1 or MN4. Normally the switch driver bias block would need to be designed to supply this current and have sufficiently low impedance to settle back to its nominal value within one clock cycle. This often requires considerable static DC current, increasing the power consumed in the circuit as in Refs. [1,7]. PMOS devices MP1-4 are added to supply a similar narrow spike of current from the VDD power supply when a data transition occurs. This allows the switch driver bias block to be designed with much smaller static current. The power consumed by the circuit is now much more a function of the clock frequency and the data pattern. To save power, two of the inverters, INV3,4, in Figure 20 can also serve as the two inverters which drive the gates of MP1,2 in Figure 24.

The switch driver bias generator is shown in Figure 25. PMOS device MP1 is scaled to mimic one of the output switches. The voltage on node VSB will be equal to the voltage on node OT_CM (output common mode level from Figure 24), plus the V\ :sub:`gs` of MP1. NMOS device MN1, driven from BIAS2, determines the overall current level in the block. A portion of MN1's current is diverted by MN2 and through the mirror gain of MP3 to MP2 (approximately 3 in this case) supplies the current to the source of MP1. This feedback provides some degree of regulation and lowers the dynamic impedance at node VSB.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/figure25.png
   :align: center
   :width: 410px

.. container:: centeralign

   Figure 25 Switch driver bias circuit.


2.9 RETURN-TO-ZERO SWITCHING
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Another way to re-time the data samples at the output of the DAC is to use a return-to-zero output stage as proposed in Ref. [6]. In this case, a set of additional switches has been added in the output path between the data-driven current switches and the external output load as shown in Figure 26, for one of the differential outputs. Switch MN1 is switched off for one-half of the clock period while the DAC current switches (IDAC) change and then back on after the currents have settled. Resistor R1 provides a load while MN1 is off. As well, there is switch MN2 to short the output to ground, through resistor R2, when the other switch is off thus the return-to-zero operation. This effectively reduces the timing skew between the various DAC switches. There is, however, a loss of one-half of the signal amplitude, 6 dB, due to the return-to-zero output.

Return-to-zero switching can reduce the distortion from digital data noise-induced timing errors, but for very high sample rates if the output does not completely settle in each half of the cycle then the history effect or intersample interference is not eliminated and can result in signal-dependent distortions. It is important to note that this scheme is not totally free of signal-dependent timing errors. The turn-on and turn-off points for MN1 and MN2 will depend on the signal levels seen at the node OUT. It is difficult to tell if the reported SFDR results for this method are really any better than those reported in Ref. [4] because both seem, for output frequencies above 25 MHz, to be limited to about -75 dBc, which seems to be the measurement limit of many spectrum analyzers.

2.10 QUAD SWITCHING/CONSTANT DATA ACTIVITY
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dynamic element matching or distortion spreading techniques are popular methods of improving spurious-free dynamic range by smearing the distortion into a noise-like component in the output of the DAC. Random spreading produces a more white noise-like result. Other approaches can shape

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/figure26.png
   :align: center
   :width: 410px

.. container:: centeralign

   Figure 26 Return-to-zero switching.


.. image:: https://wiki.analog.com/_media/university/courses/tutorials/figure27.png
   :align: center
   :width: 410px

.. container:: centeralign

   Figure 27 Quad switch.


the noise characteristic to place it out of the band of interest, if there is some amount of oversampling in the system. While DEM will increase the amount of data activity, it is not constant for each clock cycle. When constant switching techniques are used, the distortion or noise is concentrated as a tone at the sampling frequency.

Ordinary differential current switching results in some data-dependent distortions arising from the jump or glitch on the common source node of the switch pair. This ordinary switch does not toggle every clock transition, and as a result, the switching event is dependent on the data pattern, introducing distortion in the band of interest. Another approach to the data pattern-dependent dynamic errors pointed out in Ref. [12], is a quad differential current switch proposed in Ref. [17]for an oversampling DAC and again in Ref. [5] for a multibit Nyquist DAC. By using four switches instead of the normal two, we are in effect interleaving two return-to-zero switches. The configuration of the quad switch is shown in Figure 27. There are four switch devices MP1, MP2, MP3, and MP4, which share a single common source connection Cs, which nearly doubles the parasitic capacitance compared to the conventional two switch scheme. The unit element current Imsb is supplied to node Cs as in the ordinary differential switch. Only one of the four switches is on at any given time as indicated by the switching waveforms of Figure 28. The gate of each switching transistor is driven by a signal shown in Figure 28, three of the four

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/figure28.png
   :align: center
   :width: 410px

.. container:: centeralign

   Figure 28 Quad switch waveforms.


gates will be high and one low for a given clock cycle. Each clock cycle the gate that is low will transition high and another gate will transition low. At the bottom of the figure, the outputs IA and IB indicate where the current Imsb is being directed. The output at IA and IB is logically the same as with ordinary differential switching. There will be switching glitches as indicated even if the current does not change outputs. Switching in this manner eliminates the nonlinearity due to uneven pulse duration, as in RZ switching, because every pulse has the same width. There are at least two and only two signal transitions, one rising and one falling, per clock transition. Switching noise is now moved to the sample clock frequency by the constant toggling of both sides of the switch. It also important to note that the switching disturbance seen on the common source node Cs is constant and independent of the input data pattern. However, the voltage on node Cs will still be effected by the swing seen at IA and IB just as in the ordinary differential switch.

Quad switching like this incorporates some of the good points of both RZ switching and ordinary differential switching is suitable for high sample rates, and reduces transition-dependent noise. A drawback of quad switching is an increase in complexity, four gate signals need to be generated and the increased dynamic power consumption due to the fact that one pair of the four switches each cycle.

2.11 CONCLUSIONS
~~~~~~~~~~~~~~~~

A number of major contributors to errors and distortion in modern switched current DACs have been discussed. Static device matching can be addressed either though statistical averaging or calibration. One or more cascodes can be included, along with insuring that the output switches remain in saturation, to reduce the effect of output impedance variation. The importance of gate drive signals was explored. Much like the flash ADC, clock distribution is a key factor. Digital data pattern generated noise needs to be addressed and the effect on clock noise can be a major source of distortion. Return-to-zero switching can be employed to retime the output sampling time. The use of a quad switch and constant data activity switching techniques can shift spurious outputs to the sampling frequency.

**Return to** :adi:`Previous Chapter </media/en/training-seminars/design-handbooks/Basic-Linear-Design/Chapter6.pdf>`

**Go to** :doc:`Next Chapter </wiki-migration/university/courses/electronics/text/chapter-20>`

**Return to** :doc:`Table of Contents </wiki-migration/university/courses/electronics/text/electronics-toc>`

REFERENCES
~~~~~~~~~~

1. D. Mercer et al., 12-b 125 MSPS CMOS D/A designed for spectral performance, ISLPED 1996 Dig. of Tech. Pap., pp. 243–246, 1996.

2. C.H. Lin et al., A 10b 500-Msample/s CMOS DAC in 0.6 mm2 , IEEE J. Solid-State Circuits, 33(12), 1948–1958, 1998.

3. B. Tesch et al., A 14-b, 125 MSPS digital to analog converter and bandgap voltage reference in 0.5 µm CMOS, ISCAS 1999 Dig. of Tech. Pap., pp. II-452–II-455.

4. W. Schofield et al., A 16b 400MS/s DAC with < - 80 dBc IMD to 300 MHz and < - 160 dBm/Hz noise power spectral density, ISSCC Digest of Technical Papers, pp. 126–127, February 9, 2003.

5. B. Schafferer et al., A 14b 1.4 GS/s 3 V CMOS DAC for multi-carrier applications, ISSCC Dig. of Tech. Pap., February 2004.

6. A.R. Bugeja et al., A 14-b, 100-MS/s CMOS DAC designed for spectral performance IEEE J. Solid-State Circuits, 34(12), 1719–1732, 1999.

7. D. Mercer, A study of error sources in current steering digital-to-analog converters, CICC 2004 Conf. Proc., pp. 185–190.

8. D. Mercer, A low power current steering digital to analog converter in 0.18 µmCMOS, ISLPED 2005 Dig. of Tech. Pap., pp. 72–77.

9. D. Mercer, Low power approaches to high speed CMOS current steering DACs, CICC 2006 Conf. Proc., pp. 153–160.

10. J. Deveugele et al., A 10b 250 MS/s binary-weighted current-steering DAC, IEEE J. Solid-State Circuits, 41(2), 320–329, 2006.

11. M.J.M. Pelgrom et al., Matching properties of MOS transistors, IEEE J. Solid-State Circuits, 24(5), 1433–1443, 1989.

12. G.A.M Van der Plas et al., A 14-bit intrinsic accuracy Q2 random walk CMOS DAC, IEEE J. Solid-State Circuits, 34(12), 1708–1718, 1999.

13. D.W.J. Groeneveld et al., A self-calibration technique for monolithic high-resolution D/A converters, IEEE J. Solid-State Circuits, 24(6), 1517–1522, 1989.

14. S. Luschas et al., Output impedance requirements for DACs, Proc. of the 2003 ISCAS, Vol. 1, pp. I-861–I-864, May 25–28, 2003.

15. J.L. Gonzalez et al., Clock-jitter induced distortion in high speed CMOS switched-current segmented digital-to-analog converters, ISCAS 2001 Dig. of Tech. Pap., pp. I-512–I-515, May 2001.

16. T. Shui et al., Mismatch shaping for a current-mode multibit delta-sigma DAC, IEEE J. Solid-State Circuits, 34(3), 331–333, 1999.

17. S. Park et al., A digital-to-analog converter based on differential-quad switching IEEE J. Solid-State Circuits, 37(10), 1335–1338, 2002.

18. D. Mercer, A 16b D/A converter with increased spurious free dynamic range, IEEE J. Solid-State Circuits, 29(10), 1180–1185, 1994.

19. T. Rueger, A 110 dB ternary PWM current-mode audio DAC with monolithic 2 Vrms driver, ISSCC Dig. of Tech. Pap., February 2004.

20. M. Tiilikainen, A 14-bit 1.8 V 20 mW 1 mm2 CMOS DAC, IEEE J. Solid-State Circuits, 36(7), 1144–1147 , 2001.

21. A. Van den Boschet al., SFDR-bandwidth limitations for high-speed high-resolution current-steering CMOS D/A converters, Proc. IEEE Int. Conf. Electron., Circuits, and Syst., pp. 1193–1196, 1999.

22. Y. Cong et al., A 1.5 V 14-bit 100 MSPS self-calibrated DAC, IEEE J. Solid-State Circuits, 38(12), 2051– 2060, 2003.

23. D. Reynolds, MOS current source layout technique to minimize deviation, U.S. Patent 5,568,145, October 22, 1996.

24. D. Mercer et al., Skewless differential switch and DAC employing the same, U.S. Patent 5,689,257, November 18, 1997.

25. X.M. Gong, Digital signal processor with reduced pattern dependent noise, U.S. Patent no. 5,719,572, February 17, 1999.

26. D. Mercer, Differential current switch, U.S. Patent 6,031,477, February 29, 2000.

27. D. Mercer and W. Schofield, Calibrated current source, U.S. Patent 6,583,740, June 24, 2003.

28. D. Mercer and W. Schofield, Digital/analog converter including gain control for a sub-digital/analog converter, U.S. Patent 6,738,006, May 18, 2004.

29. D. Mercer and W. Schofield, Current DAC code independent switching, U.S. Patent 6,768,438, July 27, 2004.

30. D. Mercer, Latch with data jitter free clock load, U.S. Patent 7,023,255, April 4, 2006.

31. AD9754 data sheet.

32. AD9744 data sheet.

33. T. Chen et al., The analysis and improvement of a current-steering DACs dynamic SFDR—I: The cell- dependent delay differences, IEEE Trans. Circuits Syst.-I, 53(1), 3–15, 2006.

.. |image1| image:: https://wiki.analog.com/_media/university/courses/tutorials/figure14.png
   :width: 620px
