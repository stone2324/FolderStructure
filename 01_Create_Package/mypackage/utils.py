
import importlib.util
import os

def load_module(script_fpath, function_name):
    """
    Load a Python module from the given file path and return the specified function.
    """
    module_name = os.path.basename(script_fpath).split('.')[0]
    spec = importlib.util.spec_from_file_location(module_name, script_fpath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if hasattr(module, function_name):
        return getattr(module, function_name)
    else:
        print(f"Module {module.__name__} has no {function_name}() function.")
        return None
    