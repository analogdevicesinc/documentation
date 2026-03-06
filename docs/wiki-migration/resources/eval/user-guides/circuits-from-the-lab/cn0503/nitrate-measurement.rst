Optical Platform: Nitrate Measurement Demo
==========================================

The scientific method of colorimetry uses the Beer-Lambert law, which indicates that a solute's concentration is proportional to absorbance, to determine the concentration of colored compounds in solutions. Nitrate measurement with a coloring reagent is one use for colorimetry. The procedure for setting the EVAL-CN0503-ARDZ for nitrate measurement is described in this document.

General Description
-------------------

The four-channel optical platform EVAL-CN0503-ARDZ can monitor fluorescence, absorbance, and scattering. The only measurements that can be made using the two middle channels/light streams are absorbance and 180-degree scattering. In this demonstration, there is only one path used to evaluate absorbance for a single light wavelength.

A chemical reagent or indicator is required for measuring nitrate using colorimetry. Different indicators display varying color and light absorption patterns. The solution exhibits highly different color hues at the ends of the nitrate range because some indicators break down into various ions that have different characteristics. The Nitrate (NO3-) Test Kit, which includes two solutions, will be used for this demonstration. The mixture will turn yellow when Solution 1 is added, while Solution 2 includes test chemicals that produce all various color shades. Visual estimation or spectrophotometric measurement in the range of 4-40 mg/L at λmax 400 nm can be used to determine the nitrate concentration. As a result, the third path of the CN0503 will be illuminated by a light source with a wavelength of 530 nm in this demonstration.

While buffer solutions with known Nitrate solutions can be used to set up the measurement/calibration curve, the Nitrate (NO3-) Test Kit exhibits the greatest change in color in the 40 to 100 mg/L range. The demo sets up the nitrate measurement curve using a spreadsheet and makes use of the CN0503 GUI.

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  CN0503, completely assembled (see :doc:`Hardware User Guide </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0503>`)
-  EVAL-ADICUP3029 with firmware (see :doc:`Software User Guide </wiki-migration/resources/eval/user-guides/eval-adicup3029/reference_designs/demo_cn0503>`)
-  Host computer with CN0503 software (see `Quick Setup Guide <https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/cn0503_gui_quick_start_guide.docx>`__) and Microsoft Excel (Optional for setting up computation of concentration)
-  Nitrate Chemical (This demo uses Calcium Nitrate)
-  Nitrate Test Kit (API Fish Care Nitrate Test Kit)
-  Nitrate Buffer Solutions (Optional for calibration)

Setting the EVAL-CN0503-ARDZ
----------------------------

Before starting with these steps, please check the :doc:`Hardware User Guide </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0503>` for the steps to assemble the CN0503. Additionally, please check the :doc:`Software User Guide </wiki-migration/resources/eval/user-guides/eval-adicup3029/reference_designs/demo_cn0503>` for the steps in setting up the firmware and the `Quick Setup Guide <https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/cn0503_gui_quick_start_guide.docx>`__ for running the software. This demo assumes that you already have an assembled board with a working firmware already programmed on the :adi:`EVAL-ADICUP3029` and a ready-to-run software in the host computer.

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

-  Connect the 530nm LED Board to LED3.


|image5|

-  Connect the :adi:`EVAL-ADICUP3029` to the :adi:`CN0503` and connect a microUSB-to-USB cable from the board to the host computer.
-  Run the software (using python scripts or the executable, see the `Quick Setup Guide <https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/cn0503_gui_quick_start_guide.docx>`__) and wait for the main window to open.

|image6|

-  Click the Gear icon at the top right of the window to open Settings.

|image7|

   \* Select the correct COM Port of the device and connect (see `Quick Setup Guide <https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/cn0503_gui_quick_start_guide.docx>`__ for help)

   |image8|

-  Load the configuration file for Nitrate Measurement `cn0503_defaults_nitrate.zip <https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/cn0503_defaults_nitrate.zip>`__
   \* Configure the settings for path 3 with the desired name, set wavelength to 530 nm and select measurement type: absorption.

   |image9|

-  Add empty cuvette (or filled with distilled water) to the cuvette holder assembly and insert to path 3 and click Optimize LED. This properly sets the LED current in this path so that the light intensity is close to 50%.

|image10|

| 
| ==== Setting a Baseline Ratio ==== The baseline ratio is used to remove small factors introduced to the measurement by the optical glass elements, such as beam splitter, lens, and filters. The baseline ratio is the ARAT value of a known setups such as with an empty cuvette or distilled water sample where it is known that the ratio of incident and transmitted light should be approximately 1. This value is used as a reference for successive measurements which will be defined as the relative ratio RRAT.

-  Click OK on the settings window and on the main window select optical path 3 and display mode ARAT.


