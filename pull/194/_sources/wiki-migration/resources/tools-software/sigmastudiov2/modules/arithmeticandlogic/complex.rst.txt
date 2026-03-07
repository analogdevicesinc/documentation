:doc:`Click here to return to the Arithmetic and Logic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic>`

Complex Magnitude
=================

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic/complexmagnitude.png
   :alt: complexmagnitude.png

Description
-----------

| Conjugate Magnitude takes the Complex Signal(x + j y) of input signal and compute the magnitude (squareroot(x^2 + y^2)) of input signal and pass to output. This is a block based module.
| Note: The Context Menu “Input Source” option added to this module to select the algorithm for Complex FFT and Real FFT

Targets Supported
-----------------

+-------------------+---------------+------------+------------------+------------------+
| Name              | ADAU145x/146x | ADSP-214xx | ADSP-SC5xx/215xx | ADSP-218xx/SC8xx |
+===================+===============+============+==================+==================+
| Complex Magnitude | B             | NA         | NA               | NA               |
+-------------------+---------------+------------+------------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

===== ======= ====================
Name  Type    Description
===== ======= ====================
Input Complex Complex Input Signal
===== ======= ====================

Output
~~~~~~

====== ======= =====================================
Name   Type    Description
====== ======= =====================================
Output Control Magnitude of the Complex Input Signal
====== ======= =====================================

Configurable Parameters
-----------------------

No configurable parameters

DSP Parameters
--------------

NO DSP parameters
