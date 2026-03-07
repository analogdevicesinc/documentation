DIY 72V TO 96V Battery Pack for AD-BMSE2E3W-SL
==============================================

Overview
--------

| The **AD-BMSE2E3W-SL** is a BMS reference design for light electric vehicles (LEVs). With a voltage range of 72 V to 96 V, this solution is suitable for electric 2-wheeler and 3-wheeler vehicles with high current capacity ranging up to 100 A.
| ​It is designed to perform either in embedded mode or using a graphical user interface (GUI), where it calculates the battery's State of Charge (SoC) and State of Health (SoH) through enhanced coulomb counting technique.
| To demonstrate its capabilities, this application user guide will explain how to build a 72V-96V battery pack and highlight the use of the AD-BMSE2E3-W-SL for evaluating and monitoring the battery using the Light EV BMS GUI.

Demo Requirements
-----------------

-  78 pcs. 3.7V Lithium-Ion Battery
-  1 roll Lithium-Ion Nickel Strip
-  1 roll Single Wire Connector
-  1 pc. AD-BMSE2E3W-SL Board
-  1 pc. MAX32625PICO Programmer Board with 10-pin SWD Ribbon Cable
-  1 pc. Micro USB-to-USB Cable
-  4 pcs. AWG Stackable Banana Plug to Alligator Clip Cable
-  2 pcs. Cell Connector Blocks *(included in the AD-BMSE2E3W-SL)*

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/diy_battery_demo_requirements.png
   :align: center
   :width: 2000px

Battery Pack Assembly
---------------------

In this demo, two 48V battery packs will be combined to create a 92V battery pack. Note that these steps can also be applied to achieve a single battery pack with a voltage range between 72V and 96V.

-  **Determine the Number of Batteries**

   -  The number of cells in series **N** can be calculated by dividing the **total voltage needed** (48V) by the **voltage of one cell** (3.7V).

      -  In this example, 13 cells are required to build a 48V battery pack. Each cell consists of 3 batteries connected in parallel, resulting in a total of 39 batteries for the entire pack.
      -  Arrange the batteries according to the picture below.

      |image1|

-  **Connecting the Batteries**


|image2|

   -  Make a **Parallel Connection**. Connect 3 batteries in parallel by linking all positive terminals and all negative terminals using the lithium-ion battery nickel strip. Repeat this process to form 13 cells.

      -  After completing the 13 cells, make a **Series Connection** by connecting the positive terminal of one cell to the negative terminal of the next cell. Continue this process until all 13 cells are connected in series.

-  **Insulation and Final Assembly**

   -  Ensure all connections are secure and properly insulated to prevent short circuits.

      -  Use heat shrink tubing or electrical tape to cover exposed connections.
      -  Place the battery pack in a suitable enclosure for protection and ease of handling.

.. note::

   Refer to the diagram above and make sure to connect the bottom part of the pack.


Demo Setup
----------

Block Diagram
~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/hardware_setup.png
   :align: center
   :width: 2000px

Hardware Setup
~~~~~~~~~~~~~~

-  Using the single wire cables connect each battery cell to the cell connector block. Refer to the diagram to short any unused ports in the block.


|image3|

-  Attach the two cell connector blocks to the AD-BMSE2E3W-SL through P1 and P4 ports.

|image4|

-  (Using the red stackable banana plug to alligator clip) Connect the VBAT+ terminal of the battery pack to the V+ input.
-  (Using the black stackable banana plug to alligator clip) Connect the VBAT- terminal of the battery pack to the V- input on the AD-BMSE2E3W-SL.

|image5|

-  Attach the MAX32625PICO programmer to the AD-BMSE2E3W-SL board using the 10-pin SWD ribbon cable. Then, power the MAX32625PICO by connecting it to the Host PC using a micro-USB to USB cable.

|image6|

.. container:: center round box


   ..

| <fc #4682b4>\ **By default (upon purchase), the AD-BMSE2E3W-SL board comes with a MAX32625PICO programmer adapter that is loaded with firmware image.
     Otherwise, if you are using a new MAX32625PICO programmer (that is not part of the original kit), make sure to flash it first with the** :git-max32625pico-firmware-images:`correct firmware image <raw/master/bin/max32625_max32690evkit_if_crc_swd_v1.0.7.bin>` **before connecting it to the AD-BMSE2E3W-SL board. If you do not know how to load the image, follow the instructions below:**\ </fc>
   |

.. raw:: html

   <details><summary>**Click here to learn how to flash the firmware image in the MAX32625PICO**</summary>

-   Download the firmware image: :git-max32625pico-firmware-images:`MAX32625PICO Firmware Image for MAX32690 <raw/master/bin/max32625_max32690evkit_if_crc_swd_v1.0.7.bin>`
   -   Do not connect the MAX32625PICO to the AD-BMSE2E3W-SL Board yet.
   -   Connect the MAX32625PICO to the Host PC using the micro USB to USB cable.
   -   Press the button on the MAX32625PICO. **(Do not release the button until the MAINTENANCE drive is mounted)**.\

   |image7|

   -   Release the button once the MAINTENANCE drive is mounted.
   -   Drag and drop (to the MAINTENANCE drive) the firmware image.
   -   After a few seconds, the MAINTENANCE drive will disappear and be replaced by a drive named DAPLINK. This indicates that the process is complete, and the MAX32625PICO can now be used to flash the firmware of the AD-BMSE2E3W-SL Board.

.. raw:: html

   </details>

   


-  (Using the red stackable banana plug to alligator clip cable) Connect the alligator clip to V+ and insert the other end of the cable (banana plug) to TP16 (VBAT+ terminal) of the AD-BMSE2E3W-SL board.


   


