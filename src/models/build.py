# Refer to the Python quickstart on how to setup the environment:
# https://developers.google.com/calendar/quickstart/python
# Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
# stored credentials.


def Event(summary:str="Reunião",
                location:str="Discord",
                description:str="Descrição não Informada",
                start_dateTime:str='2015-05-28T09:00:00-07:00',
                timeZone:str="America/Sao_Paulo",
                end_dateTime:str='2015-05-28T17:00:00-07:00',
                recurence:list=['RRULE:FREQ=DAILY;COUNT=2'],
                attendees=[
                {'email': 'lpage@example.com'},
                {'email': 'sbrin@example.com'}
                ]):
    """
    Constroi um evento seguindo as normas do Google API
    
    Args:
        summary::str: Título do evento
        location::str: Localização onde será realizado o evento
        description::str: Descrição sobre o evento
        start_dateTime:: Data e Hora de incio do evento
        TimeZone::str: Tipo de Fuso Horário
        end_dateTime::str: Data e Hora do encerramento do Evento
        recurence::list: Recorrência
        attendees::list: Lista de dicionários contendo os emails de todos os Participantes
        
    Return
        event::dict: Dicionário contendo todos os metadados necessários para criar um evento do Google Calender API
    """    

    event = {
    'summary': summary,
    'location': location,
    'description': description,
    'start': {
        'dateTime': start_dateTime,
        'timeZone': timeZone,
    },
    'end': {
        'dateTime': end_dateTime,
        'timeZone': timeZone,
    },
    'recurrence': recurence,
    'attendees': attendees,
    "reminders": {
            "useDefault": False,
            "overrides": [
                {
                    "method": "popup",
                    "minutes": 10
                },
                {
                    "method": "popup",
                    "minutes": 1440
                }
            ]
        },
    }
    
    return event

"""
'reminders': {
        'useDefault': False,
        'overrides': [
        {'method': 'email', 'minutes': 24 * 60},
        {'method': 'popup', 'minutes': 10},
        ],
    }
"""

def Recurrence(start_date: str, end_date: str, freq: str = 'None'):
    """
    Constrói uma string de recorrência RRULE com base no intervalo de tempo fornecido.

    Args:
        start_date (str): Data de início no formato 'YYYY-MM-DD'.
        end_date (str): Data de término no formato 'YYYY-MM-DD'.
        freq (str): Frequência de recorrência (padrão: 'DAILY').
            'None': O evento ocorre apenas uma vez
            "DAILY": O evento ocorre diariamente.
            "WEEKLY": O evento ocorre semanalmente.
            "MONTHLY": O evento ocorre mensalmente.
            "YEARLY": O evento ocorre anualmente.

    Returns:
        str: String de recorrência RRULE.
    """
    
    if freq != 'None':
    
        recurrence = f'RRULE:FREQ={freq};'
        recurrence += f'UNTIL={end_date}T235959Z;'
        recurrence += f'DTSTART={start_date}T000000Z;'
        recurrence += f'WKST=SU'

    else:
        recurrence = f"RRULE:UNTIL={end_date}T235959Z;DTSTART={start_date}T000000Z;WKST=SU"

    return recurrence


def DataTime(data_br:str="28/02/2024 14:07:00"):
    from datetime import datetime, timedelta

    # Defina sua data e hora no formato brasileiro
    

    # Converta a string para um objeto datetime
    data_obj = datetime.strptime(data_br, "%d/%m/%Y %H:%M:%S")

    # Adicione o deslocamento de fuso horário (no caso do Brasil, -03:00)
    data_obj -= timedelta(hours=3)

    # Formate a data para o formato do Google Calendar
    data_google = data_obj.strftime("%Y-%m-%dT%H:%M:%S-03:00")

    return data_google

def Data(data_br:str="28/02/2024"):
    from datetime import datetime
    return datetime.strptime(data_br,"%d/%m/%Y").strftime("%Y-%m-%d")
    
    
    

def Attendees(email_str_csv:str):
    attendees = []
    
    email_list = email_str_csv.split(",")
    print(email_list)
    
    for email in email_list:
        dic = {"email": email}
        
        attendees.append(dic)
        
    
    return attendees
    



if __name__ == "__main__":
    print(Recurrence(Data("28/02/2024"),Data("28/02/2024")))
    
    
    #print(Recurrence("2024-02-28","2024-02-29","None"))
