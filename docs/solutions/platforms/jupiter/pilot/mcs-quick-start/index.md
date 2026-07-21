(adc-jupiter-mcs-quick-start)=
# Hardware Setup

This is a guide detailing how to set up the Over the Air (OTA) and RF Splitter Jupiter MCS demos on a Windows platform. Additional information can be found {ref}`here <ad-jupiter-ebz mcs-setup>`.

```{image} jupiter-mcs-pilot-cartoon.jpg
:alt: MCS Block Diagram
:width: 800px
:align: center
```  

## Hardware needed:
- 1x Main machine - its goal is to control and process data from others, through Ethernet(ssh)
- 2x jupiter_sdr + USB C Power supply (5V/3A, 9V/3A) if PoE is not available.
- 2x SD card(min 32G) for jupiter_sdr
- 1x Synchrona + ADD-ON Voltage Translation Board + 12V Power Supply
- 1x Ethernet Switch/Router (at least 5 ports)
- 4x Ethernet cables
- 3x Micro-USB (UART)
- 1x Beamforming array (OTA setup)
- 1x Transmit antenna (OTA setup)
- 9x SMA cables
    - 4x SMA cables of same length and type for > 6GHz (splitter to Jupiter_sdr Rx)
    - 4x SMA cables of same length and type for > 6GHz (Synchrona to Jupiter)
    - 1x SMA cable (Jupiter_sdr Tx to splitter input)

<!-- 
```{image} splitter-mcs.jpg
:alt: RF Splitter Setup
:width: 600px
:align: center
``` 
-->

## Setting up MCS Pilot on Windows
1.	Install Git
2.	Install VS Code, or a similar IDE
    - If VS Code, these extensions are helpful: Python Debugger, Python Environments, Pylance, and Python
3.	Open a new terminal 
4.	Make a directory for Jupiter MCS, then CD into that directory
5.	Type:  
    ```bash
    git clone -b jupiter_sync_update_refactor 
    ```
    -	This will clone the appropriate dependencies
6.	CD into pyadi.iio and follow the commands in the README
    -  	They are:
        -	`pip install . (once in pyadi-iio directory)`
        -	`pip install -r requirements_dev.txt`
7.	Get the additional requirements.txt file and put it in your Jupiter directory
8.	While in the Jupiter directory on VS Code do 
    -	`pip install -r .\requirements.txt`
9.	Go to jupiter_config.py 
    -	Change the IP addresses on lines 34-36
    -	The primary Jupiter is the one with the TX signal
10. Now follow along with the walkthrough (link here)
10.	Run the jupiter_sync_sine_example.py and jupiter_reload_profile_sync_sine_example.py
    -	The reload profile sync example does a re-configure of the devices and then loads the previously stored calibration offsets/weights and it shows the sync is maintained.
    -	You can run this example using the RF splitter and the OTA setup.  

```{image} mcs-ota-pilot.png
:alt: OTA Lab Setup
:width: 600px
:align: center
```  
<!-- 
#### OTA 
1.	If not done, do steps 1-9 in RF Splitter section.
2.	Connect Transmit Antenna to the Tx port of the primary SDR.
3.	Connect the Array Panel to the Rx ports from each of the Jupiters. It should have four connections. -->


```{note}
In the PyADI-IIO repo, you can find two versions of this pilot: one that covers the OTA portion, and another that covers using an RF splitter. The setup procedure is the same for both.
```  

<!-- 
```{note}
To use the OTA setup instead of the RF splitter, go to "jupiter_config.py" and comment the RF Splitter section and uncomment the OTA section so the correct gains are applied.
``` 
-->

```{clear-content}
```  

```{note}
For questions or help with the Jupiter SDR, please visit:

{ez}`fpga`
```

