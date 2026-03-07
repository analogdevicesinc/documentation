Advanced Vector Generator
=========================

The Advanced Vector Generator libraries contain several generators for creating vectors that mimic waveforms found in common applications. These vectors go far beyond simple tone testing, allowing for data converter evaluation with spectrum-accurate vectors for many popular waveforms.

Installation
------------

The Advanced Vector Generator libraries are installed optionally during ACE installation. They rely on the ADIThon software which license you'll have to agree to when installing it.

Cable Infrastructure
--------------------

The Cable Infrastructure Advanced Vector Generator creates spectrum-accurate vectors which can be used to simulate a DOCSIS signal.

.. image:: https://wiki.analog.com/_media/resources/eval/advancedvectorgenerator_cableinfrastructure.png
   :align: center
   :width: 850px

To begin, select the Standard for which you are trying to simulate. This will set the Symbol Rate and QAM constellation size appropriately. To set either of these manually, select Other as the Standard. Then select the Sample Rate. This will be fixed to an integer multiple of the Symbol Rate. Select the appropriate Resolution for the DAC which will be playing out this vector.

Adding Channels
~~~~~~~~~~~~~~~

Add channels to the vector by adjusting the parameters in the Add Channels section on the bottom of the panel, and click the Add Channels button. The number of channels available in a single vector is limited only by the available memory and processing power of the PC, however most users will find that a channel count of several hundred or more becomes cumbersome to work with.

To add a single channel, enter the Center Frequency and Relative Amplitude, while leaving the Number of Channels at 1. This will add one channel to the vector. This can be done as many times as needed to add all the required channels. The Relative Amplitude is the amplitude of the current channel relative to the other channels. For example, if all channels are at 0dB, they will all have the same amplitude. The absolute amplitude, as seen at the output of the DAC, will depend on the relative amplitude of each channel, the number of channels, the digital backoff (see below), and the transfer function of the DAC itself.

To save time, if a number of channels are to be added to the vector that are at a constant spacing from each other, the Number of Channels and Spacing options can be used. For example, to generate an 8-carrier vector, with each channel 6MHz away from the previous channel, select 8 for the Number of Channels, and 6MHz for the spacing. In this case, the Center Frequency is the center frequency of the *first* channel.

Each channel can be edited and deleted individually, regardless of if it was added individually or as a group.

Once a channel is added, the Actual frequency is displayed after the desired Center Frequency. This frequency is the closest frequency that could be achieved given the sample rate. Also displayed is the number of points the vector will produce. This determines how much memory the pattern generator will need in order to play out this vector, as well as indicate approximately how long the vector will take to generate and download.

Editing Channels
~~~~~~~~~~~~~~~~

The Center Frequency and Amplitude of each existing channel can be edited by double-clicking on the respective entry in the list of channels. For example, to edit the Amplitude, double click on Amplitude: or the value after it in the list. This will allow the value to be edited. When you are done editing the value, click outside the edit box.

To remove a channel, single-click on the channel to highlight it, then press the Delete key (keyboard) or right-click and select Delete.

Double-clicking on the channel type (left-most entry per line) will bring up the properties box for that channel. Advanced options for the channel can be adjusted here.

The order that the channels are displayed in the list can be altered with the up and down arrows on the right side of the list. Highlight a channel, and press the up arrow or down arrow to move the channel. This will not affect the vector generation; it is for display purposes only.

Digital Backoff
~~~~~~~~~~~~~~~

When the vector is generated, the signal will be scaled such that the peak of the time-domain signal is at the full scale of the DAC (a value determined by the Resolution option). This ensures that the vector will never clip or roll over. To lower the amplitude of the vector beyond full scale, the Digital Backoff option can be used. This scaling is applied to the vector before it is sent to the DAC.

.. hint::

   \ **Note:** Some DACs have a digital and/or analog backoff which is independent of this function. This vector backoff is applied before any backoff that the DAC may perform.


