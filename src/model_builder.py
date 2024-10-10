from PySide2 import QtWidgets
from NodeGraphQt import NodeGraph, NodesPaletteWidget

class NodeGraphWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(NodeGraphWidget, self).__init__(parent)
        
        # Set layout for the widget
        layout = QtWidgets.QVBoxLayout(self)
        
        # Create NodeGraph and NodeViewer instance
        self.node_graph = NodeGraph()
        self.viewer = self.node_graph._viewer
        
        # Embed the NodeViewer widget into the layout
        layout.addWidget(self.viewer)

        # Optional: Set up custom nodes or load default nodes
        # Example of creating a simple node
        from NodeGraphQt import BaseNode
        
        class MyNode(BaseNode):
            __identifier__ = 'com.example'
            NODE_NAME = 'My Node'
        
        self.node_graph.register_node(MyNode)
        new_node = self.node_graph.create_node('com.example.MyNode')
        new_node.set_pos(-150, 0)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    window.setWindowTitle("NodeGraphQt Widget Example")
    window.setGeometry(100, 100, 1200, 800)
    
    # Create an instance of NodeGraphWidget and set it as central widget
    node_graph_widget = NodeGraphWidget()
    window.setCentralWidget(node_graph_widget)

    # create a node palette widget.
    nodes_palette = NodesPaletteWidget(node_graph=node_graph_widget.node_graph)
    # nodes_palette.set_category_label('nodeGraphQt.nodes', 'Builtin Nodes')
    # nodes_palette.set_category_label('nodes.custom.ports', 'Custom Port Nodes')
    # nodes_palette.set_category_label('nodes.widget', 'Widget Nodes')
    # nodes_palette.set_category_label('nodes.basic', 'Basic Nodes')
    # nodes_palette.set_category_label('nodes.group', 'Group Nodes')
    nodes_palette.show()
    
    window.show()
    sys.exit(app.exec_())