|image11|

   \* Click on Start Measurement and note the average value on the graph. Remember that the solution should still be in the path. The average value will be used as the baseline ratio for this path.

   |image12|

   \* Record the average value and click on Stop Measurement then, click on the settings icon on the top right corner to bring back the settings and click on Advanced to bring up another window.

   |image13|

   \* In the “Enter a direct command” text field, type “DEF1 RATB <average value>” for path 3, then press Send Command. Replace the <average value> to the value you have noted earlier and click ok.

   |image14|

   \* Optionally, you can write mg/L to the primary unit field of path 3. These are just labels and are not necessary.

   |image15|

   \* Click Okay here and on the settings window to go back to the main. Remove the empty cuvette/s or distilled water sample/s. The device is now ready to measure Nitrate.

| 

Performing a Nitrate Measurement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Place a prepared cuvette with the test sample to path 3. Check the Preparing Test Sample section on how to prepare a cuvette with the test sample and indicator.


|image16|

   \* Select path 3, set display mode to INS1, and press Start Measurement.

   |image17|

| 

Preparing Test Samples
----------------------

Using colorimetry for Nitrate measurement requires a reagent or indicator. The demo uses the API Nitrate Test Kit which uses two test solutions. To prepare solutions in a cuvette for Nitrate measurement with the CN0503, follow the steps outlined below.

-  If the cuvette has previously been used, clean it with distilled water and allow it to dry.
-  Dissolve known amounts of Nitrate in a liter of water. Refer to the color guide included with the API test kit.

|image18|

-  Pour a 5 ml Nitrate solution onto the test tube provided in the API test kit once the Nitrate has been fully dissolved.
-  Add 10 drops of Solution #1 to the mixture and shake to combine.
-  Before adding 10 drops to the test tube, vigorously shake Solution #2 for 30 seconds to break down particles.
-  Shake the test tube upside down for 1 minute to combine the solution to the mixture, then set it aside for 5 minutes before pouring it into the cuvettes.
-  Cap the cuvettes, and if the mixture in the cuvette matches the color guide uniformly, it can now be used with the CN0503. A photo of prepared samples from various levels of Nitrate is shown below.

|image19|

| 

Generating a Measurement
------------------------

| The Nitrate measurement curve is a function which models the characteristic curve of the different levels of Nitrate present in the mixture. You can generate your own measurement curve using samples with known Nitrate. The CN0503 is capable of approximating this using a 5th order polynomial function.

.. important::

   While measurement curves use absorbance to measure pH, the CN0503 uses the relative ratio RRAT. RRAT is the absolute ratio (ARAT) of the transmitted light intensity to the incident light intensity and divided by the baseline ratio. RRAT is related to absorbance using the equation below.


   |image20|

   | It is possible to change the mathematical expression for the ARAT but this demo will stick to using the default


Using Microsoft Excel, it is easy to generate the measurement curve by following the steps outlined below.

-  Create list of the RRAT measurements of each sample and the known Nitrate in a column.


|image21|

   \* To get the RRAT measurement of a solution, select 3 and RRAT in the display units, and click Start Measurement
   \* Use the average or median of the measurement values.
-  Create a scatter plot of the two columns with RRAT as the X-variable and Nitrate level as the y-Variable

|image22|

   \* Create a trend-line for the scatter plot and select the polynomial option with an order of up to 5 depending on characteristic of the curve. Also, check the box at the bottom to Display Equation on chart.

   |image23|

   \* Use the equation of the trendline and input the coefficients to the CN0503 using the Command field in the Advanced settings. See the :doc:`Software User Guide </wiki-migration/resources/eval/user-guides/eval-adicup3029/reference_designs/demo_cn0503>` for details on the command.

   |image24|

| 
| ===== Reference Links =====

-  :doc:`Hardware User Guide </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0503>`
-  :doc:`Software User Guide </wiki-migration/resources/eval/user-guides/eval-adicup3029/reference_designs/demo_cn0503>`
-  `Quick Setup Guide <https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/cn0503_gui_quick_start_guide.docx>`__

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/ld2sel_-_ard.png
   :width: 100px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/ld3sel_-_ard.png
   :width: 100px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/iosel_-_ard.png
   :width: 100px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/p1.8v_-_ard.png
   :width: 100px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/nitrate_led_placement.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/ph_mainwindow.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/nitrate_open_settings.png
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/nitrate_click_connect.png
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/nitrate_path_setting.png
   :width: 200px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/nitrate_empty_cuvette.png
   :width: 600px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/nitarte_arat1.png
   :width: 600px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/nitrate_average_value.png
   :width: 600px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/nitarte_stop-and-advance.png
   :width: 600px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/nitrate_ratb.png
   :width: 600px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/nitrate_unit.png
   :width: 600px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/nitrate_sample.png
   :width: 600px
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/nitrate_curve.png
   :width: 600px
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/nitrate_color_guide.jpg
   :width: 600px
.. |image19| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/nitrate_test_samples.png
   :width: 600px
.. |image20| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/ph_rratabsorbance.png
   :width: 400px
.. |image21| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/nitrate_curve_table.png
   :width: 200px
.. |image22| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/nitrate_curve.png
   :width: 600px
.. |image23| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/nitrate_trendline_options.png
   :width: 400px
.. |image24| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0503/nitrate_direct_command.png
   :width: 600px
