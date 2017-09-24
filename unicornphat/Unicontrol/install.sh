#!/bin/bash

echo "The Unicontrol easy installer"
echo "To change downloads dir, cancel install and cd to the new dir."

echo "Are you sure you want to continue?"
read ANS
echo "Answered $ANS!"
if [ "x$ANS" = "xyes" ] ; then
   echo "starting installer"
   wget https://raw.githubusercontent.com/flash76/Unicontrol/master/followup.sh
   echo "gaining superuser priveleges. you may need to enter your password."
   sudo ./followup.sh
fi
