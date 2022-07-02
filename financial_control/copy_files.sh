#!/usr/bin/zsh

prev_dir=~/Downloads/
new_dir=~/Documents/extratos

cd $prev_dir
for file in *
do
    if [ "${file: 0:7}" = "Extrato" ]; 
    then 
        echo $prev_dir$file 
        mv $prev_dir$file $new_dir
    fi
done

       