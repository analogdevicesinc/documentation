Register Control Window
=======================

| :doc:`Click here to return to the Hardware Windows page. </wiki-migration/resources/tools-software/sigmastudio/developmentenvironment/hardware_windows>`
| The Register Control windows provides access to the internal registers and core settings for the DSP and IC blocks inserted in the Hardware configuration window.

To access the Register Control window:

-  Click the Hardware Configuration tab at the top of the workspace.
-  Click the Register Control tab (1) at the bottom of the Hardware Configuration window or Right-click on the DSP processor block and select Register Window (2) from the menu.

| |regpic1.png|
| The controls and settings available in the Register Control window are different for each Processor (IC/DSP) block, depending on the hardware's capability. Any changes made in the register control window are immediately sent to the hardware when there is an active USB communication channel.
| Following is a description of the AD1940 Register Control window. For information about these or other IC register settings, please see the refer to your part's datasheet: www.analog.com/sigmadsp
| |regpic2.png|

**1. Internal Registers** This area lists addresses 2642 - 2646 and their status. As you make changes in the other areas of the window, you'll see the results here. If you know the register bit locations you want to change, you can change them here as well, and the buttons in the other areas of the window will be updated accordingly.

-  2642 - DSP Core Control Register
-  2643 - Ram Configuration Register
-  2644 - Serial Output Control Register 1
-  2645 - Serial Output Control Register 2
-  2646 - Serial Input Control Register

**2. Serial Input** - affects the serial-input control register (address 2646), controlling clock polarity and data input modes.

-  **Serial Input Mode (Bits 2:0)** - These two bits control the data format that the input port expects to receive. For settings and clock diagrams, see the AD1940/-41 datasheet pp 27-29.
-  **BCLK Polarity (Bit 3)** - This bit controls on which edge of the bit clock the input data are clocked: the falling edge of BCLK_IN when this bit is set to 0, and the rising edge when it's set to 1.
-  **LRCLK Polarity (Bit 4)** - If bit 4 set to 0, the left-channel data on the SDATA_Inx pins are clocked when LRCLK_IN is low and the right data clocked when LRCLK_IN is high. When bit 4 set to 1, this is reversed.
-  In TDM mode, when this bit is set to 0, data are clocked in starting with the next appropriate BCLK edge following a falling edge on the LRCLK_IN pin. When the bit is set to 1 (in TDM mode), the input data are valid on the BCLK edge following a rising edge on LRCLK_IN.
-  **TDM Input (Bit 5)** - Setting this bit to 0 puts the AD1940/-41 into dual 8-channel TDM input mode, with the two streams coming in on SDATA_IN2 and SDATA_IN3. Setting it to 1 puts the part into 16-channel TDM input mode, input on pin SDATA_IN2.

| **3. Ram Modulo** - *affects the ram-configuration register (address 2643)*
| The AD1940/1941 uses a modulo RAM-addressing scheme to allow filters and other blocks to be coded easily without requiring filter data to be explicitly moved during the filtering operation. The default value is 12 where the entire 6144 (6k) RAM is treated as modulo memory with auto-incrementing address-offset registers. Each LSB of this register corresponds to 512 RAM locations. A modulo value of 11 would give you 5632 datawords of modulo memory and 512 in a non-modulo portion.

**4. DSP Core** - affects DSP core control register (address 2642)

The controls in this register set the operation of the AD1940/-41's DSP core.

