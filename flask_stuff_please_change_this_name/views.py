from flask import Blueprint, render_template, request, make_response, redirect


views = Blueprint("views", __name__)

# Wenn man das erste mal auf die Website kommt, wird man hiermit automatisch
# zur URL .../home weitergeleitet (deswegen redirect). request.url ist denke ich
# die grundlegende URL. Für uns ist es jetzt erstmal wahrscheinlich 127.0.0.1:5000,
# das ist dann ein lokaler Server auf deinem Gerät. 
@views.route("/")
def page_0():
    return redirect(request.url + "home")

# ich finde der Kommentar von mir hier von früher beschreibt es ziemlich gut.
# Wir haben noch nicht über function decorators gesprochen, das könntest du dir selber
# anschauen oder einfach hinnehmen, dass es so funktioniert.

@views.route("/home") # whenever this route is hit it the decorator calls the function below it 
def home():
    return render_template("/home.html")

@views.route("/idk_somwhere_else_i_guess")
def this_name_can_be_anything_btw():
    return render_template("/somewhere_else.html")

