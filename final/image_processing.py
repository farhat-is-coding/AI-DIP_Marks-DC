# IMAGE PROCESSING TO SEPARATE AND SAVE INDIVIDUAL BOXES
def image_processing(current_path, box_path):
    # import statements
    import cv2
    import numpy as np
    import os


    # !pip install opencv-python

    # Read the image
    try:
        img = cv2.imread(box_path, 0)
    except:
        print("cannot open file")
        # exit the program
        print("----------------------\nEXITING - CANNOT OPEN FILE\n----------------------")
        exit()

    # Thresholding the image
    (thresh, img_bin) = cv2.threshold(
        img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # Invert the image
    img_bin = 255-img_bin
    cv2.imwrite("image_bin.jpg", img_bin)

    # making kernels

    # Defining a kernel length
    kernel_length = np.array(img).shape[1]//80
    # converting image to a numpy array
    # shape() gives dimensions
    # shape[1] = the width of the image
    # integer division by 80 to get the size of the kernel we want


    # A verticle kernel of (1 X kernel_length), which will detect all the verticle lines from the image.
    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_length))
    # cv2.MORPH_RECT defines the shape of the kernel as rectangular

    # A horizontal kernel of (kernel_length X 1), which will help to detect all the horizontal line from the image.
    hori_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_length, 1))

    # A kernel of (3 X 3) ones.
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    # Morphological operation (opening) to detect vertical lines from an image

    # NOT USING THIS
    # img_temp1 = cv2.erode(img_bin, vertical_kernel, iterations=3)
    # verticle_lines_img = cv2.dilate(img_temp1, vertical_kernel, iterations=3)
    # cv2.imwrite("verticle_lines.jpg",verticle_lines_img)

    vertical_img = cv2.morphologyEx(
        img_bin, cv2.MORPH_OPEN, vertical_kernel, iterations=3)
    cv2.imwrite("./vertical_lines.jpg", vertical_img)

    # Morphological operation to detect horizontal lines from an image
    #  NOT USING THIS
    # img_temp2 = cv2.erode(img_bin, hori_kernel, iterations=3)
    # horizontal_lines_img = cv2.dilate(img_temp2, hori_kernel, iterations=3)
    # cv2.imwrite("horizontal_lines.jpg",horizontal_lines_img)

    horizontal_img = cv2.morphologyEx(
        img_bin, cv2.MORPH_OPEN, hori_kernel, iterations=3)
    cv2.imwrite("./horizontal_lines.jpg", horizontal_img)


    # Weighting parameters, this will decide the quantity of an image to be added to make a new image.
    alpha = 0.5
    beta = 1.0 - alpha
    # This function helps to add two image with specific weight parameter to get a third image as summation of two image.
    img_final_bin = cv2.addWeighted(vertical_img, alpha, horizontal_img, beta, 0.0)

    # applying erosion
    img_final_bin = cv2.erode(~img_final_bin, kernel, iterations=2)
    (thresh, img_final_bin) = cv2.threshold(
        img_final_bin, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cv2.imwrite("img_final_bin.jpg", img_final_bin)

    # Find contours for image, which will detect all the boxes
    contours, hierarchy = cv2.findContours(
        img_final_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #print(contours)
    # print(hierarchy)

    # saving all boxes as images
    idx = 0
    os.chdir(current_path)
    print(os.getcwd())
    # os.chdir('E:/University/Semester 6 - Spring 2023/Digital Image Processing/LabWork/dip_project/AI-DIP_Marks-DC/final/yolov5')

    # deleting everything from the results directory first 
    for filename in os.listdir('./results'):
        os.remove('./results/' + filename)

    for c in reversed(contours): # the first three detected are the full boxes (we don't need that)
            # Returns the location and width,height for every contour
            x, y, w, h = cv2.boundingRect(c)
            if (w < 180 and h < 180):
                idx += 1
                new_img = img[y:y+h, x:x+w]
                cv2.imwrite("./results/result"+str(idx) + '.png', new_img)
