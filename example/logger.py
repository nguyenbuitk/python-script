import os
import logging

def setup_logger(name, is_verbose):
    """
    Sets up a logger with both console and file handlers.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG if is_verbose else logging.INFO)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # File handler
    fh = logging.FileHandler(name + '.log')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger

def main():
    '''
    # Setup logger
    script_file_name = os.path.basename(__file__).split('.')[0]
    logger = setup_logger(script_file_name, is_verbose=True)

    # Example logging
    logger.info("Starting the script...")
    # ... rest of your main function logic ...
    logger.debug("This is a debug message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.info("Finishing the script.")
    '''

if __name__ == "__main__":
    main()
