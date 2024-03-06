import mypackage

if __name__ == "__main__":
    
    base_dir = r"D:\Python\work1"
    
    script_name = "main_v1.py"

    template_fname = "template v1.xlsb"
    results_folder = r"BAU\2024_04\v1"

    script_kwargs = {
    'script_fpath': rf"{base_dir}\Scripts\{script_name}",
    'function_name': 'main',
    }

    process_kwargs = {
    'input_dir': "",
    'template_fpath': fr"{base_dir}\Scripts\{template_fname}",
    'output_dir': fr"{base_dir}\Results\{results_folder}",
    }
    
    mypackage.scheduler.run(**script_kwargs, **process_kwargs)
