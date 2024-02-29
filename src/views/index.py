import tkinter as tk
from tkinter import messagebox

import sys
from  os.path import dirname,abspath
current_dir = dirname(dirname(abspath(__file__)))
sys.path.append(current_dir)
from models.add import event2calender
from models.build import Event,Recurrence,Data,DataTime,Attendees


class Home(tk.Tk):
    def __init__(self, largura=300, altura=400):
        super().__init__()
        self.title("Cadastrando Eventos")
        self.geometry(f"{largura}x{altura}")
        self.resizable(False, False)
        self.criar_interface()
        

    def enviar_dados(self):
        dados = [self.entry1.get(), self.entry2.get(), self.entry3.get(), self.entry4.get(), self.entry5.get(), self.entry6.get(),self.entry7.get()]
        #print("Dados enviados:", dados)
        if '' in dados:
            messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")
        
        else:
            
            try:
                summary = dados[0]
                location = dados[1]
                description = dados[6]
                br_data = dados[2] + " " + dados[3] + ":00"
                start_dateTime = DataTime(br_data)
                br_data = dados[2] + " " + dados[4] + ":00"
                end_dateTime = DataTime(br_data)
                attendees = Attendees(dados[5])
                recurrence = Recurrence(Data(dados[2]),Data(dados[2]))
                
                print([summary,location,description,start_dateTime,end_dateTime,attendees,recurrence])
                
                event = Event(summary,location,description,start_dateTime,end_dateTime=end_dateTime,recurence=recurrence,attendees=attendees)
                resposta = messagebox.askyesno("Confirmação", "Deseja realmente enviar os dados?")
                
                if resposta:
                    print("Dados enviados:", dados)
                    event2calender(token_path="token.json",evento=event)
                    messagebox.showinfo("Sucesso", "Cadastrado com sucesso!")
              
            except:
                messagebox.showerror("Erro", "Por favor, preencha todos os campos corretamente.")
        

    def criar_interface(self):
        # Criando um frame para conter os elementos
        frame = tk.Frame(self)
        frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        label1 = tk.Label(frame, text="Titulo")
        label1.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.entry1 = tk.Entry(frame)
        self.entry1.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        label2 = tk.Label(frame, text="Local")
        label2.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry2 = tk.Entry(frame)
        self.entry2.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        label3 = tk.Label(frame, text="Data (ex: 01/01/2001)")
        label3.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.entry3 = tk.Entry(frame)
        self.entry3.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        label4 = tk.Label(frame, text="Inicio (ex: 09:30)")
        label4.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.entry4 = tk.Entry(frame)
        self.entry4.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

        label5 = tk.Label(frame, text="Fim (ex: 11:00)")
        label5.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.entry5 = tk.Entry(frame)
        self.entry5.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

        label6 = tk.Label(frame, text="Participantes (a@a.a, b@b.b)")
        label6.grid(row=5, column=0, padx=10, pady=10, sticky="e")
        self.entry6 = tk.Entry(frame)
        self.entry6.grid(row=5, column=1, padx=10, pady=10, sticky="ew")
        
        label7 = tk.Label(frame, text="Descrição (Reunião para...)")
        label7.grid(row=6, column=0, padx=10, pady=10, sticky="e")
        self.entry7 = tk.Entry(frame)
        self.entry7.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

        btn_enviar = tk.Button(frame, text="Enviar", command=self.enviar_dados)
        btn_enviar.grid(row=7, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    # Exemplo de uso
    tela = Home()
    tela.mainloop()
#leviathantempest70@gmail.com