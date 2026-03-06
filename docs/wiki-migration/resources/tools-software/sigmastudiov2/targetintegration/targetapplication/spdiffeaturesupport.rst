| :doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetapplication>`
| ====== Enabling S/PDIF Transmitter Feature support In Example Demo applications ====== The S/PDIF transmitter feature is supported on all **ADSP-SC5xx/ADSP-215xx** processors with the existing example demo application.
| This feature can be used to transmit S/PDIF data from the evaluation boards.
| The steps described below are to be followed to use this feature:-
| **Step 1**:
| Add the compiler preprocessor “\ **SPDIF_TX_ENABLE**\ ” to each CCES project (for each core) as shown in below figures.
| a) Right-Click on the project folder and select **Properties**. |image1|
| b) Click on the "**+**" (**Add**) button in **Preprocessor definitions** window. |image2|
| c) Enter the Macro “\ **SPDIF_TX_ENABLE**\ ” and click **Apply and Close**.
| |image3|
| Make sure similar changes are made to all the core projects and rebuild the entire target framework application.
| **Step 2**:
| In the SigmaStudioPlus SPORT Configuration tab, add one more sink for the S/PDIF transmitter output. The SPORT configuration tab can be opened from Project window as shown in below figure.
| |image4|

.. container:: centeralign

   **Figure: \*\* SPORT configuration Tab


.. note::

   The SPORT selection must be done based on DAI pin group. The DAI pin for the S/PDIF Tx data to ASRC can be changed in SRU routing based on developer requirement and the change should be done in SigmaStudioPlus schematic SPORT configuration.


Assign the desired SPORT channel based on the DAI pin group:

-  For DAI0 – SPORT 0A, 0B, 1A, 1B, 2A, 2B, 3A, and 3B.
-  For DAI1 – SPORT 4A, 4B, 5A, 5B, 6A, 6B, 7A, and 7B.

From the drop-down menu in the configuration section, select the S/PDIF Tx SPORT channel and update the required settings as follows:

-  2 channels
-  I2S format
-  24-bit width
-  Frame sync and bit clock polarity.

| Please refer the below figure.
| |image5|

.. container:: centeralign

   **Figure: **Framework Configuration for S/PDIF Transmitter support


**\ Step 3*\*:
| The DAI pin to be used for the S/PDIF Tx feature is mentioned in the below table which varies for each target evaluation platform.
| ^ **Evaluation Target Platform** ^ **S/PDIF Tx SPORT DAI Pin To ASRC** ^ \**S/PDIF Tx Data DAI Pin **^ \| ADSP-21569 EZ-KIT\| DAI0 Pin 02 \| DAI0 Pin 10 \| \| ADSP-21569 SOM-CRR EZ-KIT\| DAI0 Pin 11 \| DAI0 Pin 10 \| \| ADSP-21593/ADSP-SC594 SOM-CRR EZ-KIT\| DAI0 Pin 06 \| DAI0 Pin 10 \| \| ADSP-SC584/ADSP-SC589 EZ-KIT\| DAI0 Pin 06 \| DAI0 Pin 20 \| \| ADSP-SC573 EZ-KIT\| DAI0 Pin 18 \| DAI0 Pin 10 \|

.. container:: centeralign

   **\ Table: **DAI Pins Used for S/PDIF Tx Feature


.. note::

   The DAI pin on each ADSP-SC5xx/ADSP-215xx evaluation boards which currently supports the S/PDIF Tx feature is mentioned in the above Table. The same DAI pin must be assigned in the SigmaStudioPlus schematic SPORT configuration for S/PDIF Tx Sink.


**\ Step 4*\*:
| Once the sport configuration changes have been completed, regenerate the config file and overwrite the existing config file in the framework using “\ **Generate Configuration File**\ ” option in SigmaStudioPlus's **Processor Settings** Tab as shown in below figure. |image6|

.. container:: centeralign

   **Figure: **Processor Settings


.. container:: centeralign

   **\ Figure: **Generating Configuration File in SigmaStudioPlus


\* The generated config file for ADSP-2156x processor must be overwritten as adi_ss_fw_config_2156x.h in “\ C:\\Analog Devices\\SigmaStudioPlus-Relx.y.z\\Target\\Examples\\Framework\\Include\ ” folder. \* For ADSP-SC5xx/ADSP-215xx processors, generated config file must be overwritten as adi_ss_fw_config.h in the same “\ C:\\Analog Devices\\SigmaStudioPlus-Relx.y.z\\Target\\Examples\\Framework\\Include\ ” folder.

.. container:: centeralign

   **\ Figure: **Framework related file's path


**\ Step 5\ **:
  In SigmaStudioPlus schematic, connect the audio data channels to the output channels 8 and 9, in order to route the data to SPORT of S/PDIF Tx as shown in below figure.

.. container:: centeralign

   **\ Figure: **SPDIF Output


**\ Step 6\ **:
  Rebuild the example demo application to generate the DXEs.
  **\ Step 7*\*:

  | With all the above changes incorporated, the target application and SigmaStudioPlus schematic application is ready to support the S/PDIF Tx feature.
|

.. note::

   
   -  For ADSP-21569 EZ-KIT the SRU configuration should be updated as **DAI0_PB_02_O → SPDIF0_TX_DAT_I** for SPDIF Tx Data input. All other Eval boards, the SPDIF Tx data input pins were assigned in SRU by default.
   -  The S/PDIF Tx feature is not supported for ADSP-SC589 Mini evaluation board.
   


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/prop1.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/prop2.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/prop3.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/sport_configuration_tab.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/sinksportconfig.png
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/processor_settings.png
