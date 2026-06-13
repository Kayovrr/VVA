import tkinter as tk
from input_inferior import JanelaInferior as jain
from config_api import api_client as apic
from grafico import janela_superior as jasu
import threading

janela = tk.Tk()

janela.geometry("850x600")
janela.resizable(False,False)
janela.title("Verificar de valor de ações")

def buscar():
    tik = interface_baixa.pegarTik()
    periodo = interface_baixa.pegarPeriodo()
    intervalo = interface_baixa.pegarIntervalo()

    def task():

        dados_indicadores = apic.dados_completos(tik)
        janela.after(0, atualizar_ui, tik, dados_indicadores,periodo,intervalo)

    threading.Thread(target=task, daemon=True).start()


def atualizar_ui(tik, dados_indicadores,periodo,intervalo):
    interface_alta.desenhar_grafico(tik,periodo,intervalo)
    interface_alta.mostrar_indicadores(dados_indicadores)

interface_baixa = jain(janela, buscar)
interface_alta = jasu(janela)

janela.mainloop()
