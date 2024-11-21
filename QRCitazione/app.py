from flask import Flask, render_template
import quote_random

app = Flask(__name__)

@app.route('/')
def home():
    qr = quote_random.quote_random()
    quote = "Errore citazione"
    author = "Riprova"

    try:
        quote_author = qr.quote_and_author()
        if quote_author:
            quote = quote_author[1]
            author = quote_author[0]
        else:
            quote = "Quote Error"
            author = ""
    except:
        quote = "Errore"
        author ="Riprova"

    return render_template('index.html', quote=quote, author=author)

if __name__ == '__main__':
    app.run(debug=True)
