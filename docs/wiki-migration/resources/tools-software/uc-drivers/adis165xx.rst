.. warning:: Conversion failed for ``resources/tools-software/uc-drivers/adis165xx``

   Reason: pandoc error: Error at "/tmp/tmpp0vedz5f.txt" (line 799, column 1):
expecting inline
not found
| 19 | Read/Write | sync_mode_select | Sync Mode Select Encoded Value | 0 - internal sync, 1 - direct input sync, 2 - scaled sync, 3 - output sync |
^

.. code-block:: text

   ====== ADIS165XX Family - No-OS Driver ======
   ===== Supported Devices =====
     * [[adi>ADIS16500]]
     * [[adi>ADIS16505]]
     * [[adi>ADIS16507]]
   
   
   ===== Overview =====
   ==== ADIS1650X ====
   <hidden>
   The ADIS1650X device series is a precision, miniature microelectromechanical system (MEMS) inertial measurement unit (IMU) that includes a triaxial gyroscope and a triaxial accelerometer. Each inertial sensor in the ADIS1650X device series combines with signal conditioning that optimizes dynamic performance. The factory calibration characterizes each sensor for sensitivity, bias, alignment, linear acceleration (gyroscope bias), and point of percussion (accelerometer location). As a result, each sensor has dynamic compensation formulas that provide accurate sensor measurements over a broad set of conditions. 
   
   Applications
     * Navigation, stabilization, and instrumentation
     * Unmanned and autonomous vehicles
     * Smart agriculture and construction machinery
     * Factory/industrial automation, robotics
     * Virtual/augmented reality
     * Internet of Moving Things
   
   {{:resources:tools-software:uc-drivers:adis16500_pcbzangle-web.png?nolink}} 
   </hidden>
   
   ===== ADI No-OS =====
   The goal of ADI Microcontroller No-OS is to be able to provide reference projects for lower end processors, which can't run Linux, or aren't running a specific operating system, to help those customers using microcontrollers with ADI parts. ADI No-OS offers **generic drivers** which can be used as a base for any microcontroller platform and also **example projects** which are using these drivers on various microcontroller platforms. 
   
   For more information about ADI No-OS and supported microcontroller platforms see: [[:resources:no-os | no-OS]]
   
   
   ===== ADIS No-OS driver =====
   
   ==== ADIS Source Code ====
   The source code for ADIS generic driver can be found here: 
   <WRAP round download 50%>
     *  {{https://github.com/analogdevicesinc/no-OS/blob/master/drivers/imu/adis.h|Header file of ADIS Generic Driver}}
     *  {{https://github.com/analogdevicesinc/no-OS/blob/master/drivers/imu/adis.c|Implementation of ADIS Generic Driver}}
   </WRAP>
   The generic ADIS driver has to be used together with the chip-specific ADIS driver. The source code for the supported chips is listed below:
   
   === ADIS1650X Driver Source Code ===
   <hidden>
   The source code for ADIS1650X driver can be found here: 
   <WRAP round download 50%>
     * {{https://github.com/analogdevicesinc/no-OS/blob/master/drivers/imu/adis1650x.h|Header file of ADIS1650X Driver}}
     *  {{https://github.com/analogdevicesinc/no-OS/blob/master/drivers/imu/adis1650x.c|Implementation of ADIS1650X Driver}}
   </WRAP>
   </hidden>
   
   === ADIS1657X Driver Source Code ===
   <hidden>
   The source code for ADIS1657X driver can be found here: 
   <WRAP round download 50%>
     * {{https://github.com/analogdevicesinc/no-OS/blob/master/drivers/imu/adis1657x.h|Header file of ADIS1657X Driver}}
     *  {{https://github.com/analogdevicesinc/no-OS/blob/master/drivers/imu/adis1657x.c|Implementation of ADIS1657X Driver}}
   </WRAP>
   </hidden>
   \\
   The driver also uses the ADI util library, so make sure you also add the necessary files in your project. The source code for the util library can be found here:
   <WRAP round download 50%>
     * {{https://github.com/analogdevicesinc/no-OS/blob/master/include/no_os_util.h| Header file of ADI util library}}
     * {{https://github.com/analogdevicesinc/no-OS/blob/master/util/no_os_util.c | Implementation file of ADI util library}}
   </WRAP>
   
   In order to be able to use this driver you will have to provide the specific implementation for the communication APIs and the specific types they use.
   For SPI communication, there are four functions which are called by the ADIS driver and have to be implemented:
     * no_os_spi_init() – initializes the communication peripheral.
     * no_os_spi_write_and_read() – writes and reads data to/from the device.
     * no_os_spi_transfer() - iterates over transfer lists and sends all SPI messages
     * no_os_spi_remove() – deinitializes the communication peripheral.
   
   And there are three data types that have to be defined:
     * no_os_spi_desc - structure holding the SPI descriptor
     * no_os_spi_init_param - structure holding the parameters for SPI initialization
     * no_os_spi_msg - structure holding the description for a SPI transfer
   
   An example of a header file containing the prototypes of the functions which have to be implemented, along with some generic data types they are using can be found below:
   
   <WRAP round download 55%>
     * {{https://github.com/analogdevicesinc/no-OS/blob/master/include/no_os_spi.h| Generic header file for SPI Communication APIs}}
   </WRAP>
   
   You will also have to provide specific APIs for GPIO handling. There are five functions which are called by the ADIS driver and have to be implemented:
     * no_os_gpio_get_optional - returns the descriptor to a specific GPIO
     * no_os_gpio_direction_output - enables the output direction of the specified GPIO descriptor
     * no_os_gpio_set_value - sets the value of the specified GPIO to high or low
     * no_os_gpio_remove - frees the resources allocated by no_os_gpio_get_optional
   
   And there are two data types that have to be defined:
     * no_os_gpio_desc - structure holding the GPIO descriptor
     * no_os_gpio_init_param - structure holding the parameters for GPIO initialization
   
   An example of a header file containing the prototypes of the functions which have to be implemented, along with some generic data types they are using can be found below:
   
   <WRAP round download 55%>
     * {{https://github.com/analogdevicesinc/no-OS/blob/master/include/no_os_gpio.h| Generic header file for GPIO APIs}}
   </WRAP>
   
   ==== ADIS Code Driver Documentation ====
   Source code documentation for the driver is automatically generated using the Doxygen tool and it is available below:
     * [[http://analogdevicesinc.github.io/no-OS/doxygen/adis_8h.html|ADIS Generic Driver Header file]]
     * [[http://analogdevicesinc.github.io/no-OS/doxygen/adis_8c.html|ADIS Generic Driver Source file]]
   
   === ADIS1650X Code Driver Documentation ===
   <hidden>
   Source code documentation for the driver is automatically generated using the Doxygen tool and it is available below:
     * [[http://analogdevicesinc.github.io/no-OS/doxygen/adis1650x_8h.html|ADIS1650X Header file]]
     * [[http://analogdevicesinc.github.io/no-OS/doxygen/adis1650x_8c.html|ADIS1650X Source file]]
   </hidden>
   
   === ADIS1657X Code Driver Documentation ===
   <hidden>
   Source code documentation for the driver is automatically generated using the Doxygen tool and it is available below:
     * [[http://analogdevicesinc.github.io/no-OS/doxygen/adis1657x_8h.html|ADIS1657X Header file]]
     * [[http://analogdevicesinc.github.io/no-OS/doxygen/adis1657x_8c.html|ADIS1657X Source file]]
   </hidden>
   
   ==== ADIS Device Initialization ====
   In order to be able to use the device, you will have to provide the support for the communication protocol and GPIO configuration as mentioned above.
   The first API to be called is **adis_init** by providing the adis descriptor and the adis1650x_chip_info. Make sure that it returns 0, which means that the driver was initialized correctly. 
   
   ==== ADIS Device Measurements - Register Readings ====
   
   === Acceleration Data ===
   If you want to obtain a data set for each axis, you may use **adis_read_x_accl**, **adis_read_y_accl** and **adis_read_z_accl** APIs to obtain the raw data. The raw data does not have the scaling applied.
   
   === Gyroscope Data ===
   If you want to obtain a data set for each axis, you may use **adis_read_x_gyro**, **adis_read_y_gyro** and **adis_read_z_gyro** APIs to obtain the raw data. The raw data does not have the scaling applied.
   
   === Delta Velocity Data ===
   If you want to obtain a data set for each axis, you may use **adis_read_x_deltvel**, **adis_read_y_deltvel** and **adis_read_z_deltvel** APIs to obtain the raw data. The raw data does not have the scaling applied.
   
   === Delta Angle Data ===
   If you want to obtain a data set for each axis, you may use **adis_read_x_deltang**, **adis_read_y_deltang** and **adis_read_z_deltang** APIs to obtain the raw data. The raw data does not have the scaling applied.
   
   === Temperature Data ===
   If you want to obtain the temperature data of the device, you may use **adis_read_temp_out** API to obtain the raw data. The raw data does not have the scaling applied.
   
   
   ==== ADIS Device Measurements - Burst Readings ====
   If you want to obtain burst readings, you may use **adis_read_burst_data** API.
   
   The following data will be retrieved, with **burst_size_selection = 0** and ** burst_data_selection = 0**:
   <hidden>
   <code>
   burst_data[0] = DIAG_STAT, bits[15:0]
   burst_data[1] = X_GYRO, bits[15:0]
   burst_data[2] = Y_GYRO, bits[15:0]
   burst_data[3] = Z_GYRO, bits[15:0]
   burst_data[4] = X_ACCEL, bits[15:0]
   burst_data[5] = Y_ACCEL, bits[15:0]
   burst_data[6] = Z_ACCEL, bits[15:0]
   burst_data[7] = TEMP, bits[15:0]
   burst_data[8] = DATA_CNTR, bits[15:0]
   </code>
   In this case, the provided buffer should have a 16-byte size and function call should look like:
   <code C>
   uint16_t burst_data[9];
   int ret = adis_read_burst_data(adis, 18, &burst_data, 0); 
   </code>
   </hidden>
   \\
   
   The following data will be retrieved, with **burst_size_selection = 0** and ** burst_data_selection = 1**:
   <hidden>
   <code>
   burst_data[0] = DIAG_STAT, bits[15:0]
   burst_data[1] = X_DELTANG, bits[15:0]
   burst_data[2] = Y_DELTANG, bits[15:0]
   burst_data[3] = Z_DELTANG, bits[15:0]
   burst_data[4] = X_DELTVEL, bits[15:0]
   burst_data[5] = Y_DELTVEL, bits[15:0]
   burst_data[6] = Z_DELTVEL, bits[15:0]
   burst_data[7] = TEMP, bits[15:0]
   burst_data[8] = DATA_CNTR, bits[15:0]
   </code>
   In this case, the provided buffer should have a 16-byte size and function call should look like:
   <code C>
   uint16_t burst_data[9];
   int ret = adis_read_burst_data(adis, 18, &burst_data, 0); 
   </code>
   </hidden>
   \\
   
   The following data will be retrieved, with **burst_size_selection = 1** and ** burst_data_selection = 0**:
   <hidden>
   <code>
   burst_data[0]  = DIAG_STAT, bits[15:0]
   burst_data[1]  = X_GYRO, bits[31:16]
   burst_data[2]  = X_GYRO, bits[15:0]
   burst_data[3]  = Y_GYRO, bits[31:16]
   burst_data[4]  = Y_GYRO, bits[15:0]
   burst_data[5]  = Z_GYRO, bits[31:16]
   burst_data[6]  = Z_GYRO, bits[15:0]
   burst_data[7]  = X_ACCEL, bits[31:16]
   burst_data[8]  = X_ACCEL, bits[15:0]
   burst_data[9]  = Y_ACCEL, bits[31:16]
   burst_data[10] = Y_ACCEL, bits[15:0]
   burst_data[11] = Z_ACCEL, bits[31:16]
   burst_data[12] = Z_ACCEL, bits[15:0]
   burst_data[13] = TEMP, bits[15:0]
   burst_data[14] = DATA_CNTR, bits[15:0]
   </code>
   In this case, the provided buffer should have a 16-byte size and function call should look like:
   <code C>
   uint16_t burst_data[30];
   int ret = adis_read_burst_data(adis, 30, &burst_data, 1); 
   </code>
   </hidden>
   \\
   
   The following data will be retrieved, with **burst_size_selection = 1** and ** burst_data_selection = 1**:
   <hidden>
   <code>
   burst_data[0]  = DIAG_STAT, bits[15:0]
   burst_data[1]  = X_DELTANG, bits[31:16]
   burst_data[2]  = X_DELTANG, bits[15:0]
   burst_data[3]  = Y_DELTANG, bits[31:16]
   burst_data[4]  = Y_DELTANG, bits[15:0]
   burst_data[5]  = Z_DELTANG, bits[31:16]
   burst_data[6]  = Z_DELTANG, bits[15:0]
   burst_data[7]  = X_DELTVEL, bits[31:16]
   burst_data[8]  = X_DELTVEL, bits[15:0]
   burst_data[9]  = Y_DELTVEL, bits[31:16]
   burst_data[10] = Y_DELTVEL, bits[15:0]
   burst_data[11] = Z_DELTVEL, bits[31:16]
   burst_data[12] = Z_DELTVEL, bits[15:0]
   burst_data[13] = TEMP, bits[15:0]
   burst_data[14] = DATA_CNTR, bits[15:0]
   </code>
   In this case, the provided buffer should have a 30-byte size and function call should look like:
   <code C>
   uint16_t burst_data[15];
   int ret = adis_read_burst_data(adis, 30, &burst_data, 1); 
   </code>
   </hidden>
   \\
   
   ==== ADIS Diagnosis Data ====
   If you want to obtain the diagnosis data of the device, you may use **adis_read_diag_stat** API to obtain the diagnosis flags structure. You may also use individual APIs for each diagnosis flag to obtain the individual value.
   The APIs for retrieving diagnosis flags are specific to the device, as shown below.
   
   === ADIS1650X Diagnosis Data ===
   <hidden>
     * **adis_read_diag_data_path_overrun** - to obtain the data path overrun flag value
     * **adis_read_diag_fls_mem_update_failure** - to obtain the flash memory update error flag value
     * **adis_read_diag_spi_comm_err** - to obtain the SPI communication error flag value
     * **adis_read_diag_standby_mode** - to obtain the standby mode flag value
     * **adis_read_diag_snsr_failure** - to obtain the sensor self test error flag value
     * **adis_read_diag_mem_failure** - to obtain the flash memory test error flag value
     * **adis_read_diag_clk_err** - to obtain the clock error flag value
     * **adis_read_diag_gyro1_failure** - to obtain the gyroscope1 self test error flag value
     * **adis_read_diag_gyro2_failure** - to obtain the gyroscope2 self test error flag value
     * **adis_read_diag_accl_failure** - to obtain the accelerometer self test error flag value
     * **adis_read_diag_checksum_err** - to obtain the checksum error flag value from a previous burst read
     * **adis_read_diag_fls_mem_wr_cnt_exceed** - to obtain the flash memory write counts exceeded flag value (set to true if the flash memory write counter exceeds the endurance value
     * **adis_read_diag_stat** - to obtain all error flags
   </hidden>
   
   === ADIS1657X Diagnosis Data ===
   <hidden>
     * **adis_read_diag_snsr_init_failure** - to obtain the sensor initialization failure flag value
     * **adis_read_diag_data_path_overrun** - to obtain the data path overrun flag value
     * **adis_read_diag_fls_mem_update_failure** - to obtain the flash memory update error flag value
     * **adis_read_diag_spi_comm_err** - to obtain the SPI communication error flag value
     * **adis_read_diag_standby_mode** - to obtain the standby mode flag value
     * **adis_read_diag_snsr_failure** - to obtain the sensor self test error flag value
     * **adis_read_diag_mem_failure** - to obtain the flash memory test error flag value
     * **adis_read_diag_clk_err** - to obtain the clock error flag value
     * **adis_read_diag_x_axis_gyro_failure** - to obtain the X-Axis Gyroscope failure flag value
     * **adis_read_diag_y_axis_gyro_failure** - to obtain the Y-Axis Gyroscope failure flag value
     * **adis_read_diag_z_axis_gyro_failure** - to obtain the Z-Axis Gyroscope failure flag value
     * **adis_read_diag_x_axis_accl_failure** - to obtain the X-Axis Accelerometer failure flag value
     * **adis_read_diag_y_axis_accl_failure** - to obtain the Y-Axis Accelerometer failure flag value
     * **adis_read_diag_z_axis_accl_failure** - to obtain the Z-Axis Accelerometer failure flag value
     * **adis_read_diag_aduc_mcu_fault** - to obtain the ADuC microcontroller fault flag value
     * **adis_read_diag_checksum_err** - to obtain the checksum error flag value from a previous burst read
     * **adis_read_diag_fls_mem_wr_cnt_exceed** - to obtain the flash memory write counts exceeded flag value (set to true if the flash memory write counter exceeds the endurance value)
     * **adis_read_diag_stat** - to obtain all error flags
   </hidden>
   ==== ADIS Identification Data ====
   If you want to obtain identification data specific to the device, you may use the following APIs:
     * **adis_read_prod_id** to obtain the product id
     * **adis_read_serial_num** to obtain the product serial number
     * **adis_read_firm_rev** to obtain the firmware revision
     * **adis_read_firm_d**, **adis_read_firm_m** and **adis_read_firm_y** to obtain the firmware date
     * **adis_read_gyro_meas_range** to obtain gyroscope measurement range encoded value
   
   
   ==== ADIS Configuration Data ====
   === Accelerometer calibration offset ===
   If you want to configure the accelerometer calibration offset on any axis, you may use the following APIs: **adis_write_xa_bias**, **adis_write_ya_bias** or **adis_write_za_bias**.
   
   If you want to read the current accelerometer calibration on any axis, you may use the following APIs:
   **adis_read_xa_bias**, **adis_read_ya_bias** or **adis_read_za_bias**.
   
   === Gyroscope calibration offset ===
   If you want to configure the gyroscope calibration offset on any axis, you may use the following APIs: **adis_write_xg_bias**, **adis_write_yg_bias** or **adis_write_zg_bias**.
   
   If you want to read the current gyroscope calibration on any axis, you may use the following APIs:
   **adis_read_xg_bias**, **adis_read_yg_bias** or **adis_read_zg_bias**.
   
   === Filters configuration ===
     * **adis_write_filt_size_var_b**,  **adis_read_filt_size_var_b**- Bartlett window FIR filter write/read APIs
     * **adis_write_dec_rate**, **adis_read_dec_rate** - decimation filter write/read APIs
     * **adis_write_up_scale**, **adis_read_up_scale** - scale factor for input clock for scaled sync mode write/read APIs
   
   === Continuous Bias Estimation Configuration ===
   Some devices offer continuous bias estimation configuration capabilities. See the information below to view the configuration APIs for the devices which offer continuous bias estimation capabilities.
   
   == ADIS1650X ==
   <hidden>
   This device does not offer continuous bias estimation capabilities.
   </hidden>
   
   == ADIS1657X ==
   <hidden>
     * **adis_write_bias_corr_tbc**, **adis_read_bias_corr_tbc** - to write/read the time base control value
     * **adis_write_bias_corr_en_xg**, **adis_read_bias_corr_en_xg** - to write/read the X-axis gyroscope bias correction enable bit (0 - disabled, 1 - enabled)
     * **adis_write_bias_corr_en_yg**, **adis_read_bias_corr_en_yg** - to write/read the Y-axis gyroscope bias correction enable bit (0 - disabled, 1 - enabled)
     * **adis_write_bias_corr_en_zg**, **adis_read_bias_corr_en_zg** - to write/read the Z-axis gyroscope bias correction enable bit (0 - disabled, 1 - enabled)
     * **adis_write_bias_corr_en_xa**, **adis_read_bias_corr_en_xa** - to write/read the X-axis accelerometer bias correction enable bit (0 - disabled, 1 - enabled)
     * **adis_write_bias_corr_en_ya**, **adis_read_bias_corr_en_ya** - to write/read the Y-axis accelerometer bias correction enable bit (0 - disabled, 1 - enabled)
     * **adis_write_bias_corr_en_za**, **adis_read_bias_corr_en_za** - to write/read the Z-axis accelerometer bias correction enable bit (0 - disabled, 1 - enabled)
   </hidden>
   
   === FIFO Configuration ===
   Some devices offer a hardware FIFO and offer configuration capabilities for the FIFO. See the information below to view the FIFO configuration APIs for the devices which have a hardware FIFO.
   
   == ADIS1650X ==
   <hidden>
   This device does not offer a hardware FIFO.
   </hidden>
   
   == ADIS1657X ==
   <hidden>
     * **adis_write_fifo_en**, **adis_read_fifo_en** - to write/read the FIFO enable bit (0 - direct output mode, 1 - FIFO output mode)
     * **adis_write_fifo_overflow**, **adis_read_fifo_overflow** - to write/read the FIFO overflow behavior bit (0 - stop enqueuing samples, 1 - overwrite the oldest sample)
     * **adis_write_fifo_wm_int_en**, **adis_read_fifo_wm_int_en** - to write/read the FIFO watermark interrupt enable bit (0 - watermark interrupt disabled, 1 - watermark interrupt enabled)
     * **adis_write_fifo_wm_int_pol**, **adis_read_fifo_wm_int_pol** - to write/read the FIFO watermark interrupt polarity (0 - active low, 1 - active high)
     * **adis_write_fifo_wm_lvl**, **adis_read_fifo_wm_lvl** - to write/read the number of samples which must be enqueued into the FIFO to trigger the watermark interrupt
     * **adis_read_fifo_cnt** - to read the current number of samples in the FIFO
   </hidden>
   
   
   === Miscellaneous configuration ===
   Below you may find a list of APIs for device miscellaneous configuration, which is available for all devices:
     * **adis_write_dr_polarity**, **adis_read_dr_polarity** - data ready polarity encoded value write/read APIs
     * **adis_write_sync_polarity**, **adis_read_sync_polarity** - sync polarity encoded value write/read APIs
     * **adis_write_sync_mode**, **adis_read_sync_mode** - synchronization mode encoded value write/read APIs
     * **adis_write_sens_bw**, **adis_read_sens_bw** - sensor bandwidth encoded value write/read APIs
     * **adis_write_pt_of_perc_algnmt**, **adis_read_pt_of_perc_algnmt** - write/read APIs for point of percurssion alignment enable bit (1 -enabled, 0 - disabled)
     * **adis_write_linear_accl_comp**, **adis_read_linear_accl_comp** - write/read APIs for linear acceleration compensation enable bit (1 -enabled, 0 - disabled)
     * **adis_write_burst_sel**, **adis_read_burst_sel** - write/read APIs for burst selection encoded value (0 - acceleration and angular velocity, 1 - delta velocity and delta angle)
     * **adis_write_burst32**, **adis_read_burst32** - write/read APIs for burst32 enable bit (0 - for 16-bit burst data, 1 - for 32-bit burst data)
   
   The following list of APIs for miscellaneous configuration are available only for specific chip-versions:
   
   == ADIS1650X ==
   <hidden>
   There are no other specific APIs for miscellaneous configuration for this chip version.
   </hidden>
   
   == ADIS1657X ==
   <hidden>
     * **adis_write_timestamp32**, **adis_read_timestamp32** - write/read APIs for timestamp32 enable bit (0 - for 16-bit timestamp, 1 - for 32-bit timestamp)
     * **adis_write_sync_4khz**, **adis_read_sync_4khz** - write/read APIs for 4KHz internal sync enable bit (0 - for 2KHz internal sync, 1 - for 4KHz internal sync)
   </hidden>
   ==== ADIS Commands ====
   
   The list below shows the available APIs for triggering device commands. These commands are specific to the selected chip.
   
   === ADIS1650X Commands ===
   <hidden>
     * **adis_cmd_fact_calib_restore** - to perform factory calibration restore command
     * **adis_cmd_snsr_self_test** - to perform sensor self test command
     * **adis_cmd_fls_mem_update** - to perform flash memory update command
     * **adis_cmd_fls_mem_test** - to perform flash memory test command
     * **adis_cmd_sw_res** - to perform software reset command
   </hidden>
   
   
   === ADIS1657X Commands ===
   <hidden>
     * **adis_cmd_bias_corr_update** - to perform bias correction update command
     * **adis_cmd_fact_calib_restore** - to perform factory calibration restore command
     * **adis_cmd_snsr_self_test** - to perform sensor self test command
     * **adis_cmd_fls_mem_update** - to perform flash memory update command
     * **adis_cmd_fls_mem_test** - to perform flash memory test command
     * **adis_cmd_fifo_flush** - to perform fifo flush command
     * **adis_cmd_sw_res** - to perform software reset command
   </hidden>
   ==== ADIS read-only register ====
   There are some other APIs which allow to read some other read-only registers. They are presented below.
     * **adis_read_time_stamp** - reads the current sample time stamp
     * **adis_read_data_cntr** - reads the current sample data counter
   
   === ADIS1650X ===
   <hidden>
   There are no other APIs for this chip version. 
   </hidden>
   
   === ADIS1657X ===
   <hidden>
     * **adis_read_spi_chksum** - reads current sample SPI transaction checksum
   </hidden>
   
   ==== ADIS scratch pad registers ====
   In order to perform read/write operations for device scratch pad registers use the following APIs:
     * **adis_write_usr_scr_1**, **adis_read_usr_scr_1** - write/read APIs for scratch pad register 1
     * **adis_write_usr_scr_2**, **adis_read_usr_scr_2** - write/read APIs for scratch pad register 2
     * **adis_write_usr_scr_3**, **adis_read_usr_scr_3** - write/read APIs for scratch pad register 3
   
   
   ==== ADIS Driver Initialization Example ====
   
   === ADIS1650X Initialization Example ===
   <hidden>
   <code C>
   struct no_os_spi_init_param adis1650x_spi_ip = {
   	.device_id = SPI_DEVICE_ID,
   	.max_speed_hz = SPI_BAUDRATE,
   	.bit_order = NO_OS_SPI_BIT_ORDER_MSB_FIRST,
   	.mode = NO_OS_SPI_MODE_3,
   	.platform_ops = SPI_OPS,
   	.chip_select = SPI_CS,
   	.extra = SPI_EXTRA,
   };
   
   struct no_os_gpio_init_param adis1650x_gpio_reset_ip = {
   	.port = GPIO_RESET_PORT_NUM,
   	.number = GPIO_RESET_PIN_NUM,
   	.pull = NO_OS_PULL_NONE,
   	.platform_ops = GPIO_OPS,
   	.extra = GPIO_EXTRA
   };
   
   struct adis_init_param adis1650x_ip = {
   	.gpio_reset = &adis1650x_gpio_reset_ip,
   	.sync_mode = ADIS_SYNC_OUTPUT,
   	.dev_id = ADIS16505_2,
   };
   
   struct adis_dev *adis1650x_desc;
   int ret;
   int val[7];
   
   adis1650x_chip_info.ip = &adis1650x_ip;
   ret = adis_init(&adis1650x_desc, &adis1650x_chip_info);
   if (ret)
   	goto error;
   
   ret = adis_read_x_gyro(adis1650x_desc, &val[0]);
   if (ret)
   	goto error_remove;
   ret = adis_read_y_gyro(adis1650x_desc, &val[1]);
   if (ret)
   	goto error_remove;
   ret = adis_read_z_gyro(adis1650x_desc, &val[2]);
   if (ret)
   	goto error_remove;
   ret = adis_read_x_accl(adis1650x_desc, &val[3]);
   if (ret)
   	goto error_remove;
   ret = adis_read_y_accl(adis1650x_desc, &val[4]);
   if (ret)
   	goto error_remove;
   ret = adis_read_z_accl(adis1650x_desc, &val[5]);
   if (ret)
   	goto error_remove;
   ret = adis_read_temp_out(adis1650x_desc, &val[6]);
   if (ret)
   	goto error_remove;
   
   error_remove:
   	adis_remove(adis1650x_desc);
   error:
   	pr_info("Error!\n");
   ...
   
   </code>
   </hidden>
   
   === ADIS1657X Initialization Example ===
   <hidden>
   <code C>
   struct no_os_spi_init_param adis1657x_spi_ip = {
   	.device_id = SPI_DEVICE_ID,
   	.max_speed_hz = SPI_BAUDRATE,
   	.bit_order = NO_OS_SPI_BIT_ORDER_MSB_FIRST,
   	.mode = NO_OS_SPI_MODE_3,
   	.platform_ops = SPI_OPS,
   	.chip_select = SPI_CS,
   	.extra = SPI_EXTRA,
   };
   
   struct no_os_gpio_init_param adis1657x_gpio_reset_ip = {
   	.port = GPIO_RESET_PORT_NUM,
   	.number = GPIO_RESET_PIN_NUM,
   	.pull = NO_OS_PULL_NONE,
   	.platform_ops = GPIO_OPS,
   	.extra = GPIO_EXTRA
   };
   
   struct adis_init_param adis1657x_ip = {
   	.gpio_reset = &adis1657x_gpio_reset_ip,
   	.sync_mode = ADIS_SYNC_OUTPUT,
   	.dev_id = ADIS16577_3,
   };
   
   struct adis_dev *adis1657x_desc;
   int ret;
   int val[7];
   
   adis1657x_chip_info.ip = &adis1657x_ip;
   ret = adis_init(&adis1657x_desc, &adis1657x_chip_info);
   if (ret)
   	goto error;
   
   ret = adis_read_x_gyro(adis1657x_desc, &val[0]);
   if (ret)
   	goto error_remove;
   ret = adis_read_y_gyro(adis1657x_desc, &val[1]);
   if (ret)
   	goto error_remove;
   ret = adis_read_z_gyro(adis1657x_desc, &val[2]);
   if (ret)
   	goto error_remove;
   ret = adis_read_x_accl(adis1657x_desc, &val[3]);
   if (ret)
   	goto error_remove;
   ret = adis_read_y_accl(adis1657x_desc, &val[4]);
   if (ret)
   	goto error_remove;
   ret = adis_read_z_accl(adis1657x_desc, &val[5]);
   if (ret)
   	goto error_remove;
   ret = adis_read_temp_out(adis1657x_desc, &val[6]);
   if (ret)
   	goto error_remove;
   
   error_remove:
   	adis_remove(adis1657x_desc);
   error:
   	pr_info("Error!\n");
   ...
   
   </code>
   </hidden>
   
   ==== ADIS Driver Application Example ====
   Below you can fine Application Example Project for ADIS driver: [[:resources:eval:user-guides:eval-adis165xx:no-os-setup| Evaluating the ADIS165XX Family ]] 
   
   ===== IIO ADIS No-OS driver =====
   The IIO ADIS driver comes on top of ADIS driver and offers support for interfacing IIO clients through IIO lib.
   
   ==== IIO ADIS Source Code ====
   The source code for IIO ADIS generic driver can be found here: 
   <WRAP round download 50%>
     *  {{https://github.com/analogdevicesinc/no-OS/blob/master/drivers/imu/iio_adis.h|Header file of IIO ADIS Generic Driver}}
     *  {{https://github.com/analogdevicesinc/no-OS/blob/master/drivers/imu/iio_adis.c|Implementation of IIO ADIS Generic Driver}}
   </WRAP>
   The generic IIO ADIS driver has to be used together with the chip-specific IIO ADIS driver. The source code for the supported chips is listed below:
   
   === IIO ADIS1650X Driver Source Code ===
   <hidden>
   The source code for IIO ADIS1650X driver can be found here: 
   <WRAP round download 50%>
     * {{https://github.com/analogdevicesinc/no-OS/blob/master/drivers/imu/iio_adis1650x.h|Header file of IIO ADIS1650X Driver}}
     *  {{https://github.com/analogdevicesinc/no-OS/blob/master/drivers/imu/iio_adis1650x.c|Implementation of IIO ADIS1650X Driver}}
   </WRAP>
   </hidden>
   
   === IIO ADIS1657X Driver Source Code ===
   <hidden>
   The source code for IIO ADIS1657X driver can be found here: 
   <WRAP round download 50%>
     * {{https://github.com/analogdevicesinc/no-OS/blob/master/drivers/imu/iio_adis1657x.h|Header file of IIO ADIS1657X Driver}}
     *  {{https://github.com/analogdevicesinc/no-OS/blob/master/drivers/imu/iio_adis1657x.c|Implementation of IIO ADIS1657X Driver}}
   </WRAP>
   </hidden>
   
   ==== IIO ADIS Code Driver Documentation ====
   Source code documentation for the IIO driver is automatically generated using the Doxygen tool and it is available below:
     * [[http://analogdevicesinc.github.io/no-OS/doxygen/iio__adis_8h.html|IIO ADIS Generic Driver Header file]]
     * [[http://analogdevicesinc.github.io/no-OS/doxygen/iio__adis_8c.html|IIO ADIS Generic Driver Source file]]
   
   === IIO ADIS1650X Code Driver Documentation ===
   <hidden>
   Source code documentation for the IIO driver is automatically generated using the Doxygen tool and it is available below:
     * [[http://analogdevicesinc.github.io/no-OS/doxygen/iio__adis1650x_8h.html|IIO ADIS1650X Header file]]
     * [[http://analogdevicesinc.github.io/no-OS/doxygen/iio__adis1650x_8c.html|IIO ADIS1650X Source file]]
   </hidden>
   
   === IIO ADIS1657X Code Driver Documentation ===
   <hidden>
   Source code documentation for the IIO driver is automatically generated using the Doxygen tool and it is available below:
     * [[http://analogdevicesinc.github.io/no-OS/doxygen/iio__adis1657x_8h.html|IIO ADIS1657X Header file]]
     * [[http://analogdevicesinc.github.io/no-OS/doxygen/iio__adis1657x_8c.html|IIO ADIS1657X Source file]]
   </hidden>
   
   ==== IIO ADIS Device Configuration ====
   === Device Attributes ===
   The generic IIO ADIS device has the following device specific attributes:
     * filter_low_pass_3db_frequency - which allows the configuration of the ADIS Bartlett window FIR filter
     * sampling_frequency - which allows the configuration of the ADIS sampling frequency
   
   === Device Channels ===
   The generic IIO ADIS device has 0 output channels and 14 input channels: 3 angular velocity channels, 3 acceleration channels, 3 rotation channels, 3 velocity channels, 1 temperature channel and 1 counter channel.
   
   == Angular Velocity Channels ==
   <hidden>
   The angular velocity channels are:
     * Channel 0: anglvel_x
     * Channel 1: anglvel_y
     * Channel 2: anglvel_z
   
   Each angular velocity channel has 3 attributes:
     * calibbias - calibration offset correction
     * raw - the raw angular velocity value read from the device
     * scale - the scale that has to be applied to the raw value in order to obtain the converted real value in rot/s, it has a constant value which is chip-specific.
   </hidden>
   
   == Acceleration Channels ==
   <hidden>
   The acceleration channels are:
     * Channel 3: accel_x
     * Channel 4: accel_y
     * Channel 5: accel_z
   
   Each acceleration channel has 3 attributes:
     * calibbias - calibration offset correction
     * raw - the raw acceleration value read from the device
     * scale - the scale that has to be applied to the raw value in order to obtain the converted real value in m/s^2, it has a constant value which is chip-specific.
   </hidden>
   
   == Temperature Channel ==
   <hidden>
   The temperature channel is:
     * Channel 6: temp
   
   The temperature channel has 2 attributes:
     * raw - the raw temperature value read from the device
     * scale - the scale that has to be applied to the raw value in order to obtain the converted real value in milidegrees Celsius, it has a constant value which is chip-specific.
   </hidden>
   
   == Rotation Channels ==
   <hidden>
   The rotation channels are:
     * Channel 7: rot_x
     * Channel 8: rot_y
     * Channel 9: rot_z
   
   Each rotation channel has 2 attributes:
     * raw - the raw rotation (delta angle) value read from the device
     * scale - the scale that has to be applied to the raw value in order to obtain the converted real value in degrees, it has a constant value which is chip-specific.
   </hidden>
   
   == Velocity Channels ==
   <hidden>
   The velocity channels are:
     * Channel 10: velocity_x
     * Channel 11: velocity_y
     * Channel 12: velocity_z
   
   Each velocity channel has 2 attributes:
     * raw - the raw velocity (delta velocity) value read from the device
     * scale - the scale that has to be applied to the raw value in order to obtain the converted real value in m/s, it has a constant value which is chip-specific.
   </hidden>
   
   == Count Channel ==
   <hidden>
   The count channel is:
     * Channel 13: count
   The count channel does not have any attributes. It is used only in buffer mode to add the data counter value for each sample set obtained in burst mode.
   </hidden>
   
   === Device Debug Attributes ===
   The IIO driver offers the possibility to configure the device and to retrieve diagnosis and configuration data from the device using debug attributes.
   The following list of debug attributes is available:
   
   == ADIS1650X ==
   <hidden>
   ^ Debug Attribute Index ^ Access Type ^ Debug Attribute Name ^ Debug Attribute Description ^ Debug Attribute Valid Values ^
   | 0 | Read-only | diag_data_path_overrun | Data Path Overrun Error Flag | 0 - error did not occur or 1 - error occurred |
   | 1 | Read-only | diag_flash_memory_update_error | Flash Memory Update Error Flag | 0 - error did not occur or 1 - error occurred |
   | 2 | Read-only | diag_spi_communication_error | SPI Communication Error Flag | 0 - error did not occur or 1 - error occurred |
   | 3 | Read-only | diag_standby_mode | Standby Mode Flag | 0 - device is in processing mode, 1 - device is in standby mode (not enough voltage supplied) |
   | 4 | Read-only | diag_sensor_self_test_error | Sensor Self Test Error Flag | 0 - error did not occur or 1 - error occurred |
   | 5 | Read-only | diag_flash_memory_test_error | Flash Memory Test Error Flag | 0 - error did not occur or 1 - error occurred |
   | 6 | Read-only | diag_clock_error | Clock Error Flag | 0 - error did not occur or 1 - error occurred |
   | 7 | Read-only | diag_gyroscope1_self_test_error | Gyroscope 1 Self Test Error Flag | 0 - error did not occur or 1 - error occurred |
   | 8 | Read-only | diag_gyroscope2_self_test_error | Gyroscope 2 Self Test Error Flag | 0 - error did not occur or 1 - error occurred |
   | 9 | Read-only | diag_acceleration_self_test_error | Accelerometer Self Test Error Flag | 0 - error did not occur or 1 - error occurred |
   | 10 | Read-only | diag_checksum_error_flag | SPI Checksum Error Flag | 0 - error did not occur or 1 - error occurred |
   | 11 | Read-only | diag_flash_memory_write_count_exceeded_error | Flash Memory Write Counts Exceeded Flag Error | 0 - error did not occur or 1 - error occurred |
   | 12 | Read-only | lost_samples_count | The number of lost samples during the previous buffer read command | 0 - 4294967295 |
   | 13 | Read-only | time_stamp | The TIME_STAMP register value | 0 - 65535 |
   | 14 | Read-only | data_counter | The DATA_CNTR register value | 0 - 65535 |
   | 15 | Read/Write | filter_size | The FILT_CTRL register value | 0 - 6 |
   | 16 | Read-only | gyroscope_measurement_range | The measurement range identifier | chip specific value with format "+/-###_degrees_per_sec" |
   | 17 | Read/Write | data_ready_polarity | Data Ready Pin Polarity Encoded Value | 0 - active low, 1 - active high |
   | 18 | Read/Write | data_ready_polarity | Sync Pin Polarity Encoded Value | 0 - active low, 1 - active high 
   | 19 | Read/Write | sync_mode_select | Sync Mode Select Encoded Value | 0 - internal sync, 1 - direct input sync, 2 - scaled sync, 3 - output sync |
   | 20 | Read/Write | internal_sensor_bandwidth | Internal Sensor Bandwidth Encoded Value | 0 - wide bandwidth, 1 - 370 Hz |
   | 21 | Read/Write | point_of_percussion_alignment | Point Of Percussion Alignment Enable Bit | 0 - disabled, 1 - enabled |
   | 22 | Read/Write | linear_acceleration_compensation | Linear Acceleration Compensation Enable Bit | 0 - disabled, 1 - enabled |
   | 23 | Read/Write | burst_data_selection | Burst Data Selection Encoded Bit | 0 - burst data contains acceleration and angular velocity measurements, 1 - burst data contains delta-angle and delta-velocity measurements |
   | 24 | Read/Write | burst_size_selection | Burst Size Selection Encoded Bit | 0 - burst data contains 16-bit values, 1 - burst data contains 32-bit values |
   | 25 | Read/Write | sync_signal_scale | Sync Input Frequency Multiplier Register Value | 0 - 65535 |
   | 26 | Read/Write | decimation_filter | Decimation Filter Register Value | 0 - 1999 |
   | 27 | Write-only | factory_calibration_restore | Triggers a factory calibration restore command | Any written value will trigger a factory calibration restore command on the device |
   | 28 | Write-only | sensor_self_test | Triggers a self test command | Any written value will trigger a self test command on the device |
   | 29 | Write-only | flash_memory_update | Triggers a flash memory update command | Any written value will trigger a flash memory update command on the device |
   | 30 | Write-only | flash_memory_test | Triggers a flash memory test command | Any written value will trigger a flash memory test command on the device |
   | 31 | Write-only | software_reset | Triggers a software reset command | Any written value will trigger a software reset command on the device |
   | 32 | Read-only | firmware_revision | The firmware revision value | String containing the firmware revision in the following format ##.## |
   | 33 | Read-only | firmware_date | The firmware data | String containing the firmware date in the following format dd-mm-yyyy |
   | 34 | Read-only | product_id | The product id | Chip specific product id, e.g. 16505, 16575, 16576, 16577, etc.) |
   | 35 | Read-only | serial_number | The serial number | The serial number of the chip - unsigned integer format |
   | 36 | Read/Write | scratch_pad_register1 | The scratch path register 1 | 0 - 65535 |
   | 37 | Read/Write | scratch_pad_register2 | The scratch path register 2 | 0 - 65535 |
   | 38 | Read/Write | scratch_pad_register3 | The scratch path register 3 | 0 - 65535 |
   | 39 | Read-only | flash_counter | The number of the flash writes performed on the device | 0 - 65535 |
   </hidden>
   
   == ADIS1657X ==
   <hidden>
   ^ Debug Attribute Index ^ Access Type ^ Debug Attribute Name ^ Debug Attribute Description ^ Debug Attribute Valid Values ^
   | 0 | Read-only | diag_sensor_initialization_failure | Sensor Initialization Failure Flag | 0 - error did not occur or 1 - error occurred |
   | 1 | Read-only | diag_data_path_overrun | Data Path Overrun Error Flag | 0 - error did not occur or 1 - error occurred |
   | 2 | Read-only | diag_flash_memory_update_error | Flash Memory Update Error Flag | 0 - error did not occur or 1 - error occurred |
   | 3 | Read-only | diag_spi_communication_error | SPI Communication Error Flag | 0 - error did not occur or 1 - error occurred |
   | 4 | Read-only | diag_standby_mode | Standby Mode Flag | 0 - device is in processing mode, 1 - device is in standby mode (not enough voltage supplied) |
   | 5 | Read-only | diag_sensor_self_test_error | Sensor Self Test Error Flag | 0 - error did not occur or 1 - error occurred |
   | 6 | Read-only | diag_flash_memory_test_error | Flash Memory Test Error Flag | 0 - error did not occur or 1 - error occurred |
   | 7 | Read-only | diag_clock_error | Clock Error Flag | 0 - error did not occur or 1 - error occurred |
   | 8 | Read-only | diag_x_axis_gyroscope_failure | X Axis Gyroscope Failure Flag | 0 - error did not occur or 1 - error occurred |
   | 9 | Read-only | diag_y_axis_gyroscope_failure | Y Axis Gyroscope Failure Flag | 0 - error did not occur or 1 - error occurred |
   | 10 | Read-only | diag_z_axis_gyroscope_failure | Z Axis Gyroscope Failure Flag | 0 - error did not occur or 1 - error occurred |
   | 11 | Read-only | diag_x_axis_accelerometer_failure | X Axis Accelerometer Failure Flag | 0 - error did not occur or 1 - error occurred |
   | 12 | Read-only | diag_y_axis_accelerometer_failure | Y Axis Accelerometer Failure Flag | 0 - error did not occur or 1 - error occurred |
   | 13 | Read-only | diag_z_axis_accelerometer_failure | Z Axis Accelerometer Failure Flag | 0 - error did not occur or 1 - error occurred |
   | 14 | Read-only | diag_aduc_mcu_fault | Internal Mcu Fault Flag | 0 - error did not occur or 1 - error occurred |
   | 15 | Read-only | diag_checksum_error_flag | SPI Checksum Error Flag | 0 - error did not occur or 1 - error occurred |
   | 16 | Read-only | diag_flash_memory_write_count_exceeded_error | Flash Memory Write Counts Exceeded Flag Error | 0 - error did not occur or 1 - error occurred |
   | 17 | Read-only | lost_samples_count | The number of lost samples during the previous buffer read command | 0 - 4294967295 |
   | 18 | Read-only | time_stamp | The TIME_STAMP register value | 0 - 65535 if timestamp is 16-bit, 0 - 0 - 4294967295 is timestamp is 32-bit |
   | 19 | Read-only | data_counter | The DATA_CNTR register value | 0 - 65535 |
   | 20 | Read-only | fifo_sample_count | The FIFO_CNT register value | 0 - 511 |
   | 21 | Read-only | spi_checksum | The SPI_CHKSUM register value | 0 - 65535 |
   | 22 | Read/Write | fifo_enable | FIFO Enable Bit Value | 0 - FIFO disabled, 1 - FIFO enabled |
   | 23 | Read/Write | fifo_overflow_behavior | FIFO Overflow Behavior Encoded Value | 0 - stop enqueuing samples, 1 - overwrite the oldest sample |
   | 24 | Read/Write | fifo_watermark_interrupt_enable | FIFO Watermark Interrupt Enable Bit Value | 0 - watermark interrupt disabled, 1 - watermark interrupt enabled |
   | 25 | Read/Write | fifo_watermark_interrupt_polarity | FIFO Watermark Interrupt Polarity Encoded Value | 0 - active low, 1 - active high |
   | 26 | Read/Write | fifo_watermark_threshold_level | FIFO Watermark Threshold Level | 0 - 511 |
   | 27 | Read/Write | filter_size | The FILT_CTRL register value | 0 - 6 |
   | 28 | Read-only | gyroscope_measurement_range | The measurement range identifier | chip specific value with format "+/-###_degrees_per_sec" |
   | 29 | Read/Write | data_ready_polarity | Data Ready Pin Polarity Encoded Value | 0 - active low, 1 - active high |
   | 30 | Read/Write | data_ready_polarity | Sync Pin Polarity Encoded Value | 0 - active low, 1 - active high 
   | 31 | Read/Write | sync_mode_select | Sync Mode Select Encoded Vaalue | 0 - internal sync, 1 - direct input sync, 2 - scaled sync, 3 - output sync |
   | 32 | Read/Write | internal_sensor_bandwidth | Internal Sensor Bandwidth Encoded Value | 0 - wide bandwidth, 1 - 370 Hz |
   | 33 | Read/Write | point_of_percussion_alignment | Point Of Percussion Alignment Enable Bit | 0 - disabled, 1 - enabled |
   | 34 | Read/Write | linear_acceleration_compensation | Linear Acceleration Compensation Enable Bit | 0 - disabled, 1 - enabled |
   | 35 | Read/Write | burst_data_selection | Burst Data Selection Encoded Bit | 0 - burst data contains acceleration and angular velocity measurements, 1 - burst data contains delta-angle and delta-velocity measurements |
   | 36 | Read/Write | burst_size_selection | Burst Size Selection Encoded Bit | 0 - burst data contains 16-bit values, 1 - burst data contains 32-bit values |
   | 37 | Read/Write | time_stamp_size | Timestamp Size Encoded Bit | 0 - timestamp is in 16-bit format, 1 - timestamp is in 32-bit format |
   | 38 | Read/Write | internal_sync_enable_4khz | 4KHz Internal Sync Enable bit | 0 - 2KHz Internal Sync, 1 - 4KHz Internal Sync |
   | 39 | Read/Write | sync_signal_scale | Sync Input Frequency Multiplier Register Value | 0 - 65535 |
   | 40 | Read/Write | decimation_filter | Decimation Filter Register Value | 0 - 1999 |
   | 41 | Read/Write | bias_correction_time_base_control | Bias Correction Time Base Control Value | 0 - 12 |
   | 42 | Read/Write | x_axis_gyroscope_bias_correction_enable | X Axis Gyroscope Bias Correction Enable Bit Value | 0 - correction disabled, 1 - correction enabled |
   | 43 | Read/Write | y_axis_gyroscope_bias_correction_enable | Y Axis Gyroscope Bias Correction Enable Bit Value | 0 - correction disabled, 1 - correction enabled |
   | 44 | Read/Write | z_axis_gyroscope_bias_correction_enable | Z Axis Gyroscope Bias Correction Enable Bit Value | 0 - correction disabled, 1 - correction enabled |
   | 45 | Read/Write | x_axis_accelerometer_bias_correction_enable | X Axis Accelerometer Bias Correction Enable Bit Value | 0 - correction disabled, 1 - correction enabled |
   | 46 | Read/Write | y_axis_accelerometer_bias_correction_enable | Y Axis Accelerometer Bias Correction Enable Bit Value | 0 - correction disabled, 1 - correction enabled |
   | 47 | Read/Write | z_axis_accelerometer_bias_correction_enable | Z Axis Accelerometer Bias Correction Enable Bit Value | 0 - correction disabled, 1 - correction enabled |
   | 48 | Write-only | bias_correction_update | Trigger a bias correction update command | Any written value will trigger a bias correction update command on the device |
   | 49 | Write-only | factory_calibration_restore | Triggers a factory calibration restore command | Any written value will trigger a factory calibration restore command on the device |
   | 50 | Write-only | sensor_self_test | Triggers a self test command | Any written value will trigger a self test command on the device |
   | 51 | Write-only | flash_memory_update | Triggers a flash memory update command | Any written value will trigger a flash memory update command on the device |
   | 52 | Write-only | flash_memory_test | Triggers a flash memory test command | Any written value will trigger a flash memory test command on the device |
   | 53 | Write-only | fifo_flush | Triggers a FIFO flush command | Any written value will trigger a FIFO flush command on the device |
   | 54 | Write-only | software_reset | Triggers a software reset command | Any written value will trigger a software reset command on the device |
   | 55 | Read-only | firmware_revision | The firmware revision value | String containing the firmware revision in the following format ##.## |
   | 56 | Read-only | firmware_date | The firmware data | String containing the firmware date in the following format dd-mm-yyyy |
   | 57 | Read-only | product_id | The product id | Chip specific product id, e.g. 16505, 16575, 16576, 16577, etc.) |
   | 58 | Read-only | serial_number | The serial number | The serial number of the chip - unsigned integer format |
   | 59 | Read/Write | scratch_pad_register1 | The scratch path register 1 | 0 - 65535 |
   | 60 | Read/Write | scratch_pad_register2 | The scratch path register 2 | 0 - 65535 |
   | 61 | Read/Write | scratch_pad_register3 | The scratch path register 3 | 0 - 65535 |
   | 62 | Read-only | flash_counter | The number of the flash writes performed on the device | 0 - 65535 |
   </hidden>
   
   === Device Buffers ===
   The IIO AIDS device driver supports the usage of a data buffer for samples reading purposes. 
   
   
   ==== IIO ADIS Driver Initialization Example ====
   
   === ADIS1650X ===
   <hidden>
   <code C>
   struct no_os_spi_init_param adis1650x_spi_ip = {
   	.device_id = SPI_DEVICE_ID,
   	.max_speed_hz = SPI_BAUDRATE,
   	.bit_order = NO_OS_SPI_BIT_ORDER_MSB_FIRST,
   	.mode = NO_OS_SPI_MODE_3,
   	.platform_ops = SPI_OPS,
   	.chip_select = SPI_CS,
   	.extra = SPI_EXTRA,
   };
   
   struct no_os_gpio_init_param adis1650x_gpio_reset_ip = {
   	.port = GPIO_RESET_PORT_NUM,
   	.number = GPIO_RESET_PIN_NUM,
   	.pull = NO_OS_PULL_NONE,
   	.platform_ops = GPIO_OPS,
   	.extra = GPIO_EXTRA
   };
   
   struct adis_init_param adis1650x_ip = {
   	.gpio_reset = &adis1650x_gpio_reset_ip,
   	.sync_mode = ADIS_SYNC_OUTPUT,
   	.dev_id = ADIS16505_2,
   };
   
   struct no_os_irq_init_param adis1650x_gpio_irq_ip = {
   	.irq_ctrl_id = GPIO_IRQ_ID,
   	.platform_ops = GPIO_IRQ_OPS,
   	.extra = GPIO_IRQ_EXTRA,
   };
   
   const struct iio_hw_trig_cb_info gpio_cb_info = {
   	.event = NO_OS_EVT_GPIO,
   	.peripheral = NO_OS_GPIO_IRQ,
   	.handle = ADIS1650X_GPIO_CB_HANDLE,
   };
   
   struct iio_hw_trig_init_param adis1650x_gpio_trig_ip = {
   	.irq_id = ADIS1650X_GPIO_TRIG_IRQ_ID,
   	.irq_trig_lvl = NO_OS_IRQ_EDGE_RISING,
   	.cb_info = gpio_cb_info,
   	.name = ADIS1650X_GPIO_TRIG_NAME,
   };
   
   #define DATA_BUFFER_SIZE 400
   uint8_t iio_data_buffer[DATA_BUFFER_SIZE*14*sizeof(int)];
   struct adis_iio_dev *adis1650x_iio_desc;
   
   struct iio_data_buffer data_buff = {
   	.buff = (void *)iio_data_buffer,
   	.size = DATA_BUFFER_SIZE*14*sizeof(int)
   };
   
   struct iio_hw_trig *adis1650x_trig_desc;
   struct no_os_irq_ctrl_desc *adis1650x_irq_desc;
   struct iio_app_desc *app;
   struct iio_app_init_param app_init_param = { 0 };
   
   ret = adis1650x_iio_init(&adis1650x_iio_desc, &adis1650x_ip);
   if (ret)
   	return ret;
   
   /* Initialize interrupt controller */
   ret = no_os_irq_ctrl_init(&adis1650x_irq_desc, &adis1650x_gpio_irq_ip);
   if (ret)
   	goto err_irq_init;
   
   ret = no_os_irq_set_priority(adis1650x_irq_desc, adis1650x_gpio_trig_ip.irq_id, 1);
   if (ret)
   	goto err_irq_set_prio;
   
   adis1650x_gpio_trig_ip.irq_ctrl = adis1650x_irq_desc;
   
   /* Initialize hardware trigger */
   ret = iio_hw_trig_init(&adis1650x_trig_desc, &adis1650x_gpio_trig_ip);
   if (ret)
   	goto err_irq_set_prio;
   
   /* List of devices */
   struct iio_app_device iio_devices[] = {
   	{
   		.name = "adis16505-2",
   		.dev = adis1650x_iio_desc,
   		.dev_descriptor = adis1650x_iio_desc->iio_dev,
   		.read_buff = &data_buff,
   	}
   };
   
   /* List of triggers */
   struct iio_trigger_init trigs[] = {
   	IIO_APP_TRIGGER(ADIS1650X_GPIO_TRIG_NAME, adis1650x_trig_desc, &adis_iio_trig_desc)
   };
   
   app_init_param.devices = iio_devices;
   app_init_param.nb_devices = NO_OS_ARRAY_SIZE(iio_devices);
   app_init_param.uart_init_params = adis1650x_uart_ip;
   app_init_param.trigs = trigs;
   app_init_param.nb_trigs = NO_OS_ARRAY_SIZE(trigs);
   app_init_param.irq_desc = adis1650x_irq_desc;
   
   ret = iio_app_init(&app, app_init_param);
   if (ret)
   	goto err_iio_app_init;
   
   /* Update the reference to iio_desc */
   adis1650x_trig_desc->iio_desc = app->iio_desc;
   
   ret = iio_app_run(app);
   if (ret)
   	goto iio_app_err;
   
   return 0;
   
   iio_app_err:
   	iio_app_remove(app);
   err_iio_app_init:
   	iio_hw_trig_remove(adis1650x_trig_desc);
   err_irq_set_prio:
   	no_os_irq_ctrl_remove(adis1650x_irq_desc);
   err_irq_init:
   	adis1650x_iio_remove(adis1650x_iio_desc);
   	pr_info("Error!\n");
   	return ret;
   </code>
   </hidden>
   
   === ADIS1657X ===
   <hidden>
   <code C>
   struct no_os_spi_init_param adis1657x_spi_ip = {
   	.device_id = SPI_DEVICE_ID,
   	.max_speed_hz = SPI_BAUDRATE,
   	.bit_order = NO_OS_SPI_BIT_ORDER_MSB_FIRST,
   	.mode = NO_OS_SPI_MODE_3,
   	.platform_ops = SPI_OPS,
   	.chip_select = SPI_CS,
   	.extra = SPI_EXTRA,
   };
   
   struct no_os_gpio_init_param adis1657x_gpio_reset_ip = {
   	.port = GPIO_RESET_PORT_NUM,
   	.number = GPIO_RESET_PIN_NUM,
   	.pull = NO_OS_PULL_NONE,
   	.platform_ops = GPIO_OPS,
   	.extra = GPIO_EXTRA
   };
   
   struct adis_init_param adis1657x_ip = {
   	.gpio_reset = &adis1657x_gpio_reset_ip,
   	.sync_mode = ADIS_SYNC_OUTPUT,
   	.dev_id = ADIS16577_3,
   };
   
   struct no_os_irq_init_param adis1657x_gpio_irq_ip = {
   	.irq_ctrl_id = GPIO_IRQ_ID,
   	.platform_ops = GPIO_IRQ_OPS,
   	.extra = GPIO_IRQ_EXTRA,
   };
   
   const struct iio_hw_trig_cb_info gpio_cb_info = {
   	.event = NO_OS_EVT_GPIO,
   	.peripheral = NO_OS_GPIO_IRQ,
   	.handle = ADIS1657X_GPIO_CB_HANDLE,
   };
   
   struct iio_hw_trig_init_param adis1657x_gpio_trig_ip = {
   	.irq_id = ADIS1657X_GPIO_TRIG_IRQ_ID,
   	.irq_trig_lvl = NO_OS_IRQ_EDGE_RISING,
   	.cb_info = gpio_cb_info,
   	.name = ADIS1657X_GPIO_TRIG_NAME,
   };
   
   #define DATA_BUFFER_SIZE 400
   uint8_t iio_data_buffer[DATA_BUFFER_SIZE*14*sizeof(int)];
   struct adis_iio_dev *adis1657x_iio_desc;
   
   struct iio_data_buffer data_buff = {
   	.buff = (void *)iio_data_buffer,
   	.size = DATA_BUFFER_SIZE*14*sizeof(int)
   };
   
   struct iio_hw_trig *adis1657x_trig_desc;
   struct no_os_irq_ctrl_desc *adis1657x_irq_desc;
   struct iio_app_desc *app;
   struct iio_app_init_param app_init_param = { 0 };
   
   ret = adis1657x_iio_init(&adis1657x_iio_desc, &adis1657x_ip);
   if (ret)
   	return ret;
   
   /* Initialize interrupt controller */
   ret = no_os_irq_ctrl_init(&adis1657x_irq_desc, &adis1657x_gpio_irq_ip);
   if (ret)
   	goto err_irq_init;
   
   ret = no_os_irq_set_priority(adis1657x_irq_desc, adis1657x_gpio_trig_ip.irq_id, 1);
   if (ret)
   	goto err_irq_set_prio;
   
   adis1657x_gpio_trig_ip.irq_ctrl = adis1657x_irq_desc;
   
   /* Initialize hardware trigger */
   ret = iio_hw_trig_init(&adis1657x_trig_desc, &adis1657x_gpio_trig_ip);
   if (ret)
   	goto err_irq_set_prio;
   
   /* List of devices */
   struct iio_app_device iio_devices[] = {
   	{
   		.name = "adis16577-3",
   		.dev = adis1657x_iio_desc,
   		.dev_descriptor = adis1657x_iio_desc->iio_dev,
   		.read_buff = &data_buff,
   	}
   };
   
   /* List of triggers */
   struct iio_trigger_init trigs[] = {
   	IIO_APP_TRIGGER(ADIS1657X_GPIO_TRIG_NAME, adis1657x_trig_desc, &adis_iio_trig_desc)
   };
   
   app_init_param.devices = iio_devices;
   app_init_param.nb_devices = NO_OS_ARRAY_SIZE(iio_devices);
   app_init_param.uart_init_params = adis1657x_uart_ip;
   app_init_param.trigs = trigs;
   app_init_param.nb_trigs = NO_OS_ARRAY_SIZE(trigs);
   app_init_param.irq_desc = adis1657x_irq_desc;
   
   ret = iio_app_init(&app, app_init_param);
   if (ret)
   	goto err_iio_app_init;
   
   /* Update the reference to iio_desc */
   adis1657x_trig_desc->iio_desc = app->iio_desc;
   
   ret = iio_app_run(app);
   if (ret)
   	goto iio_app_err;
   
   return 0;
   
   iio_app_err:
   	iio_app_remove(app);
   err_iio_app_init:
   	iio_hw_trig_remove(adis1657x_trig_desc);
   err_irq_set_prio:
   	no_os_irq_ctrl_remove(adis1657x_irq_desc);
   err_irq_init:
   	adis1657x_iio_remove(adis1657x_iio_desc);
   	pr_info("Error!\n");
   	return ret;
   </code>
   </hidden>
   
   ==== IIO ADIS Driver Application Example ====
   Below you can find an Application Example Projects for ADIS IIO drivers: [[:resources:eval:user-guides:eval-adis165xx:no-os-setup | Evaluating the ADIS165XX Family]]
