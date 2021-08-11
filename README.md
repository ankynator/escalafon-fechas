# ESCALAFON FECHAS - GUIA

Escalafon fechas es una pequeña aplicacion de escritorio escrito en python 2.7.18 para el calculo de ATS(tiempo de servicios) de un docente

### Librerias usadas

- pyinstaller 3.3.1 para la generacion del ejutable de windows
- python-dateutil 2.8.2 para las operaciones entre fechas
- Tkinter

### Para correrlo en tu local

- Debes tener instalado python 2.7.18 y tambien el gestor de paquetes pip
- Clona o descarga este repositorio.
- Instalar las librerias usadas con:
***Tkinter no requiere instalacion***

``python -m pip install pyinstaller==3.3.1 ``
``python -m pip install python-dateutil==2.8.2``

- Con el siguiente comando puedes correr el programa

``python app.py``


### Para generar el ejcutable
``python -m PyInstaller --name ESCALAFON-FECHAS  --icon=cal-ico.ico --noconsole app.py``

*Considerar visitar la documentacin de pyinstaller, la forma de correr pyinstaller varia segun como se haya instalado pip y la libreria en si*