import os
import sys
file=open(os.path.join(sys.path[0], "hash.txt"), mode ='r')

while 1:
    #read by character
    char = file.read(1)
    if not char:
        break
    print(char+"#",end="")
file.close()
#T#H#E# #W#O#R#L#D# #I#S# #N#O#T# #F#L#A#T#