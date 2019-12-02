import nuke
toolbar = nuke.toolbar("Nodes")
#toolbar.addCommand( "Shotgun/NukeTools", "nuke.createNode('MyGizmo')")
toolbar.addCommand("ShotgunTools/getShotgunData", "nuke.createNode(\"getShotgunData.gizmo\")", icon="Text.png")