from tasks import create_reminder_from_email, send_daily_calendar_summary


def main():
    # Test the send_daily_calendar_summary task
    send_daily_calendar_summary()

    # Test the create_reminder_from_email task
    query = "subject:meeting"
    create_reminder_from_email(query)

if __name__ == "__main__":
    main()