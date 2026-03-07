FAQ
===

--------------

.. container:: justify

   
   Watch Usage
   -----------
   
   <fc #4682b4>\ **1. What are the steps to be followed when a connection failure to the watch is observed?**\ </fc>
   
   .. container:: center round box

      The watch can be connected to a tool using either BLE or USB cable connection.

         
         **BLE connection:** Once the watch is reset, the tool tries to scan for BLE devices and gives a list of the MAC ID of various watches in the vicinity. The user must select the right MAC ID of their watch to complete the connection. If the user is not sure of the MAC ID, then the watch can be reset when one of the MAC IDs from the list will be removed. Once the watch comes of reset, its MAC ID will be displayed. The user can see the MAC ID of the Watch from LCD Display, by going to Settings page MAC Address page. The user can then connect to this MAC ID.
         
      **USB connection:** The user must connect the USB micro cable to establish an USB connection to the watch. Check the COM port that is identified with this connection using a HyperTerminal such as Tera Term or by observing the new COM port displayed in Device Manager-->Ports (COM & LPT) of the host machine. The user must select this COM port from the list of COM ports displayed by the Application Wavetool.

   
   <fc #4682b4>\ **2. If the log file is corrupted while streaming, then what should be done?**\ </fc>
   
   .. container:: center round box

      Try to retrieve the file again but ensure that the host machine is not doing any other task during streaming.

   
   <fc #4682b4>\ **3. How can the watch be shut down using the buttons?**\ </fc>
   
   .. container:: center round box

      From LCD Display, navigate to Settings page -> Power Off page, press Select button and then navigate to Yes or No for confirming. Press Select button once more.

   
   --------------
   
   Battery
   -------
   
   <fc #4682b4>\ **1. How long the watch must be charged?**\ </fc>
   
   .. container:: center round box

      Before using the watch for the first time, it must be charged for approximately 1 hour for the battery to get fully charged.

   
   --------------
   
   NAND Flash
   ----------
   
   <fc #4682b4>\ **1. What is the maximum size allowed to store in NAND flash?**\ </fc>
   
   .. container:: center round box

      The NAND Flash has a storage capacity of 512MB. The maximum effective size for data files storage is 511MB. The initial 1MB is used for storing certain system level parameters and information.

   
   <fc #4682b4>\ **2. How long can we log the data into flash?**\ </fc>
   
   .. container:: center round box

      The amount of time that data can be logged to flash depends on the application(s). The table below shows the time for few of the applications (assuming the battery is being charged).

         
         ============================================================ ==========
         Application(s)/User-Case                                     Time (hrs)
         ============================================================ ==========
         Use-case1 (ADPD@500Hz, ADXL@50Hz, Temp@1Hz)                  18.83
         Use-case2 (ADPD@100Hz, ADXL@50Hz, EDA@30Hz, Temp@1Hz)        63.55
         Use-case3 (ADPD@100Hz, ADXL@50Hz, ECG@250Hz, Temp@1Hz)       43.48
         Use-case4 (PPG@50Hz, ADXL@50Hz, ECG@1000Hz, Temp@1Hz         22.86
         Use-case5 (ADPD4k @100Hz from Slot F,G,H,I - 2 Channel Data) 25.37
         ADPD@50Hz – one slot and single channel                      135.31
         ADPD@100Hz – one slot and single channel                     202.96
         ECG@100Hz                                                    268.40
         EDA@30Hz                                                     488
         ============================================================ ==========
         

   
   <fc #4682b4>\ **3. What is the maximum number of files that can be stored on the NAND Flash?**\ </fc>
   
   .. container:: center round box

      The maximum number of files that can be stored on the NAND Flash is 63. This is irrespective of the space left on the NAND Flash. In case of Low touch, this limit includes the configuration file also, i.e 62 data files + 1 configuration file.

   
   <fc #4682b4>\ **4. How are the filenames on the NAND flash created?**\ </fc>
   
   .. container:: center round box

      The current file system uses 8.3 naming. This limits the length of the possible filename. File naming convention for NAND logging is: 31-12-2012 23:59:59 - MMDDTIME <2B2B4B>, we get new file named every 10 seconds. Unit value for seconds was neglected to get unique time values in hex within 4byte.

   
   <fc #4682b4>\ **5. Can a log file be removed from a list of log files on the NAND Flash?**\ </fc>
   
   .. container:: center round box

      Single log file on the NAND Flash cannot be removed. Instead the NAND Flash can be formatted to remove all log files on it.

   
   <fc #4682b4>\ **6. How can the user inject a subject ID in the log?**\ </fc>
   
   .. container:: center round box

      There is a provision in tools in the logging panel for the user to enter a 16-character subject ID which will be prefixed with a fixed key ID. This can be found at the start of the CSV log. The user can differentiate a log among a set of logs using this unique ID.

   
   --------------
   
   Sensor And Bio-Medical Applications
   -----------------------------------
   
   **A. Accelerometer (ADXL)**
   
   <fc #4682b4>\ **1. What is the measurement unit for accelerometer raw data (seen in Tools View) and the converter/multiplier to convert accelerometer raw data into unit m/s2 (9.8g)?**\ </fc>
   
   .. container:: center round box

      The ADXL 362 gives results directly in ‘g’. It has options to be configured in +/- 2g, +/- 4g or +/- 8g. And with the resolution and the value obtained from acceleration (say A) it can be converted to m/s2 as shown in table below, where value in m/s2 is obtained as (A \* Resolution \* 9.8)

         
         ============================ ========== ================
         Range                        Resolution Value in m/s2
         ============================ ========== ================
         +/-8g (Default on ADXL View) 4mg/LSB    A \* 0.004 \*9.8
         +/-4g                        2mg/LSB    A \* 0.002 \*9.8
         +/-4g                        1mg/LSB    A \* 0.001 \*9.8
         ============================ ========== ================
         

   
   **B. Photo Plethysmography**
   
   <fc #4682b4>\ **1. How is the PPG and acceleration data synchronized?**\ </fc>
   
   .. container:: center round box

      The PPG sensor (ADPD) and the acceleration sensor (ADXL) are synchronized by hardware on the PPG application. The PPG algorithm requires the same sampling frequency on both devices to perform properly under motion conditions. The ADPD and ADXL devices are configured to run in external sampling mode. The MCU triggers both the devices based on the ODR configured. Since the trigger pulses are generated from a single clock source, both are synchronized. ADPD and ADXL are also tested for synchronization when they are integer multiples of the source clock. ADPD has been tested at ODR values of 12.5,25,50,100,250,300,400,500 and 1000Hz.ADXL has been tested at ODR values of 12.5,25,50,100,200,400.

   
   --------------
   

