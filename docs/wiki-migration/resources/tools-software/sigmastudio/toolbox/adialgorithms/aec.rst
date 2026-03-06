.. warning:: Conversion failed for ``resources/tools-software/sigmastudio/toolbox/adialgorithms/aec``

   Reason: pandoc error: Error at "/tmp/tmpahxewtey.txt" (line 34, column 1):
expecting inline
not found

^

.. code-block:: text

   ====== Acoustic Echo Cancellation ======
   [[resources/tools-software/sigmastudio/toolbox/adialgorithms|Click here to return to the ADI Algorithms page]]\\
   \\
   
   The Acoustic Echo Cancellation (AEC) block is designed to remove echoes, reverberation, and unwanted added sounds from a signal that passes through an acoustic space. As shown in the diagram below, the sound coming from the remote person speaking, known as the Far End In, is sent in parallel to a DSP path and to an acoustic path. The acoustic path consists of an amplifier/loudspeaker, an acoustic environment, and a microphone returning the signal to the DSP. The AEC block is based on an adaptive FIR filter. The algorithm continuously adapts this filter to model the acoustic path. The output of the filter is then subtracted from the acoustic path signal to produce a "clean" signal output with the linear portion of acoustic echoes largely removed. The AEC block also calculates a residual signal containing nonlinear acoustic artifacts. This signal is sent to a Residual Echo Cancellation block (RES) that further recovers the input signal. The signal is then (optionally) passed through a noise reduction function to produce the output, which is a known as the "Far End Out."
   
   The filter pauses adaptation when it detects sounds in the acoustic path unrelated to the far end in. This allows sounds in to be added to the far end out. For example, in the case of a hands-free system or speakerphone, adaptation pauses when a person speaks directly into the microphone. The person at the far end hears only the local talker and not the echoes and reverberation from the far end in the near end space. This is absolutely necessary for clear, full duplex conversation over communication channel.
   
   The adaptive filter in the AEC block will remove any signal that is part of the far end in. This can be extremely useful. For example, if music that is playing in the near end space, it may be added to the far end input signal. The music will be cancelled by the adaptive filter along with the signal coming from the far end. This allows full duplex conversation while music (or any known signal) is playing in the near end space. Continuing the example above, if a driver is listening to music while talking on the hand-free, the music does not need to be paused during the conversation. Both the voice of the remote speaker and the music will be removed from the signal picked up by the microphone, and only the local speaker's voice will be sent on the far end out.
   
   There are two blocks that, together, comprise the Acoustic Echo Cancellation algorithm as implemented on the SigmaDSP. The primary block (AEC) removes the linear portion of the echoes and reverberation. operates in the stream processing domain and performs most of the functionality. A second block (RES) runs in the frequency domain and supplements the primary AEC block by performing nonlinear processing on the residual echo signal. The residual echo removal improves the performance substantially, and all performance benchmarks have been made using the two blocks together. However, the RES block is, strictly speaking, optional.
   
   An additional block, noise reduction, is also shown in the diagram below. While not formally part of the AEC algorithm, they are used together more often than not. The noise reduction block also operates in the frequency domain and can follow the residual echo suppression in the block/frequency domain space with no additional overhead. The noise reduction block has use in many applications, however, that do not requires AEC.
   
   {{ :resources:tools-software:sigmastudio:toolbox:adialgorithms:aec:aec_block_diagram.png?600 |}}
   
   Most AEC implementations, including this one, are optimized for speech. As such, the bandwidth is reduced to minimize processing resources. There are three widely accepted bandwidth standards: Narrow band (NB) uses a sampling rate of 8 kHz (bandwidth of 4 kHz). This is the bandwidth historically used in telephony (PSTN). Wide band (WB) uses a sampling rate of 16 kHz (8 kHz bandwidth). This is the most commonly used implementation for new products, and is the implementation documented below. The base implementation of SigmaDSP is narrow band. However, a wide band implementation can be constructed using two narrow band blocks, one for the lower frequencies and one for the upper frequencies. The documentation and example projects are all wide band and are implemented in this way. Ultra-wide band (UWB) uses a sampling rate of 32 kHz (16 kHz bandwidth). UWB AEC is not often used in speech applications
   
   ===== When Acoustic Echo Cancellation is Required =====
   
   AEC is needed when a far end signal (voice originating at the other end of a line of communication) is played over a loudspeaker into a reverberant acoustic space and is picked up by a microphone. If the AEC algorithm were not implemented, an echo corresponding to the delay for the sound to travel from the speaker to the microphone, as well as any reverberation, would be returned to the far end. In addition to sounding unnatural and being unpleasant to listen to, the artifacts substantially reduce speech intelligibility. The block diagram shows the algorithm cancelling the output of only one speaker being picked up by one microphone. An instantiation of this full signal path must be repeated for every microphone in the system. However, there are ways of cancelling the output of multiple speakers that are each playing a different signal. This requires that the spatial relationship between the loudspeakers and microphone be fixed and measured as an impulse response. Some variation in the impulse response, such as that caused by absorption and reflections created by people in the space, will be cancelled by the adaptive filter. This type of configuration must be designed and tuned as a system customized to a known environment as part of final tuning.
   
   The most common application for acoustic echo cancellation is full duplex communication in a telephony system such as a hand-free system in a car or a speakerphone. However, AEC is required in a wide variety of applications beyond these, such as automotive emergency eCall systems, voice UI preprocessing, intercoms, hands free communication for bedridden hospital or home care patients, etc. Also increasingly common use is "active" auditoriums, lecture halls, and conference rooms. These use fixed microphones that cover an area of the room rather than using close-up microphones for each person that might speak. This ensures that everyone in the room can hear the person speaking, and also allows microphones over an audience to be easily be opened for questions without passing a microphone around. Such as system is less disruptive and makes recording the meeting simple. Similarly, in-car communication systems that enable enhanced communications between passenger reply on AEC.
   
   ===== Standards Compliance and Testing =====
   
   The AEC-RES algorithm is compliant with the highest performance telecommunication standards tests, Skype for Business. This is a more stringent standard than most ITU standards, so the implementation is pre-qualified for many applications. One notable exception is emergency automotive eCall systems such as those mandated in Europe and the Russian Federation (Glonass). ADI are in the process of qualifying and collecting data for these applications, as well. All measurements are made in ADI's acoustics lab using the international industry standard hardware and ACQUA software from HEAD Acoustics of Germany. For more details on these tests, copies of the data, information on interpreting the results and additional test requests, please contact [[SigmaStudioLicensing@analog.com|SigmaStudioLicensing]]. 
   
   ====== Implementation of AEC on SigmaDSP ======
   
   ===== SigmaStudio Blocks =====
   
   As stated above, the implementation consist of two blocks. The primary AEC adaptive filter block operates in the stream domain, and is a narrow band implementation. A wide band implementation can be constructed by using two of these blocks and is illustrated below. The second block operates in the frequency domain and performs additional processing on the nonlinear residual (RES). Three signals are passed to the second block in the algorithm: (1) the output of the AEC block minus the signal from the microphone, (2) the FIR filter output from the AEC block before the subtraction of the microphone input, and (3) the direct signal from the microphone.
   
   ^{{:resources:tools-software:sigmastudio:toolbox:adialgorithms:aec:aec_nb_tree.png  | }}|  {{ :resources:tools-software:sigmastudio:toolbox:adialgorithms:aec:aec_block.png  |}}  | \\
   ^{{:resources:tools-software:sigmastudio:toolbox:adialgorithms:aec:res_tree.png  | }}  |  {{ :resources:tools-software:sigmastudio:toolbox:adialgorithms:aec:res_block.png  |}}  | \\
   
   
   ===== Parameters and Tuning =====
   
   The primary AEC block has two user parameters. The first is the length of the adaptive FIR filter. The default length of the filter is 640 taps. The second is a high pass filter set by default to 150 Hz. The entire block and the high pass filter each have enable/disable switches.
   
   **AEC Filter Length (Taps)**
   
   At the heart of the AEC block is an adaptive FIR filter. This parameter sets the number of FIR filter taps. The filter can be thought of as a representation of the impulse response of the acoustic path from the loudspeaker to the microphone as well as the reverberation and echoes to be cancelled. The length of this filter is related to the length of this impulse response and the duration for which the block can effectively cancel echoes. The default is 640 taps. At the sampling rate of 16 kHz, this corresponds to approximately 40 ms or 13.8 m of sound travel. Note that the standard compliance testing was performed with the default parameter, and there is no guarantee of performance if this parameter is changed.
   
   **AEC High Pass Filter (HPF)**
   
   The high pass filter, set by default to 150 Hz, removes rumble noise and other sounds below the frequency range of speech. The corner frequency of this filter may be adjusted to suit the environment of the application. Note that the standard compliance testing was performed with the default parameter, and there is no guarantee of performance if this parameter is changed.
   
   **RES Temporal Smoothing**
   
   Each bin in the frequency domain analysis is averaged over time to eliminate large jumps in the response. This parameter controls the time constant of the band-wise smoothing. Note that the standard compliance testing was performed with the default parameter of 0.2739, and there is no guarantee of performance if this parameter is changed.
   
   **RES Spectral Smoothing**
   
   In addition to frequency domain, bin-wise smoothing over time, the spectral response within a given block is smoothed to eliminate sharp resonances and notches. This parameter controls this amount of smoothing. Note that the standard compliance testing was performed with the default parameter of 0.2, and there is no guarantee of performance if this parameter is changed.
   
   **RES Smoothing Factor**
   
   The smoothing factor adjusts the amount of smoothing that is applied when processing the residual, nonlinear portion of the acoustic echoes and reverberation. Note that the standard compliance testing was performed with the default parameter of 0.7, and there is no guarantee of performance if this parameter is changed.
   
   
   ====== Using the Algorithm in a SigmaStudio Project ======
   
   ===== Trial DLLs for Evaluation =====
   
   The AEC blocks are available in trial versions that time out and mute after 30 minutes. There is a counter on each of the block in the schematic that counts down the seconds until mute (shown as the full 1800 seconds in the image above). The timer is reset on each-compile-link-download.
   
   The trial versions of the AEC and RES blocks may be downloaded using the Downloadable Add-Ins feature of SigmaStudio version 4.2 and later. Access to the downloads may be found on the Tools menu:
   
   {{ :resources:tools-software:sigmastudio:toolbox:adialgorithms:aec:downloadable_algs_menu_in_ss.png |}}
   \\
   \\
   
   ===== Example Code =====
   
   Example projects of the signal flow may be found [[/resources/tools-software/sigmastudio/tutorials/aecnrexamples|here]].
   
   ===== The Schematic Signal Flow =====
   
   **Decimate to 16 kHz**
   
   As mentioned above, an implementation at 16 kHz sample rate (8 kHz bandwidth) is known as wide band AEC and is currently the most requested bandwidth option. An incoming 48 kHz signal can be downsampled by three to reach 16 kHz either by using a hardware ASRC or an FIR anti-aliasing filter and a decimation block as shown below. The FIR filter coefficients may be found [[resources/tools-software/sigmastudio/toolbox/adialgorithms/AEC/decimate_by_3_FIR_coeffs|here]].
   
   {{ :resources:tools-software:sigmastudio:toolbox:adialgorithms:aec:flow1_decimate_to_16khz.png |}}
   
   **Splitting the signal into high and low bands using a QMF**
   
   The basic AEC building block is optimized for an 8 kHz input and can be used directly to implement Narrowband AEC. To implement Wideband AEC, the 16 kHz signal is split into two 8 KHz streams using a quadrature mirror filter (QMF). One stream represents the lower frequencies and the other the higher frequencies. The same filter is applied to the microphone input as shown below. The FIR filter coefficient are linked here for the [[resources/tools-software/sigmastudio/toolbox/adialgorithms/AEC/QMF_FIR_coeffs_low|low band]] and [[resources/tools-software/sigmastudio/toolbox/adialgorithms/AEC/QMF_FIR_coeffs_high|high band]].\\
   
   {{ :resources:tools-software:sigmastudio:toolbox:adialgorithms:aec:flow2_splitting_the_signal_qmf.png |}}
   
   **Pass the high and low bands through separate AEC blocks**
   
   The low and high frequency bands at 8 kHz are sent to separate AEC blocks. A DC blocking filter is added for the low band, In addition to the processed far end out signal, the microphone signal is passed through, along with the direct output of the adaptive FIR filter (before the mic signal is subtracted. This FIR filter output is used by the RES block for additional processing on the nonlinear residual echoes by the RES block in the frequency domain. \\
   
   {{ :resources:tools-software:sigmastudio:toolbox:adialgorithms:aec:flow3_pass_to_aec_blocks.png |}}
   
   **Pass the output of the AEC block to the block domain for residual, nonlinear, frequency domain processing**
   
   The three outputs for each of the two frequency bands are then fed into the block processing domain. These correspond to the inputs and outputs on the "Block Schematic" tab, separate from stream processing. \\
   
   {{ :resources:tools-software:sigmastudio:toolbox:adialgorithms:aec:flow4_to_freq_domain.png |}}
   
   **In the block domain, pass the signals to the residual, nonlinear processing block**
   
   A synthesis cell applies a Hann window to each block of samples with a 50% overlap. The block is converted to the frequency domain using a real-in, complex-out FFT. These complex spectrum is passed to the RES block for residual nonlinear AEC processing, an inverse FFT is applied, and the signal is reconstructed with 50% overlap-and-add back to the time domain. The three inputs to the RES block are shown in the overview block diagram above. The window coefficients are linked here for the [[resources/tools-software/sigmastudio/toolbox/adialgorithms/AEC/FFT_analysis_window_coeffs|analysis window]] and [[resources/tools-software/sigmastudio/toolbox/adialgorithms/AEC/FFT_synthesis_window_coeffs|synthesis window]].\\
   
   {{ :resources:tools-software:sigmastudio:toolbox:adialgorithms:aec:flow5_to_res.png |}}
   
   **Reconstruct the 16 kHz signal with a QMF filter**
   
   The process is reversed by upsampling the 8 kHz streams to 16 kHz and recombining the upper and lower frequency bands using the [[resources/tools-software/sigmastudio/toolbox/adialgorithms/AEC/QMF_FIR_coeffs_low|same coefficients as the low band]] of the quadrature mirror filter. \\
   
   {{ :resources:tools-software:sigmastudio:toolbox:adialgorithms:aec:flow7_reconstruct_with_qmf.png |}}
   
   **Interpolate by 3 to return the signal to 48 kHz for further processing and output**
   
   The 16 kHz signal is then resampled, using [[resources/tools-software/sigmastudio/toolbox/adialgorithms/AEC/interpolate_by_3_FIR_coeffs|these]] anti-aliasing FIR filter coefficients, to 48 kHz for optional further processing and output to DACs.\\
   
   {{ :resources:tools-software:sigmastudio:toolbox:adialgorithms:aec:flow6_interpolate_by_3.png |}}
   
   
   ====== Plug-In User Guides ======
   
   {{ :resources:tools-software:sigmastudio:toolbox:adialgorithms:aec:aec_plug-in_for_sigmastudio_user_guide.pdf |}}
   
   {{ :resources:tools-software:sigmastudio:toolbox:adialgorithms:aec:res_plug-in_for_sigmastudio_user_guide_v0.2.pdf |}}
   
   
   
   
   
   ====== Licensing ======
   
   ADI charges a licensing fee per end product shipped. If more than one AEC block runs on a single DSP or there are multiple SigmaDSP processors per system, the fee is only incurred once. Please contact [[SigmaStudioLicensing@analog.com|SigmaStudioLicensing]] for licensing information.
