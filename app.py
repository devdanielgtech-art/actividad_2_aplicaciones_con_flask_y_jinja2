from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui_cambiala'

# Ruta principal - página de inicio (portafolio)
@app.route('/')
def index():
    # Datos de ejemplo para el portafolio
    proyectos = [
        {'nombre': 'App de Tareas', 'descripcion': 'Aplicación para gestionar tareas diarias', 'tecnologias': 'Flask, SQLite, Bootstrap'},
        {'nombre': 'Juego en Python', 'descripcion': 'Juego interactivo por consola', 'tecnologias': 'Python, POO'},
        {'nombre': 'Sitio de Recetas', 'descripcion': 'Plataforma para compartir recetas', 'tecnologias': 'Flask, Jinja2, Bootstrap'},
        {'nombre': 'API de Clima', 'descripcion': 'Consumo de API de clima', 'tecnologias': 'Python, Requests, JSON'}
    ]
    
    habilidades = [
        {'nombre': 'Python', 'nivel': '90%'},
        {'nombre': 'Flask', 'nivel': '85%'},
        {'nombre': 'HTML/CSS', 'nivel': '80%'},
        {'nombre': 'Bootstrap', 'nivel': '75%'},
        {'nombre': 'JavaScript', 'nivel': '70%'},
        {'nombre': 'Git/GitHub', 'nivel': '85%'}
    ]
    
    return render_template('index.html', proyectos=proyectos, habilidades=habilidades)

# Ruta para el formulario de contacto
@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        mensaje = request.form.get('mensaje')
        
        # Aquí normalmente enviarías un correo o guardarías en BD
        print(f"Nuevo mensaje de: {nombre} - {email}")
        print(f"Mensaje: {mensaje}")
        
        flash('¡Mensaje enviado correctamente! Me pondré en contacto contigo pronto.', 'success')
        return redirect(url_for('contacto'))
    
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)