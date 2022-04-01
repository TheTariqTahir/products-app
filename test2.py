import glob
import os
home_path = os.getcwd()
# path  = 'src/shirts/'
path  = os.path.join(home_path,'src','shirts')
print(path)
contents_list = (glob.glob(str(path)+'*'))
print(contents_list)