|image8|

-  (Using the black stackable banana plug to alligator clip cable) Connect the alligator clip to V- and connect the other end of the cable to the **VBAT-** (Rsense - top side) of the AD-BMSE2E3W-SL.

|image9|

-  Connect a load to the **Link+_Out** pin and connect the other end of the load to **Shunt-**.

|image10|

-  Once all steps are completed, you are now ready to use this reference design and run GUI.

Software Setup
~~~~~~~~~~~~~~

| |image11|

.. tip::

   The AD-BMSE2E3W-SL comes complete with firmware examples and easy-to-use application GUI.


   | Access the software resources and see the setup procedure in the
   
   .. container:: hi

      :doc:`AD-BMSE2E3W-SL Software User Guide </wiki-migration/resources/eval/user-guides/ad-bmse2e3w-sl/software>`

   
   .
   |

Running the Demo
----------------

| 1. Follow the instructions provided above to set up the hardware components. Ensure all connections are secure and aligned with the diagram and specifications.
| 2. Download and install the necessary software and dependencies from the link provided above. Follow the installation guide if available to configure the software correctly.
| 3. Open the **Light_EV_BMS_GUI.exe** file to open the GUI. You should see a script running in the background separately and the landing page running in the browser.
| |image12|

+-------------------------------------------+------------------------------+-------------------------------------------------------------------------------------------------+
| **Details Available on the Landing Page** |                              |                                                                                                 |
+-------------------------------------------+------------------------------+-------------------------------------------------------------------------------------------------+
|                                           | **Function**                 | **Definition**                                                                                  |
+-------------------------------------------+------------------------------+-------------------------------------------------------------------------------------------------+
| 1                                         | Connection Indicator         | Shows if UART or CAN is connected                                                               |
+-------------------------------------------+------------------------------+-------------------------------------------------------------------------------------------------+
| 2                                         | Communication Mode Drop Down | Allows selection of the communication mode                                                      |
+-------------------------------------------+------------------------------+-------------------------------------------------------------------------------------------------+
| 3                                         | Vehicle System Mode          | Contains a dropdown list for vehicle system states such as parked, driving, charging, and fault |
+-------------------------------------------+------------------------------+-------------------------------------------------------------------------------------------------+
| 4                                         | Refresh Button               | Updates the list of available communication ports                                               |
+-------------------------------------------+------------------------------+-------------------------------------------------------------------------------------------------+
| 5                                         | Battery Specifications       | Input boxes for battery specifications which are used for SoC and SoH                           |
+-------------------------------------------+------------------------------+-------------------------------------------------------------------------------------------------+
| 6                                         | Load Defaults Button         | Sets the battery specification values to the predefined default program entries                 |
+-------------------------------------------+------------------------------+-------------------------------------------------------------------------------------------------+
| 7                                         | Start Button                 | Initiates battery monitoring and directs users to the Overview page                             |
+-------------------------------------------+------------------------------+-------------------------------------------------------------------------------------------------+

| 
| 4.Set the jumper configuration based on the communication mode being used: UART or CAN. |image13|
| 5. On the GUI landing page, hover to the Communication Mode dropdown menu. Select **UART COM** followed by the specific **port number** if using UART, or CAN if using CAN. |image14|
| 6. Press the **RESET** button (S1) every time the hardware set up is changed. |image15|
| 7. Click the **Load Defaults** button to set the initial entry values for the different parameters needed for the State of Charge (SoC) and State of Health (SoH) calculations. |image16|
| 8. Click the **Start** button to begin the measurements. |image17|

Viewing Results in the Light BMS GUI Tabs
-----------------------------------------

Overview Tab
~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/update_overview_page.png
   :align: center
   :width: 2000px

Graph
~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/update_graph_page.png
   :align: center

Console
~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/update_console_page.png
   :align: center

Diagnostic
~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/update_diagnsotic_page.png
   :align: center

.. note::

   Refer to the **Tabs** section of the :doc:`AD-BMSE2E3W-SL Software User Guide </wiki-migration/resources/eval/user-guides/ad-bmse2e3w-sl/software>` for a comprehensive overview of each tab's functions and descriptions.


Help and Support
----------------

For questions and more information, please visit the Analog Devices Engineer Zone.

.. hint::

   
   For internal support, you can raise a question or submit a ticket through our Jira Service Desk using the following link: `BU Applications Technical Support <https://jira.analog.com/servicedesk/customer/portal/131>`_.
   
   For external users, please post your questions under the :ez:`Reference Designs <reference-designs>` forum in EngineerZone to get assistance from the community and experts.
   


.. image:: https://wiki.analog.com/_media/navigation #/resources/eval/user-guides/ad-bmse2e3w-sl
   :alt: Overview #:resources:eval:user-guides:ad-bmse2e3w-sl:software|AD-BMSE2E3W-SL Software User Guide#none

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/battery_arrangement.png
   :width: 2000px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/series-parallel_connection.png
   :width: 2000px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/battery-cell_connector_block-connection.png
   :width: 2000px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/cell_connector_block-to-adbmse2e3w.png
   :width: 2000px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/vbat_vbat-.png
   :width: 2000px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/pico_connection.png
   :width: 2000px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-paarray3552r-sl/max32625pico_maxdap.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/vbat_.png
   :width: 2000px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/vbat-.png
   :width: 2000px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/load_connection.png
   :width: 2000px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/update_overview_page.png
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/home_landing_details.png
   :width: 2000px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/communication_jumper_selection.png
   :width: 300px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/communication_mode.png
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/reset_button_hardware.png
   :width: 500px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/setting_defaults.png
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/start_button.png
