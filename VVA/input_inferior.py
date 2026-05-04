import tkinter as tk

class JanelaInferior:

    def __init__(self, container, comando_buscar):

        self.comando_buscar = comando_buscar 

        self.frame = tk.Frame(
            container,
            bg="#444444",
            relief="groove",
            bd="3",
            height=400,
            width=200
        )

        self.frame.pack(side="bottom", fill="x")
    
        self.caixa_input = tk.Entry(
            self.frame,
            bg="#312f2f",
            fg="#E7C248",
            font="Impact",
            insertbackground="white",
            width=20,
            bd=3,
            relief="sunken",
            justify='center'
        )

        self.caixa_input.pack(anchor="w", padx=10, pady=10)  

        botao = tk.Button(self.frame, text="Buscar", command=comando_buscar)
        botao.pack(side="left", padx=(0,5)) 

        botoes_frame = tk.Frame(self.frame, bg="grey")
        botoes_frame.pack(pady=10)

        tickers = ["PETR4", "VALE3", "ITUB4", "MGLU3"]

        for t in tickers:
            btn = tk.Button(
                botoes_frame,
                text=t,
                command=lambda t=t: self.preencher_e_buscar(t),
            )
            btn.pack(side="left", padx=5)

        periodos = {
            "1M": "1mo",
            "6M": "6mo",
            "YTD":"ytd",
            "1A": "1y",
            "MAX":"max"
        }

        self.periodo = "1mo"  
        self.botoes_periodos = {}

        frame_periodo = tk.Frame(self.frame, bg="#F0EEEE")
        frame_periodo.pack(pady=5)

        self.intervalo = "1d"
        self.botoes_intervalo = {}

        frame_intervalo = tk.Frame(self.frame,bg="#444444")
        frame_intervalo.pack(pady=5)

        intervalos = {
            "1D":"1d",
            "1W":"1wk",
            "1M":'1mo'
        }
        for nome, valor in intervalos.items():
            btn = tk.Button(
                frame_intervalo,
                text=nome,
                command=lambda v=valor: self.set_intervalo(v),
                bg="#2c2c2c",
                fg="white"
            )
            btn.pack(side="left", padx=5)
            self.botoes_intervalo[valor] = btn

        self.botoes_intervalo[self.intervalo].config(bg="#4CAF50")

        for nome, valor in periodos.items():
            btn = tk.Button(
                frame_periodo,
                text=nome,
                command=lambda v=valor: self.set_periodo(v),
                bg="#2c2c2c",
                fg="white"
            )
            btn.pack(side="left", padx=5)
            self.botoes_periodos[valor] = btn

    def pegarTik(self):
        return self.caixa_input.get().upper()

    def preencher_e_buscar(self, ticker):
        self.caixa_input.delete(0, tk.END)
        self.caixa_input.insert(0, ticker)
        self.comando_buscar()

    def set_periodo(self, valor):
        self.periodo = valor

        for btn in self.botoes_periodos.values():
            btn.config(bg="#2c2c2c")

        self.botoes_periodos[valor].config(bg="#4CAF50")
        self.comando_buscar()
    def set_intervalo(self, valor):
        self.intervalo = valor

        for btn in self.botoes_intervalo.values():
            btn.config(bg="#2c2c2c")

        self.botoes_intervalo[valor].config(bg="#4CAF50")

        self.comando_buscar()  

    def pegarPeriodo(self):
        return self.periodo
    
    def pegarIntervalo(self):
        return self.intervalo