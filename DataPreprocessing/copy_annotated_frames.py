import json
import os
import shutil

anno_file  = os.path.join('C:/Users/onyeo/Pictures/Planet9/Pilot2data.json')

with open(anno_file,'r') as fff:
    final_annots = json.load(fff)

for frame_name in final_annots['frames']:
    if len(final_annots['frames'][frame_name])>0:
        shutil.copyfile("./Planet9/Pilot2data/"+frame_name, "./Planet9/images/"+frame_name)
    


