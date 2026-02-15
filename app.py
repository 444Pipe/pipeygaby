from flask import Flask, render_template, request
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


@app.route("/")
def index():
    couple_info = {
        "title": "Nuestra Historia",
        "subtitle": "Una página para celebrar lo bonito de nosotros",
        "you": {
            "name": "Tu Nombre",
            "about": "Soy detallista, soñador y feliz de compartir cada momento contigo.",
            "likes": ["Salir a caminar", "Escuchar música", "Tomar fotos juntos"],
        },
        "partner": {
            "name": "Nombre de Tu Novia",
            "about": "Eres dulce, fuerte y la persona que ilumina mis días.",
            "likes": ["Ver atardeceres", "Reír sin parar", "Los pequeños detalles"],
        },
        "timeline": [
            {"date": "14 Feb 2026", "event": "Seguimos construyendo recuerdos increíbles."},
            {"date": "Nuestro aniversario", "event": "Un día especial que siempre guardamos en el corazón."},
            {"date": "Próximo viaje", "event": "Un nuevo destino para vivirlo juntos."},
        ],
        "message": "Gracias por ser mi hogar favorito.",
    }

    return render_template("index.html", data=couple_info)


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['photo']
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template("upload.html", message="Foto subida exitosamente!")
    return render_template("upload.html")


if __name__ == "__main__":
    app.run(debug=True)
