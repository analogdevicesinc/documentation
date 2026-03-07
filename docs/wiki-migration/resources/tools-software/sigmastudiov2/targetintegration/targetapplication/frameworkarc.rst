| :doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetapplication>`
| =====Target Framework Architecture===== The SigmaStudio+ for SHARC (ADSP-SC5xx/ADSP-215xx) Target Framework is as shown in Figure below. The six components of the Target Framework architecture are:
| 1. Audio Control Framework
| 2. Audio Process Framework
| 3. Connection
| 4. Communication
| 5. System
| 6. IPC

| ADSP SC5xx Target Framework
| |image1|
| ADSP 2157x/2158x Target Framework
| |image2|
| ADSP 2156x Target Framework
| |image3|
| =====Audio Control Framework===== The Audio Control Framework component of the Target Framework is responsible for configuring the various audio peripherals of ADSP-SC5xx/ADSP-215xx processors, receiving the audio data and rendering it out after processing. It also handles i/o data buffering. In the provided demo code, Audio Control Framework executes out of the ARM core on ADSP-SC5xx processors while it executes out of SHARC core 1 on ADSP-215xx processors. Audio Control Framework component has two interface header files namely adi_ss_arm_fw.h and adi_ss_control_fw.h. adi_ss_arm_fw.h interface header file is used while Audio Control Framework executes out of ARM core of ADSP-SC5xx variants while adi_ss_control_fw.h interface header file is used while Audio Control Framework executes out of SHARC core of ADSP-215xx variant
| =====Audio Process Framework===== The Audio Process Framework component of the Target Framework is responsible for format conversion and for processing the data as per the different algorithms in the schematic signal chain. The Audio Process Framework component runs on each of the SHARCX1 cores of ADSP-SC5xx and ADSP-215xx processors.
| =====Connection====== The Connection component of the Target Framework architecture is responsible for the physical connection with a host or microcontroller for communication. The connection component initializes the communication peripheral for data reception and transmission. SPI is used as the physical connection for communication with host/microcontroller.
| =====Communication===== The Communication component of the Target Framework architecture is responsible for the protocol parsing of the connection packets obtained from or being sent to the host/microcontroller.
| =====System===== The System component of the Target Framework architecture includes the usage of off chip resources. The following off chip resources are configured by the System component.
| • ADC
| • DAC
| • GPIO
| • Power
| =====IPC===== The IPC component of the Target Framework architecture is used for inter-core communication between ARM and SHARC cores of ADSP-SC5xx processor. IPC between cores is required for core synchronization as well as data exchange such as back channel data. IPC is accomplished using message passing mechanism between cores using shared memory. L2 memory is used as shared memory. The shared memory for IPC will be allocated at compile time with in the LDF for each of the cores.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/sc5xx.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/2157x.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/2156x.png
   :width: 400px
