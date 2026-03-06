AD74115H ESD Test Results
=========================

The electrostatic discharge (ESD) immunity test emulates the discharges of tens of nanoseconds duration directly on the electronic components. Two discharge methods are used: Contact Discharge and Air Discharge. Contact discharge includes discharge to the conductive surfaces of the DUT (Device under test). (An ESD test generator is used with a “sharp point” to make direct connection to the DUT (pin) for Contact ESD testing. A “round tip” is added to the generator and is brought close to the DUT (pin) to trigger a spark for Air-Gap ESD testing. The IEC 61000-4-2 test levels are listed in Table 1.

Table 1 IEC 61000-4-2 Test Levels
---------------------------------

===== ====================== ==================
Level Contact Discharge (kV) Air Discharge (kV)
===== ====================== ==================
1     2                      2
2     4                      4
3     6                      8
4     8                      15
===== ====================== ==================

There are two methods of applying the discharges, direct and indirect. Direct application involves direct contact to the conductive surfaces and coupling planes. Indirect application involves air discharge at insulating surfaces. The DUT is exposed to at least 20 discharges at each rating for each type of discharge, 10 each at negative and positive polarity. The discharges are repeated at a rate of one discharge per second.

The test setup consists of a nonconductive table with a height of 0.8 m, standing on the ground reference plane. A 1.6 m × 0.8 m horizontal coupling plane (HCP) is placed on the table. The DUT and its cable are isolated from the coupling plane by an insulating mat that is 0.5 mm thick.

The contact discharges are applied to the IO_P and IO_N terminal screws of the AD74115H output terminal block P21. The AD74115H also has two uncommitted high voltage sense pins (SENSE_EXT1 and SENSE_EXT2) that can be measured with the ADC. The contact discharges were also applied to the terminal screws of the AD74115H terminal block P8.

The air discharges are applied to both AD74115H output (P21) and sense (P8) terminal blocks.

The coupling discharge are applied to the horizontal coupling plane (HCP) and vertical coupling plane (VCP). The coupling plane has two 470 kΩ bleeding resistors to the ground reference plane (GRP) which is connected to earth ground.

| 
| ===Hardware Configuration=== There was a digital multi meter (DMM) connected to the output load to ensure there was no loss of output during testing and also to ensure the integrity of the internal ADC measurement. To protect the DMM a low pass filter was placed between the load and DMM. The measurements were streamed back to the laptop throughout the testing.
| The AD74115H was tested using 3 use cases to exercise all terminal blocks.

-  Current Output Use Case:

   -  Used to check the integrity of IO_P and IO_N.
   -  Shielded cable was connected to IO_P and IO_N and a 500 Ω load while the output was set to 12.5 mA.
   -  DMM used to measure the current at the load.
   -  Also covers Voltage Input use case since the measurement path is identical (SENSELF to AGND_SENSE).

-  3 and 4 Wire RTD Use Case:

   -  Used to check the integrity of SENSE_EXT1 and SENSE_EXT2.
   -  Shielded cable was connected to the screw terminals to a junction box and a RTD connected at the junction box.
   -  Internal ADC used to measure the RTD resistance.

::

     * 

| |image1|

.. container:: centeralign

   *Figure 1 ADP1034 and AD74115H Current Output ESD Setup*


| |image2|

.. container:: centeralign

   *Figure 1 ADP1034 and AD74115H 4 wire RTD ESD Setup*


| |image3|

.. container:: centeralign

   *Figure 3 ADP1034 and AD74115H Test Setup*


Software Configuration
----------------------

The software was written in python to facilitate interaction with DMM and DUT simultaneously. At the beginning of each test the pre test configuration was performed. Before the discharges were applied the pre measurement flow of 1000 samples were taken. After discharges the post measurement of 1000 samples were taken. Each sample (ADC and DMM) was taken approximately every 25 ms. Pre test configuration

::

   *Reset DUT
   *Clear alert status register
   *Configure channel use case
   *Configure ADC measurement
   *Configure ADC sample rate for 20 SPS

Pre and Post Measurement Flow

::

   *Read and store alert status register
   *Clear alert status register
   *Read ADC code
   *Read DMM measurement
   *Save data to file
   *Repeat 1000 times

| 

Performance Summary
-------------------

Table 2 gives a summary of the ESD test results. The AD74115H was tested to level 3 according to IEC 61000-4-2 and achieved class B. There were no alert status bits activated throughout the testing. The current output use case is measured with the DMM and the RTD results are measured using the internal ADC. The ADC result is converted according to the transfer function available in the AD74115H datasheet.

Table 2 Contact Discharge Results
---------------------------------

+------------+----------------+------------------+----------------------+-----------------------+------------------+-------------+
| Test Level | Use Case       | Contact Terminal | Pre Test Average ADC | Post Test Average ADC | Deviation (%FSR) | Performance |
+============+================+==================+======================+=======================+==================+=============+
| 6 kV       | Current Output | IO_P             | 12.49870932 mA       | 12.4973029 mA         | -0.005626        | Class B     |
+------------+----------------+------------------+----------------------+-----------------------+------------------+-------------+
| :::        | :::            | IO_N             | 12.498586 mA         | 12.498401 mA          | -0.000739        | Class B     |
+------------+----------------+------------------+----------------------+-----------------------+------------------+-------------+
| :::        | 3 Wire RTD     | SENSE_EXT1       | 108.03452 Ω          | 108.0265 Ω            | -0.001526        | Class B     |
+------------+----------------+------------------+----------------------+-----------------------+------------------+-------------+
| :::        | 4 Wire RTD     | SENSE_EXT2       | 108.2588 Ω           | 108.2588 Ω            | 0.00000          | Class B     |
+------------+----------------+------------------+----------------------+-----------------------+------------------+-------------+
| - 6 kV     | Current Output | IO_P             | 12.497498 mA         | 12.497218 mA          | -0.001118        | Class B     |
+------------+----------------+------------------+----------------------+-----------------------+------------------+-------------+
| :::        | :::            | IO_N             | 12.497502 mA         | 12.497302 mA          | -0.000801        | Class B     |
+------------+----------------+------------------+----------------------+-----------------------+------------------+-------------+
| :::        | 3 Wire RTD     | SENSE_EXT1       | 108.06656 Ω          | 108.08258 Ω           | 0.003052         | Class B     |
+------------+----------------+------------------+----------------------+-----------------------+------------------+-------------+
| :::        | 4 Wire RTD     | SENSE_EXT2       | 108.25081 Ω          | 108.25081 Ω           | 0.00000          | Class B     |
+------------+----------------+------------------+----------------------+-----------------------+------------------+-------------+

Table 3 Coupling Discharge Results
----------------------------------

+------------+----------------+------------------+------------------+-------------------+------------------+-------------+
| Test Level | Use Case       | Contact Terminal | Pre Test Average | Post Test Average | Deviation (%FSR) | Performance |
+============+================+==================+==================+===================+==================+=============+
| 6 kV       | Current Output | HCP              | 12.497659 mA     | 12.497732 mA      | 0.000290         | Class B     |
+------------+----------------+------------------+------------------+-------------------+------------------+-------------+
| :::        | :::            | VCP              | 12.497540 mA     | 12.497368 mA      | -0.000688        | Class B     |
+------------+----------------+------------------+------------------+-------------------+------------------+-------------+
| :::        | 3 Wire RTD     | HCP              | 108.00247 Ω      | 108.01048 Ω       | 0.001526         | Class B     |
+------------+----------------+------------------+------------------+-------------------+------------------+-------------+
| :::        | :::            | VCP              | 108.01849 Ω      | 108.01849 Ω       | 0.000000         | Class B     |
+------------+----------------+------------------+------------------+-------------------+------------------+-------------+
| - 6 kV     | Current Output | HCP              | 12.499020 mA     | 12.497677 mA      | -0.005375        | Class B     |
+------------+----------------+------------------+------------------+-------------------+------------------+-------------+
| :::        | :::            | VCP              | 12.497425 mA     | 12.497287 mA      | -0.000551        | Class B     |
+------------+----------------+------------------+------------------+-------------------+------------------+-------------+
| :::        | 3 Wire RTD     | HCP              | 108.01048 Ω      | 108.01048 Ω       | 0.000000         | Class B     |
+------------+----------------+------------------+------------------+-------------------+------------------+-------------+
| :::        | :::            | VCP              | 108.01849 Ω      | 108.01849 Ω       | 0.000000         | Class B     |
+------------+----------------+------------------+------------------+-------------------+------------------+-------------+

Table 4 Air Discharge Results
-----------------------------

+------------+----------------+------------------+------------------+-------------------+------------------+-------------+
| Test Level | Use Case       | Contact Terminal | Pre Test Average | Post Test Average | Deviation (%FSR) | Performance |
+============+================+==================+==================+===================+==================+=============+
| 8 kV       | Current Output | IO_P             | 12.497896 mA     | 12.497660 mA      | -0.000944        | Class B     |
+------------+----------------+------------------+------------------+-------------------+------------------+-------------+
| :::        | :::            | IO_N             | 12.497921 mA     | 12.497885 mA      | -0.000143        | Class B     |
+------------+----------------+------------------+------------------+-------------------+------------------+-------------+
| :::        | 3 Wire RTD     | SENSE_EXT1       | 108.01849 Ω      | 108.01849 Ω       | 0.000000         | Class B     |
+------------+----------------+------------------+------------------+-------------------+------------------+-------------+
| - 8 kV     | Current Output | IO_P             | 12.497937 mA     | 12.498807 mA      | 0.003482         | Class B     |
+------------+----------------+------------------+------------------+-------------------+------------------+-------------+
| :::        | :::            | IO_N             | 12.499036 mA     | 12.497757 mA      | -0.005115        | Class B     |
+------------+----------------+------------------+------------------+-------------------+------------------+-------------+
| :::        | 3 Wire RTD     | SENSE_EXT1       | 108.01849 Ω      | 108.0265 Ω        | 0.001526         | Class B     |
+------------+----------------+------------------+------------------+-------------------+------------------+-------------+

| 
| :doc:`Return to AD74115H Immunity Performance </wiki-migration/resources/technical-guides/ad74115_immunity_performance>`

.. |image1| image:: https://wiki.analog.com/_media/resources/technical-guides/IMG_20211012_142910.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/technical-guides/4rtd.jpg
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/technical-guides/esd_block_diagram_2.png
   :width: 800px
