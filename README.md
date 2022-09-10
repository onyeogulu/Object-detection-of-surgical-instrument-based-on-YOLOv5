# Object-detection-of-surgical-instrument-based-on-YOLOv5

The following steps shouls be taking to reproduce the results in our work. 

1. Clone our github repository containg the YOLOv5 and YOLOv7 folder. 
2. Download our novel annotated endoscope dataset from this [link](https://drive.google.com/drive/folders/1ruH7B-IMPqNeBkWail2NruXSmMAKCcpy?usp=sharing)
3. For each refinement of our YOLOv5, we wrote a .yaml file that contains the instructions on how the model will be trianed and each refinement .ymal file is saved in the [models](https://github.com/onyeogulu/Object-detection-of-surgical-instrument-based-on-YOLOv5/tree/main/YOLOv5/models) folder inside the YOLOv5 folder.  
4. To train each YOLOv5 model, follow the instructions on how to train the YOLOv5 model documented in the Readme file inside the YOLOV5 folder.
5. To train our benchmark models, we wrote .yaml files that contains the instrustions on how to train our models. 
6. To train our YOLOv7 bencmark model used the instructions documented in the Readme file inside the YOLOv7 folder. 
7. New .yaml file for YOLOR and Scaled_YOLOv4 are written and saved in [here](https://github.com/onyeogulu/Object-detection-of-surgical-instrument-based-on-YOLOv5/tree/main/YOLOV7/cfg/training) in the YOLOv7 folder which are used to train our YOLOR and Scaled_YOLOv4 benchmark models.
8. New .yaml file for YOLOv3-SPP are written and saved in [here](https://github.com/onyeogulu/Object-detection-of-surgical-instrument-based-on-YOLOv5/tree/main/YOLOv5/models) in the YOLOv5 folder is used to train our YOLOv3-SPP benchmark model.
