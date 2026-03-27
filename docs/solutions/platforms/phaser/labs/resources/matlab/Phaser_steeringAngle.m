clear all; close all;
warning('off','MATLAB:system:ObsoleteSystemObjectMixin')

% Key Parameters
signal_freq = findTxFrequency();
plutoURI = 'ip:192.168.2.1';
phaserURI = 'ip:phaser.local';

% Setup the pluto
rx = setupPluto(plutoURI);

% Setup the phaser
bf = setupPhaser(rx,phaserURI,signal_freq);
bf.RxPowerDown(:) = 0;
bf.RxGain(:) = 127;

% Create the model of the phaser    
c = physconst('LightSpeed');
phaserModel = phased.ULA('NumElements',8,'ElementSpacing', ... 
    bf.ElementSpacing);
steeringVec = phased.SteeringVector("SensorArray",phaserModel, ...
    'NumPhaseShifterBits',7,'PropagationSpeed',c);

%% Set all gains to max and phases to zero
bf.RxGain(:) = 127;   % max gain = 127, min gain = 0
bf.RxAttn(:) = 0;     % if RxAttn=1 then insert 20dB attenuator
bf.RxPhase(:) = 0;
bf.LatchRxSettings(); % write new settings to the ADAR1000s

% Load Phase calibration values
PhaseCal = [0; -8.4375; -5.625; -5.625; 67.5; 87.1875; 90; 101.25];
%PhaseCal = PhaseCal*0;

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

%%
bf.release();
rx.release();