#!/bin/bash

if [ "$1" == "install" ]
	then
		cd /tmp
		git clone https://github.com/KaiserBarbarossa/MyBrowse.git
		sudo cp /tmp/MyBrowse/mybrowse.py /usr/local/bin/
		mkdir ~/.config/mybrowse
		cp /tmp/MyBrowse/mybrowse.cfg ~/.config/mybrowse/mybrowse.cfg
	elif [ "$1" == "remove" ]
		then
			echo "MyBrowse wird entfernt..."
			sudo rm  /usrl/local/bin/mybrowse.py		
			read -p "Konfigruationsdateien des Benutzers auch entfernen?" del_config
			case "$del_config" in
					j|J|y|Y|"") echo "Konfigurationsdateien werden entfernt..."
									rm -R ~/.config/mybrowse/
						;;
					n|N) echo "Konfigurationsdateien werden nicht entfernt"
						;;
					*) echo "Unbekanntes Parameter - Konfigurationsdateien werden nicht entfernt"
						;;
			esac
	elif [ "$1" == "upgrade" ]
		then
			sudo rm /usr/local/bin/mybrowse.py
			git clone https://github.com/KaiserBarbarossa/MyBrowse.git /tmp/MyBrowse
			sudo cp /tmp/MyBrowse/mybrowse.py /usr/local/bin/
	else
		echo "Kein Argument übergeben. Führe Installation aus."
		cd /tmp
		git clone https://github.com/KaiserBarbarossa/MyBrowse.git
		sudo cp /tmp/MyBrowse/mybrowse.py /usr/local/bin/
		mkdir ~/.config/mybrowse
		cp /tmp/MyBrowse/mybrowse.cfg ~/.config/mybrowse/mybrowse.cfg
fi
