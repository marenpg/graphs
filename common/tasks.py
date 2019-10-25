import csv, os
from .modules import brain_modules

class Task:
    def __init__(self, name, modules):
        self.name = name
        self.modules = modules
    
    def __repr__(self):
        return self.name
        
def getTasks():
    tasks = []
    filename = os.path.join(os.path.dirname(__file__), 
        '../data/modules-tasks.csv')
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            task_name = row.pop(0).strip()
            task_modules = _getModules(row)
            tasks.append(Task(task_name, task_modules))
    return tasks

def _getModule(module_name):
    return next((x for x in brain_modules if x.name == module_name.strip()), None)

def _getModules(module_names):
    _ = [_getModule(name) if name != "" else None for name in module_names]
    return list(filter(lambda x: x != None, _))
