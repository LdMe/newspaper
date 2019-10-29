import newspaper
import sys
import os
class Periodico:
        def __init__(self,url):
                self.url=url
                print("conectando a "+url)
                self.news= newspaper.build(url,language='es',memoize_articles=False)
                print(str(len(self.news.articles))+ " articulos encontrados\n")

        

                
                
        def findArticles(self,string):
                possibles=[]
                possibleNames=[]
                counter=0
                
                for article in self.news.articles:
                        if article.title!=None:
                                if string.lower() in article.title.lower() and not article.title in possibleNames:#.split(" "):
                                        
                                        possibles.append(article.url)
                                        possibleNames.append(article.title)
                                        art=self.downloadArticle(article.url)
                                        
                                        print(str(counter)+"- "+article.title+"\n"+article.url)
                                        print("\n"+str(art.keywords)+"\n------------\n")
                                        counter+=1
                if(counter==0):
                        print("no se han encontrado articulos relacionados")
                        return []
                return possibles
        def saveArticle(self,article,direct="articles"):
                print(direct)
                filename=direct+"/"+article.title+".txt"
                file=open(filename,'w+')
                file.write(str(article.title)+"\n")
                file.write("\n-----------------------------------------\n-----------------------------------------\n")
                file.write("autor(es):\n"+str(article.authors)+"\n")
                file.write("\n-----------------------------------------\n")
                file.write("fecha:\n"+str(article.publish_date)+"\n")
                file.write("\n-----------------------------------------\n")
                file.write("url:\n"+article.url+"\n")
                file.write("\n-----------------------------------------\n")
                file.write("palabras clave:\n"+str(article.keywords)+"\n")
                file.write("\n-----------------------------------------\n")
                file.write(article.text)
                file.close()
                
        def showTitulars(self):
                for article in self.news.articles:
                        if article.title!=None and article.title.strip()!="":
                                print(article.title+ "\n-------------------\n")
                                
        def findArticle(self,string):
                possibles=[]
                possibleNames=[]
                counter=0
                
                for article in self.news.articles:
                        if article.title!=None:
                                if string.lower() in article.title.lower() and not article.title in possibleNames:
                                        
                                        possibles.append(article.url)
                                        possibleNames.append(article.title)
 
                                        print(str(counter)+"- "+article.title+"\n"+article.url)
                                        print("\n------------\n")
                                        
                                        counter+=1
                if(counter==0):
                        print("no se han encontrado articulos relacionados")
                        return -1
                num=int(input("introduce el numero de articulo\n"))
                return self.downloadArticle(possibles[num])

        def comparePapers(self,p2,art):
       
                dir1="articles/"+art
                makeDir(dir1)
                dir2=dir1+"/"+self.url.replace("/","-")
                dir3=dir1+"/"+p2.url.replace("/","-")
                makeDir(dir2)
                makeDir(dir3)
                art1=self.findArticles(art)
                print(len(art1))
                for i in art1:
                        self.saveArticle(self.downloadArticle(i),dir2)
                art2=p2.findArticles(art)
                print(len(art1))
                for i in art2:
                        p2.saveArticle(p2.downloadArticle(i),dir3)

                print("done")
                return
            
            
        
        def downloadArticle(self,url):
                article=newspaper.Article(url)
                article.download()
                article.parse()
                article.nlp()
                return article
        def showArticle(self,article):
                print("\n#########################################")
                print("\n#########################################\n")
                print(str(article.title)+"\n")
                print("\n#########################################\n")
                print(str(article.authors)+"\n")
                print(article.url+"\n")
                print("\n-----------------------------------------\n")
                print(str(article.keywords)+"\n")
                print("\n-----------------------------------------\n")
                print(article.text)
                print("\n#########################################")
                print("\n#########################################\n")
                self.saveArticle(article)


def makeDir(directory):
            if not os.path.exists(directory):
                os.makedirs(directory)

if __name__ == "__main__":
        if(len(sys.argv)>4):
                p1=Periodico(sys.argv[1])
                p2=Periodico(sys.argv[2])
                p1.comparePapers(p2,sys.argv[3])
                
        elif(len(sys.argv)>3):
                p=Periodico(sys.argv[1])
                art=p.findArticle(sys.argv[2])
                if(art!=-1):
                        p.showArticle(art)
        elif(len(sys.argv)>2):
                if(sys.argv[2]=="c"):
                    p1=Periodico("https://elpais.com/")
                    p2=Periodico("https://actualidad.rt.com/")
                    p1.comparePapers(p2,sys.argv[1])
            
                elif(sys.argv[2]=="f"):
                        p=Periodico("https://elpais.com/")
                        art=p.findArticle(sys.argv[1])
                        if(art!=-1):
                                p.showArticle(art)
                elif(sys.argv[2]=="s"):
                        p=Periodico(sys.argv[1])
                        p.showTitulars()
                else:
                        p=Periodico(sys.argv[1])
                        p.findArticles(sys.argv[2])
        elif(len(sys.argv)>1):
                
                    
                    
                if(sys.argv[1]=="s"):
                        p=Periodico("https://elpais.com/")
                        p.showTitulars()
                        
                p=Periodico("https://elpais.com/")
                p.findArticles(sys.argv[1])
        

"""for category in news.category_urls():
    print(category+"\n#############\n")
"""

