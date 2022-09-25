# ILP Timetable Maker
This project has been done as a semestral work for the [Combinatorial Algorithms course](https://cw.fel.cvut.cz/b212/courses/rm35koa/start) held at the Czech Technical University in Prague in the summer semester of 2021/2022.

The task was to design an algorithm which provides a timetable for the whole school under the given constraints.
The constraints include (not exhaustively):
  * Number of teachers is limited,
  * individual teachers can teach only certain subjects,
  * number of classrooms is limited,
  * the class' curriculum has to be fulfilled,
  * if a class has lessons in the afternoon, lunch break has to be included,
  * capacity of the school canteen is limited at any given time
  * ...
  
The problem is [solved](sem.py) using the integer linear programming and uses the [Gurobi solver](https://www.gurobi.com/) and its Python API. 

Further details are described in the [PDF report](report.pdf). 

An example of the resulting timetable is shown below.

![Resulting timetable.](https://user-images.githubusercontent.com/55233762/192138423-be380dcf-2ecc-4f9a-93b5-af4b0617cf6f.PNG)
