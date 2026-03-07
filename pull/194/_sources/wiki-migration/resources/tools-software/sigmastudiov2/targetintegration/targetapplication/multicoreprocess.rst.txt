| :doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetapplication>`
| =====Multi Core Processing and Multi Instancing===== SigmaStudio for SHARC (ADSP-SC5xx/ADSP-215xx) Target Framework supports schematic processing on both SHARC cores. It also supports processing of multiple instances of SS+’s per SHARC core.
| Multi core processing is not supported by ADSP-2156x processors as it has a single SHARC core.
| =====Multi Core Processing===== Multi core processing involves executing SSn’s on each of the SHARC cores of ADSP-SC5xx/ADSP-2157x/ADSP-2158x processors. Multi core processing is supported in two modes namely,
| 1. Single signal chain within a schematic for each of the cores: In this mode an IC in the ‘Hardware configuration’ tab of the GUI corresponds to an instance running on both the SHARC cores. Refer to section 5.6.5 for more information on this mode.
| 2. Multiple signal chains within a schematic for each of the cores: In this mode an IC in the ‘Hardware configuration’ tab of the GUI corresponds to an instance running on either of the SHARC cores. This is the default mode for Multi core processing.
| The below sections describe the different ways of processing the input data using both the SHARC cores of ADSP-SC5xx processor in ‘Multiple signal chain’ mode.
| =====Serial Data Operation from SHARC Cores===== By default, both the SHARC cores of ADSP-SC5xx/ADSP-215xx processors process the input data serially i.e., the second SHARC core processes the output data of the first SHARC core.
| =====Parallel Data Operation from SHARC Cores===== SigmaStudio+ for SHARC (ADSP-SC5xx/ADSP-215xx) Target Framework also support parallel data processing by SHARC cores of ADSP-SC5xx/ADSP-215xx processor. In this mode of operation, each of the SHARC cores process the same input data and produce mutually exclusive outputs.
| Follow the steps below for modifying the demo Application to enable parallel data processing by SHARC cores
| 1. Open CrossCore Embedded Studio and browse the required Demo Application project from “<SigmaStudioForSHARC installation folder>\\Target\\Demo\\ADSP-SC58x\\” or “<SigmaStudioForSHARC installation folder>\\Target\\Demo\\ADSP-SC57x\\”
| 2. Change the processing mode on the input data by the SHARC cores from serial to parallel by changing the enumeration type of the SHARC framework configuration field ‘eFwConfigShCoreProcessMode’ from ‘ADI_SS_SHCORE_PROCESSMODE_SERIAL’ to ‘ADI_SS_SHCORE_PROCESSMODE_PARALLEL’. This configuration field is set in function ‘adi_ss_FW_Config()’ in files “adi_ss_app_sh0.c” and “adi_ss_app_sh1.c”
| 3. Rebuild and run the applications.
| Note that in ‘Parallel Data Operation’ from SHARC Cores, the output channels selected from SigmaStudio GUI for each of the cores must be mutually exclusive and the sum of the output channels across the cores must not be greater than ‘ADI_SS_FW_MAX_NUM_OUT_CHANNELS’.
| =====Sigma Studio+ Serial Instance===== This mode can be chosen by setting the ‘Process Mode’ field in the IC control window of all the instances running on a SHARC core to ‘Serial’ as shown in Figure 13. In serial mode of sigma studio+, the output of the first instance is the input to the subsequent sigma studio+ running on a given SHARC core.
| |image1|
| =====Sigma Studio+ Parallel Instance===== This mode can be chosen by setting the ‘Process Mode’ field in the IC control window of all the instances running on a SHARC core to ‘Parallel’ as shown in Figure 14. In parallel mode of sigma studio+, the same input is fed to all parallel SSn instances. The output channels selected from SigmaStudio GUI for each of the instances must be mutually exclusive and the sum of the output channels across the instances and cores must not be greater than ‘ADI_SS_FW_MAX_NUM_OUT_CHANNELS’.
| |image2|

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/processmode.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/processmodeparallel.png
   :width: 400px
