import os
import inspect

project_folder_path = os.path.abspath(os.path.join(inspect.getfile(inspect.currentframe()), os.pardir, os.pardir))
src_folder_path = os.path.join(project_folder_path, 'src')
resrc_folder_path = os.path.join(project_folder_path, 'resrc')