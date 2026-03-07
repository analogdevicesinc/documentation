| :doc:`Click here to go back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetlibapi/apifuncs>`
| =====adi_ss_schematic_process=====
| Prototype

::

    ADI_SS_RESULT adi_ss_schematic_process( ADI_SS_SSN_HANDLE hSSn, 
                                            int32_t num_input_samples_per_chan, 
                                            adi_ss_sample_t *input_data[], 
                                            adi_ss_sample_t *output_data[], 
                                            ADI_SS_SSNPROPERTIES *pProperties) 
                                           );

| 
| Description
| This is the modified process API. This function calls the function pointer of SS+. The function pointer of SS+ is the main entry point in the SS+ block which is created by SigmaStudio during the linking process. This process API is used in the Default Application provided in the package.
| Parameters
| Name: hSSn

::

   Type: ADI_SS_SSN_HANDLE 
   Direction: Input
   Description: Handle to the SS+ instance.

   Name: num_input_samples_per_channel
   Type: int32_t
   Direction: Input
   Description: Pointer to the input audio data buffer. Audio samples should be in floating point format and multiple 
                channels can be saved in the buffer as either block or interleaved. The same setting should be used 
                in the SigmaStudio Host application
                
   Name: output_data
   Type: adi_ss_sample_t *
   Direction: Input
   Description: Pointer to the output audio data buffer. Audio samples are in floating point format and multiple 
                channels are arranged in the buffer either as block or interleaved based on the setting in the 
                SigmaStudio+ Host.
                
   Name: pProperties
   Type: ADI_SS_SSNPROPERTIES *
   Direction: Output
   Description: Used to pass properties from the SSn to Application.

| 
| Return value
| An appropriate error code of type ADI_SS_RESULT is returned.
