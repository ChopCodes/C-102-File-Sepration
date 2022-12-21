
import os
import shutil
#Imports the important libraries needed
source1 = "C:/Users/user/Downloads"
#change path to your desiered location
destinationforsource = "C:/Users/user/Downloads/Testing"
listFiles = os.listdir(source1)
# Creates variables for necessery need
## source1 is the path to the folder (downloads)
## Destinationforsource is the Testing folder in which all the folders will be made by the code 
## List files get all the files with extension so it can be sorted
for filename in listFiles:
    #Runs a for loop to get the files in the list of file
    name,extension = os.path.splitext(filename)
    #Splits the extension (refer to documentation for lib)
    if extension == '':
        continue
    #discards all the other extensions
    if extension in ['.gif','.png','.jpeg','.jpg','.heic','.jfif']:
        p1 = source1+'/'+filename
        p2 = destinationforsource+'/'+"Images"
        p3 = destinationforsource+'/'+"Images"+'/'+filename
        #P1 for the file with the extensions given above
        #P2 for the images folder that the code will made
        #P3 is the destination
        if os.path.exists(p2):
            shutil.move(p1,p3)
        else:
            os.makedirs(p2)
            shutil.move(p1,p3)
            #Checks if there is already an IMAGE folder
print("Work Complete! Any questions/bugs? go to the github profile and ask :D")
#Prints that the project sucessfully ran


