from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PySide2.QtGui import QFont
import sys
import serial

class Windown(QWidget):
    def __init__ (self):
        super().__init__()

        self.sit_btn_amarelo = 1
        self.sit_btn_azul = 1
        self.sit_btn_verde = 1
        self.sit_btn_branco = 1
        self.sit_btn_vermelho = 1

        fonte = QFont('Arial', 16, QFont.Bold)

        self.setFixedSize(350, 500)
        self.setWindowTitle('Liga led')
        self.setAutoFillBackground(True)
        self.setStyleSheet("background-color: rgb(196, 255, 198);")

        txt_titulo = QLabel('Interruptor automático', self)
        txt_titulo.setGeometry(25, 50, 300, 81)
        txt_titulo.setFont(QFont('Arial', 20, QFont.Bold))
        txt_titulo.setStyleSheet('background-color: rgb(196, 255, 198);color: rgb(0, 152, 61)')

        txt_amarelo = QLabel('Amarelo', self)
        txt_amarelo.setGeometry(35, 170, 100, 40)
        txt_amarelo.setFont(fonte)
        txt_amarelo.setStyleSheet('background-color: rgb(196, 255, 198);color: rgb(0, 152, 61)')

        txt_azul = QLabel('Azul', self)
        txt_azul.setGeometry(35, 230, 100, 40)
        txt_azul.setFont(fonte)
        txt_azul.setStyleSheet('background-color: rgb(196, 255, 198);color: rgb(0, 152, 61)')
        
        txt_verde = QLabel('Verde', self)
        txt_verde.setGeometry(35, 290, 100, 40)
        txt_verde.setFont(fonte)
        txt_verde.setStyleSheet('background-color: rgb(196, 255, 198);color: rgb(0, 152, 61)')

        txt_branco = QLabel('Branco', self)
        txt_branco.setGeometry(35, 350, 100, 40)
        txt_branco.setFont(fonte)
        txt_branco.setStyleSheet('background-color: rgb(196, 255, 198);color: rgb(0, 152, 61)')

        txt_vermelho = QLabel('Vermelho', self)
        txt_vermelho.setGeometry(35, 410, 100, 40)
        txt_vermelho.setFont(fonte)
        txt_vermelho.setStyleSheet('background-color: rgb(196, 255, 198);color: rgb(0, 152, 61)')

        self.definir_botoes()

        self.create_porta()
    
    def definir_botoes (self):
        fonte = QFont('Arial', 12, QFont.Bold)

        self.btn_amarelo_on = QPushButton("Ligar", self)
        self.btn_amarelo_on.setFont(fonte)
        self.btn_amarelo_on.setGeometry(180, 170, 150, 41)
        self.btn_amarelo_on.setStyleSheet('background-color: rgb(0, 152, 61);color: white')
        self.btn_amarelo_on.clicked.connect(self.btn_amarelo_clicado)

        self.btn_amarelo_off = QPushButton("Desligar", self)
        self.btn_amarelo_off.setFont(fonte)
        self.btn_amarelo_off.setGeometry(180, 170, 150, 41)
        self.btn_amarelo_off.setStyleSheet('background-color: rgb(0, 152, 61);color: white')
        self.btn_amarelo_off.clicked.connect(self.btn_amarelo_clicado)
        self.btn_amarelo_off.close()


        self.btn_azul_on = QPushButton("Ligar", self)
        self.btn_azul_on.setFont(fonte)
        self.btn_azul_on.setGeometry(180, 230, 150, 41)
        self.btn_azul_on.setStyleSheet('background-color: rgb(0, 152, 61);color: white')
        self.btn_azul_on.clicked.connect(self.btn_azul_clicado)

        self.btn_azul_off = QPushButton("Desligar", self)
        self.btn_azul_off.setFont(fonte)
        self.btn_azul_off.setGeometry(180, 230, 150, 41)
        self.btn_azul_off.setStyleSheet('background-color: rgb(0, 152, 61);color: white')
        self.btn_azul_off.clicked.connect(self.btn_azul_clicado)
        self.btn_azul_off.close()


        self.btn_verde_on = QPushButton("Ligar", self)
        self.btn_verde_on.setFont(fonte)
        self.btn_verde_on.setGeometry(180, 290, 150, 41)
        self.btn_verde_on.setStyleSheet('background-color: rgb(0, 152, 61);color: white')
        self.btn_verde_on.clicked.connect(self.btn_verde_clicado)

        self.btn_verde_off = QPushButton("Desligar", self)
        self.btn_verde_off.setFont(fonte)
        self.btn_verde_off.setGeometry(180, 290, 150, 41)
        self.btn_verde_off.setStyleSheet('background-color: rgb(0, 152, 61);color: white')
        self.btn_verde_off.clicked.connect(self.btn_verde_clicado)
        self.btn_verde_off.close()


        self.btn_branco_on = QPushButton("Ligar", self)
        self.btn_branco_on.setFont(fonte)
        self.btn_branco_on.setGeometry(180, 350, 150, 41)
        self.btn_branco_on.setStyleSheet('background-color: rgb(0, 152, 61);color: white')
        self.btn_branco_on.clicked.connect(self.btn_branco_clicado)

        self.btn_branco_off = QPushButton("Desligar", self)
        self.btn_branco_off.setFont(fonte)
        self.btn_branco_off.setGeometry(180, 350, 150, 41)
        self.btn_branco_off.setStyleSheet('background-color: rgb(0, 152, 61);color: white')
        self.btn_branco_off.clicked.connect(self.btn_branco_clicado)
        self.btn_branco_off.close()


        self.btn_vermelho_on = QPushButton("Ligar", self)
        self.btn_vermelho_on.setFont(fonte)
        self.btn_vermelho_on.setGeometry(180, 410, 150, 41)
        self.btn_vermelho_on.setStyleSheet('background-color: rgb(0, 152, 61);color: white')
        self.btn_vermelho_on.clicked.connect(self.btn_vermelho_clicado)

        self.btn_vermelho_off = QPushButton("Desligar", self)
        self.btn_vermelho_off.setFont(fonte)
        self.btn_vermelho_off.setGeometry(180, 410, 150, 41)
        self.btn_vermelho_off.setStyleSheet('background-color: rgb(0, 152, 61);color: white')
        self.btn_vermelho_off.clicked.connect(self.btn_vermelho_clicado)
        self.btn_vermelho_off.close()

    def btn_amarelo_clicado (self):
        global portaUSB

        if self.sit_btn_amarelo == 1:
            print("Botão ligar apertado")
            #portaUSB.write('s'.encode())
            self.enviar_dado('1')
            self.sit_btn_amarelo = 0
            self.btn_amarelo_on.close()
            self.btn_amarelo_off.show()
        else:
            print("Botão desligar apertado")
            #portaUSB.write('d'.encode())
            self.enviar_dado('1')
            self.sit_btn_amarelo = 1
            self.btn_amarelo_on.show()
            self.btn_amarelo_off.close()

    def btn_azul_clicado (self):
        if self.sit_btn_azul == 1:
            print("Botão ligar apertado")
            self.enviar_dado('2')
            self.sit_btn_azul = 0
            self.btn_azul_on.close()
            self.btn_azul_off.show()
        else:
            print("Botão desligar apertado")
            self.enviar_dado('2')
            self.sit_btn_azul = 1
            self.btn_azul_on.show()
            self.btn_azul_off.close()

    def btn_verde_clicado (self):
        if self.sit_btn_verde == 1:
            print("Botão ligar apertado")
            self.enviar_dado('3')
            self.sit_btn_verde = 0
            self.btn_verde_on.close()
            self.btn_verde_off.show()
        else:
            print("Botão desligar apertado")
            self.enviar_dado('3')
            self.sit_btn_verde = 1
            self.btn_verde_on.show()
            self.btn_verde_off.close()

    def btn_branco_clicado (self):
        if self.sit_btn_branco == 1:
            print("Botão ligar apertado")
            self.enviar_dado('4')
            self.sit_btn_branco = 0
            self.btn_branco_on.close()
            self.btn_branco_off.show()
        else:
            print("Botão desligar apertado")
            self.enviar_dado('4')
            self.sit_btn_branco = 1
            self.btn_branco_on.show()
            self.btn_branco_off.close()
    
    def btn_vermelho_clicado (self):
        if self.sit_btn_vermelho == 1:
            print("Botão ligar apertado")
            self.enviar_dado('5')
            self.sit_btn_vermelho = 0
            self.btn_vermelho_on.close()
            self.btn_vermelho_off.show()
        else:
            print("Botão desligar apertado")
            self.enviar_dado('5')
            self.sit_btn_vermelho = 1
            self.btn_vermelho_on.show()
            self.btn_vermelho_off.close()

    def create_porta(self):
        global portaUSB
        aux = "COM3"
        portaUSB = serial.Serial(aux, 9600)
    
    def enviar_dado(self, mens):
        global portaUSB
        portaUSB.write(mens.encode())




def mostrar_janela ():
    myApp = QApplication.instance()
    if myApp is None:
        myApp = QApplication(sys.argv)
    janela = Windown()
    janela.show()
    myApp.exec_()

mostrar_janela()
sys.exit(0)
