# Program              : copyusb
# Author               : Ahmedur Rahman Shovon
# Description          : Copy connected USB media device to current script directory.
#                        DO NOT MISUSE IT FOR STEALING DATA.                    
# Date                 : 21/02/2017
# Version              : 1.0.1
# Tested OS            : Ubuntu (16.04 LTS)
# USB Drive Size (max) : 16GB

import string
import os
import subprocess
import sys
import glob
from datetime import datetime
import time
import inspect

mount_drive_dict = {}

def get_current_date_time():
    dt = datetime.now()
    current_time_str = dt.strftime("%Y-%m-%d_%H-%M-%S")
    return current_time_str

def copy_single_file(source, destination):
    flag = True
    try:
        cp_process = subprocess.Popen(["cp", "-R", source, destination])
        cp_output, cp_error = cp_process.communicate()
        cp_status = cp_process.wait()
    except Exception as error:
        flag = str(error)
    return flag

def get_last_modified_time(current_path):
    flag = None
    try:
        stat_process_output = subprocess.check_output(["stat", "-c", "%y", current_path])
        flag = stat_process_output.decode("ascii")[:-1]
    except Exception as error:
        flag = str(error)
    return flag
    

def make_directory(directory_name):
    flag = True
    try:
        subprocess.call(["mkdir", directory_name])
    except Exception as error:
        flag = str(error)
    return flag

def get_mount_detail():
    flag = True
    try:
        current_platform = str(sys.platform)
        current_platform = current_platform.lower()
        if 'linux' in current_platform:
            mount_str = str(subprocess.check_output(["df"]))
            mount_list = mount_str.split('\\n')
            mount_list = mount_list[1:]
            for single_mount in mount_list:
                single_mount_ar = single_mount.split()
                if len(single_mount_ar)<3:
                    continue
                current_path = single_mount_ar[-1]
                current_size = int(single_mount_ar[1])
                if 'media' in current_path:
                    single_drive_dict = {}
                    single_drive_dict["path"] = current_path
                    single_drive_dict["size"] = current_size
                    last_modified_time = 0                
                    current_label = ""
                    # current_size is in Kilo Bytes
                    # if size is greater than 16 GB then it is a drive
                    if current_size > 16777216 :                                  
                        current_label = "drive"
                    else:
                        current_label = "usb"
                        last_modified_time = get_last_modified_time(current_path)
                    single_drive_dict["label"] = current_label
                    single_drive_dict["copy_status"] = False                
                    if current_path in mount_drive_dict.keys() and current_label == "usb":
                        if mount_drive_dict[current_path]["copy_status"] == False:
                            single_drive_dict["time"] = last_modified_time
                            mount_drive_dict[current_path] = single_drive_dict
                        else:
                            old_modified_time = mount_drive_dict[current_path]["time"]
                            if old_modified_time != last_modified_time:
                                single_drive_dict["time"] = last_modified_time
                                mount_drive_dict[current_path] = single_drive_dict
                    elif current_path not in mount_drive_dict.keys():
                        single_drive_dict["time"] = last_modified_time
                        mount_drive_dict[current_path] = single_drive_dict
    except Exception as error:
        flag = str(error)
    return flag
                        
def copy_all_file_from_usb(current_script_dir):
    flag = []    
    try:
        for single_drive_key in mount_drive_dict.keys():
            single_drive = mount_drive_dict[single_drive_key]
            current_drive_label = single_drive["label"]
            current_drive_copy_status = single_drive["copy_status"]
            if current_drive_label == "usb" and current_drive_copy_status == False:
                current_drive_path = single_drive["path"]
                current_drive_size = single_drive["size"]                
                folder_time_str = get_current_date_time()
                usb_name = current_drive_path.split("/")[-1]
                destination = current_script_dir +"/"+ usb_name + "_" + folder_time_str
                mkdir_flag = make_directory(destination)
                if mkdir_flag == True:
                    file_list = glob.glob(current_drive_path+"/*")                    
                    for single_file in file_list:
                        source = single_file                
                        copy_flag = copy_single_file(source, destination)
                        if copy_flag != True:
                            raise ValueError("Failed to copy "+source)                    
                    mount_drive_dict[current_drive_path]["copy_status"] = True
                    flag.append(destination)
                else:
                    raise ValueError("Failed to create directory: "+destination)
    except Exception as error:
        return str(error)        
    return flag

def copy():
    frame, current_script_dir, line_number, function_name, lines, index = inspect.getouterframes(inspect.currentframe())[1]
    current_script_dir = os.path.dirname(current_script_dir)
    
    try:        
        flag_mount = get_mount_detail()
        if flag_mount == True:
            copy_return = copy_all_file_from_usb(current_script_dir)
            if type(copy_return) is list:
                return copy_return
            else:
                raise ValueError(copy_return)
        else:
            raise ValueError(flag_mount)
    except Exception as error:
        return str(error)
    
