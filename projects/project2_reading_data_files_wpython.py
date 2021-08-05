#!/usr/bin/python3

import numpy as np
import pandas as pd

import matplotlib
matplotlib.use('Agg')


import matplotlib.pyplot as plt

def main():
    
    excel_file = 'movies.xls'

    
    movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)
    
    
    movies_sheet2 = pd.read_excel(excel_file, sheet_name=1, index_col=0)
    

    movies_sheet3 = pd.read_excel(excel_file, sheet_name=2, index_col=0)
    
    
    movies = pd.concat([movies_sheet1, movies_sheet2, movies_sheet3])


    movies.drop_duplicates(inplace=True)
    
    print(movies.shape)
    

    sorted_by_budget = movies.sort_values(["Budget"], ascending=False)

    print(sorted_by_budget.head(10))

    sorted_by_budget["Budget"].head(10).plot(kind="pie")

    plt.savefig("/home/student/static/tpieplot.png", bbox_inches='tight')

    plt.title("Top 10 By Budget")


    # first 10 rows of data file
    print("Top 3 of Data file")
    print(movies.head(3))

    # last 10 rows of data file
    print("Last 4 of Data file")
    print(movies.tail(4))

    #Filtering Data
    print("Movies made after 2015")
    print(movies[movies.Year > 2015])

    #write to csv file
    movies.to_csv("movies.csv")
    
    #Statistical Data of Movies
    print("Statistical Data of Movies")
    print(movies.describe())

    #Alpehbetical Descending
    print("Alphebetical Descending")
    Alphebetical=movies.sort_values('Title', ascending=False)
    print(Alphebetical.head(5))

    #convert to csv
    movies.to_csv("mod_movies.csv")

    #convert to text file
    movies.to_csv("mod_movies.txt", sep='\t')

    #Finding GroupBy"
    print("GroupBy")
    groupby_movies = movies.groupby(['Duration']).mean().sort_values('Budget', ascending=False)
    print(groupby_movies.head(2))

    #Finding GroupBy Mean "
    print("GroupBy Mean")
    groupby_mean = movies.groupby(['Duration']).mean()
    print(groupby_mean.head(2))

    #count
    print("Count USA")
    print([movies.Country == "USA"].count())

    
if __name__ == "__main__":
    main()


