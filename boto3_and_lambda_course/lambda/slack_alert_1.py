import requests
import json

slack_web_hook = "https://hooks.slack.com/services/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"

slack_message = {'text': 'EC2 Instance Stopped'}
resp = requests.post(slack_web_hook, data=json.dumps(slack_message))