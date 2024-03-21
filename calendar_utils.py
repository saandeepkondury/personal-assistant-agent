from googleapiclient.discovery import build
from auth import authenticate

def get_calendar_service():
    creds = authenticate()
    service = build('calendar', 'v3', credentials=creds)
    return service

def get_upcoming_events(max_results=10):
    service = get_calendar_service()
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=max_results, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    return events