from auth import authenticate
from googleapiclient.discovery import build


def get_gmail_service():
    creds = authenticate()
    service = build('gmail', 'v1', credentials=creds)
    return service

def search_emails(query):
    service = get_gmail_service()
    results = service.users().messages().list(userId='me', q=query).execute()
    return results.get('messages', [])

def get_email_content(message_id):
    service = get_gmail_service()
    message = service.users().messages().get(userId='me', id=message_id).execute()
    return message['snippet']