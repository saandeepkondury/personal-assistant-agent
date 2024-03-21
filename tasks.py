from calendar_utils import get_upcoming_events
from gmail_utils import get_email_content, search_emails


def send_daily_calendar_summary():
    events = get_upcoming_events()
    summary = "Upcoming events:\n"
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        summary += f"{start} - {event['summary']}\n"
    # Logic to send the summary via email or other means
    print(summary)  # Temporary print statement for testing

def create_reminder_from_email(query):
    messages = search_emails(query)
    for message in messages:
        content = get_email_content(message['id'])
        # Logic to create a reminder based on the email content
        print(content)  # Temporary print statement for testing