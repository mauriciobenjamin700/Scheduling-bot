import datetime
from json import dump
from os.path import exists

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

"""
Constante SCOPES, que é uma lista de escopos de acesso à API do Google Calendar. Neste caso, é apenas leitura (calendar.readonly), o que significa que o script só pode ler os eventos do calendário, sem modificar nada.
"""


def get_events(num_events:int=10):
    """"""
    """
    Busca os N eventos solicitados no calendario
    """
    
    SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]
    
    creds = None
    """
    Verifica se o arquivo token.json existe no diretório atual. 
    Se existir, ele tenta obter as credenciais do usuário a partir desse arquivo.
    """
    if exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    

    #Se não houver credenciais válidas disponíveis, o script tenta obter novas credenciais.
    if not creds or not creds.valid:
    
        #Se as credenciais expiraram, ele as atualiza.   
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        
        #Caso contrário, inicia o fluxo de autorização para obter as credenciais do usuário.    
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        
        #Salva as credenciais em um arquivo token.json para uso futuro.
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    #Cria um objeto de serviço para interagir com a API do Google Calendar usando as credenciais obtidas.
    try:
        service = build("calendar", "v3", credentials=creds)

        # Call the Calendar API
        
        #Obtém a hora atual em formato UTC
        now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time

        """
        Busca os próximos 10 eventos no calendário do usuário usando o método events().list() do serviço criado
        A consulta é feita para o calendário principal (calendarId="primary") e limitada aos eventos futuros (timeMin=now). Os resultados são ordenados pelo horário de início do evento.
        """
        events_result = (
            service.events()
            .list(
                calendarId="primary",
                timeMin=now,
                maxResults=num_events,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])
        
        cronograma = []
        
        #events2json(events)
    
        if events:
            #print(events) //events é uma lista de dicionários
            for event in events:
                cronograma.append(process_event(event))
                #Para cada evento encontrado, obtém a data e hora de início (se disponível) ou apenas a data, e imprime a data/hora de início e o resumo do evento.
                #start = event["start"].get("dateTime", event["start"].get("date"))
                #cronograma.append([start, event["summary"]])

    except HttpError as error:
        print(f"An error occurred: {error}")
        
    except:
        print("Falhei")
        
    return cronograma


def process_event(event):
    start_datetime = event["start"].get("dateTime", None)
    if start_datetime:
        event_date = start_datetime.split("T")[0]
        event_time = start_datetime.split("T")[1][:5]  # Apenas a hora e minutos
    else:
        event_date = event["start"].get("date", "Data não especificada")
        event_time = "Horário não especificado"

    # Participantes
    attendees = [attendee["email"] for attendee in event.get("attendees", [])]

    # Descrição e título do evento
    event_title = event.get("summary", "Título não especificado")
    event_description = event.get("description", "Descrição não especificada")

    #Imprimir as informações coletadas
    """
    print("Data do evento:", event_date)
    print("Hora do evento:", event_time)
    print("Participantes:", ", ".join(attendees))
    print("Título do evento:", event_title)
    print("Descrição do evento:", event_description)
    print("-" * 50)
    """
    return {"data": event_date,"hora":event_time,"membros":attendees,"evento":event_title,"detalhes":event_description}
    
        
        
def events2json(events, json_name:str='events.json'):
    
    with open(json_name,'w') as json_file:
        dump(events,json_file,indent=4)


if __name__ == "__main__":
  print(get_events())