import matplotlib.pyplot as plt
import numpy as np
import os
import glob
import shutil

path = r'C:\Users\onyeo\Pictures\BodyCam_data'

def main():
    # new folder to store files 
    folder = r"C:\Users\onyeo\Pictures\CleanBodyCam"
    path = r'C:\Users\onyeo\Pictures\BodyCam_data'

    images  = r'C:\Users\onyeo\Pictures\Subset\Images'
    label = r'C:\Users\onyeo\Pictures\Planet9\Pilot_2_Annotated\Newfolder\test\images'
    json_list = []
    # loop through the json files 
    json_files = glob.glob('C:/Users/onyeo/Pictures/Planet9/Pilot_2_Annotated/output/test/*.jpg')
    print(len(json_files))
    for json in json_files:
        shutil.copy(json, label)

    #     shutil.move(json, folder + json.split("\\")[-1])
    # # [-1] takes the last part of the path
    # # .strip removes .TXT from the file name 
    #     json_name = json.split("\\")[-1].strip('.json')
    #     json_list.append(json_name)
    #     print(json_list)
    #     #print(jpg_name)
    # for jpg in jpg_files:
    #     jpg_name = jpg.split("\\")[-1].strip('.jpg')
    #         #print(json_name)
    #         #Check if the wav_name and txt_name are the same.  
    #         #There is no check for case.    
    #     if jpg_name in json_list:
    #         shutil.move(jpg, folder)
    # print(json_list)
if __name__ == '__main__':
    main()