Running the LwIP DNS Client Example with CrossCore Embedded Studio
==================================================================

Overview
--------

This page describes the steps to build and run the LwIP DNS Client Example for ARM (CORTEX-A5) on on ADSP-SC5xx EZ-Kit with CrossCore Embedded Studio.

\*\* Description: \*\*

LwIP (lightweight IP) is a widely used open-source TCP/IP stack designed for embedded systems. This example showing how to use the LwIP feature to connect the Network for the board the with FreeRTOS, after the Link established, the board will get a IP Address Automatically assigned by DNS.

e.g. the log from the UART:

.. code:: bash

     Link established
     IP ADDRESS: 10.99.24.65
     IP Address of analog.com is : 137.71.25.128

For the full documentation please refer to the wiki page `LwIP <https://en.wikipedia.org/wiki/LwIP>`__.

\*\* Testes With: \*\*

Currently supported board/processor and the test information are listed below:

+-------------------+--------------------------------------+---------------------------+
| Board             | Processor                            | Example                   |
+===================+======================================+===========================+
| ADSP-SC573 EZ-KIT | ``ADSP-SC573 Cortex-A5 Core0``       | CORTEX_A5_ADSP_SC573_CCES |
+-------------------+--------------------------------------+---------------------------+
| :::               | ``ADSP-SC573 SHARC Core1 and Core2`` | :::                       |
+-------------------+--------------------------------------+---------------------------+
| ADSP-SC584 EZ-KIT | ''ADSP-SC584 Cortex-A5 Core0 ''      | CORTEX_A5_ADSP_SC584_CCES |
+-------------------+--------------------------------------+---------------------------+
| :::               | ``ADSP-SC584 SHARC Core1 and Core2`` | :::                       |
+-------------------+--------------------------------------+---------------------------+
| ADSP-SC589 EZ-KIT | ``ADSP-SC589 Cortex-A5 Core0``       | CORTEX_A5_ADSP_SC589_CCES |
+-------------------+--------------------------------------+---------------------------+
| :::               | ``ADSP-SC589 SHARC Core1 and Core2`` | :::                       |
+-------------------+--------------------------------------+---------------------------+

--------------

Environment Setup
-----------------

Before running the examples with CrossCore Embedded Studio, please make some necessary preparations for the environment setup including software and hardware.

Software Requirement
--------------------

-  Analog Devices CrossCore Embedded Studio. For more information please refer to :doc:`Software environment set up for CrossCore Embedded Studio </wiki-migration/resources/tools-software/freertos/freertos-addin/examples/software-enviroment-setup-cces>`
-  Analog Devices FreeRTOS-Addin product. For more information please refer to :doc:`Installing the FreeRTOS-Addin Product </wiki-migration/resources/tools-software/freertos/freertos-addin>`
   \* Analog Devices FreeRTOS-Addin Example. For more information please refer to :doc:`Get the FreeRTOS-Addin Examples </wiki-migration/resources/tools-software/freertos/freertos-addin/examples/software-enviroment-setup-cces>`
   \* Analog Devices LwIP BSP Support: install :adi:`TCP/IP Stack for CrossCore Embedded Studio Rev. 2.6.0 <en/design-center/processors-and-dsp/evaluation-and-development-software/adswp-lwip.html#dsp-relatedsoftware>` for CCES and please refer to the linked page to :ez:`add the LwIP patch with CCES V2.9.0 or later <dsp/software-and-development-tools/freertos/w/documents/15283/how-to-use-the-lwip-dnsclient-freertos-example-with-the-cces-v2-9-0-or-later>`

Hardware Setup
--------------

\*\* POWER \*\*

Connect the power supply with Corresponding voltage Power:

-  ``ADSP-SC573 EZ-Kit:`` **P27** (with **12V** Power)
-  ``ADSP-SC584 EZ-Kit:`` **P27** (with **12V** Power)
-  ``ADSP-SC589 EZ-Kit:`` **P22** (with **5V** Power)

\*\* JTAG \*\*

Connect the ICE1000 or ICE2000 emulator to the following **DEBUG port** of EZ-Kit and the host PC using USB cable:

-  **``ADSP-SC573 EZ-Kit:``** DEBUG **P1**
-  **``ADSP-SC584 EZ-Kit:``** DEBUG **P1**
-  **``ADSP-SC589 EZ-Kit:``** DEBUG **P3**

**Ethernet**

Connect the Gigabit Ethernet port of EZ-Kit to the same LAN as PC using standard network cable:

-  **``ADSP-SC573 EZ-Kit:``** **J4** (10/100/1000 Gigabit Ethernet port)
-  **``ADSP-SC584 EZ-Kit:``** **J4** (10/100/1000 Gigabit Ethernet port)
-  **``ADSP-SC589 EZ-Kit:``** **J14** (10/100/1000 Gigabit Ethernet port)

**TTY Setup**

Connect a Micro USB cable to your PC from the following EZ-Kit UART to USB connector:

-  **``ADSP-SC573 EZ-Kit:``** USB UART **P7**
-  **``ADSP-SC584 EZ-Kit:``** USB UART **P7**
-  **``ADSP-SC589 EZ-Kit:``** USB UART **P8**

