Power Connections
=================

There are two options for supplying power to the board. The default power supply comes from the connector P2 5V pin provided by the host microcontroller. This supply drives the ADP5320 to generate low noise 5V, 1.8V and 1.2 V and 3.3V supplies for the ADAS1021. Ensure that P9 and P10 are in position 2,3 with AVDDS5V,1V8, IOVDD and DVDD jumpers in place. Alternatively, the board can be powered from connector P1 and P7. • Remove AVDD5V, 1V8, IOVDD and DVDD jumpers • Supply power through P1 and P7.

============================= ========= =============== =============
Supply Requirement            Parameter Connector & Pin Supply Range
============================= ========= =============== =============
Alternative Supplies(P1 & P7) AVDD      P1 Pin 3        +5V ± 5%
\                             IOVDD     P7 Pin 1        1.71V to 3.6V
\                             ADVDD1V8  P1 Pin 1        1.8V ± 5%
\                             DVDD      P7 Pin 3        1.2V ± 5%
\                             AGND      P1 Pin 2        Ground
\                             DGND      P7 Pin 2        Ground
============================= ========= =============== =============
