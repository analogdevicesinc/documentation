SHARC-ALSA Example (legacy)
===========================

.. important::

   These instructions refer to releases **prior** to :doc:`Linux for ADSP-SC5xx Processors 3.0.0 (develop) </wiki-migration/resources/tools-software/linuxdsp/releaselandingpages/3.0.0>`\


.. important::

   In order to run the SHARC-ALSA example it is necessary to follow the instructions on :doc:`Yocto Linux Quickstart Guide for ADSP-SC594 </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/quickstart_sc594>` and enable the SHARC-ALSA example as part of the build.


SHARC-ALSA is a framework designed to make a SHARC appear as an audio device in `ALSA <https://alsa-project.org/wiki/Main_Page>`__. It uses `RPMsg <https://www.kernel.org/doc/html/latest/staging/rpmsg.html>`__ for the communication between the ARM Core and the SHARC Core. When playing audio through ALSA the audio samples are transferred to the SHARC where additional processing can take place before the audio is played.

| 
| ==== Programming the SHARC ==== An example SHARC image providing 2-channel playback is present in the /lib/firmware folder on the target. The SHARC can be programmed with this image using the sysfs interface to remoteproc as shown below:

::

   # echo 2Channel-SC594.ldr  > /sys/class/remoteproc/remoteproc0/firmware
   # echo start > /sys/class/remoteproc/remoteproc0/state

When executing the "echo start" command you will notice the LEDs on the SOMCRR-EZKIT flashing and then settle on LED7 remaining on. This indicates that the image on the SHARC is running.

| 
| ==== Playing Audio ====

-  The audio from the SHARC is routed to DAC1/2. Connect a set of speakers to J17 also labelled as DAC1/2.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/quickstartguide/adsp-sc594-som-ezkit-alsa-example.jpg
   :width: 400px

Play back the audio sample file stored in /usr/share/sounds/alsa/

::

   # aplay /usr/share/sounds/alsa/2Ch_L440_R200_48kHz_16bit_6s.wav

You will hear a 440Hz tone on the left channel and a 200Hz tone on the right channel being played for 6 seconds.

| 
| === Adding a Tone to a Channel === The SHARC can be instructed to add a tone to the audio played using aplay. This is done through a command interface which also uses RPMsg for passing on the instructions to the SHARC Core. A helper tool for simplifying this is installed on the target. The tool creates a character device which will accept a channel number and a frequency to be added to the audio as strings allowing for simple interaction from the command line.

::

   # rpmsg-bind-chardev -d virtio0.sharc-audioweaver.-1.201 -a 60

Once the binding has been created a character device /dev/rpmsg0 is available and will accept commands with the syntax <channel> <frequency>. To add a 800Hz tone to channel 0 (Left) enter the following at the command line:

::

   # echo 0 800.0 > /dev/rpmsg0

Similarly to add a 500Hz tone to channel 1 (Right) enter the following command:

::

   # echo 1 500.0 > /dev/rpmsg0

When running aplay again you will hear a dual tone frequency on both channels. Left channel will contain 440Hz + 800Hz whereas the right channel will contain 200Hz + 500Hz.

::

   # aplay /usr/share/sounds/alsa/2Ch_L440_R200_48kHz_16bit_6s.wav
