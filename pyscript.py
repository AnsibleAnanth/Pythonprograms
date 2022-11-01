#! /usr/bin/env python3
import os
if os.path.isdir("/tmp"):
    print ("/tmp is directory")
else:
    print ("/tmp is not a directory")