AD-FMCMOTCON1-EBZ Signal Measurement Chain
==========================================


.. note::

   See `wiki/common <https://wiki.analog.com/wiki/common#retired>`_
 The motor control system allows the measurement of the Ia(phase A current), Ib(phase B current) and It(total current) as well as the measurement of Vbus using signal chains which involve components from both the controller and low voltage driver boards.

Ia, Ib Measurement Signal Chain
-------------------------------

The Ia and Ib currents are sensed using 6mΩ shunt resistors. There are two possible measurement paths showing measurement techniques for the case where the ADC can be placed close to the shunt resistor and for the case where the ADC cannot be placed in the proximity of the shunt resistor. Both techniques aim to get the best measurement accuracy.

**Case 1: The ADC is placed in the proximity of the shunt resistor**

-  The signal path between the shunt resistor and the ADC is very short and less prone to noise coupling.
-  The small differential voltage on the shunt resistor is measured directly with the :adi:`AD7401` isolated ΣΔ modulator without the need of extra interfacing and signal conditioning circuitry
-  The digital data and clock signals of the ADC travel the entire length of the drive and controller boards all the way to the FPGA. Since the analog signals were digitized close to the source and sent in a digital format to the FPGA there are no concerns related to the quality of the measurements.
-  The formula for calculating Ia or Ib is:

