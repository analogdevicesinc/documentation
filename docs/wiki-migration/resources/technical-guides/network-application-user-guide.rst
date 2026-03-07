Network-app Documentation
=========================

For creating a network application, there are pieces in place to interface with different facets of network communication.

This document works for those who are attempting to create a network application from scratch with IE stacks. This has no use without appropriate hardware and software.

Structure of the network-application:
-------------------------------------

There are two types of assets, namely Interface Assets and Functional Assets.

Interface Assets: These are the assets that provide the network application with an interface to functionality that is part of the IO application. For example, the asset network-os-srv asset extracts the freertos functionality by requesting the APIs from the freertos-ospl-srv asset that is part of the io-app workspace. These Interface assets request the APIs from the io-app assets using the registrar-srv.

Functional Assets:
------------------

These are common assets that provide the network application with a specific functionality. For instance the led-srv provides a functional API which controls the NET and MOD LEDs. As with the led-srv it is likely that the hardware interface used to access the physical devices is abstracted via an interface asset, but this is not always the case.

Component Layer:
----------------

The assets in the component layer provide the core functionality of the network application. Each asset at this layer is responsible for the control, configuration, or operation of a complex portion of the network application. For example rems-drv, industrial protocol stacks like ethernet-ip-stk, profinet-stk, ethercat-stk, TCP/IP stack like fusion-stk etc.

Manager Layer:
--------------

Assets at the manager layer provide an abstracted API for control of the associated components. This API will be used as static symbols for dependencies from other assets in the Network Application regardless of the functional layer of the asset. The API will be populated with function pointers during the request phase of registrar operation in order to dynamically link the desired component to the manager. For instance the Ethernet Interface Manager has an abstracted API for transmitting and receiving frames which can be utilized statically by any of the protocol stacks. It also has an API for interrupt and event disposition as well as initialization and configuration of the switch hardware. Each manager has to be individually designed to appropriately abstract the API of the components it is managing.

Abstraction Layer:
------------------

The assets at the abstraction layer provide both the translation and registration of the component specific API implementation of the abstract manager API. For instance the Ethernet IF Manager's abstracted interface for transmitting frames will have a REMS, GREMS, LES, and LEN specific translation at this layer which would take the common inputs from the manager API and call the component driver functions. This translation function will be registered with the registrar in order to populate the appropriate functional interface for the manager layer. User Interface Layer: The user interface layer is used to denote assets that allow user access to the Network Application. The three assets in this layer provide the IO and Network Application with the tools for communicating the necessary information across the application boundaries during various stages of operation. At initialization the Network Application Startup Service provides the IO application with static symbols to initialize and begin operation. Once initialized the registrar provides the two applications the means to share function pointers for tagged interfaces so that the Network Application may gain access to the appropriate hardware and system interfaces while the IO Application gets access to the common interface. Network Application Startup Service: The network-startup-srv provides three symbols which are exported post link which allow the IO Application to: 1. initialize the Network Application Memory and return the registrar interface, 2. start the Network Application background thread, and 3. determine if the Network Application has completed its initialization process for synchronization purposes.

Registrar:
----------

As part of the initialization performed in step 1 of the network application start up service the registrar is reset into a zero state, populated with the Network Application's component interfaces via the abstraction layer and the function pointers for the register and request APIs are returned to the IO Application. The register and request function pointers are used by the IO Application to first register the component interfaces and then request the need components interfaces from the Network Application. Once both applications have completed the registration/request process with no missing interfaces, standard program execution can begin in both the IO and Network threads.

Common Interface Service:
-------------------------

As it did in the fido1100 architecture, the common interface provides an abstracted method of configuring and exchanging data across any industrial protocol. The source of the access to the the Network Application via the common interface may be local as in the case of the Developer's Solution where the IO Application providing a single processor solution. Or the access to the Network Application may be indirect via the Unified Interface IO Application implementing calls from a secondary Application processor.

Asset Details:
~~~~~~~~~~~~~~

-  network-startup-srv: Entry point.

   -  Exports symbols for inclusion in IO application.

::

      *  Performs memory initialization.
      *  Performs network application constructors (i.e. registers the common interface)
   * registrar-srv: Provides API registration/request interface to both network and IO applications
   * network-os-srv: Interface to RTOS constructs (i.e. Tasks, Queues, Semaphore, etc.)
   * filesystem-srv: Interface to filesystem
   * network-hwal-srv: Interface to processor abstraction.
     * Includes: Atomic functions, internal watchdog interface, interrupt configuration, clock informatives.
   * uart-srv: Interface to dedicated debug UART.
   * gpio-srv: Interface to system GPIO.
   * spi-srv: Interface to system SPI.
   * flash-srv: Former interface to system flash.  Will not be necessary once filesystem-srv in place.
   * i2c-srv: Former interface to system I2C. 
   * i2c-peripherials-drv: Drivers for I2C components, EEPROM and LED Driver.  Will not be necessary on the next generation module.
   * nvm-srv:  Provided functional abstraction for nonvolatile storage.  Will not be necessary once filesystem-srv in place.
   * mdio-srv: Provides interface to system MDIO either through GPIO or SMI (Station Management Interface) hardware.
   * phy-drv: Provides abstraction of PHY functionality.
   * led-srv: Provides abstraction of LED functionality.
   * cli-srv: Provides interface to system command line operations.
   * shell-srv: Registers debug capabilities of managers.  Dispositions debug events.
   * board-configuration-srv: Interface to board configuration information stored in program flash for configuration of network or IO application hardware.
