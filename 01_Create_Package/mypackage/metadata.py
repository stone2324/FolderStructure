import sys, os
import json
import datetime as dt

def is_interactive():
    if len(sys.argv) == 0:
        return False
    return not os.path.isfile(sys.argv[0])


def get_from_script(script_fpath):

    metadata_dict = {}
    metadata_dict["StartTime"] = dt.datetime.now().isoformat()
    metadata_dict["IsInteractive"] = is_interactive()
    metadata_dict["ScriptFilePath"] = script_fpath

    return metadata_dict


def write_to_file(file_path, data):

    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)
