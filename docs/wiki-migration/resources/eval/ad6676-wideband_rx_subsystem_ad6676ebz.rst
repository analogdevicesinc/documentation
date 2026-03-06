AD6676 : Design Tools and Startup Guide for the AD6676 evaluation board, a high dynamic range, Wideband Receiver
================================================================================================================

Summary
-------

This wiki site includes information about the :adi:`ad6676` and the associated evaluation board, the :adi:`AD6676EBZ </en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD6676.html#eb-overview>`.

The :adi:`ad6676` datasheet provides a significant amount of information to aid in understanding the :adi:`ad6676` capabilities and can assist in the evaluation process. The datasheet along with the user guide and other board files provided here should be consulted when using the evaluation board.

The AD6676 is compatible with the :adi:`HSC-ADC-EVALEZ </en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-HSC-ADC-EVALEZ.html#eb-overview>`, the ADI FPGA-Based Data Capture Kit.

The software required to use the AD6676EBZ with the :adi:`HSC-ADC-EVALEZ </en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-HSC-ADC-EVALEZ.html#eb-overview>` capture board can be downloaded at the following Analog Devices ftp site:

`AD6676 Evaluation Software <https://wiki.analog.com/ftp/ftp.analog.com/pub/hsc_adc_apps/ad6676_demo_package>`__

For additional information or questions, send an email to highspeed.converters@analog.com. The user guide describes the AD6676 evaluation board, :adi:`AD6676EBZ </en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD6676.html#eb-overview>`, which provides all of the support circuitry required to operate the part in various modes and configurations. The application software used to interface with the devices is also described.

| 
| ===== Features =====

-  Full featured evaluation board with FMC connector for the :adi:`AD6676`, a Wideband IF Receiver Subsystem
-  High Instantaneous dynamic range

   -  IIP up to 36 dBm,

      -  NSD as low as -159 dBFS/Hz,

         -  Noise Figure as low as 13 dB
         -  Spurious tones < -97 dBFS

-  On chip digital Signal Processing including

   -  NCO and quadrature digital downconverter

      -  Decimation

         -  AGC Configuration

-  SPI interface for setup and control
-  JESD204B single or dual lane outputs
-  On-board LDO regulator powered through the FMC interface
-  MATLAB (R) User Interface provides complete AD6676 configuration based on user entries

| 
| ===== Helpful Links =====

-  :adi:`AD6676` data sheet
-  High Speed ADC Capture Evaluation Kit Rev E (:adi:`HSC-ADC-EVALEZ </en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-HSC-ADC-EVALEZ.html#eb-overview>`)
-  :adi:`AN-835 Application Note <an-835>`, *Understanding ADC Testing and Evaluation*
-  :adi:`AN-877 Application Note <an-877>`, *Interfacing to High Speed ADCs via SPI*
-  :adi:`VRMS / dBm / dBu / dBV Calculator <en/design-center/advanced-selection-and-design-tools/interactive-design-tools/dbconvert.html>`
-  :adi:`ADI RF Impedance Matching Tool <en/design-center/interactive-design-tools/rf-impedance-matching-calculator.html>`
-  `ADIsimRF Software <https://form.analog.com/form_pages/rfcomms/adisimrf.aspx>`__
-  :adi:`ADI RF/IF Transceiver Products Web page <en/rfif-components/rfif-transceivers/products/index.html>`
-  :doc:`AD6676 Wideband IF Receiver Subsystem Linux device driver </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad6676>`

| 

AD6676 Evaluation Platform User Guides
--------------------------------------

| User Guide for the AD6676 `ad6676_evb_rev1_quickstartguide_2015_03_27.pdf <https://wiki.analog.com/_media/resources/eval/user-guides/ad6676_evb_rev1_quickstartguide_2015_03_27.pdf>`__ (UPDATED March 2015)

|

| ===== AD6676 Evaluation Board Files ===== AD6676 Evaluation Board Schematic Board 13029 Rev D `SCHEMATIC [PDF File <https://wiki.analog.com/_media/resources/eval/user-guides/13039d_sch.pdf>`__]
| AD6676 Evaluation Board Gerber Files Board 13029 Rev D `GERBERS [Zip File <https://wiki.analog.com/_media/resources/eval/user-guides/13039d_gerber.zip>`__]
| AD6676 Evaluation Board BOM File Board 13029 Rev D `Bill of Material [XLS file <https://wiki.analog.com/_media/resources/eval/user-guides/13039d_bom.xls>`__]
| ===== AD6676 Software Files ===== AD6676 DemoTool Software Installation Files : `AD6676 Evaluation Software <https://wiki.analog.com/ftp/ftp.analog.com/pub/hsc_adc_apps/ad6676_demo_package>`__

| 
| ===== AD6676 Evaluation Board HDL Libraries and Project ===== The link below is to an external website which has a project with HDL code that can be used with some FPGA development board to interface to the AD6676
| `AD6676EVB HDL project documentation <https://analogdevicesinc.github.io/hdl/projects/ad6676evb/index.html>`__
| :git-hdl:`External Link to github.com AD6676 library <library/axi_ad6676>`
| :git-hdl:`External Link to github.com AD6676EVB project <projects/ad6676evb>`
| `External Link to general ADI github.com website <https://github.com/analogdevicesinc>`__

| 

AD6676 Ibis Model Files
-----------------------

| AD6676 Ibis Model `AD6676 Ibis [ZIP file <https://wiki.analog.com/_media/resources/eval/user-guides/ad6676_ibis.zip>`__]
| ===== AD6676 Ibis AMI Model Files ===== AD6676 Ibis AMI Model Email highspeed.converters@analog.com to request

AD6676 Matlab R2013a Simulink Model Files
-----------------------------------------

| AD6676 Simulink Model Package `AD6676 Simulink Model <https://wiki.analog.com/ftp/ftp.analog.com/pub/hsc_adc_apps/ad6676_matlab_simulink_model>`__
| AD6676 Simulink User's Guide // `AD6676 Simulink User's Guide [pdf file <https://wiki.analog.com/_media/resources/eval/user-guides/AD6676 Simulink User's Guide.pdf>`__]
