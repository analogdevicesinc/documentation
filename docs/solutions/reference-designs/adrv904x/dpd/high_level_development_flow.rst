High Level DPD Development Flow
===============================

A typical development flow for DPD development with the ADRV904x Integrated DPD
transceiver is shown below

.. image:: ../images/adrv904x_dpd_highleveldevflow.jpg
   :align: center
   :width: 400

1. **PA Selection:** The DPD development with the ADRV904x transceiver starts with PA selection for the radio's frequency of operation. ADI works closely with PA vendors to evaluate the ADI DPD with the latest and greatest PAs from the vendors. Contact ADI for evaluation reports for a specific PA of interest with ADI DPD.

2. **ADI DPD Evaluation:** Customer ADI DPD evaluation with the ADRV904x eval platform and the PA EVB follows the PA selection. This step is strongly recommended to ensure that the DPD system meets design specifications before moving the design to a custom platform. ADI provides a no. of resources to aid your evaluation including the :adi:`ADRV904x Evaluation GUI <en/lp/001/radioverse-adrv9026/software-license-agreement.html>`, :ez:`ADRV904x System Development User Guide <cfs-file/__key/communityserver-wikis-components-files/00-00-00-06-91/ADRV904x_5F00_System_5F00_Development_5F00_User_5F00_Guide_5F00_v0p9_5F00_Preliminary_5F00_EZ.pdf>` and the :ez:`DFE Wizard <rf/wide-band-rf-transceivers/design-support-adrv904x/w/documents/32553/dpd-tool>` to help configure and analyze your DPD system. Users can also ask questions and engage with ADI through the :ez:`Engineer Zone <rf/wide-band-rf-transceivers/design-support-adrv904x>`.

3. **ADI DPD Integration with Custom Radio:** This step involves bring up and tuning of ADI-DPD with custom radio. Some considerations could include optimizing DPD model and settings to account for design variation between evaluation setup and the custom radio platform to ensure that the radio is still meeting specifications from step 2.

4. **Mass Production of Custom Radios with ADI DPD:** At this stage, the user can enable ADI DPD robustness features to ensure that DPD is stable in faulty conditions and dynamic traffic that a radio could encounter in a real world deployment.
