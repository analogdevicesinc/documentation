Noise Reduction (Standard)
==========================

:doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms>`

This Noise Reduction block is optimized for speech over a communication channel. The most common application is hands-free telephony, but the adaptive filtering is applicable in a wide range of systems. It is often used with Acoustic Echo Cancellation (AEC) to remove noise as well as echoes and reverberation. For applications that require low latency, such as communications in which both a direct acoustic path and an amplified path are present, the Low Latency Noise Reduction block is more suitable.

Implementation of Noise Reduction (Standard) on SigmaDSP
--------------------------------------------------------

The standard Noise Reduction block executes entirely with the block processing domain. A Hamm window is applied with 50% overlap before being processed in the frequency domain. Therefore, the block only appears in the Tree Toolbox when the Block Schematic tab is selected. Since the algorithm is optimized for speech, it runs at the reduced sampling rates standard in telephony. A single block processes samples at 8 kHz ("narrow band" or 4 kHz bandwidth). However, two blocks may be used together with quadrature mirror filters to effectively process 16 kHz audio ("wide band" or 8 kHz bandwidth). The discussion and diagrams below all describe use at 16 kHz sampling rate.

SigmaStudio Blocks
------------------

+---+---+---+
| |:resources:tools-software:sigmastudio:toolbox:adialgorithms:nr:nr_tree.png \|| | |:resources:tools-software:sigmastudio:toolbox:adialgorithms:nr:nr_block.png \|| |   |
+===+===+===+
+---+---+---+

Parameters and Tuning
---------------------

Aside from an enable/disable switch, the Noise Reduction block only has one parameter. The smoothing factor adjusts the block-to-block coefficient smoothing of the adaptive filter in the frequency domain. Note that the standard compliance testing was performed with the default parameter (0.2), and there is no guarantee of performance if this parameter is changed.

Using the Algorithm in a SigmaStudio Project
============================================

Trial DLLs for Evaluation
-------------------------

The noise reduction block is available in a trial version that times out and mutes after 30 minutes. There is a counter on the block in the schematic that counts down the seconds until mute (shown as the full 1800 seconds in the image above). The timer is reset on each-compile-link-download.

The trial versions of the noise reduction block may be downloaded using the Downloadable Add-Ins feature of SigmaStudio version 4.2 and later. Access to the downloads may be found on the Tools menu:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/adialgorithms/aec/downloadable_algs_menu_in_ss.png
   :align: center

The Schematic Signal Flow
-------------------------

**Decimate to 16 kHz**

As mentioned above, an implementation at 16 kHz sample rate (8 kHz bandwidth) is known as wide band and is currently the most requested bandwidth option. An incoming 48 kHz signal can be downsampled by three to reach 16 kHz either by using a hardware ASRC or an FIR anti-aliasing filter and a decimation block as shown below. The FIR filter coefficients may be found :doc:`here </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms/aec/decimate_by_3_fir_coeffs>`.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/adialgorithms/nr/flow1_decimate_to_16khz.png
   :align: center

**Splitting the signal into high and low bands using a QMF**

The basic AEC building block is optimized for an 8 kHz input and can be used directly to implement Narrowband AEC. To implement Wideband AEC, the 16 kHz signal is split into two 8 KHz streams using a quadrature mirror filter (QMF). One stream represents the lower frequencies and the other the higher frequencies. The same filter is applied to the microphone input as shown below. The FIR filter coefficient are linked here for the :doc:`low band </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms/aec/qmf_fir_coeffs_low>` and :doc:`high band </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms/aec/qmf_fir_coeffs_high>`.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/adialgorithms/nr/flow2_QMF_split_decimate_by_2.png
   :align: center

**Pass the signal to the block domain for frequency domain processing**

The three outputs for each of the two frequency bands are then fed into the block processing domain. These correspond to the inputs and outputs on the "Block Schematic" tab, separate from stream processing.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/adialgorithms/nr/flow3_to_block_domain.png
   :align: center

**In the block domain, pass the signals to the residual, nonlinear processing block**

A synthesis cell applies a Hann window to each block of samples with a 50% overlap. The block is converted to the frequency domain using a real-in, complex-out FFT. These complex spectrum is passed to the RES block for residual nonlinear AEC processing, an inverse FFT is applied, and the signal is reconstructed with 50% overlap-and-add back to the time domain. The three inputs to the RES block are shown in the overview block diagram above. The window coefficients are linked here for the :doc:`analysis window </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms/aec/fft_analysis_window_coeffs>` and :doc:`synthesis window </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms/aec/fft_synthesis_window_coeffs>`.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/adialgorithms/nr/flow4_NR_block_domain_processing.png
   :align: center

**Reconstruct the 16 kHz signal with a QMF filter**

The process is reversed by upsampling the 8 kHz streams to 16 kHz and recombining the upper and lower frequency bands using the :doc:`same coefficients as the low band </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms/aec/qmf_fir_coeffs_low>` of the quadrature mirror filter.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/adialgorithms/aec/flow7_reconstruct_with_qmf.png
   :align: center

**Interpolate by 3 to return the signal to 48 kHz for further processing and output**

The 16 kHz signal is then resampled, using :doc:`these </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms/aec/interpolate_by_3_fir_coeffs>` anti-aliasing FIR filter coefficients, to 48 kHz for optional further processing and output to DACs.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/adialgorithms/aec/flow6_interpolate_by_3.png
   :align: center

Plug-In User Guide
------------------

`sigma300_nr_plug-in_for_sigmastudio_user_guide.pdf <https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/adialgorithms/nr/sigma300_nr_plug-in_for_sigmastudio_user_guide.pdf>`_

Licensing
---------

ADI charges a licensing fee per end product shipped. If more than one AEC block runs on a single DSP or there are multiple SigmaDSP processors per system, the fee is only incurred once. Please contact `SigmaStudioLicensing <https://wiki.analog.com/sigmastudiolicensing@analog.com>`_ for licensing information.

.. |:resources:tools-software:sigmastudio:toolbox:adialgorithms:nr:nr_tree.png \|| image:: /{{/resources/tools-software/sigmastudio/toolbox/adialgorithms/nr/nr_tree.png
.. |:resources:tools-software:sigmastudio:toolbox:adialgorithms:nr:nr_block.png \|| image:: /{{/resources/tools-software/sigmastudio/toolbox/adialgorithms/nr/nr_block.png
