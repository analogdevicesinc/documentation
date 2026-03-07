Digital IO - Test Case
======================

Initial Setup
-------------

In order to proceed through the test case, first of all delete the Scopy \*.ini file (saves previous settings made in Scopy tool) from the following path on Windows: C:\\Users\\your_username\\AppData\\Roaming\\ADI .

Open the DigitalIO instrument. The interface should look like the picture below:

.. image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/digitalio_init.png
   :width: 700px

Press multiple times on the "Run" button to check if the instrument works.

Test Title
----------

A. IO Operation
~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click to expand</summary>

+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Description                           | Test Steps                                                                                                                                              | Steps Resources     | Expected Results                                                                                                                                                        |
+=======================================+=========================================================================================================================================================+=====================+=========================================================================================================================================================================+
| Checking individual digital pin state | 1. Set DIO 0-7 and DIO 8-15 as individual pins                                                                                                          | |image16|           | The interface should look like in the "Step Resources" picture (left side).                                                                                             |
+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                       | 2. Set channel 0 as output                                                                                                                              | |image17|           | The interface should look like in the "Step Resources" picture (left side).                                                                                             |
+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                       | 3. Set channel 7 as input                                                                                                                               | |image18|           | The interface should look like in the "Step Resources" picture (left side).                                                                                             |
+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                       | 4. Connect digital channel 0 to channel 7 via wires.                                                                                                    | |image19|           |                                                                                                                                                                         |
+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                       | 5. Change the logic state of channel 0 (0/1) multiple times and monitor channel 7 state.                                                                | |image20| |image21| | When channel 0 is set to logic one, channel 7 will be automatically set to logic 1. When channel 0 is set to logic one, channel 7 will be automatically set to logic 1. |
+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                       | 6. Connect the channel 0 to voltmeter and channel 7 to the positive power supply.                                                                       | |image22|           |                                                                                                                                                                         |
+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                       | 7. Set channel 0 to logic state 0.                                                                                                                      | |image23|           | The interface should look like in the "Step Resources" picture (left side).                                                                                             |
+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                       | 8. Monitor the voltage value via voltmeter.                                                                                                             | |image24|           | On the voltmeter the voltage displayed is be between -0.050V and 0.4V.                                                                                                  |
+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                       | 9. Set channel 0 to logic state 1.                                                                                                                      | |image25|           | The interface should look like in the "Step Resources" picture (left side).                                                                                             |
+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                       | 10. Monitor the voltage value via voltmeter.                                                                                                            | |image26|           | On the voltmeter the voltage displayed should be between 2.9V and 3.4V.                                                                                                 |
+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                       | 11. Set positive power supply to voltage level between 0V and 0.8V.                                                                                     | |image27|           | The interface should look like in the "Step Resources" picture (left side).                                                                                             |
+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                       | 12. Monitor the channel 7 logic state.                                                                                                                  | |image28|           | Channel 7 indicates logic 0 level.                                                                                                                                      |
+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                       | 13. Set positive power supply to voltage level between 2V and 3.3V                                                                                      | |image29|           | The interface should look like in the "Step Resources" picture (left side).                                                                                             |
+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                       | 14. Monitor the channel 7 logic state.                                                                                                                  | |image30|           | Channel 7 indicates logic 1 level.                                                                                                                                      |
+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                       | 15. In step 2 replace by turn channel 0 with channels from 1 to 6 and from 8 to 15. Then, for each replacement repeat steps from 3 to 13.               |                     |                                                                                                                                                                         |
+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                       | 16. In step 2 replace with channel 7 and in step 3 by turn channels from 0 to 6 and from 8 to 15. Then, for each replacement repeat steps from 4 to 13. |                     |                                                                                                                                                                         |
+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. raw:: html

   </details>


B. Group Operation
~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click to expand</summary>

Set DIO 0-7 and DIO 8-15 groups as Group pins:

