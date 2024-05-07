from flask import Flask
from views import views
# das hier ist einfach alles boiler code. Ändere am besten nichts an den
# Variablenamen oder an den Dateinamen von den Python Dateien, dann gehen bestimmt
# Dinge kaputt.

# die Kommentare auf Englisch sind von mir, als ich das hier das erste mal geschrieben hab

# den Ordner __pychache__ kannst du übrigens ignorieren, den legt Python automatisch
# an, wenn man Dinge hin und her importiert

app = Flask(__name__)

app.register_blueprint(views, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True)  # automatically reruns the website if code is changed

