Basic Sample Application
========================

This simple sample application demonstrates how to get started with the :adi:`AD-RPI-T1LPSE-SL` HAT
by creating a basic Blinky demo. It uses two :adi:`EVAL-CN0575-RPIZ` HATs,
an :adi:`AD-RPI-T1LPSE-SL` HAT as a communication interface, and three Raspberry Pi computers.
These are set up in a parent-child configuration, where the :adi:`AD-RPI-T1LPSE-SL` HAT acts as the parent device,
and the two :adi:`EVAL-CN0575-RPIZ` HATs act as child devices.
The application toggles the on-board LED of a :adi:`EVAL-CN0575-RPIZ` HAT when the button is pressed on the
other :adi:`EVAL-CN0575-RPIZ` HAT and vice versa.

Prerequisites
-------------

- Python 3.8 or newer (3.8–3.11 tested with pyadi-iio).  
  Ensure that a compatible version is installed on your system before continuing.  
  Older versions (<3.8) may not work reliably with pyadi-iio.

- Git command-line tools installed.

- Three Raspberry Pi computers with :adi:`Kuiper 2` image installed.
  Follow the instructions in the `Kuiper 2 User Guide <https://github.com/analogdevicesinc/adi-kuiper-gen/releases>`_
  to prepare the Raspberry Pi.

Hardware Setup
--------------

.. figure:: eval-cn0575-rpiz-sample-application-blinky-system.png
   :align: center
   :width: 500

   Hardware Setup for Basic Sample Application

**Equipment Needed**

- 1x :adi:`AD-RPI-T1LPSE-SL` Board

- 2x :adi:`EVAL-CN0575-RPIZ` Boards

- 3x Raspberry Pi 5 computers running Kuiper 2

- 1x USB Type-C Power Supply (15V, 3A)

- 2x T1L Cables

**Setup Procedure**

1. Connect the :adi:`AD-RPI-T1LPSE-SL` board and both :adi:`EVAL-CN0575-RPIZ` boards to Raspberry Pis via the 40-pin header.

2. Connect the power supply to the :adi:`AD-RPI-T1LPSE-SL` HAT using the USB Type-C port.

3. Connect the two Raspberry Pi that are interfaced with the :adi:`EVAL-CN0575-RPIZ` HATs to the :adi:`AD-RPI-T1LPSE-SL` HAT 
   using T1L cables.

5. Power on the Raspberry Pi computers.

Software Setup
--------------

When running commands with *sudo*, you might be prompted to enter the password for the **analog** user.
If you have not changed it, the default password is **analog**.

Repository Cloning
~~~~~~~~~~~~~~~~~~

1. Clone the repository on both Raspberry Pi computers:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ git clone https://github.com/analogdevicesinc/pyadi-iio.git
      $ cd pyadi-iio

2. Install Python dependencies and open a virtual environment:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ python3 -m venv ./venv
      $ source venv/bin/activate
      $ pip install -e .

Applying Overlays
~~~~~~~~~~~~~~~~~

Overlays are required to enable the proper device tree configurations for the HATs.

In order to apply the overlays, open a terminal on each Raspberry Pi and follow these steps:

1. For the parent Raspberry Pi:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ sudo tee -a /boot/firmware/config.txt <<'EOF'
         dtoverlay=rpi-t1lpse-apl
         dtoverlay=rpi-t1lpse-class12
         EOF

2. For each child Raspberry Pi:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ sudo tee -a /boot/firmware/config.txt <<'EOF'
         dtoverlay=rpi-cn0575
         EOF

Reboot the Raspberry Pi computers to apply the changes:

   .. shell::
      :user: analog
      :group: analog:
      :show-user:

      $ sudo reboot

Hostname Setup
~~~~~~~~~~~~~~

Each Raspberry Pi must have a unique hostname to avoid network conflicts.

1. On each Raspberry Pi, open a terminal and enter the following command to edit the hostname file.

   Keep in mind that *<new_hostname>* should be replaced with a unique name for each Raspberry Pi. We used 
   **analog** for the parent Raspberry Pi, **cn0575a** for the first child Raspberry Pi, and **cn0575b** for the second child Raspberry Pi.

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ hostnamectl set-hostname <new_hostname>

Network Setup
~~~~~~~~~~~~~

Each Raspberry Pi must be configured with a static IP address to ensure reliable communication.

For our demo, we will use the following IP addresses:

- The Raspberry Pi with :adi:`AD-RPI-T1LPSE-SL` HAT (parent): **192.168.10.1/25** on **eth1** and **192.168.10.129/25** on **eth2**

- First Raspberry Pi with :adi:`EVAL-CN0575-RPIZ` HAT (first child): **192.168.10.2/25** on **eth1**

- Second Raspberry Pi with :adi:`EVAL-CN0575-RPIZ` HAT (second child): **192.168.10.130/25** on **eth1**

Open the terminal and write the following commands:

1. On the parent Raspberry Pi, with the :adi:`AD-RPI-T1LPSE-SL` HAT:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ sudo nmcli con add type ethernet ifname eth1 con-name t1l-cn0575a \
           ipv4.method manual ipv4.addresses 192.168.10.1/25 \
           connection.autoconnect yes 
      $ sudo nmcli con add type ethernet ifname eth2 con-name t1l-cn0575b \
            ipv4.method manual ipv4.addresses 192.168.10.129/25 \
            connection.autoconnect yes 
      $ sudo nmcli con up t1l-cn0575a
      $ sudo nmcli con up t1l-cn0575b

2. On the first child Raspberry Pi, with the first :adi:`EVAL-CN0575-RPIZ` HAT:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ sudo nmcli con add type ethernet ifname eth1 con-name t1l-master \
         ipv4.method manual ipv4.addresses 192.168.10.2/25 \
         connection.autoconnect yes
      $ sudo nmcli con up t1l-master

3. On the second child Raspberry Pi, with the second :adi:`EVAL-CN0575-RPIZ` HAT:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ sudo nmcli con add type ethernet ifname eth1 con-name t1l-master \
         ipv4.method manual ipv4.addresses 192.168.10.130/25 \
         connection.autoconnect yes
      $ sudo nmcli con up t1l-master

4. Reboot all the Raspberry Pi computers to apply the changes:
   
   .. shell::
      :user: analog
      :group: analog:
      :show-user:

      $ sudo reboot

5. Verify that the new connections are active on each Raspberry Pi:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ nmcli connection show

   .. figure:: eval-cn0575-rpiz-sample-application-nm-nmcli-conn-show.png
      :align: center
      :width: 500

      Example of active NetworkManager connections

Application Execution
~~~~~~~~~~~~~~~~~~~~~

When executed, the demo continously reads the state of the button the :adi:`CN0575` HAT and 
toggles the LED on the other :adi:`CN0575` HAT if pressed and vice versa. The code is run on the 
parent only, which communicates with both child devices using *libiio*.

Run the application the parent Raspberry Pi only, which will handle communication with both child devices.

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ cd examples/cn0575
      $ source venv/bin/activate
      $ python3 cn0591_2x_cn0575_button_blinky.py

   .. figure:: eval-cn0575-rpiz-sample-application-terminal-result.gif
      :align: center
      :width: 500

      Running Basic Sample Application with Button Presses
