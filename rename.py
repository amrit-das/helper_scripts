import os
import sys
path = os.getcwd()
name = sys.argv[1]

path = path+'/'+name
files = os.listdir(path)
i=1

for file in files:
    os.rename(os.path.join(path,file), os.path.join(path, name+'.'+str(i)+'.jpg'))
    i+=1

