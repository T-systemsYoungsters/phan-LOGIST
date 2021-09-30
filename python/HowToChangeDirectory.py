import os

path = os.getcwd()
print(path)
os.chdir('../')
print(path)

print('[change directory]')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print('getcwd:      ', os.getcwd())