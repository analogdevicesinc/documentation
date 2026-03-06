Build Server
============

Setup DHCP VM
-------------

-  Create ubuntu server VM in bridge network mode

Install packages

::

   sudo apt update; sudo apt install tftp-hpa tftpd-hpa

Update TFTP config file /var/lib/tftpboot

::

   TFTP_USERNAME="tftp"
   TFTP_DIRECTORY="/var/lib/tftpboot"
   TFTP_ADDRESS=":69"
   TFTP_OPTIONS="--secure"

Setup Board Manager VM
----------------------
