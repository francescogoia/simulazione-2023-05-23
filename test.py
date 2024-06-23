from model.model import Model

myModel = Model()
myModel._creaGrafo("2000", "5000000")
print(myModel.getGraphDetails())
print(myModel.getGradoMax())
print(myModel.getNumConnesse())
dreamTeam, dreamSalary = myModel.handleDreamTeam()
print(dreamSalary)
for d in dreamTeam:
    print(d)

