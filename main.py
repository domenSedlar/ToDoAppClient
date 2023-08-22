from client.client import Client
from son import Files

client = Client()
son = Files()

# Updating
client.opend()
b = client.l[0]
c = client.l[1]
if b != "c":
    print("CLIENT ONLINE")
    son.upd_ls(b)
    son.upd_tsk(c)

from start import Panther

app = Panther()

app.run()
