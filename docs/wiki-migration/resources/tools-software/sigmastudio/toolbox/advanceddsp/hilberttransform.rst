Hilbert Transform
=================

| 
| :doc:`Click here to return to the Advanced DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/advanceddsp>`
| The Hilbert Transform block is used to compute the imaginary part(y(t)) of the analytic signal xa(t)from given its real part (x(t)). Hilbert transform will phase shift every component in x(t) by ± 90 degrees.\|\ |image1|
| ====Input Pins====

=============== ================================== ====================
Name            Format [int/dec] - [control/audio] Function Description
=============== ================================== ====================
Pin 0: Audio In decimal - audio                    Audio Input
=============== ================================== ====================

Output Pins
-----------

================ ================================== ====================
Name             Format [int/dec] - [control/audio] Function Description
================ ================================== ====================
Pin 0: Real      decimal - audio                    Audio output
Pin 1: Imaginary decimal - audio                    Audio output
================ ================================== ====================

| 
| ==== DSP Parameters ==== NO DSP Parameters.
| ==== Configurable Parameters ==== No Configurable Parameters

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/advanceddsp/hilberttransform.jpg
