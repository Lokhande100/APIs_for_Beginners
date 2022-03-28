from twilio.rest import Client


client=Client("AC3023525a59e26a8d37caac3862e738db","f91183ea11b04012fe507b6a004c4a45")

#for msg in client.messages.list():
    #print(msg.body)

msg=client.messages.create(
    to="+918999633540",
    from_="+18597192560",
    body="hello message from twilio",
)
print(f"created new message:{msg.sid}")