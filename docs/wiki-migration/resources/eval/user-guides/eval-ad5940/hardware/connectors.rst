Connectors
==========

Electrode Connector–P8 This connector provides the primary analog input interface to which customer proprietary lead sets are connected. Connector P8 is a DB15 female connector and mates with a D-SUB plug. All ADAS1021 electrode connections are made available here for both master and slave devices in addition to the Right Leg Drive (RLD_OUT) and Shield Drive (SHIELD) pins.

Note that every effort was made to supply input protection to the electrode pins sufficient for the application; however, the intent was not to offer this module as a true medical solution. Therefore, no defibrillation pulses or voltages outside the ADAS1021 operating range should be applied to the input connector/board.

+--------+----------+----------------------------------------------------------------------------+
| Pin No | MnemoniC | Description                                                                |
+========+==========+============================================================================+
| 1      | V2       | Analog input, Master ECG5_V2                                               |
+--------+----------+----------------------------------------------------------------------------+
| 2      | V3       | Analog input, Slave ECG1_V3                                                |
+--------+----------+----------------------------------------------------------------------------+
| 3      | V4       | Analog input, Slave ECG2_V4                                                |
+--------+----------+----------------------------------------------------------------------------+
| 4      | V5       | Analog input, Slave ECG3_V5                                                |
+--------+----------+----------------------------------------------------------------------------+
| 5      | V6       | Analog input, Slave ECG4_V6                                                |
+--------+----------+----------------------------------------------------------------------------+
| 6      | SHIELD   | Output of shield driver                                                    |
+--------+----------+----------------------------------------------------------------------------+
| 7      | CE       | Common electrode, Master CM_IN                                             |
+--------+----------+----------------------------------------------------------------------------+
| 8      | NC       | Not connected                                                              |
+--------+----------+----------------------------------------------------------------------------+
| 9      | RA       | Analog input, right arm, Master ECG3_RA                                    |
+--------+----------+----------------------------------------------------------------------------+
| 10     | LA       | Analog input, left arm, Master ECG1_LA                                     |
+--------+----------+----------------------------------------------------------------------------+
| 11     | LL       | Analog input, left leg, Master ECG2_LL                                     |
+--------+----------+----------------------------------------------------------------------------+
| 12     | V1       | Analog input, Master ECG4_V1                                               |
+--------+----------+----------------------------------------------------------------------------+
| 13     | Spare    | Analog input, chest electrode or auxiliary bio-potential input, Slave ECG5 |
+--------+----------+----------------------------------------------------------------------------+
| 14     | RLD      | Right leg drive, RLD_OUT                                                   |
+--------+----------+----------------------------------------------------------------------------+
| 15     | NC       | Not connected                                                              |
+--------+----------+----------------------------------------------------------------------------+
