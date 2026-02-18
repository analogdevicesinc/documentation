.. _cn0566_matlab_setup:

CN0566 (Phaser) MATLAB Setup Guide
==================================

Getting Started and Setup
-------------------------

If the CN0566 (Phaser) board is not yet assembled, please visit the 
:ref:`Quick Start Guide <cn0566_quickstart>` and watch the 
**Unboxing/Setup Video** to see how to assemble the Phaser and
related boards.

The :ref:`Quick Start Guide <cn0566_quickstart>`
also has instructions on installing an image of ADI Kuiper Linux onto the
Raspberry Pi’s SD card, which will be required.

After that is done, a few modifications need to be made to the setup from the
quick start guide.

- Disconnect the Pluto from the Raspberry Pi, and connect the Pluto to your
  computer using a microUSB to USB cable, or other compatible standard
- Connect the Raspberry Pi to your computer via ethernet, using the onboard
  ethernet port on the Raspberry Pi

Once completed, your setup should resemble the image below: 

.. figure:: final_assembly.png

Setting Up MATLAB
-----------------

Installing MATLAB
~~~~~~~~~~~~~~~~~

.. tip::
  If you already have a recent version of MATLAB installed, please skip
  ahead to the **Installing toolboxes** section below. For the hardware
  board support packages to work, you must use Matlab version **R2022b** or newer.
  You can go to the download page by clicking `here <https://www.mathworks.com/downloads>`__,
  you may be required to sign in with your MathWorks account first.

.. figure:: matlab_download_website.png

--------------

Select the release version on the left, then click the download button.

After downloading the installer, open it to run the MATLAB installation tool.
During the installation process, there will be a window to select which
products and toolboxes will be installed, as shown in the image below. Ensure
that all the products shown in the image have been selected.

.. figure:: mathworks_products_install.png

--------------

Once this has been done, continue installing MATLAB through the installer as
normal.

Installing Toolboxes
~~~~~~~~~~~~~~~~~~~~

Once MATLAB is installed, additional toolboxes can be downloaded through the
built-in **Add-On Explorer**. It can be found by opening MATLAB, selecting the
**Home** tab, and clicking the three colored cubes labeled **Add-Ons** located
near the top. 

.. figure:: matlab_addons_button.png

--------------

This will open the Add-On Explorer. Here, you can search for toolboxes using the
search bar in the top right corner, and install them.

.. figure:: matlab_addons_search.png

--------------

- If you have **skipped here** without installing any toolboxes while installing
  MATLAB, or already had MATLAB installed, get these first:

  - Antenna Toolbox
  - Communications Toolbox
  - DSP System Toolbox
  - Phased Array System Toolbox
  - Signal Processing Toolbox

- Install these additional toolboxes:

  - Analog Devices, Inc. RF and Microwave Toolbox
  - Analog Devices, Inc. Transceiver Toolbox
  - Communications Toolbox Support Package for Analog Devices ADALM-Pluto Radio
  - MATLAB Support for MinGW-w64 C/C++ Compiler

Running the Labs
----------------

Verify Connectivity
~~~~~~~~~~~~~~~~~~~

With Phaser connected to your local network or directly to your host machine
with MATLAB installed, create an instance of the adi.Phaser class from the
command prompt with the IP address of the Raspberry Pi.

.. code:: matlab

   bf = adi.Phaser;
   bf.uri = 'ip:phaser';
   bf()

This will connect and configure Phaser with a default set of parameters. If you
receive a connectivity error verify the Raspberry Pi is powered up and you can
at least ping the device. If you are having issues reach out to our support
forums on EngineerZone.

Next verify connectivity to Pluto with a similar method. Create and instance of
the adi.AD9361.Rx class and run the operator method as so:

.. code:: matlab

   sdr = adi.AD9361.Rx
   sdr.uri = 'ip:pluto';
   data = sdr();

Like the Phaser system object this operation should not generate any errors.
The *data* vector should contain non-zero data.

If there are errors while attempting to verify connectivity, please try the
following options:

- Check all the packages/toolboxes listed above are installed properly
- Restart MATLAB and run the code again
- Disconnect and re-connect the cable to the device in question
- Ensure the Raspberry Pi’s SD card has ADI Kuiper Linux installed (and that it
  works)

Running Scripts
~~~~~~~~~~~~~~~

