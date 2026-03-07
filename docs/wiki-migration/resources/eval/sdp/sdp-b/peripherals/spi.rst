SPI: Serial Port Interface
==========================

The SPI interface on the SDP is a full duplex, synchronous serial interface. The SDP is the Master for all SPI transfers. When an SPI transfer occurs, data is simultaneously transmitted as new data is received. The SPI_CLK signal synchronises the shifting of data out and the sampling of data in on the two serial data pins (MOSI and MISO).

================= ============================== =======================
Pin Blackfin Name Pin SDP 120 Pin Connector Name Description
================= ============================== =======================
SCLK              SPI_CLK                        SPI Serial Clock
MISO              MISO                           SPI Master In Slave Out
MOSI              MOSI                           SPI Master Out Slave In
SPISS/SPISEL1     SPI_SEL1/SPI_SS                SPI Slave Select Input
Connector A only                                 
SPISEL2           SPI_SEL_C                      SPI Slave Select 2
SPISEL6           SPI_SEL_B                      SPI Slave Select 6
SPISEL4           SPI_SEL_A                      SPI Slave Select 4
Connector B only                                 
SPISEL3           SPI_SEL_C                      SPI Slave Select 3
SPISEL7           SPI_SEL_B                      SPI Slave Select 7
SPISEL5           SPI_SEL_A                      SPI Slave Select 5
================= ============================== =======================

| Table 1: SPI Pin Assignments
| The maximum clock frequency for SPI transfers is: 30MHz.
| The maximum frame frequency for SPI transfers is shown below...

============= ================================
Transfer size Frame Freq Max ( for 30MHz sclk)
============= ================================
8 bits        ~1.4MHz
16 bits       ~1MHz
24 bits       ~445kHz
32 bits       ~485kHz
40 bits       ~260kHz
48 bits       ~220kHz
============= ================================

| Table 2: SPI Frame Frequency Limits
| The SDP’s SPI protocol is a hybrid of the Blackfin’s Hardware SPI controller and a software implemented chip select option. The internal Blackfin hardware SPI controller allows 8 or 16 bit transfers only. The SDP SPI implementation uses the hardware shift registers of the Blackfin SPI controller but with a software controlled chip select. This allows the SDP to handle SPI transfers of 8, 16, 24, 32, 40 and 48 bits. The software controlled chip selects framing period is not repeatedly consistent. There is jitter on the Chip Select frame rate. For this reason the SPI can be used for control data or burst transfers but cannot implement streaming.
| The SPI protocol supports four different combinations of serial clock and polarity modes, SPI Modes 0, 1, 2 & 3.

==== ==================== =================
Mode CPOL, Clock Polarity CPHA, Clock Phase
==== ==================== =================
0    0                    0
1    0                    1
2    1                    0
3    1                    1
==== ==================== =================

Table 3 : SPI Modes

| |image1|
| Figure 1 : SPI Modes Explained

SPI Timing Examples
-------------------

Below are timing examples for each of the 4 data transfer sizes in the SDP-B SPI protocol. Note the wait times after the CS goes active and the wain times between successive bursts of 8 or 16 bit data in the 24 and 32bit transfers cannot be guaranteed but are included to give a rough estimate of the timing specifications for the SPI interface on the SDP.

| |image2|
| Figure 2 : SPI transfer protocol, CPHA = 0, 8 bit data

| |image3|
| Figure 3 : SPI transfer protocol, CPHA = 0, 16 bit data

| |image4|
| Figure 4 : SPI transfer protocol, 24 bit data

| |image5|
| Figure 5 : SPI transfer protocol, 32 bit data

| |image6|
| Figure 6 : SPI transfer protocol, 40 bit data

| |image7|
| Figure 7 : SPI transfer protocol, 48 bit data

SPI Extended Interfaces for converters
--------------------------------------

| This section introduces timing diagrams for interfacing to ADI parts that requires Busy or Ready signals combined to CS to decode the part. The singularity of these modes is that the MISO line provides double functionality, data and ready signal.
| The serial interface can operate in 3-wire mode by tying CS low. The end of conversion can be monitored using RDY and/or Busy. The DOUT/RDY pin functions as a data ready signal also, with the line going low when a new data-word is available in the output register.
| Given the complexity of the implementation, the description below provides an additional explanation of how these interfaces are programmed to be used within the SDP.
| |image8|
| Figure 8 : Single Read more with RDY

| |image9|
| Figure 9 : Single Conversion Mode with RDY (AD7190 example)

========================= ======================
LabVIEW Implementation    
========================= ======================
Interface Type            Single Conversion Mode
Bytes to Configure        
- before/while busy       4
- after busy              1
Bytes to read             Data + Status + CRC
Repeat Read Command       False
Enable CS between Samples False
SPI Write Buffer U8       0x08
:::                       0x28
:::                       0x00
:::                       0x60
========================= ======================

| |image10|
| Figure 10 : Continuous Conversion mode with RDY (ADI7190 example)

========================= ==========================
LabVIEW Implementation    
========================= ==========================
Interface Type            Continuous Conversion Mode
Bytes to Configure        
- before/while busy       0
- after busy              1
Bytes to read             Data + Status + CRC
Repeat Read Command       True
Enable CS between Samples True
SPI Write Buffer U8       0x58
========================= ==========================

| |image11|
| Figure 11 : Continuous Read Mode with RDY (ADI7190 example)

========================= ====================
LabVIEW implementation    
========================= ====================
Interface Type            Continuous Read Mode
Bytes to Configure        
Before/while busy         1
After Busy                0
Bytes to Read             Data + Status + CRC
Repeat Read Command       False
Enable CS between Samples True
SPI Write Buffer U8       0x5C
========================= ====================

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-b/sdp-b_periphexpl7.png
   :width: 500px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-b/sdp-b_periphexpl8.png
   :width: 500px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-b/sdp-b_periphexpl9.png
   :width: 800px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-b/sdp-b_periphexpl10.png
   :width: 800px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-b/sdp-b_periphexpl11.png
   :width: 800px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-b/sdp-b_periphexpl12.png
   :width: 700px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-b/sdp-b_periphexpl13.png
   :width: 700px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-b/sdp-b_periphexpl14.png
   :width: 500px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-b/sdp-b_periphexpl15.png
   :width: 700px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-b/sdp-b_periphexpl16.png
   :width: 700px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-b/sdp-b_periphexpl17.png
   :width: 700px
