from jinja2 import Template
import json
import urllib
import jwt
import os

# JWT Key
key = "aversion-chute-freeway-corporal"
algo = "HS256"

def getHelp(event):
 email = ''.join(event['email'])
 template = """
 <p>Your request has been submitted.</p>
 <p>You will receive an email at: %s</p>
 <p>This might take a reaaaaaaally long time though (forever).</p>
 """ % (urllib.parse.unquote(email).replace("<", "&lt;").replace(">", "&gt;"))
 msg = Template(template).render(dir=dir, help=help, locals=locals, globals=globals, open=open)
 msg = msg[:-len(msg)+700]
 return msg

def login(event):
 if (event['username'] == "tim"):
 if (event['password'] == "berners-lee"):
 payload = {
 'username': 'tim',
 'role': 'user'
 }
 jwt_token = jwt.encode(payload, key, algo)
 return jwt_token
 else:
 return "Login Failed"
 else:
 return "Login Failed"

flag = "muLtiStagingIT710-12"

def verify(event):
 if ("token" in event):
 try:
 payload = jwt.decode(event['token'], key, algorithms=[algo])
 if (payload['role'] == "admin"):
 return flag
 else:
 return "Insufficient Privileges"
 except (jwt.DecodeError, jwt.ExpiredSignatureError):
 return "Invalid Token"

def handle(event):
 res = "Undefined Error"
 if event['action'] == "help":
 res = getHelp(event)

 elif event['action'] == "login":
 res = login(event)

 elif event['action'] == "verify":
 res = verify(event)
 return res

def lambda_handler(event, context):
 return {
 'statusCode': 200,
 'body': handle(event)
 }

