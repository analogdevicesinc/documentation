NXP i.MX8M SOM + Carrier Board
==============================

The

\*\* Product Page \*\*

**IMAGE OF CROSBY**

Simplified Block Diagram
------------------------

For full block diagram please refer to datasheet

\*Link to ADSD3100 datasheet \*Link to NVM

Context of EVAL-ADTF3175-NXZ platforms
--------------------------------------

ADSD3100 FW, ADSD3500 FW, and calibration information is stored on an ADTF3175 onboard NVM. Before running the module, an application processor will program the ADSD3100 with the FW provided, and configure the configure the calibration parameters. If the Link:ADSD3500 is used (EVAL-ADTF3175D-NXZ), it will self-boot and program itself with the NVM contents.

After the imager is configured an FSYNC is used to trigger the imager to capture data. The raw frame data (consisting of 9 frames) is piped through MIPI to the application processor or ADSD3500 for further processing.
