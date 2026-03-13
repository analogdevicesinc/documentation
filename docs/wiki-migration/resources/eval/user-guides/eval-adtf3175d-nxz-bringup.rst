EVAL-ADTF3175D-NXZ Initial Bring-up
===================================

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/picture3.jpg
   :align: center
   :width: 400

- Download the latest evaluation software package from `here <https://github.com/analogdevicesinc/ToF/releases>`_:
- Install the evaluation software
- At the end of the installation opt to download the micro-SD Card image.

If you missed this step, not go to the image folder to execute the script:
get_image.cmd (Windows) or get_image.sh (Linux).
  - Unzip the downloaded archive to access the SD Card image and firmware
    binary.
    - The micro-SD Card image will be named similarly to the following, microsd-54c2ce9f.zip.
    - The firmware binary will be named similarly to fwUpdate_3.2.2.bin.
- Reflash the micro-SD Card included in your kit (for example microsd-54c2ce9f.zip) - :doc:`SD card flashing guide </wiki-migration/resources/eval/user-guides/eval-adsd3100-nxz/flashing_image_instructions>`
   * Flash firmware (for example fwUpdate_3.2.2.bin) onto module - :doc:`Link </wiki-migration/resources/eval/user-guides/eval-adtf3175d-nxz-upgrade-firmware>`
   * Run GUI as specified in startup guide - :doc:`Link </wiki-migration/resources/eval/user-guides/eval-adsd3100-nxz-gui>`
