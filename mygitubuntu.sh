#!/bin/sh
cd /home/memo/AI/pythonproj
sudo git pull
git add *
sudo git commit -a
#sudo git commit -m "made changes"
git push origin master
