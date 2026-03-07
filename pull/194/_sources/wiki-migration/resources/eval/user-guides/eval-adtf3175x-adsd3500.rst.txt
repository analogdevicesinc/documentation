ADSD3500 Guide
==============

.. important::

   The latest ADSD3500 firmware version is **7.0.0**.


Host Processor Integration Guide
--------------------------------

Software System Overview
~~~~~~~~~~~~~~~~~~~~~~~~

ADSD3500 is a Depth Compute Image Signal Processor (ISP) for the ADI ToF CW CMOS imaging sensors. It converts the raw frame captures from the sensor to Depth data and Active Brightness (AB) image, along with a confidence frame. ADSD3500 shall support ADSD3100 and ADSD3030 imagers and future imaging sensors if the input data format is compatible with the current imaging sensors and up to a maximum resolution of 1MP.

Host Protocol Design Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Host Protocol is software module implemented in ADSD3500 Firmware to interact with Host. Through this module, Host can,

-  Configure and control the ADSD3500 ISP
-  Get the status of ADSD3500 ISP
-  Configure Imager Module attached to ADSD3500 ISP
-  Upgrade the Flash content on the Module (Imager Firmware, Calibration Data, ADSD3500 Firmware, Configuration Parameters
-  Read the Debug/Diagnostic information stored in Flash

Standard mode and Burst mode commands are implemented to achieve the above functionalities. Supported communication channels between Host and ADSD3500 are I2C, SPI and I3C. Host works as Master in the system. Bootstraps pins #0, #1 and #2 are used to select the communication channel as follows.

+----------------+-----------------------------------------------------------------------------------------------------------------------------+
| Bootstrap Pins | Description                                                                                                                 |
| {BS3, BS1}     |                                                                                                                             |
+================+=============================================================================================================================+
| b00            | I2C Slave Interface to HOST (With Static I2C address as 0x70/0x71)                                                          |
+----------------+-----------------------------------------------------------------------------------------------------------------------------+
| b01            | SPI Slave Interface to HOST                                                                                                 |
+----------------+-----------------------------------------------------------------------------------------------------------------------------+
| b10            | I2C Slave Interface to HOST (With Static I2C address as 0x80/0x81)                                                          |
+----------------+-----------------------------------------------------------------------------------------------------------------------------+
| b11            | I3C Slave Interface to HOST (Use static I2C address as 0x70/0x71 – Used by I3C master for quick Dynamic address allocation) |
+----------------+-----------------------------------------------------------------------------------------------------------------------------+

Commands
~~~~~~~~

-  There are two command groups:

   -  Standard
   -  Burst

-  Standard commands are used to read or write 16-bits of data.
-  Burst commands are used to read or write more than 16-bits of data.
-  The ADSD3500 needs to be switched between the two modes. As a result, there is a standard mode command to switch to bust mode and a burst mode command to switch to standard mode.
-  For switching from Standard Mode to Burst Mode see the command Standard Mode command **Switch to Burst Mode**.
-  For switching from Burst Mode to Standard Mode see the command Burst Mode command **Switch to Standard Mode**.

.. important::

   It is recommended that for READ commands, a delay be inserted between the command write operation and the data read operation. This is more critical for I2C rates above 400KHz, where a delay of 1ms should be used.


STANDARD MODE COMMANDS
~~~~~~~~~~~~~~~~~~~~~~

Write Operations
^^^^^^^^^^^^^^^^

-  Write: <2-bytes for command ID> <2-bytes of data>

   -  For example, to set the frame rate to 30 fps (represented as 0x1E), the host needs to send:

      -  Command: 0x0022 and Data: 0x001E
      -  The complete host command becomes: W 00 22 00 1E

-  How the ADSD3500 interprets this

   -  The way the command and data are interpreted depends on the byte order used by the host. If the host sends LSB first, it transmits 0x22 before 0x00. If it sends MSB first, it transmits 0x00 before 0x22.
   -  Regardless of the byte order, the ADSD3500 always places the first received byte into the lowest memory address. So, if the host sends 0x22 first, the ADSD3500 stores it at the lower address, resulting in the command being interpreted as 0x2200.
   -  The same logic applies to the data. If the host sends 0x1E first, the ADSD3500 stores it at the lower address, forming 0x1E00. Internally, the ADSD3500 swaps the bytes to interpret the actual value as 0x001E, which corresponds to 30 fps.

Read Operations
^^^^^^^^^^^^^^^

-  Write: <2-bytes for command ID>
-  Read: <2-bytes of data>

   -  For Example, to get the frame rate, the host needs to send:
   -  Command: 0x0023
   -  The complete host command becomes: R 00 23

-  While receiving on host, the ADSD3500 sends as 0x000A (10 fps)

--------------

General Operations
^^^^^^^^^^^^^^^^^^

| **Name**: Switch to Burst Mode
| **Type**: Write
| **Description**: This command has to be executed before executing any burst mode commands.
| **Operations**:

===== ======
Write 0x0019
Write 0x0000
===== ======

| **Name**: Communications Test Register
| **Type**: Read
| **Description**: This register is used to check if the communication channel between the host and ADSD3500 is active.
| **Operations**:

===== ======
Write 0x0112
Read  0x5931
===== ======

| **Name**: Read ADSD3500 Chip Id
| **Type**: Read
| **Description**: Reads the Depth ISP (ADSD3500) Chip Id
| **Operations**:

===== ======
Write 0x0113
Read  0x3500
===== ======

| **Name**: Read Imager Chip Id
| **Type**: Read
| **Description**: Reads the Imager Chip Id.
| **Operations**:

===== ========================================================
Write 0x0115
Read  0x5931 - ADSD3100
      0xBD6y - ADSD3030, where 'y' denotes the revision number
===== ========================================================

| **Name**: Reset the ADSD3500
| **Type**: Write
| **Description**: Performs a soft reset of the ADSD3500.
| **Operations**:

===== ======
Write 0x0024
Write 0x0000
===== ======

Control Operations
""""""""""""""""""

| **Name**: Stream On
| **Type**: Write
| **Description**: Starts the imager and consequently the ASDSD3500 from streaming frames.
| **Operations**:

===== ======
Write 0x00AD
Write 0x00C5
===== ======

| **Name**: Stream Off
| **Type**: Write
| **Description**: Stops the imager and consequently the ASDSD3500 from streaming frames.
| **Operations**:

===== ======
Write 0x000C
Write 0x0002
===== ======

| **Name**: Set imager Mode
| **Type**: Write
| **Description**: Sets the imager Mode , number of MIPI lanes of ADSD3500 and configures depth, AB and confidence bits.
| **Operations**:

===== ======================================================
Write 0xDA\ **XX**
      **XX** → imager mode value.
      i.e., for mode 7 it should be 7.
      Supported modes are 0 to 10.
Write 0x\ **YYYY**
      **YYYY** – ADSD3500 mode setting is decoded as follow:
      Bit 0:  Depth is enabled (1)/Disabled (0) 
      Bit 1: Data interleaving (1)/Virtual channel (0)
      Bit 2: AB Enabled (1)/Disabled (0)
      Bit 3: AB averaging Enabled (1)/Disabled (0)
      Bit 6,5,4: Number of bits in Depth/Phase
      \* 000 → 16-bits
      \* 010 → 12-bits
      Bit 9,8,7: Number of bits in AB 
      \* 000 → 16-bits
      \* 100 → 8-bits
      Bit 11,10: Confidence
      \* 00 → Confidence Disabled
      \* 01 → 4-bits confidence
      \* 10 → 8bits Confidence
      Bit 13,12: MIPI Lanes
      \* 00 → 0 output MIPI lanes
      \* 01 → 1 output MIPI lane
      \* 10 → 2 output MIPI lane
      Bit 15,14: Reserved
===== ======================================================

| **Name**: Read imager Mode
| **Type**: Read
| **Description**: Reads the current mode of the imager.
| **Operations**:

+-------+----------------------------------------------------------------------+
| Write | 0x0012                                                               |
+-------+----------------------------------------------------------------------+
| Read  | Returns the current imager mode. Value returned is between 0 and 10. |
+-------+----------------------------------------------------------------------+

| **Name**: Get Status
| **Type**: Read
| **Description**: Reads the status of ADSD3500.
| **Operations**:

+-------+-----------------------------------------------------------------------------------------------------+
| Write | 0x0020                                                                                              |
+-------+-----------------------------------------------------------------------------------------------------+
| Read  | Status of the ADSD3500                                                                              |
|       | \* 0x01 ADI_STATUS_INVALID_MODE                                                                     |
|       | \* 0x02 ADI_STATUS_INVALID_JBLF_FILTER_SIZE                                                         |
|       | \* 0x03 ADI_STATUS_UNSUPPORTED_CMD                                                                  |
|       | \* 0x04 ADI_STATUS_INVALID_MEMORY_REGION                                                            |
|       | \* 0x05 ADI_STATUS_INVALID_FIRMWARE_CRC                                                             |
|       | \* 0x06 ADI_STATUS_INVALID_IMAGER                                                                   |
|       | \* 0x07 ADI_STATUS_INVALID_CCB                                                                      |
|       | \* 0x08 ADI_STATUS_FLASH_HEADER_PARSE_ERROR                                                         |
|       | \* 0x09 ADI_STATUS_FLASH_FILE_PARSE_ERROR                                                           |
|       | \* 0x0A ADI_STATUS_SPIM_ERROR                                                                       |
|       | \* 0x0B ADI_STATUS_INVALID_CHIPID                                                                   |
|       | \* 0x0C ADI_STATUS_IMAGER_COMMUNICATION_ERROR                                                       |
|       | \* 0x0D ADI_STATUS_IMAGER_BOOT_FAILURE                                                              |
|       | \* 0x0E ADI_STATUS_FIRMWARE_UPDATE_COMPLETE                                                         |
|       | \* 0x0F ADI_STATUS_NVM_WRITE_COMPLETE                                                               |
|       | \* 0x10 ADI_STATUS_IMAGER_ERROR                                                                     |
|       | \* 0x11 ADI_STATUS_TIMEOUT_ERROR                                                                    |
|       | \* 0x13 ADI_STATUS_DYNAMIC_MODE_SWITCHING_NOT_ENABLED                                               |
|       | \* 0x14 ADI_STATUS_INVALID_DYNAMIC_MODE_COMPOSITIONS                                                |
|       | \* 0x15 ADI_STATUS_INVALID_PHASE_INVALID_VALUE (Note : To get the Status , Switch to Standard Mode) |
|       | \* 0x16 ADI_STATUS_CCB_WRITE_COMPLETE                                                               |
|       | \* 0x17 ADI_STATUS_INVALID_CCB_WRITE_CRC                                                            |
|       | \* 0x18 ADI_STATUS_CFG_WRITE_COMPLETE                                                               |
|       | \* 0x19 ADI_STATUS_INVALID_CFG_WRITE_CRC                                                            |
|       | \* 0x1A ADI_STATUS_INIT_FW_WRITE_COMPLETE                                                           |
|       | \* 0x1B ADI_STATUS_INVALID_INIT_FW_WRITE_CRC                                                        |
|       | \* 0x1C ADI_STATUS_INVALID_BIN_SIZE                                                                 |
|       | \* 0x1D ADI_STATUS_ACK_ERROR                                                                        |
|       | \* 0x1E ADI_STATUS_FLASH_STATUS_CHUNK_ALREADY_FOUND                                                 |
|       | \* 0x1F ADI_STATUS_INI_ENTRY_UPDATE_COMPLETE                                                        |
|       | \* 0x20 ADI_STATUS_INI_ENTRY_UPDATE_INCORRECT_MODE                                                  |
|       | \* 0x21 ADI_STATUS_INI_ENTRY_UPDATE_INCORRECT_CRC                                                   |
|       | \* 0x22 ADI_STATUS_INVALID_INI_UPDATE_IN_PCM_MODE                                                   |
|       | \* 0x23 ADI_STATUS_UNSUPPORTED_MODE_INI_READ                                                        |
|       | \* 0x24 ADI_STATUS_P0_MAXIMUM_LIMIT_REACHED                                                         |
|       | \* 0x25 ADI_STATUS_GPIO12_ERROR                                                                     |
|       | \* 0x26 ADI_STATUS_SECOND_ADSD3500_BOOT_FAILURE                                                     |
|       | \* 0x27 ADI_STATUS_SECOND_FIRMWARE_WRITE_COMPLETE                                                   |
|       | \* 0x28 ADI_STATUS_INVALID_SECOND_FIRMWARE_WRITE_CRC                                                |
|       | \* 0x29 ADI_STATUS_STREAM_OFF_COMMAND_RECEIVED                                                      |
|       | \* 0x2A ADI_STATUS_INVALID_GPIO_ACCESS                                                              |
|       | (In Dual ADSD3500, if user tries to access GPIO18, Firmware raises this error state)                |
|       | \* 0x2B ADI_STATUS_READ_CCB_OR_CFG_CRC_MISMATCH                                                     |
|       | \* 0x2C ADI_STATUS_CONFIG_CCB_CRC_MISMATCH                                                          |
|       | \* 0x2D ADI_STATUS_CONFIG_CFG_CRC_MISMATCH                                                          |
+-------+-----------------------------------------------------------------------------------------------------+

| **Name**: Get imager Error Code
| **Type**: Read
| **Description**: Reads the imager Error code.
| **Operations**:

===== =============================================
Write 0x0038
Read  Reads 16-bit error code from ADSD3100 imager.
===== =============================================

| **Name**: Set Framerate
| **Type**: Write
| **Description**: Sets the Frame rate of the imager.
| **Operations**:

===== ===================
Write 0x0022
Write Desried frame rate.
===== ===================

| **Name**: Get Framerate
| **Type**: Read
| **Description**: Reads the frame rate.
| **Operations**:

===== ===========================
Write 0x0023
Read  The current frame rate set.
===== ===========================

| **Name**: Enable FSYNC Trigger Control
| **Type**: Write
| **Description**: Command to start or stop triggering frame sync (FSYNC). **Operations**:

+-------+----------------------------------------------------------------------------------+
| Write | 0x0025                                                                           |
+-------+----------------------------------------------------------------------------------+
| Write | \* 0x0000 - ADSD3500 Firmware stops triggering the FSYNC after processing frame. |
|       | \* 0x0001 - ADSD3500 Firmware Starts triggering the FSYNC.                       |
|       | \* 0x0002 - ADSD3500 Firmware set FSYNC signal to high impedance state.          |
+-------+----------------------------------------------------------------------------------+

| **Name**: Get FSYNC Trigger Control Status.
| **Type**: Read
| **Description**: Reads the FSYNC Trigger Control Status.
| **Operations**:

+-------+----------------------------------------------------------------------------------+
| Write | 0x0097                                                                           |
+-------+----------------------------------------------------------------------------------+
| Read  | \* 0x0000 - ADSD3500 Firmware stops triggering the FSYNC after processing frame. |
|       | \* 0x0001 - ADSD3500 Firmware Starts triggering the FSYNC.                       |
|       | \* 0x0002 - ADSD3500 Firmware set FSYNC signal to high impedance state.          |
+-------+----------------------------------------------------------------------------------+

| **Name**: Manually trigger FSYNC
| **Type**: Write
| **Description**: This command triggers the FSYNC. **Enable FSYNC Trigger Control** command must be called with data = 0x00, prior to calling this command. otherwise ADSD3500 just ignores this command.
| **Operations**:

===== ======
Write 0x0026
Write 0x0000
===== ======

| **Name**: Get imager Type and CCB Version
| **Type**: Read
| **Description**: Reads the imager type and CCB version.
| **Operations**:

===== ================
Write 0x0032
Read  0:7 CCB Version
      \* 1 - Version 0
      \* 2 - Version 1
      8:15 imager Type
      \* 1 - ADSD3100
      \* 2 - ADSD3030
===== ================

| **Name**: Get CCB Header Version
| **Type**: Read
| **Description**: Reads the CCB Header version.
| **Operations**:

===== =======================
Write 0x0039
Read  0:15 CCB Header Version
===== =======================

| **Name**: Enable/Disable Output metadata Header in AB Frame
| **Type**: Write
| **Description**: Option to Enable or Disable the output Metadata header oin AB Frame.
| **Operations**:

===== ===========================================
Write 0x0036
Write \* 0 - Disable metadata header in AB Frame.
      \* 1 - Enable metadata header in AB Frame.
===== ===========================================

| **Name**: Get Output metadata Header in AB Frame status
| **Type**: Read
| **Description**: Reads the status of enable/disable metadata header in AB Frame.
| **Operations**:

===== ====================================================
Write 0x0037
Read  \* 0x0000 - metadata header in AB Frame is Disabled.
      \* 0x0001 - metadata header in AB Frame is Enabled.
===== ====================================================

| **Name**: Set MIPI output speed
| **Type**: Write
| **Description**: Sets the ADSD3500 output MIPI speed.
| **Operations**:

+-------+--------------------------------------------------------------------------------+
| Write | 0x0031                                                                         |
+-------+--------------------------------------------------------------------------------+
| Write | Set the firmware output MIPI speed per lane from any of the predefined values. |
|       | 0xYY is any of the following values:                                           |
|       | 0x01 - 2.5 Gbps,                                                               |
|       | 0x02 - 2 Gbps,                                                                 |
|       | 0x03 - 1.5 Gbps,                                                               |
|       | 0x04 - 1 Gbps,                                                                 |
|       | 0x05 - 800 Mbps,                                                               |
|       | 0x06 - 500 Mbps,                                                               |
|       | 0x07 - 400 Mbps,                                                               |
|       | 0x08 - 250 Mbps                                                                |
+-------+--------------------------------------------------------------------------------+

| **Name**: Get MIPI output speed
| **Type**: Read
| **Description**: Reads the ADSD3500 output MIPI speed.
| **Operations**:

===== ====================================
Write 0x0034
Read  Returns one of the following values:
      0x01 - 2.5 Gbps,
      0x02 - 2 Gbps,
      0x03 - 1.5 Gbps,
      0x04 - 1 Gbps,
      0x05 - 800 Mbps,
      0x06 - 500 Mbps,
      0x07 - 400 Mbps,
      0x08 - 250 Mbps
===== ====================================

| **Name**: Set Acquisition Delay
| **Type**: Write
| **Description**: Sets the Acquisition Delay.
| Acquisition Delay × (Integration Time + [10us to 20us]) = Delay from FSYNC
| **Operations**:

===== ====================================================
Write 0x0066
Write Write the 16-bit value that controls delay of VCSEL.
===== ====================================================

| **Name**: Get Delay from FSYNC
| **Type**: Read
| **Description**: Reads the Delay from FSYNC.
| Acquisition Delay × (Integration Time + [10us to 20us]) = Delay from FSYNC
| **Operations**:

===== =========================================================
Write 0x0068
Read  Reads the 16-bit delay value from Imager sensor register.
===== =========================================================

| **Name**: Get Acquisition Delay
| **Type**: Read
| **Description**: Reads the Acquisition Delay.
| Acquisition Delay × (Integration Time + [10us to 20us]) = Delay from FSYNC
| **Operations**:

===== ====================================================
Write 0x00B3
Read  Reads the 16-bit value that controls delay of VCSEL.
===== ====================================================

Depth Control Operations
^^^^^^^^^^^^^^^^^^^^^^^^

| **Name**: Set AB Invalidation Threshold
| **Type**: Write
| **Description**: Sets the AB Invalidation Threshold value.
| Any pixel with at least one per-frequency active brightness value below AB Invalidation Threshold value will have an invalid depth value. To turn off per-frequency active brightness invalidation, set AB Invalidation Threshold value as 0.
| If AB Invalidation Threshold value is increased the invalidation increases, while noise and range decrease and vice-versa.
| **Operations**:

+-------+------------------------------------------------------------------------------------------------------------+
| Write | 0x0010                                                                                                     |
+-------+------------------------------------------------------------------------------------------------------------+
| Write | 0 to 0xFFFFF - the 16-bit AB Invalidation to be set. Threshold value would be scaled by Number of Freqs/2. |
+-------+------------------------------------------------------------------------------------------------------------+

| **Name**: Get AB Invalidation Threshold
| **Type**: Read
| **Description**: Reads the AB Invalidation Threshold value.
| **Operations**:

===== ==============================================================
Write 0x0015
Read  Invalidation threshold. Returned value is between 0 to 0xFFFF.
===== ==============================================================

| **Name**: Set Confidence Threshold
| **Type**: Write
| **Description**: Sets the Confidence Threshold value.
| Any pixel with a phase unwrapping confidence value larger than Confidence Threshold will have an invalid depth value. To turn off, set confidence Threshold to 255 (maximum value - FFFF).
| If Confidence threshold value is increased the invalidation decreases while depth error may increase and vice-versa.
| **Operations**:

===== ===========
Write 0x0011
Write 0 to 0xFFFF
===== ===========

| **Name**: Get Confidence Threshold
| **Type**: Read
| **Description**: Reads the Confidence Threshold value.
| **Operations**:

===== ============================================================
Write 0x0016
Read  Confidence threshold. Returned value is between 0 to 0xFFFF.
===== ============================================================

| **Name**: Enable/Disable JBLF Filter
| **Type**: Write
| **Description**: Option to enable or disable JBLF Filter.
| A flag to determine whether to apply edge-preserving, and noise-reducing smoothing Joint Bilateral Filtering technique on the input data.
| **Operations**:

===== ================================
Write 0x0013
Write \* 0x0000 - Disable JBLF filter.
      \* 0x0001 - Enable JBLF filter.
===== ================================

| **Name**: Get JBLF Filter Status
| **Type**: Read
| **Description**: Read the JBLF Filter enable/disable status.
| **Operations**:

===== =================================
Write 0x0017
Read  \* 0x0000 - JBLF filter disabled.
      \* 0x0001 - JBLF filter enabled.
===== =================================

| **Name**: Set JBLF Filter Size
| **Type**: Write
| **Description**: Sets the JBLF Filter Size
| Size of spatial or gaussian kernel is set to JBLF (Filter Size x JBLF Filter Size) pixels. Increasing the size will further reduce noise at the expense of computation cost (compute power).
| **Operations**:

===== =============================
Write 0x0014
Write JBLF filter size = 3, 5 or 7.
===== =============================

| **Name**: Get JBLF Filter Size
| **Type**: Read
| **Description**: The JBLF Filter Size.
| **Operations**:

===== ====================================
Write 0x0018
Read  Current JBLF filter size; 3, 5 or 7.
===== ====================================

| **Name**: Set JBLF Max Edge Threshold
| **Type**: Write
| **Description**: Sets the JBLF Max Edge Threshold.
| It defines the depth “edgeness” above which a pixel depth value is invalid.
| **Operations**:

===== =======================================================
Write 0x0074
Write 0xZZZZ is the 16-bit jblf Max Edge threshold to be set.
===== =======================================================

| **Name**: Set JBLF AB Threshold
| **Type**: Write
| **Description**: Sets the JBLF AB Threshold.
| If a pixel per-frequency active brightness is below jblfABThreshold, jblfMaxEdgeThreshold it disables edge invalidation for that pixel.
| **Operations**:

+-------+---------------------------------------------------------------------------------------------------------+
| Write | 0x0075                                                                                                  |
+-------+---------------------------------------------------------------------------------------------------------+
| Write | 0xZZZZ is the 16-bit JBLF AB threshold to be set. Threshold value would be scaled by Number of Freqs/2. |
+-------+---------------------------------------------------------------------------------------------------------+

| **Name**: Get JBLF Gaussian Sigma
| **Type**: Read
| **Description**: Reads the JBLF Gaussian Sigma value.
| **Operations**:

===== =================================
Write 0x0069
Read  16-bit JBLF Gaussian sigma value.
===== =================================

| **Name**: Set JBLF Gaussian Sigma
| **Type**: Write
| **Description**: Sets the JBLF Gaussian Sigma value.
| It defines the width of the Gaussian kernel in the noise reduction filter.
| Setting a small value effectively disables the noise reduction. Setting a value much larger than JBLF Filter Size (such as 100) provides the largest amount of noise reduction (increases depth range) at the expense of a blurrier depth image.
| **Operations**:

===== ==============================
Write 0x006B
Write Set JBLF Gaussian sigma value.
===== ==============================

| **Name**: Get JBLF Exponential Term
| **Type**: Read
| **Description**: Reads the JBLF Exponential Term.
| **Operations**:

===== =============================
Write 0x006A
Read  16-bit JBLF Exponential Term.
===== =============================

| **Name**: Set JBLF Exponential Term
| **Type**: Write
| **Description**: Sets the JBLF Exponential Term.
| It defines the amount of depth edge preservation in the noise reduction filter. Set JBLF Exponential Term as 0 to disable edge preservation. Set large value to preserve more depth edges.
| **Operations**:

===== =============================
Write 0x006C
Write JBLF Exponential Term to set.
===== =============================

| **Name**: Get Radial Threshold Minimum
| **Type**: Read
| **Description**: Reads the Radial Threshold Minimum value.
| **Operations**:

===== ====================================================
Write 0x0028
Read  Reads a 16-bit radial threshold min value to be set.
===== ====================================================

| **Name**: Set Radial Threshold Minimum
| **Type**: Write
| **Description**: Sets the Radial Threshold Minimum value.
| Radial Threshold value is used to invalidate the depth output based on the value of radial depth. If the radial depth value is less than the Radial Threshold Minimum, then the depth output will be invalidated.
| **Operations**:

===== =====================================================
Write 0x0027
Write Writes a 16-bit radial threshold min value to be set.
===== =====================================================

| **Name**: Get Radial Threshold Maximum
| **Type**: Read
| **Description**: Reads the Radial Threshold Maximum value.
| **Operations**:

===== ====================================================
Write 0x0030
Read  Reads a 16-bit radial threshold max value to be set.
===== ====================================================

| **Name**: Set Radial Threshold Maximum
| **Type**: Write
| **Description**: Sets the Radial Threshold Maximum value.
| If the radial depth value is greater than the Radial Threshold Maximum, then the depth output will be invalidated.
| **Operations**:

===== =====================================================
Write 0x0029
Write Writes a 16-bit radial threshold max value to be set.
===== =====================================================

| **Name**: Get Sensor Temperature
| **Type**: Read
| **Description**: Reads the sensor Temperature.
| **Operations**:

===== =============================================
Write 0x0054
Read  Reads 16-bit Sensor temperature in degrees C.
===== =============================================

| **Name**: Get Laser Temperature
| **Type**: Read
| **Description**: Reads the Laser Temperature.
| **Operations**:

===== ============================================
Write 0x0055
Read  Reads 16-bit Laser temperature in degrees C.
===== ============================================

| **Name**: Enable/Disable Phase Value Invalidation
| **Type**: Write
| **Description**: Option to Enable or Disable phase invalidation.
| **Operations**:

===== ============================================
Write 0x0072
Write \* 0x0000 - Disable Phase Value Invalidation
      \* 0x0001 - Enable Phase Value Invalidation
===== ============================================

| **Name**: Get Enable/Disable Phase Value Invalidation
| **Type**: Read
| **Description**: Option to Read Enable or Disable phase value invalidation.
| **Operations**:

===== =============================================
Write 0x009E
Read  \* 0x0000 - Disabled Phase Value Invalidation
      \* 0x0001 - Enabled Phase Value Invalidation
===== =============================================

| **Name**: Enable/Disable Edge Confidence
| **Type**: Write
| **Description**: Option to enable or disable the JBLF Edge confidence
| When JBLF Egde confidence is enabled
| Confidence 8 bits -> Dealias confidence - MSB 4 bits and JBLF Edge confidence - LSB 4 bits.
| **Operations**:

===== ====================================
Write 0x0062
Write \* 0x0000 - Disable Edge Confidence.
      \* 0x0001 - Enable Edge Confidence.
===== ====================================

| **Name**: Get Enable/Disable Edge Confidence
| **Type**: Read
| **Description**: Option to get enable or disable status of the JBLF Edge confidence
| When JBLF Egde confidence is enabled
| Confidence 8 bits -> Dealias confidence - MSB 4 bits and JBLF Edge confidence - LSB 4 bits.
| **Operations**:

===== =====================================
Write 0x009F
Read  \* 0x0000 - Disabled Edge Confidence.
      \* 0x0001 - Enabled Edge Confidence.
===== =====================================

| **Name**: Enable/Disable Temperature Compensation
| **Type**: Write
| **Description**: Option to enable or disable the temperature compensation.
| **Operations**:

===== =============================================
Write 0x0021
Write \* 0x0000 - Disable temperature compensation.
      \* 0x0001 - Enable temperature compensation.
===== =============================================

| **Name**: Get Temperature Compensation Status
| **Type**: Read
| **Description**: Reads the temperature compensation status.
| **Operations**:

===== =================================================
Write 0x0076
Read  \* 0x0000 - Temperature Compensation is Disabled.
      \* 0x00001 - Temperature Compensation is Enabled.
===== =================================================

| **Name**: Enable/Disable 1PPS Timer Mode
| **Type**: Write
| **Description**: Option to enable or disable 1PPS Timer mode.
| **Operations**:

===== ===============================
Write 0x006D
Write \* 0x0000 - Free-Wheeling mode.
      \* 0x0001 - 1PPS Mode.
===== ===============================

| **Name**: Enable/Disable Dynamic Mode Switching
| **Type**: Write
| **Description**: Option to enable or disable Dynamic Mode switching. **MUST BE ENABLED BEFORE CONFIGURING OTHER DYNAMIC MODE SWITCHING REGISTERS**
| **Operations**:

+-------+--------------------------------------------------------------------------------------------+
| Write | 0x0080                                                                                     |
+-------+--------------------------------------------------------------------------------------------+
| Write | \* 0x0000 - Disable dynamic mode switching. \\\\\* 0x0001 - Enable dynamic mode switching. |
+-------+--------------------------------------------------------------------------------------------+

| **Name**: Set Dynamic Sequence Composition0
| **Type**: Write
| **Description**: This command is applicable only when Dynamic mode switching is enabled.
| This field shows first four mode numbers of the sequence in dynamic mode switching.
| **Operations**:

===== ==============================================
Write 0x0081
Write 0xYYYY
      modes m3 [12:15], m2 [11:8], m1 [7:4] m0 [3:0]
===== ==============================================

| **Name**: Set Dynamic Sequence Composition1
| **Type**: Write
| **Description**: These commands is applicable only when Dynamic mode switching is enabled.
| This field shows next four mode numbers of the sequence in dynamic mode switching.
| **Operations**:

===== ========================================
Write 0x0082
Write 0xYYYY
      m7 [12:15], m6 [11:8], m5 [7:4] m4 [3:0]
===== ========================================

| **Name**: Set Dynamic Sequence Repeat Count0
| **Type**: Write
| **Description**: This command is valid only for ADSD3030 and when dynamic mode switch is enabled
| This fields indicate the number of times the specified mode should repeat before going to the next mode in sequence0 mode selection. (i.e., repeat counts- rc).
| **Operations**:

+-------+------------------------------------------------------------------------------------+
| Write | 0x0083                                                                             |
+-------+------------------------------------------------------------------------------------+
| Write | This command is valid only for ADSD3030 and when dynamic mode switching is enabled |
|       | 0xYYYY                                                                             |
|       | m3_rc [12:15], m2 \_rc[11:8], m1_rc [7:4] m0_rc [3:0]                              |
+-------+------------------------------------------------------------------------------------+

| **Name**: Set Dynamic Sequence Repeat Count1
| **Type**: Write
| **Description**: This command is valid only for ADSD3030 and when dynamic mode switch is enabled
| This fields indicate the number of times the specified mode should repeat before going to the next mode in sequence1 mode selection. (i.e., repeat counts).
| Note: In ADTF3175, the repeat count (using the Set Dynamic Sequence Repeat Count0 and Set Dynamic Sequence Repeat Count1) commands are not used. Even if the user programs these commands, the ADSD3500 firmware ignores them, and the dynamic sequence pattern will be given using ADI_SET_DYNAMIC_SEQUENCE_COMPOSITION0 and ADI_SET_DYNAMIC_SEQUENCE_COMPOSITION1. Maximum sequence Length supported is 8.
| **Operations**:

+-------+---------------------------------------------------------------------------------+
| Write | 0x0084                                                                          |
+-------+---------------------------------------------------------------------------------+
| Write | This command is valid only for ADSD3030 and when dynamic mode switch is enabled |
|       | 0xYYYY                                                                          |
|       | m7_rc [12:15], m6_rc [11:8], m5_rc [7:4] m4_rc [3:0]                            |
|       | Example: For dynamic mode switching(For Tembin)                                 |
|       | W 00 80 00 01                                                                   |
|       | W 00 81 32 56                                                                   |
|       | W 00 82 FF F2                                                                   |
|       | W 00 83 43 21                                                                   |
|       | W 00 84 FF F5                                                                   |
|       | The expected sequence is                                                        |
|       | 655222333322222 655222                                                          |
+-------+---------------------------------------------------------------------------------+

| **Name**: Get dynamic mode switching enable\\disable status
| **Type**: Read
| **Description**: Reads dynamic mode switching status
| **Operations**:

===== ===============================================
Write 0x0085
Read  \* 0x0000 - Dynamic mode switching is Disabled.
      \* 0x00001 - Dynamic mode switching is Enabled.
===== ===============================================

| **Name**: Get Invalid Phase Value
| **Type**: Read
| **Description**: Read the Phase Invalid value.
| **Operations**:

===== =====================================================
Write 0x0091
Read  Reads the value assigned for the Invalid Phase Value.
===== =====================================================

| **Name**: Set Invalid Phase Value
| **Type**: Write
| **Description**: Sets the Phase Invalid value.
| The pixels are invalidated based on this value.
| **Operations**:

===== ===================================================
Write 0x0090
Write Writes a value 0x0YYY to the Invalid Phase Value.
      Where the maximum value of 0x0YYY is 0x0FFF (4095).
===== ===================================================

| **Name**: Enable/Disable Raw Data Bypass Mode
| **Type**: Write
| **Description**: Option to enable or disable Raw Data Bypass Mode.
| **Operations**:

===== =========================================
Write 0x0033
Write \* 0x0000 - Disable Raw Data Bypass Mode.
      \* 0x0001 - Enable Raw Data Bypass Mode.
===== =========================================

| **Name**: Get Raw Data Bypass Enable/Disable Status
| **Type**: Read
| **Description**: It reads the Raw Data Bypass Enable/Disable Status
| **Operations**:

===== =============================================
Write 0x00B4
Read  \* 0x0000 - Raw Data Bypass Mode is Disabled.
      \* 0x0001 - Raw Data Bypass Mode is Enabled.
===== =============================================

| **Name**: Enable/Disable Only AB Mode
| **Type**: Write
| **Description**: Option to enable or disable Only AB Mode.
| **Operations**:

===== =================================
Write 0x006E
Write \* 0x0000 - Disable Only AB Mode.
      \* 0x0001 - Enable Only AB Mode.
===== =================================

| **Name**: Enable/Disable Output metadata Header in Raw Frame
| **Type**: Write
| **Description**: Option to Enable or Disable the output Metadata header in Raw Frame.
| **Operations**:

===== =================================================
Write 0x0077
Write \* 0x0000 - Disable metadata header in Raw Frame.
      \* 0x0001 - Enable metadata header in Raw Frame.
===== =================================================

| **Name**: Get Output metadata Header in Raw Frame status
| **Type**: Read
| **Description**: Reads the status of enable/disable metadata header in Raw Frame.
| **Operations**:

===== =====================================================
Write 0x0078
Read  \* 0x0000 - metadata header in Raw Frame is Disabled.
      \* 0x0001 - metadata header in Raw Frame is Enabled.
===== =====================================================

| **Name**: Get Firmware Boot Section
| **Type**: Read
| **Description**: Gives the section where ADSD3500 is booted from.
| **Operations**:

+-------+-----------------------------------------------------------------------------+
| Write | 0x0092                                                                      |
+-------+-----------------------------------------------------------------------------+
| Read  | \* 0x0001 - ADSD3500 booted from Current Section.                           |
|       | \* 0x0002/3 - ADSD3500 booted from Upgrade Section                          |
|       | \* 0x0004 - ADSD3500 booted from Factory Firmware (Recovery)                |
|       | \* 0x0005 - ADSD3500 booted from Factory Firmware (Forced via Host Command) |
+-------+-----------------------------------------------------------------------------+

| **Name**: Get Ping/Pong Section Status
| **Type**: Read
| **Description**: Gives the section where ADSD3500 is booted from.
| **Operations**:

===== ==============================================
Write 0x0094
Read  \* 0x0000 - ADSD3500 booted from Ping Section.
      \* 0x0001 - ADSD3500 booted from Pong Section
===== ==============================================

| **Name**: Force ADS3500 to boot from Factory/Current Section
| **Type**: Write
| **Description**: Option to Force ADS3500 to boot from Factory/Current Section.
| **Operations**:

===== =======================================================
Write 0x0093
Write \* 0x0000 - Force ADS3500 to boot from Current Section.
      \* 0x0001 - Force ADS3500 to boot from Factory Section.
===== =======================================================

| **Name**: Add Flash status chunk
| **Type**: Write
| **Description**: Option to add Flash status chunk at the end of Flash to support init version - 2.0.
| **Operations**:

===== =========
Write 0x0095
Write \* 0x0000
===== =========

| **Name**: Get Init Firmware Version
| **Type**: Read
| **Description**: Gives the init firmware version.
| **Operations**:

===== =============================
Write 0x0096
Read  \* 0x0001 - Init Version 1.0.
      \* 0x0002 - Init Version 2.0.
===== =============================

| **Name**: Enable/Disable All Frequency AB Frame
| **Type**: Write
| **Description**: Option to enable or disable all frequency AB frame along with phase frame.
| (2/3 phase frame + 2/3 AB frame).
| **Operations**:

===== ===========================================
Write 0x0098
Write \* 0x0000 - Disable All Frequency AB Frame.
      \* 0x0001 - Enable All Frequency AB Frame.
===== ===========================================

| **Name**: Get All Frequency AB Frame Status
| **Type**: Read
| **Description**: Read the All Frequency AB Frame enable/disable status.
| **Operations**:

===== ============================================
Write 0x0099
Read  \* 0x0000 - All Frequency AB Frame disabled.
      \* 0x0001 - All Frequency AB Frame enabled.
===== ============================================

| **Name**: Enable/Disable Filtered AB
| **Type**: Write
| **Description**: Option to selected filtered or unfiltered AB frame.
| **Operations**:

===== ==========================
Write 0x009C
Write \* 0x0000 - Unfiltered AB.
      \* 0x0001 - Filtered AB.
===== ==========================

| **Name**: Get Enable/Disable Filtered AB Status
| **Type**: Read
| **Description**: Read the status of filtered/unfiltered AB.
| **Operations**:

===== =================================================
Write 0x009D
Read  \* 0x0000 - Unfiltered AB will be sent as output.
      \* 0x0001 - Filtered AB will be sent as output.
===== =================================================

| **Name**: Set ABA Weights for Active Brightness Computation.
| **Type**: Write
| **Description**: Set ABA Weights for Active Brightness Computation.
| **Operations**:

===== ========================================
Write 0x00A1 - Set ABA_WEIGHT_1
      0x00A2 - Set ABA_WEIGHT_2
      0x00A3 - Set ABA_WEIGHT_3
Write 0xXXXX - Set value between 0x000 - 0x3FF
===== ========================================

| **Name**: Get ABA Weights for Active Brightness Computation.
| **Type**: Read
| **Description**: Get ABA Weights for Active Brightness Computation.
| **Operations**:

===== ==============================================
Write 0x00A5 - Get ABA_WEIGHT_1
      0x00A6 - Get ABA_WEIGHT_2
      0x00A7 - Get ABA_WEIGHT_3
Read  0xXXXX - Returns the Set Value for ABA_WEIGHTS
===== ==============================================

| **Name**: Set ABA Scale Factor for Active Brightness Computation.
| **Type**: Write
| **Description**: Set ABA Scale Factor for Active Brightness Computation.
| **Operations**:

+-------+---------------------------------------------------------------------------+
| Write | 0x00A4                                                                    |
+-------+---------------------------------------------------------------------------+
| Write | 0x0000 - Extract the MSB Bits from the Calculated AB Data - MSB Selection |
|       | 0x0001 - Extract the LSB Bits from the Calculated AB Data - LSB Selection |
+-------+---------------------------------------------------------------------------+

| **Name**: Get ABA Scale Factor for Active Brightness Computation.
| **Type**: Read
| **Description**: Get ABA Scale Factor for Active Brightness Computation.
| **Operations**:

===== ==================================
Write 0x00A8
Read  0x0000 - Output AB is MSB Selected
      0x0001 - Output AB is LSB Selected
===== ==================================

| **Name**: Get Micro Sequencer Firmware version - LSB Bits
| **Type**: Read
| **Description**: Get Micro Sequencer Firmware version - LSB Bits
| **Operations**:

===== =======================================
Write 0x00B1
Read  0xXXXX - Returns the Version's LSB Bits
===== =======================================

| **Name**: Get Micro Sequencer Firmware version - MSB Bits
| **Type**: Read
| **Description**: Get Micro Sequencer Firmware version - MSB Bits
| **Operations**:

===== =======================================
Write 0x00B2
Read  0xXXXX - Returns the Version's MSB Bits
===== =======================================

| **Name**: Configure GPIO with feature
| **Type**: Write
| **Description**: Host command specific to the GPIO number has been added so that user can select the features which they would need.
| List of Features:
| SET_SOF_PROGRAMMABLE_DELAY = 1
| 1PPS_TIMER = 2
| SECOND_INTERRUPT_SENSOR = 3
| List of GPIO Pins:
| I2C: 8, 10, 11, 14, 15, 18, 16, 17, 20, 21
| SPI: 8, 10, 11, 14, 15, 18, 12, 19
| Example: Command to Configure GPIO8 with SET_SOF_PROGRAMMABLE_DELAY Feature.
| Write: W 00 B5
| Data : 0xXX YY
| where ‘YY’ represents feature and ‘XX’ represents Enable /Disable.
| YY is 01 for SOF PROGRAMMABLE DELAY Feature, XX is 01 for Enabling the feature.
| W 00 B5 01 01 : ENABLE
| W 00 B5 00 01 : DISABLE
| **Operations**:

========= ====== ======
GPIO Port Write  Data
GPIO8     0x00B5 0xXXYY
GPIO10    0x00B6 0xXXYY
GPIO11    0x00B7 0xXXYY
GPIO12    0x00B8 0xXXYY
GPIO14    0x00B9 0xXXYY
GPIO15    0x00BA 0xXXYY
GPIO16    0x00BB 0xXXYY
GPIO17    0x00BC 0xXXYY
GPIO18    0x00BD 0xXXYY
GPIO20    0x00BE 0xXXYY
GPIO21    0x00BF 0xXXYY
========= ====== ======

| **Name**: Get Status of GPIO configured with feature
| **Type**: Read
| **Description**: Reads respective GPIO feature, along with Enable/Disable Status.
| Where Data represents: 0xXXYY: where ‘YY’ represents feature and ‘XX’ represents Enable/Disable
| List of Features:
| SET_SOF_PROGRAMMABLE_DELAY = 1
| 1PPS_TIMER = 2
| SECOND_INTERRUPT_SENSOR = 3
| List of GPIO Pins:
| I2C: 8, 10, 11, 14, 15, 18, 16, 17, 20, 21
| SPI: 8, 10, 11, 14, 15, 18, 12, 19
| Example: Command to read GPIO8 feature along with enable/disable status: R 00 F5
| Value Returned: 01 01 -> SET_SOF_PROGRAMMABLE_DELAY - Enabled
| Value Returned: 00 01 -> SET_SOF_PROGRAMMABLE_DELAY - Disabled
| **Operations**:

========= ======
GPIO Port Read
GPIO8     0x00F5
GPIO10    0x00F6
GPIO11    0x00F7
GPIO12    0x00F8
GPIO14    0x00F9
GPIO15    0x00FA
GPIO16    0x00FB
GPIO17    0x00FC
GPIO18    0x00FD
GPIO20    0x00FE
GPIO21    0x00FF
========= ======

| **Name**: Set MIPI Continuous HS Clock Register.
| **Type**: Write
| **Description**: Sets the MIPI Continuous HS Clock Register.
| **Operations**:

===== =============================================
Write 0x00A9
Write \* 0x0000 - Disable MIPI Continuous HS Clock.
      \* 0x0001 - Enable MIPI Continuous HS Clock.
===== =============================================

| **Name**: Get MIPI Continuous HS Clock Register.
| **Type**: Read
| **Description**: Reads MIPI Continuous HS Clock Register.
| **Operations**:

===== =================================================
Write 0x00AA
Read  \* 0x0000 - MIPI Continuous HS Clock is Disabled.
      \* 0x0001 - MIPI Continuous HS Clock is Enabled.
===== =================================================

| **Name**: Set Enable Deskew at Stream On.
| **Type**: Write
| **Description**: Set Enable Deskew at Stream On.
| **Operations**:

===== ===========================
Write 0x00AB
Write \* 0x0000 - Disable Deskew.
      \* 0x0001 - Enable Deskew.
===== ===========================

| **Name**: Get Status of Deskew at Stream On.
| **Type**: Read
| **Description**: Reads the Status of Deskew at Stream On.
| **Operations**:

===== ===============================
Write 0x00AC
Read  \* 0x0000 - Disabled - Default.
      \* 0x0001 - Enabled.
===== ===============================

| **Name**: Set GPIO High to Low after SOF with Programmable delay
| **Type**: Write
| **Description**: Set the delay after which the GPIOx [Configured for programmable delay] will go low starting at high from SOF.
| **Operations**:

===== ===============================
Write 0x009A
Write 0 to 0xFFFF - the 16-bit value.
===== ===============================

| **Name**: Set GPIO High to Low after SOF with Programmable delay
| **Type**: Read
| **Description**: Read the delay of GPIOx [Configured for programmable delay] high to low.
| **Operations**:

===== ======================================
Write 0x009B
Read  Returned value is between 0 to 0xFFFF.
===== ======================================

| **Name**: Read the last two ADSD3500 System States
| **Type**: Read
| **Description**: ADSD3500 stores the last two System states. User can read the same via the host command.
| **Operations**:

+-------+---------------------------------------------------------------------------------------------------+
| Write | 0x00C0                                                                                            |
+-------+---------------------------------------------------------------------------------------------------+
| Read  | 0xXXYY - It returns 0xXXYY: XX represents recent Error State, YY represents previous Error State. |
+-------+---------------------------------------------------------------------------------------------------+

| **Name**: Clear the Interrupt and System Status
| **Type**: Write
| **Description**: It will clear the ADSD3500 current system status and interrupt [Host Interrupt] if raised.
| Note: It will not clear the last two System States.
| **Operations**:

===== ======
Write 0x00C1
Write 0x0000
===== ======

| **Name**: Set PCIR (Phase Coding Interference Reduction) Seed Value
| **Type**: Write
| **Description**: Sets the PCIR Seed value of the imager.
| **Operations**:

===== =============================================
Write 0x00C3
Write 0xXXXX - Any random seed value to be written.
===== =============================================

| **Name**: Get PCIR (Phase Coding Interference Reduction) Seed Value
| **Type**: Read
| **Description**: Reads PCIR Seed Value of the Imager.
| **Operations**:

===== =====================================
Write 0x00C4
Read  0xXXXX - Returns the PCIR seed value.
===== =====================================

| **Name**: Get Second ADSD3500 Interrupt Reason
| **Type**: Read
| **Description**: Reads Second ADSD3500 Interrupt Reason.
| **Operations**:

===== =======================================================
Write 0x0056
Read  Returns the reason for the Second ADSD3500 Interrupt.
      0x0001 - Imager Error
      0x0002 - Stream off Interrupt from the second ADSD3500.
===== =======================================================

| **Name**: Get Second ADSD3500 System Status
| **Type**: Read
| **Description**: Reads Second ADSD3500 System Status.
| **Operations**:

===== ===========================================================
Write 0x0057
Read  0xXXXX - Returns the System Status for the Second ADSD3500.
      Same as Get System Status Command 0x0020.
===== ===========================================================

| **Name**: Get Imager Micro Sequencer Status
| **Type**: Read
| **Description**: Reads the Imager Micro Sequencer Status.
| **Operations**:

===== ============================================
Write 0x0058
Read  0xXXXX - Returns the Imager Micro Sequencer.
===== ============================================

| **Name**: Get Is Dual ADSD3500 Enabled
| **Type**: Read
| **Description**: Reads the Dual ADSD3500 Enabled Status.
| **Operations**:

===== ===============================
Write 0x005A
Read  0x0000 - Dual ADSD3500 Disabled
      0x0001 - Dual ADSD3500 Enabled
===== ===============================

--------------

BURST MODE COMMANDS
~~~~~~~~~~~~~~~~~~~

.. important::

   The ADSD3500 data format is little-endian. However, when the stock ADSD3500 Linux device driver is used, **the payload size must be in big-endian** and **the checksum, the address and custom data are in little-endian**.


Get Camera Intrinsics
^^^^^^^^^^^^^^^^^^^^^

This is burst mode command to get the camera intrinsic structures from the ADSD3500 for a given Mode (Supported Modes are 0 to 10). This is the calibration data required for R-depth to Point Cloud conversion.

+--------+-----------+--------+---------+---------------------------------------------+-------------+
| ID     | Size      | Cmd    | Address | Header Checksum                             | Custom Data |
| 1 Byte | 2 Bytes   | 1 Byte | 4 Bytes | 4 Bytes                                     | 4 Bytes     |
+========+===========+========+=========+=============================================+=============+
| 0xAD   | 0x00 0x38 | 0x01   | 0x0000  | Header Checksum (size, CMD, address) - 0x39 | Mode        |
+--------+-----------+--------+---------+---------------------------------------------+-------------+

**Operations**:

===== ===============================
Write 0x006D
Write \* 0x0000 - Free-Wheeling mode.
      \* 0x0001 - 1PPS Mode.
===== ===============================

Upon reception of this command, Firmware sends 56 Bytes CAMERA INSTRINSIC structure as follow:

::

   typedef struct { 
     float fx; 
     float fy; 
     float cx; 
     float cy; 
     float codx; 
     float cody; 
     float k1; 
     float k2; 
     float k3; 
     float k4; 
     float k5; 
     float k6; 
     float p2; 
     float p1; 
   } CameraIntrinsics; 

Get Dealias Parameters
^^^^^^^^^^^^^^^^^^^^^^

This is BURST mode command to get the dealias parameters for a given mode (Supported Modes are 0 to 10). For getting the calibration data required for partial depth to full depth conversion

+--------+-----------+--------+---------+---------------------------------------------+-------------+
| ID     | Size      | Cmd    | Address | Header Checksum                             | Custom Data |
| 1 Byte | 2 Bytes   | 1 Byte | 4 Bytes | 4 Bytes                                     | 4 Bytes     |
+========+===========+========+=========+=============================================+=============+
| 0xAD   | 0x00 0x20 | 0x02   | 0x0000  | Header Checksum (size, CMD, address) - 0x22 | Mode        |
+--------+-----------+--------+---------+---------------------------------------------+-------------+

Upon reception of this command, Firmware send 32-byte dealias parameter structure as follow:

::

   typedef struct { 
     int n_rows; 
     int n_cols; 
     uint8_t n_freqs; 
     uint8_t row_bin_factor; 
     uint8_t col_bin_factor; 
     uint16_t n_offset_rows; 
     uint16_t n_offset_cols; 
     uint16_t n_sensor_rows; 
     uint16_t n_sensor_cols; 
     uint8_t FreqIndex[3]; 
     uint16_t Freq[3]; 
   } DealiasDataStructure; 

Firmware Upgrade Command
^^^^^^^^^^^^^^^^^^^^^^^^

This is burst mode command to upgrade the ADSD3500 Current firmware stored in Flash memory.

+--------+---------------------------------+--------+-------------------------------+--------------------------------------+----------------------------+
| ID     | Size                            | Cmd    | Address                       | Header Checksum                      | Custom Data                |
| 1 Byte | 2 Bytes                         | 1 Byte | 4 Bytes                       | 4 Bytes                              | 4 Bytes                    |
+========+=================================+========+===============================+======================================+============================+
| 0xAD   | Chunk Size (Size of Flash Page) | 0x04   | Total size of Firmware Binary | Header Checksum (size, CMD, address) | CRC of the Firmware Binary |
+--------+---------------------------------+--------+-------------------------------+--------------------------------------+----------------------------+

Host first send this 16 byte header to ADSD3500. ADSD3500 will receive header and derives, One Chunk Size, total number of chunks (Total size / one chunk size), Expected CRC of the complete firmware.

If firmware size is 16 KB and Flash page size is 512 Byte, then SIZE = 512 and Total size = 16384 (16 KB). ADSD3500 firmware shall expect 32 (16 KB/512) data chunk each of size 512 Byte.

If the firmware size is not multiple of Page size, then Host shall pad the remaining byte with 0x00 to make it multiple of Page size. i.e. Firmware size = 16000 Byte. Size is 384 bytes short to 16 KB (16384), so Host shall send Total size = 16 KB and pad the last 384 bytes of last chuck with 0x00.

Second Firmware Upgrade Command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is burst mode command to upgrade the second ADSD3500 firmware stored in Flash memory.

+--------+---------------------------------+--------+-------------------------------+--------------------------------------+----------------------------+
| ID     | Size                            | Cmd    | Address                       | Header Checksum                      | Custom Data                |
| 1 Byte | 2 Bytes                         | 1 Byte | 4 Bytes                       | 4 Bytes                              | 4 Bytes                    |
+========+=================================+========+===============================+======================================+============================+
| 0xAD   | Chunk Size (Size of Flash Page) | 0x2A   | Total size of Firmware Binary | Header Checksum (size, CMD, address) | CRC of the Firmware Binary |
+--------+---------------------------------+--------+-------------------------------+--------------------------------------+----------------------------+

Host first send this 16 byte header to ADSD3500. ADSD3500 will receive header and derives, One Chunk Size, total number of chunks (Total size / one chunk size), Expected CRC of the complete firmware.

Get ADSD3500 Firmware Version and GitHash
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is burst mode command to retrieve the ADSD3500 Firmware version and GIT HASH of the commit used to generate the Firmware binary. GIT HASH is computed using SHA-1 algorithm so it is 160 bits log (20 BYTES (40 hex characters, 40 bytes ASCII values) ). First 4 bytes of the Firmware binary are reserved for Firmware version. GIT HASH shall be appended at the END of the Firmware Binary while storing to Flash.

+--------+-----------+--------+---------+---------------------------------------------+----------------------------------------------------------+
| ID     | Size      | Cmd    | Address | Header Checksum                             | Custom Data                                              |
| 1 Byte | 2 Bytes   | 1 Byte | 4 Bytes | 4 Bytes                                     | 4 Bytes                                                  |
+========+===========+========+=========+=============================================+==========================================================+
| 0xAD   | 0x00 0x2C | 0x05   | 0x0000  | Header Checksum (size, CMD, address) - 0x31 | \* 0x01 - To get the version of Current Firmware         |
|        |           |        |         |                                             | \* 0x02 - To get the version of Upgrade Firmware         |
|        |           |        |         |                                             | \* 0x03 - To get the version of Factory Firmware         |
|        |           |        |         |                                             | \* 0x04 - To get the version of Second ADSD3500 Firmware |
+--------+-----------+--------+---------+---------------------------------------------+----------------------------------------------------------+

Upon reception of this command, upon reception of this command, Firmware retrieves the version and GIT Hash from the Firmware stored in Flash for a given Section (Current, Upgrade, Factory, Second ADSD3500 firmware if it is a Dual Setup) and sends 44 bytes (4 Byte version followed by 40 bytes Hash) to Host.

Switch to Standard Mode
^^^^^^^^^^^^^^^^^^^^^^^

This command switches the protocol mode of the ADSD3500 Firmware from BURST MODE to STANDARD MODE. After this command, ADSD3500 supports only STANDARD MODE commands. 

+--------+---------+--------+---------+---------------------------------------------+-------------+
| ID     | Size    | Cmd    | Address | Header Checksum                             | Custom Data |
| 1 Byte | 2 Bytes | 1 Byte | 4 Bytes | 4 Bytes                                     | 4 Bytes     |
+========+=========+========+=========+=============================================+=============+
| 0xAD   | 0x00    | 0x10   | 0000    | Header Checksum (size, CMD, address) - 0x10 | 0x00        |
+--------+---------+--------+---------+---------------------------------------------+-------------+

Get ADSD3500 System Status
^^^^^^^^^^^^^^^^^^^^^^^^^^

+--------+-----------+--------+---------+---------------------------------------------+---------------------+
| ID     | Size      | Cmd    | Address | Header Checksum                             | Custom Data         |
| 1 Byte | 2 Bytes   | 1 Byte | 4 Bytes | 4 Bytes                                     | 4 Bytes             |
+========+===========+========+=========+=============================================+=====================+
| 0xAD   | 0x00 0x10 | 0x18   | 0x0000  | Header Checksum (size, CMD, address) - 0x28 | 0x00 0x00 0x00 0x00 |
+--------+-----------+--------+---------+---------------------------------------------+---------------------+

Get CCB Serial Number
^^^^^^^^^^^^^^^^^^^^^

+--------+-----------+--------+---------+---------------------------------------------+---------------------+
| ID     | Size      | Cmd    | Address | Header Checksum                             | Custom Data         |
| 1 Byte | 2 Bytes   | 1 Byte | 4 Bytes | 4 Bytes                                     | 4 Bytes             |
+========+===========+========+=========+=============================================+=====================+
| 0xAD   | 0x00 0x20 | 0x19   | 0x0000  | Header Checksum (size, CMD, address) - 0x39 | 0x00 0x00 0x00 0x00 |
+--------+-----------+--------+---------+---------------------------------------------+---------------------+

1PPS Commands: Setting the Initial Time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Setting 32bit seconds value in initial time
"""""""""""""""""""""""""""""""""""""""""""

+--------+-----------+--------+----------------------+--------------------------------------+---------------------+
| ID     | Size      | Cmd    | Address              | Header Checksum                      | Custom Data         |
| 1 Byte | 2 Bytes   | 1 Byte | 4 Bytes              | 4 Bytes                              | 4 Bytes             |
+========+===========+========+======================+======================================+=====================+
| 0xAD   | 0x00 0x04 | 0x14   | 32-bit seconds value | Header Checksum (size, CMD, address) | 0x00 0x00 0x00 0x00 |
+--------+-----------+--------+----------------------+--------------------------------------+---------------------+

.. important::

   32-bit seconds value should be sent in little endian format.


Setting 32bit fractional seconds value in initial time
""""""""""""""""""""""""""""""""""""""""""""""""""""""

+--------+-----------+--------+-------------------------+--------------------------------------+---------------------+
| ID     | Size      | Cmd    | Address                 | Header Checksum                      | Custom Data         |
| 1 Byte | 2 Bytes   | 1 Byte | 4 Bytes                 | 4 Bytes                              | 4 Bytes             |
+========+===========+========+=========================+======================================+=====================+
| 0xAD   | 0x00 0x04 | 0x15   | 32-bit fractional value | Header Checksum (size, CMD, address) | 0x00 0x00 0x00 0x00 |
+--------+-----------+--------+-------------------------+--------------------------------------+---------------------+

Note: The fractional value to be set should be in Fixed Format. Since fractional values are in floating format, it must be converted to a 32-bit fixed format by multiplying the value with 2^32. E.g.: If the initial fractional value is to be set to 0.5s. Then the value in commands is 0.5 \* (2^32), i.e., 2147483648u. In hex format, it would be 0x8000000 (0x00 0x00 0x00 0x80 in Address block)

.. important::

   32-bit fractional value should be sent in little endian format.


CCB As Master
^^^^^^^^^^^^^

Read Mode Map Table from ADSD3500
"""""""""""""""""""""""""""""""""

This is burst mode command to get the mode map table from the ADSD3500.

+--------+-----------+--------+---------+---------------------------------------------+-------------+
| ID     | Size      | Cmd    | Address | Header Checksum                             | Custom Data |
| 1 Byte | 2 Bytes   | 1 Byte | 4 Bytes | 4 Bytes                                     | 4 Bytes     |
+========+===========+========+=========+=============================================+=============+
| 0xAD   | 0x00 0xA8 | 0x24   | 0x0000  | Header Checksum (size, CMD, address) - 0xCC | 00 00 00 00 |
+--------+-----------+--------+---------+---------------------------------------------+-------------+

Upon reception of this command, Firmware sends 168 Bytes Mode Map structure as follow:

**Note:** For each default mode the, modemap table holds 24 bytes of data. ADSD3500 can stores 6 such modes. Hence total size of modemap table is 24\*6 = 144 bytes(0x90)+24 empty bits(reserved).

::

   struct MODEMAP_TABLE_ENTRY {
    uint8_t UserDefinedMode;
    uint8_t CFGMode;
    uint16_t Height;
    uint16_t Width;
    uint8_t nFreq;
    uint8_t P0Mode;
    uint8_t TempMode;
    uint8_t INIIndex;
    uint8_t default_mode;
    uint8_t PassiveModeFlag;
    uint8_t nPhases;
    uint8_t nCaptures;
    uint16_t SensorRowsPerMipiPacket;
    uint16_t spare5;
    uint16_t spare6;
    uint16_t spare7;
    uint16_t spare8;
   };

Read IniTable from ADSD3500 for particular mode
"""""""""""""""""""""""""""""""""""""""""""""""

This is burst mode command to get the INI table for default modes from the ADSD3500.

+--------+-----------+--------+---------+---------------------------------------------+-------------+
| ID     | Size      | Cmd    | Address | Header Checksum                             | Custom Data |
| 1 Byte | 2 Bytes   | 1 Byte | 4 Bytes | 4 Bytes                                     | 4 Bytes     |
+========+===========+========+=========+=============================================+=============+
| 0xAD   | 0x00 0x28 | 0x25   | 0x0000  | Header Checksum (size, CMD, address) - 0x4D | Mode        |
+--------+-----------+--------+---------+---------------------------------------------+-------------+

\*\* Example \*\*

To get INI table for mode 1, Command to be used is:

\*\* R AD 00 28 25 00 00 00 00 4D 00 00 00 01 00 00 00 \*\*

Upon reception of this command, Firmware sends 40 Bytes Mode Map structure as follow:

::


    uint8_t INIIndex;
     uint8_t rsvd;                              // for byte alignment of following fields 
     uint16_t abThreshMin;
     uint16_t confThresh;
     uint16_t radialThreshMin;
     uint16_t radialThreshMax;
     uint16_t jblfApplyFlag;
     uint16_t jblfWindowSize;
     uint16_t jblfGaussianSigma;
     uint16_t jblfExponentialTerm;
     uint16_t jblfMaxEdge;
     uint16_t jblfABThreshold;
     uint16_t spare0;
     uint16_t spare1;
     uint16_t spare2;
     uint16_t spare3;
     uint16_t spare4;
     uint16_t spare5;
     uint16_t spare6;
     uint16_t spare7;
     uint16_t spare8;
   };

