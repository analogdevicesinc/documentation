| :doc:`Click here to return to the IO page </wiki-migration/resources/tools-software/sigmastudiov2/modules/inputoutput>`
| ====== SPDIF Output ======
| |spdif_op_ssp.jpg|
| ===== Description =====
| The SPDIF Output blocks route signals between the schematic design and the hardware's SPDIF pins.
| ===== Usage =====
| Use the output block's drop-down list control to select from the available SPDIF outputs.

|

.. note::

   Note: These blocks are only available for use with DSPs that have SPDIF I/O.


| ===== Targets Supported =====

+--------------+------------+-----------------------+----------------+------------------+
| Name         | ADSP-214xx | ADSP-215xx/ADSP-SC5xx | ADAU145x/1456x | ADSP-218xx/SC8xx |
+==============+============+=======================+================+==================+
| SPDIF Output | NA         | NA                    | S              | NA               |
+--------------+------------+-----------------------+----------------+------------------+

| 
| ===== Pins =====

Input
=====

====== ===== =============================
Name   Type  Description
====== ===== =============================
Output Audio Interface read output channel
====== ===== =============================

| 
| ===== Configurable Parameters =====

+------------------------+---------------+--------+-------------------------------+
| GUI Parameter Name     | Default Value | Range  | Function Description          |
+========================+===============+========+===============================+
| SelectedSPDIFOPChannel | 0             | 0 to 2 | Selects the SPDIF out channel |
+------------------------+---------------+--------+-------------------------------+

| 
| ===== DSP Parameters ===== Not applicable

| 
| ===== DSP Parameter Computation ===== Not applicable

.. |spdif_op_ssp.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/inputoutput/spdif_op_ssp.jpg
