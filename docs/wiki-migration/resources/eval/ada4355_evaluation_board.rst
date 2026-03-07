General Description
===================

The ADA4355 evaluation system is used to evaluate the performance of the ADA4355 receive uModule . The system couples the Analog Devices ADA4355 evaluation board to a Xilinx KC705 FPGA evaluation platform. The KC705 provides ample memory, GPIOs and processing power to perform all control and data manipulation functions. All evaluation system control and data processing is easily accomplished via a MATLAB-based, highly intuitive graphical user interface. |image1| *Figure 1. ADA4355 Evaluation System*

Getting Started
===============

Installing the Software
-----------------------

| Install the software before connecting the FMC communication board to the USB port of the PC.
| **When the software is installed the default location will be C:\\Program Files\\Analog Devices\\ADA4355. If you do not have write privileges at this location choose another location where you do have write privileges, typically under “C:\\Users\\<user_name>”**
| \* Start the Windows Operating System and download the software, ADA4355 Evaluation Software, provided below.

-  Launch the evaluation board software installation by clicking the*\* ADA4355.exe*\* file. The software installation window opens as shown in Figure 2. To continue click **Next**. |image2| *Figure 2*.
-   Choose the folder location for installation as shown in figure 3 and click **Next**. If desired a shortcut can be added to the PC desktop.
   **Reminder: The software must be installed in a location where you have write privileges.**\ |image3| *Figure 3*.
-  The evaluation software requires a MATLAB Runtime engine. If the MATLAB Runtime engine is already installed, this step is skipped. Choose the location for the installation of the Runtime engine and click **Next**.
-  Accept the **MathWorks** software license agreement as shown in Figure 4 and click **Next**. The Runtime engine download is about 700MB. Ensure there is sufficient free hard drive space on the PC.\ |image4|\ *Figure 4*.
-  Click Finish to complete the installation.\ |image5| *Figure 5*.
-  Connect and power up the evaluation system as described on the **Powering Up** section.

Hardware
--------

ADA4355 Evaluation System
~~~~~~~~~~~~~~~~~~~~~~~~~

|image6| *Figure 6. ADA4355 Evaluation System*

-  12V FPGA board supply and on/off switch
-  5V ADA4355 evaluation board supply (See figure 7)
-  Optional external photo diode (APD) voltage supply connector (see figure 8)
-  DC2159A communication interface board USB port.
-  ADA4355 receive uModule.

| |image7|
| *Figure 7. Evaluation board 5V connection detail*
| |image8|
| // Figure 8. Optional high-voltage photo detector bias voltage connection detail (Header P5 and Resistor R7)\ *====Powering Up==== The ADA4355 evaluation system requires two power supplies, a 12V supplyfor the FPGA board and a clean, well-regulated, 5V supply (user to provide) for the ADA4355 board. Additionally, a high voltage supply is needed to reverse bias the photo detector. The evaluation system includes an on-board high-voltage bias generator that is fully controlled via the GUI. Alternatively, the user has the option to supply their own photo detector bias voltage through header P5. All connection points are indicated in Figure 6. Detail for the 5V supply connection is also shown in Figure 7 while detail for the optional, user-supplied, high-voltage reverse bias connection (HV) is shown in Figure 8. If supplying your own photo detector reverse bias voltage, the 10Ω resistor R7 (shown in Figure 8) should be removed from the ADA4355 evaluation board prior to making any supply connections. Evaluation system connection instructions are as follows: \* Connect the 12V supply to the FPGA board. \* Connect the included USB cable from the PC to the USB port on the LTC communication interface board. \* Connect the user provided 5V power supply to the ADA4355 evaluation board. See Figure 7 for connection details. \* If using the on-board bias generator (default) then skip this step and leave header P5 unconnected.If providing your own photo detector reverse bias voltage be sure that 10Ω resistor R7 has been removed and apply the desired reverse bias voltage at pin 1 (HV) of header P5. See Figure 8 for R7 location and header P5 connection details. =====Software Operation ===== ====Setup and Measurement Configuration==== \* Start up the software by double clicking the desktop shortcut (if present), or navigate to the directory location chosen during installation, and under the application subfolder, run* **ADA4355.exe**\ *.
  You may also Search in all programs for* **ADA4355.exe** *to launch the software.
  Due to initialization of the MATLAB runtime engine initial start-up after reboot could take up to 2 minutes. \* Once the software starts up the main user panel is shown as in Figure 8. Note the* **Connect to FPGA** *button is red indicating that the software is not yet connected to the evaluation system. Click the* **Connect to FPGA** *button to initiate connection to the system.
  *\ Figure 9.\ *\* Once the FPGA is connected with no issues, the red button will turn green and display FPGA Connected as shown in Figure 10. If any error occurs while using the software, click the Reset FPGA button to reinitialize the FPGA.
  *\ Figure 10.\ *\* The There are two panels. Main Panel and FFT Panel. Main Panel is shown in Figure 11 and controls the following settings\ 
  *\ Figure 11. Main Panel Settings.//

-  **Gain** drop down menu is used to set the gain of the TIA.
-  **LPF** drop down menu is used to set the Analog Low Pass Filter inside the ADA4355.
-  **Current Driver On** radio button is used to enable or disable the laser driver from pulsing the laser.

