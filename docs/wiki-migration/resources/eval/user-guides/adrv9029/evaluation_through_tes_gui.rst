EVALUATING ADRV9029 DPD
=======================

The DPD tab on the :adi:`ADRV9029 TES GUI <en/license/licensing-agreement/adrv9029-software-license-agreement.html>` is the primary evaluation tool for the DPD feature. In addition, the DPD application programming interface (API) and dynamic link library (DLL) may be used to interact and control the DPD via Python or C#. The ADRV9029 GUI supports an IronPython tab that can be used for scripting purposes.

-  Connect all the hardware equipment as shown in the :doc:`Pre-Requisites page </wiki-migration/resources/eval/user-guides/adrv9029/prerequisites>`. Keep the PA turned off until programming of ADRV9029 is complete. This is to ensure that large amplitude tones generated during initialization of the ADRV9029 device doesn't damage the Power Amplifier.
-  Program the device by selecting Usecase = 51_nonLinkSharing in the Overview Tab of the ADRV9029 TES GUI, turn on the power amplifier and verify that the Transmitter is functioning correctly as described in the :adi:`ADRV902x unboxing video <en/products/adrv9029.html#product-reference>`. A couple of things to note before programming the device

   -  Ensure that the LO frequency matches the operating frequency range of the Power Amplifier in the Initialization Window of the ADRV9029 TES GUI as shown in the figure below. Set the Observation Receivers(ORx) to use the same LO as transmitters(ObsRxLO = TxLO).
      Also, ensure the Tx to ORx mapping selection is correct. Typically, a one to one Tx-ORx mapping is used as shown in the figure below.

::

      {{ :resources:eval:user-guides:adrv9029:adrv9029_initializationwindow.png?600 |}} 
      
   * Ensure that the Observation Receiver is not saturating by adjusting the ORx gain in the ORx tab shown below. In this example, the PA output is observed via ORx1 and the ORx gain index is set to 232, which provides an attenuation of 11.5 dB on the ORx front end. A gain index of 255 provides 0dB attenuation and decrementing the gain index by 1 increases the attenuation by 0.5dB.
       
       {{ :resources:eval:user-guides:adrv9029:adrv9029_orx_setup.png?400 |}} 
      
   * Bring the Power Amplifier to it's rated power by adjusting the ADRV9029 Tx Front End attenuation on the transmit tab highlighted in the figure below.
       
       {{ :resources:eval:user-guides:adrv9029:adrv9029_txattenadjust.png?400 |}} 
       
   * Browse to the DFE Tab in the ADRV9029 GUI. Load a DPD model by clicking the "Load Model from file" button in the "DPD Model Setup" UI. The DPD model is a polynomial function that models the PA through memory terms(i,j) and polynomial degree 'k'. ADI provides a set of pre-calculated DPD models that can be accessed in the "Resources" folder of the ADRV9029 TES GUI Installation directory. After loading the DPD model, set the linear term coefficient corresponding to (i=1,j=1,k=0) to 1 + j0 as shown in the figure below. For evaluation purposes, any model can be chosen. To optimize the DPD model for a particular PA, follow the instructions on the DPD Model Optimization page.
         
         {{ :resources:eval:user-guides:adrv9029:adrv9029_dpd_modelload.png?800 |}} 
       
   * Configure ‘DPD Tracking Config’ parameters (default values provide a good starting point).
         
         {{ :resources:eval:user-guides:adrv9029:adrv9029_dpdtrackingconfig.png?400 |}} 
         
   * In the DPD functions window, select desired Tx channel to apply settings(In this example Tx1 is selected).   
     * Apply DPD model on the M and C tables using ‘Apply Model on Device from M Table’ and ‘Apply Model on Device from C Table’ buttons. The C-Table is a low power model only applicable in DPD Mode 2.
       * Apply DPD tracking configuration by clicking on ‘Apply Tracking Config’ button.
       * Run Path Delay initial calibration using ‘Run Path Delay Init Cal’ button.
       * Click ‘Enable DPD on selected channels (only)’ to enable DPD Tracking.
            
           {{ :resources:eval:user-guides:adrv9029:adrv9029_dpdtrackingcal_enable.png?400 |}} 

-  Now the DPD tracking must be enabled and running. The DPD status can be monitored by selecting the Tx channel and clicking the "Get DPD Status and Statistics" button. Ensure that the error status returns "No Error" and the "Iteration Count" and "Update Count" fields are incrementing

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9029/adrv9029_dpdstatus.png
   :align: center
   :width: 300px

.. image:: https://wiki.analog.com/_media/navigation ADRV9029 DPD USER GUIDE#prerequisites
   :alt: Getting Started#resources:eval:user-guides:adrv9029|main page#dpd_error_troubleshooting|DPD error troubleshooting
