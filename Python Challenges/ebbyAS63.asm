ldm 15
xch r1

clb
ld r1

main:
ral
jcn c1 add_one
jcn az finish
jun main

add_one:
inc r0
clc
jun main

finish:
jms $3ff
nop