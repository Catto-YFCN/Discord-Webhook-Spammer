from discord_webhook import DiscordWebhook

counter = 0
url= input("Webhook URL: ")
content= input("Input message: ")
print("Starting..")
while True:
    try:
        counter += 1
        print("Successfully sent", "'",content,"' | " "Messages sent:", counter)
        DiscordWebhook(
            url=url, rate_limit_retry=True,
            content=content
            ).execute()
    except KeyboardInterrupt:
           break
           #Doesn't work but idk what else to put for except
