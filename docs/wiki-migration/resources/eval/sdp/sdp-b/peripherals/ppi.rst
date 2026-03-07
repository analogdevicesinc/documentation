.. warning:: Conversion failed for ``resources/eval/sdp/sdp-b/peripherals/ppi``

   Reason: pandoc error: Error at "/tmp/tmpsir_0nql.txt" (line 27, column 1):
expecting inline
not found

^

.. code-block:: text

   ==== PPI: Parallel Peripheral Interface ====
   
   PPI is a half-duplex, bi-directional port accommodating up to 16 bits of data. It has a dedicated clock pin and three multiplexed frame sync pins. PPI supports up to 16 bits of data with programmable clock and frame sync polarities. PPI requires an externally generated free running clock. \\
   The maximum PPI Clock Frequency achievable on the SDP for a single frame transfer is 50MHz. The maximum transfer rate on SDP for streaming data over the PPI is achievable by using a 20-25 MHz PPI clock.
   
   ^Pin - Blackfin Name^Pin - SDP 120 Pin Connector Name^Description^
   |PPI_CLK|PAR_CLK|PPI Clock|
   |PPI_FS1|PAR_FS1|PPI Frame Sync 1|
   |PPI_FS2|PAR_FS2|PPI Frame Sync 2|
   |PPI_FS3|PAR_FS3|PPI Frame Sync 3|
   |PPI_D0|PAR_D0|PPI Data 0|
   |PPI_D1|PAR_D1|PPI Data 1|
   |PPI_D2|PAR_D2|PPI Data 2|
   |PPI_D3|PAR_D3|PPI Data 3|
   |PPI_D4|PAR_D4|PPI Data 4|
   |PPI_D5|PAR_D5|PPI Data 5|
   |PPI_D6|PAR_D6|PPI Data 6|
   |PPI_D7|PAR_D7|PPI Data 7|
   |PPI_D8|PAR_D8|PPI Data 8|
   |PPI_D9|PAR_D9|PPI Data 9|
   |PPI_D10|PAR_D10|PPI Data 10|
   |PPI_D11|PAR_D11|PPI Data 11|
   |PPI_D12|PAR_D12|PPI Data 12|
   |PPI_D13|PAR_D13|PPI Data 13|
   |PPI_D14|PAR_D14|PPI Data 14|
   |PPI_D15|PAR_D15|PPI Data 15| \\
   Table 1 : Pin Assignments
   
   The maximum transfer rate is entirely dependent on the PC performance, so can vary depending on the other software tasks running at teh same time. The USB transfer rate can also vary as a result of the CPU workload so the frame sync length across the PPI interface can vary accordingly. \\
   The PPI interface requires an external source to generate a free running clock and implement some flow control. \\ 
   {{:resources:eval:sdp:sdp-b:sdp-b_periphexpl18.png?500|}}
   \\ Figure 1 : PPI Interface connection to receive data \\
   
   A maximum of 32k words of 16 bits per frame (PPI_FS1) can be sent in each PPI transfer. The SDP board controls the transfer through the implementation of a second frame called Master Ready (PPI_FS2-MR). This enables, or stops, the data transfer from the FPGA or external source. If the SDP internal buffer structure is full or the USB connection is very slow, the MR signal goes low and will pause the data transfer. Otherwise, MR is active and a new PPI_FS1 signal is generated.
   
   {{:resources:eval:sdp:sdp-b:sdp-b_periphexpl19.png?800|}}
   \\ Figure 2 : PPI Transfer Protocol \\
   
   === Asynchronous Parallel === 
   The Asynchronous memory interface is available through the External Bus Interface Unit (EBIU). The Asynchronous Memory Bank made available is from 0x20000000 to 0x200FFFFF. The EBIU is clocked by the System Clock, SCLK, which runs at 120MHz.
   
   ^Pin - Blackfin Name^Pin - SDP 120 Pin Connector Name^Description^
   |/ARE|/PAR_RD|Asynchronous Read Enable|
   |/AWE|/PAR_WR|Asynchronous Write Enable|
   |/AMS0|/PAR_CS|Asynchronous Memory Bank Select|
   |PG9|PAR_INT|Asynchronous Interrupt|
   |A1|PAR_A0|External Address Bus|
   |A2|PAR_A1|External Address Bus|
   |A3|PAR_A2|External Address Bus|
   |A4|PAR_A3|External Address Bus|
   |D0|PAR_D0|External Data Bus|
   |D1|PAR_D1|External Data Bus|
   |D2|PAR_D2|External Data Bus|
   |D3|PAR_D3|External Data Bus|
   |D4|PAR_D4|External Data Bus|
   |D5|PAR_D5|External Data Bus|
   |D6|PAR_D6|External Data Bus|
   |D7|PAR_D7|External Data Bus|
   |D8|PAR_D8|External Data Bus|
   |D9|PAR_D9|External Data Bus|
   |D10|PAR_D10|External Data Bus|
   |D11|PAR_D11|External Data Bus|
   |D12|PAR_D12|External Data Bus|
   |D13|PAR_D13|External Data Bus|
   |D14|PAR_D14|External Data Bus|
   |D15|PAR_D15|External Data Bus|
   \\ Table 2:Asynchronour Parallel Pin Assignment
   
   {{:resources:eval:sdp:sdp-b:sdp-b_periphexpl20.png?800|}}
   \\ Figure 3 : Asynchronous Write Followed by a Read\\
   
   
   
