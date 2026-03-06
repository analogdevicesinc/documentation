nanoDAC+ Evaluation Board Programmer
====================================

Overview
--------

The nanoDAC+ Evaluation Board Programmer can be used to program the evaluation board ID on a selection of nanoDAC+ evaluation boards for use with legacy evaluation software or :doc:`ACE </wiki-migration/resources/tools-software/ace>` evaluation software. The evaluation kits which this program can be used for are listed below, all other nanoDAC+ evaluation kits are already compatible with both evaluation platforms.

-  :adi:`EVAL-AD5675SDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD5675.html#eb-overview>`
-  :adi:`EVAL-AD5675RSDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD5675.html#eb-overview>`
-  :adi:`EVAL-AD5676SDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD5676.html>`
-  :adi:`EVAL-AD5676RSDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD5676.html>`
-  :adi:`EVAL-AD5686RSDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD5686R.html>`
-  :adi:`EVAL-AD5696RSDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD5696R.html>`

Installing the Software
-----------------------

**ACE or legacy evaluation software must already be installed on the PC before installing the nanoDAC+ Evaluation Board Programmer.**

-  Download the nanoDAC+ Evaluation Board Installer from `here <https://wiki.analog.com/_media/eval/nanodac/nanodacplusprogrammer.zip>`__.
-  Unzip the files and run setup.exe
-  Follow the installation instructions.

Running the Software
--------------------

**There must only be one System Demonstration Platform (SDP) Board Connected to the PC when running the software.**

-  Connect the evaluation board to the SDP as described in the Evaluation Kit User Guide.
-  To run the software, click Start → All Programs → Analog Devices → Nanodac+ Evaluation Board Programmer → Nanodac+ Evaluation Board Programmer.

|image1|

-  Click Continue to continue.
-  If nanoDAC+ evaluation board is not found, the below message will appear. Reset the SDP board and wait for 30 seconds before clicking OK. Click Cancel to exit the software.\

|image2|

-  When the evaluation board is identified by the software, a prompt will appear for the user to select the evaluation software to reprogram the board to.\

|image3|

-  Select the evaluation platform, and confirm in the following window.
-  When programming is complete, it is reported to the user.\

|image4|

-  Click OK to close the application.

Evaluation board is now ready for use with the selected evaluation platform.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/nanodacplus_welcomemessage.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/nanodacplus_boardnotfound.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/nanodacplus_chooseplatform.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/nanodacplus_confirmation.png
   :width: 600px
