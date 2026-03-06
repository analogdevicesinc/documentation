Analysis Window
===============

The Analysis Window is used for making measurements using a physical hardware. An AD4130-8 Evaluation board is needed to capture data. Data is captured by clicking on 'Run Once' or 'Run Continuously'.

| The **Histogram** or **Waveform** sections (3) display the results of the noise analysis or the waveform for the selected analysis channel, including both noise and resolution measurements.
| |screenshot_2021-04-09_122534.png|

-  The data graph (1) shows each successive sample of the ADC output. Zoom in on the data in the graphusing the scroll wheel on your mouse or by selecting the magnifying glass.
-  The **Result** section (2) shows the analysis of the channel selected.
-  The **Samples** numeric control sets the number of samples gathered per batch. This control is unrelated to the ADC mode. You can capture a defined sample set or continuously gather batches of samples. In both cases, the number of samples set in the **Samples**\ (4) numeric input dictates the number of samples.
-  Click the Run Once button (2) to start gathering ADC results. Click the **Run Continuously** button (2) to start gathering ADC results continuously. Results appear in the waveform graph (1).
-  Click the **Codes** drop-down menu (5) to select whether the data graph displays in units of voltages or codes. This control affects both the waveform graph and the histogram graph. The axis controls is fixed. When selecting **Fixed**, the axis ranges can be programmed; however, these ranges do not automatically adjust after each batch of samples.

.. |screenshot_2021-04-09_122534.png| image:: https://wiki.analog.com/_media/resources/eval-ad4130/screenshot_2021-04-09_122534.png
