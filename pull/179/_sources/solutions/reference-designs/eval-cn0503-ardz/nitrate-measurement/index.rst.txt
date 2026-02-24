.. _nitrate-measurement:

Nitrate Measurement Demo
=========================

The scientific method of colorimetry uses the Beer-Lambert law, which indicates
that a solute’s concentration is proportional to absorbance, to determine the
concentration of colored compounds in solutions. Nitrate measurement with a
coloring reagent is one use for colorimetry. The procedure for setting the
EVAL-CN0503-ARDZ for nitrate measurement is described in this page.

General Description
-------------------

The four-channel optical platform EVAL-CN0503-ARDZ can monitor fluorescence,
absorbance, and scattering. The only measurements that can be made using the two
middle channels/light streams are absorbance and 180-degree scattering. In this
demonstration, there is only one path used to evaluate absorbance for a single
light wavelength.

A chemical reagent or indicator is required for measuring nitrate using
colorimetry. Different indicators display varying color and light absorption
patterns. The solution exhibits highly different color hues at the ends of the
nitrate range because some indicators break down into various ions that have
different characteristics. The Nitrate (NO3-) Test Kit, which includes two
solutions, will be used for this demonstration. The mixture will turn yellow
when Solution 1 is added, while Solution 2 includes test chemicals that produce
all various color shades. Visual estimation or spectrophotometric measurement in
the range of 4 to 40 mg/L at λmax 400 nm can be used to determine the nitrate
concentration. As a result, the third path of the CN0503 will be illuminated by
a light source with a wavelength of 530 nm in this demonstration.

While buffer solutions with known Nitrate solutions can be used to set up the
measurement/calibration curve, the Nitrate (NO3-) Test Kit exhibits the greatest
change in color in the 40 to 100 mg/L range. The demo sets up the nitrate
measurement curve using a spreadsheet and makes use of the CN0503 GUI.

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

- :adi:`CN0503`, completely assembled (see :ref:`Hardware User Guide <eval-cn0503-ardz>`)
- :adi:`EVAL-ADICUP3029` with firmware (see :ref:`Software User Guide <cn0503-software>`)
- Host computer with CN0503 software (Optional for setting up computation of concentration)
- Nitrate Chemical (This demo uses Calcium Nitrate)
- Nitrate Test Kit (API Fish Care Nitrate Test Kit)
- Nitrate Buffer Solutions (Optional for calibration)

Setting the EVAL-CN0503-ARDZ
----------------------------

Before starting with these steps, please check the :ref:`Hardware User Guide
<eval-cn0503-ardz>` for the steps to assemble the CN0503. Additionally, please
check the :ref:`Software User Guide <cn0503-software>` for the steps in setting
up the firmware and the :download:`Quick Setup Guide <cn0503_gui_quick_start_guide.docx>`
for running the software. This demo assumes that you already have an assembled
board with a working firmware already programmed on the :adi:`EVAL-ADICUP3029`
and a ready-to-run software in the host computer.

Configure the onboard jumper shunt connection as below:

+-----------------------+----------------+-----------------------------+
| Jumper Header         | Setting        | Image                       |
+=======================+================+=============================+
| *LD2SEL and LD3SEL*   | Set to VARD    | .. image:: ld2sel-ard.png   |
+-----------------------+----------------+-----------------------------+
| *IOSEL*               | Set to ARD     | .. image:: iosel-ard.png    |
+-----------------------+----------------+-----------------------------+
| *P1.8V*               | Shorted        | .. image:: p1.8v-ard.png    |
+-----------------------+----------------+-----------------------------+

Initial Connection and Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Connect the 530nm LED Board to LED3.

   .. image:: nitrate_led_placement.png

#. Connect the :adi:`EVAL-ADICUP3029` to the :adi:`CN0503`
   and connect a microUSB-to-USB cable from the board to
   the host computer.
#. Run the software (using python scripts or the executable,
   see the :download:`Quick Setup Guide <cn0503_gui_quick_start_guide.docx>`)
   and wait for the main window to open.

   .. image:: ph_mainwindow.png

#. Click the Gear icon at the top right of the window to open Settings.

   .. image:: nitrate_open_settings.png

   - Select the correct COM Port of the device and connect
     (see :download:`Quick Setup Guide <cn0503_gui_quick_start_guide.docx>` for help)

     .. image:: nitrate_click_connect.png

#. Load the configuration file for Nitrate Measurement: :download:`cn0503_defaults_nitrate.zip`

#. Configure the settings for path 3 with the desired name, set wavelength to
   530nm and select measurement type: Absorption.

   .. image:: nitrate_path_setting.png

#. Add empty cuvette (or filled with distilled water) to the cuvette holder
   assembly and insert to path 3 and click ``Optimize LED``. This properly sets the
   LED current in this path so that the light intensity is close to 50%.

   .. image:: nitrate_empty_cuvette.png

Setting a Baseline Ratio
-------------------------