Then Download, install, and launch your prefered TTY terminal (e.g.\ `PuTTY/TeraTerm <https://www.putty.org/>`__) and configure a serial connection with the settings listed in Table-1. ``NOTE:`` The COM port number will be changed as plugging USB cables in and out of the PC. It can be found in the Windows **Device Manager** facility, under the Ports (COM &LPT) collapsible section.

.. container:: column

   
   ======================== ======
   **Table 1** COM Settings 
   ======================== ======
   Configuration            Value
   Baud Rate                115200
   Data bits                8
   Baud Rate                1
   Parity                   None
   Flow                     None
   \                        
   ======================== ======
   


.. container:: column

   


|image1|

Now we take the ADSP-SC573 EZ-Kit as an example, the hardware connection of LwIP Dns Client example is shown as follows:

.. container:: group

   
   .. container:: half column


   
   |image2|

         .. container:: centeralign

            POWER JATG and Ethernet Connection

         

   
   .. container:: half column


         

   
   |image3|

         .. container:: centeralign

            TTY UART Connection

         

   


.. container:: centeralign

   **Diagram 1** Hardware Connection


--------------

Build the Example
-----------------

Before running the FreeRTOS-Addin example in CrossCore Embedded Studio, please follow below steps to import and build it, now we take ADSP-SC573-EzKit as the example to demonstrate.

1. Import the FreeRTOS-Addin example into CrossCore Embedded Studio:

-  Select the **File** menu and then select the **Import** option from the menu
-  When the **Import** project window appears:
-  Click on the **General** folder, then click on the **Existing Projects into Workspace** entry, and click **Next**
-  Click the **Select root directory** radio button and then click the **Browse** button
-  Browse the root folder where you previously installed the FreeRTOS-Addin example and then browse down into the **freertos-addin-examples\\Demo\\LwIP_DnsClient\\CORTEX_A5_ADSP_SC573_CCES** folder
-  Click **OK** to close the file browser dialog
-  A single project should appear in the **projects** pane of the **Import** window
-  Check the entry in the **projects** pane and click **Finish**

|image4|

.. container:: centeralign

   **Diagram 2** Import the FreeRTOS-Addin Example


2. Choose Debug/Release mode to build the project.



|image5|

.. container:: centeralign

   **Diagram 3** Build Mode Selection


3. Build the project in CrossCore Embedded Studio

-  In the **Project Explorer** right click on the **LwIP_DnsClient_CORTEX_A5_SC573** project and select the **Build Project** option from the menu

--------------

Run the Example
---------------

Follow below four steps to do debug configuration, download and run the built binary on the target board.

1. In the **Project Explorer** right click on the **LwIP_DnsClient_CORTEX_A5_SC573** project and select the **Debug As** option from the menu

2. From the popup menu select **Debug Configurations** option to create a new debug configuration that matches your emulator and target board


|image6|

.. container:: centeralign

   **Diagram 4** Set Debug Configuration


3. Disable the semihosting function in Automatic Breakpoints for CORTEX-A5



|image7|

.. container:: centeralign

   **Diagram 5** Disable the semihosting Function


.. hint::

   Semihosting I/O Mechanism 

.. raw:: html

   <details><summary>Click to expand</summary>

.. container:: center round box

      The semihosting I/O mechanism, which writes to the CCES console during debug sessions, uses SWI interrupts. This is incompatible with default GCC-compiled I/O code which also uses SWI interrupts. For this reason, stdio function calls initiated on the ARM core are routed out over UART instead and shall be read with a serial terminal external to CCES. Importantly, note that:

         
         -  This is currently only supported within FreeRTOS threads, any stdio function call performed out without a thread will crash the application.
         -  If you need to use other peripherals, please take care of that do not to change the power service clock rate (which is set in the UART I/O device)

.. raw:: html

   </details>

   


4. Click the **Debug** button to close the **Debug Configuration** window


   


|image8|

.. container:: centeralign

   **Diagram 5** Close Debug Configuration


5. Click the **Run/Resume** button or press **F5** to start running your application



|image9|

.. container:: centeralign

   **Diagram 6** Load and Run the Example


--------------

Test Results
------------

Output from the application should be visible within the TTY terminal (e.g. PuTTY/TeraTerm). You should see link is established, and IP ADDRESS assigned from DHCP server will be printed after you install the LwIP.


|image10|

.. container:: centeralign

   **Diagram 7** Example Test Results


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/examples/sc573.kou.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/examples/lwip-dns-client/573-lwip-hw.jpg
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/examples/bounded-buffer/img_0399.jpg
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/examples/lwip-dns-client/lwip_dnsclient_sc573_import_project_001.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/examples/common-cces-debug-release_001.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/examples/lwip-dns-client/lwip_dnsclient_sc573_debug_configuration_001.png
   :width: 1000px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/examples/lwip-dns-client/lwip_dnsclient_sc573_disabe_semihosting_003.png
   :width: 1000px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/examples/lwip-dns-client/lwip_dnsclient_sc573_debug_configuration_002.png
   :width: 1000px
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/examples/lwip-dns-client/lwip_dnsclient_sc573_load_application_003.png
   :width: 1000px
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/examples/lwip-dns-client/lwip_dnsclient_sc573_test_result_007.png
   :width: 1000px
