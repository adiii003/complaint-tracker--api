#this is mainly the function called to get the email sent message with these values which are printed accordingly
#this is a mock and no main email is sent as written below to make that happen we need to sue the SMTP logic

def send_email_notification(to_email: str, subject: str, body: str):
    print("Mock Email Sent:")
    print(f"To: {to_email}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    # Use real SMTP logic here if needed-  sample mail transfer protocol
