#!/bin/bash

cd /tmp
git clone https://github.com/KaiserBarbarossa/MyBrowse.git
sudo cp /tmp/MyBrowse/mybrowse.py /usr/local/bin
mkdir ~/.config/mybrowse
cp /tmp/MyBrowse/mybrowse.cfg ~/.config/mybrowse/mybrowse.cfg