#!/bin/bash

for i in $(ls -c1 /media/lab12/BK_WS/Carreras_Illumina)
do
	zip -r "/home/lab12/toBackUp/$i.zip" "/media/lab12/BK_WS/Carreras_Illumina/$i/"
	python3 /home/lab12/Desktop/Script_drive/script_drive/drive_upload.py "/home/lab12/toBackUp/$i.zip"
	echo "Carrera subida: $i" >> log.txt
	rm -r "/home/lab12/toBackUp/$i.zip"
	echo "ZIP eliminado: $i" >> log.txt
	rm -rf ~/.local/share/Trash/*

done

