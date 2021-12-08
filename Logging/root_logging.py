import logging
import functools
from functools import wraps
import numpy as np
import pandas as pd


ERROR = 40
WARNING = 30
INFO = 20
DEBUG = 10

loggingERROR = {'ERROR':ERROR,
                'WARNING':WARNING,
                'INFO':INFO,
                'DEBUG':DEBUG}



def create_logger(name = False, debug = False, logs_filename=False):

    """ Build a logger with a name 
           
        Args:
            name (str) : the name of the logger
            debug (bool) : if true, log level is set to Debug
            logs_filename (bool) : if filename, logs are store in file with name logs_filename
         
        Return:
            logging.logger
    """    

    level = ''
    if debug == True:
        level = 'DEBUG'
    else:
        level = 'WARNING'
        
    #create a logger object
    if not name:
        logger = logging.getLogger('exc_logger')
        if logs_filename:
            logfile = logging.FileHandler(logs_filename)
    else :
        logger = logging.getLogger(__name__)
        if logs_filename:
            logfile = logging.FileHandler(logs_filename)
        logfile = logging.FileHandler('logs.log')
    logger.setLevel(level)    
    
    #formatter and handler
    fmt = '%(levelname)s:%(asctime)s:%(message)s, In %(name)s file , In line : %(lineno)d'
    formatter = logging.Formatter(fmt)
    logfile.setFormatter(formatter)
    logger.addHandler(logfile)

    return logger


def exception(logger, DEBUG):  
    
    """ Logging decorator for functions  
           
        Args:
            logger (logging.logger) : the file logger         
        Return:
            decorate function with logging features
    """ 

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            if DEBUG:
                try:
                    return func(*args, **kwargs)
                except:
                    issue = "exception in "+func.__name__+"\n"
                    issue = issue+"-------------------------\
                    ---------------------------------------\n"
                    logger.exception(issue)
            else:
                return func(*args, **kwargs)
        
        wrapper.__doc__ = func.__doc__ if func.__doc__ else ""
        wrapper.__doc__ += "\n@about: keep trace of exception in a log file\n"
        return wrapper
    
    return decorator



if __name__=='__main__':
    print('.Create Logger')
    logger = create_logger('main')
    DEBUG = True
    @exception(logger, DEBUG)
    def divideStrByInt():
        return "Aadil"/7
    divideStrByInt()
    print('.Catching exception in logs.log file')