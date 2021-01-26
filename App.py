#Envisioned and defined by Razvan Manescu

from waitress import serve
from controller import Controller

serve(Controller.app, host='0.0.0.0', port=8080)
