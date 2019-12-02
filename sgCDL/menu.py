import nuke
import os


sgCDL_file = os.path.join(os.path.dirname(__file__), "sgCDL.nk")


"Create Menu"
toolbar = nuke.toolbar("Nodes")
#toolbar.addCommand( "Shotgun/NukeTools", "nuke.createNode('MyGizmo')")
#toolbar.addCommand("Shotgun/Tools/sgCDL", "nuke.createNode(\"sgCDL.gizmo\")", icon="Text.png")
toolbar.addCommand("ShotgunTools/sgCDL", "nuke.loadToolset(sgCDL_file)")