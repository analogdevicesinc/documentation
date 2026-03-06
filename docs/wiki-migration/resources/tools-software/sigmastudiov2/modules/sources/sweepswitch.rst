:doc:`Click here to return to the Sources page </wiki-migration/resources/tools-software/sigmastudiov2/modules/sources>`

Sweep Input with Switch
=======================

| |log_swwep_switch_ssp.png|
| ===== Description =====
| The Sweep block generates a sinewave that sweeps from a start frequency to an end frequency. The sweep rate is determined by the number of sweep steps and cycles per step. In case of the linear sweep, the frequency sweep is linear across time whereas in the case of log sweep input, the frequency sweeps logarithmically cross time. The following variants of the module are available:

-  Linear Sweep Switch
-  Linear Sweep With Switch Tone Burst
-  Log Sweep Switch
-  Log Sweep With Switch Tone Burst

| 
| ===== Usage =====
| Enter the desired start and stop frequency and step size using the edit controls:

-  **Start Freq**

   -  The frequency at which to begin the sweep.

-  **Stop Freq**

   -  The frequency at which to end the sweep.

-  **# Steps**

   -  Determines the number of steps in the sweep.

-  **# Cycles/Step**

   -  Determines the number of the cycles (sine wave cycles) in each step.

-  **On/Off switch**

   -  Starts the sweep

Targets Supported
-----------------

+--------------------------+------------+-----------------------+----------------+------------------+
| Name                     | ADSP-214xx | ADSP-215xx/ADSP-SC5xx | ADAU145x/1456x | ADSP-218xx/SC8xx |
+==========================+============+=======================+================+==================+
| LinearSweep and variants | NA         | NA                    | S              | NA               |
+--------------------------+------------+-----------------------+----------------+------------------+
| LogSweep and variants    | NA         | NA                    | S              | NA               |
+--------------------------+------------+-----------------------+----------------+------------------+

| 
| ===== Pins =====

Output
~~~~~~

======= ===== ================
Name    Type  Description
======= ===== ================
Output0 Audio Output channel 0
======= ===== ================

| 
| ===== Configurable Parameters =====

+--------------------+---------------+------------------------+-----------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range                  | Function Description                                                  |
+====================+===============+========================+=======================================================================+
| StartFrequency     | 20            | 0 to 0.5\* sample rate | Sets the initial frequency for sinetone sweep                         |
+--------------------+---------------+------------------------+-----------------------------------------------------------------------+
| StopFrequency      | 20000         | 0 to 0.5\* sample rate | Sets the final/end frequency for sinetone sweep                       |
+--------------------+---------------+------------------------+-----------------------------------------------------------------------+
| Steps              | 4             | 2 to 48000             | Number of increments in the range defined by start and stop frequency |
+--------------------+---------------+------------------------+-----------------------------------------------------------------------+
| Cycles             | 5             | 1 to 500               | Number of cycles to be rendered of a particular frequency             |
+--------------------+---------------+------------------------+-----------------------------------------------------------------------+
| Enable             | false         | false(off)/true(on)    | Switch on and off the sine sweep                                      |
+--------------------+---------------+------------------------+-----------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+--------------------+---------------------------------------------------+---------------+
| Parameter Name     | Description                                       | ADAU145x/146x |
+====================+===================================================+===============+
| start_freq         | normalised value of start frequency               | FixPoint8d24  |
+--------------------+---------------------------------------------------+---------------+
| stop_freq          | normalised value of end frequency                 | FixPoint8d24  |
+--------------------+---------------------------------------------------+---------------+
| numcycles_per_step | Gain, the sinetone wave to be multiplied          | Integer32     |
+--------------------+---------------------------------------------------+---------------+
| numsteps           | number of steps between start and stop            | Integer32     |
+--------------------+---------------------------------------------------+---------------+
| freq_increment     | frequency increment defined by range and numsteps | FixPoint8d24  |
+--------------------+---------------------------------------------------+---------------+
| ison               | Enabled/Disabled the sweep                        | FixPoint8d24  |
+--------------------+---------------------------------------------------+---------------+

| 
| ===== DSP Parameter Computation ===== start_freq= StartFrequency/(FS/2)
| freq_increment= EndFrequency/(FS/2)
| numsteps= Steps
| numcycles_per_step = Cycles
| freq_increment = (StartFrequency-StopFrequency)/(Steps-1)
| ison = Sweep
| FS, Where fs is frequency and FS is the sampling rate

.. |log_swwep_switch_ssp.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/log_swwep_switch_ssp.png