:math:`I = (counts - 32768) \times ADCrange / 2^{ADCbits-1} \times RS` where $delimlbracematrix{4}{1}\ |counts = ADC value } {RS = 6e-3} {ADCrange = 320e-3 } {ADCbits = 16| $

**Case 2: The ADC is not placed in the proximity of the shunt resistor**

-  The signal path between the shunt resistor and the ADC is long and very prone to noise coupling, especially due to the switching noise of the power stage that's driving the motor and to the motor itself. Special care must be taken in properly designing the signal conditioning circuitry that sits between the ADC and the shunt resistor and in properly shielding the analog signals on the way to the ADC.
-  The small differential voltage on the shunt resistor is amplified on the drive board with the :adi:`AD8207` difference amplifier placed close to the shunt resistor in order to avoid noise coupling. The signal is amplified from the 0..250mV input range to 0..5V to minimize the effect of the coupled noise.
-  The amplified signal goes on the drive board through another programmable amplification stage realized using the :adi:`AD8251` PGA. This ensures that the ADC will always receive at input signals properly scaled to fit its input range.
-  The amplified analog signals go through the connector to the controller board. The connector has proper shielding for each analog signal to mitigate noise coupling.
-  On the controller board the analog signals coming from the drive board are transferred from the +/-2.5V input range to a +/-250mV range suited for the :adi:`AD7401` ΣΔ modulator. The attenuation is done using the :adi:`ADA4084-2` amplifier.
-  The formula for calculating Ia or Ib is:

:math:`I = (counts-32768) \times ADCrange/2^{ADCbits-1} \times CTRLgain / (RS \times DRVgain \times PGAgain)` where $\\displaystyle delimlbracematrix{7}{1}\ |counts = ADC value } {RS = 6e-3} {ADCrange = 320e-3} {ADCbits = 16} \\frac{CTRLgain = 1}{10}{DRVgain = 20}{PGAgain = 1, 2, 4 or 8| $

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/current_chain.png
   :width: 800px

+---+
+---+

Ia, Ib XADC Measurement Signal Chain
------------------------------------

The Ia and Ib XADC measurement chain utilizes the entire path of the regular measurement chain and adds on the controller board after the :adi:`AD7401` isolated ΣΔ modulator a Sallen Key analog reconstruction filter implemented using :adi:`AD8646` operational amplifiers. The combination between the isolated ΣΔ modulator and the analog reconstruction filter provides a convenient and cheap way to achieve analog isolation of the XADC input signals. This analog isolation technique is described in this |paper|.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/current_chain_xadc.png
   :width: 800px

+---+
+---+

It Measurement Signal Chain
---------------------------

The It current is sensed using a 5mΩ shunt resistor. There are two possible measurement paths showing measurement techniques for the case where the ADC can be placed close to the shunt resistor and for the case where the ADC cannot be placed in the proximity of the shunt resistor. Both techniques aim to get the best measurement accuracy.

**Case 1: The ADC is placed in the proximity of the shunt resistor**

-  The signal path between the shunt resistor and the ADC is very short and less prone to noise coupling.
-  The small differential voltage on the shunt resistor is measured directly with the :adi:`AD7401` isolated ΣΔ modulator without the need of extra interfacing and signal conditioning circuitry
-  The formula for calculating It is:

| :math:`I = (32768-counts) \times ADCrange / 2^{ADCbits-1} \times RS` where $delimlbracematrix{4}{1}\ |counts = ADC value } {RS = 5e-3} {ADCrange = 320e-3 } {ADCbits = 16| $
| **Case 2: The ADC is not placed in the proximity of the shunt resistor**

-  The small differential voltage on the shunt resistor is amplified on the drive board with the :adi:`AD8630` difference amplifier placed close to the shunt resistor in order to avoid noise coupling. The signal is amplified to 0..5V to minimize the effect of the coupled noise.
-  The amplified signal goes on the drive board through another programmable amplification stage realized using the :adi:`AD8251` PGA. This ensures that the ADC will always receive at input signals properly scaled to fit its input range.
-  The amplified analog signals go through the connector to the controller board. The connector has proper shielding for each analog signal to mitigate noise coupling.
-  On the controller board the analog signals coming from the drive board are transferred from the 0..5V input range to a 0..250mV range suited for the :adi:`AD7401` ΣΔ modulator. The attenuation is done using the :adi:`ADA4084-2` amplifier.
-  The formula for calculating It is:

:math:`I = (32768-counts) \times ADCrange/2^{ADCbits-1} \times CTRLgain / (RS \times DRVgain \times PGAgain)` where $\\displaystyle delimlbracematrix{7}{1}\ |counts = ADC value } {RS = 5e-3} {ADCrange = 320e-3} {ADCbits = 16} \\frac{CTRLgain = 1}{10}{DRVgain = 20}{PGAgain = 1, 2, 4 or 8| $

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/current_chain_it.png
   :width: 800px

+---+
+---+

It XADC Measurement Signal Chain
--------------------------------

The It XADC measurement chain utilizes the entire path of the regular measurement chain and adds on the controller board after the :adi:`AD7401` isolated ΣΔ modulator a Sallen Key analog reconstruction filter implemented using :adi:`AD8646` operational amplifiers. The combination between the isolated ΣΔ modulator and the analog reconstruction filter provides a convenient and cheap way to achieve analog isolation of the XADC input signals. This analog isolation technique is described in this |paper|.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/current_chain_it_xadc.png
   :width: 800px

+---+
+---+

Vbus Measurement Signal Chain
-----------------------------

Vbus sensing is done on the drive board using a resistive divider and an attenuation circuit implemented with the :adi:`AD8207` operational amplifier. The total gain of this stage is 0.83 giving an output range of 0..5V. The analog signals go through the connector to the controller board. On the controller board the analog signals coming from the drive board are transferred from the 0..5V input range to a 0..250mV range suited for the :adi:`AD7401` ΣΔ modulator. The attenuation is done using the :adi:`ADA4084-2` amplifier.

-  The formula for calculating Vbus is:

:math:`V = (32768-counts) \times ADCrange / 2^{ADCbits-1} \times DRVgain \times CTRLgain` where :math:`\displaystyle delimlbracematrix{5}{1}{{counts = ADC value } {ADCrange = 320e-3 } {ADCbits = 16 } \frac{DRVgain=5}{60} \frac{CTRLgain=1}{10 }}{ }`


|image1|

+---+
+---+

Vbus XADC Measurement Signal Chain
----------------------------------

The Vbus XADC measurement chain utilizes the entire path of the regular measurement chain and adds on the controller board after the :adi:`AD7401` isolated ΣΔ modulator a Sallen Key analog reconstruction filter implemented using :adi:`AD8646` operational amplifiers. The combination between the isolated ΣΔ modulator and the analog reconstruction filter provides a convenient and cheap way to achieve analog isolation of the XADC input signals. This analog isolation technique is described in this |paper|.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/vbus_chain_xadc.png
   :width: 800px

+---+
+---+

.. image:: https://wiki.analog.com/_media/navigation AD-FMCMOTCON1-EBZ#lv_board
   :alt: Low Voltage Drive Board#..:\|Overview#dyno|Dynamometer Drive system

.. |counts = ADC value } {RS = 6e-3} {ADCrange = 320e-3 } {ADCbits = 16| image:: https://wiki.analog.com/_media/counts = ADC value } {RS = 6e-3} {ADCrange = 320e-3 } {ADCbits = 16
.. |counts = ADC value } {RS = 6e-3} {ADCrange = 320e-3} {ADCbits = 16} \\frac{CTRLgain = 1}{10}{DRVgain = 20}{PGAgain = 1, 2, 4 or 8| image:: https://wiki.analog.com/_media/counts = ADC value } {RS = 6e-3} {ADCrange = 320e-3} {ADCbits = 16} \frac{CTRLgain = 1}{10}{DRVgain = 20}{PGAgain = 1, 2, 4 or 8
.. |paper| image:: http://www.analog.com/static/imported-files/newsletters/digital_isolation/Using_the_AD7400A_as_an_Isolated_Amplifier.pdf
.. |counts = ADC value } {RS = 5e-3} {ADCrange = 320e-3 } {ADCbits = 16| image:: https://wiki.analog.com/_media/counts = ADC value } {RS = 5e-3} {ADCrange = 320e-3 } {ADCbits = 16
.. |counts = ADC value } {RS = 5e-3} {ADCrange = 320e-3} {ADCbits = 16} \\frac{CTRLgain = 1}{10}{DRVgain = 20}{PGAgain = 1, 2, 4 or 8| image:: https://wiki.analog.com/_media/counts = ADC value } {RS = 5e-3} {ADCrange = 320e-3} {ADCbits = 16} \frac{CTRLgain = 1}{10}{DRVgain = 20}{PGAgain = 1, 2, 4 or 8
.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/vbus_chain.png
   :width: 800px
