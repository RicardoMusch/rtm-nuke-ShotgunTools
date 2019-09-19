import os

new_version = raw_input("Version to Publish: ")
#print new_version

app_root = os.path.dirname((os.path.dirname(__file__))).replace("\\", "/")
app_name = os.path.basename(os.path.dirname(app_root).replace("_github",""))
new_app_version_root = os.path.dirname(app_root)
new_app_version_root = os.path.join(new_app_version_root,app_name+"_v"+new_version).replace("\\", "/")


#print "app_root:", app_root
#print "app_name:", app_name
#print "new_app_version_root:", new_app_version_root

import shutil

import subprocess

"Create the New Directory\n\n"
try:
    #os.mkdir(new_app_version_root)
    print "\n\n "
    proc = subprocess.Popen(["cmd", "/c", "mkdir", new_app_version_root.replace("/", os.sep)], stdout=subprocess.PIPE, shell=True)
except Exception as e:
    print e
    pass


print "\n\nCreating Publish and Copying Files"
proc = subprocess.Popen(["robocopy", app_root, new_app_version_root, "/S"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
#print "program output:", out


"Complete"
print "\n\nCompleted Publish"
raw_input("Press Enter to exit...")
