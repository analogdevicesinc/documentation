.. _adrd5161-01z software-guide:

ADRD5161-01Z Software Guide
===========================

Hardware Requirements
---------------------

* ADRD5161-01Z board
* MAX32625PICO (or compatible) DAPLINK programmer
* battery pack or connection to USB-C supply (otherwise module is not powered)
* CAN to USB adaptor to connect to the PC, to view data on CAN bus

Software Requirements
---------------------

* MaximSDK
* Zephyr Workspace

Install Tools
--------------

Install MSDK following the
`MSDK User Guide <https://analogdevicesinc.github.io/msdk/USERGUIDE/#download>`_.
On WSL, we recommend installing it as root in ``/MaximSDK``, instead of the
default user home install path.

If you do not have Zephyr SDK already set up, start by creating a Zephyr
workspace, following the
`Zephyr Getting Started <https://docs.zephyrproject.org/latest/develop/getting_started/index.html>`_
tutorial.

Setup Zephyr Workspace
----------------------


.. tab-set::

  .. tab-item:: Create new west workspace

    Set up virtualenv:

    .. shell::

       $ mkdir zephyrproject
       $ cd zephyrproject
       $ python3 -m venv .venv
       $ source .venv/bin/activate

    Set up west workspace:

    .. shell::

       $ pip install west
       $ west init -m https://github.com/analogdevicesinc/adrd5161-fw . # This might take a while - big download
       $ west update # This might take a while - big download
       $ west zephyr-export
       $ west packages pip --install
       $ cd zephyr
       $ west sdk install
       $ cd ..

  .. tab-item:: Use existing west workspace

    You may reuse a pre-existing West workspace. This is especially convenient if working on other boards in the ADRD family.

    .. shell::

       $ cd path/to/west
       $ source .venv/bin/activate
       $ git clone https://github.com/analogdevicesinc/adrd5161-fw
       $ west config manifest.path adrd5161-fw
       $ west update

Enter the workspace and load the python virtual environment:

.. shell::

   $ cd <path to west workspace>
   $ source .venv/bin/activate
   $ cd adrd5161-fw

Build and Flash the Firmware
----------------------------

The ADRD5161-01Z firmware is based on Zephyr. The source code is available at
:git-adrd5161-fw:`releases/latest+`.

The CiA 419 profile prescribes a standard set of CANopen objects and their
function for BMS systems. While hand-crafting compatible CAN messages is
possible, it is recommended to use an implementation of the CANopen and CiA 419
stack that exposes a simpler API, such as the Python ``canopen`` package or the
ROS2 ``ros2_canopen`` package, exemplified in the following sections.

Build the firmware:

.. shell::

   $ west build -p auto app

Flash the firmware (will build if necessary):

.. shell::

   # Replace /MaximSDK/ with the path to MSDK
   $ west flash --openocd-search /MaximSDK/Tools/OpenOCD/scripts/ \
          --openocd /MaximSDK/Tools/OpenOCD/openocd

Control through Python ``canopen``
----------------------------------

Install the python canopen package:

.. code-block:: console

   $ pip install canopen

Before running any examples, make sure the CAN network is properly set up.

.. code-block:: console

   $ ip link set can0 down
   $ ip link set can0 type can bitrate 500000
   $ ip link set can0 up

The code block below is a minimal example of accessing the BMS parameters through Python.

