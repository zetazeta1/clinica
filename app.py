from flask import Flask, render_template, request,redirect,url_for

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('menu.html')

@app.route('/consul')
def consulta():
    return render_template('consultas.html')

@app.route('/reg',methods=['POST'])
def contato():    
    return redirect('https://n067bp2pw2.execute-api.us-east-1.amazonaws.com/')

@app.route('/infos')
def info():
    return render_template('informações.html')

if __name__=='__main__':
    app.run(debug=True)