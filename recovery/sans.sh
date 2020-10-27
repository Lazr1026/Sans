#!/bin/bash
cd /home/lucas/Documents/Sans
git reset #this is not a very elegant or perfect way to do it, but I suck at Git and also do not care
git pull
systemctl restart sans
systemctl restart sansrecovery