Generating the Vector
~~~~~~~~~~~~~~~~~~~~~

When the resulting data vector is requested, either to graph or to download to a board, it will be generated automatically. After it has been generated, the Peak to Average ratio (crest factor) will be displayed above the list of channels. Note that changing the channels will not update this value until the vector is generated again.

DOCSIS 3.0
~~~~~~~~~~

Beyond the standard Center Frequency and Amplitude options, DOCSIS 3.0 channels have a number of other properties that can be adjusted. Double-clicking the **DOCSIS 3.0** text in the channel list will bring up the Channel Properties box:

.. image:: https://wiki.analog.com/_media/resources/eval/advancedvectorgenerator_docsis30.png
   :align: center

From here, a number of items can be viewed, and several items can be altered.

+-------------------+-------------------------------------------------------------------------------------------------------+
| Property          | Description                                                                                           |
+===================+=======================================================================================================+
| Name              | The internal name of the channel. This is displayed for debugging use only.                           |
+-------------------+-------------------------------------------------------------------------------------------------------+
| Number of Symbols | The calculated number of symbols in the vector. This is determined automatically.                     |
+-------------------+-------------------------------------------------------------------------------------------------------+
| Modulation Rate   | The Modulation Rate is specified in the main window, but is displayed again here.                     |
+-------------------+-------------------------------------------------------------------------------------------------------+
| Center Frequency  | The Center Frequency of the channel. Changing this value will update the main window as well.         |
+-------------------+-------------------------------------------------------------------------------------------------------+
| Interpolation     | The interpolation factor used internally to arrive at the specified sample rate.                      |
+-------------------+-------------------------------------------------------------------------------------------------------+
| Power Level       | The relative amplitude of the vector. Changing this value will update the main window as well.        |
+-------------------+-------------------------------------------------------------------------------------------------------+
| Alpha             | Excess Bandwidth, specified by the DOCSIS standard for the configuration you are generating           |
+-------------------+-------------------------------------------------------------------------------------------------------+
| Modulation        | The modulation routine used, specified by the DOCSIS standard for the configuration you a generating. |
+-------------------+-------------------------------------------------------------------------------------------------------+
| Source            | The source of the data which is modulated to form the DOCSIS channel. This is always set to Random.   |
+-------------------+-------------------------------------------------------------------------------------------------------+

Wireless Infrastructure
-----------------------

The Wireless Infrastructure Advanced Vector Generator creates spectrum-accurate vectors which can be used to simulate a variety of carries commonly used in the Wireless/Cellular industries.

.. image:: https://wiki.analog.com/_media/resources/eval/advancedvectorgenerator_wirelessinfrastructure.png
   :align: center

Multiple carrier types can be combined in a single vector. For example, one vector could contain both a GSM carrier and a WCDMA carrier. Multiple carriers of the same type are also allowed (for example: multi-carrier GSM).

.. hint::

   \ **Note:** The vectors created with this tool are spectrally accurate. However, in most cases they are not complete implementations of a given standard, and thus may not demodulate properly when received by a standards-compliant receiver or test equipment. They are provided as a way to quickly evaluate a signal chain's analog performance in a lab environment.


Adding Carriers
~~~~~~~~~~~~~~~

Adding carriers to the vector can be accomplished multiple ways. Carriers can be added individually, or they can be added as Carrier Groups. When carriers are in a group, they can easily be frequency shifted and scaled, without adjusting each individual carrier.

Single Carriers
^^^^^^^^^^^^^^^

To add a single carrier to the vector, enter the Center Frequency and Relative Amplitude, and select the air standard, leaving the number of carriers at 1. Click Add Carriers, and the carrier will be added to the list.

Carrier Groups
^^^^^^^^^^^^^^

If multiple carriers of the same type, with equal spacing between them, are to be added to the vector, adjust the No. of Carriers to the desired number of carriers, and adjust the Carrier Spacing. The Center Frequency in this case is the center frequency of the group of carriers.

