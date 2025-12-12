Temperature Controller Application
==================================

This sample application demonstrates a basic Temperature Controller using the :adi:`AD-AD-RPI-T1LPSE-SL-RPIZ` 
board, two :adi:`AD-SWIOT1L-SL` boards, a Raspberry Pi, a fan actuator and a temperature 
sensor. The system reads temperature data and adjusts fan speed (via SWIOT1L output) 
based on configurable thresholds and hysteresis.

Prerequisites
-------------

- Python 3.8 or newer (3.8–3.11 tested with pyadi-iio).  
  Ensure that a compatible version is installed on your system before continuing.  
  Older versions (<3.8) may not work reliably with pyadi-iio.

- Git command-line tools installed.

- Raspberry Pi with :adi:`Kuiper 2` image installed.
  Follow the instructions in the `Kuiper 2 User Guide <https://github.com/analogdevicesinc/adi-kuiper-gen/releases>`_
  to prepare the Raspberry Pi.

- Ensure that the first two **Software Setup** steps described in :ref:`software-setup`
  (*Downloading and Flashing the Micro-SD Card* and *Configuring the Micro-SD Card*)
  are performed **with the Kuiper 2 image**, not with previous Kuiper releases.  
  These steps must be redone after flashing Kuiper 2 to ensure proper compatibility
  before continuing.


Hardware Setup
--------------

.. figure:: temperature_controller_system.png
   :align: center
   :width: 500

   Temperature Controller System

**Equipment Needed**

- 1x :adi:`AD-AD-RPI-T1LPSE-SL-RPIZ` Board
- 2x :adi:`AD-SWIOT1L-SL` Boards
- 1x Raspberry Pi 4 Model B running Kuiper 2
- 1x :adi:`TMP01` Temperature Sensor
- 1x MC002103 DC Axial Fan
- 1x Raspberry Pi USB Type-C Power Supply (5V, 3A)

**Setup Procedure**

1. Connect the :adi:`AD-AD-RPI-T1LPSE-SL-RPIZ` board to the Raspberry Pi via the 40-pin header

2. Connect the two :adi:`AD-SWIOT1L-SL` boards to the :adi:`AD-AD-RPI-T1LPSE-SL-RPIZ` board via the T1L connectors

3. Connect the first :adi:`AD-SWIOT1L-SL` board to the :adi:`TMP01` temperature sensor

   The first SWIOT1L-SL board is used to both power the TMP01 sensor and measure its
   analog output voltage (VPTAT), which encodes the temperature.

   - **Channel 3 (CH3)** is configured as a **Voltage Output** and provides the sensor
     supply voltage. Connect:
     
     - ``CH3 SWIO`` → ``TMP01 V+``  
     - ``CH3 GND`` → ``TMP01 GND``  

   - **Channel 4 (CH4)** is configured as a **Voltage Input** to measure the TMP01
     analog output. Connect:
     
     - ``CH4 SWIO`` → ``TMP01 VOUT``  
     - ``CH4 GND`` → ``TMP01 GND``  

   .. note::
      CH3 provides a regulated 5 V supply to power the TMP01, while CH4 is configured as a
      high-impedance voltage input with a 0–5 V range to measure the TMP01 VOUT signal.  
      Both channels must share the same ground reference with the sensor.


4. Connect the second :adi:`AD-SWIOT1L-SL` board to the fan actuator

   The second SWIOT1L-SL board drives the fan according to the control loop.

   - The fan is powered directly from channel 0, configured as a **Voltage Output**:

     - ``CH0 SWIO`` → ``Fan +``  
     - ``CH0 GND`` → ``Fan −``  

   - Connect the tachometer output to channel 1 to monitor fan speed (optional):

     - ``CH1 SWIO`` → ``Fan Tach Out``  

5. Power the Raspberry Pi with a 5V, 3A USB Type-C power supply.

Software Setup
--------------

Repository Cloning
~~~~~~~~~~~~~~~~~~

1. Clone the repository and checkout the *swiot* branch:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ git clone https://github.com/analogdevicesinc/pyadi-iio.git
      $ cd pyadi-iio
      $ git checkout swiot

2. Install Python dependencies:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ python3 -m venv ./venv
      $ source venv/bin/activate
      $ pip install -e .

Firmware Flashing
~~~~~~~~~~~~~~~~~

Each :adi:`AD-SWIOT1L-SL` must be updated with the provided firmware image.

