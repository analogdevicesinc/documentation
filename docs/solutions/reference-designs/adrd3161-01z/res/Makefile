all: svgs

wireviz_files := $(wildcard *.wireviz.yml)
pngs: $(wireviz_files:.wireviz.yml=.png)
svgs: $(wireviz_files:.wireviz.yml=.lfs.svg)
gvs: $(wireviz_files:.wireviz.yml=.gv)

%.png: %.wireviz.yml
	wireviz -fp $^ -O $(patsubst %.png,%,$@)

%.lfs.svg: %.wireviz.yml
	wireviz -fs $^ -O $(patsubst %.svg,%,$@)

%.gv: %.wireviz.yml
	wireviz -fg $^ -O $(patsubst %.gv,%,$@)
