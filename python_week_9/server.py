from flask import Flask, request, render_template, redirect
from artists import Artist

app = Flask(__name__)

@app.route('/')
def index():
    artists = Artist.get_all()
    return render_template('index.html', artists = artists )

# Goes to New Artist Page
@app.route('/new_artist')
def new_artist():
    return render_template('new_artist.html')

# Submits New Artist
@app.route('/create_artist', methods=['POST'])
def create_artist():
    Artist.save(request.form)
    return redirect('/')

@app.route('/delete/<int:artist_id>/artist')
def destroy(artist_id):
    data = {
        'id' : artist_id
    }
    Artist.destroy(data)
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)