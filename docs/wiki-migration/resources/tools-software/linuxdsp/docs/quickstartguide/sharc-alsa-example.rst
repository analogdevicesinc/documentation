.. warning::

   These pages are not updated anymore. Documentation has been moved to :git-lnxdsp-adi-meta:`wiki\`


SHARC-ALSA Example
==================

.. note::

   SHARC-ALSA is currently supported only on SC598


.. important::

   For releases **prior** to :doc:`Linux for ADSP-SC5xx Processors 3.0.0 </wiki-migration/resources/tools-software/linuxdsp/releaselandingpages/3.0.0>`, follow :doc:`SHARC-ALSA example (legacy) </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/sharc-alsa-example_legacy>`\


.. note::

   SHARC-ALSA is **not** enabled by default when following the Quickstart guides within :doc:`Linux for ADSP-SC5xx Processors 3.0.0 </wiki-migration/resources/tools-software/linuxdsp/releaselandingpages/3.0.0>`. You need to change the final line in the ``conf/local.conf`` file from ``DISTRO_FEATURES:append = " linux_only_audio"`` to ``DISTRO_FEATURES:append = " adi_sharc_alsa_audio"`` before building the image.


SHARC-ALSA is a framework designed to make a SHARC appear as an audio device in `ALSA <https://alsa-project.org/wiki/Main_Page>`__. It uses `RPMsg <https://www.kernel.org/doc/html/latest/staging/rpmsg.html>`__ for the communication between the ARM Core and the SHARC Core. When playing audio through ALSA the audio samples are transferred to the SHARC where additional processing can take place before the audio is played.

SHARC-ALSA modes
----------------

There are 2 modes for SHARC-ALSA, and they differ in how the SHARCs are programmed. The mode is set in the ``conf/local.conf`` file, when building the Linux image. E.g. : ``DISTRO_FEATURES:append = " adi_sharc_alsa_audio"``

| 
| == adi_sharc_alsa_audio == Audio playback handled through SHARC firmware, no codec control (volume, etc) from Linux. Remoteproc is used to load the SHARC LDR firmware files.

| 
| == adi_sharc_alsa_audio_uboot == Audio playback handled through SHARC firmware, no codec control (volume, etc) from Linux. Remoteproc is *not* used to load the SHARC LDR firmware file.

| 
| ==== Programming the SHARC ====

Using Linux (remoteproc)
~~~~~~~~~~~~~~~~~~~~~~~~

adi_sharc_alsa_audio
^^^^^^^^^^^^^^^^^^^^

An example SHARC image is present in the ``/lib/firmware`` directory on the target. The SHARC can be programmed with this image using the Linux shell. The SHARCs are running already when Linux has booted, so you can stop them, reload the example image or your own one, and start them again

.. code:: bash

   $ cd /lib/firmware

   $ echo stop > /sys/class/remoteproc/remoteproc0/state
   ADI Reset Control Unit 3108b000.rcu: Timeout waiting for remote core 1 to IDLE!
   remoteproc remoteproc0: stopped remote processor core1-rproc

   $ echo icap-sharc-alsa_Core1.ldr  > /sys/class/remoteproc/remoteproc0/firmware

   $ echo start > /sys/class/remoteproc/remoteproc0/state
   remoteproc remoteproc0: powering up core1-rproc
   remoteproc remoteproc0: Booting fw image adi_adsp_core1_fw.ldr, size 132860
   adi_remoteproc 28240000.core1-rproc: Core1 rpmsg init timeout, probably not supported.
   virtio_rpmsg_bus virtio0: rpmsg host is online
    remoteproc0#vdev0buffer: registered virtio0 (type 7)
   remoteproc remoteproc0: remote processor core1-rproc is now up

When executing the ``echo start`` command you will notice the LEDs on the SOMCRR-EZKIT flashing and then settle on LED7 remaining on. This indicates that the image on the SHARC is running.


| 

Using U-Boot
~~~~~~~~~~~~

adi_sharc_alsa_audio_uboot
^^^^^^^^^^^^^^^^^^^^^^^^^^

An example SHARC image is present in the /lib/firmware folder on the target. The SHARC can be programmed with this image via U-Boot. You need to store ``icap-sharc-alsa_Core1.ldr`` & ``icap-sharc-alsa_Core2.ldr`` (or your own image/images) in the TFTP server used throughout the booting process in the :doc:`Linux for ADSP-SC5xx Processors 3.0.0 (develop) </wiki-migration/resources/tools-software/linuxdsp/releaselandingpages/3.0.0>`. With these stored in the TFTP server, you need to input the following at the U-Boot prompt

.. code:: bash

   => rproc init
   => tftp ${loadaddr} icap-sharc-alsa_Core1.ldr  
   => rproc load 0 ${loadaddr} ${filesize}
   Load Remote Processor 0 with data@addr=0x96000000 132860 bytes: Success!
   => tftp ${loadaddr} icap-sharc-alsa_Core2.ldr
   => rproc load 1 ${loadaddr} ${filesize}
   Load Remote Processor 1 with data@addr=0x96000000 79892 bytes: Success!
   => rproc start 1
   => rproc start 0

You can now proceed to booting Linux as per usual. The SHARCs will be programmed and running.

|

| ==== Playing Audio ====

.. note::

   The audio from the SHARC is routed to DAC1/2. Connect a set of speakers to J17 also labelled as DAC1/2.


   |image1|

Play back the audio sample file stored in ``/usr/share/sounds/alsa/``

.. code:: bash

   $ aplay /usr/share/sounds/alsa/2Ch_L440_R200_48kHz_16bit_6s.wav

You will hear a 440Hz tone on the left channel and a 200Hz tone on the right channel being played for 6 seconds.

| 
| === Adding a Tone to a Channel === The SHARC can be instructed to add a tone to the audio played using aplay. This is done through a command interface which also uses RPMsg for passing on the instructions to the SHARC Core. A helper tool for simplifying this is installed on the target. The tool creates a character device which will accept a channel number and a frequency to be added to the audio as strings allowing for simple interaction from the command line.

.. code:: bash

   $ rpmsg-bind-chardev -d virtio0.sharc-audioweaver.-1.201 -a 60

Once the binding has been created a character device /dev/rpmsg0 is available and will accept commands with the syntax <channel> <frequency>. To add a 800Hz tone to channel 0 (Left) enter the following at the command line:

.. code:: bash

   $ echo 0 800.0 > /dev/rpmsg0

Similarly to add a 500Hz tone to channel 1 (Right) enter the following command:

.. code:: bash

   $ echo 1 500.0 > /dev/rpmsg0

When running aplay again you will hear a dual tone frequency on both channels. The left channel will contain 440Hz + 800Hz whereas the right channel will contain 200Hz + 500Hz.

.. code:: bash

   $ aplay /usr/share/sounds/alsa/2Ch_L440_R200_48kHz_16bit_6s.wav

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/quickstartguide/adsp-sc594-som-ezkit-alsa-example.jpg
   :width: 400px
