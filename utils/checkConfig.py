import os
import sys
from utils import my_print

p = my_print

errors = {0: 'OK',
          1: 'Error in config file'}


def check_config(cfg_path):
    if os.path.exists(cfg_path):
        p.cout("[" + sys._getframe().f_code.co_name + "] | OK : found logging config at '" + cfg_path + "'")
    else:
        p.cerr("[" + sys._getframe().f_code.co_name + "] | Error no logging config found at '" + cfg_path + "' !")
        exit(errors[1])
