import logging



if __name__=='__main__':
    file_name = __name__
    print(file_name)
    #process, name
    logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='a', format='%(name)s - %(asctime)s - %(levelname)s - %(message)s')
    # logging.debug('This is a debug message')
    # logging.info('This is an info message')
    # logging.warning('This is a warning message')
    # logging.error('This is an error message')
    logging.critical('This is a critical message')

    a = 5
    b = 0
    try:
        c = a / b
    except Exception as e:
        logging.exception(f"Exception occurred in file {file_name}", exc_info=True)


    logger = logging.getLogger('new_logger')
    logger.warning('This is a warning')
