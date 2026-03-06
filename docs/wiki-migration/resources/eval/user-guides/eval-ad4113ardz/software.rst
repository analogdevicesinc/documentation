Software Guide
==============

ACE Software
============

The ACE software is available :adi:`Here. <en/design-center/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html>`

The quick start guide is available on the landing page here :doc:`(Quick Start Guide) </wiki-migration/resources/eval/user-guides/eval-ad4113ardz>` or for the step by step install guide see the below

Install Guide
-------------

The EVAL-AD4113ARDZ evaluation kit includes a link to the software that needs to be installed before using the EVAL-AD4113ARDZ evaluation board.

.. important::

   \ **Warning**: The evaluation software and drivers must be installed before connecting both the evaluation board and the SDP-K1 board to the PC. This ensures that the evaluations system is correctly recognized when it is connected to the PC.


Installing the ACE Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To install the **ACE** software,

-  With the SDP board disconnected from the USB port of the PC, download the ACE evaluation software package to start the ACE evaluation software installation
-  Click on **Download ACE Installer**
-  Run the installer and follow the instructions to complete the software installation process

During the installation process, be sure to select Precision Converter Components when prompted and enable the LibIIO Wrapper to ensure that all necessary software components are installed.

.. tip::

   The LibIIO Wrapper must be installed for ACE to detect the connected hardware. If you need to install the LibIIO Wrapper after ACE has been installed, click the 'Help' button in the main ACE window. In the 'ACE Help' panel that appears expand the 'Application Resources' section, and you will find a link to run a local copy of the LibIIO Wrapper Installer.


.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad4113ardz/libiio.png
   :align: center
   :width: 400px

**Figure X. Select Precision Converter Components during ACE installation**

When the following prompt appears, be sure to select **LibIIO** and **LibIIODrivers** options, then click **Install**.


|image1|

**Figure X. Select LibIIO components during ACE installation**

Evaluation Hardware Setup
~~~~~~~~~~~~~~~~~~~~~~~~~

When the ACE evaluation software installation is complete, take the following steps to set up the SDP-K1 and evaluation board together.

-  Connect the SDP-K1 and evaluation board using the Arduino headers.
-  Connect the power supplies configuration.
-  Connect the USB cable to the SDP-K1.
-  Open the ACE software.

Software Operation
~~~~~~~~~~~~~~~~~~

To start the ACE evaluation software, from the Windows Start menu, click Analog Devices > ACE. The software window opens (See Figure X) until the software recognizes the AD4113 evaluation board. When the software recognizes the board, double-click on the icon in the **Start** view to open the main window seen in Figure XX. Make sure that you already have the AD411x plugin in the plugin manager.

By clicking on the part in the main ACE evaluation software window (See Figure XX), the chip view will be opened (Figure XX).

The chip view shows the block diagram of the AD4113. This tab allows the user to select inputs, set up the ADC, reset the ADC, and view errors present, as well as configure the device for different demonstration modes. Figure XX shows the chip view in detail, and the following sections discuss the different elements on the Chip view of the software window.

CONFIGURATION TAB
~~~~~~~~~~~~~~~~~

The **Configuration tab** shows a block diagram of the AD4113. This tab allows the user to select inputs, set up the ADC, reset the ADC, and view errors present, as well as configure the device.

Functional Block Diagram (1)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  The functional block diagram of the AD4113 (Label 1 in Figure AZ) shows each of the functional blocks within the AD4113. Clicking a functional block on this diagram opens the configuration pop-up window for that block.

Configuration Pop-Up Button (2)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Each block has a pop-up window (Label 2 in Figure XX) which opens a different window to configure the relevant block.

External Parameters (3, 4, 5)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  There are three external parameters that are set by the EVAL-AD4113ARDZ but must be entered into the software: the external reference (Label 3 in Figure XX), AVDD (Label 4 in Figure XX), and AVSS (Label 5 in Figure XX). The external reference on the EVAL-AD4113ARDZ is set to 2.5 V by using an ADR4525. If bypassing the ADR4525 on the board, change the external reference voltage value in the software to ensure correct calculation of results in the Waveform and Histogram tabs in the Waveform Analysis window.

Status Bar (6)
^^^^^^^^^^^^^^

-  The status bar (Label 6 in Figure XX) displays status updates.

Reset (7)
^^^^^^^^^

-  Click **Reset** to perform a software reset of the AD4113. There is no hardware reset pin on the AD4113. To perform a hard reset, remove power from the board. The software reset has the same effect as a hard reset.

Memory Map Button (8)
^^^^^^^^^^^^^^^^^^^^^

-  Opens the Memory Map tab.

Waveform Analysis Button (9)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Opens the Waveform tab.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad4113ardz/ad4113_functional_block_diagram.png
   :align: center

**Figure X. AD4113 Functional Block Diagram**

WAVEFORM TAB
~~~~~~~~~~~~

