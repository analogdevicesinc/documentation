Optical Platform: pH Measurement Demo
=====================================

Colorimetry can be used to determine the concentration of materials in a solution based on its absorbance. One application of colorimetry is pH measurement with the aid of a coloring reagent. This document details the steps in setting up the EVAL-CN0503-ARDZ for pH measurement.

General Description/Overview
----------------------------

| The EVAL-CN0503-ARDZ is a four-channel optical platform capable of fluorescence, absorbance and scattering measurements. The two middle channels/light paths are only capable of absorbance and 180-degree scattering measurements. This demo uses the two paths for absorbance measurements for two different light wavelengths.

| Measuring pH using colorimetry involves using a chemical reagent or indicator. Different indicators exhibit different color and light absorbance behavior. Some indicators break down into different ions which also exhibit different properties which is why the solution has very different color hues at the ends of the pH range. For this demo we will be using bromothymol blue from either a prepared solution or the API pH Test Kit. Bromothymol blue separates into a weak acid (HIn) and a conjugate base (In). HIn has high absorbance to 430nm light while In has high absorbance at 615nm light. The demo will use light sources with these two wavelengths for the two middle channels.

While bromothymol blue exhibits the most change in color in the 6 to 8 pH range, buffer solutions with known pH solutions can be used to set up the measurement/calibration curve. The demo uses the CN0503 GUI and details steps to set-up the pH measurement curve using a spreadsheet.

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  :adi:`CN0503`, completely assembled (see :doc:`Hardware User Guide </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0503>`)
-  :adi:`EVAL-ADICUP3029` with firmware (see :doc:`Software User Guide </wiki-migration/resources/eval/user-guides/eval-adicup3029/reference_designs/demo_cn0503>`)
-  Host computer with CN0503 software (see `Quick Setup Guide <https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/cn0503_gui_quick_start_guide.docx>`_) and Microsoft Excel (Optional for generating your own measurement curve)
-  Bromothymol blue or API pH Test Kit `API Fish Care pH Test Kit <https://apifishcare.com/product/ph-test-kit>`_)
-  pH Buffer Solutions (Optional for calibration)
-  Common household chemicals for testing (caustic soda, baking soda, vinegar, and distilled water)

Setting the EVAL-CN0503-ARDZ
----------------------------

Before starting with these steps, please check the :doc:`Hardware User Guide </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0503>` for the steps to assembling the :adi:`CN0503`. Additionally, please check the :doc:`Software User Guide </wiki-migration/resources/eval/user-guides/eval-adicup3029/reference_designs/demo_cn0503>` for the steps in setting up the firmware and the `Quick Setup Guide <https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/cn0503_gui_quick_start_guide.docx>`_ for running the software. This demo assumes that you already have an assembled board with a working firmware already programmed on the :adi:`EVAL-ADICUP3029` and a ready-to-run software in the host computer.

Configure the onboard jumper shunt connection as below:

=================== =========== =================
Jumper Header       Setting     Image
=================== =========== =================
*LD2SEL and LD3SEL* Set to VARD |image1|

|image2|

*IOSEL*             Set to ARD

|image3|

*P1.8V*             Shorted

|image4|

=================== =========== =================

Initial Connection and Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Connect the 430nm LED Board and the 615nm LED Board to LED2 and LED3, respectively.


|image5|

-  Connect the :adi:`EVAL-ADICUP3029` to the :adi:`CN0503` and connect a microUSB-to-USB cable from the board to the host computer.
-  Run the software (using python scripts or the executable, see the `Quick Setup Guide <https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/cn0503_gui_quick_start_guide.docx>`_) and wait for the main window to open.

|image6|

-  Click the Gear icon at the top right of the window to open Settings.

|image7|

-  Select the correct COM Port of the device and connect (see `Quick Setup Guide <https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/cn0503_gui_quick_start_guide.docx>`_ for help)

|image8|

-  Load the configuration file for pH Measurement (`cn0503_defaults_ph.zip <https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/cn0503_defaults_ph.zip>`_)
-  Configure the settings for path 2 and 3 with the desired name, set wavelengths to 430 and 615, respectively, and select measurement type: absorption for both.

|image9|

-  Add empty cuvette/s (or filled with distilled water) to the cuvette holder assembly and insert to path 2 and 3, and click Optimize LED for each path. This properly sets the LED current in these paths so that the light intensity is close to 50%.

|image10|

Setting a Baseline Ratio
~~~~~~~~~~~~~~~~~~~~~~~~

The baseline ratio is used to remove small factors introduced to the measurement such as by the optical glass elements, e.g. beam splitter, lens, and filters. The baseline ratio is the ARAT value of a known setups such as with an empty cuvette or distilled water sample where it is known that the ratio of incident and transmitted light should be approximately 1. This value is used as a reference for successive measurements which will be defined as the relative ratio RRAT.

-  Click OK on the settings window and on the main window select optical path 3 and display mode ARAT.


|image11|

-  Click on Start Measurement and note the average value on the graph. Remember the empty cuvette or distilled water sample should still be in the path. The average value will be used as the baseline ratio for this path.

