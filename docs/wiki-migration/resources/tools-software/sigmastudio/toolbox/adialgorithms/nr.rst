.. warning:: Conversion failed for ``resources/tools-software/sigmastudio/toolbox/adialgorithms/nr``

   Reason: pandoc error: Error at "/tmp/tmpdhunji0c.txt" (line 13, column 1):
expecting inline
not found
===== Parameters and Tuning =====
^

.. code-block:: text

   ====== Noise Reduction (Standard) ======
   [[resources/tools-software/sigmastudio/toolbox/adialgorithms|Click here to return to the ADI Algorithms page]]\\
   \\
   
   This Noise Reduction block is optimized for speech over a communication channel. The most common application is hands-free telephony, but the adaptive filtering is applicable in a wide range of systems. It is often used with Acoustic Echo Cancellation (AEC) to remove noise as well as echoes and reverberation. For applications that require low latency, such as communications in which both a direct acoustic path and an amplified path are present, the Low Latency Noise Reduction block is more suitable.
   
   ===== Implementation of Noise Reduction (Standard) on SigmaDSP =====
   
   The standard Noise Reduction block executes entirely with the block processing domain. A Hamm window is applied with 50% overlap before being processed in the frequency domain. Therefore, the block only appears in the Tree Toolbox when the Block Schematic tab is selected. Since the algorithm is optimized for speech, it runs at the reduced sampling rates standard in telephony. A single block processes samples at 8 kHz ("narrow band" or 4 kHz bandwidth). However, two blocks may be used together with quadrature mirror filters to effectively process 16 kHz audio ("wide band" or 8 kHz bandwidth). The discussion and diagrams below all describe use at 16 kHz sampling rate.
   
   ===== SigmaStudio Blocks =====
   
   ^{{{{:resources:tools-software:sigmastudio:toolbox:adialgorithms:nr:​nr_tree.png?direct|:​resources:​tools-software:​sigmastudio:​toolbox:​adialgorithms:nr:​nr_tree.png ​ | }}  |  {{ {{:resources:tools-software:sigmastudio:toolbox:adialgorithms:nr:nr_block.png?direct|:​resources:​tools-software:​sigmastudio:​toolbox:​adialgorithms:nr:nr_block.png ​ |}}  | \\
   
   ===== Parameters and Tuning =====
   
   Aside from an enable/disable switch, the Noise Reduction block only has one parameter. The smoothing factor adjusts the block-to-block coefficient smoothing of the adaptive filter in the frequency domain. Note that the standard compliance testing was performed with the default parameter (0.2), and there is no guarantee of performance if this parameter is changed. 
   
   ====== Using the Algorithm in a SigmaStudio Project ======
   
   ===== Trial DLLs for Evaluation =====
   
   The noise reduction block is available in a trial version that times out and mutes after 30 minutes. There is a counter on the block in the schematic that counts down the seconds until mute (shown as the full 1800 seconds in the image above). The timer is reset on each-compile-link-download.
   
   The trial versions of the noise reduction block may be downloaded using the Downloadable Add-Ins feature of SigmaStudio version 4.2 and later. Access to the downloads may be found on the Tools menu:
   
   {{ :resources:tools-software:sigmastudio:toolbox:adialgorithms:aec:downloadable_algs_menu_in_ss.png |}}
   \\
   \\
   ===== The Schematic Signal Flow =====
   
   **Decimate to 16 kHz**
   
   As mentioned above, an implementation at 16 kHz sample rate (8 kHz bandwidth) is known as wide band and is currently the most requested bandwidth option. An incoming 48 kHz signal can be downsampled by three to reach 16 kHz either by using a hardware ASRC or an FIR anti-aliasing filter and a decimation block as shown below. The FIR filter coefficients may be found [[resources/tools-software/sigmastudio/toolbox/adialgorithms/AEC/decimate_by_3_FIR_coeffs|here]].
   
   {{ :resources:tools-software:sigmastudio:toolbox:adialgorithms:nr:flow1_decimate_to_16khz.png |}}
   
   
   **Splitting the signal into high and low bands using a QMF**
   
   The basic AEC building block is optimized for an 8 kHz input and can be used directly to implement Narrowband AEC. To implement Wideband AEC, the 16 kHz signal is split into two 8 KHz streams using a quadrature mirror filter (QMF). One stream represents the lower frequencies and the other the higher frequencies. The same filter is applied to the microphone input as shown below. The FIR filter coefficient are linked here for the [[resources/tools-software/sigmastudio/toolbox/adialgorithms/AEC/QMF_FIR_coeffs_low|low band]] and [[resources/tools-software/sigmastudio/toolbox/adialgorithms/AEC/QMF_FIR_coeffs_high|high band]].\\
   
   {{ :resources:tools-software:sigmastudio:toolbox:adialgorithms:nr:flow2_QMF_split_decimate_by_2.png |}}
   
   
   **Pass the signal to the block domain for frequency domain processing**
   
   The three outputs for each of the two frequency bands are then fed into the block processing domain. These correspond to the inputs and outputs on the "Block Schematic" tab, separate from stream processing. \\
   
   {{ :resources:tools-software:sigmastudio:toolbox:adialgorithms:nr:flow3_to_block_domain.png |}}
   
   **In the block domain, pass the signals to the residual, nonlinear processing block**
   
   A synthesis cell applies a Hann window to each block of samples with a 50% overlap. The block is converted to the frequency domain using a real-in, complex-out FFT. These complex spectrum is passed to the RES block for residual nonlinear AEC processing, an inverse FFT is applied, and the signal is reconstructed with 50% overlap-and-add back to the time domain. The three inputs to the RES block are shown in the overview block diagram above. The window coefficients are linked here for the [[resources/tools-software/sigmastudio/toolbox/adialgorithms/AEC/FFT_analysis_window_coeffs|analysis window]] and [[resources/tools-software/sigmastudio/toolbox/adialgorithms/AEC/FFT_synthesis_window_coeffs|synthesis window]].\\
   
   {{ :resources:tools-software:sigmastudio:toolbox:adialgorithms:nr:flow4_NR_block_domain_processing.png |}}
   
   **Reconstruct the 16 kHz signal with a QMF filter**
   
   The process is reversed by upsampling the 8 kHz streams to 16 kHz and recombining the upper and lower frequency bands using the [[resources/tools-software/sigmastudio/toolbox/adialgorithms/AEC/QMF_FIR_coeffs_low|same coefficients as the low band]] of the quadrature mirror filter. \\
   
   {{ :resources:tools-software:sigmastudio:toolbox:adialgorithms:aec:flow7_reconstruct_with_qmf.png |}}
   
   **Interpolate by 3 to return the signal to 48 kHz for further processing and output**
   
   The 16 kHz signal is then resampled, using [[resources/tools-software/sigmastudio/toolbox/adialgorithms/AEC/interpolate_by_3_FIR_coeffs|these]] anti-aliasing FIR filter coefficients, to 48 kHz for optional further processing and output to DACs.\\
   
   {{ :resources:tools-software:sigmastudio:toolbox:adialgorithms:aec:flow6_interpolate_by_3.png |}}
   
   ===== Plug-In User Guide =====
   
   {{ :resources:tools-software:sigmastudio:toolbox:adialgorithms:nr:sigma300_nr_plug-in_for_sigmastudio_user_guide.pdf |}}
   
   ===== Licensing =====
   
   ADI charges a licensing fee per end product shipped. If more than one AEC block runs on a single DSP or there are multiple SigmaDSP processors per system, the fee is only incurred once. Please contact [[SigmaStudioLicensing@analog.com|SigmaStudioLicensing]] for licensing information.
