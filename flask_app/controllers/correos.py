from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.correo import Correo


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/validacion',methods=['POST'])
def validacion():
    if not Correo.is_valid(request.form):
        return redirect('/')
    Correo.guardar(request.form)
    return redirect('/resultados')


@app.route('/resultados')
def results():
    return render_template("resultados.html",correos=Correo.get_all())

@app.route('/eliminar/<int:id>')
def eliminar_email(id):
    data = {
        "id": id
    }
    Correo.eliminar(data)
    return redirect('/resultados')