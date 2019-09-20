def update():

    import nuke
    from datetime import datetime
    import os
    import sys


    ########################################################################################################
    print "Connecting to Shotgun"

    try:
        import sgtk
        # get the engine we are currently running in
        current_engine = sgtk.platform.current_engine()
        # get hold of the shotgun api instance used by the engine, (or we could have created a new one)
        sg = current_engine.shotgun
        print "Connected to Shotgun via current SGTK engine...\n"
    except:
        import sg_connection
        sys.path.append(os.environ["SHOTGUN_API3"])
        import shotgun_api3
        # Connect to SG
        sg = shotgun_api3.Shotgun(os.environ["SERVER_PATH"], os.environ["SCRIPT_NAME"], os.environ["SCRIPT_KEY"])
        print "Connected to Shotgun via api...\n"


    ########################################################################################################
    print "Loading Functions"
    def getSGStatusFriendlyName(status_short_code):
        fields = ["name"]
        filters = [ ['code', 'is', status_short_code ] ]
        friendly_status = sg.find_one("Status", filters, fields)
        #print friendly_status
        return friendly_status.get("name")


    "Me"
    try:
        n = nuke.selectedNode()
    except Exception as e:
        print e
        n = nuke.thisNode()


    "Making sure we are connected to a node with a file knob"
    try:
        try:
            "Get Upstream Node"
            read = nuke.toNode(n.input(0)["name"].getValue())
        except:
            "Get Node from Knob"
            read = nuke.toNode(n["source_node"].getValue())
        print "Using Read:"+str(read["name"].getValue())
        print "File knob: "+read["file"].getValue()
    except:
        nuke.message("Please connect to a node with a file knob or add the name in the input knob!")
        return


    "Filename to search Shotgun with"
    searchString_backwards = read["file"].getValue().replace("/","\\")
    searchString_forwards = read["file"].getValue().replace("\\","/")
    print "Searching Shotgun for data with search string:\n"+searchString_forwards+"\n"


    print "\nSearching Shotgun for version data"
    fields = [ "code", "sg_status_list", "client_code", "entity", "sg_slate_notes", "project", "user", "created_at", "description", "sg_version_type", "sg_tech_check_notes", "sg_tech_check_approved", "sg_editorial_status" ]
    filters = [ ["sg_path_to_frames", "contains", searchString_forwards] ]
    version_data = sg.find_one('Version', filters, fields)
    #print version_data

    if version_data == None:
        filters = [ ["sg_path_to_frames", "contains", searchString_backwards] ]
        version_data = sg.find_one('Version', filters, fields)
        #print version_data


    print "\nSearching Shotgun for entity data "
    fields = ["sg_asset_type", "sg_status_list", "sg_head_in", "sg_tail_out", "sg_head_handle", "sg_tail_handle", "sg_cut_in", "sg_cut_out", "tank_name", "sg_sequence", "sg_episode"]
    filters = [ ["id", "is", version_data.get("entity").get("id")] ]
    entity_data = sg.find_one(version_data.get("entity").get("type"), filters, fields)
    #print entity_data

    
    print "\nSearching Shotgun for project data "
    fields = ["tank_name", "sg_fps"]
    filters = [ ['name', 'contains', version_data.get("project").get("name")] ]
    project_data = sg.find_one("Project", filters, fields)
    #print project_data


    #############################################################################
    print "\nProcessing Project data"
    try:
        field = "tank_name"
        n[field].setValue("")
        n[field].setValue(project_data.get(field))
    except Exception as e:
        print field
        print e
    try:
        n["project_fps"].setValue("")
        n["project_fps"].setValue(str(project_data.get("sg_fps")))
    except Exception as e:
        print "project_fps"
        print e


    #############################################################################
    print "\nProcessing Version data"
    try:
        field = "project"
        n[field].setValue("")
        n[field].setValue(version_data.get(field).get("name"))
    except Exception as e:
        print field
        print e
    try:
        n["version_name"].setValue("")
        n["version_name"].setValue(version_data.get("code"))
    except Exception as e:
        print "version_name"
        print e
    try:
        field = "client_code"
        n[field].setValue("")
        n[field].setValue(version_data.get(field))
    except Exception as e:
        print field
        print e
    try:
        field = "user"
        n[field].setValue("")
        n[field].setValue(version_data.get(field).get("name"))
    except Exception as e:
        print field
        print e
    try:
        field = "created_at"
        n[field].setValue("")
        n[field].setValue(str(version_data.get(field)))
    except Exception as e:
        print field
        print e
    try:
        n["entity_type"].setValue(version_data.get("entity").get("type"))
    except Exception as e:
        print "entity_type"
        print e
    try:
        entity_name = version_data.get("entity").get("name")
        n["entity_name"].setValue("")
        n["entity_name"].setValue(entity_name)
    except Exception as e:
        print "entity_name"
        print e
    try:
        field = "description"
        n[field].setValue("")
        n[field].setValue(version_data.get(field))
    except Exception as e:
        print field
        print e
    try:
        field = "sg_slate_notes"
        n[field].setValue("")
        n[field].setValue(version_data.get(field))
    except Exception as e:
        print field
        print e
    try:
        field = "sg_version_type"
        n[field].setValue("")
        n[field].setValue(version_data.get(field))
    except Exception as e:
        print field
        print e
    try:
        field = "sg_tech_check_notes"
        n[field].setValue("")
        n[field].setValue(version_data.get(field))
    except Exception as e:
        print field
        print e
    try:
        field = "sg_tech_check_approved"
        n[field].setValue("")
        n[field].setValue(version_data.get(field))
    except Exception as e:
        print field
        print e
    try:
        field = "sg_editorial_status"
        n[field].setValue("")
        n[field].setValue(version_data.get(field))
    except Exception as e:
        print field
        print e
    try:
        field = "sg_status_list"
        status = getSGStatusFriendlyName(version_data.get(field))
        n["sg_version_status_list"].setValue("")
        n["sg_version_status_list"].setValue(status)
    except Exception as e:
        print field
        print e


    #############################################################################
    print "\nProcessing Entity data"
    try:
        field = "sg_asset_type"
        n[field].setValue("")
        n[field].setValue(entity_data.get(field))
    except Exception as e:
        print field
        print e    
    try:
        field = "sg_episode"
        n[field].setValue("")
        n[field].setValue(entity_data.get(field).get("name"))
    except Exception as e:
        print field
        print e
    try:
        field = "sg_sequence"
        n[field].setValue("")
        n[field].setValue(entity_data.get(field).get("name"))
    except Exception as e:
        print field
        print e
    try:
        field = "sg_head_in"
        n[field].setValue("")
        value = str(entity_data.get(field))
        if value == "None":
            value = "0"
        n[field].setValue(str(value))
    except Exception as e:
        print field
        print e
    try:
        field = "sg_tail_out"
        n[field].setValue("")
        value = str(entity_data.get(field))
        if value == "None":
            value = "0"
        n[field].setValue(str(value))
    except Exception as e:
        print field
        print e
    try:
        field = "sg_head_handle"
        n[field].setValue("")
        value = str(entity_data.get(field))
        if value == "None":
            value = "0"
        n[field].setValue(str(value))
    except Exception as e:
        print field
        print e
    try:
        field = "sg_tail_handle"
        n[field].setValue("")
        value = str(entity_data.get(field))
        if value == "None":
            value = "0"
        n[field].setValue(str(value))
    except Exception as e:
        print field
        print e
    try:
        field = "sg_cut_in"
        n[field].setValue("")
        value = str(entity_data.get(field))
        if value == "None":
            value = "0"
        n[field].setValue(str(value))
    except Exception as e:
        print field
        print e
    try:
        field = "sg_cut_out"
        n[field].setValue("")
        value = str(entity_data.get(field))
        if value == "None":
            value = "0"
        n[field].setValue(str(value))
    except Exception as e:
        print field
        print e
    try:
        field = "sg_status_list"
        n["sg_entity_status_list"].setValue("")
        friendly_status = getSGStatusFriendlyName(entity_data.get(field))
        n["sg_entity_status_list"].setValue(friendly_status)
    except Exception as e:
        print field
        print e



    #############################################################################
    print "\nFinding Step"
    try:
        n["step"].setValue("")
        try:
            step = read["file"].getValue().replace("\\","/").lower()
            step = step.split(entity_name.lower())[1]
            step = step.split("/")[1]
            n["step"].setValue(step)
        except:
            step = read["file"].getValue().replace("\\","/").lower()
            step = step.split("/publish")[0]
            step = step.split("/")[-1]
            n["step"].setValue(step)
    except Exception as e:
        print "step"
        print e