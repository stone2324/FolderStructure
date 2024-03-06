from . import mylogger
from . import utils


def _run_module_function(script_fpath, function_name, logger, *args, **kwargs):

    # Load Module
    module_function = utils.load_module(script_fpath, function_name)

    # Run function
    if module_function:
        logger.info(f"Starting execution of {script_fpath} {function_name}")

        kwargs['script_fpath'] = script_fpath

        result = module_function(*args, **kwargs)
        logger.info(f"Result = {result}")
        logger.info(f"Finished execution of {script_fpath} {function_name}")
    else:
        logger.warning(f"Unable to load function {function_name} from {script_fpath}")


def run(script_fpath: str, function_name: str, *args, **kwargs):
    """Main entry point for the script."""
    log_file = r"D:\Python\Scheduler\log.txt"
    logger = mylogger.configure_logging(log_file)
    _run_module_function(script_fpath, function_name, logger, *args, **kwargs)
