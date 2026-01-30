from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
# Bildirim mesajları (flash) için gerekli güvenlik anahtarı
app.secret_key = "super_gizli_anahtar_123"

# Veritabanı kurulumu (Proje ana dizinine db.sqlite oluşturur)
db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Veritabanı Modeli (OOP yapısı)
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    deadline = db.Column(db.String(20))
    completed = db.Column(db.Boolean, default=False)

# Tabloları oluşturma
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    # Görevleri çek ve index.html'e gönder
    todo_list = Todo.query.all()
    return render_template('index.html', tasks=todo_list)

@app.route('/add', methods=['POST'])
def add():
    task_title = request.form.get('title')
    task_deadline = request.form.get('deadline')
    
    # Boş veri kontrolü
    if not task_title or task_title.strip() == "":
        flash("Lütfen bir görev başlığı girin!", "error")
    else:
        new_task = Todo(title=task_title, deadline=task_deadline, completed=False)
        db.session.add(new_task)
        db.session.commit()
        flash("Görev başarıyla eklendi!", "success")
    
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    task = Todo.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        flash("Görev başarıyla silindi.", "info")
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete(task_id):
    task = Todo.query.get(task_id)
    if task:
        task.completed = not task.completed
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)