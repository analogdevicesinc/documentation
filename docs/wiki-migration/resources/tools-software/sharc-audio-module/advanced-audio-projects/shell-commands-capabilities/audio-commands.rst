.. warning:: Conversion failed for ``resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/audio-commands``

   Reason: pandoc error: Error at "/tmp/tmpt3nqr_sz.txt" (line 144, column 1):
expecting inline
not found

^

.. code-block:: text

   ======== Overview ========
   This section describes each of the audio shell commands in detail.
   
   ----
   
   ====== Audio Configuration Shell Commands ======
   
   ===== route =====
   | **Description** | Configures the audio routing table |
   | **Inputs** | idx, src, src offset, dst, dst offset, channels, attenuation, mix/set |
   | **Outputs** | List of routes in the table from indices 0 to 15 |
   | ** Syntax ** | route [<idx> <src> <src offset> <dst> <dst offset> <channels> [attenuation] [mix/set]]\\  {{:resources:tools-software:sharc-audio-module:advanced-audio-projects:shell-commands-capabilities:route_help.png?400|}}|
   | **Example Usage** | route 0 usb 0 codec 0 2 0 (Add a route at 0th index in audio routing table from USB to codec dst with 0 offsets with 2 channels and 0dB attenuation) {{:resources:tools-software:sharc-audio-module:advanced-audio-projects:shell-commands-capabilities:route.png?400|}}|
   
   | **Inputs to route command ** | **Description** | ** Acceptable Values ** |
   | idx | Routing index to add a route to. If the same idx is used to add a new route, the earlier one is overwritten by the new route. Higher the position of the route, the higher is the priority, that is, if two routes have the same source and different destination, the route with higher priority (lower number) is used. In the above picture from example usate, a USB RX to CODEC OUT is at index 0. | 0 to 15 |
   | src | Source stream can be usb, a2b, etc. For a specific list of possible routing options, type help route | Platform specific |
   | src offset | Source offset relates to physical hardware channel mapping. Any route with the same src offset overwrites the already present route at the same offset for the same index. Refer to [[:resources:tools-software:sharc-audio-module:advanced-audio-projects:shell-commands-capabilities:audio-commands:channel-mapping|Hardware channel mapping]] for more details on channel mapping. | 0 to any number |
   | dst| Destination stream, this can be any of the streams listed under src or possible destinations can be listed with help route | Platform specific |
   | dst offset | Destination stream offset relates to physical hardware channel mapping. Refer to [[:resources:tools-software:sharc-audio-module:advanced-audio-projects:shell-commands-capabilities:audio-commands:channel-mapping|Hardware channel mapping]] for more details on channel mapping. | 0 to any number |
   | channels | Number of channels, this can be a number from 0 to any number | 0 to any number |
   | attenuation | Source attenuation in dB (0dB default). It can be negative or positive, they both attenuate by reducing overall gain | any number (positive or negative) |
   | mix/set | Mix or set source into destination ('set' is default). 'mix' lets the two different sources to be mixed and routed to the same output. Without this option, if two routes are set with the same destination, the lower priority (idx) route is clobbered | mix or set (set if none entered) |
   
   ----
   
   ===== a2b =====
   | **Description** | Set A2B Parameters |
   | **Inputs** | none or mode |
   | **Outputs** | Display current A2B mode as main or sub OR set A2B mode |
   | ** Syntax ** | a2b |
   | ::: | a2b [cmd]\\ {{:resources:tools-software:sharc-audio-module:advanced-audio-projects:shell-commands-capabilities:a2b_help.png?400|}} |
   | **Example Usage** | a2b |
   | ::: | a2b mode main\\ {{:resources:tools-software:sharc-audio-module:advanced-audio-projects:shell-commands-capabilities:a2b.png?400|}} |
   
   | **Inputs to a2b command ** | **Description** | ** Acceptable Values ** |
   | cmd | Sets A2B parameter | mode as main/sub |
   
   ----
   
   ===== discover =====
   | **Description** | Discover an A2B network |
   | **Inputs** | A2B command list xml, verbosity, I2C port and tranceiver addr |
   | **Outputs** | Discover A2B nodes in the network and display the status of discovery with number of nodes discovered |
   | ** Syntax ** | discover <a2b.xml> <verbose> <i2c_port> <i2c_addr>\\ {{:resources:tools-software:sharc-audio-module:advanced-audio-projects:shell-commands-capabilities:discover_help.png?400|}} |
   | **Example Usage** | discover <file.xml>\\ {{:resources:tools-software:sharc-audio-module:advanced-audio-projects:shell-commands-capabilities:discover.png?400|}} |
   
   | **Inputs to discover command ** | **Description** | ** Acceptable Values ** |
   | a2b.xml | A SigmaStudio A2B XML config export file | xml file (default 'a2b.xml') |
   | verbose | Print out results to output | 0:none, 1:stdout, 2:syslog (default: 1) |
   | i2c_port | Set the AD242x transceiver I2C port | Valid port number (default: 0 for TWI0) |
   | i2c_addr | Set the AD242x transceiver I2C address | Valid I2C address (default: 0x68) |
   
   ----
   
   ===== wav =====
   | **Description** | Manages wave file source/sink |
   | ** Inputs ** | src/sink, on/off, file, channels, bits | 
   | **Outputs** | Turns src/sink on/off. When no inputs are entered, it lists status of src and sink |
   | ** Syntax ** | wav <src or sink> <on or off> [file] [channels] [bits]\\ {{:resources:tools-software:sharc-audio-module:advanced-audio-projects:shell-commands-capabilities:wav_help.png?400|}} |
   | **Example Usage** | wav src on <file.wav> (Turn on wav source, it can also be passed number of channels and bits per channel) |
   | ::: | wav sink on <file> 2 32 (Turn on sink save the recorded file as 'file') |
   | ::: | wav src off <file.wav> (Turn off wav source) |
   | ::: | wav sink off (Turn off wav sink) |
   | ::: | When both src and sink are ON\\ {{:resources:tools-software:sharc-audio-module:advanced-audio-projects:shell-commands-capabilities:wav.png?400|}} |
   
   | **Inputs to wav command ** | **Description** | ** Acceptable Values ** |
   | src/sink | source or sink | src or sink |
   | on/off | start or stop playing the wav file | on or off |
   | file | wav file name to be played (path/filename) | filename (.wav) |
   | channels | number of audio channels to use | (Optional) Any number |
   | bits | number of bits per channel | (Optional) Any number |
   
   ----
   
   ===== vban =====
   | **Description** | Manages VBAN stream Rx/Tx | 
   | **Inputs** | rx/tx, on/off, ip, port, channels, bits | 
   | **Outputs** | Turns vban src/sink on/off for given IP address and port. When no inputs are entered, it displays status of Rx, Tx channels of vban |
   | **Syntax** | vban <rx/tx> <on/off> <ip> [port] [channels] [bits]\\ {{:resources:tools-software:sharc-audio-module:advanced-audio-projects:shell-commands-capabilities:vban_help.png?400|}}|
   | **Example Usage** | vban rx on 169.254.242.246 6980 2 16 (start receiving vban data on entered IP address and port for 2 channels 16 bits each. Here IP address is that of the board's ethernet interface that can be obtained by 'eth' shell command) |
   | :::               | vban rx domain system (change clock domain from vban to system) |
   | ::: | {{:resources:tools-software:sharc-audio-module:advanced-audio-projects:shell-commands-capabilities:vban_usage.png?400|}} |
   
   | **Inputs to vban command ** | **Description** | ** Acceptable Values ** |
   | rx/tx | direction (receive or transmit) of vban stream | rx or tx |
   | on/off | start or stop vban stream | on or off |
   | ip | IP address of the ethernet port (IP addr of the board when it is configured to receive vban stream and IP addr of the host PC when the board is configured to transmit vban stream) | IP address based on whether it is rx or tx path |
   | port | transport port number that the board is listening on for vban stream | valid port number (Default 6980) |
   | channels | number of audio channels to use | 0 to 32 (Default 2) |
   |bits | number of bits per channel | 16 or 32 (Default 16) |
   
   ----
   
   ===== rtp =====
   | **Description** | Manages RTP stream Rx/Tx |
   | **Inputs** | rx/tx, on/off, ip, port, channels, bits | 
   | **Outputs** | Turns RTP src/sink on/off for given IP address and port. When no inputs are entered, it displays status of Rx, Tx channels of RTP |
   | **Syntax** | rtp <rx/tx> <on/off> <ip> [port] [channels] [bits]\\ {{:resources:tools-software:sharc-audio-module:advanced-audio-projects:shell-commands-capabilities:rtp_help.png?400|}} |
   | **Example Usage** | rtp rx on 169.254.242.246 6980 2 16 (start receiving RTP stream on entered IP address and port for 2 channels 16 bits each. Here IP address is that of the board's ethernet interface that can be obtained by 'eth' shell command) |
   | ::: | rtp rx domain system (change clock domain from rtp to system)\\ {{:resources:tools-software:sharc-audio-module:advanced-audio-projects:shell-commands-capabilities:rtp_usage.png?400|}} |
   
   | **Inputs to rtp command ** | **Description** | ** Acceptable Values ** |
   | rx/tx | direction (receive or transmit) of rtp stream | rx or tx |
   | on/off | start or stop rtp stream | on or off |
   | ip | IP address of the ethernet port (IP addr of the board when it is configured to receive rtp stream and IP addr of the host PC when the board is configured to transmit rtp stream) | IP address based on whether it is rx or tx path |
   | port | transport port number that the board is listening on for rtp stream | valid port number (Default 6970) |
   | channels | number of audio channels to use | 0 to 32 (Default 2) |
   |bits | number of bits per channel | 16 or 32 (Default 16) |
   
   ----
   
   ===== cmdlist =====
   | **Description** | Play a SigmaStudio XML command list |
   | **Inputs** | cmdlist.xml, verbose, i2c_port |
   | **Outputs** | Runs commands from xml file generated by SigmaStudio project to configure A2B network |
   | ** Syntax ** | cmdlist <cmdlist.xml> <verbose> <i2c_port>\\ {{:resources:tools-software:sharc-audio-module:advanced-audio-projects:shell-commands-capabilities:cmdlist_help.png?400|}} |
   | **Example Usage** | cmdlist adi_a2b_commandlist_1.xml 1 0\\ {{:resources:tools-software:sharc-audio-module:advanced-audio-projects:shell-commands-capabilities:cmdlist.png?400|}} |
   
   | **Inputs to cmdlist command ** | **Description** | ** Acceptable Values ** |
   | cmdlist.xml | A SigmaStudio XML command list file | xml file (default 'cmdlist.xml') |
   | verbose | Print out results to selected output | 0:none, 1:stdout, 2:syslog (default: 1) |
   | i2c_port | Set the AD242x transceiver I2C port | Valid I2C port (default: 2 - TWI2) |
   
   ----
   
   ===== vu =====
   | **Description** | Show VU meters |
   | **Inputs** | None |
   | **Outputs** | Shows VU animation for the audio being played |
   | ** Syntax ** | vu\\ {{:resources:tools-software:sharc-audio-module:advanced-audio-projects:shell-commands-capabilities:vu_help.png?400|}} |
   | **Example Usage** | route 3 codec 0 vu 0 32 0 |
   | ::: | vu\\ {{:resources:tools-software:sharc-audio-module:advanced-audio-projects:shell-commands-capabilities:vu.png?400|}} |
   
   ----
   
   ===== adc =====
   | **Description** | Enable or disable the carrier board ADC inputs. Set J4 on SOMCRR-EZKIT to Input or Output. |
   |:::| {{:resources:tools-software:sharc-audio-module:advanced-audio-projects:shell-commands-capabilities:somcrr-ezkit-adc-j4.jpg?200|}} |
   | **Inputs** | None or enable/disable |
   | **Outputs** | Shows adc status or enables/disables adc for J4 connector on SOMCRR-EZKIT. When it is enabled, J4 is set as output, else it is set as input. |
   | ** Syntax ** | adc [enable/disable]\\ {{:resources:tools-software:sharc-audio-module:advanced-audio-projects:shell-commands-capabilities:adc_help.png?400|}} |
   | **Example Usage** | adc disable |
   | ::: | adc enable\\ {{:resources:tools-software:sharc-audio-module:advanced-audio-projects:shell-commands-capabilities:adc.png?400|}} |\\ 
   
   ----
    
   \\ 
   
   ----
   
   {{navigation Shell Commands|Advanced Audio Projects#.examples-ethernet-audio|Application Examples - Ethernet Audio#.|Advanced Audio Projects#.shell-commands-capabilities/audio-commands|Audio Shell Commands}}
