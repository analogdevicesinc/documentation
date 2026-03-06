Workflow for the ADI ToF Evaluation Kits
========================================

ADTF3175D Eval-Kit
------------------

4.x.x
~~~~~

-  Update the ADTF3175D Eval Kit.

   -  Download the latest software version. See the ADI ToF GitHub page :git-ToF:`releases`.
   -  Checklist for updates:

      -  Install the downloaded package. During installation, download the latest image file.
      -  Update the SD card image.
      -  Update the firmware.

-  Visualization of ToF in real-time aka using the GUI

   -  Go to the **bin** folder on the installed package.
   -  Run **ADIToFGUI**.

      -  Note: The GUI is called **ADIToFGUI**, but is sometimes called the Viewer.

-  Collecting data with data_collect.

   -  Use data collect to stream frames from the ADTF3175D Eval Kit.
   -  Use tofi_compute_depth to extract AB, Depth and Confidence frames from the raw frames.
   -  Use the Python tools
