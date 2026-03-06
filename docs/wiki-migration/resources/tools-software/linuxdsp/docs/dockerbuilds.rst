.. warning::

   These pages are not updated anymore. Documentation has been moved to :git-lnxdsp-adi-meta:`wiki\`


Building ADI Yocto Linux In A Docker Container
==============================================

A Docker image is available that is configured to build Yocto Linux images for the ADSP-SC5xx development boards. The Docker image is based off the Ubuntu 18.04 LTS 64-Bit Image with additional packages installed, and scripts to automate the building of Yocto Linux.

.. warning::

   The Docker image used on this page is not maintained or provided by Analog Devices


The docker build is deployed so the artefacts remain on the host machine after the docker instance has terminated.

Running the Docker Image
------------------------

To run the docker image and build the ADI Yocto Linux artefacts:

::

   % docker run -v `pwd`/docker_artefacts:/linux/build/tmp/deploy/images wintee/adsp-sc5xx-yocto-linux ./buildOnDocker.sh

The output images from the build will be found in the **docker_artefacts** directory on the host PC.

Information Regarding the Docker Image
--------------------------------------

-  `wintee/adsp-sc5xx-yocto-linux <https://hub.docker.com/repository/docker/wintee/adsp-sc5xx-yocto-linux/>`__ Docker Image
-  `sc5xx_yocto_docker Github repository <https://github.com/wintee/sc5xx_yocto_docker>`__ containing original Dockerfile
