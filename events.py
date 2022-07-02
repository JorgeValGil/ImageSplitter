import var, sys
from PIL import Image
from PyQt5 import QtWidgets
from pathlib import Path

class Eventos():

    def Salir(self):
        try:
            sys.exit()
        except Exception as error:
            print("Error %s: " % str(error))

    def Split(self, image_path, cols, rows, destination_path):
        im = Image.open(image_path)
        im_width, im_height = im.size
        col_width = int(im_width / cols)
        row_height = int(im_height / rows)
        n = 0
        for i in range(0, cols):
            for j in range(0, rows):
                box = (i * col_width, j * row_height, i * col_width +
                       col_width, j * row_height + row_height)
                im_box = im.crop(box)
                out_path = destination_path +"/"+ Path(image_path).stem + "-" + str(j) + "-" + str(i) + "." + image_path.split(".")[1]
                im_box.save(out_path)
                n += 1
        var.ui.labelstatusbar.setText('GENERADAS '+str(n)+' IMÁGENES')


    def GenerarImagenes(self):
        if var.ui.lineEdit_imagen.text() != "":
            ventana_carpeta = QtWidgets.QFileDialog
            carpeta_destino = ventana_carpeta.getExistingDirectory(None, 'Selecciona la carpeta de destino')
            if ventana_carpeta.Accepted and carpeta_destino != '':
                Eventos.Split(self, var.ui.lineEdit_imagen.text(), var.ui.spinBox_columnas.value(), var.ui.spinBox_filas.value(), carpeta_destino)
        else:
            var.ui.labelstatusbar.setText('DEBES SELECCIONAR LA IMAGEN')

    def SeleccionarImagen(self):
        '''Función que selecciona la imagen.
        Se abre una ventana para seleccioanr la imagen y se guarda la ruta en un campo de texto.'''
        try:
            ventana_imagen = QtWidgets.QFileDialog
            filename, filtro = ventana_imagen.getOpenFileName(None, 'Seleccionar imagen', "Imagen",
                                                                 "Imagen (*.png *.jpg)")
            if ventana_imagen.Accepted and filename != '':
                var.ui.lineEdit_imagen.setText(filename)
        except Exception as error:
            print("Error %s: " % str(error))

    def LimpiarImagen(self):
        '''Función que limpia el campo de texto de la imagen.'''
        var.ui.lineEdit_imagen.setText("")

