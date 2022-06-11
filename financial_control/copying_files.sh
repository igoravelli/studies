prev_dir=/mnt/c/Users/rebuz_bvrnqpm/Downloads/
new_dir=/home/igoregly/automation_financial_management/copied_files/

cd $prev_dir
for file in *
do
    if [ "${file: 0:7}" = "Extrato" ]; 
    then 
        echo $file
        cp $prev_dir$file $new_dir
    fi
done

       