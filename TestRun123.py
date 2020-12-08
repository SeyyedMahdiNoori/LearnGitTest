from pyomo.environ import Reals
# from pyomo.environ import NonNegativeReals
# from pyomo.environ import Constraint
from pyomo.environ import ConstraintList
from pyomo.environ import ConcreteModel
#from pyomo.environ import Reals
from pyomo.environ import Var
from pyomo.environ import Objective
from pyomo.opt import SolverFactory
from pyomo.environ import sin
# from math import pi
import  time
import random

# print(A)

s=time.time()

model=ConcreteModel()

model.Thet= Var(within=Reals)
model.Cons = ConstraintList()
model.Cons.add( sin(model.Thet) == 0.5  + random.random()*0.1  )

model.obj = Objective(expr=model.Thet)

opt = SolverFactory('ipopt')

results = opt.solve(model)
E =time.time()

print(model.obj.expr() )

#print(E-s)
'''


s=time.time()
random.seed(10)
opt = SolverFactory('ipopt')

for t in range(0,5):

    model=ConcreteModel()

    model.Thet= Var(within=Reals)
    model.Cons = ConstraintList()
    model.Cons.add( sin(model.Thet) == 0.5 + random.random()*0.1 )

    model.obj = Objective(expr=model.Thet)

    results = opt.solve(model)
    E =time.time()

    print(model.obj.expr() )
    #print(E-s)
'''

aa=10
