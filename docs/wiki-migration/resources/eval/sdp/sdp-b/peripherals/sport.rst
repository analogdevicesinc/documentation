SPORT: Synchronous Serial Peripheral Port
=========================================

Sport interface supports a variety of serial data communication protocols. Key features and capability of SPORT interface are

-  Continuously running clock
-  Serial data words from 3 to 32 bits in lengths, either MSB or LSB first
-  Two synchronous transmit and two synchronous receive data signals and buffers to double the total supported data stream
-  Configurable frame synchronisation signals

:math:`SPORT TSCLK =SCLK/(2 x(SPORT TCLKDIV+1))`

| SCLK = 120MHz
| SPORT_TCLKDIV = 0 to 65535
| :math:`TSCLK Max = ((120M)/ (2 x(1+1)))=60MHz`
| :math:`\displaystyle TSCLK Min = (\frac{120M}{2 x(65535+1)}) ≈ 915.52Hz`
| Other allowable values : 60MHz, 30MHz, 20MHz, 12MHz, 10MHz, 7.5MHz, 6MHz
| NOTE : The value of Transmit Frame Sync Frequency is a function of the clock frequency of the transmit clock. SPORT_TFSDIV is the number of serial clock cycles between frame sync assertions.

:math:`SPORT TFS = (TSCLK / SPORT TFSDIV +1)`

| SPORT_TFSDIV must be greater than the serial word length -1. This ensures that the the frame sync is deasserted prior to reassertion for the the framed word. Therefore depending on the word size chosen for data transmission and the clock frequency selected the Frame Sync freqency will vary. Taking a 60MHz TSCLK and a serial wordlenght of 32. The minimum and maximum SPORT TFS are calculated as follows
| :math:`\displaystyle SPORT TFS Max = (\frac{60M}{32 +1}) ≈ 1800000 Hz`
| :math:`\displaystyle SPORT TFS Min = (\frac{60M}{65536 +1}) ≈ 1000Hz` The Receive Clock freqency and the Receive Frame Rates available can be calculated similarily to the TSCLK and the TFS rates
| :math:`SPORT RSCLK = (SCLK/(2 x(SPORT_RCLKDIV+1)))`
| SCLK = 120MHz
| SPORT_RCLKDIV = 0 to 65535
| RSCLK Max = 60MHz, RSCLK MIN ≈ 915.52Hz
| :math:`SPORT RFS = (RSCLK/(SPORT RFSDIV +1))`

================= ========================== =======================
Pin Blackfin Name Pin 120 Pin Connector Name Description
================= ========================== =======================
DTxPRI            SPORT_DT0                  Transmit Data Primary
DTxSEC            SPORT_DT1                  Transmit Data Secondary
TSCLKx            SPORT_TSCLK                Transmit Clock
TFSx              SPORT_TFS                  Transmit Frame Sync
DRxPRI            SPORT_DR0                  Receive Data Primary
DRxSEC            SPORT_DR1                  Receive Data Secondary
RSCLKx            SPORT_RSCLK                Receive Clock
TRSx              SPORT_RFS                  Receive Frame Sync
================= ========================== =======================

| Table 1: SPORT Pin Assignments
| There are two transmit and two receive channels in the SPORT interface. By default the primary transmit and receive channels, DT0 and DR0, are enabled and the secondary transmit and receive channels, DT1 and DR1, are disabled. To enable the secondary transmit and receive channels, set the secEnable property in the SPORT object to true and wire the second transmit and receive lines to DT1 and DR1. The max clock frequency which can be used in this case is now halved, so 30MHz SPORT TSCLK and RSCLK. The data sent down to the SDP should be interleaved, the every second location containing data for DT0 and DT1 respectively. Below is a timing example showing the transmit clock, frame sync and data lines with SecEnable set to true.
| To achieve the example below the array transmitted over the SPORT interface is

===== ======= =======
Index Element Channel
===== ======= =======
0     0x49    DT0
1     0x96    DT1
2     0x31    DT0
3     0xC6    DT1
===== ======= =======

.. image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-b/sdp-b_periphexpl1.png
   :alt: sdp-b_periphexpl1.png
   :align: left
   :width: 750px

Similarly data read from the SDP SPORT Interface in secEnable mode must be de-interleaved in the top level application to separate the data into data from DR0 and DR1.

Understanding the Frame Sync Signal
-----------------------------------

| 
| An Early Frame Sync Signal will be active for one clock pulse, and then become deactivate. Once the signal has been deactivated, valid data will be available.
| A Late Frame Sync Signal frames the valid data, so is active for the length of time that valid data is available and is deactivated once the word to be transmitted or received has been fully sent.
| |sdp-b_periphexpl2.png|
| Figure 1 : SPORT Frame Sync Signals

| 
| Receive Data
| |sdp-b_periphexpl3.png|
| Figure 2 : SPORT_DR0/SPORT_DR1 & early frame sync
| |sdp-b_periphexpl4.png|
| Figure 3 : SPORT_DR0/SPORT_DR1 & late frame sync
| Transmit Data
| |sdp-b_periphexpl5.png|
| Figure 4 : SPORT_DT0/SPORT_DT1 & late frame sync
| There are two SPORT Controllers on the Blackfin BF527 and these are exposed through the two connectors on the SDP-B.
| SPORT0 is on Connector A of the SDP, SPORT1 is on Connector B of the SDP.
| The SPORT Interface Pins are 3.3V tolerant only.

.. |sdp-b_periphexpl2.png| image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-b/sdp-b_periphexpl2.png
   :width: 500px
.. |sdp-b_periphexpl3.png| image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-b/sdp-b_periphexpl3.png
   :width: 500px
.. |sdp-b_periphexpl4.png| image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-b/sdp-b_periphexpl4.png
   :width: 500px
.. |sdp-b_periphexpl5.png| image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-b/sdp-b_periphexpl5.png
   :width: 500px
