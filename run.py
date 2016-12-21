from blog import app
import os

app.secret_key = os.urandom(25)
app.run(debug=True)