import json
import os
from glob import glob


# convert labelme json to DOTA txt format

def custombasename(fullname):
    return os.path.basename(os.path.splitext(fullname)[0])


IN_PATH = r'C:\Users\onyeo\Pictures\Subset_1\Labels'
OUT_PATH = r'C:\Users\onyeo\Pictures\Subset_1\DotaLabels'

file_list = glob(IN_PATH + '/*.json')


for i in range(len(file_list)):
    
    with open(file_list[i]) as f:
        label_str = f.read()
        
        label_dict = json.loads(label_str)  # json文件读入dict

        # 输出 txt 文件的路径
        out_file = OUT_PATH + '/' + custombasename(file_list[i]) + '.txt'

        # 写入 poly 四点坐标 和 label
        fout = open(out_file, 'w')
        out_str = ''
        for shape_dict in label_dict['shapes']:
            points = shape_dict['points']
            for p in points:
                out_str += (str(p[0]) + ' ' + str(p[1]) + ' ') 
            out_str += shape_dict['label'] + ' 0\n'
            print(out_str)
        
        fout.write(out_str)
        fout.close()
    print('%d/%d' % (i + 1, len(file_list)))