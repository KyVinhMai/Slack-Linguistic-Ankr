import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
#I want all the events to be sent to this endpoint
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'],'/slack/events',app)

client = slack.WebClient(token = os.environ['SLACK_TOKEN'])

BOT_ID = client.api_call("auth.test")['user_id']

@slack_event_adapter.on('message')
def message(payload):
    event = payload.get("event", {})
    """
    "event" key will return information about the event.
     If event does not exist, return a dictionary
    """
    channel_id = event.get('channel') # Get the location of where the message was sent from
    user_id = event.get("user") #Grabs user id from event key
    text = event.get("text")

    if BOT_ID != user_id:
        client.chat_postMessage(channel= channel_id, text= text)


if __name__ == "__main__":
    app.run(debug=True, port = 5002) # Changed port to 5002 because 5000 was not working