Analog Devices Precision Toolbox Software-Setup
===============================================

This setup guide assumes you already have MATLAB R2021b and :doc:`Libiio </wiki-migration/resources/eval/user-guides/ad-fmcdaq2-ebz/software/linux/applications/libiio>` installed. To be able to install the Precision Toolbox and run the example scripts present within, some dependencies need to be installed first. The entire installation/setup procedure, after MATLAB R2021b has been installed, is described below –

-  Install the Precision Toolbox from Mathworks File Exchange - `125890-analog-devices-inc-precision-toolbox <https://www.mathworks.com/matlabcentral/fileexchange/125890-analog-devices-inc-precision-toolbox>`__
-  Alternatively, download the .mltbx installer file from the :git-PrecisionToolbox:`latest release <releases>` on GitHub. Right click on the file and click install

|image1|

-  When the installation is finished (through either method) the following window should pop up in MATLAB.

|image2|

-  You can keep the ‘Open Documentation’ selected and close the dialog box if you want to consult the documentation. But the setup procedure in this guide should also be sufficient for the purpose of getting started with the toolbox.
-  Go back to the Add-On Manager and open the toolbox folder, as depicted in the image below

|image3|

-  The following should show up. Under ‘Current Folder’ you should be able to see the toolbox contents

|image4|

-  The example scripts present under the 'examples' directory won't work just yet. We need to install some toolbox dependencies. We require MATLAB-libiio bindings. These are automatically installed once we install either of the two other toolboxes listed on :doc:`this page </wiki-migration/resources/tools-software/pcx-toolbox>`. In this setup guide we are going to go with 'Communications Toolbox Support Package for Analog Devices ADALM-Pluto Radio'.
-  Navigate to the ‘Get Add-Ons’ section in the ‘Home’ tab

|image5|

-  Search for ‘Communications Toolbox Support Package for Analog Devices ADALM-Pluto Radio

|image6|

-  As seen in the previous step under the ‘Requires’ section on the right, this support package has certain dependencies of its own. We will need to install them in order to install the toolbox.
-  Run the MATLAB installer again, but this time check only the required toolboxes, and install those

|image7|

-  Now we can install the ‘Communications Toolbox Support Package for Analog Devices ADALM-Pluto Radio’.

|image8|

-  Install the toolbox. In the ‘Installation Complete’ dialog box, select ‘Setup Later’ as that’s not required in order to run the Precision Toolbox scripts.

|image9|

--------------

--------------

This completes the software setup for the Precision Toolbox. Provided the evaluation hardware setup is also completed, the example scripts can be run for any connected and supported part.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/pcxinstall.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/pcxinstallfinished.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/opentoolboxfolder.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/toolboxfoldercontents.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/gotogetaddons.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/communicationssupportpackage.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/mathworksproductinstaller.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/basedependenciesinstalledpart2.png
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/setuplater.png
   :width: 400px