.. code-block:: python

   #!/usr/bin/env python3
   import canopen
   import time
   import sys
   import struct

   # Configuration
   CAN_INTERFACE = 'socketcan'
   CAN_CHANNEL = 'can0'
   CAN_BITRATE = 500000
   NODE_ID = 2


   def setup_network():
       """Initialize CANopen network and node"""
       try:
           # Create network
           network = canopen.Network()

           # Connect to CAN bus
           network.connect(interface=CAN_INTERFACE, channel=CAN_CHANNEL, bitrate=CAN_BITRATE)
           print(f"Connected to {CAN_INTERFACE} on {CAN_CHANNEL} at {CAN_BITRATE} bit/s")

           # Add remote node
           node = canopen.RemoteNode(NODE_ID, object_dictionary=None)
           network.add_node(node)
           print(f"Added node {NODE_ID}")

           return network, node
       except Exception as e:
           print(f"Error setting up network: {e}")
           sys.exit(1)


   def read_sdo_auto(node, index, subindex=0, signed=False):
       """Read a value via SDO and auto-detect size"""
       try:
           data = node.sdo.upload(index, subindex)
           data_len = len(data)

           if data_len == 1:
               fmt = '<b' if signed else '<B'
           elif data_len == 2:
               fmt = '<h' if signed else '<H'
           elif data_len == 4:
               fmt = '<i' if signed else '<I'
           elif data_len == 8:
               fmt = '<q' if signed else '<Q'
           else:
               return None, f"Unsupported data length: {data_len} bytes", data_len

           value = struct.unpack(fmt, data)[0]
           return value, None, data_len
       except Exception as e:
           return None, str(e), 0

   def charger_status_str(status):
       """Convert charger status to string"""

       if status == 0:
           return "?"
       if status == 1:
           return "charging"
       if status == 2:
           return "fault"
       if status == 3:
           return "off"
       if status == 4:
           return "full"
       return None


   def read_od_values(node):
       """Read all Object Dictionary values from the device"""

       print("\n" + "=" * 60)
       print("Reading Object Dictionary Values")
       print("=" * 60)

       # Battery Cell Voltages (0x2060, array of 4)
       print("\n[Battery Cell Voltages - 0x2060]")
       for i in range(4):
           voltage, error = read_sdo_auto(node, 0x2060, i + 1, signed=False)
           if error:
               print(f"  Cell {i + 1}: Error - {error}")
           else:
               print(f"  Cell {i + 1}: {voltage} mV ({voltage / 1000:.3f} V)")

       # Current (0x2071) - signed
       print("\n[Current - 0x2071]")
       current, error, size = read_sdo_auto(node, 0x2071, 0, signed=True)
       if error:
           print(f"  Current: Error - {error}")
       else:
           print(f"  Current: {current} uA ({current / 1000:.3f} mA)")

       # Battery Status (0x6000)
       print("\n[Battery Status - 0x6000]")
       status, error = read_sdo_auto(node, 0x6000, 0, signed=False)
       if error:
           print(f"  Battery Status: Error - {error}")
       else:
           print("Battery status: discharging" if status == 1 else "Battery status: charging")

       # Charger Status (0x6001)
       print("\n[Charger Status - 0x6001]")
       status, error = read_sdo_auto(node, 0x6001, 0, signed=False)
       if error:
           print(f"  Charger Status: Error - {error}")
       else:
           print(f"  Charger Status is {charger_status_str(status)}")

       # Temperature (0x6010) - signed
       print("\n[Temperature - 0x6010]")
       temp, error, size = read_sdo_auto(node, 0x6010, 0, signed=True)
       if error:
           print(f"  Temperature: Error - {error}")
       else:
           print(f"  Temperature: {temp} °C")

       # Ah Returned During Last Charge (0x6052)
       print("\n[Ah Returned During Last Charge - 0x6052]")
       ah, error = read_sdo_auto(node, 0x6052, 0, signed=False)
       if error:
           print(f"  Ah Returned: Error - {error}")
       else:
           print(f"  Ah Returned: {ah} mAh ({ah / 1000:.3f} Ah)")

       # Battery Voltage (0x6060)
       print("\n[Battery Voltage - 0x6060]")
       voltage, error = read_sdo_auto(node, 0x6060, 0, signed=False)
       if error:
           print(f"  Battery Voltage: Error - {error}")
       else:
           print(f"  Battery Voltage: {voltage} mV ({voltage / 1000:.3f} V)")

       # Battery State of Charge (0x6081)
       print("\n[Battery State of Charge - 0x6081]")
       soc, error = read_sdo_auto(node, 0x6081, 0, signed=False)
       if error:
           print(f"  Battery SOC: Error - {error}")
       else:
           print(f"  Battery SOC: {soc}%")

       print("\n" + "=" * 60)


   def main():

       print("ADRD5161-01Z CAN Example \n")
       print("-" * 60)

       # Setup network
       print("Connect to CAN network\n")
       network, node = setup_network()

       try:
           read_od_values(node)
           print("No Errors. System test passed.\n")
       except Exception as e:
           print(f"\nError: {e}")
           import traceback
           traceback.print_exc()
       finally:
           # Cleanup
           print("\nDisconnecting...")
           network.disconnect()
           print("Disconnected")


   if __name__ == "__main__":
       main()

