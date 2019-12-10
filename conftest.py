import os, sys
from os.path import join

lambda_dir = join(os.path.dirname(os.path.abspath(__file__)), 'hello_world')
sys.path.append(lambda_dir)