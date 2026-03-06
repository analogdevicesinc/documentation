AD74115H Surge Test Results
===========================

The surge immunity test indicates the capability of the device or equipment to survive surges caused by events such as lightning strikes or industrial power surges caused by switching heavy loads or short-circuit fault conditions.

Per the IEC 61000-4-5 standard for industrial environments, the surge is a combination wave of 1.2 μs rising time with 50 μs pulse width open circuit voltage and 8 μs rising time with 20 μs pulse width short-circuit current. The DUT (Device under test) is subject to five positive and five negative surges at each rating. The interval between each surge is 1 min. The surge is tested to the AD74115H output cable, which is treated as unshielded asymmetrically operated interconnection lines of the DUT. The surge is applied to the I/O and sense lines through CDN 117.

The CDNs (coupling decoupling network) do not influence the specified functional conditions of the DUT. The interconnection line between the DUT and the CDN is 2 m in length or shorter

Table 1 IEC 61000-4-5 Surge Test Levels
---------------------------------------

===== =================
Level Voltage Peak (kV)
===== =================
1     0.5
2     1
3     2
4     4
===== =================

| 
| |image1|

.. container:: centeralign

   *Figure 1 ADP1034 and AD74115H Surge Block Diagram*


| 
| ===Hardware Configuration=== The use cases tested during surge testing were voltage output (and voltage input by reconfiguring the ADC input nodes), internal digital output sourcing and sinking. The external sense pins SENSE_EXT1 and SENSE_EXT2 were also subject to testing. The reasoning for these particular use cases were to ensure the integrity of the I/O and sense screw terminals along with the internal fets used for the internal digital output use case. The surge was coupled to each screw terminal one at a time with respect to IO_N (AGND). Unshielded cable was used for all use cases.

For the voltage output use case, 6 V was configured as the output into a 100 kΩ load connected between IO_P and IO_N. The measurement (voltage input) was configured as IO_P to IO_N in the range 0 V to 12 V. The SENSE_EXT1 and SENSE_EXT2 nodes were selected as diagnostic nodes and configured as inputs to the ADC in the range 0 V to 12 V. Two AA batteries connected in series were used as a 3.1 V input to each of the SENSE_EXTx pins.

For internal digital output a 1 kΩ load resistor was connected between IO_P and IO_N. The measurement was configured for the internal diagnostic of current flowing through the internal RSET.

Software Configuration
----------------------

The software used was the evaluation software made available with the AD74115H evaluation board. At the beginning of each test the pre test configuration was performed. Before the discharges were applied the pre measurement flow of was taken. After discharges the post measurement was taken.

Pre test configuration

::

   *Reset DUT
   *Clear alert status register
   *Configure channel use case
   *Configure ADC measurement nodes
   *Configure ADC sample rate for 20 SPS

Pre and Post Measurement Flow

::

   *Read and store alert status register
   *Clear alert status register
   *Read ADC data
   *Save data to file

| 

Performance Summary
-------------------

| Table 2 gives a summary of the surge test results. For the digital output use cases a deviation is not recorded as the accuracy is dependent on the load. The test verified that the digital output did not turn off unexpectedly. The ADC conversion error bit in the Alert Status register was set after each test. The ADC error indicates a saturation error (ADC measurement is reading full scale) indicating that > 12 V of the surge voltage was observed on the pin under test.

Table 2 Surge Results
---------------------

+------------+--------------------------------+----------------------+-----------------------+------------------+-------------+
| Test Level | Use Case                       | Pre Test Measurement | Post Test Measurement | Deviation (%FSR) | Performance |
+============+================================+======================+=======================+==================+=============+
| 1 kV       | Voltage Output                 | 5.9942 V             | 5.9940 V              | − 0.00016        | Class B     |
+------------+--------------------------------+----------------------+-----------------------+------------------+-------------+
| :::        | SENSE EXT1                     | 3.1086 V             | 3.1084 V              | − 0.00016        | Class B     |
+------------+--------------------------------+----------------------+-----------------------+------------------+-------------+
| :::        | SENSE EXT2                     | 3.1015 V             | 3.1017 V              | 0.00016          | Class B     |
+------------+--------------------------------+----------------------+-----------------------+------------------+-------------+
| :::        | Digital Output Internal Source | 22.55 mA             | 21.98 mA              | N/A              | Class B     |
+------------+--------------------------------+----------------------+-----------------------+------------------+-------------+
| :::        | Digital Output Internal Sink   | 22.49 mA             | 22.49 mA              | N/A              | Class B     |
+------------+--------------------------------+----------------------+-----------------------+------------------+-------------+
| − 1 kV     | Voltage Output                 | 5.9942 V             | 5.9940 V              | − 0.00016        | Class B     |
+------------+--------------------------------+----------------------+-----------------------+------------------+-------------+
| :::        | SENSE EXT1                     | 3.1088 V             | 3.109 V               | 0.00016          | Class B     |
+------------+--------------------------------+----------------------+-----------------------+------------------+-------------+
| :::        | SENSE EXT2                     | 3.1017 V             | 3.019 V               | 0.00016          | Class B     |
+------------+--------------------------------+----------------------+-----------------------+------------------+-------------+
| :::        | Digital Output Internal Source | 22.55 mA             | 21.98 mA              | N/A              | Class B     |
+------------+--------------------------------+----------------------+-----------------------+------------------+-------------+
| :::        | Digital Output Internal Sink   | 22.49 mA             | 22.49 mA              | N/A              | Class B     |
+------------+--------------------------------+----------------------+-----------------------+------------------+-------------+

| 
| :doc:`Return to AD74115H Immunity Performance </wiki-migration/resources/technical-guides/ad74115_immunity_performance>`

.. |image1| image:: https://wiki.analog.com/_media/resources/technical-guides/surge_block_diagram.png
   :width: 800px
