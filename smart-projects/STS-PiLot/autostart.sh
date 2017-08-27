#!/bin/bash
# Autodetect username
USER=$(stat -c '%U' $0)
# Uncomment following line to manually configure username
#USER="yourname"
# Absolute path to this script.
SCRIPT=$(readlink -f $0)
# Absolute path this script is in.
SCRIPTPATH=$(dirname $SCRIPT)
su -c "python $SCRIPTPATH/app.py >/dev/null 2>&1 &" $USER 


