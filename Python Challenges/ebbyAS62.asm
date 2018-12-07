ldm 3
xch r0
ldm 11
xch r1
ldm 8
xch r2
ldm 10
xch r3

clb
add r3
add r3
xch r3
tcc
add r2
add r2
xch r2
tcc
add r1
add r1
xch r1
tcc
add r0
add r0
xch r0

jms $3ff
nop
