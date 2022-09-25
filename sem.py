import gurobipy as g
import numpy as np
import matplotlib.pyplot as plt

def pickColor(subject):
    if subject == 'czech':
        return 'white'
    if subject in ['arts', 'music','crafts']:
        return 'green'
    if subject == 'sport':
        return 'blue'
    if subject in ['science', 'biology', 'IT','physics','chem','geo']:
        return 'yellow'
    if subject in ['german','english']:
        return 'orange'
    if subject in ['history', 'civics']:
        return 'magenta'
    if subject == 'math':
        return 'red'
    return 'silver'

def showTimetables(timetable, teachers, subjects, classes, days, rooms, lessons, teaches):
    n = len(classes)
    for tID,t in enumerate(classes):
        ax = plt.subplot(n // 3 ,3,tID+1, frameon=False)
        y = 5
        plt.title("Class " + str(t))
        for d in days:
            dailykeys = [(p,m,h) for p in subjects for m in rooms for h in lessons if timetable[t,p,m,d,h].x > 0.5]
            for key in dailykeys:
                # Subject
                plt.text(key[2]+0.0, y + 0.5, key[0])
                # Classroom
                plt.text(key[2]+0.05, y + 0.1, key[1])
                # Teacher
                u = teachers[np.argmax([teaches[uc,t,key[0]].x for uc in teachers])]
                plt.text(key[2]+0.5, y+0.1, u)
                ax.broken_barh([(key[2],0.9)], (y, 0.8), alpha=0.4, edgecolor='black', facecolor=pickColor(key[0]))
            # Day
            plt.text(0.5, y+0.25, d)
            
            y -= 1
            plt.axis('off')
    manager = plt.get_current_fig_manager()
    manager.resize(*manager.window.maxsize())
    plt.subplots_adjust(left=0.02,bottom=0,right=0.998,top=0.957,wspace=0.026,hspace=0.1)
    plt.show()
    

# CONSTANTS

# No. of lessons in a day
H = 9

# Zakladni skola Lesni v Liberci, prvni stupen
teachers = ['T1','T2','T3','T4','T5','T6','T7', 'T8', 'T9', 'T10', 'T11',
            'T12','T13','T14']
subjects = ['math','czech','english','IT','science','biology',
            'history','arts','music','crafts','sport',
            'health','physics','geo','civics', 'chem',
            'elect','prof','german']
classes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
days = ['Mo', 'Tu', 'We', 'Th', 'Fr']
rooms = ['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10', 'R11']
lessons = list(range(1,H+1))
lunch_lessons = [5, 6,7]
lunch_limit = 3

# PARAMETERS
Curriculum = dict()

Curriculum[(1, 'czech')] = 7
Curriculum[(1, 'english')] = 2
Curriculum[(1, 'math')] = 4
Curriculum[(1, 'science')] = 2
Curriculum[(1, 'arts')] = 2
Curriculum[(1, 'music')] = 1
Curriculum[(1, 'crafts')] = 1
Curriculum[(1, 'sport')] = 2

Curriculum[(2, 'czech')] = 7
Curriculum[(2, 'english')] = 2
Curriculum[(2, 'math')] = 5
Curriculum[(2, 'science')] = 2
Curriculum[(2, 'arts')] = 1
Curriculum[(2, 'music')] = 1
Curriculum[(2, 'crafts')] = 1
Curriculum[(2, 'sport')] = 3

Curriculum[(3, 'czech')] = 7
Curriculum[(3, 'english')] = 3
Curriculum[(3, 'math')] = 5
Curriculum[(3, 'science')] = 3
Curriculum[(3, 'arts')] = 2
Curriculum[(3, 'music')] = 1
Curriculum[(3, 'crafts')] = 1
Curriculum[(3, 'sport')] = 2

Curriculum[(4, 'czech')] = 7
Curriculum[(4, 'english')] = 3
Curriculum[(4, 'math')] = 5
Curriculum[(4, 'biology')] = 2
Curriculum[(4, 'history')] = 2
Curriculum[(4, 'arts')] = 1
Curriculum[(4, 'music')] = 1
Curriculum[(4, 'crafts')] = 1
Curriculum[(4, 'sport')] = 2
Curriculum[(4, 'IT')] = 1

Curriculum[(5, 'czech')] = 8
Curriculum[(5, 'english')] = 3
Curriculum[(5, 'math')] = 5
Curriculum[(5, 'IT')] = 1
Curriculum[(5, 'biology')] = 2
Curriculum[(5, 'history')] = 2
Curriculum[(5, 'arts')] = 1
Curriculum[(5, 'music')] = 1
Curriculum[(5, 'crafts')] = 1
Curriculum[(5, 'sport')] = 2

Curriculum[(6, 'czech')] = 4
Curriculum[(6, 'english')] = 3
Curriculum[(6, 'math')] = 4
Curriculum[(6, 'IT')] = 1
Curriculum[(6, 'biology')] = 2
Curriculum[(6, 'civics')] = 2
Curriculum[(6, 'physics')] = 2
Curriculum[(6, 'history')] = 2
Curriculum[(6, 'geo')] = 2
Curriculum[(6, 'arts')] = 2
Curriculum[(6, 'music')] = 1
Curriculum[(6, 'crafts')] = 1
Curriculum[(6, 'sport')] = 2
Curriculum[(6, 'health')] = 1

Curriculum[(7, 'czech')] = 5
Curriculum[(7, 'english')] = 3
Curriculum[(7, 'math')] = 4
Curriculum[(7, 'IT')] = 1
Curriculum[(7, 'biology')] = 2
Curriculum[(7, 'civics')] = 2
Curriculum[(7, 'physics')] = 2
Curriculum[(7, 'history')] = 2
Curriculum[(7, 'geo')] = 2
Curriculum[(7, 'arts')] = 2
Curriculum[(7, 'music')] = 1
Curriculum[(7, 'crafts')] = 1
Curriculum[(7, 'sport')] = 2
Curriculum[(7, 'health')] = 1
Curriculum[(7, 'IT')] = 1

Curriculum[(8, 'czech')] = 4
Curriculum[(8, 'english')] = 3
Curriculum[(8, 'german')] = 3
Curriculum[(8, 'math')] = 5
Curriculum[(8, 'biology')] = 1
Curriculum[(8, 'civics')] = 1
Curriculum[(8, 'physics')] = 2
Curriculum[(8, 'history')] = 2
Curriculum[(8, 'chem')] = 2
Curriculum[(8, 'geo')] = 2
Curriculum[(8, 'arts')] = 2
Curriculum[(8, 'sport')] = 2
Curriculum[(8, 'health')] = 1
Curriculum[(8, 'IT')] = 1

Curriculum[(9, 'czech')] = 4
Curriculum[(9, 'english')] = 3
Curriculum[(9, 'german')] = 3
Curriculum[(9, 'math')] = 4
Curriculum[(9, 'biology')] = 2
Curriculum[(9, 'civics')] = 1
Curriculum[(9, 'physics')] = 2
Curriculum[(9, 'history')] = 2
Curriculum[(9, 'chem')] = 2
Curriculum[(9, 'geo')] = 0
Curriculum[(9, 'arts')] = 1
Curriculum[(9, 'music')] = 1
Curriculum[(9, 'sport')] = 2
Curriculum[(9, 'elect')] = 2
Curriculum[(9, 'prof')] = 1

upper = dict()
lower = dict()

Approbation = dict()

Approbation[('T5','physics')] = 1
Approbation[('T5','chem')] = 1
Approbation[('T5','elect')] = 1
Approbation[('T5','math')] = 1

Approbation[('T6','geo')] = 1
Approbation[('T6','biology')] = 1

Approbation[('T7','english')] = 1
Approbation[('T7','czech')] = 1

Approbation[('T8','math')] = 1
Approbation[('T8','civics')] = 1

Approbation[('T9','music')] = 1
Approbation[('T9','english')] = 1

Approbation[('T10','history')] = 1
Approbation[('T10','civics')] = 1

Approbation[('T11','czech')] = 1

Approbation[('T12','czech')] = 1
Approbation[('T12','german')] = 1

Approbation[('T13','arts')] = 1
Approbation[('T13','crafts')] = 1
Approbation[('T13','elect')] = 1
Approbation[('T13','prof')] = 1

Approbation[('T14','IT')] = 1
Approbation[('T14','sport')] = 1
Approbation[('T14','health')] = 1




##  PHASE 1

m1 = g.Model() 

# VARIABLES

# Teacher teaches a subject in a class
Teaches = m1.addVars(teachers, classes, subjects, vtype=g.GRB.BINARY, name="Teaches")

# Number of lessons that a teacher teaches during the week
Lessons = m1.addVars(teachers, vtype=g.GRB.INTEGER, name="Lessons")

# CONSTRAINTS

##  class teachers for the first 4 classes for all lessons, except languages
pairings = [(t,c) for (t,c) in zip(teachers[:4],classes[:4])]

for pair in pairings:
    m1.addConstrs(Teaches[pair[0],pair[1],s] == 1 for s in subjects if s != 'english' and Curriculum.get((pair[1],s),0) > 0)
    m1.addConstrs(Teaches[pair[0],c,s] == 0 for c in classes for s in subjects if c != pair[1])
    m1.addConstr(Lessons[pair[0]] == sum([Curriculum.get((pair[1],s),0) for s in subjects if s != 'english']))

for teacher in teachers[4:]:
    m1.addConstr(sum([Curriculum.get((c, s), 0) * Teaches[teacher, c, s] for c in classes for s in subjects]) == Lessons[teacher], name=f"curriculum*teacher=lessons,{teacher}")

    m1.addConstr(Lessons[teacher] <= upper.get(teacher, 22),name=f"teacher {teacher} upper")
    m1.addConstr(Lessons[teacher] >= lower.get(teacher, 14),name=f"teacher {teacher} lower")

    m1.addConstrs((Approbation.get((teacher,s), 0) >= Teaches[teacher,c,s] for c in classes for s in subjects),name="approbations")

for c in classes:
    for s in subjects:
        if Curriculum.get((c, s), 0) > 0:
            m1.addConstr(Teaches.sum('*', c, s) == 1)

m1.optimize()

print([(t,Lessons[t].x) for t in teachers])

# m1.computeIIS()
# m1.write('iis.ilp')
# exit()

print([f"{t} teaches {s} in {c}" for t in teachers for c in classes for s in subjects if Teaches[t,c,s].x > 0.5])

## PHASE 2

m2 = g.Model()

# VARIABLES

Timetable = m2.addVars(classes, subjects, rooms, days, lessons, 
                       vtype=g.GRB.BINARY, name="Timetable")

mSumsTimetable = m2.addVars(classes, subjects, days,lessons,
                            vtype=g.GRB.BINARY, name="mSumsTimetable")

# 1 if the class has a lunch in that time
Lunches = m2.addVars(classes, days, lessons, vtype=g.GRB.BINARY, name="Lunches")

# 1 during and after lunch that day
Lunches_helper = m2.addVars(classes, days, lessons, vtype=g.GRB.BINARY, name="Lunches_helper")

Afternoon_sums = m2.addVars(classes, days, vtype=g.GRB.INTEGER, name="Afternoon_sums")

Afternoon = m2.addVars(classes, days, vtype=g.GRB.BINARY, name="Afternoon")

# CONSTRAINTS

# Defining the sums across the rooms
m2.addConstrs(mSumsTimetable[c,s,d,l] == Timetable.sum(c,s,'*',d,l) for c in classes for s in subjects for d in days for l in lessons)

# Each room can host at most a single lesson
m2.addConstrs((Timetable.sum('*', '*', m, d, h) <= 1 for m in rooms for d in days for h in lessons))

# Avoid teacher's timetable collisions
for teacher in teachers:
    # A teacher teaches more than a single subject in a single class
    assignedSubjectsClasses = [(t,p) for p in subjects for t in classes if
        Teaches[teacher,t,p].x > 0.5]
    for outerPair in assignedSubjectsClasses:
        for innerPair in assignedSubjectsClasses:
            if outerPair != innerPair:
                m2.addConstrs((mSumsTimetable[outerPair[0],outerPair[1],d,h] == 1) >> 
                    (mSumsTimetable[innerPair[0],innerPair[1],d,h] == 0) for d in days for h in lessons)

# Adhere to the curriculum
m2.addConstrs(Timetable.sum(t,p,'*','*','*') == Curriculum.get((t,p),0) for t in classes for p in subjects)

# Timetable has occupied the first time slot
m2.addConstrs(Timetable.sum(t,'*','*',d,lessons[0]) == 1 for t in classes for d in days)

# Avoid time conflicts in the class' schedule
m2.addConstrs(Timetable.sum(t,'*','*',d,h) <= 1 for t in classes for d in days for h in lessons)

# Ensure that if the subject can be spread throughout the week, they are
m2.addConstrs(Timetable.sum(t,p,'*',d,'*') <= 1 for t in classes for p in subjects for d in days if Curriculum.get((t,p), 0) <= 5)

# Only one lunch per day
m2.addConstrs(Lunches.sum(t,d,'*') == 1 for t in classes for d in days)

# Specify lunch lessons
m2.addConstrs(Lunches[t,d,h] == 0 for t in classes for d in days for h in lessons if h not in lunch_lessons)

# If there is a lunch, there cannot be any lesson at that time
m2.addConstrs((Lunches[t,d,h0] == 1) >> (Timetable.sum(t,'*','*',d,h0) == 0) for t in classes for d in days for h0 in lunch_lessons)

# Limit classes having the lunch simultaneously
m2.addConstrs(Lunches.sum('*',d,h0) <= lunch_limit for d in days for h0 in lunch_lessons)

# Implement the lunch helper
m2.addConstrs(Lunches_helper[t,d,h-1] <= Lunches_helper[t,d,h] for t in classes for d in days for h in lessons if h > lessons[0])

m2.addConstrs((Lunches_helper[t,d,h-1] == 0) >> (Lunches[t,d,h] == Lunches_helper[t,d,h]) for t in classes for d in days for h in lessons if h > lessons[0])

# Define Afternoon_sums
m2.addConstrs(g.quicksum([Timetable[t,p,m,d,h] * Lunches_helper[t,d,h] for p in subjects for m in rooms for h in lessons]) == Afternoon_sums[t,d] for t in classes for d in days)

# Bind Afternoon_sums to Afternoon
m2.addConstrs((Afternoon[t,d] == 0) >> (Afternoon_sums[t,d] == 0) for t in classes for d in days)
m2.addConstrs((Afternoon[t,d] == 1) >> (Afternoon_sums[t,d] >= 1) for t in classes for d in days)

# If there are more than 5 lessons per week for a subject, all days must contain at least one lesson
m2.addConstrs(Timetable.sum(t,p,'*',d,'*') >= 1 for t in classes for p in subjects for d in days if Curriculum.get((t,p),0) >= 6)

# There cannot be any afternoon lessons on friday
m2.addConstr(Afternoon.sum('*', days[-1]) == 0)

# No class has more than three afternoon education
m2.addConstrs(Afternoon.sum(t, '*') <= 3 for t in classes)

# The first 4 classes do not have afternoon lessons
m2.addConstrs(Afternoon.sum(t, '*') == 0 for t in classes[:4])

# Music lessons can only be taught in 'R1'
m2.addConstrs(Timetable.sum('*', 'music', m, '*', '*') == 0 for m in rooms if m != rooms[0])

# Chemistry lessons can only be taught in 'R2'
m2.addConstrs(Timetable.sum('*', 'chem', m, '*', '*') == 0 for m in rooms if m != rooms[1])



# OBJECTIVE - penalize later lessons
m2.setObjective(g.quicksum([h * Timetable[t,p,m,d,h] for t in classes for p in subjects for m in rooms for d in days for h in lessons]), sense=g.GRB.MINIMIZE)

# Logging
# g.setParam("LogFile", 'm2.log')

m2.optimize()
# m2.computeIIS()
# m2.write("model.ilp")

showTimetables(Timetable, teachers, subjects, classes, days, rooms, lessons, Teaches) 