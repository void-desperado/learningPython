def showMessages(messages):
    for message in messages:
        print(message)

def sendMessages(messagesPending,messagesSent):
    while messagesPending:
        messagesSent.append(messagesPending.pop())

messagesToBeSent=["Hello","How are you","What are you doing"]
messagesThatAreSent=[]

showMessages(messagesToBeSent)
sendMessages(messagesToBeSent[:],messagesThatAreSent)
showMessages(messagesThatAreSent)
