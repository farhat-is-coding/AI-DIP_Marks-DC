def run_model(current_path, img_input):
    # cloning the yolov5 repo
    # only needs to be run once
    # import subprocess

    # # Run the "git clone" command
    # subprocess.run(['git', 'clone', 'https://github.com/ultralytics/yolov5.git'])

    # making the repo our working directory (in cmd)
    # change as necessary!!!

    import os
    os.chdir(current_path + '/yolov5')

    # also needs to be run only once to satisfy requirements
    # subprocess.run(['pip', 'install', '-r', 'requirements.txt'])

    print("")

    # imports
    import torch
    import torchvision
    from PIL import Image
    import cv2
    import numpy as np

    # Load the YOLOv5 model
    print(os.getcwd()) # gets the current working directory

    # getting the path - to allow the app to run on any machine
    parent_dir = os.path.dirname(os.getcwd()) 
    print(f"-------------\n{parent_dir}\n---------------")
    model_name = parent_dir + "/best.pt" 

    # loading the model into a pytorch object
    model = torch.hub.load(os.getcwd(), 'custom', source='local', path = model_name, force_reload = True)
    print("")

    # Prepare the input image
    img_name = img_input # will use this below

    # img_path = f'{parent_dir}/{img_name}'
    img = Image.open(img_name) 

    # running the model on the image
    results = model(img) # returns batch of images
    # results.save()
    crops = results.crop(save=True)  # cropped detections dictionary


    # listing where the processed image is stored
    folder_path = 'runs/detect'
    subfolders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]   
    print(subfolders)
    latest_subfolder = max(subfolders, key=lambda x: os.path.getctime(os.path.join(folder_path, x)))    
    print(latest_subfolder)
    image_path = folder_path+'/'+latest_subfolder 
    print(image_path)



    # listing where the cropped images are stored
    crop_images_path = image_path+'/crops' 
    print(crop_images_path)

    img_name = os.path.basename(img_name) # getting the image name from the path
    crop_subfolders = [f for f in os.listdir(crop_images_path) if os.path.isdir(os.path.join(crop_images_path, f))]   

    print(crop_subfolders)
    # marks_box
    marks_box_path = f"{crop_images_path}/{crop_subfolders[0]}/{img_name}"
    roll_no_box_path = f"{crop_images_path}/{crop_subfolders[1]}/{img_name}"
    subject_name_path = f"{crop_images_path}/{crop_subfolders[2]}/{img_name}"

    print(marks_box_path)
    print(roll_no_box_path)
    print(subject_name_path)

    
    return marks_box_path, roll_no_box_path, subject_name_path