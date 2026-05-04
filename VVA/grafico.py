import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt
from config_api import api_client
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class janela_superior():

    def __init__(self,container):

        self.grafico = tk.Frame(
            container,
            bd="2",
            relief="solid",
            bg="white",
            height=300
               
        )

        self.info_frame = tk.Frame(container, bg="#1e1e1e")
        self.info_frame.pack(fill="x", padx=10, pady=(0, 10))

        self.grafico.pack(side="top",fill="x",padx=10,pady=10)
        self.grafico.pack_propagate(False)

        self.frame = tk.Frame(

            container,
            bg="#DDEEEB",
            relief="raised",
            bd="3",
            height=600,
            width=200

        )
        self.frame.pack(side="bottom", fill="x")

    def desenhar_grafico(self, ticker,periodo,intervalo):

        if periodo == "max":
            intervalo == "1wk"
        elif periodo == "ytd":
            intervalo = "1d"
        
        #dados = api_client.historico_tik()

        for widget in self.grafico.winfo_children():
            widget.destroy()

        loading = tk.Label(self.grafico, text="Carregando...", bg="white")
        loading.pack(expand=True)

        try:
            dados = api_client.historico_tik(ticker,periodo=periodo,intervalo=intervalo)
        except Exception as e:
            print("Erro:", e)
            return

        if not dados:
            print("Sem dados")
            return

        df = pd.DataFrame(dados)

        for widget in self.grafico.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(figsize=(7, 4))


        fig.patch.set_facecolor("#1e1e1e")
        ax.set_facecolor("#1e1e1e")

        ax.plot(df["data"], df["close"], color="#4CAF50", linewidth=2)

        ax.fill_between(df["data"], df["close"], color="#4CAF50", alpha=0.1)

        ax.set_title(f"{ticker}", fontsize=14, color="white")


        ax.set_ylabel("Preço (R$)", color="white")
        ax.set_xlabel("Data", color="white")

        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')

    
        ax.grid(True, linestyle="--", alpha=0.2)

        for spine in ax.spines.values():
            spine.set_visible(False)

        fig.autofmt_xdate()

        ultimo_preco = df["close"].iloc[-1]
        ultima_data = df["data"].iloc[-1]

        ax.text(
            ultima_data,
            ultimo_preco,
            f"R$ {ultimo_preco:.2f}",
            color="white",
            fontsize=10
        )

        canvas = FigureCanvasTkAgg(fig, master=self.grafico)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

        plt.close(fig)

    def mostrar_indicadores(self, dados):

        for widget in self.info_frame.winfo_children():
            widget.destroy()

        if not dados:
            return
 
        d = dados[0]

        infos = {
            "Abertura": d.get("open"),
            "Fech. Ant.": d.get("previousClose"),
            "Volume": d.get("volume"),
            "máx": d.get("max"),
            "min": d.get("min"),
            "Market Cap": d.get("marketCap")
        }

        for i, (chave, valor) in enumerate(infos.items()):

            frame = tk.Frame(self.info_frame, bg="#2c2c2c", padx=10, pady=5)
            frame.grid(row=0, column=i, padx=5, pady=5, sticky="nsew")

            label_nome = tk.Label(
                frame,
                text=chave,
                fg="white",
                bg="#2c2c2c",
                font=("Segoe UI", 9)
            )
            label_nome.pack()

            label_valor = tk.Label(
                frame,
                text=str(valor),
                fg="#4CAF50",
                bg="#2c2c2c",
                font=("Segoe UI", 11, "bold")
            )
            label_valor.pack()

        for i in range(len(infos)):
            self.info_frame.grid_columnconfigure(i, weight=1)

        