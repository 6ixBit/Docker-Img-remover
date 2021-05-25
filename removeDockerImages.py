import os
import subprocess
import sys

def getDockerImages(rowsToProcess):
    # Run command as subprocess to pipe output
    data = subprocess.Popen(['docker', 'image', 'ls'], stdout=subprocess.PIPE)
    data = str(data.communicate())
    data = data.split("\n") 
    data = data[0].split('\\')

    result = []
    output = []
  
    # iterate through the parsed output and append to result
    for line in data:
        result.append(line)
    
    del result[0] # Remove columns. e.g: Repository, Image ID

    for ele in result: # Range up to n rows based on input
        output.append(ele.split())

    return output[:rowsToProcess]

def removeImages(ImgData):
    queue = []
    for ele in ImgData:
        queue.append(ele[2]) # Parse img ID from input and add to queue

    # Pop from queue and then remove docker images 
    deleteCounter = 0
    while queue:
        img = queue.pop(0)
        try:
            os.system(f"docker image rm -f {img}")
            deleteCounter += 1
        except:
            print(f"Couldn't delete {img}")
    
    print("\n")
    print(f"Succesfully deleted {deleteCounter} docker images")

def parseCLIArgs():

    if len(sys.argv) == 2:
        try:
            rows = int(sys.argv[1])
            return rows
        except:
            print("Please specify the amount of images to delete. It removes the images from top to bottom based on the output from docker image ls.")
            print("\n")
            print("\t Example: python removeDockerImages.py 3")

            quit()

def main():
    numOfImagesToDelete = parseCLIArgs()

    data = getDockerImages(numOfImagesToDelete)
    removeImages(data)

if __name__ == "__main__":
    main()

# TODO: Check if input int will exceed the number of images available. check result in getDockerImg()
