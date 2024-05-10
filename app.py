from flask import Flask, render_template, send_file

app = Flask(__name__)

# Page d'accueil de l'application
@app.route('/')
def home():
    # Informations sur la vidéo
    video_info = {
        'name': 'excel_formation.mp4'  # Nom de la vidéo
    }
    # Affichage de la page HTML avec les informations sur la vidéo
    return render_template('index.html', video_info=video_info)

# Route pour télécharger la vidéo
@app.route('/download')
def download_video():
    # Chemin vers la vidéo
    video_path = "static/excel_formation.mp4"
    # Téléchargement du fichier vidéo
    return send_file(video_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
