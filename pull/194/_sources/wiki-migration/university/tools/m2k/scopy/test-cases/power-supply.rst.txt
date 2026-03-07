Power Supply - Test Case
========================

Initial Setup
-------------

In order to proceed through the test case, first of all delete the Scopy \*.ini file (saves previous settings made in Scopy tool) from the following path on Windows: C:\\Users\\your_username\\AppData\\Roaming\\ADI .

Open the Power Supply instrument. The interface should look like the picture below:

.. image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/powersupply_init.png
   :width: 700px

Press multiple times on the "Enable" buttons to check if the instrument works.

Test Title
----------

A. Independent Controls
~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click to expand</summary>

+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------+----------------------------------------------------------------------------------------+
| Description                                | Test Steps                                                                                                          | Steps Resources                              | Expected Results                                                                       |
+============================================+=====================================================================================================================+==============================================+========================================================================================+
| Checking positive voltage output           | 1. Set Tracking ratio control to Independent Controls                                                               | |image12|                                    | The interface should look like in the "Step Resources" picture (left side).            |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------+----------------------------------------------------------------------------------------+
|                                            | 2. Connect the power supply and voltmeter with the following pins: V+ power supply pin (red) to Scope Ch 1 (orange) | |image13|                                    |                                                                                        |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------+----------------------------------------------------------------------------------------+
| Setting values                             | 3. Set the value to 3.3V and click enable.                                                                          | |image14|                                    | The interface should look like in the "Step Resources" picture (left side).            |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------+----------------------------------------------------------------------------------------+
|                                            | 4. Monitor the power supply output with voltmeter.                                                                  | |image15|                                    | The voltmeter should read values between 3.25V and 3.35V. Just like shown on the left. |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------+----------------------------------------------------------------------------------------+
| Changing set values                        | 5. Change the power supply output value to 1.8V.                                                                    | |Power Supply interface| |Voltmeter reading| | The voltmeter should read values between 1.75V and 1.85V                               |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------+----------------------------------------------------------------------------------------+
|                                            | 6. Change the power supply output value to 2.5V.                                                                    | |image16| |image17|                          | The voltmeter should read values between 2.45V and 2.55V                               |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------+----------------------------------------------------------------------------------------+
|                                            | 7. Change the power supply output value to 5V.                                                                      | |image18| |image19|                          | The voltmeter should read values between 4.95V and 5.05V                               |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------+----------------------------------------------------------------------------------------+
| Checking Increment/Decrement Value; ±1V    | 8. Set the knob to ±1V interval. No orange dot on the center.                                                       | |image20|                                    | The interface should look like in the “Step Resources picture (left side).             |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------+----------------------------------------------------------------------------------------+
|                                            | 9. Set value to 3V. Then use +/- sign to change value with ±1V interval.                                            |                                              | The value should change accordingly. Set Value ± 1V = the new value                    |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------+----------------------------------------------------------------------------------------+
| Checking Increment/Decrement Value; ±100mV | 10. Set the knob to ±100mV interval. Orange dot seen on the center.                                                 | |image21|                                    | The interface should look like in the “Step Resources picture (left side).             |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------+----------------------------------------------------------------------------------------+
|                                            | 11. Set value to 300mV. Then use +/- sign to change value with ±100mV interval.                                     |                                              | The value should change accordingly. Set Value ± 100mV = the new value                 |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------+----------------------------------------------------------------------------------------+
| Checking Negative Voltage Output           | 12. Change pin connections to the following: V- power supply pin (white) to Scope Ch 1 (orange).                    | |image22|                                    |                                                                                        |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------+----------------------------------------------------------------------------------------+
|                                            | 13 Repeat Steps 3 to 11. Set the values mentioned to negative in checking negative output.                          |                                              |                                                                                        |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------+----------------------------------------------------------------------------------------+

.. raw:: html

   </details>


B. Tracking
~~~~~~~~~~~



.. raw:: html

   <details><summary>Click to expand</summary>

