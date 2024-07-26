import os
import json
import shutil
from win32_setctime import setctime

#IMPORTANT: PHOTOS AND METADATA DIRECTORIES
media_path='Input/'
meta_path='Input/'
processed_path='Processed/'

#Initializing console
os.system('cls')
if not os.path.exists('Processed'):
    os.mkdir('Processed')
acceptedExtensions = (".JPG", ".JPEG")

#Iteration over all photos in media_path
processedCounter = 0
notProcessedCounter = 0
txtJsonNotFound = open("Unprocessed.txt","w")
txtJsonNotFound.write("It was not possible to found an associated JSON file for the following files:\n")

for file in os.listdir(media_path):
    filename = os.fsdecode(file) #filename contains also the extension of the file
    if not (filename.upper()).endswith(".JSON"):
        #Copy file into destination folder
        shutil.copyfile(media_path+filename,processed_path+filename)

        try:
            jsonFile=open(meta_path+filename+".json")
            jsonData=json.load(jsonFile)
            creationTimestamp=jsonData['photoTakenTime']['timestamp']

            #Setting Creation and LastModify date and time
            setctime(processed_path+filename, int(creationTimestamp))
            os.utime(processed_path+filename,(int(creationTimestamp),int(creationTimestamp)))
            processedCounter=processedCounter+1
            
        except:
            txtJsonNotFound.write(filename+"\n")
            notProcessedCounter=notProcessedCounter+1
             
        print(str(processedCounter)+" images processed",end="\r")


txtJsonNotFound.close()
print("\n\n")
print(str(processedCounter)+" files merged")
print(str(notProcessedCounter)+" files NOT merged (JSON not found)")

print("\033[92m")
print("  ____                   _ ")
print(" |  _ \\  ___  _ __   ___| |")
print(" | | | |/ _ \\| '_ \\ / _ \\ |")
print(" | |_| | (_) | | | |  __/_|")
print(" |____/ \\___/|_| |_|\\___(_)")
print("\033[37m")
input("\nPress ENTER to exit")

