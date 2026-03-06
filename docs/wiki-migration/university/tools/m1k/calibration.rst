ADALM1000 Calibration Procedure
===============================

.. important::

   Note that Revision F of the M1k is calibrated in the Factory and does not need the user to perform any calibration. The purpose of this Document is codify the steps required if the factory settings need to be changed or updated and for the legacy Revision D of the M1k hardware.


The ADALM1000 device can be calibrated by the user to achieve more accurate measurements and signal generation. The calibration procedure requires a Digital Multimeter (DMM) and a resistor with a value anywhere between 2.5Ω and 25Ω.

The device is calibrated by taking a set of measurements according to the procedures described in the sections below. The measurement results must be hand written into a calibration file that will be afterwards used by the calibration software to compute all the calibration parameters and write them into the device.

.. important::

   Calibration support is available only stating from :git-Pixelpulse2:`Pixelpulse v0.88 <releases/latest>` and :git-m1k-fw>`__ (You don't need to look at the firmware unless you want to - it's only added here for completeness).

   
   Make sure to `update the firmware <https::`firmware version v2.06 </wiki.analog.com/firmware-upgrade>` on your device and Pixelpulse before starting the calibration procedure.


Calibration file
----------------

The calibration files contains *<reference, value>* data pairs for all the measurement and source channels. Below is an example of how a default calibration file looks like.

::

   # Channel A, measure V
   </>
   <0.0000, 0.0000>
   <2.5000, 2.5000>
   <\>

   # Channel A, measure I
   </>
   <0.0000, 0.0000>
   <0.1000, 0.1000>
   <-0.1000, -0.1000>
   <\>

   # Channel A, source V
   </>
   <0.0000, 0.0000>
   <2.5000, 2.5000>
   <\>

   # Channel A, source I
   </>
   <0.0000, 0.0000>
   <0.1000, 0.1000>
   <-0.1000, -0.1000>
   <\>

   # Channel B, measure V
   </>
   <0.0000, 0.0000>
   <2.5000, 2.5000>
   <\>

   # Channel B, measure I
   </>
   <0.0000, 0.0000>
   <0.1000, 0.1000>
   <-0.1000, -0.1000>
   <\>

   # Channel B, source V
   </>
   <0.0000, 0.0000>
   <2.5000, 2.5000>
   <\>

   # Channel B source I
   </>
   <0.0000, 0.0000>
   <0.1000, 0.1000>
   <-0.1000, -0.1000>
   <\>

The calibration file must contain for each channel at least the data points shown in the example above. It is possible to add as many data points as desired, the only constraint is that the measurement for offset calibration (0V or 0A reference) has to be the first data pair in the data set. A data set for a channel is delimited by the </> and <\\> tags. The order of the data sets in the calibration file must be as in the example and the calibration file must contain all the shown data sets otherwise it is not valid.

The example calibration file can be downloaded from the link below. This file assumes perfect device operation - no offset or gain errors, and can be used to reset your device calibration in case an inaccurate calibration file was loaded into the device.

.. admonition:: Download
   :class: download

   |ADALM1000 default calibration file|

.. important::

   If an inaccurate calibration file was loaded into the device this can be erased by writing into the device the default calibration file.


.. important::

   When you want to re-calibrate your device, before starting the calibration process write into the device the default calibration file and power cycle the device. This will erase the previous calibration and will ensure correct re-calibration.


Storing the calibration data into the device
--------------------------------------------

To store the calibration data into the device:

-  Use the *smu* binary by typing in a terminal *smu --write-calibration /path/to/cal/file* (or as *smu -w /path/to/cal/file*)

The smu binary also supports displaying and resetting calibration for all supported, attached devices via the following:

-  reset: *smu --reset-calibration* (also as *smu -r*)
-  display: *smu --display-calibration* (also as *smu -d*)

.. important::

   Make sure that Pixelpulse is closed when running the *smu* binary.


To acquire the smu binary, use the libsmu installer below in addition to installing the correct architecture support for Microsoft's `Visual C++ Redistributable for Visual Studio 2015 <https://www.microsoft.com/en-us/download/details.aspx?id=48145>`__.

Instructions on how to build, install and use libsmu can be found :doc:`here </wiki-migration/university/tools/m1k/libsmu>`.

.. admonition:: Download
   :class: download

   libsmu installer: :git-libsmu:`libsmu-setup.exe <releases/latest>`


.. important::

   If you have multiple ADALM1000 devices make sure that just one device is plugged in when trying to store the calibration data.


Calibration procedures
----------------------

The procedures below describe all the required steps to perform and record the calibration measurements. The Voltage Source of the ADALM1000 is very precise and normally does not require calibration so it can be left to the default values in the calibration file.

Voltage measurement calibration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Voltage measurement calibration requires at least 2 data points - 0V and 2.5V. The steps below describe the calibration procedure:

-  On the ADALM1000 device connect the CH A and CH B inputs to GND
-  In Pixelpulse set the mode for both channels to *Measure Voltage*
-  Using Pixelpulse read the voltage measurements for the two channels
-  Replace into the calibration file in the **# Channel A/B, measure V** sections the *<0.0000, 0.0000>* data pairs with *<0.0000, gnd_value>*, where *gnd_value* is the voltage measurement read in Pixelpulse
-  On the ADALM1000 device connect the CH A and CH B inputs to 2.5V
-  Using Pixelpulse read the voltage measurements for the two channels
-  Using a DMM read the actual value of the 2.5V
-  Replace into the calibration file in the **# Channel A/B, measure V** sections the *<2.5000, 2.5000>* data pairs with *<dmm_value, pixelpulse_value>*, where *pixelpulse_value* is the voltage measurement read in Pixelpulse and *dmm_value* is the 2.5V measurement taken with the DMM

