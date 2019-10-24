import csv, os

def getTasks():
    tasks = set()
    modules = set()
    filename = os.path.join(os.path.dirname(__file__), 
        '../data/modules-tasks.csv')
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            tasks.add(row[0].strip())
            for module in row[1:]:
                if(module != ''):
                    modules.add(module.strip())

    return (tasks, modules)

print(getTasks())