| **Name**: Read Calibration File Version
| **Type**: Standard Read
| **Description**: Get calibration mode from ADSD3500.
| **Operations**:

===== ===========================================================
Write 0x0032
Read  0x0203 - ADSD3500 configured to support CCB as master. \\\\
===== ===========================================================

| **Name**: Reset INI Parameters
| **Type**: Write
| **Description**: Reset INI table for all modes to default values.
| **Operations**:

===== ======
Write 0x0040
Write 0x0000
===== ======

Burst Mode Response
"""""""""""""""""""

The response from the ADSD3500 will be: (To read the status of ADSD3500 in burst mode)

+--------+---------+--------+---------+--------------------------------------+------------------------+
| ID     | Size    | Cmd    | Address | Header Checksum                      | Custom Data            |
| 1 Byte | 2 Bytes | 1 Byte | 4 Bytes | 4 Bytes                              | 4 Bytes                |
+========+=========+========+=========+======================================+========================+
| 0xAD   | 0x00    | 0x18   | 0x0000  | Header Checksum (size, CMD, address) | ADSD3500 System Status |
+--------+---------+--------+---------+--------------------------------------+------------------------+

Example Flow
------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adsd3500-host-commands-example-flow.png
   :alt: adsd3500-host-commands-example-flow.png
   :align: center
   :width: 400px

