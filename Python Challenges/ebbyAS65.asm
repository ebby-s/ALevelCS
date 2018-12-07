ldm 1
xch r3
ldm 2
xch r4
ldm 15
xch r15
jun dec_count

main:
clb
xch r1
add r3
xch r1
xch r0
add r2
ral
clc
rar
xch r0
xch r1
xch r3
xch r1
xch r0
xch r2
xch r0
jun dec_count

dec_count:
clb
ld r5
jcn az dec_higher
xch r5
dac
xch r5
jun main

dec_higher:
clb
xch r4
jcn az finish
dac
xch r4
ld r15
xch r5
jun main

finish:
jms $3ff
nop