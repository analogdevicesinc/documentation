Programming EVAL-CN0428-EBZ or EVAL-CN0429-EBZ with Custom Firmware
===================================================================

.. important::

   \ **Important note: This page applies to both** :doc:`EVAL-CN0428-EBZ </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0428>` **and** :doc:`EVAL-CN0429-EBZ </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0429>`\ **. From here on, these will be referred to generically as "Sensor Board". Any differences are called out specifically.**

   
   Some of the example setup images are of EVAL-CN0428-EBZ, but still apply to both projects.


Although the Sensor Board ships programmed with tested firmware out of the box, it is often important to be able to modify the firmware and reprogram the board with new functionality. The following procedure gives some options for how to do this.

Additional Wiki Resources
-------------------------

This guide focuses on programming and debugging the Sensor Board. General information about the Sensor Board can be found at :doc:`EVAL-CN0428-EBZ </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0428>` and :doc:`EVAL-CN0429-EBZ </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0429>`, depending on which Sensor Board is used.

::

   *For additional info on configuring the switches and using the debug connector on the [[:adi:`en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-M355-ARDZ-INT`.html|EVAL-M355-ARDZ-INT]] arduino interposer shield, consult the [[/resources/eval/user-guides/circuits-from-the-lab/aducm355_arduino_interposer|EVAL-M355-ARDZ-INT wiki page]].
   *For additional info about the switches and connectors on the [[:adi:`en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADICUP3029`.html|EVAL-ADICUP3029]], consult the [[/resources/eval/user-guides/eval-adicup3029/hardware/adicup3029|EVAL-ADICUP3029 Base Board Hardware wiki page]].

Programming the Sensor Board Using a Stand-Alone Debugger such as a J-Link
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If a stand-alone debugger is available, it can be plugged into P10 of the :adi:`EVAL-M355-ARDZ-INT <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-M355-ARDZ-INT.html>` directly and none of the below rework is required. This is a good option for both programming and debugging if there is a stand-alone debugger available. The IAR project for the Sensor Board is set up by default for a J-Link/J-Trace debugger. An adapter cable such as the following is typically required to convert the 20-pin connector at the output of the debugger to the 10-pin connector on the :adi:`EVAL-M355-ARDZ-INT <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-M355-ARDZ-INT.html>`. This cable is not included and can be found from distributors.

https://www.segger.com/products/debug-probes/j-link/accessories/adapters/9-pin-cortex-m-adapter/

If using this option, most of the remainder of this page is not needed. When plugging in the debugger to the :adi:`EVAL-M355-ARDZ-INT <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-M355-ARDZ-INT.html>`, make sure the pins of the cable and the on-board connector are correctly aligned and that pin 1 of the cable matches pin 1 on the :adi:`EVAL-M355-ARDZ-INT <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-M355-ARDZ-INT.html>` board. Some more info is available on the :doc:`EVAL-M355-ARDZ-INT wiki page </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/aducm355_arduino_interposer>`. The items in the `Software <https://wiki.analog.com/>`__ section still apply, including installing IAR and running the ADuCM355 Installer. After that, the project can be opened from the .eww workspace file in the source code and the project can be edited and the boards can be programmed and debugged from within IAR.

Programming the Sensor Board Using the ADICUP3029 On-Board Debugger
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Alternately, if a stand-alone debugger is not available, the on-board debugger on the :adi:`EVAL-ADICUP3029 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADICUP3029.html>` can be used to program both the :adi:`EVAL-ADICUP3029 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADICUP3029.html>` AND the Sensor Board separately. This does not require any extra equipment beyond what is included with the boards in the CN0428/CN0429 package, but it requires 3 traces to be cut on the :adi:`EVAL-ADICUP3029 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADICUP3029.html>`. Once this is done, the SWD connections from the output of the debugger are disconnected from the ADuCM3029, but these SWD connections are available at connector P12.

After this rework is done, it is simple to program or debug ADuCM3029 by connecting P12 to P14, or to program or debug the ADuCM355 on a Sensor Board by connecting P12 on the :adi:`EVAL-ADICUP3029 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADICUP3029.html>` to the P10 on the :adi:`EVAL-M355-ARDZ-INT <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-M355-ARDZ-INT.html>`.

USB power and communications are not affected by these reworks, only the SWD signals are affected.

Board Modifications for Using the on-board Debugger for Programming the Sensor Board
------------------------------------------------------------------------------------