Examples that work on the ADTF3175D Eval Kit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See the ctrl_app source code in GitHub: :git-ToF:`tools/debug_apps/ctrl_app/ctrl_app.cpp`

See the NVM Tools in GitHub: :git-ToF:`tools/nvm_tools`

:git-ToF:`Connect to Camera via V4L2 <tools/nvm_tools/fw_upgrade/fw_upgrade.cpp#L75>`

:git-ToF:`Hard Reset the ADSD3500 <tools/nvm_tools/fw_upgrade/fw_upgrade.cpp#L88>`

:git-ToF:`Switch to Burst Mode <tools/nvm_tools/fw_upgrade/fw_upgrade.cpp#L90>`

:git-ToF:`Get ADSD3500 Firmware Version and GitHash <tools/nvm_tools/fw_upgrade/fw_upgrade.cpp#L92>`

:git-ToF:`Firmware Upgrade Command <tools/nvm_tools/fw_upgrade/fw_upgrade.cpp#L94>` -> :git-ToF:`Write Firmware Data Packets <tools/nvm_tools/fw_upgrade/fw_upgrade.cpp#L101>`

Sample Code: C
~~~~~~~~~~~~~~

The following code shows how to access ADSD3500 host commands via the ToF Linux device driver. The program executes from the command line on a Linux embedded host.

