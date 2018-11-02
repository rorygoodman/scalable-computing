__author__ = 'rorygoodman'
hashfile = open("goodmanr.broken", "r")
newfile=open("goodmanr.broken", "w")
lines = hashfile.readlines()

for line in lines:
    if len(line.rstrip().replace(':',' '))==22:
        newfile.write(line.rstrip().replace(':',' ')[0:21]+"\n")
    else:
        newfile.write(line.rstrip().replace(':',' ')+"\n")



