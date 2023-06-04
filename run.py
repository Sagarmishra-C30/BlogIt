from flaskblog import create_app
from news import news

app = create_app()

@app.context_processor
def side_news():
    return news()

if __name__ == "__main__":    
    app.run(debug=True)
