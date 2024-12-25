import os
directory_path='users'

content=os.listdir(directory_path)

for items in content:
    print(items)