from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

def adicionar_evento(token_path, evento):
    # Carrega as credenciais do usuário
    creds = Credentials.from_authorized_user_file(token_path)

    # Cria um serviço para acessar a API do Google Calendar
    service = build("calendar", "v3", credentials=creds)

    # Insere o evento no calendário do usuário
    evento_inserido = service.events().insert(calendarId="primary", body=evento).execute()
    print("Evento inserido:", evento_inserido.get("htmlLink"))

if __name__ == "__main__":
    # Token de autenticação
    token_path = "token.json"
    from build import *
    
    inicio_evento = Data("28/02/2024 14:40:0")
    fim_evento = Data("28/02/2024 14:50:0")
    recorrencia = Recurrence("2024-2-28","2024-2-29",'None')
    participantes = Attendees(["mauriciobenjamin700@gmail.com"])
    
    evento = Event("Teste","Teste","Testando Automatizar as Reuniões",inicio_evento,end_dateTime=fim_evento,recurence=recorrencia,attendees=participantes)
    


    # Adiciona o evento ao Google Calendar
    adicionar_evento(token_path, evento)