Voltage source calibration
~~~~~~~~~~~~~~~~~~~~~~~~~~

Voltage source calibration requires at least 2 data points - 0V and 2.5V. The steps below describe the calibration procedure:

-  In Pixelpulse set the mode for both channels to *Source Voltage Measure Current*
-  In Pixelpulse make sure that the *Repeated Sweep* mode is not active
-  From Pixelpuse source 0V on channels A and B
-  Using a DMM measure the voltage outputs of CH A and CH B relative to GND
-  Replace into the calibration file in the **# Channel A/B, source V** sections the *<0.0000, 0.0000>* data pairs with *<pixelpulse_value, dmm_value>*, where *pixelpulse_value* is the voltage source value in Pixelpulse and *dmm_value* is the measurement taken with the DMM
-  From Pixelpuse source 2.5V on channels A and B
-  Using a DMM measure the voltage outputs of CH A and CH B relative to GND
-  Replace into the calibration file in the **# Channel A/B, source V** sections the <2.5000, 2.5000> data pairs with *<pixelpulse_value, dmm_value>*, where *pixelpulse_value* is the voltage source value in Pixelpulse and *dmm_value* is the measurement taken with the DMM

Current measurement calibration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Current measurement calibration requires at least 3 data points - 0A, 100mA and -100mA. Channels A and B must be calibrated sequentially. The steps below describe the calibration procedure:

-  On the ADALM1000 leave both CH A and CH B open
-  In Pixelpulse set the mode of the channel to be calibrated to *Source Voltage Measure Current*
-  In Pixelpulse read the current measurement for the channel to be calibrated
-  Replace into the calibration file in the **# Channel A/B, measure I** sections the *<0.0000, 0.0000>* data pairs with *<0.0000, gnd_value>*, where *gnd_value* is the current measurement read in Pixelpulse
-  On the ADALM1000 device connect the CH A or CH B to one end of the resistor
-  Connect the other end of the resistor to the current input of a DMM
-  Connect the GND of the DMM to the ADALM1000 2.5V pin
-  In Pixelpulse source a voltage value on the channel to be calibrated so that the current measurement is close to 100mA
-  In Pixelpulse read the current measurement for the channel to be calibrated
-  Read the current measurement on the DMM
-  Replace into the calibration file in the **# Channel A/B, measure I** sections the *<0.1000, 0.1000>* data pairs with *<dmm_value, pixelpulse_value>*, where *pixelpulse_value* is the current measurement read in Pixelpulse and *dmm_value* is the current measurement taken with the DMM
-  In Pixelpulse source a voltage value on the channel to be calibrated so that the current measurement is close to -100mA
-  In Pixelpulse read the current measurement for the channel to be calibrated
-  Read the current measurement on the DMM
-  Replace into the calibration file in the **# Channel A/B, measure I** sections the *< -0.1000, -0.1000>* data pairs with *<dmm_value, pixelpulse_value>*, where *pixelpulse_value* is the current measurement read in Pixelpulse and *dmm_value* is the current measurement taken with the DMM

Current source calibration
~~~~~~~~~~~~~~~~~~~~~~~~~~

Current source calibration requires at least 3 data points - 0A, 100mA and -100mA. Channels A and B must be calibrated sequentially. The steps below describe the calibration procedure:

-  On the ADALM1000 device connect the CH A or CH B to one end of the resistor
-  Connect the other end of the resistor to the current input of a DMM
-  Connect the GND of the DMM to the ADALM1000 2.5V pin
-  In Pixelpulse set the mode of the channel to be calibrated to Source Current Measure Voltage
-  In Pixelpulse source 0A on the channel to be calibrated
-  Read the current measurement on the DMM
-  Replace into the calibration file in the **# Channel A/B, source I** sections the *<0.0000, 0.0000>* data pairs with *<pixelpulse_value, dmm_value>*, where *pixelpulse_value* is the current source value in Pixelpulse and *dmm_value* is the measurement taken with the DMM
-  In Pixelpulse source 100mA on the channel to be calibrated
-  Read the current measurement on the DMM
-  Replace into the calibration file in the **# Channel A/B, source I** sections the *<0.1000, 0.1000>* data pairs with *<pixelpulse_value, dmm_value>*, where *pixelpulse_value* is the current source value in Pixelpulse and *dmm_value* is the measurement taken with the DMM
-  In Pixelpulse source -100mA on the channel to be calibrated
-  Read the current measurement on the DMM
-  Replace into the calibration file in the **# Channel A/B, source I** sections the *< -0.1000, -0.1000>* data pairs with *<pixelpulse_value, dmm_value>*, where *pixelpulse_value* is the current source value in Pixelpulse and *dmm_value* is the measurement taken with the DMM

Semi-automated Procedure
------------------------

The :doc:`ALICE 1.3 DeskTop Software </wiki-migration/university/tools/m1k/alice/self-calibration-user-guide>` includes a semi-automated method to calibrate the ADALM1000 using the AD584 precision 2.5 V reference from the ADALP2000 Analog Parts Kit. Just wire up an AD584 for a 2.5 V output, powered from the fixed 5V supply from the ALM1000 and follow the steps as outlined in the ALICE desktop user's guide. No DMM needed (except to maybe verify the output of the AD584).

.. |ADALM1000 default calibration file| image:: https://wiki.analog.com/_media/:git-libsmu:`contrib/calib`.txt
