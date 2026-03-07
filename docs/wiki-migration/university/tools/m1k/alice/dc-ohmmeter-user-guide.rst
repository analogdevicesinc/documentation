DC Ohmmeter Virtual Instruments for ADALM1000 in ALICE 1.3
==========================================================

Objective:
----------

This document serves as the DC Ohmmeter section of the User’s Guide in the ALICE 1.3 Desktop software interface written for use with the ADALM1000 active learning kit hardware.

DC Ohmmeter Window:
-------------------

The method used to measure unknown resistance is based on the voltage divider configuration shown figure 1.

.. image:: https://wiki.analog.com/_media/university/tools/ohm-meter-fig6.png
   :align: center
   :width: 450px

.. container:: centeralign

   Figure 1, Voltage Divider Method


If we assume that voltage source V\ :sub:`S` is known, resistance of R\ :sub:`1` is known and we can measure voltage V\ :sub:`2`, the voltage across R\ :sub:`2`, we can use the voltage divider formula to calculate the resistance of R\ :sub:`2`.

:math:`V_2 = V_S \times (R_2/( R_1 + R_2 ))`

Which can be rearranged to:

:math:`R_2 = R_1 \times (V_2 / (V_S - V_2))`

There is a certain advantage to using this voltage divider method over the Ohm's Law method in that a much wider range of resistances can be measured. The Ohm's Law method is limited in one extreme by the maximum current that the ALM1000 can safely source ( about 200 mA or 5 Ohms ) and in the other by the minimum current that the ALM1000 can accurately measure ( about 200 uA or 25 KOhms). Using the voltage divider method, because we can choose a range of R\ :sub:`1` values, we are only limited by the voltage measurement resolution of the ALM1000 (about 100 uV). R\ :sub:`1` can range from as low as 10 Ohms to as high as 10 KOhms in practice which extends the range from 1 Ohm or less to nearly a MOhm.

For the highest values of R\ :sub:`2` the internal 1 MOhm resistance of Channel B comes into effect and the software removes this parallel resistance when calculating the value for R\ :sub:`2`.

Slight Variation:
~~~~~~~~~~~~~~~~~

Built into the ALM1000 is a switch that can connect an on-board 50 Ohm resistor from the channel B input / output pin to ground. We can use this "known" resistor as R\ :sub:`2` in the voltage divider figure and calculate for R\ :sub:`1` instead.

:math:`\displaystyle R_1 = R_2 \times (\frac{V_S - V_2}{V_2})`

The series resistance of the switch, which is approximately 1 Ohm, must be included in the value of R\ :sub:`2`. The actual value for R\ :sub:`2` is more like slightly less than 51 Ohms. Of course the true value for R\ :sub:`2` can be found by calibrating its value based on measuring a known precision resistor standard.

Both ways can be used in the DC Ohmmeter tool. The test voltage can be adjusted as well as the value of the known resistor. The Ext Int selector picks which variation will be used to calculate the unknown resistance.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/dc-ohmmeter-screen.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure2, DC Ohmmeter window


**For Further Reading:**

**Return to the** :doc:`ALICE Main Page </wiki-migration/university/tools/m1k/alice/desk-top-users-guide>`\ **.**