Control through ROS2 (Python ``canopen`` wrapper)
-------------------------------------------------

This section demonstrates how to create a ROS2 node that wraps the Python
``canopen`` library to interface with the ADRD5161-01Z BMS board. This approach
uses the same Python ``canopen`` library from the previous section, but wraps
it in a ROS2 node to publish ``BatteryState`` messages.

.. note::

   This example uses the Python ``canopen`` library directly within a ROS2
   node. For production robotics applications, see the :ref:`adrd5161-01z
   ros2-canopen-todo` section below.

Prerequisites
~~~~~~~~~~~~~

* Ubuntu 22.04 or later
* Docker installed on your PC
* ADRD5161-01Z board connected via CAN-to-USB adapter
* CAN network configured (see Python canopen section above)

Pull the ADI ROS2 Docker Image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADI ROS2 Docker image provides a pre-configured environment with ROS2
Humble and the necessary dependencies.

**Available Images:**

* `astanea/adi_ros2 <https://hub.docker.com/r/astanea/adi_ros2>`__ - Standard
  Ubuntu-based images for x86_64 and ARM64

**Resources:**

* :git-adi_ros2:`ADI ROS2 GitHub Repository </+>`
* :external+adi_ros2:doc:`index`

**Image Tag Format:** ``{ros-distro}-{arch/platform}-{stage}``

* **{ros-distro}**: ROS2 distribution (e.g., ``humble``, ``iron``, ``jazzy``)
* **{arch/platform}**: Target architecture (``amd64``, ``arm64``)
* **{stage}**: Build stage:

  * ``base`` - Basic ROS2 installation + ADI ROS2 packages
  * ``full`` - Base + Navigation2, SLAM Toolbox, CANopen, etc.
  * ``desktop`` - Full + ROS desktop visualization tools (rviz2, rqt, etc.)

For PC development with CAN support, use the ``full`` or ``desktop`` image:

.. code-block:: console

   # For x86_64 PC (recommended for development)
   sudo docker pull astanea/adi_ros2:humble-amd64-desktop

   # For ARM64 device/SBC
   sudo docker pull astanea/adi_ros2:humble-arm64-desktop

Verify the image was downloaded:

.. code-block:: console

   docker images | grep adi_ros2

Create a ROS2 Workspace
~~~~~~~~~~~~~~~~~~~~~~~

Create a workspace directory on your PC:

.. code-block:: console

   mkdir -p ~/adrd5161_ws/src
   cd ~/adrd5161_ws

Create a Custom BMS Node
~~~~~~~~~~~~~~~~~~~~~~~~

Use the ROS2 package creation tool to generate the package structure. This must be run inside the Docker container.

For more details on ROS2 package creation, see the official
`ROS2 Creating Your First Package Tutorial <https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-Your-First-ROS2-Package.html>`__.

.. code-block:: console

   cd ~/adrd5161_ws
   docker run --rm -v $(pwd):/ros2_ws -w /ros2_ws/src astanea/adi_ros2:humble-amd64-desktop \
       ros2 pkg create --build-type ament_python --license Apache-2.0 --node-name bms_node adrd5161_bms_node

This creates a complete package with all necessary files:

