import pandas as pd

movies_df = pd.read_table('ml-1m/movies.dat',header=None,sep='::',names=['movie_id','movie_title','movie_genre'])

ratings_df = pd.read_table('ml-1m/ratings.dat',header=None,sep='::',names=['user_id','movie_id','rating','timestamp'])

del ratings_df['timestamp']

ratings_df = pd.merge(ratings_df,movies_df,on='movie_id')[['user_id','movie_title','movie_id','rating']]
