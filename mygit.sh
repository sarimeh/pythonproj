#!/bin/sh
cd /c/pythongit
git pull
git add .
git commit -am "made changes"
git push origin master

echo Press Enter...
read
