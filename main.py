import events
import sys
import var
from ventana import *


class Main(QtWidgets.QMainWindow):
    """Clase principal del programa"""

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)

        var.ui.pushButton_Salir.clicked.connect(events.Eventos.salir)
        var.ui.pushButton_Generar.clicked.connect(events.Eventos.generar_imagenes)
        var.ui.pushButton_Seleccionar.clicked.connect(events.Eventos.seleccionar_imagen)
        var.ui.pushButton_Eliminar.clicked.connect(events.Eventos.limpiar_imagen)

        var.ui.statusbar.addPermanentWidget(var.ui.labelstatusbar, 1)


if __name__ == '__main__':
    '''Ejecución del programa'''
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())
