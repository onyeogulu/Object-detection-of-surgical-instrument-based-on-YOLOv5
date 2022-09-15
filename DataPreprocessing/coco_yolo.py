import json
import os

def coco_to_yolo():
    inputTags = ["Crocodilegrasper","Yohangrasper","HookDiathermy","Marylandgrasper","Clipper","Scissors","Bagholder","Trocar"]
    anno_file  = os.path.join('C:/Users/onyeo/Pictures/Planet9/Pilot2data.json')

    with open(anno_file,'r') as fff:
        final_annots = json.load(fff)
    
    for frame_name in final_annots['frames']:
        if len(final_annots['frames'][frame_name])>0:
            txt_f_name = frame_name[:-4]
            with open('./Planet9/labels/'+txt_f_name+'.txt', 'w') as f:
                for item in final_annots['frames'][frame_name]:

                    
                    width = item['width']
                    height =item['height']
                    x1 = item['x1']
                    x2 = item['x2']
                    y1 = item['y1']
                    y2 = item['y2']
                    label_ind = inputTags.index(item['tags'][0])
                    yolox1 = ((x1 + x2)/2)/width
                    yoloy1 = ((y1 + y2)/2)/height
                    yolox2 = (x2 - x1)/width
                    yoloy2 = (y2 - y1)/height

                    f.write('{:d} {:8f} {:8f} {:8f} {:8f} \n'.format(label_ind,yolox1,yoloy1,yolox2,yoloy2))
            f.close()

coco_to_yolo()