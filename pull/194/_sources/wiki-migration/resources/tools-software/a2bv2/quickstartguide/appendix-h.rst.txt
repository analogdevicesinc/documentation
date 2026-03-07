:doc:`Click here to return to the QSG homepage </wiki-migration/resources/tools-software/a2bv2/quickstartguide>`

APPENDIX : Flashing ADSP-21569 SOM
==================================

The following steps can be followed to flash the ADSP-21569-SOM with an .ldr file. Place the intended .ldr file in C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Relx.y.z\\Target\\LDR

-  Connect the SOM board to the EV-SOM-CRR ez kit.
-  Connect the ICE-1000 JTAG emulator to the SOM.
-  Connect a USB cable between the JTAG emulator and PC.
-  Open the file at C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Relx.y.z\\Target\\Utility\\Flash_LDR.bat with notepad.
-  Replace -driver "./is25lp512m_dpia_21569.dxe" with -driver "./is25lp512m_dpia_2156x.dxe" .
-  Replace -file ./../LDR/SS_App_21569.ldr with -file ./../LDR/<intended LDR file>.ldr .
-  Save this file.
-  Set the bootmode rotary switch on the SOM board to 0.
-  Turn ON the power to the SOM-CRR board.
-  Run the saved .bat file and wait for the execution to complete.
