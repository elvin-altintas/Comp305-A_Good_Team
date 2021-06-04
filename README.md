# Comp305-A_Good_Team
Comp 305 Term Project 

Summary

This is a project to maximize the score of players on a board. To do this, we brought the board as close as possible to a checkerboard format. To overcome the disadvantage of having pre-assigned spots. Firstly the most suitable checkerboard format is determined. Secondly, we filled the spots that fit predetermined checkerboard version which has no neighbours. In the end, the left available spots with 0 or 1 neighbours are filled too. The algorithm returns the possible maximum score as a result of player allignment.

RUNTIME FOR CUSTOM TEST CASES

extra test case 1
```
2
7 5
#???.
??#?#
?????
.?..?
?#?#?
????.
.? # .?
6 5
??#?#
?????
.?..?
?#?#?
????.
.?#.?
```

extra test case 2
```
2
6 4
#???
.#.?
??##
????
????
?#?.
12 3
.?.
??#
??.
???
???
?#?
.??
#?.
??#
???
?##
?##
```
Output 1
Score:  56
Runtime for custom cases:  0.00018715858459472656
Score:  48
Runtime for custom cases:  0.00033402442932128906

Output 2
Score:  42
Runtime for custom cases:  0.00013399124145507812
Score:  60
Runtime for custom cases:  0.0002758502960205078



RUNTIME FOR DEFAULT TEST CASES

Test case t: 0
Algorithm Score: 68  |  Real Score: 68
Runtime for default cases:  0.0018069744110107422


Test case t: 1
Algorithm Score: 294  |  Real Score: 296
Runtime for default cases:  0.0027658939361572266


Test case t: 2
Algorithm Score: 100  |  Real Score: 100
Runtime for default cases:  0.0030889511108398438


Test case t: 3
Algorithm Score: 144  |  Real Score: 146
Runtime for default cases:  0.0035409927368164062


Test case t: 4
Algorithm Score: 438  |  Real Score: 438
Runtime for default cases:  0.004897117614746094


Test case t: 5
Algorithm Score: 28  |  Real Score: 28
Runtime for default cases:  0.004993915557861328


Test case t: 6
Algorithm Score: 258  |  Real Score: 264
Runtime for default cases:  0.005873918533325195


Test case t: 7
Algorithm Score: 246  |  Real Score: 246
Runtime for default cases:  0.0067179203033447266


Test case t: 8
Algorithm Score: 42  |  Real Score: 42
Runtime for default cases:  0.006854057312011719


Test case t: 9
Algorithm Score: 82  |  Real Score: 82
Runtime for default cases:  0.007161855697631836


Test case t: 10
Algorithm Score: 56  |  Real Score: 56
Runtime for default cases:  0.00791311264038086


Test case t: 11
Algorithm Score: 72  |  Real Score: 72
Runtime for default cases:  0.008142948150634766


Test case t: 12
Algorithm Score: 34  |  Real Score: 34
Runtime for default cases:  0.008258819580078125


Test case t: 13
Algorithm Score: 382  |  Real Score: 388
Runtime for default cases:  0.009580850601196289


Test case t: 14
Algorithm Score: 88  |  Real Score: 88
Runtime for default cases:  0.009816884994506836


Test case t: 15
Algorithm Score: 44  |  Real Score: 44
Runtime for default cases:  0.00998687744140625


Test case t: 16
Algorithm Score: 124  |  Real Score: 130
Runtime for default cases:  0.010404825210571289


Test case t: 17
Algorithm Score: 180  |  Real Score: 184
Runtime for default cases:  0.010959863662719727


Test case t: 18
Algorithm Score: 72  |  Real Score: 72
Runtime for default cases:  0.011190176010131836


Test case t: 19
Algorithm Score: 310  |  Real Score: 310
Runtime for default cases:  0.012269973754882812


Test case t: 20
Algorithm Score: 194  |  Real Score: 194
Runtime for default cases:  0.013117074966430664


Test case t: 21
Algorithm Score: 40  |  Real Score: 40
Runtime for default cases:  0.013302803039550781


Test case t: 22
Algorithm Score: 128  |  Real Score: 128
Runtime for default cases:  0.013702869415283203


Test case t: 23
Algorithm Score: 70  |  Real Score: 70
Runtime for default cases:  0.013923883438110352


Test case t: 24
Algorithm Score: 64  |  Real Score: 64
Runtime for default cases:  0.014103889465332031


Test case t: 25
Algorithm Score: 110  |  Real Score: 110
Runtime for default cases:  0.01444387435913086


