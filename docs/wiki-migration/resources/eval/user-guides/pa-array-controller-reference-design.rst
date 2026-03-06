Power Amplifier (PA) Array Controller User Guide
================================================

Overview
--------

| The PA Array Controller Board is a reference design utilizing ADI's portfolio for control, protection, and appropriate bias sequencing of Power Amplifier (PA) Arrays designed for massive MIMO and macro base station RF front-end applications.
| The system effectively manages the power-up and power-down progression of 4-channel, 8-channel, and 32-channel power amplifiers while continuously monitoring crucial parameters such as drain voltages, drain current, gate voltages, and temperature. To achieve rapid transition between bias point and gate voltage pinch-off within a timeframe of less than 5 microseconds, a high-speed DAC is employed. The biasing sequence, sensor management, and user interface are overseen by the MAX32662 microcontroller. Additionally, the system incorporates fault detection capabilities to safeguard the amplifiers against overvoltage, overcurrent, and overtemperature events.

| 
| |pa_top_view.jpg|

Features
~~~~~~~~

-  Fault Event Protection -- undervoltage, overvoltage, overcurrent, overtemperature
-  Fast GaN gate voltages settling time ~ <5 microseconds
-  Fast fault event to gate pinch-off time ~ <10 microseconds
-  Wide range of gate bias voltages +/- 10 V
-  Precise power-up and down sequence of up to two GaN HEMTs-based amplifiers

| 
| ==== Applications ====

-  5G massive MIMOs
-  Macro base stations

| 
| ==== Block Diagram ==== |block_diagram.jpg|

Specifications
--------------

`sample_text_only;_please_replace_details_with_actual_board_specs._you_may_add_other_items_as_necessary. <https://wiki.analog.com/sample_text_only;_please_replace_details_with_actual_board_specs._you_may_add_other_items_as_necessary.>`__

=================================== =================================
Electrical Specs                    
=================================== =================================
Power                               3.6 kW
Input voltage                       230 V +/-15%
Input current                       16 A
Input frequency                     50 Hz
Output voltage                      230 V +/-15%
Output current                      10 A/16 A
Output frequency                    50 Hz
Operating Conditions                
Operating temperature               -25°C to +45°C
Residual current device             6 mA DC/30 mA rms
Safety Features                     
Overvoltage category                II
Protection features                 Relay soldered contacts detection
\                                   Overvoltage
\                                   Undervoltage
\                                   Overcurrent
\                                   Overtemperature
Other features                      Integrated isolation
\                                   Diode detection
User Interface & Control            
Communication                       Bluetooth 5.2
Status Indicators                   LEDs
Debugging                           RS-232
Designed to the following standards 
\                                   IEC 61851, IEC 62752
=================================== =================================

----

Package Contents
----------------

`list_here_the_items_that_customers_will_get_when_they_open_the_package;_include_all_accessories._insert_package_photo_in_this_section <https://wiki.analog.com/list_here_the_items_that_customers_will_get_when_they_open_the_package;_include_all_accessories._insert_package_photo_in_this_section>`__

The development kit is delivered with a set of accessories required to put the system together and get it up and running in no time. This is what you'll find in the development kit box:

-  Unordered List Item
-  Unordered List Item
-  Unordered List Item
-  Unordered List Item
-  Unordered List Item
-  Unordered List Item

----

Getting your System Up and Running
----------------------------------

|

.. tip::

   For Hardware Setup, check out the :doc:`PA Array Controller Hardware User Guide </wiki-migration/resources/eval/user-guides/pa-array-controller-reference-design/hardware>`


   | For Software Setup, check out the `PA Array Controller Board Software User Guide <https://wiki.analog.com/resources/eval/user-guides/pa-array-controller-reference-design/software>`__


--------------

Help and Support
----------------

For questions and more information, please visit the Analog Devices Engineer Zone.

.. hint::

   :ez:`EngineerZone Support Community <reference-designs>`


|

.. |pa_top_view.jpg| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/pa_top_view.jpg
   :width: 400px
.. |block_diagram.jpg| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/block_diagram.jpg
   :width: 800px
