######################################
print " "
print "Loading getShotgunData gizmo"
######################################

import getShotgunData

toolbar = nuke.toolbar("Nodes")
#toolbar.addCommand( "Shotgun/NukeTools", "nuke.createNode('MyGizmo')")
toolbar.addCommand("Shotgun/NukeTools/getShotgunData", "nuke.createNode(\"getShotgunData.gizmo\")", icon="Text.png")