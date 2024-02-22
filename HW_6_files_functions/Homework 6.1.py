import json

with open('departments.json', 'r') as f:
    dep = json.loads(f.read())

for departments in dep['departments']:
    if departments['expenses'] < departments['income']:
        for employee in departments['employees']:
            employee['salary'] = int(employee['salary'] * 1.1)

with open('new_costs.json', 'w') as f:
    f.write(json.dumps(dep, indent=4))
