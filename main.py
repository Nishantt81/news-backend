from GoogleNews import GoogleNews

googlenews = GoogleNews()
googlenews.set_lang('en')  


topic = input("Which news topic do you want? : ")


googlenews.search(topic)
results = googlenews.result()

print(results)

news_data = []


if results:
    for news in results[:10]:  # Limit to the top 10 results
        news_data.append({
            "title": news['title'],
            "desc": news.get('desc', ''),  # Description
            "link": news['link'],
            "img": news.get('img', '')    # Add the image URL if available
        })
else:
    news_data = {"error": f"No news found for '{topic}'."}

print(news_data)
