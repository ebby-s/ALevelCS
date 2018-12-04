ldm 1
xch r0
ldm 2
xch r1
ldm 3
xch r2
ldm 9
xch r3

main:
ld r0
jcn an process_ones
ld r1
jcn an process_tens
ld r2
jcn an process_huns
ld r3
jcn an process_thous
jun finish

process_ones:
clb
xch r0
add r8
xch r8
tcc
add r9
xch r9
tcc
add r10
xch r10
tcc
add r11
xch r11
jun main

process_tens:
clb
xch r1
dac
xch r1
ldm 10
xch r0
jun main

process_huns:
clb
xch r2
dac
xch r2
ldm 10
xch r1
jun main

process_thous:
clb
xch r3
dac
xch r3
ldm 10
xch r2
jun main

finish:
jms $3ff
nop
