OSAL DFP for FreeRTOS
=====================

For the Cortex-M33 core in the ADSP-SC83x family, an additional DFP is required to provide OSAL for FreeRTOS. OSAL is the O/S Abstraction Layer and is used in ADI library and driver code to support different O/S options via a consistent API to avoid having to rebuild libraries. Currently support is available for bare metal ("No-OS") and FreeRTOS. No-OS is installed by default, and FreeRTOS needs an additional pack file to be installed.

To install via the CMSIS index
------------------------------

Open the **CMSIS Pack Manager** via **Window** > **Perspective** > **Open Perspective** > **Other**, then select **CMSIS Pack Manager** and then click **Open**.

Click on the **Check for Updates on the Web** icon, which is the blue arrows:

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/cmsis_web_update.jpg
   :width: 400px

Find the **AnalogDevices.ADSP-SC83x_FreeRTOS-OSAL** pack and click install:

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/cmsis_m33_pack_install.jpg
   :width: 400px

Finally, agree to the license and click **OK**.

The pack should then be available via the **system.rteconfig** file at the top level of your project.

To install directly
-------------------

Download the pack file from here: `AnalogDevices.ADSP-SC83x_FreeRTOS-OSAL.1.0.0.pack <https://download.analog.com/tools/EZBoards/ADSP-SC83x/Releases/AnalogDevices.ADSP-SC83x_FreeRTOS-OSAL.1.0.0.pack>`__

Open the **CMSIS Pack Manager** via **Window** > **Perspective** > **Open Perspective** > **Other**, then select **CMSIS Pack Manager** and then click **Open**.

Click on the **Import Pack** Icon, which is the folder:

Browse to and select the downloaded file, agree to the license text and click **OK**

The pack should then be available via the **system.rteconfig** file at the top level of your project.

Selecting the FreeRTOS OSAL
---------------------------

In your **system.rteconfig**, you need to select **Device** > **OSAL** > **FreeRTOS**.

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos_osal_rteconfig.jpg
   :width: 400px

You will also need need **Device** > **Runtime** > **OSAL API**, though this will be added by clicking on **Resolve** at the top if not selected manually.
