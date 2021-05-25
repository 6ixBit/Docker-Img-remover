# Docker-Img-remover
Remove unwanted docker images from your machine.

# Run

Pass the number of images you want to delete from your system. You can determine how many images you want to remove by typing docker image ls into your terminal.
Then from there if you want to delete 3 of your most recent images which are at the top of the return output, simply pass that as an argument to the script and it 
will be removed from your machine.

python removeDockerImages.py 3