|image12|

-  Click on Stop Measurement (Repeat the two previous steps for path 3) then, click on the settings icon on the top right corner to bring back the settings and click on Advanced to bring up the another window.

|image13|

-  In the "Enter a direct command" text field, type "DEF1 RATB <average value>" for path 2 and "DEF2 RATB <average value>" for path3, then press Send Command. Replace the <average value> to the value you have noted earlier.

|image14|

-  Optionally, you can write pH to the primary unit field of path 2 and path 3. These are just labels and are not necessary.

|image15|

-  Click Okay here and on the settings window to go back to the main. Remove the empty cuvette/s or distilled water sample/s. The device is now ready to measure pH.

Performing a pH Measurement
~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Place a prepared cuvette with the test sample to either path 2 and path 3. Check the Preparing Test Sample section on how to prepare a cuvette with the test sample and indicator.


|image16|

-  Select either path 2 or path 3, set display mode to INS1, and press Start Measurement.

|image17|

.. important::

   For quick demo purposes, the system was configured in path 3, by default, to use the measurement curve shown below. Check the :doc:`Generating a Measurement Curve </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0503/fluorescence>` section on how to set your own using spreadsheets and the advanced settings


Preparing Test Samples
----------------------

| Using colorimetry for pH measurement requires a reagent or indicator. The demo uses the API pH Test Kit which uses a reagent with hue similar to that of bromothymol blue. To prepare solutions in a cuvette for pH measurement with the CN0503, follow the steps outlined below.

-  If the cuvette was previously used, clean the cuvette with distilled water and let dry
-  Add the solution to be tested to the cuvette up to 3/4 of the line at the top.
-  Add one drop of from the API pH Test Kit dropper bottle.
-  Cap the cuvette tightly and turn it upside down at least 3 times to thoroughly mix the reagent with the solution.
-  If the solution in the cuvette has uniform color, it can now be used with the CN0503. Below is a photo of prepared samples from common household chemicals.

|image18|

Generating a Measurement Curve
------------------------------

| The pH measurement curve is a function which models the relationship of the absorbance of either the weak acid or conjugate base of the reagent used to the pH of the solution. You can generate your own measurement curve using samples with known pH. The CN0503 is capable of approximating this using a 5th order polynomial function.

.. important::

   While measurement curves use absorbance to measure pH, the CN0503 uses the relative ratio RRAT. RRAT is the absolute ratio (ARAT) of the transmitted light intensity to the incident light intensity, and divided by the baseline ratio. RRAT is related to absorbance using the equation below.

   | |image19|
   | It is possible to change the mathematical expression for the ARAT but this demo will stick to using the default


Using Microsoft Excel, it is easy to generate the measurement curve by following the steps outlined below.

-  Create list of the RRAT measurements of each sample and the known pH in 2 different columns.


|image20|

   -  To get the RRAT measurement of a solution, select either path 2 or 3 and RRAT in the display units, and click Start Measurement


   |image21|

   -  Use the average or median of the measurement values.

-  Create a scatter plot of of the two columns with RRAT as the X-variable and pH as the y-Variable


|image22|

-  Create a trend-line for the scatter plot and select the polynomial option with an order of up to 5. Also, check the box at the bottom to Display Equation on chart

|image23|

-  Use the equation of the trendline and input the coefficients to the CN0503 using the Command field in the Advanced settings. See the :doc:`Software User Guide </wiki-migration/resources/eval/user-guides/eval-adicup3029/reference_designs/demo_cn0503>` for details on the command.

|image24|

Reference Links
---------------

-  :doc:`Hardware User Guide </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0503>`
-  :doc:`Software User Guide </wiki-migration/resources/eval/user-guides/eval-adicup3029/reference_designs/demo_cn0503>`
-  `Quick Setup Guide <https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/cn0503_gui_quick_start_guide.docx>`_

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/ld2sel_-_ard.png
   :width: 100px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/ld3sel_-_ard.png
   :width: 100px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/iosel_-_ard.png
   :width: 100px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/p1.8v_-_ard.png
   :width: 100px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/ph_ledplacement.jpg
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/ph_mainwindow.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/ph_opensettings.png
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/ph_clickconnect.png
   :width: 600px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/ph_pathsetting.png
   :width: 600px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/ph_emptycuvette.jpg
   :width: 600px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/ph_arat.png
   :width: 600px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/ph_arataverage.png
   :width: 600px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/ph_stopandadvance.png
   :width: 600px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/ph_ratb.png
   :width: 600px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/ph_unit.png
   :width: 600px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/ph_samples.png
   :width: 600px
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/ph_curve.png
   :width: 600px
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/ph_solutions.jpg
   :width: 600px
.. |image19| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/ph_rratabsorbance.png
   :width: 400px
.. |image20| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/ph_excelrrat.png
   :width: 200px
.. |image21| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/ph_rrat.png
   :width: 600px
.. |image22| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/ph_curve.png
   :width: 600px
.. |image23| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/ph_trendline.png
   :width: 400px
.. |image24| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/ph_polycommand.png
   :width: 600px
