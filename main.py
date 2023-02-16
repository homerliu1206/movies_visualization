import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

movies = pd.read_csv('D:\\coding\\python\\Movie-Ratings.csv')
movies.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRating', 'BudgetMillions', 'Year']
movies.Film = movies.Film.astype('category') # 將'Film'轉換為「種類」
movies.Genre = movies.Genre.astype('category')
movies.Year = movies.Year.astype('category') # 雖然年份是數字，但其平均數並沒有意義

# joinplots
j = sns.jointplot(data=movies, x='CriticRating', y='AudienceRating', kind='hex')
plt.show() # 蜂巢點陣圖

# Histogram
m1 =sns.distplot(movies.AudienceRating, bins=15) 
plt.show() # 長條+曲線圖
m2 = sns.distplot(movies.CriticRating, bins=15) 
plt.show() # 長條+曲線圖
n1 = plt.hist(movies.AudienceRating, bins=15) 
plt.show() # 長條圖
n2 = sns.hist(movies.CriticRating, bins=15) 
plt.show() # 長條圖

# Stacked Histogram
# method 1
h1 = plt.hist(movies[movies.Genre == 'Drama'].BudgetMillions, bins=15)
h2 = plt.hist(movies[movies.Genre == 'Action'].BudgetMillions, bins=15)
h3 = plt.hist(movies[movies.Genre == 'Thriller'].BudgetMillions, bins=15)
plt.show() # 三個重疊的長條圖

# method 2
plt.hist(
    [movies[movies.Genre == 'Drama'].BudgetMillions, 
    movies[movies.Genre == 'Action'].BudgetMillions,         
    movies[movies.Genre == 'Thriller'].BudgetMillions],
    bins=15)
plt.show() # 獨立的長條圖

# method 3
list1 = list()
for gen in movies.Genre.cat.categories:
    list1.append(movies[movies.Genre == gen].BudgetMillions)
h = plt.hist(list1, bins=30, stacked=True, rwidth=1)
plt.show()

# KDE Plot
k1 = sns.kdeplot(
        [movies.CriticRating, movies.AudienceRating], 
        shade=True, shade_lowest=False)
plt.show() # 密度圖
sns.set_style('dark')
k2 = sns.kdeplot([movies.BudgetMillions, movies.AudienceRating])
plt.show() # 密度圖
k3 = sns.kdeplot([movies.BudgetMillions, movies.CriticRating])
plt.show() # 密度圖

# Subplots
f, axes = plt.subplots(1,2, figsize=(12,6), sharex=True, sharey=True)
k1 = sns.kdeplot([movies.CriticRating, movies.AudienceRating], ax=axes[0])
k2 = sns.kdeplot([movies.BudgetMillions, movies.AudienceRating], ax=axes[1])
k1.set(xlim=(-20, 160))
plt.show() # 分割頁面，並帶入數個圖表

# BoxPlots 
w1 = sns.boxplot(data=movies, x='Genre', y='CriticRating')
plt.show()
w2= sns.boxplot(data=movies[movies.Genre=='Drama'], x='Year', y='CriticRating')
plt.show()

# ViolinPlots
z = sns.violinplot(data=movies, x='Genre', y='CriticRating')
plt.show()

# Facet Grid
g = sns.FacetGrid(movies, row='Genre', col='Year', hue='Genre')
kws = dict(s=50, linewidth=0.5, edgecolor='black')
g = g.map(plt.scatter, 'CriticRating', 'AudienceRating', **kws)
plt.show()
g = sns.FacetGrid(movies, row='Genre', col='Year', hue='Genre')
g = g.map(plt.hist, 'BudgetMillions')
plt.show()

# Controlling axes and adding Diagnols
g = sns.FacetGrid(movies, row='Genre', col='Year', hue='Genre')
kws = dict(s=50, linewidth=0.5, edgecolor='black')
g = g.map(plt.scatter, 'CriticRating', 'AudienceRating', **kws)
g.set(xlim=(0,100), ylim=(0,100))
for ax in g.axes.flat:
    ax.plot((0,100), (0,100), c='gray', ls='--')
g.add_legend()
plt.show()

