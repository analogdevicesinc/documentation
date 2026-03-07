FreeRTOS Add-In Examples
========================

The FreeRTOS Add-In has several examples that have been created so that the user can easily get a feel for how FreeRTOS works, and how the Add-In is used to control the configuration parameters through the use of the User Interface.

These examples are shipped separately from the FreeRTOS Add-In for now, with plans to fully integrate the examples with future releases.

--------------

Get the Hardware Ready
----------------------

The Analog Devices FreeRTOS product supports a couple of reference development board from Analog Devices, including ADSP-SC589/ADSP-SC584/ADSP-SC573 EZ-Kit board, BF707 EZ-Kit board and ADZS-21569 EZ-Kit board. Depending on which software development tool you are using, different JTAG debug board are required.

Below is a list of the hardware involved.

\*\* ADI reference board: **\* ADSP-BF707 EZ-kit:** http://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-bf707.html\ **\* ADZS-21569 EZ-kit:** :adi:`en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ADZS-21569-EZKIT`.html\ **\* ADSP-SC589 EZ-kit:** http://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADSP-SC589.html\ **\* ADSP-SC584 EZ-kit:** http://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADSP-SC584.html\ **\* ADSP-SC573 EZ-kit:** http://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/SC573EZKIT.html Jtag debugger: \*\*

-  ICE1000/2000: http://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/emulators.html

\*\* Host PC: \*\*

A mainstream configuration of Windows PC is required. Verify that your PC has these minimum requirements:

-  2 GHz single core processor; 3.3GHz dual core or better recommended
-  4 GB RAM; 8GB or more recommended
-  2 GB available disk space
-  One open USB port

--------------

Get the Source Code Ready
-------------------------

You can get examples for FreeRTOS (with and without the Add-In) from `freertos-examples <https://github.com/analogdevicesinc/freertos-examples>`_

--------------

References & External Links
---------------------------

::

   ; ** Processor Hardware Reference **
   : [[:adi:`en/products/adsp-bf707`.html#product-documentation|ADSP-BF707 Hardware Reference Manual]]
   : [[:adi:`en/products/adsp-21569`.html#product-documentation|ADSP-21569 Hardware Reference Manual]]
   : [[:adi:`en/products/adsp-sc573`.html#product-documentation|ADSP-SC573 Hardware Reference Manual]]
   : [[:adi:`en/products/adsp-sc584`.html#product-documentation|ADSP-SC584 Hardware Reference Manual]]
   : [[:adi:`en/products/adsp-sc589`.html#product-documentation|ADSP-SC589 Hardware Reference Manual]]
   ; ** Evaluation Kits Schematic **
   :[[:adi:`en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-bf707`.html#eb-documentation|ADSP-BF707 EZ-Kit Schematic]]
   :[[:adi:`en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ADZS-21569-EZKIT`.html#eb-documentation|ADSP-21569 EZ-Kit Schematic]]
   :[[:adi:`en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/SC573EZKIT`.html#eb-documentation|ADSP-SC573 EZ-Kit Schematic]]
   :[[:adi:`en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADSP-SC584`.html#eb-documentation|ADSP-SC584 EZ-Kit Schematic]]
   :[[:adi:`en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADSP-SC589`.html#eb-documentation|ADSP-SC589 EZ-Kit Schematic]]
   ; ** FreeRTOS Manual **
   :[[https://www.freertos.org/Documentation/RTOS_book.html|FreeROS Documentation]]
   :[[https://www.freertos.org/a00102.html|FreeRTOS Demo Applications]]
       
