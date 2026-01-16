set pagination off
file u-boot-spl
target remote :3333
tbreak board_init_r
load
continue
load u-boot
continue
