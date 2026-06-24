AD-PZSDR2400TDD-EB Characteristics & Performance
================================================

The following equipment was used to generate the characterization data seen
below.

Agilent Technologies E5071C ENA Series Network Analyzer (100kHz to 8.5GHz)

|image1|

Receive Channels Gain vs. Frequency
-----------------------------------

The following images show the gain verse frequency response of the receive channels. Each image contains two traces. The first trace shows the gain vs frequency response when the LNA (:adi:`HMC669`) is enabled. The second trace shows the gain vs frequency response when the LNA is bypassed.

.. image:: ../images/rx1_unzoom_lna_comparison.jpg
   :width: 600

Channel 1 - Gain vs frequency response - 1MHz to 6GHz.

.. image:: ../images/rx1_zoom_lna_comparison.jpg
   :width: 600

Channel 1 - Gain vs frequency response - Zoomed in, 2.2GHz to 2.7GHz.

.. image:: ../images/rx2_unzoom_lna_comparison.jpg
   :width: 600

Channel 2 - Gain vs frequency response - 1MHz to 6GHz.

.. image:: ../images/rx2_zoom_lna_comparison.jpg
   :width: 600

Channel 2 - Gain vs frequency response - Zoomed in, 2.2GHz to 2.7GHz.

Transmit Channels Gain vs. Frequency
------------------------------------

The following images show the gain verse frequency response of the receive channels. Each image contains two traces. The first trace shows the gain vs frequency response when the LNA (:adi:`HMC669`) is enabled. The second trace shows the gain vs frequency response when the LNA is bypassed.

.. image:: ../images/tx1_unzoom.jpg
   :width: 600

Channel 1 - Gain vs frequency response - 1MHz to 6GHz.

.. image:: ../images/tx1_zoom.jpg
   :width: 600

Channel 1 - Gain vs frequency response - Zoomed in, 2.2GHz to 2.7GHz.

.. image:: ../images/tx2_unzoom.jpg
   :width: 600

Channel 2 - Gain vs frequency response - 1MHz to 6GHz.

.. image:: ../images/tx2_zoom.jpg
   :width: 600

Channel 2 - Gain vs frequency response - Zoomed in, 2.2GHz to 2.7GHz.

Switch Isolation
----------------

The following plots detail results showing the isolation provided by the :adi:`HMC546LP2` for both channels.

.. image:: ../images/isolation_ch1_unzoom_ensm_test_enabled.jpg
   :width: 600

:adi:`HMC546LP2` Isolation Test, RX Channel 1 - (Signal driving TX1, switch alternating between TX to RFC and RX to RFC, and measuring the signal present on RX1).

.. image:: ../images/isolation_ch1_zoom_ensm_test_enabled.jpg
   :width: 600

:adi:`HMC546LP2` Isolation Test, RX Channel 1 - Zoomed in, 2.2GHz to 2.7GHz.

.. image:: ../images/isolation_ch2_unzoom_ensm_test_enabled.jpg
   :width: 600

:adi:`HMC546LP2` Isolation Test, RX Channel 2 - (Signal driving TX2, switch alternating between TX to RFC and RX to RFC, and measuring the signal present on RX2).

.. image:: ../images/isolation_ch2_zoom_ensm_test_enabled.jpg
   :width: 600

:adi:`HMC546LP2` Isolation Test, RX Channel 2 - Zoomed in, 2.2GHz to 2.7GHz.

.. |image1| image:: ../images/equipment-copy.png
   :width: 600
