##########################################
print " "
print "Loading getShotgunData gizmo Menu"
##########################################

import nuke
toolbar = nuke.toolbar("Nodes")
#toolbar.addCommand( "Shotgun/NukeTools", "nuke.createNode('MyGizmo')")
toolbar.addCommand("Shotgun/NukeTools/getShotgunData", "nuke.createNode(\"getShotgunData.gizmo\")", icon="Text.png")