The baseline ratio is used to remove small
factors introduced to the measurement by the optical glass elements, such as
beam splitter, lens, and filters. The baseline ratio is the ARAT value of a
known setups such as with an empty cuvette or distilled water sample where it
is known that the ratio of incident and transmitted light should be
approximately 1. This value is used as a reference for successive measurements
which will be defined as the relative ratio RRAT.

#. Click ``OK`` on the settings window and on the main window select optical path 3
   and display mode ARAT.

   .. image:: nitarte_arat1.png

#. Click on ``Start Measurement`` and note the average value on the graph.
   Remember that the solution should still be in the path. The average value
   will be used as the baseline ratio for this path.

   .. image:: nitrate_average_value.png

#. Record the average value and click on ``Stop Measurement`` then, click on the
   settings icon on the top right corner to bring back the settings and click on
   Advanced to bring up another window.

   .. image:: nitarte_stop-and-advance.png

#. In the “Enter a direct command” text field, type “DEF1 RATB <average
   value>” for path 3, then press ``Send Command``. Replace the <average value> to
   the value you have noted earlier and click ``Okay``.

   .. image:: nitrate_ratb.png

#. Optionally, you can write mg/L to the primary unit field of path 3. These
   are just labels and are not necessary.

   .. image:: nitrate_unit.png

#. Click ``Okay`` here and on the settings window to go back to the main. Remove
   the empty cuvette/s or distilled water sample/s. The device is now ready to
   measure Nitrate.

Performing a Nitrate Measurement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Place a prepared cuvette with the test sample to path 3. Check the Preparing
   Test Sample section on how to prepare a cuvette with the test sample and
   indicator.

   .. image:: nitrate_sample.png

#. Select path 3, set display mode to INS1, and press ``Start Measurement``.

   .. image:: nitrate_curve.png

Preparing Test Samples
----------------------

Using colorimetry for Nitrate measurement requires a reagent or indicator. The
demo uses the API Nitrate Test Kit which uses two test solutions. To prepare
solutions in a cuvette for Nitrate measurement with the CN0503, follow the steps
outlined below.

#. If the cuvette has previously been used, clean it with distilled water and
   allow it to dry.
#. Dissolve known amounts of Nitrate in a liter of water. Refer to the color
   guide included with the API test kit.

   .. image:: nitrate_color_guide.jpg

#. Pour a 5ml Nitrate solution onto the test tube provided in the API test kit
   once the Nitrate has been fully dissolved.
#. Add 10 drops of Solution #1 to the mixture and shake to combine.
#. Before adding 10 drops to the test tube, vigorously shake Solution #2 for 30
   seconds to break down particles.
#. Shake the test tube upside down for 1 minute to combine the solution to the
   mixture, then set it aside for 5 minutes before pouring it into the cuvettes.
#. Cap the cuvettes, and if the mixture in the cuvette matches the color guide
   uniformly, it can now be used with the CN0503. A photo of prepared samples
   from various levels of Nitrate is shown below.

   .. image:: nitrate_test_samples.png

Generating a Measurement
------------------------

The Nitrate measurement curve is a function which models the characteristic
curve of the different levels of Nitrate present in the mixture. You can
generate your own measurement curve using samples with known Nitrate. The
CN0503 is capable of approximating this using a 5th order polynomial function.

.. important::

   While measurement curves use absorbance to measure pH, the
   CN0503 uses the relative ratio RRAT. RRAT is the absolute ratio (ARAT) of the
   transmitted light intensity to the incident light intensity and divided by the
   baseline ratio. RRAT is related to absorbance using the equation below.

   .. image:: ph_rratabsorbance.png

   It is possible to change the mathematical expression for the ARAT but this
   demo will stick to using the default.

Using Microsoft Excel, it is easy to generate the measurement curve by following
the steps outlined below.

#. Create list of the RRAT measurements of each sample and the known Nitrate in
   a column.

   .. image:: nitrate_curve_table.png

   - To get the RRAT measurement of a solution, select 3 and RRAT in the
     display units, and click ``Start Measurement``.
   - Use the average or median of the measurement values.

#. Create a scatter plot of the two columns with RRAT as the X-variable and
   Nitrate level as the Y-variable.

   .. image:: nitrate_curve.png

   - Create a trend-line for the scatter plot and select the polynomial option
     with an order of up to 5 depending on characteristic of the curve. Also,
     check the box at the bottom to Display Equation on chart.

     .. image:: nitrate_trendline_options.png

   - Use the equation of the trendline and input the coefficients to the CN0503
     using the Command field in the Advanced settings. See the
     :ref:`Software User Guide <cn0503-software>` for details on the command.

     .. image:: nitrate_direct_command.png

Reference Links
---------------

- :ref:`Hardware User Guide <eval-cn0503-ardz>`
- :ref:`Software User Guide <cn0503-software>`
- :download:`Quick Setup Guide <cn0503_gui_quick_start_guide.docx>`
