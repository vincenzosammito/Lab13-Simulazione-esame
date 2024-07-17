import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listShape = []

    def fillDD(self):
        #riempimento dropdown anno
        for year in range(1910,2015):
            anno = str(year)
            self._listYear.append(year)
            self._view.ddyear.options.append(ft.dropdown.Option(key= anno,
                                                              data=anno,
                                                              text=anno,
                                                              on_click=self.fillshape))
    def fillshape(self, e):
        #riempimento dropdown shape
        anno = e.control.data
        print(anno)
        self._listShape = self._model.add_shapes(anno)
        print(self._listShape)
        for shape in self._listShape:
            self._view.ddshape.options.append(ft.dropdown.Option(key = shape,
                                                                 data=shape,
                                                                 text=shape,
                                                                 ))
        self._view.update_page()
    def handle_graph(self, e):
        self._model.buildGraph(self._view.ddyear.value, self._view.ddshape.value)
        for state in self._model.stati:
            somma_pesi = 0
            for vicino in self._model.myGraph.neighbors(state):
                somma_pesi += int(self._model.myGraph[vicino][state]['weight'])
            self._view.txt_result.controls.append(ft.Text(f"Nodo {state}, somma peso su archi={somma_pesi}"))
        self._view.update_page()
    def handle_path(self, e):
        self._model.ricorsione([], 0)