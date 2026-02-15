from flask import Flask, render_template, request
import os

app = Flask(__name__)


def resolve_upload_folder() -> str:
    preferred_folder = os.path.join("static", "uploads")
    fallback_folder = os.path.join("/tmp", "uploads")

    try:
        os.makedirs(preferred_folder, exist_ok=True)
        return preferred_folder
    except OSError:
        os.makedirs(fallback_folder, exist_ok=True)
        return fallback_folder


app.config['UPLOAD_FOLDER'] = resolve_upload_folder()


@app.route("/")
def index():
    couple_info = {
        "title": "Pipe y Gaby",
        "subtitle": "Una página para celebrar lo bonito de nosotros",
        "you": {
            "name": "Pipe",
            "about": "Soy detallista, soñador y feliz de compartir cada momento contigo.",
            "likes": ["Salir a caminar", "Escuchar música", "Tomar fotos juntos"],
        },
        "partner": {
            "name": "Gaby",
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


@app.route("/health")
def health():
    return {"status": "ok"}, 200


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('photo')
        if file and file.filename:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template("upload.html", message="Foto subida exitosamente!")
    return render_template("upload.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
