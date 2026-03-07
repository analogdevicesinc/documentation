Overview
========

This short guide is intended to show how you may set a static IP for network interfaces on Linux or Windows systems. For both examples we're going to be setting the 192.168.1.1 IP address for a specific network interface created by plugging the :doc:`AD-T1LUSB-EBZ </wiki-migration/resources/eval/user-guides/ad-t1lusb-ebz>` converter into an USB port.

Manually setting static IPs is required if the device we're connecting to also configures a static IP for its network interface. Otherwise, our host won't know which interface to use in order to communicate.

Linux
=====

You should plug the AD-T1LUSB-EBZ into an USB port and then open a terminal and run **ip a**. This will give you a list of the network interfaces Linux has created.

::

   ╭─xvr@debian
   ╰$ ip a
   1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
       link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
       inet 127.0.0.1/8 scope host lo
          valid_lft forever preferred_lft forever
       inet6 ::1/128 scope host noprefixroute 
          valid_lft forever preferred_lft forever
   2: enx381428d8dcf4: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
       link/ether 38:14:28:d8:dc:f4 brd ff:ff:ff:ff:ff:ff
       inet 10.48.65.147/24 brd 10.48.65.255 scope global dynamic noprefixroute enx381428d8dcf4
          valid_lft 21392sec preferred_lft 21392sec
       inet6 fe80::3a14:28ff:fed8:dcf4/64 scope link noprefixroute 
          valid_lft forever preferred_lft forever
   4: enx00e04c68045c: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc fq_codel state DOWN group default qlen 1000
       link/ether 00:e0:4c:68:04:5c brd ff:ff:ff:ff:ff:ff
   5: enx00e04c366f06: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
       link/ether 00:e0:4c:36:6f:06 brd ff:ff:ff:ff:ff:ff
   6: wlp0s20f3: <BROADCAST,MULTICAST> mtu 1500 qdisc noqueue state DOWN group default qlen 1000
       link/ether 2a:ee:a2:3b:72:c0 brd ff:ff:ff:ff:ff:ff permaddr 48:51:c5:63:37:60
   3150: ztugavxm3z: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 2800 qdisc fq_codel state UNKNOWN group default qlen 1000
       link/ether 16:af:6e:75:9b:81 brd ff:ff:ff:ff:ff:ff
       inet6 fe80::14af:6eff:fe75:9b81/64 scope link 
          valid_lft forever preferred_lft forever
   3151: ztugatxm3z: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 2800 qdisc fq_codel state UNKNOWN group default qlen 1000
       link/ether 16:af:0e:75:9b:81 brd ff:ff:ff:ff:ff:ff
       inet 192.168.192.30/24 brd 192.168.192.255 scope global ztugatxm3z
          valid_lft forever preferred_lft forever
       inet6 fcbe:2234:666e:c018:e974::1/40 scope global 
          valid_lft forever preferred_lft forever
       inet6 fe80::14af:eff:fe75:9b81/64 scope link 
          valid_lft forever preferred_lft forever
   2727: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
       link/ether 06:d6:97:8c:32:37 brd ff:ff:ff:ff:ff:ff

Next, you'll have to identify the interface which is specific to the AD-T1LUSB-EBZ converter. This may be named differently depending on your Linux distribution and other interfaces you may already have. This can be done by running **ip a** before and after plugging the converter. In out case the interface is eth0.

Now, we may run the following command in order to add an IP address to the interface.

::

   sudo ip addr add 192.168.1.1/24 dev eth0

If you run **ip a** again, you may see the network interface now has the new IP.

::

   2727: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
       link/ether 06:d6:97:8c:32:37 brd ff:ff:ff:ff:ff:ff
       inet 192.168.1.1/24 scope global eth0
          valid_lft forever preferred_lft forever

You may now try to test your connection.

Windows
=======

You should plug the AD-T1LUSB-EBZ into an USB port. Open Control Panel and go to the **Network and Internet** tab.

.. image:: https://wiki.analog.com/_media/resources/no-os/misc_guides/control_panel_first.png
   :alt: control_panel_first.png

Then click on the **Network and Sharing Center**, then **Change adapter settings**.

.. image:: https://wiki.analog.com/_media/resources/no-os/misc_guides/control_panel.png
   :alt: control_panel.png

.. image:: https://wiki.analog.com/_media/resources/no-os/misc_guides/network_sharing_center.png
   :alt: network_sharing_center.png

We can now see all the network interfaces created by Windows, along with their associated network adapter. Right click on the **LAN9500A USB 2.0 to Ethernet 10/100 Adapter** one and then go to **Properties**.

.. image:: https://wiki.analog.com/_media/resources/no-os/misc_guides/network_connections.png
   :alt: network_connections.png

Then, if you double click the **Internet Protocol Version 4 (TCP/IP)** item, the following windows shows up, where we can configure the IP settings. After this is done, click on "OK" a close the Properties window.

.. image:: https://wiki.analog.com/_media/resources/no-os/misc_guides/interface_properties.png
   :alt: interface_properties.png

.. image:: https://wiki.analog.com/_media/resources/no-os/misc_guides/ip_settings.png
   :alt: ip_settings.png
   :width: 369px

You may now try to test your connection.