Editing Carriers
~~~~~~~~~~~~~~~~

The Center Frequency and Amplitude of a carrier or carrier group can be edited by double-clicking on the current value displayed in the list of carriers. Advanced properties for each carrier can be edited by double-clicking on the carrier type (GSM, CDMA, etc) in the carrier list.

When editing the center frequency of a Carrier Group, the center frequencies of each carrier within the group will be shifted so that the difference between the carrier's center frequency and the group's center frequency is maintained.

When editing the amplitude of the Carrier Group, the amplitude of each carrier in the group will be shifted by the same amount. The difference (in dB) between the group's amplitude and the individual carrier's amplitude will be maintained.

The individual carriers within a group can be edited in the same way that a single carrier is edited.

Carrier Order
~~~~~~~~~~~~~

The first carrier in the list is considered the Primary Carrier. This carrier is used to define many of the parameters of the overall vector, including the length of the data vector and the allowable sample rates. This should always be the carrier that is considered "most important." Subsequent carriers may be automatically windowed and resampled so that they fit properly into the vector length determined by the primary carrier. When this occurs, "Windowed" and/or "Resampled" will appear in light gray just to the right of the carrier's settings (see image above).

To change the order of the carriers, select the carrier to move, and use the up and down arrow buttons on the right side of the carrier list.

.. _digital-backoff-1:

Digital Backoff
~~~~~~~~~~~~~~~

When the vector is generated, the signal will be scaled such that the peak of the time-domain signal is at the full scale of the DAC (a value determined by the Resolution option). This ensures that the vector will never clip or roll over. To lower the amplitude of the vector beyond full scale, the Digital Backoff option can be used. This scaling is applied to the vector before it is sent to the DAC.

.. hint::

   \ **Note:** Some DACs have a digital and/or analog backoff which is independent of this function. This digital backoff is applied before any backoff that the DAC may perform.


.. _generating-the-vector-1:

Generating the Vector
~~~~~~~~~~~~~~~~~~~~~

When the resulting data vector is requested, either to graph or to download to a board, it will be generated automatically. After it has been generated, the Peak to Average ratio (crest factor) will be displayed above the list of carriers. Note that changing the carriers will not update this value until the vector is generated again.

WCDMA/CDMA2k
~~~~~~~~~~~~

The WCDMA and CMDA2k Carrier Properties screens provide the option to override many of the parameters used to generate a vector.

.. image:: https://wiki.analog.com/_media/resources/eval/advancedvectorgenerator_wcdmacdma2k.png
   :align: center

General Carrier Properties
^^^^^^^^^^^^^^^^^^^^^^^^^^

In addition to the Center Frequency and Power Level (Amplitude) options, the Spreading Factor, Interpolation, and Windowing mode can be changed. The Chip Frequency is provided for reference only. It is fixed by the selected standard (3.84MHz for WCDMA, 1.2288MHz for CDMA2k). The Number of Symbols is also provided for reference only, as it is calculated automatically. It is recommended that the Spreading Factor, Interpolation, and Windowing not be changed for optimal performance.

Users
^^^^^

A WCDMA/CDMA2k carrier contains a number of user code slots. The Users section of the carrier properties allows these user codes to be configured. Up to 223 user codes can be added at once. For the most realistic peak-to-average ratio (crest factor), at least 12 users should be placed across the full 32 to 255 code range.

Adding Users
""""""""""""

To add a new user, click the Add User button. This will create a user with a randomly selected code, and add it to the end of the user list. It can then be edited just as any existing user can.

Editing Users
"""""""""""""

To edit an existing user, click on the user in the user list. The properties on the right side of the screen will then be updated to reflect the settings of the selected user.

