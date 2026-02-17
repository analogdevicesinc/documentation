all: pngs

pngs: cable-can.png cable-encoder-bldc-abn.png cable-encoder-bldc-vesc.png cable-encoder-bldc.png cable-encoder-stepper.png

%.png: %.yml
	wireviz -fp $^

wireviz: cable-can.gv cable-encoder-bldc-abn.gv cable-encoder-bldc-vesc.gv cable-encoder-bldc.gv cable-encoder-stepper.gv 

%.gv: %.yml
	wireviz -fg $^