In order to make the debugger available to either the ADuCM3029 or the ADuCM355, the SWD signals must be cut so they are not connected directly to the ADuCM3029 SWD pins. This requires 3 traces to be cut with an X-Acto or similar hobby knife or utility knife. 2 of the SWD traces to be cut are on the primary side and 1 trace is on the secondary side.

.. note::

   Use caution when reworking boards. Protective eyewear should be worn and knife safety should be observed carefully. ESD straps are recommended.


The traces are cut after the P12 connector on the debugger side of the :adi:`EVAL-ADICUP3029 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADICUP3029.html>` so that the SWD signals are available at P12 and the ribbon cable that is included with :adi:`EVAL-M355-ARDZ-INT <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-M355-ARDZ-INT.html>` can be used to connect those signals to the device to be programmed or debugged.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/on_board_debug_traces_to_cut_primaryside.png
   :alt: Traces to cut on ADICUP3029 Primary (top) side
   :align: center

As shown in this magnification, the upper trace is SWD_CLK_3029 and the lower trace is 3029_RESET. These traces should both be cut completely. Both signals still go to P12, this just removes them from P14. |Magnification showing signal names of the traces on the primary side of the board|


|image1|

The trace that needs to be cut on the secondary side of the board is SWD_DIO_3029. This is the outside trace of the 3 that cross the island from the debugger board to the main :adi:`EVAL-ADICUP3029 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADICUP3029.html>` board on the secondary side, but it is simpler to cut the trace in the location indicated to avoid accidentally cutting one of the other traces.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/on_board_debug_traces_to_cut_secondaryside.png
   :alt: Trace to cut on ADICUP3029 Secondary (bottom) side (note: top view, see real image)
   :align: center

This magnified version of the 3 traces that cross the island shows that the other two traces that cross the island are MBED_TX (shown bottom in picture) and MBED_RX (shown middle in picture). These two lower traces must not be cut or USB communication to the board would no longer work. |Traces that cross the island on secondary side. ONLY CUT THE TOP-MOST TRACE.|


|image2|

Now, in order to program the Sensor Board, connect the 10-pin ribbon cable (included with the EVAL-M355-ARDZ-INT package) from P12 on the :adi:`EVAL-ADICUP3029 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADICUP3029.html>` to P10 on the :adi:`EVAL-M355-ARDZ-INT <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-M355-ARDZ-INT.html>`

-  **Make sure the pin 1 of the cable (red) matches the pin 1 on the connector (printed on silk screen) of both boards as shown below.**
-  Set S1 on :adi:`EVAL-M355-ARDZ-INT <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-M355-ARDZ-INT.html>` to the appropriate channel of the board to be programmed. (Note here: multiple boards can be plugged in during programming, only the board selected by S1 will be programmed).

|Ribbon Cable Connection to EVAL-M355-ARDZ-INT| *Image showing ribbon cable connection and installed EVAL-CN0428-EBZ, ready for programming. The other side of the ribbon cable is still connected to P12 on the* :adi:`EVAL-ADICUP3029 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADICUP3029.html>` *as was shown above.*

Once the modifications are in place and the cable is connected between P12 on the :adi:`EVAL-ADICUP3029 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADICUP3029.html>` and P10 on :adi:`EVAL-M355-ARDZ-INT <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-M355-ARDZ-INT.html>`, there are two main options how to program the ADuCM355 on the Sensor Board.

.. important::

   **Before Proceeding:**

   
   Both programming options require the following conditions to be met:
   
   -  IAR Embedded Workbench for ARM (version 8.30.2 or above) has been installed and set up.
   -  The ADuCM355 installer has been run to install the project source code and drivers locally.
   
   If either of the above conditions are not met, go to the `Software <https://wiki.analog.com/>`__ section to set up the software first.


Option 1: mbed Programming (simplest programming method)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   *From within IAR, go into project > options and make sure that the project is setup to generate a .hex file output when you build it.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/iar_settings_mbed_hex_file.png
   :align: center

::

   *Based on the default project options, the .hex file is found in the iar/debug/exe/ folder of the project. Find the .hex file in that folder and drag it onto the DAPLINK: drive. 
   *The drive disappears momentarily and then reappears. The board has been programmed as long as there is no "fail.txt" in the DAPLINK: drive.