1. Follow the official update instructions here:
   `Updating the AD-SWIOT1L-SL firmware <https://analogdevicesinc.github.io/documentation/solutions/reference-designs/ad-swiot1l-sl/software-guide/index.html#updating-the-ad-swiot1l-sl-firmware>`_.

2. Repeat the process for **both boards**.

3. Use the firmware images provided in the `pyadi-iio <https://github.com/analogdevicesinc/pyadi-iio/tree/swiot/examples/rpi_t1lpse/host_setup>`_ repository,
   under ``examples/rpi_t1lpse/host_setup/config/firmware``. These images configure the boards with static IP addresses:

   - The first board will have the ``192.168.97.40`` IP address
   - The second board will have the ``192.168.97.41`` IP address

4. After flashing, verify that each board responds to ping:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ ping 192.168.97.40
      $ ping 192.168.97.41

   .. figure:: ad-rpi-t1lpse-sl-rpiz-sample-application-ping.png
      :align: center
      :width: 500

      Ping Results

Network Setup
~~~~~~~~~~~~~

The SWIOT1L boards use static IP addresses. You can configure them in two ways:

- **Manual static IP** — follow the steps on the AD-RPI-T1LPSE-SL main page under :ref:`setting-up-static-ip`.
- **NetworkManager profiles** — use the provided connection profiles and steps below (recommended).

1. From the project folder, navigate to the ``host_setup`` directory.

2. Copy the connection profiles into NetworkManager's system folder:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ sudo cp -v "Wired connection 2" /etc/NetworkManager/system-connections/
      $ sudo cp -v "Wired connection 3" /etc/NetworkManager/system-connections/

   .. figure:: ad-rpi-t1lpse-sl-rpiz-sample-application-network-setup.png
      :align: center
      :width: 500

      Result of copying the NetworkManager profiles

3. Ensure correct permissions:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ sudo chmod 600 /etc/NetworkManager/system-connections/Wired\ connection\ 2
      $ sudo chmod 600 /etc/NetworkManager/system-connections/Wired\ connection\ 3

   .. figure:: ad-rpi-t1lpse-sl-rpiz-sample-application-network-chmod.png
      :align: center
      :width: 500

      Result of changing permissions on the NetworkManager profiles

4. Reload NetworkManager:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ sudo nmcli connection reload

5. Verify the connections are active:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ nmcli connection show

   .. figure:: ad-rpi-t1lpse-sl-rpiz-sample-application-nmcli-conn-show.png
      :align: center
      :width: 500

      Example of active NetworkManager connections

For full host setup details (including the NetworkManager profiles and context), see the README here:
`pyadi-iio host_setup README <https://github.com/analogdevicesinc/pyadi-iio/blob/swiot/examples/rpi_t1lpse/host_setup/README.md>`_.


Application Execution
~~~~~~~~~~~~~~~~~~~~~~

When executed, the demo continuously reads the temperature from the :adi:`TMP01` sensor
and compares it against the configured thresholds. The fan is automatically turned **ON**
once the temperature rises above ``TEMP_ON`` (default 27 °C) and turned **OFF** once the
temperature falls below ``TEMP_OFF`` (default 26 °C). This hysteresis prevents rapid
switching when the temperature hovers around the threshold.

During runtime, the application prints sensor readings and fan state in the console,
and displays two plots:

- **Temperature vs Time** — TMP01 and ADT75 temperature measurements with ON/OFF thresholds.  
- **Fan State vs Time** — graphical representation of when the fan is active.

Run the Temperature Controller example:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ cd examples/rpi_t1lpse
      $ python3 temperature_controller.py

   .. figure:: ad-rpi-t1lpse-sl-rpiz-sample-application-console-output.png
      :align: center
      :width: 500

      Example Console Output of the Temperature Controller Application

   .. figure:: ad-rpi-t1lpse-sl-rpiz-sample-application-plot-output.png
      :align: center
      :width: 500

      Example Plot Result of the Temperature Controller Application

Use Cases
^^^^^^^^^

This demo illustrates how the :adi:`AD-AD-RPI-T1LPSE-SL-RPIZ` platform together with
:adi:`AD-SWIOT1L-SL` boards can be applied in:

- **Thermal management** - automatically controlling fans in enclosures or test setups
- **Process monitoring** - maintaining temperature ranges in small-scale industrial or lab equipment
- **Educational examples** - demonstrating closed-loop control
