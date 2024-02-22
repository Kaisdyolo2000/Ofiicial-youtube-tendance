# Import des modules Flask et autres dépendances
import os
import requests
import schedule
import time
from flask import Flask, render_template, session, request, redirect, url_for, jsonify
from dotenv import load_dotenv
from google_auth_oauthlib.flow import Flow
import random

# Initialisation de l'application Flask
app = Flask(__name__)
app.secret_key = os.urandom(24)

# Configuration OAuth 2.0
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']

# Configuration de l'objet Flow pour l'authentification avec Google
flow = Flow.from_client_secrets_file(
    'client_secrets.json',
    scopes=SCOPES,
    redirect_uri=REDIRECT_URI)