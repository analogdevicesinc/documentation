SPI: Serial Port Interface
==========================

The SPI interface on the SDP is a full duplex, synchronous serial interface. The SDP is the Master for all SPI transfers. When an SPI transfer occurs, data is simultaneously transmitted as new data is received. The SPI_CLK signal synchronises the shifting of data out and the sampling of data in on the two serial data pins (MOSI and MISO).

===== ============================== =======================
Pin # Pin SDP 120 Pin Connector Name Description
===== ============================== =======================
82    SPI_CLK                        SPI Serial Clock
83    SPI_MISO                       SPI Master In Slave Out
84    SPI_MOSI                       SPI Master Out Slave In
85    SPI_SEL_A                      SPI Slave Select 1
37    SPI_SEL_B                      SPI Slave Select 2
38    SPI_SEL_C                      SPI Slave Select 3
===== ============================== =======================

| Table 1: SPI Pin Assignments

The SPI protocol supports four different combinations of serial clock and polarity modes, SPI Modes 0, 1, 2 & 3.

==== ==================== =================
Mode CPOL, Clock Polarity CPHA, Clock Phase
==== ==================== =================
0    0                    0
1    0                    1
2    1                    0
3    1                    1
==== ==================== =================

Table 2 : SPI Modes

| |image1|
| Figure 1 : SPI Modes Explained

| The maximum clock frequency for SDP-S SPI transfers is 10MHz.
| The maximum frame frequency for SDP-S SPI transfers is shown below...

============= ==================== ======== ======== ========
Transfer size Frame Freq Max                         
============= ==================== ======== ======== ========
\             SPI Write, WriteRead          SPI Read 
\             Mode 0,2             Mode 1,3 Mode 0,2 Mode1,3
8 bits        500kHz               465.1kHz 456.6kHz 450.4kHz
16 bits       323.6kHz             308.6kHz 310.5kHz 307.6kHz
24 bits       255.1kHz             245.7kHz 246.9kHz 245kHz
32 bits       210kHz               203.6kHz 204.4kHz 203.2kHz
============= ==================== ======== ======== ========

| Table 3: SPI Frame Frequency Limits

SPI Timing Examples
-------------------

These timing examples are estimated and not guaranteed to be an exact reflection of the interface timing. These examples were generated for a 10MHz SCLK and the delays listed are the estimated maximum times.

| |image2|
| Figure 2 : SPI transfer protocol, CPHA = 0, 8 bit data

| |image3|
| Figure 3 : SPI transfer protocol, CPHA = 1, 8 bit data

| |image4|
| Figure 4 : SPI transfer protocol, CPHA = 0, 16 bit data

| |image5|
| Figure 5 : SPI transfer protocol, CPHA = 1, 16 bit data

| |image6|
| Figure 6 : SPI transfer protocol, CPHA = 0, >16 bit data

| |image7|
| Figure 7 : SPI transfer protocol, CPHA = 1, >16 bit data

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
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-s/peripherals/cpha0-u8.jpg
   :width: 500px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-s/peripherals/cpha1-u8.jpg
   :width: 500px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-s/peripherals/cpha0-u16.jpg
   :width: 750px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-s/peripherals/cpha1-u16.jpg
   :width: 750px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-s/peripherals/cpha0-u16plus.jpg
   :width: 750px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-s/peripherals/cpha1-u16plus.jpg
   :width: 750px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-b/sdp-b_periphexpl14.png
   :width: 500px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-b/sdp-b_periphexpl15.png
   :width: 700px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-b/sdp-b_periphexpl16.png
   :width: 700px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-b/sdp-b_periphexpl17.png
   :width: 700px