Option 2: IAR programming/debugging (allows debugging)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   *In the menu bar, go into project > options, then in the general options tab, click on the file box next to Device and set the device to 'AnalogDevices ADuCM3029'

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/iar_settings_mbed_m355_cup3029_device.png
   :align: center

::

   *In Linker > Config, check the box to override the default file
   * **Caution: CN0428 and CN0429 use a different linker file** 
     * For CN0428 (water quality) choose 'ADuCM355.icf' (shown in the image)
     * For CN0429 (gas sensing), choose the custom linker file, which is distributed together with the M355 software. By default, it is located at: 'C:\Analog Devices\ADuCM355V2.1.0.54\examples\M355_CN0429\iar\ADuCM355_64kSRAM.icf'    (or current version number)
       * //Note: This custom linker file enables use of 64k of SRAM for diagnostics (pulse test)//

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/iar_settings_mbed_m355_cup3029_linker.png
   :align: center

::

   *In Debugger > Setup > Driver, choose CMSIS DAP
     *In the Device description file box, Override default and choose 'ioADUCM355.ddf'

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/iar_settings_mbed_m355_cup3029_debugger.png
   :align: center

::

   *In Debugger > Download, check the box to Override default .board file and choose 'FlashADUCM355.board'

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/iar_settings_mbed_m355_cup3029_flash_loader.png
   :align: center

::

   *Click OK. Then click Download and Debug.

::

   *You may get a message like this. Just click OK and click OK on the next window also.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/iar_settings_mbed_m355_cup3029_cspy_alert.png
   :align: center

**Note: After Programming, the cable must stay connected to P12 on the** :adi:`EVAL-ADICUP3029 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADICUP3029.html>` **and either P14 on the ADICUP3029 or P10 on the** :adi:`EVAL-M355-ARDZ-INT <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-M355-ARDZ-INT.html>` **even during normal operation.**

::

   *If the cable is disconnected, the COM port will not appear and there will be a MAINTENANCE: drive instead of the DAPLINK: drive.
     *This is because the debugger expects the SWD_RESET signal to be pulled high when it is plugged in. If SWD_RESET is held low during power up, it enters maintenance mode.

SOFTWARE
~~~~~~~~

Downloading and Setting up IAR
------------------------------

-   Install IAR Embedded Workbench for ARM

   -  Please visit https://www.iar.com/ to download IAR Embedded Workbench for ARM (version 8.32 or above)

-   License Installation

   -   Once downloaded, the IAR window pops up as shown below. To activate the IAR workbench, click on the help tab.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/help.jpg
   :align: center

-  Then select the License Manager option. This will open a tab asking the user to register for a license key.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/register_for_license_iar.jpg
   :align: center

-  When the user clicks on register, they are redirected to IAR website wherein they need to fill out their details to get access to a license number. After filling in the details, the user will receive a license number which has to be entered back in the tab above then hit Next. This completes the IAR setup and the user can validate their IAR license by looking at this window that pops up in the License Manager option now.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/license_window.jpg
   :align: center

-  The user can load the CN0428 or CN0429 project as-desired in IAR by opening the .eww workspace file in the iar subfolder of the source code.

   -  Note: this source code is downloaded by the ADuCM355 installer (see below).

-  The project code can now be modified and the Sensor Board can be programmed or debugged according to one of the programming options above.
-  Further details of using IAR can be found :doc:`here </wiki-migration/resources/eval/user-guides/ev-cog-ad3029lz/tools/iar_guide>`.

Downloading and Running the ADuCM355 Installer
----------------------------------------------

::

   *The Installer can be found at ftp://ftp.analog.com/pub/MicroConverter/ADuCM355 
   *Download the latest version, extract the .zip archive, and open the .exe.
   *The necessary example projects, drivers, and files will be installed.

.. |Magnification showing signal names of the traces on the primary side of the board| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/on_board_debug_traces_to_cut_primaryside_magnified.png
.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/primary_board_cut_mbed_with_p12.jpg
   :width: 600px
.. |Traces that cross the island on secondary side. ONLY CUT THE TOP-MOST TRACE.| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/on_board_debug_traces_to_cut_secondaryside_magnified.png
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/secondary_board_cut_mbed.jpg
   :width: 600px
.. |Ribbon Cable Connection to EVAL-M355-ARDZ-INT| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/mbed_ribbon_cable_to_shield_connection.jpg
   :width: 600px