Test case t: 26
Algorithm Score: 80  |  Real Score: 82
Runtime for default cases:  0.014690876007080078


Test case t: 27
Algorithm Score: 288  |  Real Score: 288
Runtime for default cases:  0.01562190055847168


Test case t: 28
Algorithm Score: 118  |  Real Score: 120
Runtime for default cases:  0.015993833541870117


Test case t: 29
Algorithm Score: 170  |  Real Score: 170
Runtime for default cases:  0.016387939453125


Test case t: 30
Algorithm Score: 194  |  Real Score: 194
Runtime for default cases:  0.016937971115112305


Test case t: 31
Algorithm Score: 198  |  Real Score: 198
Runtime for default cases:  0.01749897003173828


Test case t: 32
Algorithm Score: 290  |  Real Score: 292
Runtime for default cases:  0.018390178680419922


Test case t: 33
Algorithm Score: 60  |  Real Score: 60
Runtime for default cases:  0.018590927124023438


Test case t: 34
Algorithm Score: 52  |  Real Score: 52
Runtime for default cases:  0.018774032592773438


Test case t: 35
Algorithm Score: 328  |  Real Score: 330
Runtime for default cases:  0.019949913024902344


Test case t: 36
Algorithm Score: 100  |  Real Score: 100
Runtime for default cases:  0.020290851593017578


Test case t: 37
Algorithm Score: 174  |  Real Score: 174
Runtime for default cases:  0.02074599266052246


Test case t: 38
Algorithm Score: 220  |  Real Score: 220
Runtime for default cases:  0.021373987197875977


Test case t: 39
Algorithm Score: 330  |  Real Score: 334
Runtime for default cases:  0.02238607406616211


Test case t: 40
Algorithm Score: 0  |  Real Score: 0
Runtime for default cases:  0.022424936294555664


Test case t: 41
Algorithm Score: 286  |  Real Score: 292
Runtime for default cases:  0.023344993591308594


Test case t: 42
Algorithm Score: 8  |  Real Score: 8
Runtime for default cases:  0.023415803909301758


Test case t: 43
Algorithm Score: 142  |  Real Score: 146
Runtime for default cases:  0.02391791343688965


Test case t: 44
Algorithm Score: 380  |  Real Score: 380
Runtime for default cases:  0.025218963623046875


Test case t: 45
Algorithm Score: 38  |  Real Score: 38
Runtime for default cases:  0.025385141372680664


Test case t: 46
Algorithm Score: 32  |  Real Score: 32
Runtime for default cases:  0.02550506591796875


Test case t: 47
Algorithm Score: 134  |  Real Score: 134
Runtime for default cases:  0.025996923446655273


Test case t: 48
Algorithm Score: 374  |  Real Score: 374
Runtime for default cases:  0.02711796760559082


Test case t: 49
Algorithm Score: 124  |  Real Score: 124
Runtime for default cases:  0.0275421142578125


Test case t: 50
Algorithm Score: 210  |  Real Score: 212
Runtime for default cases:  0.028261899948120117


Test case t: 51
Algorithm Score: 4  |  Real Score: 4
Runtime for default cases:  0.02830195426940918


Test case t: 52
Algorithm Score: 372  |  Real Score: 378
Runtime for default cases:  0.029850006103515625


Test case t: 53
Algorithm Score: 372  |  Real Score: 382
Runtime for default cases:  0.03132987022399902


Test case t: 54
Algorithm Score: 280  |  Real Score: 280
Runtime for default cases:  0.032205820083618164


Test case t: 55
Algorithm Score: 64  |  Real Score: 64
Runtime for default cases:  0.03236889839172363


Test case t: 56
Algorithm Score: 136  |  Real Score: 144
Runtime for default cases:  0.032790184020996094


Test case t: 57
Algorithm Score: 326  |  Real Score: 334
Runtime for default cases:  0.033828020095825195


Test case t: 58
Algorithm Score: 224  |  Real Score: 224
Runtime for default cases:  0.03473806381225586


Test case t: 59
Algorithm Score: 168  |  Real Score: 168
Runtime for default cases:  0.0352940559387207


Test case t: 60
Algorithm Score: 228  |  Real Score: 232
Runtime for default cases:  0.03600192070007324


Test case t: 61
Algorithm Score: 126  |  Real Score: 126
Runtime for default cases:  0.03633689880371094


Test case t: 62
Algorithm Score: 84  |  Real Score: 84
Runtime for default cases:  0.03662896156311035


Test case t: 63
Algorithm Score: 16  |  Real Score: 16
Runtime for default cases:  0.036708831787109375


