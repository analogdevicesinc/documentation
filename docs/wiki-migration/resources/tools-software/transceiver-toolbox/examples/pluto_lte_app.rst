LTE eNB Transmitter Conformance Tests Using ADALM-PLUTO
=======================================================

This article describes the MATLAB app that ADI has developed in order to run LTE's eNodeB Test Model waveforms using ADALM-Pluto. Using this app, users connect the transmit and receive ports of their PlutoSDR using a cable and verify that the error vector magnitude (EVM) of the AD9363 transceiver inside their Pluto SDR conforms to the specifications listed in the datasheet. Users can view the EVM corresponding to the channels present in the LTE downlink resource grid over time, frequency and resource grid also. In order to run the code that builds this app, users would need:

-  `MATLAB <https://www.mathworks.com/products/matlab>`_
-  `Communications Toolbox <https://www.mathworks.com/products/communications/>`_
-  `DSP System Toolbox <https://www.mathworks.com/products/dsp-system/>`_
-  `Signal Processing Toolbox <https://www.mathworks.com/products/signal/>`_
-   `LTE Toolbox <https://www.mathworks.com/products/lte/>`_
-  `Communications Toolbox Support Package for ADALM-Pluto <https://www.mathworks.com/hardware-support/adalm-pluto-radio.html>`_

The GitHub repository that contains the code can be found `here <https://github.com/TransceiverToolbox?/pluto_lte_app/trx_examples/streaming/LTE_PA_App>`_. Alternatively, a standalone version of the app can be installed using the executable provided. Users need to be connected to the internet when installing the app using this executable since MATLAB Runtime which enables the execution of compiled MATLAB applications needs to be installed also. In both cases, users would need:

-  an ADALM-Pluto
-  a loopback cable with SMA male ports on both ends

Available versions of the app:

-  :git-TransceiverToolbox:`Standalone Compiled App (Release 20.1.1+) <releases>`
-  `MATLAB Source <https://github.com/TransceiverToolbox?/pluto_lte_app/trx_examples/streaming/LTE_PA_App>`_

During the application installation, the "Next" button shows up a few times. When you click it, it does not grey out and become non-sensitive. It is still active, and you may be tempted to click it again. Doing so will shoot off multiple (conflicting) processes that all eventually try to write to the same temporarily directory on your machine, eventually causing random failures, either during the installation, or during the first time you run the application. Instead, we suggest that you click "Next" once, and only once to avoid any issues, both during installation and during runtime.

A screenshot of the app in action is shown below. To run the app, users connect a PlutoSDR to their host computer and select the constellation of PDSCH (LTE's physical channel that carries user data), bandwidth, and channel indicated by the LO (MHz) field in the top left panel of the app. Test models are standardized tests defined within `3GPP LTE specifications <https://www.etsi.org/deliver/etsi_ts/136100_136199/136141/10.01.00_60/ts_136141v100100p.pdf>`_ commonly used for hardware performance testing. Currently, TMN numbers 3.1, 3.1a, 3.1b, 3.2 and 3.3 for 5, 10, 15 and 20 MHz bandwidths are supported. If you want to use other test models these can be easily added using the built-in functions in `LTE Toolbox <https://www.mathworks.com/products/lte/>`_ from MathWorks.

Then, upon pressing the play button, the app will establish communication with the PlutoSDR connected to the host computer. If a PlutoSDR is not connected, the app would simply terminate and indicate to the user that a PlutoSDR was not found in the message field above the spectrum plot. Otherwise, a frame is repeatedly transmitted over the transmit port and demodulated from the waveform received at the receive port. For each trial, the same frame is demodulated and the corresponding EVM is displayed. As shown in the screenshot, EVM corresponding to various LTE PHY signals are computed and displayed in the table on the left. Similarly, EVM as a function of the OFDM symbol index, the OFDM subcarrier index and the resource block index corresponding to the TM Number chosen are also displayed. Additionally, the waveform spectrum plot of the entire frame and the constellation plot are also shown.


|image1|

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/transceiver-toolbox/examples/lte_app.png
