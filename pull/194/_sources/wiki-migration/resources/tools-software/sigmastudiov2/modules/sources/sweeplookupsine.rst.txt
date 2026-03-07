:doc:`Click here to return to the Sources page </wiki-migration/resources/tools-software/sigmastudiov2/modules/sources>`

Sweep Look Up Sine
==================

| |sweep_lookup.png|
| ===== Description =====
| The Sweep (Lookup/Sine) block generates a sinewave that sweeps from a start to an end frequency. The sweep speed is determined by the number of steps and cycles per step.
| ===== Usage =====
| Enter the desired start and stop frequency and step size using the edit controls:

-  **Initial Freq**

   -  The frequency at which to begin the sweep.

-  **Ending Freq**

   -  The frequency at which to end the sweep.

-  **Step**

   -  Determines the number of steps in the sweep.

-  **Reset**

   -  Resets the current sweep frequency to the "Initial Freq".

-  **Sweep**

   -  Starts the frequency sweep.

-  **Speed**

   -  Sets the sweep speed, the relative duration of each sweep step.

A valid slope range will be computed depending on the step size entered. The ending tone will be held until reset is clicked, which returns to the initial frequency. The plot below shows the correlation for sweep plots with varying step sizes and slopes.

| 
| |image1|
| ===== Targets Supported =====

+--------------------+------------+------------------+---------------+------------------+
| Name               | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+====================+============+==================+===============+==================+
| Sine Look up Sweep | NA         | NA               | S             | NA               |
+--------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Output
------

====== ===== ==============
Name   Type  Description
====== ===== ==============
Output Audio Output channel
====== ===== ==============

| 
| ===== Configurable Parameters =====

+--------------------+---------------+------------------------+--------------------------------------------------------+
| GUI Parameter Name | Default Value | Range                  | Function Description                                   |
+====================+===============+========================+========================================================+
| InitialFrequency   | 150           | 0 to 0.5\* sample rate | Sets the initial frequency for sinetone sweep          |
+--------------------+---------------+------------------------+--------------------------------------------------------+
| EndFrequency       | 10000         | 0 to 0.5\* sample rate | Sets the final/end frequency for sinetone sweep        |
+--------------------+---------------+------------------------+--------------------------------------------------------+
| SlewStep           | 16            | 1 to 23                | Slew step                                              |
+--------------------+---------------+------------------------+--------------------------------------------------------+
| Slope              | 1             | 0 to 12                | Gain, the sinetone wave to be multiplied in the lookup |
+--------------------+---------------+------------------------+--------------------------------------------------------+
| Sweep              | 1             | 0(off)/1(on)           | Switch on and off the sine sweep                       |
+--------------------+---------------+------------------------+--------------------------------------------------------+

| 
| ===== DSP Parameters =====

============== ======================================== =============
Parameter Name Description                              ADAU145x/146x
============== ======================================== =============
increment1     increment value for initial frequency    FixPoint8d24
increment2     increment value for endfrequency         FixPoint8d24
slope          Gain, the sinetone wave to be multiplied FixPoint8d24
step           slew step                                FixPoint8d24
ison           Enabled/Disabled the sweep               FixPoint8d24
============== ======================================== =============

| 
| ===== DSP Parameter Computation ===== increment1= InitialFrequency/(FS/2)
| increment2= EndFrequency/(FS/2)
| slope= Slope\* 2^(SlewStep-23)
| step = 2 ^ (-1\* SlewStep)
| ison = Sweep
| FS, Where fs is frequency and FS is the sampling rate

.. |sweep_lookup.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/sweep_lookup.png
.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/sweeplookupsine008.jpg
