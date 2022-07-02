from ventana import *
import var, sys, events

class Main(QtWidgets.QMainWindow):
    '''Clase principal del programa'''

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)

        var.ui.pushButton_Salir.clicked.connect(events.Eventos.Salir)
        var.ui.pushButton_Generar.clicked.connect(events.Eventos.GenerarImagenes)
        var.ui.pushButton_Seleccionar.clicked.connect(events.Eventos.SeleccionarImagen)
        var.ui.pushButton_Eliminar.clicked.connect(events.Eventos.LimpiarImagen)

        var.ui.statusbar.addPermanentWidget(var.ui.labelstatusbar, 1)

if __name__ == '__main__':
    '''Ejecución del programa'''
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())