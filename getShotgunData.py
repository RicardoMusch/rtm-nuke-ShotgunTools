def update():

    import nuke
    from datetime import datetime
    import os
    import sys

    try:
        sys.path.append(os.environ["SHOTGUN_API3"])
    except Exception as e:
        sys.path.append("F:/Archive/common_studio/Shotgun/_api/python-api")
    import shotgun_api3



    ########################################################################################################
    print " "

    try:
        import sgtk
        # get the engine we are currently running in
        current_engine = sgtk.platform.current_engine()
        # get hold of the shotgun api instance used by the engine, (or we could have created a new one)
        sg = current_engine.shotgun
        print "Connected to Shotgun...\n"
    except:
        import sg_connection
        # Connect to SG
        # sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)
        print "Connected to Shotgun...\n"


    ########################################################################################################
    print "Loading Functions"
    def getSGStatusFriendlyName(status_short_code):
        fields = ["name"]
        filters = [
        ['code', 'is', status_short_code ],
        #["id", "is", version_data.get("entity").get("id")]
        ]
        friendly_status = sg.find_one("Status", filters, fields)
        #print friendly_status
        return friendly_status.get("name")


    "Me"
    try:
        n = nuke.selectedNode()
    except Exception as e:
        print e
        n = nuke.thisNode()

    try:
        try:
            "Get Upstream Node"
            read = nuke.toNode(n.input(0)["name"].getValue())
        except:
            read = nuke.toNode(n["source_node"].getValue())
        print "Using Read:"+str(read["name"].getValue())
    except:
        nuke.message("Please connect to a node with a file knob or add the name in the input knob!")
        return


    "Filename to search Shotgun with"
    filename = os.path.basename(read["file"].getValue())

    print "Searching Shotgun for version data"
    fields = [ "code", "sg_status_list", "client_code", "entity", "sg_slate_notes", "project", "user", "description", "sg_version_type", "sg_tech_check_notes", "sg_tech_check_approved", "sg_editorial_status" ]
    filters = [ ["sg_path_to_frames", "contains", filename] ]
    version_data = sg.find_one('Version', filters, fields)
    #print version_data


    print "Searching Shotgun for entity data "
    fields = ["sg_status_list", "sg_head_in", "sg_tail_out", "sg_head_handle", "sg_tail_handle", "sg_cut_in", "sg_cut_out", "tank_name", "sg_sequence", "sg_episode"]
    filters = [
    #['project', 'name_contains', project],
    ["id", "is", version_data.get("entity").get("id")]
    ]
    entity_data = sg.find_one(version_data.get("entity").get("type"), filters, fields)
    #print entity_data

    
    print "Searching Shotgun for project data "
    fields = ["tank_name", "sg_fps"]
    filters = [
    ['name', 'contains', version_data.get("project").get("name")],
    #["id", "is", version_data.get("entity").get("id")]
    ]
    project_data = sg.find_one("Project", filters, fields)
    #print project_data


    #############################################################################
    "Processing Project data"
    try:
        n["tank_name"].setValue(project_data.get("tank_name"))
    except Exception as e:
        print e
    try:
        n["project_fps"].setValue(project_data.get("sg_fps"))
    except Exception as e:
        print e


    #############################################################################
    print "Processing Version data"
    try:
        n["project"].setValue(version_data.get("project").get("name"))
    except Exception as e:
        print e
    try:
        n["version_name"].setValue(version_data.get("code"))
    except Exception as e:
        print e
    try:
        n["client_version_name"].setValue(version_data.get("client_code"))
    except Exception as e:
        print e
    try:
        n["artist"].setValue(version_data.get("user").get("name"))
    except Exception as e:
        print e
    try:
        n["entity_type"].setValue(version_data.get("entity").get("type"))
    except Exception as e:
        print e
    try:
        entity_name = version_data.get("entity").get("name")
        n["entity_name"].setValue(entity_name)
    except Exception as e:
        print e
    try:
        field = "description"
        n[field].setValue(version_data.get(field))
    except Exception as e:
        print e
    try:
        n["slate_notes"].setValue(version_data.get("sg_slate_notes"))
    except Exception as e:
        print e
    try:
        n["version_type"].setValue(version_data.get("sg_version_type"))
    except Exception as e:
        print e
    try:
        field = "sg_tech_check_notes"
        n[field].setValue(version_data.get(field))
    except Exception as e:
        print e
    try:
        field = "sg_tech_check_approved"
        n[field].setValue(version_data.get(field))
    except Exception as e:
        print e
    try:
        field = "sg_editorial_status"
        n[field].setValue(version_data.get(field))
    except Exception as e:
        print e
    try:
        field = "sg_status_list"
        status = getSGStatusFriendlyName(version_data.get(field))
        n["sg_version_status_list"].setValue(status)
    except Exception as e:
        print e


    #############################################################################
    print "Processing Entity data"
    try:
        n["episode"].setValue(entity_data.get("sg_episode").get("name"))
    except Exception as e:
        print e
    try:
        n["sequence"].setValue(entity_data.get("sg_sequence").get("name"))
    except Exception as e:
        print e
    try:
        n["head_in"].setValue(str(entity_data.get("sg_head_in")))
    except Exception as e:
        print e
    try:
        n["tail_out"].setValue(str(entity_data.get("sg_tail_out")))
    except Exception as e:
        print e
    try:
        n["head_handle"].setValue(str(entity_data.get("sg_head_handle")))
    except Exception as e:
        print e
    try:
        n["tail_handle"].setValue(str(entity_data.get("sg_tail_handle")))
    except Exception as e:
        print e
    try:
        n["cut_in"].setValue(str(entity_data.get("sg_cut_in")))
    except Exception as e:
        print e
    try:
        n["cut_out"].setValue(str(entity_data.get("sg_cut_out")))
    except Exception as e:
        print e
    try:
        field = "sg_status_list"
        friendly_status = getSGStatusFriendlyName(entity_data.get(field))
        n["sg_entity_status_list"].setValue(friendly_status)
    except Exception as e:
        print e



    #############################################################################
    print "Finding Step"
    try:
        step = read["file"].getValue().replace("\\","/").lower()
        step = step.split(entity_name.lower())[1]
        step = step.split("/")[1]
        n["step"].setValue(step)
    except Exception as e:
        print e