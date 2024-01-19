from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)

# Главная страница
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


