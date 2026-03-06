Network Configuration
=====================

There are two types of network configuration supported by the Analog Devices Kuiper Linux Distribution:

-  Dynamic Configuration (default)
-  Static Configuration

Updating the networking configuration will require a serial connection (UART), existing network connection, or having a physical keyboard/mouse/monitor connected. In all cases, to find out what your Ethernet port IP address is within ADI Kuiper Linux all you need to do is type the following:

-  Open up a terminal window
-  Type in the following command and hit <Enter> ``ifconfig``
-  Check the inet address of **eth 0** to view the IP address assigned\

|image1|

Dynamic Host Configuration Protocol (DHCP)
------------------------------------------

By default, the Ethernet port of your host platform is configured for DHCP when using the ADI Kuiper Linux Distribution. Typically the Ethernet port is named *eth 0*, but if a platform has multiple Ethernet ports than those ports get enumerated (For example - Port 1 will be named *eth 0* and Port 2 will be named *eth 1*)

Request a New DHCP IP Address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you require a new IP address for some reason (Perhaps your internet isn't working or there are multiple devices using the same address) use the following instructions.

-  Open up a terminal window
-  Type in the following command and hit <Enter> ``sudo dhclient -r eth0``

   -  Password = *analog*

-  Type in the following command and hit <Enter> ``sudo dhclient eth0``

   -  Password = *analog*

-  Type in the following command and hit <Enter> ``ifconfig``
-  Check the inet address of **eth 0** to view the new IP address assigned

Return from Static IP Address Configuration to DCHP IP Address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are returning from a static IP configuration, and require to have a new DHCP IP address assigned to the host platform, follow these steps:

-  Open a terminal window
-  Type in the following command and hit <Enter> ``enable_dhcp.sh``
-  Type in the following command and hit <Enter> ``ifconfig``
-  Check the inet address of **eth 0** to view the new IP address assigned

.. important::

   Some versions of Kuiper have an incompatible configuration script for enabling static addresses. If you receive the error "can't read /etc/NetworkManager/NetworkManager.conf: No such file or directory", you will need to do the following.

   
   -  Use your PC to get the updated script `enable_dhcp.sh <https://raw.githubusercontent.com/analogdevicesinc/linux_image_ADI-scripts/master/enable_dhcp.sh>`__
   -  Copy that script onto your clip board
   -  Using a UART connection to the target device, open up a serial terminal with the correct COM port and set the baud rate to 115200
   -  Type in the user/password which is *analog/analog*
   -  Then type in the following commands:
   
   ::
   
      sudo cat > /usr/local/bin/enable_dhcp.sh
      #!/bin/bash
      #
      # Re-enable the default DHCP-based NetworkManager support. Use to revert the
      # static IP configuration performed by the enable_static_ip.sh script.
      #
      # Example usage:
      # enable_dhcp.sh
      #
      # WARNING: Do not use this script if there is a custom network configuration
      # set up in /etc/network/interfaces as it will be overwritten.
   
      set -e
   
      if [[/${uid}_-ne_0|${uid}_-ne_0]]; then
          echo "This script must be run as root!"
          exit 1
      fi
   
      if grep -qi kuiper "/etc/os-release"; then
          cat <<-EOF > /etc/dhcpcd.conf
              hostname
          EOF
          systemctl daemon-reload
          systemctl restart dhcpcd.service
      else
          echo "Re-enabling DHCP via NetworkManager for all network interfaces"
   
          cat <<-EOF > /etc/network/interfaces
              # interfaces(5) file used by ifup(8) and ifdown(8)
              # Include files from /etc/network/interfaces.d:
              source-directory /etc/network/interfaces.d
          EOF
   
          # enable DHCP via NetworkManager (assumes the config file hasn't been touched much)
          sed -i 's/^managed=true/managed=false/' /etc/NetworkManager/NetworkManager.conf
   
          service network-manager restart
      fi
      #<Then Press "Ctrl + D" to save>
      sudo chmod +x /usr/local/bin/enable_dhcp.sh
   


Setting a Static IP Address Configuration
-----------------------------------------

If you desire to directly connect the Ethernet port of your host platform to the Ethernet port of another host, such as a PC (without the use of a network or router) a static configuration is required.

Kuiper Linux
~~~~~~~~~~~~

In order to change the default settings of ADI Kuiper Linux please use the following steps.

-  Open up a terminal window
-  Type in the following command and hit <Enter> ``enable_static_ip.sh <ip address> eth0`` Where *<ip address>* is a usable and unique value such as **192.168.255.1**
-  Type in the following command and hit <Enter> ``ifconfig``
-  Check the inet address of **eth 0** to make sure that the new IP address has been set properly

.. important::

   Some versions of Kuiper have an incompatible configuration script for enabling static addresses. If you receive the error "can't read /etc/NetworkManager/NetworkManager.conf: No such file or directory", you will need to do the following.

   
   -  Use your PC to get the updated script `enable_static_ip.sh <https://raw.githubusercontent.com/analogdevicesinc/linux_image_ADI-scripts/master/enable_static_ip.sh>`__
   -  Copy that script onto your clip board
   -  Using a UART connection to the target device, open up a serial terminal with the correct COM port and set the baud rate to 115200
   -  Type in the user/password which is *analog/analog*
   -  Then type in the following commands:
   
   ::
   
      sudo cat > /usr/local/bin/enable_static_ip.sh
      #!/bin/bash
      #
      # Enable a static IP for eth0 (or another interface) on Ubuntu-based setups.
      # Note that the wanted IP address should be specified as the first argument;
      # otherwise, it defaults to 192.168.0.101. Also, the interface can be specified
      # as the second argument if the default (eth0) isn't wanted.
      #
      # Example usage:
      # enable_static_ip.sh [10.66.99.101] [eth1]
      #
      # WARNING: Do not use this script if there is a custom network configuration
      # set up in /etc/network/interfaces as it will be overwritten.
   
      set -e
   
      IP_ADDR=${1:-192.168.0.101}
      ETH_DEV=${2:-eth0}
   
      if [[/${uid}_-ne_0|${uid}_-ne_0]]; then
          echo "This script must be run as root!"
          exit 1
      fi
   
      echo "Enabling the static IP address ${IP_ADDR} on ${ETH_DEV}"
   
      if grep -qi kuiper "/etc/os-release"; then
          cat <<-EOF > /etc/dhcpcd.conf
              interface ${ETH_DEV}
              static ip_address=${IP_ADDR}/24
          EOF
          systemctl daemon-reload
          systemctl restart dhcpcd.service
      else
          # disable NetworkManager (assumes the config file hasn't been touched much)
          sed -i 's/^managed=false/managed=true/' /etc/NetworkManager/NetworkManager.conf
   
          # set up loopback and add static IP config for ${ETH_DEV} (defaults to eth0)
          cat <<-EOF > /etc/network/interfaces
              auto lo
              iface lo inet loopback
   
              auto ${ETH_DEV}
              iface ${ETH_DEV} inet static
              address ${IP_ADDR}
              netmask 255.255.255.0
          EOF
   
          service network-manager restart
      fi
      #<Then Press "Ctrl + D" to save>
      sudo chmod +x /usr/local/bin/enable_static_ip.sh
   


Once complete, you will need to change the networking configuration of your PC. I am going to use a Windows 10 PC as an example, but similar procedures can be done with MAC OS and Linux based Machines.

Windows Operating System
~~~~~~~~~~~~~~~~~~~~~~~~

-  Open up Control Panel > Network and Internet > Network and Sharing Center
-  Click on **Change Adaptor Settings**\

|image2|

-  Find the Ethernet Port and right-click and select **Properties**
-  Find the **Internet Protocol Version 4 (IPv4)** and click on **Properties**\

|image3|

-  Select the radio button that says **Use this IP Address**
-  Enter in the IP address you want to use. To connect with the host board above use an address such as the subnet is the same but the final address is different. For example **192.168.255.2**\

|image4|

Now you will be ready to directly connect your ADI Kuiper Linux host directly to your PC using the Ethernet port of both devices.

.. note::

   Remember once you are done to come back into the setting on your PC to change the Ethernet port back to the **Obtain an IP address automatically** radio button. Otherwise anything connected to your PC using the Ethernet port will likely not work.


*End of Document*

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/serial_terminal_linux_ifconfig_inet.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/network_sharing_adaptor.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/ipv4_properties.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/static_ip.png
   :width: 400px
