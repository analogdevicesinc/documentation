Appendix D: Auto Configuration from EEPROM
==========================================

| :doc:`Click here to return to the A2B SSPLUS STACK USER GUIDE </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide>`
| Auto-configuration of slave nodes allows the register and peripheral configuration of a slave node to be programmed from an EEPROM attached to the node during discovery by the Stack. To enable the auto-configuration feature in the Stack, define the macro A2B_FEATURE_EEPROM_PROCESSING in ‘Target\\examples\\demo\\<a2b-xx>\\a2bstack-pal\\platform\\a2b\\features.h’.

The pre-requisite for this feature is that the configuration needs to be programmed in the EEPROM attached to the slave node and the exported bus configuration file from Sigma Studio should have the auto-configuration enabled for the node. Refer :doc:`a2bssplususerguide </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide>` to configure the same in Sigma Studio.