Test case t: 64
Algorithm Score: 342  |  Real Score: 342
Runtime for default cases:  0.03786611557006836


Test case t: 65
Algorithm Score: 274  |  Real Score: 276
Runtime for default cases:  0.03882718086242676


Test case t: 66
Algorithm Score: 286  |  Real Score: 286
Runtime for default cases:  0.039691925048828125


Test case t: 67
Algorithm Score: 314  |  Real Score: 324
Runtime for default cases:  0.040789127349853516


Test case t: 68
Algorithm Score: 204  |  Real Score: 210
Runtime for default cases:  0.0414118766784668


Test case t: 69
Algorithm Score: 424  |  Real Score: 424
Runtime for default cases:  0.0427699089050293


Test case t: 70
Algorithm Score: 118  |  Real Score: 122
Runtime for default cases:  0.043150901794433594


Test case t: 71
Algorithm Score: 10  |  Real Score: 10
Runtime for default cases:  0.04320812225341797


Test case t: 72
Algorithm Score: 286  |  Real Score: 292
Runtime for default cases:  0.04405474662780762


Test case t: 73
Algorithm Score: 102  |  Real Score: 104
Runtime for default cases:  0.04445910453796387


Test case t: 74
Algorithm Score: 194  |  Real Score: 202
Runtime for default cases:  0.045083045959472656


Test case t: 75
Algorithm Score: 138  |  Real Score: 138
Runtime for default cases:  0.04561805725097656


Test case t: 76
Algorithm Score: 394  |  Real Score: 398
Runtime for default cases:  0.04695296287536621


Test case t: 77
Algorithm Score: 48  |  Real Score: 52
Runtime for default cases:  0.047178030014038086


Test case t: 78
Algorithm Score: 70  |  Real Score: 70
Runtime for default cases:  0.04739093780517578


Test case t: 79
Algorithm Score: 114  |  Real Score: 116
Runtime for default cases:  0.04773211479187012


Test case t: 80
Algorithm Score: 220  |  Real Score: 220
Runtime for default cases:  0.04835391044616699


Test case t: 81
Algorithm Score: 118  |  Real Score: 118
Runtime for default cases:  0.048709869384765625


Test case t: 82
Algorithm Score: 144  |  Real Score: 144
Runtime for default cases:  0.04923200607299805


Test case t: 83
Algorithm Score: 392  |  Real Score: 392
Runtime for default cases:  0.05062580108642578


Test case t: 84
Algorithm Score: 136  |  Real Score: 136
Runtime for default cases:  0.05120396614074707


Test case t: 85
Algorithm Score: 380  |  Real Score: 382
Runtime for default cases:  0.052525997161865234


Test case t: 86
Algorithm Score: 170  |  Real Score: 170
Runtime for default cases:  0.052971839904785156


Test case t: 87
Algorithm Score: 168  |  Real Score: 168
Runtime for default cases:  0.05342912673950195


Test case t: 88
Algorithm Score: 114  |  Real Score: 116
Runtime for default cases:  0.05378103256225586


Test case t: 89
Algorithm Score: 190  |  Real Score: 190
Runtime for default cases:  0.05456185340881348


Test case t: 90
Algorithm Score: 114  |  Real Score: 114
Runtime for default cases:  0.054939985275268555


Test case t: 91
Algorithm Score: 4  |  Real Score: 4
Runtime for default cases:  0.054982900619506836


Test case t: 92
Algorithm Score: 140  |  Real Score: 140
Runtime for default cases:  0.05530095100402832


Test case t: 93
Algorithm Score: 352  |  Real Score: 360
Runtime for default cases:  0.05659818649291992


Test case t: 94
Algorithm Score: 136  |  Real Score: 136
Runtime for default cases:  0.05706787109375


Test case t: 95
Algorithm Score: 266  |  Real Score: 266
Runtime for default cases:  0.05779218673706055


Test case t: 96
Algorithm Score: 178  |  Real Score: 178
Runtime for default cases:  0.05838608741760254


Test case t: 97
Algorithm Score: 278  |  Real Score: 278
Runtime for default cases:  0.05931591987609863


Test case t: 98
Algorithm Score: 92  |  Real Score: 92
Runtime for default cases:  0.05958986282348633


Test case t: 99
Algorithm Score: 74  |  Real Score: 74
Runtime for default cases:  0.05977797508239746

Accuracy of the algorithm:  0.68

Process finished with exit code 0

     


Information on Running the Code

The code was written in Python3 and compiled in PyCharm. You can run this code by writing a test case array as the given example in the code.


