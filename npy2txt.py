import matplotlib.pylab as plt
import numpy as np
from PIL import Image
import random
import json
from collections import OrderedDict

MAX_X = 1200
MAX_Y = 720
'''
npy 파일을 txt파일 변환하는 코드

'''
NPY_FOLDER = 'npyfiles/'
SAVE_FOLDER = 'data'
def pasta_img(origin_img, num_i):
    sizex = random.randint(28, 700)
    sizey = random.randint(28, 700)
    x = random.randint(0, MAX_X-sizex)
    y = random.randint(0, MAX_Y-sizey)

    i = num_i.reshape(28,28)
    im = Image.fromarray(i)
    resize_image = im.resize((sizex,sizey))
    new_img.paste(resize_image, (x,y, x+sizex, y+sizey))
    return x,y, sizex, sizey
'''
이미지 resize나 이미지 합성을 확인하기 위한 코드
'''


nps = np.load(NPY_FOLDER+'house.npy')
file_data = OrderedDict()

f = open("house.txt", 'w')
print(nps[0])
for i in range(1000):
    cnt = random.randint(1,3)
    file_name = str(i) + '.jpg'
    new_img = Image.new("RGB", (MAX_X, MAX_Y))
    for j in range(cnt):
        randomi = random.randint(1, len(nps))
        x, y, sizex, sizey  = pasta_img(new_img, nps[randomi])
        inputstr = (SAVE_FOLDER+"/"+file_name)+","+str(x)+","+str(y)+","+str(x+sizex)+","+str(y+sizey)+",house\n"
        f.write(inputstr)
    new_img.save(SAVE_FOLDER+"/"+file_name)
    
    # file_data[file_name] = inputd
    
    
# with open(SAVE_FOLDER+'/train/via_region_data.json', 'w', encoding='utf-8') as make_file:
    # json.dump(file_data, make_file, ensure_ascii=False, indent="\t")



# file_data = OrderedDict()

# for i in range(8, 10):
#     file_name = str(i) + '.jpg'
#     new_img = Image.new("RGB", (MAX_X, MAX_Y))
#     x, y, sizex, sizey  = pasta_img(new_img, nps[i])
#     new_img.save(SAVE_FOLDER+"/"+"val/"+file_name)
    
#     inputd = OrderedDict()
#     inputd['fileref'] = ""
#     inputd['filename'] = file_name
#     inputd['base64_img_data'] = ""
#     inputd['file_attributes'] = OrderedDict()
#     inputd['regions'] = {
#         "0":{
#             "shape_attributes": {
#                 "name": "polygon",

#                 'all_points_x': [x, x+sizex, x+sizex, x],
#                 'all_points_y': [y, y, y+sizey, y+sizey]},
#                 # "x": x, 
#                 # "y": y, 
#                 # "width": sizex, 
#                 # "height": sizey},
#                 "region_attributes": {}
#             }
#         }
    
#     file_data[file_name] = inputd
    
    
# with open(SAVE_FOLDER+'/val/via_region_data.json', 'w', encoding='utf-8') as make_file:
#     json.dump(file_data, make_file, ensure_ascii=False, indent="\t")


# cnt = 1
# for i in nps:
#     new_img = Image.new("RGB", (1200, 720))
#     pasta_img(new_img, 



#     # im.show()
#     # im.save('eye.bmp')
#     if cnt == 10:
#         break