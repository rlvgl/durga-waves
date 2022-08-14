import os
path = "/Users/sohum/Desktop/durga-waves/assets/pictures"
dir_list = os.listdir(path)
 
# print("Files and directories in '", path, "' :")
for pic in dir_list:
    html = '<div class="col-md-4"><div class="card-box-a card-shadow"><div class="img-box-a"><img src="/assets/pictures/' + pic + '" alt="" class="img-a img-fluid" /> </div> </div> </div>'
    print(html)
    # print(pic)