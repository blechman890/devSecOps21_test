def send_email(recipient, subject, /, *, priority="normal", include_signature=True):
    if priority != "normal":
        raise ValueError("Priority must be 'normal'")
    summary = f"\nRrecipient - {recipient}. \nSubject - {subject}. \nPriority - {priority}. \nSignature - {include_signature}."
    print(f"Email Summary: {summary}")

send_email("ilya@example.com", "Test Subject")
send_email("moshe@example.com", "Drill", priority="high")
send_email("recipient="jacob@example.com")


# summary = f"""

# Email summary:

# -----------------------------------------
# Recipient : {recipient}.
# Subject : {subject}.
# Priority : {priority}.
# Signature included : {include_signature}.
# -----------------------------------------
# """
# print(f"Email Summary: {summary}")