#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Assignment - mini project
# take a folder which consist of different files 
# based on the extention using the program create folders
# move the respective extention files to the folders

'''
folder : test.pdf, test.doc, test.mp4, test.mp3, test.txt

new folder based on files :
 pdf, doc, mp4,mp3,txt

pdf : test.pdf
doc: test.doc ...
'''


# In[1]:


import os


# In[2]:


#printing files from folder i.e. Demo.
path = "C://Users//Saif//Desktop//Demo"
dir_list = os.listdir(path)
print(dir_list)


# In[3]:


#creating folder according to the files which is present in Demo folder..
for i in dir_list:
#     print(i)
    parent_dir = "C://Users//Saif//Desktop//"
    path = os.path.join(parent_dir, i[-3:])
    os.mkdir(path)


# In[4]:


import shutil


# In[5]:


source = "C://Users//Saif//Desktop//Demo"
destination1 = "C://Users//Saif//Desktop//txt"
destination2 = "C://Users//Saif//Desktop//doc"
destination3 = "C://Users//Saif//Desktop//pdf"
destination4 = "C://Users//Saif//Desktop//mp4"
destination5 = "C://Users//Saif//Desktop//mp3"

# gather all files
allfiles = os.listdir(source)
#iterate on all files to move them to their  destination folder
for f in allfiles:
#     print(f[-3:])
    if f[-3:] == "doc":
        src_path = os.path.join(source, f)
        dst_path = os.path.join(destination2, f)
        shutil.move(src_path, dst_path)
    elif f[-3:] == "mp3":
        src_path = os.path.join(source, f)
        dst_path = os.path.join(destination5, f)
        shutil.move(src_path, dst_path)
    elif f[-3:] == "mp4":
        src_path = os.path.join(source, f)
        dst_path = os.path.join(destination4, f)
        shutil.move(src_path, dst_path)
    elif f[-3:] == "pdf":
        src_path = os.path.join(source, f)
        dst_path = os.path.join(destination3, f)
        shutil.move(src_path, dst_path)
    else:
        src_path = os.path.join(source, f)
        dst_path = os.path.join(destination1, f)
        shutil.move(src_path, dst_path)

