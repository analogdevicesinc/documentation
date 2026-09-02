%% simple_jupiter.m — 1-to-1 MATLAB equivalent of sanity_check_v2.py
% This script mirrors the Python sanity check: configure Rx, build two
% complex tones, transmit them on TX0/TX1, receive on RX0/RX1, and plot
% the overlay spectrum.

uri = 'ip:10.75.162.60'; % Change this to the correct IP

%% Configure Rx
rx = adi.ADRV9002.Rx('uri', uri);
rx.ENSMModeChannel0  = 'rf_enabled';
rx.ENSMModeChannel1  = 'rf_enabled';
rx.EnabledChannels   = [1 2];
rx.SamplesPerFrame   = 2^16;           % Match Python: N = 2^16

rx.CenterFrequencyChannel0 = 5.836e9;
rx.CenterFrequencyChannel1 = 5.836e9;

% Connect to hardware so read-only properties are populated
rx();

Fs = double(rx.SamplingRate);
disp(['Sample rate: ', num2str(Fs)]);
% disp(['RF BW Ch0:   ', num2str(rx.RFBandwidthChannel0)]);
% disp(['RF BW Ch1:   ', num2str(rx.RFBandwidthChannel1)]);

%% Create two complex sinusoid waveforms (match Python exactly)
N  = 2^16;
ts = 1 / Fs;
t  = (0:N-1)' * ts;                    % column vector

fc0 = 0.5e6;                           % Tone 0: 0.5 MHz
i0  = cos(2*pi*fc0*t) * 2^14;
q0  = sin(2*pi*fc0*t) * 2^14;
iq0 = i0 + 1j*q0;

fc1 = 1e6;                             % Tone 1: 1 MHz
i1  = cos(2*pi*fc1*t) * 2^14;
q1  = sin(2*pi*fc1*t) * 2^14;
iq1 = i1 + 1j*q1;

%% Configure Tx and transmit
tx = adi.ADRV9002.Tx('uri', uri);
tx.EnabledChannels       = [1 2];
tx.ENSMModeChannel0      = 'rf_enabled';
tx.ENSMModeChannel1      = 'rf_enabled';
tx.DataSource            = 'DMA';
tx.CenterFrequencyChannel0 = 5.836e9;
tx.CenterFrequencyChannel1 = 5.836e9;
tx.EnableCyclicBuffers   = true;

tx([iq0, iq1]);                         % TX0 = 0.5 MHz, TX1 = 1 MHz

%% Receive data
data = rx();
rx0 = data(:,1);
rx1 = data(:,2);

%% FFT with Hanning window (same as Python)
win = hanning(length(rx0));

X0  = fftshift(fft(rx0 .* win));
X1  = fftshift(fft(rx1 .* win));

freq = (-N/2:N/2-1)' * (Fs/N) / 1e6;  % MHz

mag0_dB = 20*log10(abs(X0) / (2^15 * N));
mag1_dB = 20*log10(abs(X1) / (2^15 * N));

%% Plot — single overlay figure (matches Python output)
figure('Position', [100 100 900 350]);
plot(freq, mag0_dB, 'Color', [0.12 0.47 0.71], 'LineWidth', 1);
hold on;
plot(freq, mag1_dB, 'Color', [1.0 0.50 0.05], 'LineWidth', 1);
xline(fc0/1e6, '--', 'Color', [0.12 0.47 0.71], 'Alpha', 0.7);
xline(fc1/1e6, '--', 'Color', [1.0 0.50 0.05], 'Alpha', 0.7);
xlabel('Frequency [MHz]');
ylabel('Magnitude [dBFS]');
title('RX0 and RX1 Gain vs Frequency');
legend('RX0', 'RX1');
grid on;
hold off;
