import sys
import constants

DEBUG = constants.DEBUG

# Print a message to the logs.
def log(message):
    if DEBUG:
        print str(message)
        sys.stdout.flush()