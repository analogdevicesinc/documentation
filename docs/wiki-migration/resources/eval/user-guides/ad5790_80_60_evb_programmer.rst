AD5790 AD5780 AD5760 Evaluation Board Programmer
================================================

Overview
--------

The 'AD5790 AD5780 AD5760 Evaluation Board Programmer' can be used to program the board ID on the evaluation boards for the AD5790, AD5780, and AD5760 for use with their legacy or :doc:`ACE </wiki-migration/resources/tools-software/ace>` evaluation software. The evaluation kits this program can be used with are listed here.

-  :adi:`EVAL-AD5790SDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad5790.html>`
-  :adi:`EVAL-AD5780SDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad5780.html>`
-  :adi:`EVAL-AD5760SDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad5760.html>`

The AD5791 and AD5781 evaluation kits are already compatible with both evaluation platforms.

Installing the Software
-----------------------

**ACE or the legacy evaluation software must already be installed on the PC before installing the AD5790 AD5780 AD5760 Evaluation Board Programmer.**

-  Download the AD5790 AD5780 AD5760 Evaluation Board Programmer Installer from `here <https://wiki.analog.com/_media/resources/eval/user-guides/ad5790_80_60_evb_prog/ad5790_80_60_evb_programmer_installer.zip>`_.
-  Unzip the files and run 'setup.exe'
-  Follow the installation instructions

Running the Software
--------------------

**There must only be one System Demonstration Platform (SDP) Board Connected to the PC when running the software.**

-  Connect the evaluation board to the SDP as described in the Evaluation Kit User Guide.
-  To run the software, click Start Menu → All Programs → Analog Devices → AD5790 AD5780 AD5760 Evaluation Board Programmer.

|image1|

-  Click 'Continue' to detect connected hardware.
-  If a supported evaluation board is not found, this message will appear. Reset the SDP board and wait for 30 seconds before clicking 'OK'. Click 'Cancel' to exit the software.\

|image2|

-  When the evaluation board is identified by the software, a prompt will appear for the user to select the evaluation software to reprogram the board to. If the evaluation board is currently configured for use with legacy software, then the user must select the actual device on the board before clicking the 'ACE' button for the software to program it with the correct board ID.\

|image3|

-  If the evaluation board is currently configured for use with the ACE software, the only option is 'Legacy' to configure the board ID for use with legacy evaluation software.\

|image4|

-  When programming is complete and successful this is reported to the user.

|image5|

-  Click 'OK' to close the application.

The evaluation board is now ready for use with the selected evaluation platform.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad5790_80_60_evb_prog/intro.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad5790_80_60_evb_prog/board_not_detected.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad5790_80_60_evb_prog/set_id_for_ace_sw.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad5790_80_60_evb_prog/set_id_for_legacy_sw.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad5790_80_60_evb_prog/successful_program.png
   :width: 400px
