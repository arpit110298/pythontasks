from newspaper import *
from flask import Flask,redirect,url_for,request,render_template,make_response,session,abort,flash
from werkzeug.utils import secure_filename

def main():
    url = "https://timesofindia.indiatimes.com/india/hyderabad-encounter-all-four-accused-in-hyderabad-vet-rape-murder-case-killed-in-encounter/articleshow/72392991.cms"
    article_name = Article(url, language="en")
    article_name.download()
    article_name.parse()
    text = article_name.text
    title = article_name.title
    
    
    app = Flask(__name__)
    @app.route('/article')
    def show_ar():
        return(render_template('article.html'))
    app.run(debug=True)



if __name__ == '__main__': 
    main() 