This file ingests infile.txt. infile.txt contains the commands.

Example 1:

-  Issue the 'Get Chip ID' command

::

   analog@aditof:~$ mode infile.txt
   R 01 12
   analog@aditof:~$ ./burst_ctrl
   59 31

Example 2:

-  Issue the 'Get Confidence Threshold' command
-  Issue the 'Get Chip ID' command
-  Issue the 'Set Confidence Threshold' command
-  Issue the 'Get Chip ID' command
-  Issue the 'Get Confidence Threshold' command

::

   analog@aditof:~$ more infile.txt
   R 00 16
   R 01 12
   W 00 11 00 34
   R 01 12
   R 00 16
   analog@aditof:~$ ./burst_ctrl
   00 19
   59 31
   59 31
   00 34

.. code:: c

   #include <string>
   #include <iostream>
   #include <sstream>
   #include <fstream>

   #include <fcntl.h>
   #include <errno.h>
   #include <unistd.h>
   #include <stdint.h>
   #include <malloc.h>
   #include <cstring>
   #include <stdbool.h>
   #include <sys/mman.h>
   #include <sys/ioctl.h>
   #include <linux/videodev2.h>

   #define IOCTL_TRIES 3
   #define CLEAR(x) memset (&(x), 0, sizeof (x))
   #define CTRL_SIZE 4099
   #define VER_MAJ 1
   #define VER_MIN 0
   #define VER_PATCH 1

   static int xioctl(int fd, int request, void *arg)
   {
           int r;
           int tries = IOCTL_TRIES;
           do {
               r = ioctl(fd, request, arg);
           } while (--tries > 0 && r == -1 && EINTR == errno);

           return r;
   }

   bool v4l2_ctrl_set(int fd, uint32_t id, uint8_t *val)
   {
       static struct v4l2_ext_control extCtrl;
       static struct v4l2_ext_controls extCtrls;

       extCtrl.size = CTRL_SIZE * sizeof(char);
       extCtrl.p_u8 = val;
       extCtrl.id = id;
       memset(&extCtrls, 0, sizeof(struct v4l2_ext_controls));
       extCtrls.controls = &extCtrl;
       extCtrls.count = 1;
       if (xioctl(fd, VIDIOC_S_EXT_CTRLS, &extCtrls) == -1) {
           std::cout << "Failed to set ctrl with id " << id;
           return false;
       }

       return true;
   }

   bool v4l2_ctrl_get(int fd, uint32_t id, uint8_t *val)
   {
       static struct v4l2_ext_control extCtrl;
       static struct v4l2_ext_controls extCtrls;

       extCtrl.size = CTRL_SIZE * sizeof(char);
       extCtrl.p_u8 = val;
       extCtrl.id = id;
       memset(&extCtrls, 0, sizeof(struct v4l2_ext_controls));
       extCtrls.controls = &extCtrl;
       extCtrls.count = 1;
       if (xioctl(fd, VIDIOC_G_EXT_CTRLS, &extCtrls) == -1) {
           std::cout << "Failed to get ctrl with id " << id;
           return false;
       }

       return true;
   }


   int main() {
       uint8_t data[CTRL_SIZE] = {0};

       int fd = open("/dev/v4l-subdev1", O_RDWR | O_NONBLOCK);
       if (fd == -1) {
           std::cout << "Failed to open the camera" << std::endl;
           return -1;
       }
       
       std::ifstream infile("infile.txt");
       std::string line;

       if (!infile.is_open()) {
           std::cout << "File infile.txt not found\n";
           return -1;
       }
       
       printf("Burst Control app version: %d.%d.%d\n", VER_MAJ, VER_MIN, VER_PATCH);

       while (std::getline(infile, line))
       {
           std::stringstream lineStream(line);
           std::string token;
           std::string r_w;
           int i = 0;
           lineStream >> r_w;
           while(lineStream >> token) {
               try {
                   data[i+3] = stoi(token, 0, 16);
               }
               catch(std::invalid_argument& e){
               }
               i++;
               if (i > 4096) {
                   std::cout << "Command line has to many bytes\n";
                   return -1;
               }
           }
           //Delay functionality
           if (r_w == "D") {
               usleep(1000 * data[3]);
               continue;
           }

           data[0] = 1;
           data[1] = i >> 8;
           data[2] = i & 0xFF;

           v4l2_ctrl_set(fd, 0x009819e1, data);        
           if ((r_w == "R") && (i != 2) && (i != 4)) {
               data[0] = 0;
               data[1] = data[4];
               data[2] = data[5];
               v4l2_ctrl_set(fd, 0x009819e1, data);
               v4l2_ctrl_get(fd, 0x009819e1, data);

               int read_len = (data[1] << 8) | data[2];

               for (int j = 0; j < read_len; j++)
                   printf("%02X ", data[j + 3]);
               printf("\n");
           } else if (((r_w == "R") && (i == 2)) || ((r_w == "R") && (i == 4))) {
               data[0] = 0;
               data[1] = 0;
               data[2] = 2;
               usleep(1000 * 33);
               v4l2_ctrl_set(fd, 0x009819e1, data);
               v4l2_ctrl_get(fd, 0x009819e1, data);

               int read_len = 2;

               for (int j = 0; j < read_len; j++)
                   printf("%02X ", data[j + 3]);
               printf("\n");
           }
       }

       return 0;
   }

