A2B Bus Configuration XML Specification
=======================================

XML uses tags that are not predefined or standard, which means that they are created by the person who is writing the XML file. Usually, the first tag begins by specifying the XML version and the encoding being used. This is standard tag and is called prolog.

Bus config XML contains the configuration of A2B Bus

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/image1.png
   :align: center

Under Bus configuration, there are multiple sections as shown in the below image.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/image2.png
   :align: center

Section Specification
---------------------

| :doc:`Version_Info </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/bcfxml/version>` - Version Information of Bus Configuration File
| :doc:`Bus_Properties </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/bcfxml/busprop>` - Bus Properties indicating number of nodes in the A2B Network
| :doc:`Master_Slave_Chains </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/bcfxml/masterslavechains>` - Label used for A2B Chain
| :doc:`Master_Slave_Chain </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/bcfxml/masterslavechain>` - Details of main node and slave nodes configurations
| :doc:`Network_Configuration </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/bcfxml/networkcfg>` - Properties of the A2B Network
| :doc:`Stream_Configuration </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/bcfxml/streamcfg>` - Details of Stream Configuration
| :doc:`TimeStamp and Signature </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/bcfxml/timestamp>`
| Differences in Specification on different plugins

+---+
| \*\* Xml Fields\ **\|** SigmaStudio+                     |
| (ADI_A2B-SSPlus_Software-Rel1.3.2) **\|** SigmaStudio    |
| (ADI_A2B_Software-Rel19.10.0) **\|** SigmaStudio         |
| (ADI_A2B_Software-Rel19.4.5) **\|** Comments \*\*        |
+---+

| A2BDLL_Version (A2B Plugin Version)                      |

+----------------------------------------------------------+

| A2BStackDLL_Version (A2B Stack version)                  |

+----------------------------------------------------------+

| SigmaStudio_Version (SigmaStudio / SigmaStudio+ Version) |

+----------------------------------------------------------+

| Pin_Assignment_Settings                                  |

+----------------------------------------------------------+

| SPI_Settings                                             |

+----------------------------------------------------------+

| TXXBAR_Settings                                          |

+----------------------------------------------------------+

| RXXBAR_Settings                                          |

+----------------------------------------------------------+

| VMTR_Settings                                            |

+----------------------------------------------------------+

| PWM_Settings                                             |

+----------------------------------------------------------+

| Stream                                                   |

+----------------------------------------------------------+

| Slave Select                                             |

+----------------------------------------------------------+

| Device_Type of Peripheral                                |

+----------------------------------------------------------+

| Two_Step_Discovery_Field(Authentication_Settings)        |

+----------------------------------------------------------+

| Local_power(Node)                                        |

+----------------------------------------------------------+

| Serial_Rx_on_DTx1(I2S_Settings)                          |

+----------------------------------------------------------+

| Sync(I2S_Settings)                                       |

+----------------------------------------------------------+

| PDM_HPF_Corner_Freq(PDM_Settings)                        |

+----------------------------------------------------------+

| Dis_I2C_Interface(Basic_Configuration_and_Control)       |

+----------------------------------------------------------+

| I2C_FmPlus(Basic_Configuration_and_Control)              |

+----------------------------------------------------------+

| SWCTL2(Register_Settings)                                |

+----------------------------------------------------------+

| SWCTL5(Register_Settings)                                |

+----------------------------------------------------------+

| TXACTL_Register(Register_Settings)                       |

+----------------------------------------------------------+

| TXBCTL_Register(Register_Settings)                       |

+----------------------------------------------------------+

| TXCTL_Register(Register_Settings)                        |

+----------------------------------------------------------+

| AnalyzerNode(Authentication_Settings)                    |

+----------------------------------------------------------+

| SPI_Interface_in_Use(Network_Peripheral_Config)          |

+----------------------------------------------------------+

| Current_Interface(Network_Configuration)                 |

+----------------------------------------------------------+

| Redisc_WaitTime(Network_Configuration)                   |

+----------------------------------------------------------+

| Reduce_Rate_on_Bus(Common_Config)                        |

+----------------------------------------------------------+

| System_Reduce_Rate_Factor(Common_Config)                 |

+----------------------------------------------------------+

| SPI_SlaveSelect(Peripheral_x_Config)                     |

+----------------------------------------------------------+

| SPI_interface_status(Peripheral_x_Config)                |

+----------------------------------------------------------+
