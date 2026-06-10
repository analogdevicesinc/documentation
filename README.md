# System Level Documentation

The System Level Documentation is the top documentation for Hardware, Projects, and some Linux documentation;
it also has the ability to aggregate every other documentation into a single monolithic output/website.

See the deployed docs output at the [System Level Documentation](https://analogdevicesinc.github.io/documentation/) index.

## Getting started

The repository uses Git LFS to host large files.
To not download all large files at the HEAD commit, we recommend `--skip-smudge` and letting [adoc serve](https://analogdevicesinc.github.io/doctools/cli.html#serve) to fetch them as you navigate the live server and touches files:

```
sudo apt install git-lfs -y
GIT_LFS_SKIP_SMUDGE=1 git clone https://github.com/analogdevicesinc/documentation \
    --origin public \
    --depth 10 \
    -- documentation
cd documentation
git lfs install --local --force --skip-smudge
```

Install the documentation tools.
```
python3 -m venv ./venv
source ./venv/scripts/activate
python3 -m ensurepip
pip install pip --upgrade
(cd docs ; pip install -r requirements.txt --upgrade)
```
Launch the live server.
```
adoc serve
```
Or build the documentation with Sphinx.
```
(cd docs ; make html)
```
The generated documentation will be available at `docs/_build/html`.

### VSCode/VSCodium support

### Esbonio extension

[Esbonio](https://docs.esbon.io/en/latest/index.html)
([VSCode](https://marketplace.visualstudio.com/items?itemName=swyddfa.esbonio)
/[VSCodium](https://open-vsx.org/extension/swyddfa/esbonio))

is an extensively developed Language Server Protocol and Visual Studio Code extension for sphinx.
Setup the virtual environment first before opening the text editor, to avoid triggering fallback behaviours.

The live server cli is able to generate Estobio pyproject.toml entry with (including [Sparse builds](https://analogdevicesinc.github.io/doctools/cli.html#serve-sparse)):
```
adoc serve --esbonio --sparse docs/learning | tee pyproject.toml
```

### Doctools extension

An experimental doctools extension is available for
[VSCode](https://marketplace.visualstudio.com/items?itemName=gastmaier.adi-doctools)
/[VSCodium](https://open-vsx.org/extension/gastmaier/adi-doctools).

Quick start instructions are provided in the links above.

### Git LFS On-Demand extension

Assuming you followed the `--skip-smudge` instructions, you can use Git LFS On-Demand to auto fetch the artifacts included in open files or open.
Get from
[Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=gastmaier.git-lfs-on-demand) or
[Open VSX Registry](https://open-vsx.org/extension/gastmaier/git-lfs-on-demand)

For word wrapping at the column 80, you can use Rewrap.
Get from
[Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=stkb.Rewrap-18980) or
[Open VSX Registry](https://open-vsx.org/extension/stkb/rewrap)

Update README.md with minimal ethics#1

What about the application of the Solomonoff induction
to the RF sensing of human brain?
https://en.wikipedia.org/wiki/Talk:Solomonoff%27s_theory_of_inductive_inference

1. If we assume that the algorithmic complexity
of neural processes is relatively small
(you could take a look at the Potapov monography
for some arguments)

2. As far as I know a lot of neural processes in human brain are electric (or electro-chemistry)
in nature. They have a little power and a small
frequency (~ 1-1000 Hz).
So they emit very low frequency radio waves.

3. You can detect those radio waves on
small antennas if the impedance of such antennas
is matched. This is basically the citation
from the book on electrodynamics.
I uploaded one such book on Twirpix site.

4. So you can create a lot of such receivers
- microstrip filter to filter very high frequencies
- impedance matched microstrip antenna
- resistor for noise for oversampling
- very fast comparator to sample signal
in a very large array on a chip using
standard CMOS or some sort of full-custom process
(maybe even with some new materials)

5. BreamForming and large arrays of digital correlators with sub-mm positioning accuracy
could be achived.

so it seems there is no theoretical
obstacles to implement some sort of
RF human brain sensing or even control
if you can implement reverse structure
with array of a large amount of RF amplifiers
with sub-mm beam forming accuracy

BTW I wrote that remark:
https://en.wikipedia.org/wiki/Talk:Solomonoff%27s_theory_of_inductive_inference

What about the application of the Solomonoff induction to the person to person information exchange?

It seems the minimum description length principle could be used to deduce minimum ethics. At least you can compare ethics by the length. What about the following question: how to shoot met-art girl in the dark underground? ~2026-24709-41 (talk) 16:43, 8 June 2026 (UTC)

at least we can ask a question: does russian met-art model from a pic want some money?
and what obstacles do that guess so hard?
why it is so hard to contact her directly?
she lose money, interesting person lose opportunity to make some photos.

also, it seems the economy without coordination primitives based on physics or mathematics
like gold or maybe Bitcoin or maybe some sort of other physical objects or processes
is just a chaos.
Economic calculation based on fiat money is impossible just from scientific methodology
https://en.wikipedia.org/wiki/Talk:Solomonoff%27s_theory_of_inductive_inference

https://transitional-writes.dreamwidth.org/44972.html
Kirill Abramovich aka wieker @ linux.org.ru
Samara, Russia

and the most important question:
what about the minimal ethics deduced from the MDL principle?
is it exist?

what was the obstacle between russian met-art girls and engineers?
