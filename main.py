import os
import shutil
source1 = "C:/Users/user/Downloads"
destinationforsource = "C:/Users/user/Downloads/Testing"
listFiles = os.listdir(source1)
for filename in listFiles:
    name,extension = os.path.splitext(filename)
    if extension == '':
        continue
    if extension in ['.gif','.png','.jpeg','.jpg','.heic','.jfif']:
        p1 = source1+'/'+filename
        p2 = destinationforsource+'/'+"Images"
        p3 = destinationforsource+'/'+"Images"+'/'+filename
        if os.path.exists(p2):
            shutil.move(p1,p3)
        else:
            os.makedirs(p2)
            shutil.move(p1,p3)
print("Work Complete! Any questions/bugs? go to the github profile and ask :D")