Sample Code: Python Code
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   from i2chw_d import * 
   import binascii 
   from binascii import hexlify 
   import os 
   import ctypes 
   import time  

   def hexstring(values): 
       """ 
       Convert a bytes like object to a hex string 
       :param values : bytes like object 
       :return: hex string representing the value 
       """ 
       return hexlify(bytearray(values)).decode("ascii") 

   def intstring(values): 
       """ 
       Convert a bytes like object to a hex string 
       :param values : bytes like object 
       :return: hex string representing the value 
       """ 
       return hexlify(bytearray(values)).decode("int") 

   if __name__ == "__main__": 
       global ft4222_handle
        
       I2C_FREQ = 0 
       n = len(sys.argv) 
       print("Total arguments passed:", n) 
       I2C_FREQ = sys.argv[1] 
       print(I2C_FREQ)  
       i2cInit(int(I2C_FREQ)) 
       count = 0 
       i2c_fifo_depth = 1 
       i2c_fifo_word_size = 1 

       ########################################################################################## 
       #Get chip id CMD : 0x0112 - This is READ command. ADSD3500 returns 2 BYTE chip ID (0x5931) 
       data_out_list_append = [] 
       for i in range(1, i2c_fifo_word_size * i2c_fifo_depth+1): 
           data_out_list_append.extend(int(0x0112).to_bytes(2,byteorder="big")) 

       data_out = bytes(data_out_list_append) 
       print('I2C data written') 
       print(hexlify(data_out)) 
       count = i2cWrite(0x38, data_out)     
       count, rx_data = i2cRead(0x38, 2) 
       print('I2C data read') 
       print(hexlify(rx_data)) 
       print("Number of data bytes read: %2d bytes\n" % (count)) 
       time.sleep(0.5) 

       ######################################################################################### 
       #Stream on : CMD : 0x00AD DATA : 0x00C5 
       data_out_list_append = [] 
       for i in range(1, i2c_fifo_word_size * i2c_fifo_depth+1): 
           data_out_list_append.extend(int(0x00AD).to_bytes(2,byteorder="big")) 
           data_out_list_append.extend(int(0x00C5).to_bytes(2,byteorder="big")) 

       data_out = bytes(data_out_list_append) 
       print('I2C data written') 
       print(hexlify(data_out)) 
       count = i2cWrite(0x38, data_out)     
       print("Number of data bytes written: %2d bytes \n" % (count)) 
       time.sleep(0.5)  

       ########################################################################################## 
       #Stream off : CMD : 0x000C DATA : 0x0002 
       data_out_list_append = [] 
       for i in range(1, i2c_fifo_word_size * i2c_fifo_depth+1): 
           data_out_list_append.extend(int(0x000C).to_bytes(2,byteorder="big")) 
           data_out_list_append.extend(int(0x0002).to_bytes(2,byteorder="big")) 

       data_out = bytes(data_out_list_append) 
       print('I2C data written') 
       print(hexlify(data_out)) 
       count = i2cWrite(0x38, data_out)     
       print("Number of data bytes written: %2d bytes \n" % (count)) 
       time.sleep(0.5) 
        
       ########################################################################################## 
       #Set Imager mode CMD : 0xDA07 DATA : 0x2021 (Depth is enabled, 12 bit depth, Virtual Channel is enabled, 2 o/p MIPI lanes) 
       data_out_list_append = [] 
       for i in range(1, i2c_fifo_word_size * i2c_fifo_depth+1): 
           data_out_list_append.extend(int(0xDA07).to_bytes(2,byteorder="big")) 
           data_out_list_append.extend(int(0x00FF).to_bytes(2,byteorder="big")) 
           
       data_out = bytes(data_out_list_append) 
       print('I2C data written') 
       print(hexlify(data_out)) 
       count = i2cWrite(0x38, data_out)     
       print("Number of data bytes written: %2d bytes \n" % (count)) 
       #time.sleep(0.5) 

       #read transaction 

       count, rx_data = i2cRead(0x38, 2) 
       print('I2C data read') 
       print(hexlify(rx_data)) 
       print("Number of data bytes read: %2d bytes\n" % (count)) 
       time.sleep(0.5) 

       ######################################################################################### 
       #Stream on CMD : 0x00AD DATA : 0x00C5 
       data_out_list_append = [] 
       for i in range(1, i2c_fifo_word_size * i2c_fifo_depth+1): 
           data_out_list_append.extend(int(0x00AD).to_bytes(2,byteorder="big")) 
           data_out_list_append.extend(int(0x00C5).to_bytes(2,byteorder="big")) 

       data_out = bytes(data_out_list_append) 
       print('I2C data written') 
       print(hexlify(data_out)) 
       count = i2cWrite(0x38, data_out)     
       print("Number of data bytes written: %2d bytes \n" % (count)) 
       time.sleep(0.5) 

       ########################################################################################## 
       #Stream off CMD : 0x000C DATA : 0x0002 
       data_out_list_append = [] 
       for i in range(1, i2c_fifo_word_size * i2c_fifo_depth+1): 
           data_out_list_append.extend(int(0x000C).to_bytes(2,byteorder="big")) 
           data_out_list_append.extend(int(0x0002).to_bytes(2,byteorder="big")) 

       data_out = bytes(data_out_list_append) 
       print('I2C data written') 
       print(hexlify(data_out)) 
       count = i2cWrite(0x38, data_out)     
       print("Number of data bytes written: %2d bytes \n" % (count)) 
       time.sleep(0.5) 
       
       ########################################################################################## 
       #Set Framerate command CMD : 0x0022 DATA : 0x20 (32 FPS)  
       data_out_list_append = [] 
       for i in range(1, i2c_fifo_word_size * i2c_fifo_depth+1): 
           data_out_list_append.extend(int(0x0022).to_bytes(2,byteorder="big")) 
           data_out_list_append.extend(int(0x0020).to_bytes(2,byteorder="big")) 
           
       data_out = bytes(data_out_list_append) 
       print('I2C data written') 
       print(hexlify(data_out)) 
       count = i2cWrite(0x38, data_out)     
       print("Number of data bytes written: %2d bytes \n" % (count)) 
       #time.sleep(0.5) 

       #read transaction 
       count, rx_data = i2cRead(0x38, 2) 
       print('I2C data read') 
       print(hexlify(rx_data)) 
       print("Number of data bytes read: %2d bytes\n" % (count)) 
       time.sleep(0.5)  

       ######################################################################################### 
       #Stream on CMD : 0x00AD DATA : 0x00C5 
       data_out_list_append = [] 
       for i in range(1, i2c_fifo_word_size * i2c_fifo_depth+1): 
           data_out_list_append.extend(int(0x00AD).to_bytes(2,byteorder="big")) 
           data_out_list_append.extend(int(0x00C5).to_bytes(2,byteorder="big")) 

       data_out = bytes(data_out_list_append) 
       print('I2C data written') 
       print(hexlify(data_out)) 
       count = i2cWrite(0x38, data_out)     
       print("Number of data bytes written: %2d bytes \n" % (count)) 
       time.sleep(0.5) 
       ######################################################################################### 

