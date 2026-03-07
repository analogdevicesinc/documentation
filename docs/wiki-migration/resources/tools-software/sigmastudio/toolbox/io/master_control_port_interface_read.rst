Interface Read(ADAU145x)
========================

:doc:`Click here to return to the Inputs and Outputs Toolbox page. </wiki-migration/resources/tools-software/sigmastudio/toolbox/io>`

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/io/interfaceread.png
   :align: center

The Interface Read module reads the value of the parameter setting during selfboot and puts it to the output pin.This module can be used to start running the sigmaStudio schematic with the same parameters (like volume setting) stored before power off.Interface Read module works in tandem with the Interface Write module.

| Interface Read module will keep giving the parameter read from the EEPROM during self boot as output. When the current parameter is changed during execution, the Interface write module updates the present value in the Interface read block.The Interface read module will always have the current parameter setting.
| NOTE:
| \* Make sure that the interface read and interface write modules that are with each interacting have the same **Interface number paramter**.
| \* The current release has only the I2C features, SPI will be supported in the upcoming releases.
| ====Use Case==== |image1|

The interface read module can be used an input moudule to the UPDown LUT. The Interface read module serves as a starting index to the UPDown LUT. One of the outputs of the UPDown LUT module is given to the Interface write module which will write the same to the EEPROM.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/io/usecaseinterfacereadandwrite.png
