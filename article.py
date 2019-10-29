from newspaper import Article






if __name__=="__main__":
    url="https://politica.elpais.com/politica/2018/06/02/actualidad/1527957135_802248.html"
    article=Article(url)
    article.download()
    article.parse()
    article.nlp()
    print(article.authors)
    print(article.publish_date)
    print(article.keywords)
    print(article.summary)
