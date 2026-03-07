Probe and Stimulus Blocks
=========================

:doc:`Click here to return to the Tutorials page </wiki-migration/resources/tools-software/sigmastudio/tutorials>`

| Complete the first tutorial in order for an explanation of the input, output, and EQ blocks that are used in this tutorial.
| Its purpose is to show you how to use probe and stimulus blocks to monitor the frequency response of the filters you set.

-  Insert an Input from the IO tab of the ToolBox.
-  Click the System tab and drag two Stimuliblock blocks to the workspace.
-  Connect wires from the input channels to the Stimuliblock block.
-  Insert two Medium Size Eq blocks from the Filters tab.
-  For each EQ block, right-click and select Add Algorithm > IC 1 > Single - Double Precision.
-  Right-click each again and select Grow Algorithm > 1. Single - Double Precision > 2.
-  Connect wires from the output of the Stimuliblock block to the input of the EQ block. Your workspace should look like this:\\\\\

|probestim1.png|

   \* Click the System tab and drag one Probeblock block into your workspace.
-  Right-click the block and select Add Pins.
-  Connect wires from the output of the EQ to the input of the Probeblock.
-  Click the IO tab and drag two Output blocks into the workspace.
-  Connect wires from the output of the probes to the input of the Output block. Your workspace should look like this:\\\\\

|probestim2.png|

   \* Compile the project: Click Link Compile Download on the toolbar or select Action, Link Compile Download.
-  Click the Probe block to bring up the Simulated Frequency Response window. There will be nothing displayed.
-  Click the Stimulus block buttons to bring up the Frequency Response window. You can now view in real time any changes you make to the EQ. The response for the above parameters is shown here:

| \\\\\ |probestim3.png|
|

.. important::

   The stimulus/probe cells only work with linear, time-domain processing blocks. The Probe will not work if a transform (for example, the Hilbert transform) is placed between it and the Stimulus.


.. important::

   Examples of valid and invalid block combinations for Stimulus/Probe are on this page: :ez:`dsp/sigmadsp/w/documents/14469/stimulus-probe-capability-and-limitations`


.. |probestim1.png| image:: https://wiki.analog.com/_media/probestim1.png
.. |probestim2.png| image:: https://wiki.analog.com/_media/probestim2.png
.. |probestim3.png| image:: https://wiki.analog.com/_media/probestim3.png
