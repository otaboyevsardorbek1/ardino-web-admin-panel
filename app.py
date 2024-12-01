from flask import Flask, render_template, request, redirect, url_for, flash, session
from arduino import turn_off_arduino  # Arduino boshqaruvi
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Flash xabarlarini ishlatish uchun kerakli kalit

USER_CREDENTIALS = {
    'admin': 'admin'  
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            session['user'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password!', 'danger')
            return redirect(url_for('login'))
    
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        flash('Please login first!', 'warning')
        return redirect(url_for('login'))
    
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/turn_off_arduino')
def turn_off():
    turn_off_arduino()
    flash('Arduino turned off successfully!', 'success')
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port='5000')
