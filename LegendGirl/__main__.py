from .core.clients import *

async def main():
  apps = [Client1,Client2,Client3,Client4]
  compose([apps])

Client1.run(main())
