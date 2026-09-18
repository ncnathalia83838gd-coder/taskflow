from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import User, Task

main = Blueprint('main', __name__)

@main.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    return redirect(url_for('main.login'))

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Usuario ou senha invalidos.', 'error')
    
    return render_template('login.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if User.query.filter_by(username=username).first():
            flash('Nome de usuario ja existe.', 'error')
            return redirect(url_for('main.register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email ja cadastrado.', 'error')
            return redirect(url_for('main.register'))
        
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('Conta criada com sucesso!', 'success')
        return redirect(url_for('main.login'))
    
    return render_template('register.html')

@main.route('/dashboard')
@login_required
def dashboard():
    tasks = Task.query.filter_by(user_id=current_user.id).order_by(Task.created_at.desc()).all()
    return render_template('dashboard.html', tasks=tasks)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@main.route('/task/create', methods=['POST'])
@login_required
def create_task():
    title = request.form.get('title')
    description = request.form.get('description')
    priority = request.form.get('priority', 'medium')
    
    task = Task(title=title, description=description, priority=priority, user_id=current_user.id)
    db.session.add(task)
    db.session.commit()
    
    flash('Tarefa criada com sucesso!', 'success')
    return redirect(url_for('main.dashboard'))

@main.route('/task/<int:task_id>/update', methods=['POST'])
@login_required
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user_id != current_user.id:
        flash('Acesso negado.', 'error')
        return redirect(url_for('main.dashboard'))
    
    status = request.form.get('status')
    if status:
        task.status = status
    
    db.session.commit()
    flash('Tarefa atualizada!', 'success')
    return redirect(url_for('main.dashboard'))

@main.route('/task/<int:task_id>/delete', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user_id != current_user.id:
        flash('Acesso negado.', 'error')
        return redirect(url_for('main.dashboard'))
    
    db.session.delete(task)
    db.session.commit()
    flash('Tarefa removida.', 'success')
    return redirect(url_for('main.dashboard'))
