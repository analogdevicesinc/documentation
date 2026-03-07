A notable challenge in embedded systems development is to overcome the lack of feedback that such systems typically provide. Many developers resort to blinking LEDs or instrumenting their code with *printf()* in order to determine whether or not their systems are running as expected. **Micrium** provides a unique tool named **µC-Probe** to assist these developers. With this tool, developers can effortlessly read and write the variables on a running embedded system. This section presents the steps required to run the demonstration project for the ADI evaluation board. A description of the **uC-Probe** demonstration interface is provided.

Configure uC-Probe
==================

Launch **uC-Probe** from the **Start -> All Programs -> Micrium -> uC-Probe**.

Select **uC-Probe** options.

-  Click on the **uC-Probe** icon on the top left portion of the screen.
-  Click on the **Options** button to open the dialog box.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/ced1z/ucprobeoptionsbtn.png
   :alt: ucprobeoptionsbtn.png
   :align: center
   :width: 300px

Set target board communication protocol as **JTAG UART**

-  Click on the **Communication** tab icon on the top left portion of the dialog box
-  Select the **JTAG UART** option.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/image067.png
   :alt: image067.png
   :align: center
   :width: 400px

Setup **JTAG UART** communication settings

-  Select the **JTAG-UART** option from the **Communication** tab.
-  Press the **Open File** button to select the JTAG Debug Information file (**.jdi**)
-  Navigate to the **ADIEvalBoard/FPGA** folder and select the ced1z.jdi file. Press Open.
-  Type the value **1** in the the **Device Id** window.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/ced1z/ucprobeoptionsjtag.png
   :alt: ucprobeoptionsjtag.png
   :align: center
   :width: 600px

-  Select **uCProbe_uart(0)** from the **Instance Id** pulldown menu.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/ced1z/ucprobeinstanceid.png
   :alt: ucprobeinstanceid.png
   :align: center
   :width: 400px

-  Press **Apply** and **OK** to exit the options menu. The embedded target has two UARTs. **uC-Probe** will be communicating with the **uCProbe_uart**.
