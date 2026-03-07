Appendix C: Target Debug Features
=================================

| :doc:`Click here to return to the A2B SSPLUS STACK USER GUIDE </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide>`
| ===== Bit Error Rate Test (BERT) ===== An example application for running BERT after discovery is provided in ‘ADI_A2B-SSPlus_Software-RelX.Y.Z\\Target\\examples\\advancedapp\\bert’ of the A2B Software package. The macro ‘A2B_RUN_BIT_ERROR_TEST’ is enabled in ‘a2bstack-pal\\platform\\a2b\\features.h’ to start the BERT test after discovery for a period defined by A2B_BERT_CALC_PERIOD and constantly updated after a time period mentioned in A2B_BERT_UPDATE_PERIOD. The BERT handler structure must be defined in the Application structure. ADI_A2B_BERT_HANDLER oBertHandler.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplusstackuserguide/bert.jpg
   :align: center