+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| Description                           | Test Steps                                                                                                                        | Steps Resources                    | Expected Results                                                                                                                           |
+=======================================+===================================================================================================================================+====================================+============================================================================================================================================+
| Checking output when in Tracking mode | 1. Set Tracking ratio control to Tracking                                                                                         | |image34|                          | The interface should look like in the "Step Resources" picture (left side).                                                                |
+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
|                                       | 2. Connect the following pins: V+ power supply pin (red) to Scope Ch 1 (orange); V- power supply pin (while) to Scope Ch 2 (blue) | |image35|                          |                                                                                                                                            |
+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| Setting tracking ratio                | 3. Set value of positive output to 5V. Set tracking ratio to 50%                                                                  | |image36|                          | The negative output value should be set automatically following the equation: V-= -(ratio\*V+). For 50% tracking ratio, V-= -2.5V.         |
+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
|                                       | 4. Monitor the power supply output with voltmeter.                                                                                | |image37|                          | The voltmeter should read the following values: V+ = 4.95V to 5.05V; V- = -2.55V to -2.45V                                                 |
+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| Changing tracking ratio               | 5. Set tracking ratio to 10%.                                                                                                     | |image38| |image39|                | Negative output Value should be set to -500mV. The voltmeter should read the following values: V+ = 4.95V to 5.05V; V- = -505mV to -495mV  |
+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
|                                       | 6. Set tracking ratio to 25%..                                                                                                    | |image40| |image41|                | Negative output Value should be set to -1.25V. The voltmeter should read the following values: V+ = 4.95V to 5.05V; V- = -1.30V to -1.20V  |
+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
|                                       | 7. Set tracking ratio to 66 %.                                                                                                    | |Power supply interface| |image42| | Negative output Value should be set to -3.3 V. The voltmeter should read the following values: V+ = 4.95V to 5.05V; V- = -3.35V to -3.25V |
+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
|                                       | 8. Set tracking ratio to 100%.                                                                                                    | |image43| |image44|                | Negative output Value should be set to -5V. The voltmeter should read the following values: V+ = 4.95V to 5.05V; V- = -5.05V to -4.95V     |
+---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+

.. raw:: html

   </details>


Test Results will be recorded in the following document: `Power Supply - Test Case <https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/power_supply_-_test_case.xlsx>`_

| 
| **Return to Test Cases** :doc:`Table of Contents </wiki-migration/university/tools/m2k/scopy/test-cases>`

.. |image1| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Astep1.JPG
   :width: 100px
.. |image2| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Astep2.JPG
   :width: 100px
.. |image3| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Astep3.JPG
   :width: 100px
.. |image4| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Astep4.JPG
   :width: 100px
.. |Power Supply interface| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Astep5a.JPG
   :width: 100px
.. |Voltmeter reading| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Astep5b.JPG
   :width: 100px
.. |image5| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Astep6a.JPG
   :width: 100px
.. |image6| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Astep6b.JPG
   :width: 100px
.. |image7| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Astep7a.JPG
   :width: 100px
.. |image8| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Astep7b.JPG
   :width: 100px
.. |image9| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Aknobstep8.JPG
   :width: 100px
.. |image10| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Aknobstep10.JPG
   :width: 100px
.. |image11| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Astep12.JPG
   :width: 100px
.. |image12| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Astep1.JPG
   :width: 100px
.. |image13| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Astep2.JPG
   :width: 100px
.. |image14| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Astep3.JPG
   :width: 100px
.. |image15| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Astep4.JPG
   :width: 100px
.. |image16| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Astep6a.JPG
   :width: 100px
.. |image17| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Astep6b.JPG
   :width: 100px
.. |image18| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Astep7a.JPG
   :width: 100px
.. |image19| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Astep7b.JPG
   :width: 100px
.. |image20| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Aknobstep8.JPG
   :width: 100px
.. |image21| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Aknobstep10.JPG
   :width: 100px
.. |image22| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Astep12.JPG
   :width: 100px
.. |image23| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Bstep1.JPG
   :width: 100px
.. |image24| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Bstep2.JPG
   :width: 100px
.. |image25| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Bstep3.JPG
   :width: 100px
.. |image26| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Bstep4.JPG
   :width: 100px
.. |image27| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Bstep5a.JPG
   :width: 100px
.. |image28| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Bstep5b.JPG
   :width: 100px
.. |image29| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Bstep6a.JPG
   :width: 100px
.. |image30| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Bstep6b.JPG
   :width: 100px
.. |Power supply interface| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Bstep7a.JPG
   :width: 100px
.. |image31| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Bstep7b.JPG
   :width: 100px
.. |image32| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Bstep8a.JPG
   :width: 100px
.. |image33| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Bstep8b.JPG
   :width: 100px
.. |image34| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Bstep1.JPG
   :width: 100px
.. |image35| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Bstep2.JPG
   :width: 100px
.. |image36| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Bstep3.JPG
   :width: 100px
.. |image37| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Bstep4.JPG
   :width: 100px
.. |image38| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Bstep5a.JPG
   :width: 100px
.. |image39| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Bstep5b.JPG
   :width: 100px
.. |image40| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Bstep6a.JPG
   :width: 100px
.. |image41| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Bstep6b.JPG
   :width: 100px
.. |image42| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Bstep7b.JPG
   :width: 100px
.. |image43| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Bstep8a.JPG
   :width: 100px
.. |image44| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/ ps_Bstep8b.JPG
   :width: 100px
