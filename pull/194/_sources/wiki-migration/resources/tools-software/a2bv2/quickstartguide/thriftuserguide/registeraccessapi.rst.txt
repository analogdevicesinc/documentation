:doc:`Click here to return to Thrift User Guide Homepage </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide>`

List of API for Register Access for A2B and Peripheral
======================================================

-  :doc:`Peripheral Write/Read (SPI/I2C) </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/registeraccessapi>`
-  :doc:`Add Peripheral XML file and I2C address </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/registeraccessapi>`

| 
| ====Peripheral Write/Read (SPI/I2C)==== This API is used for performing Write/Read operations for both SPI and I2C mode based on selected peripherals and selected A2B network. It takes element Uid and ReadWritePacket info as arguments and returns int value.

| **API:**
| int PeripheralReadWrite(string elementUid, AnalogDevices.SigmaStudio.Scripting.ReadWritePacket rdwrpkt);

| **Arguments:**
| \* “elementUid” = UID of the peripheral

-  “ReadWritePacket” = ReadWritePacket contains below parameters as shown below.

   -  DevAddr – Device Address used for I2C Read/Write

      -  SPICmdWidth – SPI Command Width
      -  SPICmd – SPI Command
      -  AddrWidth – Address width
      -  Addr – Register Address of the Peripheral
      -  DataWidth – Data Width which we are going to write/read.
      -  Data – Data which we are going to write, incase of read no need to specify.
      -  PeriWrite – true for SPI/I2C write operation.

::

                     false for SPI/I2C read operation.

| **Result:**
| It will return packet data. For error case, API will return exception.

| **Csharp Example:**
| 1. Peripheral Write SPI:

::

          ReadWritePacket pkt = new ReadWritePacket();
          pkt.SPICmd = 0;
          pkt.Addr = 0;
          pkt.SPICmdWidth = 0;
          pkt.AddrWidth = 1;
          pkt.DataWidth = 1;
          pkt.Data = 0x6;
          pkt.PeriWrite = true; // Write Enable
          pkt.Data = client.PeripheralReadWrite("GenericDevices_4", pkt);
   2. Peripheral Read SPI:
          ReadWritePacket pkt = new ReadWritePacket();
          pkt.SPICmdWidth = 0;
          pkt.SPICmd = 0;
          pkt.Addr = 0;
          pkt.AddrWidth = 1;
          pkt.DataWidth = 1;
          pkt.PeriWrite = false; // Write Disable
          pkt.Data = client.PeripheralReadWrite("GenericDevices_4", pkt);
   3. Peripheral Write I2C:
          ReadWritePacket pkt1 = new ReadWritePacket(); 
          pkt1.DevAddr = 0x38;
          pkt1.Addr = 0xF798;
          pkt1.AddrWidth = 2;
          pkt1.DataWidth = 2;
          pkt1.Data = 0x08;
          pkt1.PeriWrite = true; // Write Enable
          pkt1.Data = client.PeripheralReadWrite("GenericDevices_0", pkt1);
   4. Peripheral Read I2C:
          ReadWritePacket pkt = new ReadWritePacket();
          pkt.DevAddr = 0x38;
          pkt.Addr = 0xF798;
          pkt.AddrWidth = 2;
          pkt.DataWidth = 2;
          pkt.PeriWrite = false; // Write disable
          pkt.Data = client.PeripheralReadWrite("GenericDevices_0", pkt);

| **Python Example:**
| 1. Peripheral Write SPI:

::

          pkt = ReadWritePacket()
          pkt.SPICmdWidth = 0
          pkt.SPICmd = 0
          pkt.AddrWidth = 2
          pkt.Addr = 0
          pkt.DataWidth = 2
          pkt.Data = 0x6
          pkt.PeriWrite = True
          pkt.Data = client.PeripheralReadWrite("GenericDevices_4", pkt)
   2. Peripheral Read SPI:
          pkt = ReadWritePacket()
          pkt.SPICmdWidth = 0
          pkt.SPICmd = 0
          pkt.AddrWidth = 2
          pkt.Addr = 0
          pkt.DataWidth = 2
          pkt.PeriWrite = False
          pkt.Data = client.PeripheralReadWrite("GenericDevices_4", pkt)
   3. Peripheral Write I2C:
          pkt = ReadWritePacket()
          pkt.DevAddr = 0x38
          pkt.AddrWidth = 2
          pkt.Addr = 0xF798
          pkt.DataWidth = 2
          pkt.Data = 0X08
          pkt.PeriWrite = True
          pkt.Data = client.PeripheralReadWrite("GenericDevices_0", pkt)
   4. Peripheral Read I2C:
          pkt = ReadWritePacket()
          pkt.DevAddr = 0x38
          pkt.AddrWidth = 2
          pkt.Addr = 0xF798
          pkt.DataWidth = 2
          pkt.PeriWrite = False
          pkt.Data = client.PeripheralReadWrite("GenericDevices_0", pkt)

| 
| ====Add Peripheral XML file and I2C address==== This API is used for adding Peripheral . It takes element Uid and property name and property value as arguments and returns SSPResult.

| **API:**
| SSPResult UpdateStringProperty(string elementUid, string propertyName, string propertyVal);

| **Arguments:**
| \* “elementUid” = UID of the A2B Channel

-  “propertyName” = Name of the action property. Some of the property name examples are listed below

   -  PeripheralFile – Peripheral File

      -  I2CAddress– I2C address

-  “PropertyValue” = Value of the property in string.

| **Result:**
| SSPResult contains 'IsSuccess' flag and 'Message' information of UpdateStringProperty action.

-  IsSuccess is set to 'True' if the UpdateStringProperty was successful else 'False'.
-  Message contains the Success/Failure information in the form of list of string.

| **Csharp Example:**
| \_sspresult = client.UpdateStringProperty("GenericDevices_0", "PeripheralFile", @"C:\\Analog Devices\\ADI_A2B_Software-Rel19.4.4\\Schematics\\BF\\A2BSchematics\\xml\\adi_a2b_master_ADAU1761.xml");

::

   _sspresult = client.UpdateStringProperty("GenericDevices_0", "I2CAddress", "0x39");

| **Python Example:**
| ssp_result = client.UpdateStringProperty("GenericDevices_0", "PeripheralFile", "C:\\\\Analog Devices\\\\ADI_A2B_Software-Rel19.4.4\\\\Schematics\\\\BF\\\\A2BSchematics\\\\xml\\\\adi_a2b_master_ADAU1761.xml")

::

   ssp_result = client.UpdateStringProperty("GenericDevices_0", "I2CAddress", "0x39")

.. tip::

   For additional details on Peripheral configuration, you may refer the :doc:`A2B Plugin for SigmaStudio+ User Guide </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/schematics-components>`.