Metadata
--------

Note: The embedded header is 128-bytes.

The following defines the data in the ADSD3500 output embedded data.

+-------------------+-------------------------------+---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| 32-bit Word Index | Name                          | Bit-fields                      | Additional Comments                                                                                                                               |
+===================+===============================+=================================+===================================================================================================================================================+
| 0                 | Frame Characteristics         | **0:15** Width of the image     |                                                                                                                                                   |
|                   |                               | **16:31** Height of the image   |                                                                                                                                                   |
+-------------------+-------------------------------+---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| 1                 | Use Case Details              | **0:7** Output Configuration    | ADSD3500 Output Configuration:                                                                                                                    |
|                   |                               | **8:15** Bits in Depth/Phase    | 0 Full Depth Frame                                                                                                                                |
|                   |                               | **16:23** Bit in AB             | 1 Phase Frame (Partial Depth)                                                                                                                     |
|                   |                               | **24:31** Bits in Confidence    | 2 AB Frame                                                                                                                                        |
|                   |                               |                                 | 3 Confidence Frame                                                                                                                                |
|                   |                               |                                 | 4 Depth AB Interleaved                                                                                                                            |
|                   |                               |                                 | 5 Phase and AB Interleaved                                                                                                                        |
|                   |                               |                                 | 6 Phase, JBLF Confidence and AB Interleaved                                                                                                       |
|                   |                               |                                 | 7 Depth, Confidence and AB Interleaved                                                                                                            |
|                   |                               |                                 | Bit in Depth/Phase:                                                                                                                               |
|                   |                               |                                 | 8, 12 or 16 Based on use case                                                                                                                     |
|                   |                               |                                 | Bits in AB:                                                                                                                                       |
|                   |                               |                                 | 8, 12 or 16 Based on use case                                                                                                                     |
|                   |                               |                                 | Bits in Confidence:                                                                                                                               |
|                   |                               |                                 | 4 or 8 Based on use case                                                                                                                          |
+-------------------+-------------------------------+---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| 2                 | Phase Frame Characteristics   | **0:15** Invalid Phase Value    | In partial depth case, the host must know the invalid phase value used by the ADSD3500, which is used for invalidation during full depth compute. |
|                   |                               | **16:23** Frequency Index       | Frequency Index: Stores index of the frequency for which the phase frame is outputted.                                                            |
|                   |                               | **24:31** AB Frequency Index    | AB Frequency Index:                                                                                                                               |
|                   |                               |                                 | 0 AB of frequency 0                                                                                                                               |
|                   |                               |                                 | 1 AB of frequency 1                                                                                                                               |
|                   |                               |                                 | 2 AB of frequency 2                                                                                                                               |
|                   |                               |                                 | 3 AB Averaged                                                                                                                                     |
+-------------------+-------------------------------+---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| 3                 | Frame Number                  | 0:31 Frame Number               | The frame number, which is incremented per frame                                                                                                  |
+-------------------+-------------------------------+---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| 4                 | Mode                          | **0:7** Imager Mode             | Imager Mode: The imager mode in use                                                                                                               |
|                   |                               | **8:15** Number of Phases       | Number of Phases: Number of phases in the input raw capture fed to the ADSD3500                                                                   |
|                   |                               | **16:23** Number of Frequencies | Number of Frequencies: Number of frequencies in the input raw capture fed to the ADSD3500.                                                        |
+-------------------+-------------------------------+---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| 5                 | Elapsed Time Fractional Value | **0:15** Lower 16-bit value     | 32-bit fractional value out of total elapsed time.                                                                                                |
|                   |                               | **16:31** Upper 16-bit value    |                                                                                                                                                   |
+-------------------+-------------------------------+---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| 6                 | Elapsed Time Seconds Value    | **0:15** Lower 16-bit value     | 32-bit seconds value out of total elapsed time.                                                                                                   |
|                   |                               | **16:31** Upper 16-bit value    |                                                                                                                                                   |
+-------------------+-------------------------------+---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| 7                 | Sensor Temperature            | **0:31** Sensor Temperature     | Sensor temperature in degrees Celsius                                                                                                             |
+-------------------+-------------------------------+---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| 8                 | Laser Temperature             | **0:31** Laser Temperature      | Laser temperature in degrees Celsius                                                                                                              |
+-------------------+-------------------------------+---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