+-----------------+---------------------------------------------------------------------------------------------------+
| Property        | Description                                                                                       |
+=================+===================================================================================================+
| Code            | This is the code assigned to the selected user. There should not be two users with the same code. |
+-----------------+---------------------------------------------------------------------------------------------------+
|                 |                                                                                                   |
+-----------------+---------------------------------------------------------------------------------------------------+
| Modulation      | Offers a choice of different modulation techniques for this user:                                 |
|                 | \* QPSK - Quadrature Phase-Shift Keying                                                           |
|                 | \* 8QAM - Quadrature Amplitude Modulation, with 8 symbols                                         |
|                 | \* 16QAM - Quadrature Amplitude Modulation, with 16 symbols                                       |
|                 | \* 32QAM - Quadrature Amplitude Modulation, with 32 symbols                                       |
+-----------------+---------------------------------------------------------------------------------------------------+
|                 |                                                                                                   |
+-----------------+---------------------------------------------------------------------------------------------------+
|                 |                                                                                                   |
+-----------------+---------------------------------------------------------------------------------------------------+
|                 |                                                                                                   |
+-----------------+---------------------------------------------------------------------------------------------------+
|                 |                                                                                                   |
+-----------------+---------------------------------------------------------------------------------------------------+
|                 |                                                                                                   |
+-----------------+---------------------------------------------------------------------------------------------------+
| Source          | This determines what data is fed to the modulation. This is always set to Random.                 |
+-----------------+---------------------------------------------------------------------------------------------------+

Deleting Users
""""""""""""""

To delete an existing user, select the user in the user list, and click Delete User.

GSM
~~~

The GSM Carrier Properties screens provide the option to override many of the parameters used to generate a vector.

.. image:: https://wiki.analog.com/_media/resources/eval/advancedvectorgenerator_gsm.png
   :align: center

The Power Level (Amplitude) and Center Frequency are the same as those that can be edited on the main screen. The Interpolation is computed automatically.

Modulation
^^^^^^^^^^

The following modulations are available for a GSM carrier:

==== =======================
GMSK Original GSM modulation
==== =======================
8PSK GSM EDGE modulation
==== =======================

Timeslots
^^^^^^^^^

Each GSM carrier contains 8 timeslots, labeled 0 through 7. For each timeslot, a Source can be specified, which determines what data is given to the modulation routine to come up with the carrier. The source is always a pseudo-random data generator. When using the random source, the Seed can be specified to ensure that the "random" data generated is consistent each run.

LTE
~~~

The LTE (Uplink/Downlink) Carrier Properties screens provide the option to adjust many of the parameters used to generate a vector.

.. image:: https://wiki.analog.com/_media/resources/eval/advancedvectorgenerator_lte.png
   :align: center

The Power Level (Amplitude) and Center Frequency are the same as those that can be edited on the main screen. The Interpolation is computed automatically.

Transmission Bandwidth
^^^^^^^^^^^^^^^^^^^^^^

The following bandwidths are supported, with the corresponding Resource Block (RB) count:

====== =====
1.4MHz 6RB
====== =====
3.0MHz 15RB
5.0MHz 25RB
10MHz  50RB
15MHz  75RB
20MHz  100RB
====== =====

Changing the transmission bandwidth will change the vertical (y-axis) scale on the payload graph.

Cyclical Prefix
"""""""""""""""

Both Normal and Extended options are supported. This affects the number of symbols per slot, with Extended having one less slot than Normal.

ACLR
""""

This option adjusts the trade-offs between achieving better ACLR versus better EVM.

Enabled Slots
"""""""""""""

This sets the horizontal (x-axis) on the payload graph, and determines how many slots will be generated in the vector. A lower slot count will improve the time it takes to generate a vector.

Payload Graph
"""""""""""""

This graph provides a visual representation of each frame's payload. Payloads can be added by clicking and dragging within the graph. Once a payload has been added, it can be removed by right-clicking on the payload and selecting Delete from the menu. To edit a payload, right-click the payload and select Properties. From the Payload Properties window, the Source, Modulation, and Power Level can be adjusted.
