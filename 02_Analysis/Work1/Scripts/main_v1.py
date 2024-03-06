import mypackage
import os

#------------------------
# Main Function
#------------------------

def main(input_dir, output_dir, template_fpath, script_fpath=None):
    
    print(script_fpath)

    metadata_dict = mypackage.metadata.get_from_script(script_fpath)
    
    print("I am running main_v1.py")
    
    os.makedirs(output_dir, exist_ok=True)
    metadata_fpath = fr"{output_dir}\metadata.txt"
    print(metadata_fpath)

    mypackage.metadata.write_to_file(metadata_fpath, metadata_dict)

#-------------------------------
# Local testing
#-------------------------------

if __name__ == "__main__":

    base_dir = r"D:\Python\work1"

    template_fname = "template v1.xlsb"
    results_folder = r"BAU\2024_03\v1"
    
    input_dir = ""

    process_kwargs = {
    'input_dir': input_dir,
    'template_fpath': fr"{base_dir}\Scripts\{template_fname}",
    'output_dir': fr"{base_dir}\Results\{results_folder}",
    }
    
    main(**kwargs)
