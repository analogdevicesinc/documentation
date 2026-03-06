ADRV9009-ZU11EG Phase Synchronization
=====================================

Phase sync ADRV9009 feature
---------------------------

:git-linux_image_ADI-scripts:`Sync script <adrv9009_multichip_sync.sh>`

DMA Gating
----------

Steps:

-  Stop sysref
-  Write to sync bit
-  Check sync bit
-  Configure DMA
-  Generate sysref pulse
-  Pull DMA buffer
