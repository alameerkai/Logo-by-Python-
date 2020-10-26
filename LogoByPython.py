import os
from  PIL import Image 

Logo_name = input('Enter the logo Name with Extension')
New_folder_name = input('input the new folder name : ')
 
logo_image = Image.open(Logo_name) 
logo_width , logo_height = logo_image.size

if not os.path.exists(New_folder_name):
    os.mkdir(New_folder_name)


for filename in os.listdir('.'): #Put it inside the file 

    if not(filename.endswith('.png') or filename.endswith('.jpg') or filename == Logo_name):
        continue
    img = Image.open(filename)
    width , height = img.size


    img.paste(logo_image , (width-logo_width , height-logo_height))
    img.save(os.path.join(New_folder_name,filename))
    print(f'done image : {filename}')

print("DONE")
