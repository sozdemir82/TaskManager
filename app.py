from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Geçici veri listemiz (Sayfa yenilendiğinde veriler kalır ama sunucu durursa sıfırlanır)
tasks = [
    {'id': 1, 'title': 'Flask Projesini Başlat', 'completed': False},
    {'id': 2, 'title': 'Git Arayüzünü Çöz', 'completed': True}
]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    if title:
        # Yeni bir ID oluştur (Listenin uzunluğuna göre)
        new_id = tasks[-1]['id'] + 1 if tasks else 1
        tasks.append({'id': new_id, 'title': title, 'completed': False})
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    global tasks
    # ID'si eşleşen görevi listeden filtreleyerek çıkarıyoruz
    tasks = [t for t in tasks if t['id'] != task_id]
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed'] # Durumu tersine çevir (True/False)
            break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)