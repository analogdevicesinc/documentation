Optical Platform: Turbidity Measurement Demo
============================================

An important water quality indicator for almost any use is the presence of dispersed, suspended solids—particles not in true solution (often including silt, clay, algae, other microorganisms, organic matter, and other minute particles). Turbidity is a qualitative characteristic imparted by how these suspended solids obstruct the transmittance of light. Turbidity is not a direct measure of suspended particles in water but rather a measure of the scattering effect such particles have on light.

General Description/Overview
----------------------------

| The EVAL-CN0503-ARDZ is a four-channel optical platform capable of fluorescence, absorbance and scattering measurements. The two middle channels/light paths are only capable of absorbance and 180-degree scattering measurements. This demo uses one of the side paths for 90- and 180-degree scattering measurements.

| Turbidity measurements follow design standards requiring specific types of light sources and number and angle of detectors. One of the standards is ISO7027 Water Quality - Determination of Turbidity which requires a monochromatic light source usually an IR LED, and a primary detector at a 90-degree angle. The demo will follow the standard using a single 940nm LED and two detectors at 90- and 180-degree angles. The unit for turbidity under the standard is FTU and the CN0503 computes this using 2 linear approximations (for low and high turbidity measurements) obtained from a 3-point calibration.

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  :adi:`CN0503`, completely assembled (see :doc:`Hardware User Guide </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0503>`)
-  :adi:`EVAL-ADICUP3029` with firmware (see :doc:`Software User Guide </wiki-migration/resources/eval/user-guides/eval-adicup3029/reference_designs/demo_cn0503>`)
-  Host computer with CN0503 software (see `Quick Setup Guide <https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/cn0503_gui_quick_start_guide.docx>`_) and Microsoft Excel (Optional for computing the parameters of the linear approximation)
-  Lumileds Luxeon IR Compact 940nm LED L1IZ-0940000000000 (https://www.digikey.com/en/products/detail/lumileds/L1IZ-0940000000000/7243419)
-  Oakton T100 calibration kit (Optional for calibration) (https://www.amazon.com/Oakton-AO-35635-52-Replacement-Turbidity-Calibration/dp/B00DDOW1JS)
-  Test solutions (common household liquids, such as milk, mixed with water or cement slurry water)

Assembling the 940nm LED
~~~~~~~~~~~~~~~~~~~~~~~~

| The default options for the LED sources do not include infrared wavelength. Spare Lumiled and Lite-on LED boards are available for users to mount custom LEDs. The demo uses the Lumiled Luxeon IR Compact Series 940nm LED.
| |image1|

Setting the EVAL-CN0503-ARDZ
----------------------------

Before starting with these steps, please check the :doc:`Hardware User Guide </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0503>` for the steps to assembling the :adi:`CN0503`. Additionally, please check the :doc:`Software User Guide </wiki-migration/resources/eval/user-guides/eval-adicup3029/reference_designs/demo_cn0503>` for the steps in setting up the firmware and the `Quick Setup Guide <https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/cn0503_gui_quick_start_guide.docx>`_ for running the software. This demo assumes that you already have an assembled board with a working firmware already programmed on the :adi:`EVAL-ADICUP3029` and a ready-to-run software in the host computer.

Configure the onboard jumper shunt connection as below:

============= =========== ========
Jumper Header Setting     Image
============= =========== ========
*LD4SEL*      Set to VARD

|image2|

*IOSEL*       Set to ARD

|image3|

*P1.8V*       Shorted

|image4|

============= =========== ========

.. important::

   You can use either path 1 or 4 for turbidity measurements. The steps outlined here will use path 4, and setting LED4, P4ASEL, and P4BSEL.


-  Connect the 940nm LED Board to LED4



|image5|

-  Remove the fluorescent filter, if present, from the slot shown below:

|image6|

-  Set the jumper headers P4ASEL and P4BSEL as instructed in the table below:

============= ============ ========
Jumper Header Setting      Image
============= ============ ========
*P4ASEL*      Set to 0DEG

|image7|

*P4BSEL*      Set to 90DEG

|image8|

============= ============ ========

Initial Connection and Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Connect the :adi:`EVAL-ADICUP3029` to the :adi:`CN0503` and connect a microUSB-to-USB cable from the board to the host computer.
-  Run the software (using python scripts or the executable, see the `Quick Setup Guide <https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/cn0503_gui_quick_start_guide.docx>`_) and wait for the main window to open.

|image9|

-  Click the Gear icon at the top right of the window to open Settings.

|image10|

-  Select the correct COM Port of the device and connect (see `Quick Setup Guide <https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/cn0503_gui_quick_start_guide.docx>`_ for help)

|image11|

-  Load the configuration file for pH Measurement (`cn0503_defaults_turbidity.zip <https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/cn0503_defaults_turbidity.zip>`_)
-  Configure the settings for path 4 with the desired name, set wavelength to 940nm, and select measurement type: turbidity.

|image12|

-  Add empty an cuvette (or filled with distilled water) to the cuvette holder assembly and insert to path 4. Click Optimize LED for path 4. This properly sets the LED current in these paths so that the light intensity is close to 50%.

|image13|

-  Remove the cuvette and click Okay to return to the Main Window.

Linear Approximation using 3-Point Calibration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Turbidity measurement is sensitive to multiple factors including ambient light and particulate contamination of samples. A pseudo-three-point calibration routine allows for high precision turbidity measurements.

-  Fill three different cuvettes with the 20, 100, and 800 FTU calibration solutions up to the level marking as shown below.


|image14|

-  Go to the main window of the application and set the optical path to RRAT and the click on Start Measurement.

|image15|

-  Note the average value of the RRAT measured from the samples and stop measurement.
   |image16|\ |image17|\ |image18|
-  Two linear equations can be computed from the three turbidity (FTU) and average RRAT data points using the slope formula and point-slope form.

|image19|

-  You can also use this Excel file (`turbidity_calibration.xlsx <https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/turbidity_calibration.xlsx>`_) which plots the calibration points and generates a linear equation from a trendline.

|image20|

.. important::

   You can include more calibration points in the Excel table for both high and low turbidity ranges


-  To use the linear approximation, go to the Settings Window then, the Advanced Settings Window. In the command field, enter the coefficients of the linear approximation following the syntax: *DEF3 INS1 <x-intercept> <slope>*



|image21|

.. important::

   You can only use one linear approximation at a time using INS1. Select the measurement range best fitted for the liquid sample. You can also start with using the low turbidity range first before switching to the high turbidity measurement when the measured value is greater than 100 FTU


Performing a Turbidity Measurement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Set the INS1 polynomial to the linear approximation for either low or high turbidity measurement. If you are unsure of the turbidity range of the sample, choose the low turbidity range and check if the measurement is greater than 100 FTU. If it is, set the INS polynomial to the linear approximation for high turbidity measurements.


|image22|

-  Place a prepared cuvette with the test sample to either path 4. The liquid sample should reach up to the marking as detailed in the :doc:`Linear Approximation using 3-Point Calibration </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0503/turbidity>` section.

|image23|

-  Go back to the Main Window by clicking Okay to both the Advanced Settings and Settings. Select path 4 and, set display mode to INS1, and press Start Measurement.

|image24|

|

.. important::

   Optionally, you can set the unit displayed in the plot to FTU by writing this in the primary unit field of path 4 found by clicking the Advanced button in the Settings window.

   | |image25|\


Reference Links
---------------

-  :doc:`Hardware User Guide </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0503>`
-  :doc:`Software User Guide </wiki-migration/resources/eval/user-guides/eval-adicup3029/reference_designs/demo_cn0503>`
-  `Quick Setup Guide <https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/cn0503_gui_quick_start_guide.docx>`_

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/940nm_assembly.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/ld4sel_-_ard.png
   :width: 100px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/iosel_-_ard.png
   :width: 100px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/p1.8v_-_ard.png
   :width: 100px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/tr_940nm.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/fl_fluorescentfilter.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/p4asel_-_0.png
   :width: 100px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/p4bsel_-_90.png
   :width: 100px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/ph_mainwindow.png
   :width: 600px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/ph_opensettings.png
   :width: 600px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/tr_selectcom.png
   :width: 600px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/tr_wavelength.png
   :width: 200px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/tr_optimizeled.png
   :width: 600px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/tr_level.png
   :width: 600px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/tr_calstart.png
   :width: 600px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/tr_20ftu.png
   :width: 200px
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/tr_100ftu.png
   :width: 200px
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/tr_800ftu.png
   :width: 200px
.. |image19| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/tr_eqtn.png
   :width: 400px
.. |image20| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/tr_calplot.png
   :width: 600px
.. |image21| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/tr_polylincmd.png
   :width: 600px
.. |image22| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/tr_polylincmd.png
   :width: 600px
.. |image23| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/tr_sample.png
   :width: 600px
.. |image24| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/tr_meas.png
   :width: 600px
.. |image25| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/tr_unit.png
   :width: 600px
