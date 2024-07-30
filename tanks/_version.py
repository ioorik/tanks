# MAJOR ----------
# 0 = beta/alpha code
# incremented any time you change the API that may break backwards compatibility
# in a fairly major way
MAJOR = 0
# MINOR ------------
# recommend using datetime info to show last update as part of a version
# but the other option is to manually rev, and put the revision in the build
MINOR = 1
# BUILD ------
# either make this a manual number to increment or use the SVN revision
# (which increments like crazy...hopefully it doesn't drive users a bit crazy)
BUILD = "0"  # or __revision__
__version__ = f"{MAJOR}.{MINOR}.{BUILD}"
