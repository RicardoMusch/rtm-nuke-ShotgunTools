# nuke-getShotgunData

https://github.com/RicardoMusch/nuke-getShotgunData/blob/master/screenshots/scr1.JPG?raw=true


# Installation
## Install (easy - but not flexible)
1) Download the latest release on the releases tab on Github
2) Unzip in your .nuke folder and add contents of the menu.py to your exisiting menu.py file. If one does not exist, use the supplied menu.py

## Install (managed pipeline)
1) Place the unzipped folder on a network location accesible by all machines, preferably in a root folder called "nuke-getShotgunData" and then in a subfolder with the version number of the downloaded release (i.e. v1.0)
2) Add the location of the folder to the NUKE_PATH environement variable or use nuke.pluginAddPath("folder location") to point to it


## Shotgun Connection
- Uses the SGTK from the current running tk-nuke engine if possible, else uses external API which needs to be set up
- For setting up the API connection, copy and rename the sg_connection_example.py file to sg_connection and fill in your API details


# Usage
1) Either connect the gizmo to a read node (or any node with a file knob) or leave disconnected and specify the node name
2) Press "Update" which searches all active Shotgun Projects for a version with a matching sg_path_to_frames field value to the connected file knob
(Logic is included to search for the path with either forward or backward slashes)
3) Information that was found will be filled into the knobs, any knobs left empty did not have any info in the corresponding Shotgun field

## Project and Entity data
Apart from only displaying information from the version's fields, the node also displays information about the entity that that version belongs to (Shot or Asset, or other entity) as well as information about the project
 
