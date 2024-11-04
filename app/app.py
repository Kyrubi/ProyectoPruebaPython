from flask import Flask , render_template, request

app = Flask(__name__)

#Decorador
@app.route('/') 
#Vista
def index():
    # Interpolacion
    cursos = ['html', 'css', 'js', 'python', 'c++']
    data = {
        'titulo':'Index',
        'bienvenido':'¡Saludos!',
        'cursos':cursos,
        'numero_cursos': len(cursos)
    }

    return render_template('index.html', data = data)

#URL's Dinamicas 
#Decorador
@app.route('/contacto/<nombre>/<int:edad>')
#Vista
def contacto(nombre, edad): 
    data = {
        'titulo':'contacto', 
        'nombre':nombre,
        'edad': edad
    }
    return render_template('contacto.html', data = data)

#QueryString
def query_string(): 
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    print(request.args.get('param2'))
    return "WA"

#Manejo de errores
def pagina_not_found(error): 
    return render_template('404.html'), 404



if __name__ == '__main__':
    app.add_url_rule('/query_string', view_func = query_string)
    app.run(debug = True, port = 5000)