.. code-block:: text

   src/adrd5161_bms_node/
   ├── package.xml
   ├── setup.py
   ├── setup.cfg
   ├── resource/
   │   └── adrd5161_bms_node
   ├── adrd5161_bms_node/
   │   ├── __init__.py
   │   └── bms_node.py
   └── test/
       ├── test_copyright.py
       ├── test_flake8.py
       └── test_pep257.py

Now replace the generated ``src/adrd5161_bms_node/adrd5161_bms_node/bms_node.py`` with the BMS node code:

.. code-block:: python

   #!/usr/bin/env python3
   import sys
   import rclpy
   from rclpy.node import Node
   from sensor_msgs.msg import BatteryState
   import canopen
   import struct

   class BMSNode(Node):
       def __init__(self):
           super().__init__('bms_node')

           # Parameters
           self.declare_parameter('can_interface', 'socketcan')
           self.declare_parameter('can_channel', 'can0')
           self.declare_parameter('can_bitrate', 500000)
           self.declare_parameter('node_id', 2)
           self.declare_parameter('publish_rate', 1.0)

           # Get parameters
           can_interface = self.get_parameter('can_interface').value
           can_channel = self.get_parameter('can_channel').value
           can_bitrate = self.get_parameter('can_bitrate').value
           node_id = self.get_parameter('node_id').value
           publish_rate = self.get_parameter('publish_rate').value

           # Initialize CANopen network with error handling
           self.network = canopen.Network()
           self.can_connected = False

           try:
               self.network.connect(interface=can_interface, channel=can_channel, bitrate=can_bitrate)
               self.can_connected = True
           except OSError as e:
               self.get_logger().error(
                   f'Failed to connect to CAN interface {can_channel}: {e}\n'
                   f'Make sure the CAN interface is configured:\n'
                   f'  $ sudo ip link set {can_channel} down\n'
                   f'  $ sudo ip link set {can_channel} type can bitrate {can_bitrate}\n'
                   f'  $ sudo ip link set {can_channel} up'
               )
               raise SystemExit(1)

           self.node = canopen.RemoteNode(node_id, object_dictionary=None)
           self.network.add_node(self.node)

           self.get_logger().info(f'Connected to BMS on {can_channel} at {can_bitrate} bps')

           # Publisher
           self.battery_pub = self.create_publisher(BatteryState, 'battery_state', 10)

           # Timer
           self.timer = self.create_timer(1.0 / publish_rate, self.publish_battery_state)

       def read_sdo(self, index, subindex=0, signed=False):
           """Read SDO value from BMS"""
           try:
               data = self.node.sdo.upload(index, subindex)
               data_len = len(data)

               if data_len == 1:
                   fmt = '<b' if signed else '<B'
               elif data_len == 2:
                   fmt = '<h' if signed else '<H'
               elif data_len == 4:
                   fmt = '<i' if signed else '<I'
               else:
                   return None

               return struct.unpack(fmt, data)[0]
           except canopen.SdoCommunicationError as e:
               self.get_logger().warning(f'SDO communication error reading 0x{index:04X}: {e}')
               return None
           except canopen.SdoAbortedError as e:
               self.get_logger().warning(f'SDO aborted reading 0x{index:04X}: {e}')
               return None
           except Exception as e:
               self.get_logger().warning(f'Failed to read 0x{index:04X}: {e}')
               return None

       def publish_battery_state(self):
           """Read BMS data and publish as BatteryState message"""
           msg = BatteryState()
           msg.header.stamp = self.get_clock().now().to_msg()
           msg.header.frame_id = 'battery'

           # Read voltage (0x6060) in mV
           voltage_mv = self.read_sdo(0x6060, 0, signed=False)
           if voltage_mv is not None:
               msg.voltage = voltage_mv / 1000.0  # Convert to V

           # Read current (0x2071) in uA
           current_ua = self.read_sdo(0x2071, 0, signed=True)
           if current_ua is not None:
               msg.current = current_ua / 1000000.0  # Convert to A

           # Read State of Charge (0x6081) in %
           soc = self.read_sdo(0x6081, 0, signed=False)
           if soc is not None:
               msg.percentage = float(soc) / 100.0

           # Read temperature (0x6010) in °C
           temp = self.read_sdo(0x6010, 0, signed=True)
           if temp is not None:
               msg.temperature = float(temp)

           # Read individual cell voltages
           cell_voltages = []
           for i in range(4):
               cell_mv = self.read_sdo(0x2060, i + 1, signed=False)
               if cell_mv is not None:
                   cell_voltages.append(cell_mv / 1000.0)
           msg.cell_voltage = cell_voltages

           # Publish
           self.battery_pub.publish(msg)
           self.get_logger().info(f'Battery: {msg.voltage:.2f}V, {msg.percentage*100:.1f}%, {msg.temperature}°C')

       def destroy_node(self):
           """Cleanup on shutdown"""
           if self.can_connected:
               self.network.disconnect()
           super().destroy_node()

   def main(args=None):
       rclpy.init(args=args)
       try:
           node = BMSNode()
       except SystemExit:
           rclpy.shutdown()
           sys.exit(1)

       try:
           rclpy.spin(node)
       except KeyboardInterrupt:
           pass
       finally:
           node.destroy_node()
           rclpy.shutdown()

   if __name__ == '__main__':
       main()

