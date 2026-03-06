Device Control and Data Streaming with MATLAB Toolboxes
=======================================================

Device interfaces which provide control and data streaming are implemented with MATLAB System Objects and Simulink Blocks. These System Objects can be access under the "adi" namespace in MATLAB and are followed by their part number or board name and finally Tx or Rx:

::

   adi.<Part or Board Name>.<Tx or Rx>

For example, to instantiate an AD9361 object to control the Tx aspects of the transceiver it can be created as follows:

::

   tx = adi.AD9361.Tx;

All supported boards are derived from low level objects based on their parts. For example, the DAQ2 Evaluation board actually contains an AD9680 and AD9144. Therefore, it simply uses AD9680 and AD9144 objects under the hood. However, to interact with the more familiar DAQ2 interface naming the Rx side can be instantiated like above as:

::

   rx = adi.DAQ2.Rx;

For example usage of certain objects, it can be useful to inspect their related test code which exercises initiations in different configurations. The available code is available in the GitHub repo folder :git-MathWorks_tools:`here <test>`, where object tests have the naming convention <Object>Tests.m.

To get a list of currently available objects with the BSP installed simply run:

::

   help adi

To get more information on a given object run:

::

   help adi.<Part of Board Name>.<Tx or Rx>

or

::

   doc adi.<Part of Board Name>.<Tx or Rx>

Property information can be queried as well:

::

   help adi.<Part of Board Name>.<Tx or Rx>.<PropertyName>

For example:

::

   help adi.ADRV9009.Rx.GainControlMode
    GainControlMode Gain Control Mode
       specified as one of the following:
       'slow_attack' — For signals with slowly changing power levels
       'fast_attack' — For signals with rapidly changing power levels
       'manual' — For setting the gain manually with the Gain property
       'hybrid' — For configuring hybrid AGC mode

Common Attributes
-----------------

There are some common attributes that need to be set for system objects and parts.

-  ``uri`` Context address of IIO device. Possible options include:

   -  IP with usage ''rx.uri = 'ip:192.168.2.1' ''
   -  USB with usage ''rx.uri = 'usb:1.2.3' ''

Basic Example
-------------

Here is a basic example of using a transmit and receiver together.

::

   % Create a receiver and transmitter pairs
   tx = adi.AD9361.Tx();
   rx = adi.AD9361.Rx();
   % Defined URIs
   uri = 'ip:analog';
   tx.uri = uri;
   rx.uri = uri;

   %% Generate and transmit data continuously
   amplitude = 2^15; frequency = 0.12e6;
   swv1 = dsp.SineWave(amplitude, frequency);
   swv1.ComplexOutput = true;
   swv1.SamplesPerFrame = 1e5;
   swv1.SampleRate = tx.SampleRate;
   data = swv1();
   % Send to hardware and repeat forever
   tx.EnableCyclicBuffers = true;

   %% Receive
   for k=1:10
       valid = false;
       while ~valid
           [out, valid] = rx();
       end
   end

   %% Cleanup
   rx.release();
   tx.release();

   %% Plot
   nSamp = length(out);
   fs = tx.SamplingRate;
   FFTRxData  = fftshift(10*log10(abs(fft(out))));
   df = fs/nSamp;  freqRangeRx = (-fs/2:df:fs/2-df).'/1000;
   plot(freqRangeRx, FFTRxData);
   xlabel('Frequency (kHz)');ylabel('Amplitude (dB)');grid on;

More examples are included in each toolbox

-  :git-TransceiverToolbox:`Transceiver Examples <trx_examples/streaming>`
-  :git-HighSpeedConverterToolbox:`High-Speed Converter Examples <hsx_examples/streaming>`

Extending Interfaces
--------------------

If a driver attribute or setting is not available in the standard objects it can be easily extended to cover more IIO attributes. See this :doc:`guide </wiki-migration/resources/eval/user-guides/matlab_bsp_extend>`.
