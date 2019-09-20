# nuke-getShotgunData

## Shotgun Connection
- Uses the SGTK from the current running tk-nuke engine if possible, else uses external API which needs to be set up.
- For setting up the API connection, copy and rename the sg_connection_example.py file to sg_connection and fill in your API details.


## Usage
1) Either connect the gizmo to a read node (or any node with a file knob) or leave disconnected and specify the node name
2) Press "Update" which searches all active Shotgun Projects for a version with a matching sg_path_to_frames field value to the connected file knob.
(Logic is included to search for the path with either forward or backward slashes)
3) Information that was found will be filled into the knobs, any knobs left empty did not have any info in the corresponding Shotgun field.

## Project and Entity data
Apart from only displaying information from the version's fields, the node also displays information about the entity that that version belongs to (Shot or Asset, or other entity) as well as information about the project.
 
