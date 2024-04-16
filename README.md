## Movie Analysis Visualization
This Python script utilizes the pandas library for data manipulation and seaborn and matplotlib libraries for data visualization. It explores various aspects of movie data including ratings, genres, budgets, and years of release.

### Features
- `Jointplot`: Visualizes the relationship between CriticRating and AudienceRating using a hexagonal bin plot.
- `Histograms`: Displays the distribution of AudienceRating and CriticRating separately using histograms with and without a kernel density estimate (KDE) overlay.
- `Stacked Histogram`: Shows the distribution of movie budgets across different genres using stacked histograms.
- `KDE Plot`: Illustrates the kernel density estimation of budgets against AudienceRating and CriticRating.
- `Subplots`: Utilizes subplots to compare the KDE plots of CriticRating vs. AudienceRating and BudgetMillions vs. AudienceRating.
- `Boxplots`: Presents boxplots to display the distribution of CriticRating across different genres and years for Drama genre movies.
- `Violin Plots`: Demonstrates the distribution of CriticRating across different genres using violin plots.
- `Facet Grid`: Utilizes facet grid to create scatter plots and histograms for CriticRating vs. AudienceRating and BudgetMillions across different genres and years.

### Usage
Data Input: Ensure the movie dataset ('Movie-Ratings.csv') is placed in the directory specified in the script.
Run Script: Execute the Python script using a Python interpreter.
Visualization: Various plots and visualizations will be displayed to analyze different aspects of movie data.
