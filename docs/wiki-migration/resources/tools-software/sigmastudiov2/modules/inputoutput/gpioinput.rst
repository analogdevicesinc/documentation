:doc:`Click here to return to the IO page </wiki-migration/resources/tools-software/sigmastudiov2/modules/inputoutput>`

GPIO Input and GPIO Output
==========================

| 
| ===GPIO Input=== |gpio_ip_ssp.jpg|
| ===GPIO Output===

| |gpio_op_ssp.jpg|
| ===== Description =====
| The General Purpose Input block allows signals from the hardware's GPIO input pins to be used in a schmeatic design. The output pin should typcially be connected to a GPIO Conditioning block. There are 26 selectable inputs to this GPIO block.

The General Purpose Output block routes a signal to the hardware's GPIO output. Each block is linked to one output channel.

|

.. note::

   Note: The block is only available for DSPs that include GPIO. To configure the hardware's GPIO input and outputs settings, see the processors Register Control Window.


| ===== Usage =====
| To use the GPIO Input: Select the channel desired for sending your signal using the General Purpose Input drop-down control.

-  Every enabled input must be connected to an output, else there will be errors on compilation.
-  Observe that as you drag more output blocks to your schematic, your number of input channels available in the drop-down decreases.

To use the GPIO Output:

-  Use the drop-down to select the hardware GPIO output that is assigned to the block.
-  Observe that as you drag more blocks to your schematic, your number of output channels available in the drop-down list decreases.

Targets Supported
-----------------

+-------------+------------+-----------------------+---------------+------------------+
| Name        | ADSP-214xx | ADSP-215xx/ADSP-SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=============+============+=======================+===============+==================+
| GPIO Input  | NA         | NA                    | S             | NA               |
+-------------+------------+-----------------------+---------------+------------------+
| GPIO Output | NA         | NA                    | S             | NA               |
+-------------+------------+-----------------------+---------------+------------------+

| 
| ===== Pins =====

GPIO Input
~~~~~~~~~~

Output
^^^^^^

======= ===== ================
Name    Type  Description
======= ===== ================
Output0 Logic Output channel 0
======= ===== ================

| 
| ====GPIO Output====

Input
^^^^^

====== ===== ===============
Name   Type  Description
====== ===== ===============
Input0 Logic Input channel 0
====== ===== ===============

| 

Configurable Parameters
-----------------------

+---------------------+---------------+-------------------+---------------------------------+
| GUI Parameter Name  | Default Value | Range             | Function Description            |
+=====================+===============+===================+=================================+
| SelectedGPIOChannel | GPIO_0        | GPIO_0 to GPIO_25 | Sets the GPIO channel selection |
+---------------------+---------------+-------------------+---------------------------------+

| 
| ===== DSP Parameters ===== Not applicable

.. |gpio_ip_ssp.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/inputoutput/gpio_ip_ssp.jpg
.. |gpio_op_ssp.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/inputoutput/gpio_op_ssp.jpg