- Once both the Phaser and Pluto are able to communicate with MATLAB, download
  and extract 

  :download:`Phaser_steeringAngle_rev1<phaser_steeringangle_rev1.zip>`

- Then open the file **Phaser_steeringAngle_rev1.m**
- This script functions to scan through a range of steering angles and output a
  plot of the array factor.

--------------

.. code:: matlab

   % Key Parameters
   signal_freq = 10.145e9;  % this is the HB100 frequency
   signal_freq = findTxFrequency();
   plutoURI = 'ip:192.168.2.1';
   phaserURI = 'ip:phaser.local';

   % Setup the pluto
   rx = setupPluto(plutoURI);

   % Setup the phaser
   bf = setupPhaser(rx,phaserURI,signal_freq);
   bf.RxPowerDown(:) = 0;
   bf.RxGain(:) = 127;

This segment of the code serves to initialize the Pluto and Phaser objects in
MATLAB using the ADI toolboxes installed earlier, here labeled as “rx” and “bf”
respectively. It also scans briefly to find the frequency of the HB100 emitter.

.. code:: matlab

   % Create the model of the phaser    
   c = physconst('LightSpeed');
   phaserModel = phased.ULA('NumElements',8,'ElementSpacing', ... 
       bf.ElementSpacing);
   steeringVec = phased.SteeringVector("SensorArray",phaserModel, ...
       'NumPhaseShifterBits',7,'PropagationSpeed',c);

This segment creates a model of the antenna array on the Phaser, using the
Phased Array System Toolbox (phased) from MathWorks. The Phaser features 8
uniformly spaced elements, which is modeled using the Uniform Linear Array
object (phased.ULA) from the Phased Array System Toolbox. A corresponding
steering vector is created using the SteeringVector object, also from the 
Phased Array System Toolbox.

.. code:: matlab

   %% Set all gains to max and phases to zero
   bf.RxGain(:) = 127;   % max gain = 127, min gain = 0
   bf.RxAttn(:) = 0;     % if RxAttn=1 then insert 20dB attenuator
   bf.RxPhase(:) = 0;
   bf.LatchRxSettings(); % write new settings to the ADAR1000s

   % Load Phase calibration values
   PhaseCal = [0; -8.4375; -5.625; -5.625; 67.5; 87.1875; 90; 101.25];

This segment just sets the gain levels and phase calibration values.

.. code:: matlab

   %% Sweep the steering angle and capture data
   steeringAngle = -90 : 90;
   ArrayFactor = zeros(size(steeringAngle));
   for ii = 1 : numel(steeringAngle)
       arrayWeights = steeringVec(signal_freq,steeringAngle(ii));
       phases = rad2deg(angle(conj(arrayWeights(:))));
       phases = phases - phases(1);
       phases = phases + PhaseCal;
       phases = wrapTo360(phases);
       bf.RxPhase(:) = phases.';
       bf.LatchRxSettings();
       receivedSig_HW = rx();
       receivedSig_HW_sum = sum(receivedSig_HW,2);
       receivedFFT = fft(receivedSig_HW_sum);
       ArrayFactor(ii) = (max(abs(receivedFFT)));
   end

Here is where the actual beam steering action happens in the code.
The code creates an array containing the angles that the beam will be steered
through. Then, it performs a loop where:

#. Takes a given angle from the array of angles
#. Uses the given steering angle to create another array containing the
   respective phase shifts to be applied to each antenna element
#. Applies the phase shifts to the Phaser
#. Collects data from the ADALM-PLUTOPluto, perform FFT on the data to get the max
   amplitude, and record it
#. Repeats for the next steering angle

.. code:: matlab

   %% Compare the measured array factor and model
   [~,ind] = max(ArrayFactor);
   EmitterAz = steeringAngle(ind)
   figure(101)
   arrayWeights = steeringVec(signal_freq,EmitterAz);
   pattern(phaserModel,signal_freq,-90:90,0,'CoordinateSystem', ...
       'Rectangular','Type','powerdb','weights',arrayWeights)
   hold on;

   % Plot the measured data and the model
   plot(steeringAngle,mag2db(ArrayFactor./max(abs(ArrayFactor))))

Here, the Phased Array System Toolbox is used to simulate the array factor for
the Phaser. Then both the experimentally obtained array factor (from the data
above) and the simulated array factor are plotted. The resulting plot that
appears should resemble the image below: 

.. figure:: phaser_steeringangle_output.png
