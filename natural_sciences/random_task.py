#!/usr/bin/env python

import os
from pathlib import Path
import importlib.machinery
import importlib.util
from random import choice

def walkpath(path):
    files = []
    for file in path.iterdir():
        if file.is_dir():
            files += walkpath(file)
        elif str(file).endswith("tasks.py"):
            files.append(file)
    return files

scriptdir = Path(os.path.dirname(os.path.realpath(__file__)))
tasks_file = choice(walkpath(scriptdir))

loader = importlib.machinery.SourceFileLoader("tasks", str(tasks_file))
spec = importlib.util.spec_from_loader("tasks", loader)
module = importlib.util.module_from_spec(spec)
loader.exec_module(module)
