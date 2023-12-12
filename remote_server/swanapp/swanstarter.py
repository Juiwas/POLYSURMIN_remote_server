from .models import SwanTask, SwanSubTask
import os
from django.conf import settings
import json
import os
import csv
import subprocess
# from itertools import product
from typing import Tuple
import shutil
import pathlib

from .swan import Swan

def copy_swan_files(swan_task):
    cur_dir = pathlib.Path(__file__).parent.resolve()
    src_path = os.path.join(cur_dir, 'app')
    #sub_task_dir = f"subtask_{swan_subtask.vel}_{swan_subtask.dir}"
    dst_path = os.path.join(settings.MEDIA_ROOT, 'swan-tasks', swan_task.hash)
    #os.makedirs(dst_path)
    shutil.copytree(src_path, dst_path)
    return dst_path


def get_swan_matrixes(swan_task):
    task_dir = os.path.join(settings.MEDIA_ROOT, 'swan-tasks', swan_task.hash)
    #os.makedirs(task_dir)
    copy_swan_files(swan_task)
    swan_subtasks = SwanSubTask.objects.filter(swan_task=swan_task)
    data = {}
    for i, swan_subtask in enumerate(swan_subtasks):
        data[f"{i}"] = {"velocity": swan_subtask.vel, "direction": swan_subtask.dir}

    s = Swan(task_dir)
    print(data)
    result = s.run(data)
    return result

        


        