Build and Run the Node Inside Docker
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We'll mount the workspace directly into the ADI ROS2 container and use helper scripts.

**Directory structure:**

.. code-block:: text

   ~/adrd5161_ws/
   ├── docker-compose.yaml
   ├── build.sh
   ├── run.sh
   └── src/
       └── adrd5161_bms_node/
           ├── package.xml
           ├── setup.py
           ├── setup.cfg
           ├── resource/
           │   └── adrd5161_bms_node
           ├── adrd5161_bms_node/
           │   ├── __init__.py
           │   └── bms_node.py
           └── test/
               └── ...

Create the ``docker-compose.yaml`` file in ``~/adrd5161_ws/``:

.. code-block:: yaml

   services:
     ros2:
       image: astanea/adi_ros2:humble-amd64-desktop
       working_dir: /ros2_ws
       volumes:
         - ./src:/ros2_ws/src
         - ./build:/ros2_ws/build
         - ./install:/ros2_ws/install
         - ./log:/ros2_ws/log
       network_mode: host
       environment:
         - DEBIAN_FRONTEND=noninteractive
         - PIP_ROOT_USER_ACTION=ignore
       command: /bin/bash

     build:
       extends: ros2
       command: >
         /bin/bash -c "
           apt-get update >/dev/null 2>&1 &&
           apt-get install -y python3-pip >/dev/null 2>&1 &&
           pip install canopen >/dev/null 2>&1 &&
           source /opt/ros/humble/setup.bash &&
           colcon build --symlink-install
         "

     run:
       extends: ros2
       privileged: true
       volumes:
         - ./src:/ros2_ws/src
         - ./build:/ros2_ws/build
         - ./install:/ros2_ws/install
         - ./log:/ros2_ws/log
         - /dev:/dev
       command: >
         /bin/bash -c "
           apt-get update >/dev/null 2>&1 &&
           apt-get install -y python3-pip >/dev/null 2>&1 &&
           pip install canopen >/dev/null 2>&1 &&
           source /opt/ros/humble/setup.bash &&
           source /ros2_ws/install/setup.bash &&
           ros2 run adrd5161_bms_node bms_node
         "

     echo:
       extends: ros2
       command: >
         /bin/bash -c "
           source /opt/ros/humble/setup.bash &&
           ros2 topic echo /battery_state
         "

Optionally, create convenience scripts in ``~/adrd5161_ws/``:

``build.sh``:

.. code-block:: bash

   #!/bin/bash
   docker compose run --rm build

``run.sh``:

.. code-block:: bash

   #!/bin/bash
   docker compose run --rm run

Make the scripts executable:

