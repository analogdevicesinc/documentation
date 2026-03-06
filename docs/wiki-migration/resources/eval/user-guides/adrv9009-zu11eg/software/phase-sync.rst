ADRV9009-ZU11EG Phase Synchronization
=====================================

Phase sync ADRV9009 feature
---------------------------

`Sync script <https://github.com/analogdevicesinc/linux_image_ADI-scripts/blob/master/adrv9009_multichip_sync.sh>`__

DMA Gating
----------

Steps:

-  Stop sysref
-  Write to sync bit
-  Check sync bit
-  Configure DMA
-  Generate sysref pulse
-  Pull DMA buffer
