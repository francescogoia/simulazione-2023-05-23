import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model












    def handle_graph(self, e):
        anno = self._view._txtAnno.value
        salario = self._view._txtSalario.value
        try:
            intAnno = int(anno)
            floatSalario = float(salario)
        except ValueError:
            self._view.txt_result1.controls.clear()
            self._view.txt_result1.controls.append(ft.Text(f"Inserire un numero intero in 'anno' e un numero in 'salario'"))
            self._view.update_page()
            return
        if intAnno < 1871 or intAnno > 2019:
            self._view.txt_result1.controls.clear()
            self._view.txt_result1.controls.append(ft.Text(f"Inserire un anno tra 1871 e 2019"))
            self._view.update_page()
            return
        self._model._creaGrafo(anno, salario)
        numNodi, numArchi = self._model.getGraphDetails()
        self._view.txt_result1.controls.clear()
        self._view.txt_result1.controls.append(ft.Text(f"Il grafo ha {numNodi} nodi e {numArchi} archi."))
        self._view._btnGradoMassimo.disabled = False
        self._view._btnConnesse.disabled = False
        self._view._btnDreamTeam.disabled = False
        self._view.update_page()

    def handle_gradoMax(self, e):
        nodo, grado = self._model.getGradoMax()
        self._view.txt_result1.controls.append(ft.Text(f"Il nodo di grado massimo è {nodo}, con grado {grado}."))
        self._view.update_page()

    def handle_connesse(self, e):
        nConnesse = self._model.getNumConnesse()
        self._view.txt_result1.controls.append(ft.Text(f"Il grafo ha {nConnesse} componenti connesse."))
        self._view.update_page()


    def handle_dreamTeam(self, e):
        dreamTeam, dreamSalary = self._model.handleDreamTeam()
        self._view.txt_result2.controls.clear()
        self._view.txt_result2.controls.append(ft.Text(f"Salario dream team: {dreamSalary}$"))
        for p in dreamTeam:
            self._view.txt_result2.controls.append(ft.Text(f"{p}"))
        self._view.update_page()
