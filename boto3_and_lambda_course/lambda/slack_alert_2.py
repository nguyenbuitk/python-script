import requests
import json

slack_web_hook = "https://hooks.slack.com/services/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"

def send_slack(event, context):
    print(str(event))
    slack_message = {'text': 'EC2 Instance Stopped'}
    resp = requests.post(slack_web_hook, data=json.dumps(slack_message))
    return resp.text