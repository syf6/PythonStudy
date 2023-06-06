import os
import cv2

# the path of the image 
folder_path = r"/path you want"

# initialize a new image list
image_list = []

# traverse all the images in the file
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        # check whether the files are in images' formats
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            try:
                # use open CV to read image
                image = cv2.imread(file_path)
                image_list.append(image)
            except Exception as e:
                print("cannot read the image in ", file_path)

# The image list now contains all image objects in the folder
# The list of images can be manipulated, eg accessed, modified or further processed
for image in image_list:
    # just show the images in the list
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
