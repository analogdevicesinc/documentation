ADXL345/6 Android Acceleration Sensor
=====================================

Using the ADXL345/6 under Android as Acceleration Sensor

.. image:: https://wiki.analog.com/_media/software/driver/android/adxl_sensor_list.png

The ADXL345/6 can be easily used as Android Acceleration Sensor. A few steps are necessary to add appropriate sensor support.

Add Linux Driver Support:
-------------------------

Starting with linux-2.6.36 the ADXL34x driver is mainlined. If you are using an pre linux-2.6.36 kernel get the source from our repositories and add them to your kernel tree.

Example platform data:

.. code:: c

   #include <linux/input/adxl34x.h>
   static const struct adxl34x_platform_data adxl34x_info = {
       .x_axis_offset = 0,
       .y_axis_offset = 0,
       .z_axis_offset = 0,
       .tap_threshold = 0x31,
       .tap_duration = 0x10,
       .tap_latency = 0x60,
       .tap_window = 0xF0,
       .tap_axis_control = 0,
       .act_axis_control = 0xFF,
       .activity_threshold = 5,
       .inactivity_threshold = 3,
       .inactivity_time = 4,
       .free_fall_threshold = 0x7,
       .free_fall_time = 0x20,
       .data_rate = 0x8,
       .data_range = ADXL_FULL_RES,

       .ev_type = EV_ABS,
       .ev_code_x = ABS_X,     /* EV_REL */
       .ev_code_y = ABS_Y,     /* EV_REL */
       .ev_code_z = ABS_Z,     /* EV_REL */

       .ev_code_tap = {BTN_0, BTN_1, BTN_2}, /* EV_KEY x,y,z */

   /*  .ev_code_ff = KEY_F,*/      /* EV_KEY */
   /*  .ev_code_act_inactivity = KEY_A,*/  /* EV_KEY */
       .power_mode = ADXL_AUTO_SLEEP | ADXL_LINK,
       .fifo_mode = ADXL_FIFO_STREAM,
       .orientation_enable = 0, /* Disable Orientation Reports */
       .deadzone_angle = ADXL_DEADZONE_ANGLE_10p8,
       .divisor_length =  ADXL_LP_FILTER_DIVISOR_16,
       /* EV_KEY {+Z, +Y, +X, -X, -Y, -Z} */
       .ev_codes_orient_3d = {BTN_Z, BTN_Y, BTN_X, BTN_A, BTN_B, BTN_C},
   };

Create an Android sensor library
--------------------------------

The readme file in libhardware states: The source code for the "board" variant, usually lives under partners/... The source code for "default" and "arch" would usually live under hardware/modules/.

The sensor file is typically source code for the "board" variant. However for simplicity this example puts it into a common folder structure under libhardware/modules/.

-  Create an sensors folder under libhardware/modules

-  Copy files sensors_adxl34x.c and Android.mk to libhardware/modules/sensors

--------------

| **The files can be downloaded here:**
| `android_hardware.zip <https://wiki.analog.com/_media/resources/tools-software/android-drivers/sensor-acceleration/android_hardware.zip>`__

--------------

-  Make sure the makefile in the higher folder hierarchy picks up the one in libhardware/modules/sensors.

-  Add following lines to: libhardware/Android.mk

::

   include $(addsuffix /Android.mk, $(addprefix $(LOCAL_PATH)/, \
               modules/sensors \
           ))

In your platforms init.rc file make sure all ADXL34x drivers sysfs files {disable, rate} are owned by system:system

-  Add following lines to your init.rc script:

::

       chown system system /sys/class/input/event0/device/device/disable
       chown system system /sys/class/input/event0/device/device/rate

.. tip::

   In case the ADXL345/6 is not always event0 you can alternatively approach via /sys/bus/i2c/devices/...


-  Rebuilt your Android tree

.. tip::

   Upon start the Android log file (use logcat) should include following lines:

   
   ::
   
      I/SystemServer( 1862): Sensor Service
      [--snip--]
      D/SensorManager( 2064): found sensor: Analog Devices ADXL345/6 3-axis Accelerometer, handle=0
   


Hints
-----

Sample Rate
~~~~~~~~~~~

The ADXL345/6 sample rate is configurable. The maximum sample rate is by default limited to 200Hz, to change this limit modify define ADXL_MAX_SAMPLE_RATE_VAL in the sensor file.

.. warning::

   Very high sample rates > 400Hz can freeze your system!


