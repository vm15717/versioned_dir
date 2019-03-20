import sys
sys.exit(-1)
lines=open("README.md","r").readlines()
for line in lines:
    print(line,end="")
print("\n everything is ok")
