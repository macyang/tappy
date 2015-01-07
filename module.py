import json
import requests

tapServer = 'http://localhost:8090/'

def connect(server):
  global tapServer
  tapServer = server

def createContext(contextName):
  global tapServer
  q = tapServer + 'contexts/' + contextName
  r = requests.post(q)
  return r

def deleteContext(contextName):
  global tapServer
  q = tapServer + 'contexts/' + contextName
  r = requests.delete(q)
  return r

def run(contextName, classPath, conf, sync=True):
  global tapServer
  q = tapServer + 'jobs?' + 'appName=tap&context=' + contextName + '&classPath=' + classPath
  if (sync):
    q += '&sync=true'
  else:
    q += '&sync=false'
  r = requests.post(q, data = conf)
  return json.loads(r.text)

if __name__ == "__main__":
  import sys
  run(sys.argv[1], sys.argv[2], True)
