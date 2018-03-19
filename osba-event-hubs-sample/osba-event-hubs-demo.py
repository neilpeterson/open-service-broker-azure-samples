from eventhubs import EventHubClient, Sender, EventData

# Event Hubs
EH_CONNECTION_STRING = os.environ['EH_CONNECTION_STRING']

sender = Sender()
client = EventHubClient(EH_CONNECTION_STRING).publish(sender).run_daemon()

sender.send(EventData(hello-osba))

client.stop