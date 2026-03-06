`Click here to return to 'SigmaStudio for SHARC Host Controller' page. <https://wiki.analog.com/resources/tools-software/sigmastudio/usingsigmastudio/ss4shhostcontroller>`__

Payload Types
=============

Code
----

| ‘Code’ refers to the compiled binary code of the entire Schematic. SS_CMD_PROGRAM_SSN command indicates that the packet contains code payload. MEM_ADDR field is not used.
| =====Initial Parameter===== ‘Initial Parameter’ refers to the entire parameter set of the Schematic.
| SS_CMD_PARAMETER_NO_SAFE command indicates that the packet contains complete block parameter payload. MEM_ADDR field is not used.
| =====Block Parameter===== Block Parameter’ refers to a block of parameters sent to the SHARC Target as part of Tuning the Schematic. The SS_CMD_PARAMETER_NO_SAFE command indicates that the packet contains block parameter payload. The MEM_ADDR field indicates the offset of the block from the start of the parameter buffer. When the block parameter is received on the SHARC Target, it is immediately copied to the parameter buffer.
| =====Safeload Parameter===== ‘Safeload Parameter’ refers to payload of up to 5 sets of parameter and address combination sent to the SHARC Target as part of Tuning the Schematic. The SS_CMD_PARAMETER_SAFE command indicates that the packet contains safeload parameter payload. MEM_ADDR field is not used. When safeload parameters are received on the SHARC Target, it is not immediately copied to the parameter buffer. Parameters are updated just before the execution of the Schematic code. This ensures that the parameter updates are not performed during the execution of the Algorithm.
| =====Block Safeload Parameter===== ‘Block Safeload Parameter’ refers to a block of parameters sent to the SHARC Target as part of Tuning the Schematic. SS_CMD_BLOCK_SAFE command indicates that the packet contains block safeload parameter payload. MEM_ADDR field indicates the offset of the block from the start of the parameter buffer. When block safeload parameter is received on the SHARC Target, it is not immediately copied to the parameter buffer. Parameters are updated only after ensuring that the SigmaStudio Schematic code is not being executed. If the code is being executed, the update waits until the code execution completes.
