import os
import shutil

"""
    Removing files if not needed after template creation.
"""

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


# Remove signature.png

create_signature = '{{cookiecutter.Signature}}' == 'y'

if not create_signature:
    remove('signature.png')
