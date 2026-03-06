Osc Spectrum Analyzer Plugin
============================

This Spectrum Analyzer plugin works with the `iio_oscilloscope <https://wiki.analog.com/iio_oscilloscope>`__. You use the latest version if possible.

The plugin is made available by IIO Oscilloscope only when one of the following boards is detected:

-  :doc:`ad-fmcomms2-ebz </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz>`
-  :doc:`ad-fmcomms3-ebz </wiki-migration/resources/eval/user-guides/ad-fmcomms3-ebz>`
-  :doc:`ad-fmcomms4-ebz </wiki-migration/resources/eval/user-guides/ad-fmcomms4-ebz>`

The AD-FMComms3-EBZ is more targeted for wider tuning ranges than the other boards enumerated above which make it the best candidate to be used with this plugin.

Description
-----------

The "`Spectrum analyzer <https://en.wikipedia.org/wiki/Spectrum analyzer>`__" measures the magnitude of an input signal versus frequency within the full frequency range of the instrument (in this case the PCB). For the AD-FMCOMMS3-EBZ that is 70 MHz - 6000 MHz (the limits of the AD9361).

This is not meant to be the worlds best spectrum analyzer, but an example of how to use the fast lock feature of the AD9361, with a small contrived example (which is multi-threaded, so it does actually get adequate performance).

The overall method uses is known as a Hybrid SuperHeterodyne-FFT. The technique used is to combine sweeping the LO and using FFT analysis on the captured signals for consideration of wide and narrow spans. This technique typically allows for faster sweep time.

One benefit of digitizing the intermediate frequency is the ability to use digital filters, which have a range of advantages over analog filters such as near perfect shape factors and improved filter settling time. Also, for consideration of narrow spans, the FFT can be used to increase sweep time without distorting the displayed spectrum.

Issues
~~~~~~

-  Minimum signal detection time - This is related to the sampling rate of the converter and the FFT rate. Since we are doing FFTs in software, they are pretty slow (relatively). Since the LO is sweeping, if the frequency of interest is hopping, it needs to remain at one place for some duration, so it can be captured and displayed.
-  Blind time: On traditional spectrum analyzers, they are able to sample the incoming RF spectrum in the time domain and convert the information to the frequency domain using the FFT process. Since we capture, and then convert, we do have times we are not capturing - and we can miss information.
-  DC correction: The AD9361 will remove signals which are exactly at the LO frequency - so you may miss something if it is very narrow band, at the LO. This is normally solved by shifting the LO a tiny bit (few Hz) on different sweeps.

Spectrum Analyzer Controls
--------------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/spectrum_analyzer_plugin.png
   :align: right
   :width: 320px

-  **Center Frequency (MHz):** The frequency halfway between the stop and start frequencies to be displayed on the spectrum analyzer.
-  **Span (MHz):** The range between the start and the stop frequencies.
-  **RBW (KHz):** The resolution bandwidth.
-  **Start Sweep:** The frequency analysis start button.
-  **Stop Sweep:** The frequency analysis stop button.
-  **Receiver:** Selects which AD9361 Rx channel to be used for data capture (1 or 2)

Software Implementation Architecture
------------------------------------

To try to minimize blind time, we wrote a multi-threaded application, which spawns a few different threads to capture and process the FFT data, to try to do as much in parallel as possible. While data is being processed (FFT), we are changing the LO for the next capture.

Initial conditions:

-  Mutex **FFT** is set in order to prevent a deadlock at startup between the Capture Thread waiting for Mutex **FFT** and FFT Thread waiting for Mutex **Demux**.

Threads layout:

<graphviz dot> digraph { "Main Application" -> "Load initial Profiles" -> "Set Mutex FFT" -> "Start Threads" -> "GTK Update / Drawing" -> "repeat" -> "GTK Update / Drawing"; "Manage Profiles Thread" -> "Wait for Mutex New data" -> "recall profile 'n'\\nin AD9361" -> "Set Mutex Recall" -> "load profile\\n 'n + 1' over SPI" -> "Wait for Mutex New data" [color = red]; "Capture Thread" -> "Capture new Data \\n (profile n-1 in use)" -> "Set Mutex New Data" -> "Wait for Mutex FFT" -> "Demux Data" -> "Set Mutex Demux" -> "Wait Mutex Recall" -> "Capture new Data \\n (profile n-1 in use)" [color = green]; "FFT Thread" -> "Wait for Mutex Demux" -> FFT -> "Stitch to results" -> "Set Mutex FFT " -> "Wait for Mutex Demux" [damping = 2, color = blue];

"Set Mutex Demux" -> "Wait for Mutex Demux" [constraint=false, style = dashed]; "Set Mutex FFT " -> "Wait for Mutex FFT" [constraint=false, style = dashed]; "Set Mutex New Data" -> "Wait for Mutex New data" [constraint=false, style = dashed]; "Set Mutex Recall" -> "Wait Mutex Recall" [constraint=false, style = dashed];

} </graphviz>

Help
====

If you have questions, please ask on :ez:`EngineerZone <community/linux-device-drivers/linux-software-drivers>`.
