from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Geçici olarak görevleri tutacak bir liste (Veritabanı yapana kadar)
tasks = [
    {'id': 1, 'title': 'Flask Öğren', 'completed': False},
    {'id': 2, 'title': 'Git Arayüzünü Kullan', 'completed': True}
]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)