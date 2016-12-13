import warnings

warnings.warn("please use 'util.deb822' instead", DeprecationWarning,
              stacklevel=2)

from util.deb822 import *
