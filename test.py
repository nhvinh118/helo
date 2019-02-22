files = []
files = open('vntxt.txt','w')
for x in range(100):
    files.writelines(x)
    
files.close