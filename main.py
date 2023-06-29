from kivy.app import App
from mainwidget import MainWidget
from kivy.lang.builder import Builder

class MainApp(App):
    """
    Widdget principal da aplicação
    """
    def build(self):
        """
        Método que gera o aplicativo com o widget principal
        """
        self._widget=MainWidget(scantime=1000,server_ip='localhost',server_port=502,
        modbus_addrs={
            'tempCarc':{
                'addr':706, 
                #Temperatura da carcaça
                'tipo':'FP',
                'div':10.0
            },
            'velEsteira':{
                'addr':724, 
                #Velocidade da esteira
                'tipo':'FP',
                'div':1.0
            },
            'cargaPV':{
                'addr':710,
                #Valor lido da carga na esteira(PV) 
                'tipo':'FP',
                'div':1.0

            },
            'tensaoRS':{
                'addr':847,
                #Valor de ddp entre R e S   
                'tipo':'4X',
                'div':10.0
            },
            'statusPID':{
                'addr':722,
                #Status do PID     
                'tipo':'4X',
                'div':1.0
            },
            'frequencia':{
                'addr':830,
                #Frequência da rede
                'tipo':'4X',
                'div':100.0
            }   ,
            'correnteMedia':{
                'addr':845,
                #Corrente média     
                'tipo':'4X',
                'div':100.0
            },
            'potAtivaTotal':{
                'addr':855,
                #Potência ativa total
                'tipo':'4X',
                'div':1.0

            },
            'fpTotal':{
                'addr':871,
                #Fator de potência total
                'tipo':'4X',
                'div':1000.0
            },
            'freqRotacao':{
                'addr':884,
                #Frequência de rotação
                'tipo':'FP',
                'div':1.0
            },
            'indicaPartida':{
                'addr':1216, 
                #Indica a partida selecionada(Direta=3, Soft Start=1, Inversor=2)         
                'tipo':'4X',
                'div':1.0
            },
            'torque':{
                'addr':1420,
                #Torque
                'tipo':'FP',
                'div':100.0
            },
            'tipoMotor':{
                'addr':708,
                #Tipo de motor
                'tipo':'4X',
                'div':1.0
            }
            
        },
        atuadores={
            'partidaInversor':{
                'addr':1312,
                #Partida do inversor(0=desligado, 1=ligado, 2=reset)
                'tipo':'4X',
                'div':1.0
            },
            'partidaSoftStart':{
                'addr':1316,
                #Partida do soft start(0=desligado, 1=ligado, 2=reset)
                'tipo':'4X',
                'div':1.0
            },
            'partidaDireta':{
                'addr':1319,
                #Partida direta(0=desligado, 1=ligado, 2=reset)
                'tipo':'4X',
                'div':1.0
            },
            'velInversor':{
                'addr':1313,
                #Velocidade do inversor
                'tipo':'4X',
                'div':10.0
            },
            'selPID':{
                'addr':1332,
                #Seleção do PID(0=automático, 1=manual)
                'tipo':'4X',
                'div':1.0
            },
            'selTipoPartida':{
                'addr':1324,
                #Seleção do tipo de partida(3=direta, 1=soft start, 2=inversor)
                'tipo':'4X',
                'div':1.0
            },
            'defineSetPoint':{
                'addr':1302,
                #Define o set point do PID
                'tipo':'FP',
                'div':1.0
            },
            'defineMV':{
                'addr':1310,
                #Define o MV% do PID
                'tipo':'FP',
                'div':1.0
            }

        }
        )
        return self._widget
    
if __name__ == "__main__":
    
    Builder.load_string(open("mainwidget.kv",encoding="utf-8").read(),rulesonly=True)
    Builder.load_string(open("popups.kv",encoding="utf-8").read(),rulesonly=True)
    MainApp().run()

#ERROS ENCONTRADOS
#2) Carga sobre a esteira PV não muda nem no supervisório da bancada
#3) Quando fecho a janela o programa trava, por que?