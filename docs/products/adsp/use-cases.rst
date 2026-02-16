.. _adsp use-cases:

Use cases
=========

Analog Devices Digital Signal Processors (ADSP) are industry standards for both
automotive and consumer audio.

Professional & Consumer Audio
-----------------------------

Neural DSP Quad Cortex
^^^^^^^^^^^^^^^^^^^^^^

The `Neural DSP Quad Cortex <https://neuraldsp.com/quad-cortex>`_ is a flagship
floorboard amp modeler that utilizes the :adi:`ADSP-SC589
<en/products/ADSP-SC589.html>` (Quad-Core SHARC+). The dual SHARC+ cores
provide the high-performance floating-point processing required for neural
capture, an AI-driven process that replicates physical amplifiers and effects
with extreme accuracy. The integrated ARM Cortex-A5 core manages the
Linux-based multi-touch UI, while the SHARC+ cores handle real-time audio
processing at extremely low latency.

* :adi:`Quad Cortex Success Story <en/lp/001/customer-success-stories-quad-cortex.html>`

Audinate Dante networking
^^^^^^^^^^^^^^^^^^^^^^^^^

The Dante Embedded Platform (DEP) is available as a software-based solution for
ADSP-SC5xx processors. Manufacturers can integrate high-performance Dante
audio-over-IP networking directly onto the chip's ARM core. This provides a
single-chip solution for low-latency networked audio, eliminating the need for
separate hardware modules in professional AV systems.

* `Audinate Announces Availability of Dante Embedded Platform for Analog Devices’ SHARC® Audio Digital Signal Processors
  <https://www.audinate.com/press/audinate-announces-availability-of-dante-embedded-platform-for-analog-devices-sharc-audio-digital-signal-processors/>`__

Automotive
----------

Modern vehicles use high-performance SHARC+ processors (like the **SC59x**
series) to manage complex cabin acoustics.

* **Road Noise Cancellation (RNC):** SHARC+ processors generate anti-noise
  signals in real-time to cancel tire and road vibrations. This requires the
  extremely low deterministic latency provided by the SHARC architecture.
* **In-Car Communications (ICC):** Uses beamforming and noise reduction to allow
  passengers to speak clearly across the cabin without shouting.
* **Personal Audio Zones (PAZ):** Creates localized "sound bubbles" for
  individual passengers, allowing different audio streams (calls, music,
  navigation) to be heard without headphones or disturbing others.
* **Electric Vehicle (EV) Sound:** Handles Engine Sound Synthesis (ESS) for
  driver feedback and Acoustic Vehicle Alerting Systems (AVAS) to ensure
  pedestrian safety at low speeds.

Automotive Grade Linux
^^^^^^^^^^^^^^^^^^^^^^

Automotive Grade Linux is a project under The Linux Foundation that defines a
full software stack for vehicles. It classically targets infotainment systems,
but in 2026 expanded support to the Electronic Control Unit (ECU) of vehicles.
It provides a complex layering of software based on virtualization
technologies, making application development easier and safer.

ADSP SoCs are far more resource constrained than the processors that AGL is
targeting. Additionally, in order to optimize the performance of the ADSP SoCs
many tasks done by Linux in AGL are off-loaded from the ARM cores to the DSP
cores (e.g. EAVB, A2B).