The **Waveform tab** can display the different waveforms for voltage input, current input and select the channel. The waveform tab graph the conversions gathered and processes the data, calculating the peak-to-peak noise, rms noise, and resolution.

Waveform Graph and Controls (10, 11)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  The data waveform graph (Label 10 in Figure XX) shows each successive sample of the ADC output. Zoom in on the data in the graph using the control toolbar (Label 11 in Figure XX). Change the scales on the graph by typing values into the x-axis and y-axis fields.

Samples (12)
^^^^^^^^^^^^

-  The Samples numeric control (Label 12 in Figure XX) set the number of samples gathered per batch.

Input Range (13)
^^^^^^^^^^^^^^^^

-  Sets the input range of the ADC (Label 13 in Figure XX).

Run (14)
^^^^^^^^

-  Click **Run Once or Run Continuously** (Label 14 in Figure XX) to start gathering ADC results. If **Run Once** is clicked, the ADC returns the number of samples specified by the Samples control. If **Run Continuously**, the ADC continuously returns samples until stopped by the user. Samples specifies the amounts of samples to be shown on the data graph. This control is unrelated to the ADC mode. Results appear in the waveform graph (Label 10 in Figure XX).

Plot Selection (15)
^^^^^^^^^^^^^^^^^^^

-  The plot selection control (Label 15 in Figure XX) selects which inputs display on the data waveform and shows the name of the input next to the on and off controls. These controls only affect the waveform graphs and have no effect on the channel settings in the ADC register map.

Display Units and Axis Controls (16)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Click the Units dropdown box (Label 16 in Figure XX) to select whether the data graph displays in units of voltages/amps or codes. This control is independent for each graph.

Results Pane (17)
^^^^^^^^^^^^^^^^^

-  The **RESULTS** pane (Label 17 in Figure XX) displays parametric values for the selected display format. The bottom of the **RESULTS** pane also has buttons that allow the user to import or export sample data.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad4113ardz/ad4113_waveform_tab.png
   :align: center

**Figure X. AD4113 Waveform Tab**

HISTOGRAM TAB
~~~~~~~~~~~~~

The Histogram tab generates a histogram using the gathered samples and processes the data, calculating the peak-to-peak noise, rms noise, and resolution.

Histogram Graph and Controls (18, 19)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  The data histogram graph (Label 18 in Figure XX) shows the number of times each sample of the ADC output occurs. Zoom in on the data using the control toolbar (Label 19 in Figure XX) in the graph.

Plot Selection (20)
^^^^^^^^^^^^^^^^^^^

-  The plot selection control (Label 20 in Figure XX) selects which inputs display on the data waveform and shows the name of the input next to the on and off controls. These controls only affect the histogram graphs and have no effect on the channel settings in the ADC register map.

Display Units and Axis Controls (21)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Click the Units dropdown box (Label 21 in Figure XX) to select whether the data graph displays in units of voltages/amps or codes. This control is independent for each graph.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad4113ardz/ad4113_histogram_tab.png
   :align: center

**Figure X. Histogram Tab**

Memory Map
~~~~~~~~~~

Register Tree (22)
^^^^^^^^^^^^^^^^^^

-  The register maps nested list (Label 22 in Figure XX) shows the full register map in a tree control. Each register is shown. Clicking the expand button next to each register shows all the bit fields contained within that register.

Register Tree Search (23)
^^^^^^^^^^^^^^^^^^^^^^^^^

-  The register tree search box (Label 23 in Figure XX) allows the user to search the tree for any register or bit field. Enter a value into this field to filter the register tree.

Register and Bit Field Control (24, 25, 26, 27)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  The register and bit field control section (Label 24 in Figure XX) allows the user to change the individual bit of the register selected in the register tree by clicking the bits or by programming the register value directly into the number control field (Label 25 in Figure XX). This control also shows all bit fields for the selected register. Change the values by using a dropdown box (Label 26 in Figure XX) or by selecting or clearing a checkbox (Label 27 in Figure XX).

Documentation (28)
^^^^^^^^^^^^^^^^^^

-  The Bitfield Documentation (Label 28 in Figure X) contains the documentation for the register or the bit field selected. This field can be updated by selecting a register or bit field in the register tree or hovering over the register or bit field in the register tree or register control. This documentation will be displayed by clicking the |image2| button (Label 28 in Figure XX).

Import and Export (29)
^^^^^^^^^^^^^^^^^^^^^^

-  Save and Load (Label 29 in Figure 20) allow the user to save the current register map setting to a file and to load the setting from the same file, respectively.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad4113ardz/ad4113_memory_map.png
   :align: center

**Figure X. Memory Map**

| :doc:`Return to Hardware Guide </wiki-migration/resources/eval/user-guides/eval-ad4113ardz/hardware_guide>`
| :doc:`Return to Homepage </wiki-migration/resources/eval/user-guides/eval-ad4113ardz>`

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad4111ardz/libiio_drivers.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad4111ardz/ad4111_documentation_button.png
   :width: 20px
