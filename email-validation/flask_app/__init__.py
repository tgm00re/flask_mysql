from flask import Flask, session
app = Flask(__name__)
app.secret_key = "Do you have the key..."