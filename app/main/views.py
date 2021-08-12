from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news,news_sources
from ..models import News,Sources
# from ..models import Sources

@main.route('/')
def source():
    display_sources = news_sources()
    title = 'Home - Global News Sources'

    search_sources = request.args.get('news_search')
    if search_sources:
        return redirect(url_for('main.source',sources=search_sources))
    else:
        return render_template('source.html',source=display_sources,title = title)

@main.route('/news')
def index():
    sources=news_sources()
    title = 'Home - The home to International news'

    search_news = request.args.get('news_search')
    if search_news:
        return redirect(url_for('main.search',news_feed=search_news))
    else:
        return render_template('index.html',sources=sources,title= title)

@main.route('/search/<news_feed>')
def search(news_feed):
    search_list = news_feed.split(" ")
    title_format = "+".join(search_list)
    searched_news = get_news(title_format)
    title = 'News results'
    search_news = request.args.get('news_search')
    if search_news:
        return redirect(url_for('main.search',news_feed=search_news))
    else:
        return render_template('search.html',related=searched_news,title=title)

@main.route('/source/<sourcesId>')
def articles(sourcesId):
    '''
    View function that displays top stories from a particular source
    '''
    articles= get_top_articles(sourcesId)
    title = f"{sourcesId}"
    header = sourcesId.upper()
    get_keyword = request.args.get('keyword_query')

    if get_keyword:
        return redirect(url_for('main.keyword', keyword_name=get_keyword))
    else:
        return render_template('articles.html', title=title, header=header, article=articles)