-  **Program Length (Bits 1:0)** - These bits set the length of the internal program. The default length is 1536 instructions, but it can be shortened by factors of 2 to accommodate sample rates higher than 48 kHz.
-  **Input Serial Port to Sequencer Synch (Bits 3:2)** - Normally the internal sequencer is synchronized to the incoming audio frame rate by comparing the internal program counter with the edge of the LRCLK input signal. In some cases the AD1940/-41 may be used to decimate an incoming signal by some integer factor. In this case, it is desirable to synch the sequencer to a submultiple of the incoming LRCLK rate so more than one audio input sample is available to the program during a single audio output frame. (Operation in this mode may require custom assembly-language coding not currently supported by ADI graphical tools.)
-  **Zero Serial Input (Bit 6)** - When this bit is set to 1, the eight serial input channels are forced to all zeros.
-  **Zero Data Memory (Bit 7)** - Setting this bit to 1 initializes all data memory locations to 0. This bit is cleared to 0 after the operation is complete. This bit should be asserted after a complete program/parameter download has occurred to ensure clickfree operation.
-  **Zero Multiplier (Bit 8)** - When this bit is set to 1, the input to the DSP multiplier is set to 0, which results in the multiplier output being 0. This control bit is included for maximum flexibility and normally is not used.
-  **Zero All Registers (Bit 9)** - Active low. Setting this bit to 0 sets the contents of the accumulators and serial output registers to 0. Like the other register bits, this one powers up to 0. That means the AD1940/-41 will not pass a signal until a 1 is written to this bit. This is intended to prevent inadvertent noises from accruing during the powerup sequence.
-  **Use LRCLK for Output Latch (Bit 10)** - Normally, data are transferred from the DSP core to the serial output registers at the end of each program cycle. In some cases (e.g., when the output sample rate is set to some multiple of the input sampling rate), it is desirable to transfer the internal core data multiple times during a single input audio sample period. Setting this bit to 1 allows the output LRCLK signal to control the data transfer rather than the internal end-of-sequence signal. (Operation in this mode may require custom assembly-language coding not currently supported by ADI graphical tools.)
-  **Mute Slew Ram (Bit 12)** - Setting this bit to 1 initiates a mute of all 64 slew RAM locations. When reset to 0, all RAM locations return to their previous state. This bit is functional only if slew RAM locations are used in the custom program design.

**5, 6. Serial Outputs 1 (address 2644) and 2 (address 2645)** The output control registers give the user control of clock polarities, clock frequencies and types, and data format. In all modes except for the right-justified ones (MSB delayed by 8, 12, or 16), the serial port accepts an arbitrary number of bits up to 24. Extra bits will not cause an error but will be truncated internally. Proper operation of the right-justified modes requires the LSB to align with the edge of the LRCLK.

-  **Wordlength (Bits 1:0)** - These bits set the length of the output dataword. Options are 16, 20, or 24 bits.
-  **MSB Position (Bits 4:2)** - These three bits set the position of the MSB of data with respect to the LRCLK edge. The data output of the AD1940/-41 is always MSB first.
-  **Frame Synch Type (Bit 6)** - This bit sets the type of signal on the LRCLK_OUTx pins. When set to 0, the signal is a clock with a 50% duty cycle; when set to 1, the signal is a pulse with a duration of one bit clock at the beginning of the data frame.
-  **Frame Synch Frequency (Bits 8:7)** - When the output port is used as a clock master, these bits set the frequency of the output LRCLK, which is divided down from the internal 73.728 MHz core clock.
-  **BCLK frequency (Bits 10:9)** - When the output port is being used as a clock master, these bits set the frequency of the output bit clock, which is divided down from the internal 73.728 MHz core clock.
-  **Master/Slave (Bit 11)** - This bit sets whether the output port is a clock master or slave. The default setting is slave; on powerup, Pins BCLK_OUTx and LRCLK_OUTx are set as inputs until this bit is set to 1, at which time they become clock outputs.
-  **BCLK Polarity (Bit 12)** - This bit controls on which edge of the bit clock the output data are clocked: on the falling edge of BCLK_OUTx when this bit is set to 0, and on the rising edge when it's set at 1.
-  **LRCLK Polarity (Bit 13)** - When set to 0, the left-channel data are clocked when LRCLK is low, and the right data clocked when LRCLK is high. When set to 1, this is reversed.
-  **Link TDM Streams (Bit 14, Serial Output Control Register 1)** - When this bit is set to 1, the TDM output streams a linked to output a single 16-channel stream on SDATA_OUT0. When set to 0, TDM data are output on two independent 8-channel streams, on pins SDATA_OUT0 and SDATA_OUT4.
-  **Dither-Enable (Bit 15)** - Setting this bit to 1 enables dither on the appropriate channels.

.. |regpic1.png| image:: https://wiki.analog.com/_media/regpic1.png
.. |regpic2.png| image:: https://wiki.analog.com/_media/regpic2.png