+-------------------------------------+----------------------------------------------------------------+-----------------+---------------------------------------------------------------------------------------------------+
| Description                         | Test Steps                                                     | Steps Resources | Expected Results                                                                                  |
+=====================================+================================================================+=================+===================================================================================================+
| Checking grouped digital pin states | 1. Set DIO 0-7 and DIO 8-15 as Group pins.                     | |image39|       | The interface should look like in the "Step Resources" picture (left side).                       |
+-------------------------------------+----------------------------------------------------------------+-----------------+---------------------------------------------------------------------------------------------------+
|                                     | 2. Connect DIO 0-7 to DIO 8-15 via wires.                      | |image40|       |                                                                                                   |
+-------------------------------------+----------------------------------------------------------------+-----------------+---------------------------------------------------------------------------------------------------+
|                                     | 3. Set DIO 0-7 as output.                                      | |image41|       | The interface should look like in the "Step Resources" picture (left side).                       |
+-------------------------------------+----------------------------------------------------------------+-----------------+---------------------------------------------------------------------------------------------------+
|                                     | 4. Set DIO 8-15 as input.                                      | |image42|       | The interface should look like in the "Step Resources" picture (left side).                       |
+-------------------------------------+----------------------------------------------------------------+-----------------+---------------------------------------------------------------------------------------------------+
|                                     | 5. Set DIO 0-7 at value 0.                                     | |image43|       | The same value of DIO 0-7 group must be displayed on the DIO 8-15 group.                          |
+-------------------------------------+----------------------------------------------------------------+-----------------+---------------------------------------------------------------------------------------------------+
|                                     | 6. Set DIO 0-7 at value 128.                                   | |image44|       | The same value of DIO 0-7 group must be displayed on the DIO 8-15 group.                          |
+-------------------------------------+----------------------------------------------------------------+-----------------+---------------------------------------------------------------------------------------------------+
|                                     | 7. Set DIO 0-7 at value 170.                                   | |image45|       | The same value of DIO 0-7 group must be displayed on the DIO 8-15 group.                          |
+-------------------------------------+----------------------------------------------------------------+-----------------+---------------------------------------------------------------------------------------------------+
|                                     | 8. Set DIO 0-7 at value 255.                                   | |image46|       | The same value of DIO 0-7 group must be displayed on the DIO 8-15 group.                          |
+-------------------------------------+----------------------------------------------------------------+-----------------+---------------------------------------------------------------------------------------------------+
|                                     | 9. Set DIO 0-7 as input and DIO 8-15 as output. Repeat step 2. |                 | For each value set for the DIO 8-15 group, the same value must be displayed on the DIO 0-7 group. |
+-------------------------------------+----------------------------------------------------------------+-----------------+---------------------------------------------------------------------------------------------------+

.. raw:: html

   </details>


Test Results will be recorded in the following document: `Digital IO - Test Case <https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/digitalio_-_test_case.xlsx>`_

| 
| **Return to Test Cases** :doc:`Table of Contents </wiki-migration/university/tools/m2k/scopy/test-cases>`

.. |image1| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/dio-individual.png
   :width: 100px
.. |image2| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/0out.png
   :width: 100px
.. |image3| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/7in.png
   :width: 100px
.. |image4| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/0-7pin_connection.png
   :width: 100px
.. |image5| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/high0-7.png
   :width: 100px
.. |image6| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/low0-7.png
   :width: 100px
.. |image7| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/0-ps_7-vm_pin_connection.png
   :width: 100px
.. |image8| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/low0.png
   :width: 100px
.. |image9| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/low-voltmeter.png
   :width: 100px
.. |image10| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/high0.png
   :width: 100px
.. |image11| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/high-voltmeter.png
   :width: 100px
.. |image12| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ps-low.png
   :width: 100px
.. |image13| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/7low.png
   :width: 100px
.. |image14| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ps-high.png
   :width: 100px
.. |image15| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/7high.png
   :width: 100px
.. |image16| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/dio-individual.png
   :width: 100px
.. |image17| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/0out.png
   :width: 100px
.. |image18| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/7in.png
   :width: 100px
.. |image19| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/0-7pin_connection.png
   :width: 100px
.. |image20| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/high0-7.png
   :width: 100px
.. |image21| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/low0-7.png
   :width: 100px
.. |image22| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/0-ps_7-vm_pin_connection.png
   :width: 100px
.. |image23| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/low0.png
   :width: 100px
.. |image24| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/low-voltmeter.png
   :width: 100px
.. |image25| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/high0.png
   :width: 100px
.. |image26| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/high-voltmeter.png
   :width: 100px
.. |image27| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ps-low.png
   :width: 100px
.. |image28| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/7low.png
   :width: 100px
.. |image29| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ps-high.png
   :width: 100px
.. |image30| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/7high.png
   :width: 100px
.. |image31| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/dio-group.png
   :width: 100px
.. |image32| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/group-pinconnection.png
   :width: 100px
.. |image33| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/dio07out.png
   :width: 100px
.. |image34| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/dio815in.png
   :width: 100px
.. |image35| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/grp-val0.png
   :width: 100px
.. |image36| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/grp-val128.png
   :width: 100px
.. |image37| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/grp-val170.png
   :width: 100px
.. |image38| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/grp-val255.png
   :width: 100px
.. |image39| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/dio-group.png
   :width: 100px
.. |image40| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/group-pinconnection.png
   :width: 100px
.. |image41| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/dio07out.png
   :width: 100px
.. |image42| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/dio815in.png
   :width: 100px
.. |image43| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/grp-val0.png
   :width: 100px
.. |image44| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/grp-val128.png
   :width: 100px
.. |image45| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/grp-val170.png
   :width: 100px
.. |image46| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/grp-val255.png
   :width: 100px
