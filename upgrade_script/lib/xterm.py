from __future__ import print_function
class XTerm:
    """XTerm: Support print to stdout with difference type of messages.
        Type: (info, warn, success, error)
   
    """
    HEADER = '\033[93m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    BLACK = '\033[30m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    
    def __init__(self):
        pass

    @staticmethod
    def print(message, *others, **keywords):
        ops={
            'info': XTerm.info,
            'error' : XTerm.error,
            'success': XTerm.success,
            'warn': XTerm.warn,
            'debug': XTerm.debug,
        }
        type='info'
        if 'type' in keywords:
            type=keywords['type']
            
        ops[type](message, others)
        
    @staticmethod
    def info(message, *others):
        XTerm.__print_head('[INFO]', message, others)
    @staticmethod
    def debug(message, *others):
        XTerm.__print_head(XTerm.BOLD + '[DEBUG]', message, others)
    @staticmethod
    def success(message, *others):
        XTerm.__print_head(XTerm.OKGREEN+'[INFO]', message, others)

    @staticmethod
    def error(message, *others):
        XTerm.__print_head(XTerm.FAIL + '[ERROR]', message, others)
    @staticmethod
    def warn(message, *others):
        XTerm.__print_head(XTerm.WARNING + '[WARN]', message, others)

    @staticmethod
    def __print_head(head, message, others):
        
        if not head is None:
            print(head, end='') # print "head" without nextline
        print("{}".format(message),end='') # print "message" without nextline
        
        for item in others:
            print('{}'.format(item), end='')

        # print end message format and go next line
        print(XTerm.ENDC)
        
    @staticmethod
    def print_title(message, *others):
        XTerm.__print_head(XTerm.YELLOW + '>', message, others)
    @staticmethod    
    def print_in_red(message, *others):
        XTerm.__print_head(XTerm.RED, message, others)
    @staticmethod
    def print_in_yellow(message, *others):
        XTerm.__print_head(XTerm.YELLOW, message, others)
    @staticmethod
    def print_in_green(message, *others):
        XTerm.__print_head(XTerm.GREEN, message, others)
    @staticmethod
    def print_in_purple(message, *others):
        XTerm.__print_head(XTerm.PURPLE, message, others)
    @staticmethod
    def print_in_cyan(message, *others):
        XTerm.__print_head(XTerm.CYAN, message, others)
        