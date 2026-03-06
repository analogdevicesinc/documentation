ADALM2000 Testing with Libm2k
=============================

A Python testing suite, based on libm2k. was developed in order to check the behaviour of the ADALM2000 module. By default, when running the test suite, a results directory is created, where all resulting files are stored: plots, csv and txt files(see examples below). The results of all tests are stored in a txt file and displayed on an html page, as well. If these files are not needed, one can opt to run the test suite without generating results files. The test suite can be found here - link. ! Provide link after merging tests |image1| |image2| |image3| Before running the test scripts, make sure all the required packages are installed. To do this, in your tests directory and type this:

::

   pip install -r requirements.txt

The tests are launched when running main.py. In the current working directory, a results directory is created. This contains:

-  HTML test report
-  plots
-  .csv files with data used to plot the signals
-  .txt file with results used in the tests

To suppress the generation of output files, add the “nofiles” parameter, when running main.py.

::

   python main.py nofiles

The tests are divided into categories: Analog Tests, Trigger Tests, Power Supply Tests, Digital Tests. Each test suite can run independently, as well as in various combinations. (e.g. run only trigger and power supply tests).The resulting HTML test report, states whether each test passed or failed. If any test failed, it also prints the Python error message.

::

   python main.py A_AnalogTests.test_1_analog_objects nofiles

Analog Tests
------------

This suite ensures that the analog segment of the module operates correctly by running the following tests:

-  test_analog_objects - checks if AnalogIn, AnalogOut and Trigger objects were retrieved
-  test_calibration -test if ADC and DAC were calibrated
-  test_amplitude - test different signal amplitudes on both channels
-  test_analog_trigger - test each analog trigger condition on each channel
-  test_cyclic_buffer - test if a single buffer is received when cyclic buffer is set to false
-  test_frequency - loop through all available sampling rates for AnalogIn and AnalogOut and test some frequency values on both channels
-  test_offset - test different signal offsets on both channels
-  test_oversampling_ration - test different oversampling ratio values for each channel
-  test_phase_difference_between_channels_in_degrees - test that channels are in phase at different sample rates, result in degrees
-  test_phase_difference_between_channels_in_samples - test that channels are in phase at different sample rates, result in samples
-  test_shapes - test different waveforms on both channels
-  test_timeout - test if timeout occurs
-  test_voltmeter - read a constant buffer on both channels of the ADC

.. image:: https://wiki.analog.com/_media/university/tools/m2k/libm2k/analog_m2ktests.png
   :align: center
   :width: 500px

Trigger Tests
-------------

Here, some additional tests are done on the trigger object:

-  test_trigger_object - check if TriggerObject was received
-  test_trigger_jitter - test if the number of triggers counted is equal to the number of buffers pushed

Power Supply Tests
------------------

The power supply functionality is checked with the following tests:

-  test_power_supply_object - check if PowerSupply object was retrieved
-  test_positive_power_supply - set different values on the positive power supply pin and compare these to the value read by the ADC
-  test_negative_power_supply - set different values on the positive negative supply pin and compare these to the value read by the ADC

Digital Tests
-------------

The digital segment of the ADALM2000 module is tested with the following:

-  test_cyclic_buffer - checks to see that the pushed buffer is acquired multiple times
-  test_digital_output_channels - push buffer on each digital channel and ensure that the buffer read back matches the one that was pushed
-  test_state_digital_channels - for each channel, toggle the state and see that it updated accordingly
-  test_trig_conditions - for each channel, check every possible trigger condition

.. image:: https://wiki.analog.com/_media/university/tools/m2k/libm2k/trig_pwrspl_dig_m2ktests.png
   :align: center
   :width: 500px

.. |image1| image:: https://wiki.analog.com/_media/university/tools/m2k/libm2k/plot_example1_m2ktests.png
   :width: 500px
.. |image2| image:: https://wiki.analog.com/_media/university/tools/m2k/libm2k/plot_example2_m2ktests.png
   :width: 500px
.. |image3| image:: https://wiki.analog.com/_media/university/tools/m2k/libm2k/results_files_sample_m2ktests.png
   :width: 500px
