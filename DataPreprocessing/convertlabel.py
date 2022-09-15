from dataclasses import replace
import json
import os
import re
import glob
def coco_to_yolo():
   
    
    json_files = glob.glob('C:/Users/onyeo/Pictures/Labels/*.json')
    for frames in json_files:
        with open(frames,'r') as fff:
            final_annots = json.load(fff)

        for frame_name in final_annots['shapes']:
            d = re.sub(r"\s+", "", frame_name['label'])
            frame_name['label'] = frame_name['label'].replace(frame_name['label'],d)
            print(frame_name['label'])
        with open(frames, 'w') as outfile:
            json.dump(final_annots, outfile)
                
    # anno_file  = os.path.join('./Labels/Frame_158.json')
    

    # with open(anno_file,'r') as fff:
    #     final_annots = json.load(fff)

    # for frame_name in final_annots['shapes']:

    #     d = re.sub(r"\s+", "", frame_name['label'])
    #     frame_name['label'] = frame_name['label'].replace(frame_name['label'],d)
    #     print(frame_name['label'])
        
    # with open(anno_file, 'w') as outfile:
    #     json.dump(final_annots, outfile)
coco_to_yolo()