.. code-block:: console

   chmod +x build.sh run.sh

**Usage:**

1. Pull the ADI ROS2 Docker image (one-time):

   .. code-block:: console

      sudo docker pull astanea/adi_ros2:humble-amd64-desktop

2. Build the workspace:

   .. code-block:: console

      cd ~/adrd5161_ws
      docker compose run --rm build

3. Configure the CAN interface (on the host):

   .. code-block:: console

      sudo ip link set can0 down
      sudo ip link set can0 type can bitrate 500000
      sudo ip link set can0 up

4. Run the BMS node:

   .. code-block:: console

      docker compose run --rm run

5. In another terminal, monitor the battery data:

   .. code-block:: console

      docker compose run --rm echo

**Docker Compose services explained:**

* ``ros2``: Base service configuration with common settings
* ``build``: Installs dependencies and builds the ROS2 workspace
* ``run``: Runs the BMS node with access to CAN devices
* ``echo``: Echoes the ``/battery_state`` topic for monitoring

.. _adrd5161-01z ros2-canopen-todo:

Future: Native ``ros2_canopen`` Integration
-------------------------------------------

.. todo::

   This section will be expanded to use the native
   `ros2_canopen <https://github.com/ros-industrial/ros2_canopen>`__ package instead of
   wrapping Python ``canopen``. The ros2_canopen stack provides a more robust
   integration with ROS2 lifecycle management, standardized CANopen interfaces,
   and better support for multi-device CAN networks.

**ros2_canopen Architecture:**

The ros2_canopen stack consists of:

* **Master Driver**: Manages the CAN bus and coordinates communication
* **Proxy Driver**: Exposes CANopen node data as ROS2 topics and services
* **BMS Node**: Subscribes to proxy driver topics and publishes ``BatteryState`` messages

**How the files connect:**

.. code-block:: text

   ┌─────────────────────────────────────────────────────────────────────────┐
   │  canopen_core (docker compose run canopen)                              │
   │                                                                         │
   │  bus.yml ──────► Configures master + creates proxy driver "bms"         │
   │     │                                                                   │
   │     └── dcf: "adrd5161.eds" ──► Proxy driver uses EDS for CANopen comm  │
   │                                                                         │
   │  Creates ROS2 interfaces:                                               │
   │     /bms/rpdo          (topic)   ◄── PDO data from BMS device           │
   │     /bms/sdo_read      (service) ◄── Read any object via SDO            │
   │     /bms/sdo_write     (service) ◄── Write any object via SDO           │
   └─────────────────────────────────────────────────────────────────────────┘
                              │
                              │ ROS2 topics/services
                              ▼
   ┌─────────────────────────────────────────────────────────────────────────┐
   │  bms_node.py (docker compose run bms)                                   │
   │                                                                         │
   │  canopen_proxy_node = 'bms'  ◄── Must match node name in bus.yml        │
   │                                                                         │
   │  Subscribes to: /bms/rpdo    ◄── Receives COData messages               │
   │  Publishes:     /battery_state                                          │
   └─────────────────────────────────────────────────────────────────────────┘

The key connection is the **node name** ``bms`` defined in ``bus.yml`` under ``nodes:``:

* In ``bus.yml``: ``nodes: bms:`` creates topics/services prefixed with ``/bms/``
* In ``bms_node.py``: ``canopen_proxy_node = 'bms'`` connects to those same topics

The BMS node communicates via ROS2 interfaces created by the canopen_core process, not by reading the EDS or bus.yml files directly.

**Proxy driver interfaces:**

* ``/bms/rpdo`` topic (``COData``) - Received PDO data from BMS
* ``/bms/tpdo`` topic (``COData``) - Transmit PDO data to BMS
* ``/bms/sdo_read`` service (``CORead``) - Read SDO values
* ``/bms/sdo_write`` service (``COWrite``) - Write SDO values

For more information, see the `ros2_canopen documentation <https://ros-industrial.github.io/ros2_canopen/manual/humble/>`__.
