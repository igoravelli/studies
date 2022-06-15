#!/usr/bin/zsh

prev_dir=/mnt/c/Users/rebuz/Documents/raw_extratos/
new_dir=/home/igorregly/estudos/financial_control/extratos

cd $prev_dir
for file in *
do
    if [ "${file: 0:7}" = "Extrato" ]; 
    then 
        echo $prev_dir$file 
        cp $prev_dir$file $new_dir
    fi
done

       