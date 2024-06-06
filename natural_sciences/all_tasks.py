#!/usr/bin/env python

import os.path as path
from pathlib import Path
import importlib.machinery
import importlib.util
from random import choice, randint


def walkpath(dir_path):
    files = []
    for file in dir_path.iterdir():
        if file.is_dir():
            files += walkpath(file)
        elif str(file).endswith("tasks.py") and str(file) != __file__:
            files.append(file)
    return files


class Tasks:
    def __init__(self, scriptdir):
        self.scriptdir = scriptdir
        self.tasks     = self.__import_tasks()


    def __import_tasks(self):
        tasks = dict()

        for (idx, taskmod) in enumerate(walkpath(self.scriptdir)):
            modname = path.basename(path.dirname(taskmod))

            loader = importlib.machinery.SourceFileLoader(modname, str(taskmod))
            spec = importlib.util.spec_from_loader(modname, loader)
            module = importlib.util.module_from_spec(spec)
            loader.exec_module(module)

            module_tasks = [getattr(module, func) for func in dir(module)
                            if func.startswith("task") and
                            callable(getattr(module, func))]
            tasks[modname] = module_tasks

        return tasks


    def pop_random(self):
        while True:
            if not self.tasks:
                return None

            tasks = choice(list(self.tasks.keys()))

            if not self.tasks[tasks]:
                del self.tasks[tasks]
            else:
                break

        idx = randint(0, len(self.tasks[tasks]) - 1)
        return self.tasks[tasks].pop(idx)

tasks = Tasks(Path(path.dirname(path.realpath(__file__))))

if __name__ == "__main__":
    n_tasks = sum([len(i) for i in tasks.tasks.values()])
    print(f"Loaded {n_tasks} tasks.")

    while True:
        print('-' * 80)
        task = tasks.pop_random()
        if task is None:
            break
        task()