::

   -** PD Voltage** drop down menu is used to set the Reverse Bias Voltage of the Photo Detector when using the on-board APD bias generator.
   * **DC Current** drop down menu is used to set the DC current through the laser diode. This biases the laser to a threshold level just below the current level where the laser would begin to emit light. The default and recommended level for the included laser diode is 10mA. See Figure 11 and Figure 12.
   * **Pulsed Current** drop down menu is used to set the pulsed current through the laser diode. See Figure 11 and Figure 12.
   * Pulse Width is the width of the optical pulse launched into the fiber. This setting is in steps of 2nS and cannot exceed 20uS.\\{{ :resources:eval:figure12_ada4355.png?400 |}} //Figure 12. DC current and pulsed current definition//\\
   * **Samples** drop down menu specifies the number of samples to be collected for each pulse. The samples collected are referred to as a "Frame" {{ :resources:eval:ada4355_frame.jpg?600 |}}  //Figure 13.//\\
   * **Averages** drop down menu is used to set the number of data frames averaged for the measurement result.

| |image9|\ *Figure 14.*
| \* **Configure & Run** is used to start the measurement any time measurement settings are changed.

-  **Enable** is used to enable a moving average filter on the collected data.
-  **Window Size** sets the number of samples in the moving average filter.
-  **Equivalent BW** is the bandwidth of the moving average filter and is shown for convenience.

Making a Measurment
~~~~~~~~~~~~~~~~~~~

Once the measurement configurations are selected, click the Configure & Run button. A pop-up window is displayed with the remaining time of the measurement. Once the data is collected it is plotted as shown in figure 15. |image10| *Figure 15.*

Moving Average Filter
~~~~~~~~~~~~~~~~~~~~~

Once the measurement is done and the data is plotted, checking the **Enable** radio button, as shown in Figure 16, will apply a moving average filter on the data. Change the Window Size and click the Filter button to update the filter window size (number of samples averaged). |image11| *Figure 16.*

Axes Configuration
~~~~~~~~~~~~~~~~~~

| The Axes Configuration panel is shown in Figure 17. The*\* X-Lower Limit*\* and **X-Upper Limit** set the lower and upper y-axis limits respectively.
| The*\* Y-Lower Limit*\* and **Y-Upper Limit** set the lower and upper y-axis limits respectively.
| When any changes are made in the Axes Configuration panel the **Configure Axes** button is enabled and must be clicked for the changes to take place. |image12| *Figure 17*

Cursors
~~~~~~~

| In the top left corner of the plot the Cursors radio button enables two vertical cursors to appear on the plot.
| When the Cursors radio button is checked the cursors data is displayed underneath the legend as shown in Figure 18. The X and Y location of the cursors is shown as well as the delta X, delta Y, and ratio of the two deltas.
| To slide the cursor click and hold on the intended cursor and move the mouse to the intended location.
| By default, the cursors are tracking the raw data (blue curve). To track the filtered data (orange curve) click anywhere on the filtered data. The filtered data momentarily flashes and the color of the vertical cursor lines changes to match the color of the data trace they are tracking. |image13|
| *Figure 18. Cursor functionality*

FFT Panel
~~~~~~~~~

| Once data is collected FFT Panel tab appears at the top of the main. Click FFT Panel tab, an FFT is run on the data and the FFT result appear. |image14|
| *Figure 19. FFT Panel*
| ====Tool Bar==== The **Tool Bar** is located on the top left corner of the GUI.
| Selecting Zoom-in toggle and clicking on the plot will zoom in and center at the mouse location. Alternatively, click and drag to draw a box around the area to zoom. When the mouse button is released the axes zoom in to the region enclosed by the box. The Zoom-out toggle works in the same manner but zooms out.
| Each mouse click zooms in or out by a factor of 2.
| While Zoom in or Zoom out is enabled right click on the main plot and select Reset to Original View to go back to the original axes limits.
| The Pan toggle (hand) turns on the pan mode for axes in the main plot. The Save toggle (floppy disk) saves the Raw Voltage data sampled by the ADC. |image15|
| *Figure 20. Tool Bar*
| =====For Only Application Board User =====

-  D23 in the FMC Connector, which is labeled as "1P8VA_EN", needs to be driven by more than 1.2V to make the ADA4355 Application board work properly.

Downloads
=========

.. admonition:: Download
   :class: download

   `ada4355_evaluation_board.zip <https://wiki.analog.com/_media/resources/eval/ada4355_evaluation_board.zip>`_\ `ada4355_evaluation_board_schematics.pdf <https://wiki.analog.com/_media/resources/eval/ada4355_evaluation_board_schematics.pdf>`_\ `ada4355_kc705_bitfile.zip <https://wiki.analog.com/_media/resources/eval/ada4355_kc705_bitfile.zip>`_


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/kintexkit_angle-web.gif
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/figure2_ada4355.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/figure_3_ada4355.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/figure_4_ada4355.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/figure_5_ada4355.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/full_system1.jpg
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/figure7_ada4355.png
   :width: 200px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/figure8_ada4355.png
   :width: 200px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/ada4355_averages.jpg
   :width: 600px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/figure14_ada4355.jpg
   :width: 600px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/figure15_ada4355.png
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/figure16_ada4355.jpg
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/figure17_ada4355.jpg
   :width: 600px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/figure18_ada4355.jpg
   :width: 600px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/toolbar_ada4355.png
   :width: 400px
