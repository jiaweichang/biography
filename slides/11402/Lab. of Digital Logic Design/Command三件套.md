```ssh
iverilog -o wave design.sv testbench.sv
```
```ssh
vvp wave
```
```ssh
gtkwave dump.vcd
```
