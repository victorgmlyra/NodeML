import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from ui.ui_mainwindow import Ui_MainWindow

from src.model_builder import NodeGraphWidget
from NodeGraphQt import NodesPaletteWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Create an instance of NodeGraphWidget
        self.node_graph_widget = NodeGraphWidget()
        self.ui.tabWidget.addTab(self.node_graph_widget, "Model Builder")

        # Create the nodes list
        self.nodes_palette_widget = NodesPaletteWidget(node_graph=self.node_graph_widget.node_graph)
        self.ui.splitter.insertWidget(0, self.nodes_palette_widget)
        
        # Setup Ui sizes
        self.ui.splitter.setSizes([100, 500, 100])


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
