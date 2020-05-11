
# TODO: Try not use import *
# https://stackoverflow.com/questions/2386714/why-is-import-bad
from newspaper import *
from flask import Flask,redirect,url_for,request,render_template,make_response,session,abort,flash
from werkzeug.utils import secure_filename

def main():
    url = "https://timesofindia.indiatimes.com/india/hyderabad-encounter-all-four-accused-in-hyderabad-vet-rape-murder-case-killed-in-encounter/articleshow/72392991.cms"
    article_name = Article(url, language="en")
    article_name.download()
    article_name.parse()
    # TODO: Where are 'text' and 'title' used?
    text = article_name.text
    title = article_name.title
    
    
    app = Flask(__name__)
    @app.route('/article')
    def show_ar():
        # TODO: return(render_template('article.html', article_name = title, article_text = text))
        return(render_template('article.html'))
    app.run(debug=True)
    # TODO: You are just showing an empty page. You needed to get the content from webpage and show it in your own different format



if __name__ == '__main__': 
    main() 
