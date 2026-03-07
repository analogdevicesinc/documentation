Voltage Controlled Delay
========================

| :doc:`Click here to return to the Basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| ----------------------------------------------------------------------------------------------------------

|voltagecontrolledpic1.png| The Voltage Controlled Delay block adds a variable amount of sample delay to the input signal. Unlike the Delay block which adds a fixed amount designated in the control, the VCD allows for a data input to control the amount of delay that is applied to the input signal.

The 1st input pin (green) is the audio input signal. The 2nd input pin (red) is the first delay "tap" to the input signal. The output pin (blue) is the delayed output signal corresponding to the first delay tap. This algorithm can be grown to support multiple input-tap/output pairs. Thus the same input signal can be delayed by various different data control taps.

The **Max** setting still corresponds to the maximum amount of delay that is reserved for the input signal. Thus any delay values designated by the data control pin, must be between 0 samples and the value in the **Max** drop-down. There is more detailed information about the data memory reserved by the **Max** drop-down in the last section below.

Voltage Control Delay Example
-----------------------------

| |voltagecontrolledpic2.png|
| In the example above, the VCD algorithm is grown in order to support 2 separate delay taps to the input signal. The first output pin of the VCD is connected to channel 0 - Output1. Output1 is receiving a delayed version of the input signal by 480 samples. This is a fixed amount of delay designated by the DC input block which has the value 480 in integer format (28.0).

The second output pin of the VCD is connected to channel 1 - Output2. Output2 is receiving a variable delayed version of the input signal. This is accomplished by using a low-frequency oscillator (LFO). The rate of the LFO (0.1Hz) determines how quickly the sweep of delay will be using a :doc:`Sine tone </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources/sinetone>` generator. The max delay amount of the sweep is determined by the other supporting blocks: :doc:`DC input </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources/dcinputentry>`, :doc:`Linear Gain </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp/lineargain>`, :doc:`Adder </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp/signaladd>`, :doc:`Multiply </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp/multiply>` etc. In this example the sample delay will vary from 0 to 480 samples with a rate of 0.1Hz. If you follow the signal flow you will see how this is accomplished: 48000*[0.005 \*(sin(x) + 1)]. Thus the minimum output value sent to the tap input of the VCD is 0 and the maximum delay in samples is equal to 480 samples: 48000\*.005 + 48000\*.005. Thus, the value in the linear gain block denotes the max delay in seconds divided by 2 and the last DC block leading to the multiplication block represents the sample rate of the schematic.

The maximum delay available for a particular delay block depends on the total available system data RAM, which is specified in the DSP processor data sheet. Setting the **Max** control's value, allocates memory on the DSP, reserving that memory for use by this particular block only, and reducing the available memory for all other delay blocks in the design. This is a compiler directive and modifies the assembly code, so any time you change the Max setting you must recompile and download the program. The maximum delay value range is limited to the remaining unallocated memory of the RAM.

.. |voltagecontrolledpic1.png| image:: https://wiki.analog.com/_media/voltagecontrolledpic1.png
.. |voltagecontrolledpic2.png| image:: https://wiki.analog.com/_media/voltagecontrolledpic2.png
