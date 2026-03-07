Obsolete Algorithms
===================

| :doc:`Click here to return to the Building Schematics page </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/buildingschematics>`
| SigmaStudio is designed to support backward compatibility with previous releases, including binary compatibility of the assembled DSP program. In most cases, the binary DSP code produced by SigmaStudio from one version to the next should be identical. Occasionally software defects or other issues are found in a SigmaStudio algorithm that require changes to the algorithm code and this would break the binary compatibility with previous releases.
| To preserve the binary backward compatibility, the original defective algorithm code is preserved in SigmaStudio and is used when a legacy project file (created in a previous SigmaStudio release) is loaded in a new release. This way the assembled DSP code is identical to a previous release. These old algorithms are called "Obsolete" and their presence in a project is shown the "Output" window after a "Link Compile Download" operation.

--------------

| To remove an obsolete algorithm and update to the latest "fixed" version, each cell with an obsolete algorithm can be updated manually as follows:
| 1. Open the old project file with obsolete algorithms.
| 2. Locate the obsolete algorithm list in the output window (version 3.11 and newer)
| 3. Right click on each cell and select "Remove Algorithm" from context menu.
| 4. Right click on the now empty cell and select "Add Algorithm" and select the desired updated algorithm version.
| 5. Reconnect any wires and/or grow the algorithm as necessary to recreate the original design.
