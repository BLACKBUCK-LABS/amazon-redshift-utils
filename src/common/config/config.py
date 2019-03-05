import sys
import os

def get_env_val(var):
    if var in os.environ:
        return os.environ[var]
env = None
if len(sys.argv) > 1 and sys.argv[1] is not None:
    env = sys.argv[1]
else:
    if "ENV" in os.environ:
        env = os.environ['ENV']

if env == 'prod':
    from config_prod import *
elif env == 'preprod':
    from config_preprod import *
else:
    from config_local import *

