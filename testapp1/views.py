from django.shortcuts import render,HttpResponse
from .models import Registration
import pandas as pd
import numpy as np
# Create your views here. 
import imdb
import requests
from tmdbv3api import Movie
from tmdbv3api import TMDb
tmdb = TMDb()
tmdb.api_key = '926646ce8955961847b0a854eaa7ac9e'
movie = Movie()
def HomePageView(request):
    if(request.method=='GET'):
        l=[]
        account_obj=Registration.objects.all()
        for i in account_obj.iterator():
            l.append(str(i.title))
        l=set(l)
        le=len(l)
        return render(request,'index.html',{'l':l})
    else:
        moviename=request.POST['browser']
        print(moviename)
        l=[]
        r1=[]
        r2=[]
        account_obj=Registration.objects.all()
        for i in account_obj.iterator():
            l.append(str(i.title))
        l=set(l)
        le=len(l)
        tl=[]
        pl=[]
        h=0
        movie1=[]
        s1=[]
        s2=[]
        s3=[]
        poster=[]
        d={}
        df= pd.DataFrame.from_records(Registration.objects.values())
        df.groupby('title')['rating'].mean().sort_values(ascending=False).head()
        df.groupby('title')['rating'].count().sort_values(ascending=False).head()
        ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
        ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())
        moviemat = df.pivot_table(index='user_id',columns='title',values='rating')
        try:
            starwars_user_ratings = moviemat[moviename]
        except:
            search = movie.search(moviename)
            r4=[]
            for res in search:
                try:
                    movie1.append("https://image.tmdb.org/t/p/original/"+res.poster_path[1::])
                except:
                     movie1.append("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAHlBMVEX09PTh4eH19fXg4ODk5OTw8PDs7Ozq6uru7u7n5+dZKxXMAAAELUlEQVR4nO2dWXKtMAwFwQMX9r/hB9RNMOARhCTyTv/kIxVQl4kHYZmuAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADgAsZ03o9eA6OfwyH360bXWz30kyd2HHvbq8LaibQdJ2V+C7Yf6RSdQsEZOxApGqWCsyJNK5qPVsEZCsHOS1tksBNFI2rsZTY8gaG0QxaCRjRj0ITS4/wvW0judguaKbjaID1f+xLEZG8/psZtV6OeKF3GbH2DHW9fbDN0WgTn/j0wvBtVYEjSM9MAwxZgKAMMW4ChDLyGxoQ/eGA0NMYPk3O9c9PH80nyGZo1A/e9l3WEiZM8DxmeZm3GH/Ib1jFNXZna0AzntTFZcigPj2E8f2M/HIoshqkEFYsih+Fu7b9XZOhvWNow4bdw85YVMBjmkqg0Kb4sHG2YaUKaFF+W5w3zefDnO5vnR/wwPxXh8YwOw1Oaz4Pbmzct8ryhLxhe+EdsivRxw/RgePW2821a/uZ5w8ILt/auZp7Ct8Qqb9g6/17XKA3BKnhK227yswirjvZtPc22yqwN912jxW6bQGW87xrx93mCuoBfNWs7JkKqIuaYeWcf04brn3ey1ITMsXrK7F9oWD1Ft+pUxPyeFXB8L1I5aJYsRnKbTcM9E5utyleQzUTVz2eSu8mKYb8km5jbLleI+xUZ4cJ+wHzgr8jqFzY85iNnfPe0vJn5uVff8mamuKMzGzrn27Xu9+3a4Bu2JddsWc3Erv4NaeWe3HTw6t9yV246Tkev3bB6V3UyfOWGDdvGU/HrNmzbFx8X0GzYvPE/asA14l+hubIhqqC4DS+UbsQc9Bpeq005S2g1vFx8c7LQani5uuikIWhohnR5wI3yqaOHnOG8ZLQpxVv1YYd1p5jhuiZOKN4sgNsrShl+F/0xxfsVfjtFoRE/yGqcfkdQwhgqyrRhmLY5tiJJjWbwvkfEcJeXOjyoNEWoVrYND4m3UJGqyla2DU+ZxUCRqoxY1DCWOv3pbsjqpCUNo4LfVqQrBBc0jAquioaylF/OMCG4KlKW8j9vmBjxk4LUSLUhm6CUIZ+gkCGjoIwhp6CIIaughCGvoIAhsyC/Ibcg+4jPLsjdhvyCzIYCgryGEoK8hoV93u83lDn+i9VQ4iGFIQwrDN2fN/z7bQhDGMIQhjCEYdnwvxrxPyKnljIadn6QgNOwMxKwGgoDwxZgKAMMW4ChDE/N2kiCoyA4eYTgPO/t/PPluyc6COrICc5kDybZ1jodhPP+u4LFg1qkofjXyR9jIgzFaaKl84Rkoen9FDci1Tmb0h5JqM6gNFo7m2R5zgVFbd8kW5nHZzJOx0MowNqhHHiL4+h2H7ARZvl4HvUHAtfD1yfpycyX6TPSfwCxE8o+JXhADwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAs/ANyGFT0fw3sTAAAAABJRU5ErkJggg==")
                movie1.append(res.title)
                movie1.append(res.overview)
                movie1.append(res.vote_average)
                movie1.append(res.release_date)
                break
            print(movie1)
            search = movie.search(moviename)
            for res in search:
                id1=res.id
                break
            r=requests.get('https://api.themoviedb.org/3/movie/'+str(id1)+'/credits?api_key=926646ce8955961847b0a854eaa7ac9e&language=en-US')
            events=r.json()
            eachcast=[]
            for i in events["cast"]:
                id=i['id']
                s=requests.get('https://api.themoviedb.org/3/person/'+str(id)+'?api_key=926646ce8955961847b0a854eaa7ac9e&language=en-US')
                cast=s.json()
                try:
                    eachcast.append([i['id'],i['name'],i['character'],"https://image.tmdb.org/t/p/original/"+i['profile_path'][1::],cast['biography'],cast['birthday'],cast['place_of_birth']])
                except:
                    pass
                print(eachcast)
                if(len(eachcast)==8):
                    break
            print(eachcast)
            return render(request,'Home.html',{'l':l,'poster':r4,'movie':movie1,'eachcast':eachcast})
        similar_to_starwars = moviemat.corrwith(starwars_user_ratings)
        corr_starwars = pd.DataFrame(similar_to_starwars,columns=['Correlation'])
        corr_starwars.dropna(inplace=True)
        corr_starwars.sort_values('Correlation',ascending=False).head(10)
        corr_starwars = corr_starwars.join(ratings['num of ratings'])
        li=corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlation',ascending=False).head(25)
        ri=(np.array(li.to_records().view(type=np.matrix))).tolist()
        for i in ri:
            for j in i:
                if(j[0]==moviename):
                    continue
                else:
                    s1.append(j[0])
                    if(len(s1)==10):
                        break
        for i in ri:
            for j in i:
                if(j[0]==moviename):
                    continue
                else:
                    s2.append(j[1])
                    if(len(s2)==10):
                        break
        for i in ri:
            for j in i:
                if(j[0]==moviename):
                    continue
                else:
                    s3.append(j[2])
                    if(len(s3)==10):
                        break
        for i in ri:
            for j in i:
                if(j[0]==moviename):
                    continue
                else:
                    search = movie.search(j[0][0:-6])
                    if(search):
                        r1.append(j[0])
                    else:
                        print(j[0],'hello')
                    for res in search:
                        print(res.title)
                        try:
                            r1.append("https://image.tmdb.org/t/p/w200/"+res.poster_path[1::])
                        except:
                            r1=[]
                        break
                r2.append(r1)
                if(len(r2)==20):
                    break
                r1=[]
        print(len(r2))
        print(r2)
        r3 = filter(None,r2)
        r4=list(r3)
        r4=r4[:12]
        s=moviename
        if '(' in s:
            moviename=s[:s.index('(')]   
        search = movie.search(moviename)
        for res in search:
            try:
                movie1.append("https://image.tmdb.org/t/p/original/"+res.poster_path[1::])
            except:
                movie1.append("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAHlBMVEX09PTh4eH19fXg4ODk5OTw8PDs7Ozq6uru7u7n5+dZKxXMAAAELUlEQVR4nO2dWXKtMAwFwQMX9r/hB9RNMOARhCTyTv/kIxVQl4kHYZmuAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADgAsZ03o9eA6OfwyH360bXWz30kyd2HHvbq8LaibQdJ2V+C7Yf6RSdQsEZOxApGqWCsyJNK5qPVsEZCsHOS1tksBNFI2rsZTY8gaG0QxaCRjRj0ITS4/wvW0judguaKbjaID1f+xLEZG8/psZtV6OeKF3GbH2DHW9fbDN0WgTn/j0wvBtVYEjSM9MAwxZgKAMMW4ChDLyGxoQ/eGA0NMYPk3O9c9PH80nyGZo1A/e9l3WEiZM8DxmeZm3GH/Ib1jFNXZna0AzntTFZcigPj2E8f2M/HIoshqkEFYsih+Fu7b9XZOhvWNow4bdw85YVMBjmkqg0Kb4sHG2YaUKaFF+W5w3zefDnO5vnR/wwPxXh8YwOw1Oaz4Pbmzct8ryhLxhe+EdsivRxw/RgePW2821a/uZ5w8ILt/auZp7Ct8Qqb9g6/17XKA3BKnhK227yswirjvZtPc22yqwN912jxW6bQGW87xrx93mCuoBfNWs7JkKqIuaYeWcf04brn3ey1ITMsXrK7F9oWD1Ft+pUxPyeFXB8L1I5aJYsRnKbTcM9E5utyleQzUTVz2eSu8mKYb8km5jbLleI+xUZ4cJ+wHzgr8jqFzY85iNnfPe0vJn5uVff8mamuKMzGzrn27Xu9+3a4Bu2JddsWc3Erv4NaeWe3HTw6t9yV246Tkev3bB6V3UyfOWGDdvGU/HrNmzbFx8X0GzYvPE/asA14l+hubIhqqC4DS+UbsQc9Bpeq005S2g1vFx8c7LQani5uuikIWhohnR5wI3yqaOHnOG8ZLQpxVv1YYd1p5jhuiZOKN4sgNsrShl+F/0xxfsVfjtFoRE/yGqcfkdQwhgqyrRhmLY5tiJJjWbwvkfEcJeXOjyoNEWoVrYND4m3UJGqyla2DU+ZxUCRqoxY1DCWOv3pbsjqpCUNo4LfVqQrBBc0jAquioaylF/OMCG4KlKW8j9vmBjxk4LUSLUhm6CUIZ+gkCGjoIwhp6CIIaughCGvoIAhsyC/Ibcg+4jPLsjdhvyCzIYCgryGEoK8hoV93u83lDn+i9VQ4iGFIQwrDN2fN/z7bQhDGMIQhjCEYdnwvxrxPyKnljIadn6QgNOwMxKwGgoDwxZgKAMMW4ChDE/N2kiCoyA4eYTgPO/t/PPluyc6COrICc5kDybZ1jodhPP+u4LFg1qkofjXyR9jIgzFaaKl84Rkoen9FDci1Tmb0h5JqM6gNFo7m2R5zgVFbd8kW5nHZzJOx0MowNqhHHiL4+h2H7ARZvl4HvUHAtfD1yfpycyX6TPSfwCxE8o+JXhADwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAs/ANyGFT0fw3sTAAAAABJRU5ErkJggg==")
            movie1.append(res.title)
            movie1.append(res.overview)
            movie1.append(res.vote_average)
            movie1.append(res.release_date)
            break
        print(movie1)
        s=moviename
        if '(' in s:
            moviename=s[:s.index('(')]   
        search = movie.search(moviename)
        print(search)
        for res in search:
            id1=res.id
            break
        r=requests.get('https://api.themoviedb.org/3/movie/'+str(id1)+'/credits?api_key=926646ce8955961847b0a854eaa7ac9e&language=en-US')
        events=r.json()
        eachcast=[]
        for i in events["cast"]:
            id=i['id']
            s=requests.get('https://api.themoviedb.org/3/person/'+str(id)+'?api_key=926646ce8955961847b0a854eaa7ac9e&language=en-US')
            cast=s.json()
            try:
                eachcast.append([i['id'],i['name'],i['character'],"https://image.tmdb.org/t/p/original/"+i['profile_path'][1::],cast['biography'],cast['birthday'],cast['place_of_birth']])
            except:
                pass
            print(eachcast)
            if(len(eachcast)==8):
                break
        print(eachcast)
        return render(request,'Home.html',{'l':l,'a':ri,'s1':s1,'s2':s2,'s3':s3,'poster':r4,'movie':movie1,'eachcast':eachcast})