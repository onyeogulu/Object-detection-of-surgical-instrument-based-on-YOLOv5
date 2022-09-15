import os
from os import path
import shutil

source_path = r"C:\Users\onyeo\Pictures\Subset_1\LABELS_"

# with open('readme.txt', 'w') as f:
#     for count, filename in enumerate(os.listdir(source_path)):
#         out_str = str(filename.splitext) + ' 0\n'
#         f.write('readme')
with open('readme.txt', 'w') as f:
    for count, filename in enumerate(os.listdir(source_path)):
        name = filename.split(".")[0] + '\n'
        f.write(name)
    