import argparse
import sys
import os
def generate(args):
    directory=args.name
    parent_dir=os.getcwd()
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    os.chdir(path)
    os.mkdir("src")
    os.mkdir("models")
    os.mkdir("db")
    os.mkdir("routes")
    os.mkdir("config")
    f = open("app.py", "a")
    f.write("print('this is app.py write code for your project')")
    f.close()
    
    
if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--name',type=str,default="new project",help="Enter the name for the project")
    args=parser.parse_args()
    sys.stdout.write(str(generate(args)))

