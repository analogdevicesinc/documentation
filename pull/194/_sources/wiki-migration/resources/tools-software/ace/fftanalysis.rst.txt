FFT Analysis Features
=====================

ACE includes the ability for plug-ins to use a full-featured FFT analyzer. The details of the implementation and the specific user interface depend on the plug-in for a specific product, but the AD9208 will be used to demonstrate the features of the analyzer.

Running Analysis and Viewing the Results
----------------------------------------

The FFT can be run in "Run Once" or "Run Continous" modes. With the "Run Once" mode the capture history will be stored and the user can navigate to previous captures and their associated analysis. The currently selected analysis can be re-run allowing the user to change the values in the Analysis Settings Wizard.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/run_buttons.png
   :alt: Buttons to initiate analyses
   :width: 400px

Setting the fundamentals
------------------------

There are three modes available for finding the fundamentals, for the AD9208 these can be set in the Analysis Wizard.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/fundamental_provider_options.png
   :alt: FundametnalProvider Options
   :width: 400px

-  Highest Bin - Set the fundamentals to the highest spurs. This is the legacy behavior and a good

default

-  Mirror Image - Set spurs to the highest bin of the values in the Analysis Wizard and their mirror images.
-  Fixed - Set spurs locations in the Analysis Wizard.

Adjusting Window and Spectral Leakage Compensation
--------------------------------------------------

For non-coherent signals it is necessary to apply a windowing function. However, windowing causes spectral spreading around the spurs, requiring spectral leakage compensation. ACE performs windowing and spectral leakage compensation by default for the AD9208 using the recommended settings, however the user is able to modify these settings if there are specific requirements.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/spectral_leakage_compensation_settings.png
   :alt: Spectral Leakage Compensation Settings
   :width: 400px

Two Tone Analysis
-----------------

Two tone analysis will automatically find the two highest spurs and set them as fundamentals. The harmonics and inter-modulation distortion spurs will be found automatically. Only the spurs above the noise floor will be marked.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/two_tone.png
   :alt: Enabling Two Tone Analysis
   :width: 400px

Averaging FFT
-------------

The FFT analysis can only be run in "Run Continuous" mode. The graph view will show a countdown as the required samples are captured, and a FFT spectrum will be displayed once the data is valid. You can stop the "Run Continuous" capture and inspect or export the data when desired.

To save memory, you can de-select the Averaging FFT when it is not needed using the checkbox next to the AveragingFFT icon.\


|Averaging|

Setting Custom Spurs
--------------------

To open the dialog where you can add your own spurs to the analysis, click on the "Dynamic Settings" button on the bottom of the Analysis Wizard.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/dynamic_settings_btn.png
   :alt: Dynamic Settings Button
   :width: 200px

The spurs are separate for each type of FFT analysis available in the plug-in and can be focused by selecting the tabs on the left side of the dialog. There are several columns that can be used to describe the location and the way the analysis will handle the spur.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/custom_spurs.png
   :alt: Custom Spurs Dialog
   :align: center
   :width: 800px

Frequency
~~~~~~~~~

This can be a number entered in MHz or an equation that includes spur names. The names must be in the following format:

-  Start with a "-" if it is an image.
-  A "2" if it is related to the second fundamental
-  F
-  The multiplier

Following these rules the first fundamental would be F1 and the second fundamental would be F2. You can use standard operations including "^" for exponents as well as parentheses to force the order of operations.

Additional Examples:

-  "F1 - 20" -> This is the first fundamental minus 20 MHz.
-  "2F2 + 20" -> This is the second harmonic of the second fundamental plus 20 MHz.
-  "-F2" -> This is the image of the second harmonic of the first fundamental

Single Side Band
~~~~~~~~~~~~~~~~

If the Units setting is "Bins", then this is the number of bins that will be used on each side of the center bin when calculating the power of the spur with spectral leakage compensation. If the Units setting is set to "MHz" then this value will be the number of MHz on each side of the center bin to use when calculating the power of the spur with spectral leakage compensation.

Is Excluded From Noise
~~~~~~~~~~~~~~~~~~~~~~

If this box is checked, then the spur will be added to the FFT analysis, therefore affecting the calculation for noise and everything derived from it. If this box is unchecked, then the power of the spur will be reported, but it will not affect the other analysis results in any way.

Is Enabled
~~~~~~~~~~

This will disable the spur if unchecked, so that the spur information can be saved, but not used in the next analysis. If there are no custom spurs defined or enabled, then the Worst Other spur will be reported, but if there are any custom spurs in the analysis, the Worst Other will not be reported because it is assumed that the user is taking control of what to measure in addition to the standard analysis.

.. |Averaging| image:: https://wiki.analog.com/_media/resources/tools-software/ace/averaging.png
   :width: 400px
