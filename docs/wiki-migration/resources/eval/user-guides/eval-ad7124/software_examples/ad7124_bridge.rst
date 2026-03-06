4 Wire Bridge Demo
==================

Hardware Set-up
---------------

Requirements
~~~~~~~~~~~~

-  Eval+ software installed and open
-  AD7124-4/AD7124-8 evaluation board
-  System demonstration platform board (EVAL-SDP-CB1Z)
-  USB cable
-  PC running Windows with USB 2.0 port
-  Sensor voltage measured across AIN2-AIN3
-  <fc #ff0000> LOAD CELL: TEDEA HUNTLEIGH 505H-0002-F070 </fc>
-   \* AD3303 3.3V Low Dropout Linear Regulator

The configuration for the weigh bridge circuit is shown below. The 3.3V is supplied by the regulator to the top of the weigh bridge and to AVDD, the bottom of the weigh bridge is connected to <fc #ff0000>GND</fc>. The voltage difference between the left and right side of the weigh bridge is sensed across AIN2 and AIN3. In this configuration the voltage difference reflects the resistance change in R1 which is caused by the application of a weight to the sensor. The Reference pins are connected to <fc #ff0000>EXC+ and EXC-</fc>

Jumper positions
~~~~~~~~~~~~~~~~

**<fc #ff0000>To be confirmed</fc>**

See layout below for jumper locations

-  **LK1** noise test jumper must be **removed**.
-  **LK4** jumper between REFIN- and AVss must be **removed**.
-  **LK5** is used to apply external 2.5V or internal 2.5V to REFIN+ must be **removed**.

All other jumpers in their default positions, see `Hardware Link Options <https://wiki.analog.com/resources/eval/user-guides/eval-ad7124/eval-ad7124/hardware_guide/link_opt>`__


|image1|

Software
--------

Below details the procedure for setting up the Eval software to perform a weigh scale measurement. For information opening the Eval+ software see: `Launching the Software <https://wiki.analog.com/resources/eval/user-guides/eval-ad7124/software/launch_software>`__.

Once the software has been launched and the evaluation board is selected the, configuration tab of Eval+ software (shown below) should be displayed. For full information on the Eval+ software please go to the `Eval+ Guide <https://wiki.analog.com/resources/eval/user-guides/eval-ad7124/software/eval_plus>`__ section.

Weigh Scale (1)
~~~~~~~~~~~~~~~

In order to configure the evaluation board for the 2-wire RTD measurement demo, click the **Weigh Scale** button. This configures the device to the following settings:

Tutorial Access (2)
~~~~~~~~~~~~~~~~~~~

For quick access to the tutorial click the blue question mark icon next to the weigh scale button

Sampling mode (4)
~~~~~~~~~~~~~~~~~

-  Setting this to **single capture** causes a single batch of samples to be collected
-  Setting the program to **repeated capture** causes the software to continuously capture batches of samples from the ADC when sample is clicked.
-  Setting this to **data logging** causes the samples to be written to a file. Upon pressing sample in this mode, a dialog box will appear allowing the file name and save location to be set.

Required Samples (5)
~~~~~~~~~~~~~~~~~~~~

To select the number of samples required from the ADC in a batch, enter the value in the samples box. Default value is 100 samples.

Sample (6)
~~~~~~~~~~

The sample button sends the configuration to the evaluation board and initiates the data collection effort.

While the software is communicating with the board and retrieving the data, the window below will be displayed


|image2|

Waveform Tab
^^^^^^^^^^^^

Histogram Tab
^^^^^^^^^^^^^

Saving the conversion data
^^^^^^^^^^^^^^^^^^^^^^^^^^

To **save the conversion data** into an Excel file, right-click the waveform graph and select Export Data from the drop-down list that appears. A save dialog box displays, prompting the user to save the data to an appropriate folder location.

:doc:`Return to Software Examples </wiki-migration/resources/eval/user-guides/eval-ad7124/software_examples>`

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software_examples/eval_plus_layout_noise_test.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software_examples/eval_plus_test_underway.png
   :width: 400px
