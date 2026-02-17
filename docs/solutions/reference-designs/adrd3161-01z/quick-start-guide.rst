ADRD3161-01Z Quick Start Guide
==============================

Connect a motor and encoder
---------------------------

Connect the motor windings to screw terminal block P3 and a motor position encoder to terminal P16. Consult the :doc:`hardware-guide` for pinouts and wiring diagrams.

Control using TMCL-IDE
----------------------

:adi:`TMCL-IDE <en/resources/evaluation-hardware-and-software/motor-motion-control-software/tmcl-ide.html>`
is the main software package for Trinamic parts. The TMC9660 may be directly interfaced with from TMCL-IDE if connected via UART. The TMC9660 may be controlled via UART and by the MAX32662 at the same time, seamlessly. This usage is helpful for debugging and lower level access to the TMC9660 than the CANopen interface allows.

Prerequisites:

* Install the latest version of :adi:`TMCL-IDE <en/resources/evaluation-hardware-and-software/motor-motion-control-software/tmcl-ide.html>`
* Obtain a suitable UART probe (:adi:`MAX32625PICO` or other MAXDAP compatible)

Steps:

#. Connect a UART probe to header P7.
#. In TMCL-IDE, select the corresponding serial port from the *Connected devices* menu on the left side.
#. Use the following settings to initiate a connection:

   * 115200 baud
   * search IDs from 1 to 1

Initially, use the TMCL-IDE TMC9660 tuning wizard to obtain proper motor control parameters. Carefully go through each step, up to and including encoder configuration.

After you have found suitable motor control parameters, use the "Position/Velocity/Torque mode" tools from the menu to move it.

Control via CAN bus
-------------------

The ADRD3161-01Z implements CANopen, with the CiA 402 profile for motor drives. The device is interoperable with other CANopen devices, but has limited applicability on a CAN bus that is not CANopen, unless carefully configured.

Check that the board has started up correctly:

* The RUN LED (green) should be blinking at 2.5Hz
* The FAULT LED (red) should be off

Set up CAN adapter
''''''''''''''''''

On the software side, CAN communication depends on the OS and used hardware interface. The following guide assumes a **Linux** machine. On Windows, this setup can be achieved in WSL with USB forwarding of CAN adapters.

Install / load the appropriate kernel modules for your CAN adapter:

.. tab-set::

   .. tab-item:: gs_can

      Many off-the-shelf USB-CAN adapters need the ``gs_usb`` driver which is provided by many common Linux distros.

      If the driver is loaded, you should automatically see a ``can0`` network interface being listed when you run ``ip link``.

   .. tab-item:: slcan

      Adapters using the ``slcan`` protocol and driver, such as the :adi:`ADRD4161`, need the slcan daemon to run. On the ADRD4161, run:

      .. code-block:: bash

         sudo slcand -o -c -f -t hw -s 6 -S 2000000 /dev/ttyAMA0 can0

      Other devices will need a different set of arguments to ``slcand``.

Configure and bring up the CAN interface (replace can0 with the name of the interface, if different):

.. shell::

   $ ip link set can0 down
   $ ip link set can0 type can bitrate 500000
   $ ip link set can0 up

Additionally, the ``can-utils`` package has a useful set of tools which aid in bus monitoring and troubleshooting.

If connected to an ADRD3161-01Z board, you should see regular heartbeat messages using `candump`:

.. shell::

   $ candump can0
     can0  717   [1]  7F
     can0  717   [1]  7F
     can0  717   [1]  7F
     ...

In the above snippet, ``717`` is the CAN message ID, and it corresponds to node ID ``0x17``. The following content of each line signifies a message length of 1 bytes and hexadecimal content ``7F``. This is an CANopen NMT heartbeat message signaling the node is in the ``PRE-OPERATIONAL`` state.

To remotely reset all nodes on the bus, run:

.. shell::

   $ cansend can0 000#0081

To remotely reset a specific node, with ID xx, run (after replacing xx with the ID in hexadecimal):

.. shell::

   $ cansend can0 000#xx81

Run a simple Python example
'''''''''''''''''''''''''''

The following example code uses the Python ``canopen`` library to communicate with the ADRD3161-01Z and spin it in velocity mode.

.. code-block:: python3

   import canopen
   import time

   node_address = 0x17 # Change this to your node address

   net = canopen.Network()
   net.connect(channel='can0', interface='socketcan') # Change if using another adapter
   node = canopen.BaseNode402(node_address, 'adrd3161.eds')
   net.add_node(node)

   # Wait for node to say something, or block if there are communication problems
   node.nmt.wait_for_heartbeat()


   # Set up CiA 402 and set mode of operation to Cyclic Synchronous Velocity
   node.load_configuration()
   node.setup_402_state_machine()
   node.state = 'SWITCH ON DISABLED'
   node.sdo['Modes of Operation'] = 9

   time.sleep(1)
   node.nmt.state = 'OPERATIONAL'
   time.sleep(1)

   # Engage motor drive
   node.state = 'OPERATION ENABLED'
   time.sleep(2)

   # Send velocity commands
   RPM = 4000 # Scaling between internal units and real-life units
   node.sdo['Target Velocity'].raw = 10 * RPM
   time.sleep(1)
   node.sdo['Target Velocity'].raw = -20 * RPM
   time.sleep(1)
   node.sdo['Target Velocity'].raw = 30 * RPM
   time.sleep(1)
   node.sdo['Target Velocity'].raw = 0

   # Stop
   node.state = 'SWITCH ON DISABLED'

   node.nmt.state = 'PRE-OPERATIONAL'

