Running the Dining Philosophers example for ADSP-BF707 EZ-Kit with CrossCore Embedded Studio
============================================================================================

Overview
--------

This page describes the steps required to build and run Dining Philosophers example on ADSP-BF707 EZ-Kit board using CrossCore Embedded Studio.

--------------

Environment Setup
-----------------

Before running the basic example with CrossCore Embedded Studio, you should make some preparation for environment setup including software and hardware.

Software Requirement
--------------------

-  Analog Devices CrossCore Embedded Studio. For more information please refer to :doc:`Software environment set up for CrossCore Embedded Studio </wiki-migration/resources/tools-software/freertos/freertos-addin/examples/software-enviroment-setup-cces>`
-  Analog Devices FreeRTOS-Addin product. For more information please refer to :doc:`Installing the FreeRTOS-Addin Product </wiki-migration/resources/tools-software/freertos/freertos-addin>`
   \* Analog Devices FreeRTOS-Addin Example. For more information please refer to :doc:`Get the FreeRTOS-Addin Examples </wiki-migration/resources/tools-software/freertos/freertos-addin/examples/software-enviroment-setup-cces>`
   ===== Hardware Setup =====
-  An ADSCP-BF707 EZ-Kit board
-  An ICE1000 or ICE2000 emulator

Connect the ICE1000 or ICE2000 emulator to **DEBUG P3** port of EZ-Kit and the host PC using USB cable and simultaneously connect the power supply with 5 volts as in the **Diagram 1** below

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/examples/supported-boards/adsp-bf707-ezkit/bf707-hw.jpg
   :align: center
   :width: 400px

.. container:: centeralign

   **Diagram 1** Hardware Connection


--------------

Build the Example
-----------------

Before you run the FreeRTOS-Addin example in CrossCore Embedded Studio, follow below three steps to import and build it.

1. Import the FreeRTOS-Addin example into CrossCore Embedded Studio:

-  Select the **File** menu and then select the **Import** option from the menu
-  When the **Import** project window appears:
-  Click on the **General** folder, then click on the **Existing Projects into Workspace** entry, and click **Next**
-  Click the **Select root directory** radio button and then click the **Browse** button
-  Browse the root folder where you previously installed the FreeRTOS-Addin example and then browse down into the \**freertos-addin-examples\\Demo\\DiningPhilosophers\\BLACKFIN_ADSP_BF707_CCES \*\* folder
-  Click **OK** to close the file browser dialog
-  A single project should appear in the **projects** pane of the **Import** window
-  Check the entry in the **projects** pane and click **Finish**

|image1|

.. container:: centeralign

   **Diagram 2** Import the FreeRTOS-Addin Example


2. Choose Debug/Release mode to build the project.



|image2|

.. container:: centeralign

   **Diagram 3** Build Mode Selection


3. Build the project in CrossCore Embedded Studio

-  In the **Project Explorer** right click on the **DiningPhilosophers_BLACKFIN_BF707** project and select the **Build Project** option from the menu

--------------

Run the Example
---------------

Follow below four steps to do debug configuration, download and run the built binary on the target board.

1. In the **Project Explorer** right click on the **DiningPhilosophers_BLACKFIN_BF707** project and select the **Debug As** option from the menu

2. From the popup menu select **Debug Configurations** option to create a new debug configuration that matches your emulator and target board


|image3|

.. container:: centeralign

   **Diagram 4** Set Debug Configuration


3. Click the **Debug** button to close the **Debug Configuration** window



|image4|

.. container:: centeralign

   **Diagram 5** Close Debug Configuration


4. Click the **Run/Resume** button to start running your application



|image5|

.. container:: centeralign

   **Diagram 6** Load and Run the Example


--------------

Test Results
------------

Output from the application should be visible within the **Console** window in the CrossCore Embedded Studio IDE. and **Test Passed** will be printed if the all tests passed.


|image6|

.. container:: centeralign

   **Diagram 7** Example Test Results


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/examples/supported-boards/adsp-bf707-ezkit/diningphilosophers_bf707_cces_001.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/examples/common-cces-debug-release_001.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/examples/supported-boards/adsp-bf707-ezkit/diningphilosophers_bf707_cces_002.png
   :width: 1000px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/examples/supported-boards/adsp-bf707-ezkit/diningphilosophers_bf707_cces_003.png
   :width: 1000px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/examples/supported-boards/adsp-bf707-ezkit/diningphilosophers_bf707_cces_004.png
   :width: 1000px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/examples/supported-boards/adsp-bf707-ezkit/diningphilosophers_bf707_cces_005.png
   :width: 1000px
