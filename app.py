from flask import Flask, request, jsonify
from flask_cors import CORS
from GoogleNews import GoogleNews

app = Flask(__name__)
CORS(app)  

@app.route('/get-news', methods=['POST'])
def get_news():
    data = request.json 
    topic = data.get('topic', '')  
    
    if not topic:
        return jsonify({"error": "Topic is required"}), 400
    
    
    googlenews = GoogleNews()
    googlenews.set_lang('en')
    googlenews.search(topic)
    results = googlenews.result()

    if results:
        news_list = [
            {
                "title": news.get("title", ""), 
                "desc": news.get("desc", ""), 
                "link": news.get("link", ""),
                "img": news.get("img", "")  
            }
            for news in results[:10] 
        ]
        return jsonify({"topic": topic, "news": news_list}), 200
    else:
        return jsonify({"topic": topic, "news": []}), 404

if __name__ == '__main__':
    app.run(debug=True)
