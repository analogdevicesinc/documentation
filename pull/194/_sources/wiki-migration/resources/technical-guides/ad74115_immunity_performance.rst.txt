AD74115H Immunity Performance
=============================

Introduction
------------

The :adi:`AD74115H` is a single-channel software configurable input/output device for industrial control applications. The AD74115H provides analog output, analog input, digital output, digital input, 2-, 3- and 4– wire resistance temperature detector (RTD) and thermocouple measurements integrated into a single chip solution with a serial peripheral interface (SPI) and an integrated HART modem. The AD74115H is designed to operate with a companion power & isolation chip. The :adi:`ADP1034` is a high performance, isolated micropower management unit (microPMU) that provides three isolated power rails. The isolated rail VOUT1 can be programmed via the AD74115H reducing unnecessary power dissipation. Additionally, the ADP1034 contains four high speed serial peripheral interface (SPI) isolation channels and three general-purpose isolators for channel-to-channel applications where low power dissipation and small solution size are required.

| This technical guide demonstrates the robustness of the AD74115H and ADP1034 (using the :adi:`EVAL-AD74115H` evaluation board) during transient immunity testing. Testing is performed as per the IEC 61000-4-x set of standards that cover the evaluation of the immunity of electrical and electronic equipment at a system level. The AD74115H evaluation board is characterized to ensure that the circuit performance has sufficient immunity against electrostatic discharge (ESD), electrical fast transients (EFT), and surge.

Circuit Description
-------------------

| Figure 1 shows the connectivity between the AD74115H and the ADP1034. This diagram shows a fully isolated solution for a single channel software configurable I/O. The AVDD, AVCC, DVCC and AVSS supply voltages for the AD74115H are provided by the ADP1034. The AVDD supply is fixed at 24 V. To improve the accuracy of the input/output functions the ADR4525 2.5 V external reference is used. HART functionality is not enabled. The interface to the ADP1034 used is the SDP-K1 controller board. The resistor connecting the SDP-K1 GPIO to the AD74115H RESET pin is removed to mitigate the SDP-K1 pulling Reset low during testing.
| On-chip line protectors ensure that the I/OP screw terminal does not provide power to the IC when brought to a higher potential than the AVDD pin. The recommended external components documented in the :adi:`AD74115H` datasheet, including the TVS, are selected to withstand surge on the input/output terminals. With the recommended components, the I/OP and I/ON screw terminals tolerate over-voltages up to ± 36 V (limited by the external TVS).

Below is a summary of the configuration settings on the board:

::

   *System Supply (VINP) = 24 V
   *DO_VDD = AVDD = 24 V Excluding external digital output use case where DO_VDD = 21 V
   *2.5 V external reference connected to REFIN
   *AVSS = − 15 V
   *DVCC = AVCC = 5 V

| The AD74115H board was configured using the SDP-K1 interface board and a python script. |image1|

.. container:: centeralign

   *Figure 1 ADP1034 and AD74115H Block Diagram*


Performance Criteria
~~~~~~~~~~~~~~~~~~~~

The results of an immunity test are typically classified into four categories, as listed in Table 1. The end-application requirements and its ability to tolerate transient noise determine whether the system sees the specific performance criteria as a failure or not.

Table 1
~~~~~~~

+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Performance Criteria | Description                                                                                                                                                                                     |
+======================+=================================================================================================================================================================================================+
| Class A              | Normal performance within an error band specified by the manufacturer.                                                                                                                          |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Class B              | Temporary loss of function or degradation of performance which ceases after the disturbance is removed. The equipment under test recovers its normal performance without operator intervention. |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Class C              | Temporary loss of function or degradation of performance, correction of performance requires operator intervention such as manual restart, or power off, or power on, etc.                      |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Class D              | Loss of function or degradation of performance which is not recoverable, permanent damage to hardware or software, or loss of data.                                                             |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 

Performance Summary
-------------------

| Table 2 gives a summary of the immunity test results. More details are available on each test result linked at the end.

Table 2
~~~~~~~

+-------+---------------------------------------------+---------------+------------+------------+-------------+
| Test  | Use Case                                    | Standard      | Test Level | Cable Type | Performance |
+=======+=============================================+===============+============+============+=============+
| ESD   | Current Output                              | IEC 61000-4-2 | ± 6kV      | Shielded   | Class B     |
+-------+---------------------------------------------+---------------+------------+------------+-------------+
|       | 3/4 Wire RTD                                |               |            |            |             |
+-------+---------------------------------------------+---------------+------------+------------+-------------+
| EFT   | Current Output                              | IEC 61000-4-4 | ± 2kV      | Shielded   |             |
+-------+---------------------------------------------+---------------+------------+------------+-------------+
|       | 4 wire RTD                                  |               |            |            |             |
+-------+---------------------------------------------+---------------+------------+------------+-------------+
|       | Current Input Loop and Externally Powered   |               |            |            |             |
+-------+---------------------------------------------+---------------+------------+------------+-------------+
|       | Digital Input Logic                         |               |            | Unshielded |             |
+-------+---------------------------------------------+---------------+------------+------------+-------------+
|       | Digital Output Internal and External Source |               |            |            |             |
+-------+---------------------------------------------+---------------+------------+------------+-------------+
| Surge | Voltage Output                              | IEC 61000-4-5 | ± 1kV      | Unshielded |             |
+-------+---------------------------------------------+---------------+------------+------------+-------------+
|       | Voltage Input                               |               |            |            |             |
+-------+---------------------------------------------+---------------+------------+------------+-------------+
|       | Digital Output Internal Sink and Source     |               |            |            |             |
+-------+---------------------------------------------+---------------+------------+------------+-------------+

| 
| The guide below provides the links to each set of test results:

::

   *[[/resources/technical-guides/esd|AD74115H ESD Test Results]] - Provides all the details of the ESD tests and results. 
   *[[/resources/technical-guides/eft|AD74115H EFT Test Results]] - Provides all the details of the ESD tests and results. 
   *[[/resources/technical-guides/surge|AD74115H Surge Test Results]] - Provides all the details of the ESD tests and results. 

.. |image1| image:: https://wiki.analog.com/_media/resources/technical-guides/ad74115h_adp1034_circuit_diagram.png
   :width: 900px