.. code:: c

   static int control_set_delay(struct sensors_control_context_t *dev, int32_t ms)
   {
       int rate_val;
       int32_t us = ms * MSEC_TO_USEC;

       /*
        * The ADXL34x Supports 16 sample rates ranging from 3200Hz-0.098Hz
        * Calculate best fit and limit to max 200Hz (rate_val 11)
        */

       for (rate_val = 0; rate_val < 16; rate_val++)
           if (us  >= ((10000 * MSEC_TO_USEC) >> rate_val))
               break;

       if (rate_val > ADXL_MAX_SAMPLE_RATE_VAL) {
           rate_val = ADXL_MAX_SAMPLE_RATE_VAL;
           LOGD("Control set delay %d ms requetsed, limiting to rate %d [%d mHz]\n",
                ms, rate_val, (3200000 >> (15 - rate_val)));
       } else {
           LOGD("Control set delay %d ms requetsed, using rate %d [%d mHz]\n",
                ms, rate_val, (3200000 >> (15 - rate_val)));
       }
       return write_int("rate", rate_val);
   }

Platform data configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Don't use BTN_TOUCH
^^^^^^^^^^^^^^^^^^^

In case you experience strange input device gui interaction it might be the case that Android EventHub included the ADXL34x as input device. This is typically the case if you put an BTN_TOUCH key into your ADXL34x drivers platform data.

Upon start EventHub must emit classes=0x0:

::

   I/EventHub( 1862): New device: path=/dev/input/event0 name=ADXL34x 
   accelerometer id=0x10003 (of 0x4) index=4 fd=50 classes=0x0

classes=0x4 means that the ADXL34x driver is considered as Touchscreen.

Auto Sleep
^^^^^^^^^^

The default platform configuration sets the driver automatically switch to sleep mode during periods of inactivity. To disable this feature remove ADXL_AUTO_SLEEP from power_mode.

Alternatively during runtime:

::

   #echo 0 > /sys/class/input/event0/device/device/autosleep

For more information visit the :doc:`ADXL34x driver page </wiki-migration/resources/tools-software/linux-drivers/input-misc/adxl345>`

The Sources
~~~~~~~~~~~

Android.mk
^^^^^^^^^^

.. code:: c

   # Copyright (C) 2008 The Android Open Source Project
   #
   # Licensed under the Apache License, Version 2.0 (the "License");
   # you may not use this file except in compliance with the License.
   # You may obtain a copy of the License at
   #
   #      http://www.apache.org/licenses/LICENSE-2.0
   #
   # Unless required by applicable law or agreed to in writing, software
   # distributed under the License is distributed on an "AS IS" BASIS,
   # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   # See the License for the specific language governing permissions and
   # limitations under the License.


   LOCAL_PATH := $(call my-dir)

   include $(CLEAR_VARS)
   LOCAL_PRELINK_MODULE := false
   LOCAL_MODULE_PATH := $(TARGET_OUT_SHARED_LIBRARIES)/hw
   LOCAL_SHARED_LIBRARIES := liblog libcutils
   LOCAL_SRC_FILES := sensors_adxl34x.c
   LOCAL_MODULE := sensors.default
   include $(BUILD_SHARED_LIBRARY)

sensors_adxl34x.c
^^^^^^^^^^^^^^^^^

