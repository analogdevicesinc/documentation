:doc:`Click here to return to the Master Control Port page </wiki-migration/resources/tools-software/sigmastudiov2/modules/mastercontrolport>`

Master Control Port Status
==========================

| 
| |mc_status_ssp.jpg|
| ===== Description =====
| The master control port Status block sends out the Master control port status in the output pins. Master control errors can be cleared by setting input pin to non-zero value
| ===== Usage =====
| Use the output pins to monitor master control port status and error. The error can be cleared by inputting a non-zero value at the input.
| ===== Targets Supported =====

+----------------------------+------------+-----------------------+----------------+------------------+
| Name                       | ADSP-214xx | ADSP-215xx/ADSP-SC5xx | ADAU145x/1456x | ADSP-218xx/SC8xx |
+============================+============+=======================+================+==================+
| Master Control Port Status | NA         | NA                    | S              | NA               |
+----------------------------+------------+-----------------------+----------------+------------------+

| 
| ===== Pins =====
| ====Input Pins====

=========== ======= ==================================================
Name        Type    Description
=========== ======= ==================================================
ClearErrors Control Any non -zero value in the input clears the error.
=========== ======= ==================================================

| 
| ====Output Pins====

+----------------+---------+----------------------------------------------------------------------------------------------------------+
| Name           | Type    | Description                                                                                              |
+================+=========+==========================================================================================================+
| Status         | Control | Outputs 1 while the Master control port is busy, otherwise outputs 0                                     |
+----------------+---------+----------------------------------------------------------------------------------------------------------+
| I2CErrorStatus | Control | It is a 2 bit value. Bit-0 is set if I2C error is encountered. Bit-1 is set when timeout error occurred. |
+----------------+---------+----------------------------------------------------------------------------------------------------------+

| 
| ===== Configurable Parameters =====
| Not applicable

DSP Parameters
--------------

| 
| Not applicable
| ===== DSP Parameter Computation =====
| Not applicable

.. |mc_status_ssp.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mastercontrolport/mc_status_ssp.jpg