.. code:: c

   /*
     * Copyright (C) 2010 Analog Devices Inc.
     * Copyright (C) 2008 The Android Open Source Project
    *
     * Licensed under the Apache License, Version 2.0 (the "License");
     * you may not use this file except in compliance with the License.
     * You may obtain a copy of the License at
    *
     *      http://www.apache.org/licenses/LICENSE-2.0
    *
     * Unless required by applicable law or agreed to in writing, software
     * distributed under the License is distributed on an "AS IS" BASIS,
     * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     * See the License for the specific language governing permissions and
     * limitations under the License.
    */

   #define LOG_TAG "sensors"
   #define SENSORS_SERVICE_NAME "sensors"
   #define ACCEL_SENSOR_NAME "ADXL34x accelerometer"

   #include <stdint.h>
   #include <string.h>
   #include <unistd.h>
   #include <errno.h>
   #include <fcntl.h>
   #include <stdlib.h>
   #include <stdio.h>
   #include <pthread.h>
   #include <dirent.h>
   #include <sys/poll.h>
   #include <sys/ioctl.h>
   #include <sys/types.h>
   #include <linux/input.h>

   #include <cutils/sockets.h>
   #include <cutils/properties.h>
   #include <cutils/atomic.h>
   #include <cutils/log.h>
   #include <cutils/native_handle.h>

   #include <hardware/sensors.h>

   /******************************************************************************/
   #define ID_BASE SENSORS_HANDLE_BASE
   #define ID_ACCELERATION (ID_BASE + 0)
   #define MAX_NUM_SENSORS 1
   /*
     * This driver assumes the ADXL345/6 set in 13-bit full resolution mode +/-16g.
    */

   #define LSG                     (256.0f)    /* 3.9 mg resolution */
   #define CONVERT                 (GRAVITY_EARTH / LSG)
   #define CONVERT_X               CONVERT
   #define CONVERT_Y               CONVERT
   #define CONVERT_Z               CONVERT

   #define SENSORS_ACCELERATION    (1 << ID_ACCELERATION)
   #define ID_A            (0)
   #define INPUT_DIR               "/dev/input"
   #define SUPPORTED_SENSORS       (SENSORS_ACCELERATION)
   #define EVENT_MASK_ACCEL_ALL    ((1 << ABS_X) | (1 << ABS_Y) | (1 << ABS_Z))
   #define DEFAULT_THRESHOLD 100

   #define ACCELERATION_X      (1 << ABS_X)
   #define ACCELERATION_Y      (1 << ABS_Y)
   #define ACCELERATION_Z      (1 << ABS_Z)
   #define SENSORS_ACCELERATION_ALL (ACCELERATION_X | ACCELERATION_Y | \
           ACCELERATION_Z)
   #define SEC_TO_NSEC         1000000000LL
   #define USEC_TO_NSEC        1000
   #define MSEC_TO_USEC        1000

   #define ADXL_MAX_SAMPLE_RATE_VAL    11 /* 200 Hz */

   struct sensors_control_context_t {
       struct sensors_control_device_t device;
       int sensor_fd;
       uint32_t active_sensors;
   };

   struct sensors_data_context_t {
       struct sensors_data_device_t device;
       int event_fd;
       sensors_data_t sensors[MAX_NUM_SENSORS];
   };

   static char input_name[20];
   static char devname[PATH_MAX];

   static int open_sensors_phy(struct sensors_control_device_t *dev, int keep_open)
   {
       char *filename;
       int fd;
       int res;
       uint8_t bits[4];
       DIR *dir;
       struct dirent *de;
       char name[80];

       dir = opendir(INPUT_DIR);
       if (dir == NULL)
           return -1;

       strcpy(devname, INPUT_DIR);
       filename = devname + strlen(devname);
       *filename++ = '/';

       while ((de = readdir(dir))) {
           if (de->d_name[0] == '.' &&
               (de->d_name[1] == '\0' ||
                (de->d_name[1] == '.' && de->d_name[2] == '\0')))
               continue;
           strcpy(filename, de->d_name);
           fd = open(devname, O_RDONLY);
           if (fd < 0) {
               LOGE("Couldn't open %s, error = %d", devname, fd);
               continue;
           }
           res = ioctl(fd, EVIOCGBIT(EV_ABS, 4), bits);
           if (res <= 0 || bits[0] != EVENT_MASK_ACCEL_ALL) {
               close(fd);
               continue;
           }

           if (ioctl(fd, EVIOCGNAME(sizeof(name) - 1), &name) < 1) {
               name[0] = '\0';
           }

           if (!strcmp(name, ACCEL_SENSOR_NAME)) {
               strcpy(input_name, &devname[5]);
               LOGD("using %s (name=%s)", devname, name);
           } else {
               close(fd);
               continue;
           }
           closedir(dir);
           if (keep_open) {
               return fd;
           } else {
               close(fd);
               return 0;
           }
       }
       closedir(dir);

       return -1;
   }

   static int write_int(char const *item, int value)
   {
       int fd;
       static int already_warned = 0;
       char path[80];

       if (input_name[0] == 0)
           open_sensors_phy(NULL, 0);

       sprintf(path, "/sys/class/%s/device/device/%s", input_name, item);

       fd = open(path, O_RDWR);
       if (fd >= 0) {
           char buffer[20];
           int bytes = sprintf(buffer, "%d\n", value);
           int amt = write(fd, buffer, bytes);
           close(fd);
           return amt == -1 ? -errno : 0;
       } else {
           if (already_warned == 0) {
               LOGE("write_int failed to open %s\n", path);
               already_warned = 1;
           }
           return -errno;
       }
   }

   /*
     * the following is the list of all supported sensors
    */
   static const struct sensor_t device_sensor_list[] = {
       {
        .name = "Analog Devices ADXL345/6 3-axis Accelerometer",
        .vendor = "ADI",
        .version = 1,
        .handle = ID_ACCELERATION,
        .type = SENSOR_TYPE_ACCELEROMETER,
        .maxRange = (GRAVITY_EARTH * 16.0f),
        .resolution = (GRAVITY_EARTH * 16.0f) / 4096.0f,
        .power = 0.145f,
        .reserved = {},
        },
   };

   static int sensors_get_list(struct sensors_module_t *module,
                    struct sensor_t const **list)
   {
       *list = device_sensor_list;
       return sizeof(device_sensor_list) / sizeof(device_sensor_list[0]);
   }

   /** Close the sensors device */
   static int sensors__common_close(struct hw_device_t *dev)
   {
       struct sensors_data_context_t *device_data =
           (struct sensors_data_context_t *)dev;

       if (device_data) {
           if (device_data->event_fd > 0)
               close(device_data->event_fd);

           free(device_data);
       }
       return 0;
   }

   static native_handle_t* control_open_data_source(struct sensors_control_device_t *dev)
   {
       native_handle_t* handle;
       int fd = open_sensors_phy(dev, 1);
       if (fd < 0) {
           return NULL;
       }

       handle = native_handle_create(1, 0);
       handle->data[0] = fd;

       return handle;
   }

   static int control_activate(struct sensors_control_context_t *dev,
                   int handle, int enabled)
   {
       uint32_t mask = (1 << handle);
       uint32_t sensors;
       uint32_t new_sensors, active, changed;
       int value;

       sensors = enabled ? mask : 0;
       active = dev->active_sensors;
       new_sensors = (active & ~mask) | (sensors & mask);
       changed = active ^ new_sensors;
       if (!changed)
           return 0;

       dev->active_sensors = new_sensors;

       if (enabled) {
           LOGD("Activate sensor\n");
           value = 0;
       } else {
           LOGD("Deactivate sensor\n");
           value = 1;
       }

       return write_int("disable", value);
   }

   static int control_set_delay(struct sensors_control_context_t *dev, int32_t ms)
   {
       int rate_val;
       int32_t us = ms * MSEC_TO_USEC;

       /*
        * The ADXL34x Supports 16 sample rates ranging from 3200Hz-0.098Hz
        * Calculate best fit and limit to max 200Hz (rate_val 11)
        */

       for (rate_val = 0; rate_val < 16; rate_val++)
           if (us  >= ((10000 * MSEC_TO_USEC) >> rate_val))
               break;

       if (rate_val > ADXL_MAX_SAMPLE_RATE_VAL) {
           rate_val = ADXL_MAX_SAMPLE_RATE_VAL;
           LOGD("Control set delay %d ms requetsed, limiting to rate %d [%d mHz]\n",
                ms, rate_val, (3200000 >> (15 - rate_val)));
       } else {
           LOGD("Control set delay %d ms requetsed, using rate %d [%d mHz]\n",
                ms, rate_val, (3200000 >> (15 - rate_val)));
       }
       return write_int("rate", rate_val);
   }

   static int control_wake(struct sensors_control_context_t *dev)
   {
       int err = 0;
       int fd = open(devname, O_WRONLY);
       if (fd > 0) {
           struct input_event event[1];
           event[0].type = EV_SYN;
           event[0].code = SYN_CONFIG;
           event[0].value = 0;
           err = write(fd, event, sizeof(event));
           LOGD_IF(err < 0, "control__wake, err=%d (%s)", errno, strerror(errno));
           close(fd);
       }
       return err;
   }

   static int control_close(struct hw_device_t *dev)
   {
       struct sensors_control_context_t *device_control = (void *)dev;

       if (device_control) {
           if (device_control->sensor_fd > 0)
               close(device_control->sensor_fd);
           free(device_control);
       }

       return 0;
   }

   static int sensors__data_open(struct sensors_data_context_t *dev, native_handle_t* handle)
   {
       int i;
       memset(&dev->sensors, 0, sizeof(dev->sensors));

       for (i = 0; i < MAX_NUM_SENSORS; i++) {
           dev->sensors[i].vector.status = SENSOR_STATUS_ACCURACY_HIGH;
       }
       dev->event_fd = dup(handle->data[0]);
       /* native_handle_close(handle); */
       native_handle_delete(handle);
       return 0;

   }

   static int sensors__data_close(struct sensors_data_device_t *dev)
   {
       struct sensors_data_context_t *data_device =
           (struct sensors_data_context_t *)dev;

       if (data_device->event_fd > 0) {
           close(data_device->event_fd);
       }

       return 0;
   }

   static int sensors__data_poll(struct sensors_data_context_t *dev, sensors_data_t * values)
   {
       struct input_event ev;
       int ret;
       uint32_t new_sensors = 0;
       int fd = dev->event_fd;

       while (1) {
           ret = read(fd, &ev, sizeof(ev));

           if (ret < (int)sizeof(ev))
               break;

           if (ev.type == EV_ABS) {
               /* Orientation or acceleration event */
               switch (ev.code) {
               case ABS_X:
                   new_sensors |= ACCELERATION_X;
                   dev->sensors[ID_A].acceleration.x = ev.value * CONVERT_X;
                   break;
               case ABS_Y:
                   new_sensors |= ACCELERATION_Y;
                   dev->sensors[ID_A].acceleration.y = ev.value * CONVERT_Y;
                   break;
               case ABS_Z:
                   new_sensors |= ACCELERATION_Z;
                   dev->sensors[ID_A].acceleration.z = ev.value * CONVERT_Z;
                   break;
               }
           } else if (ev.type == EV_SYN) {

               if (ev.code == SYN_CONFIG) {
                   /* Injected event by control_wake
                    * return immediately
                    */
                   return 0x7FFFFFFF;
               }

               /*
                * Linux Input suppresses identical events, so if
                * only ABS_Z changes and ABS_X,Y stays constant
                * between events we need to report the cached values.
                * Many other drivers start to scramble events by
                * waiting for a full triplet to arrive.
                * Other events on the ADXL345/6 such as TAP
                * should be turned off.
                */
               if (new_sensors) {
                   int64_t t =
                       ev.time.tv_sec * SEC_TO_NSEC +
                       ev.time.tv_usec * USEC_TO_NSEC;
                   new_sensors = 0;

                   dev->sensors[ID_A].time = t;
                   *values = dev->sensors[ID_A];
                   values->sensor = ID_ACCELERATION;
                   return ID_ACCELERATION;
               }
           }
       }
       return 0;
   }

   /******************************************************************************/

   /**
     * module methods
    */

   /** Open a new instance of a sensor device using name */
   static int open_sensors(const struct hw_module_t *module, const char *name,
               struct hw_device_t **device)
   {
       int status = -EINVAL;
       if (!strcmp(name, SENSORS_HARDWARE_CONTROL)) {
           struct sensors_control_context_t *dev;
           dev = malloc(sizeof(*dev));
           memset(dev, 0, sizeof(*dev));
           dev->sensor_fd = -1;
           dev->device.common.tag = HARDWARE_DEVICE_TAG;
           dev->device.common.version = 0;
           dev->device.common.module = (struct hw_module_t *)module;
           dev->device.common.close = control_close;
           dev->device.open_data_source = control_open_data_source;
           dev->device.activate = control_activate;
           dev->device.set_delay = control_set_delay;
           dev->device.wake = control_wake;
           *device = &dev->device.common;
       } else if (!strcmp(name, SENSORS_HARDWARE_DATA)) {
           struct sensors_data_context_t *dev;
           dev = malloc(sizeof(*dev));
           memset(dev, 0, sizeof(*dev));
           dev->event_fd = -1;
           dev->device.common.tag = HARDWARE_DEVICE_TAG;
           dev->device.common.version = 0;
           dev->device.common.module = (struct hw_module_t *)module;
           dev->device.common.close = sensors__common_close;
           dev->device.data_open = sensors__data_open;
           dev->device.data_close = sensors__data_close;
           dev->device.poll = sensors__data_poll;
           *device = &dev->device.common;
       }
       return status;
   }

   static struct hw_module_methods_t sensors_module_methods = {
       .open = open_sensors,
   };

   /*
     * The Sensors Hardware Module
    */
   const struct sensors_module_t HAL_MODULE_INFO_SYM = {
       .common = {
              .tag = HARDWARE_MODULE_TAG,
              .version_major = 1,
              .version_minor = 0,
              .id = SENSORS_HARDWARE_MODULE_ID,
              .name = "Analog Devices ADXL345/6 sensor",
              .author = "OPS MH",
              .methods = &sensors_module_methods,
              },
       .get_sensors_list = sensors_get_list,
   };
