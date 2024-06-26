# UniNest: Housing Price Estimator
**Medium Artcile:**

Data geared project designed to project housing market prices in University cities

## Web Scraping
Created a web scraper from scratch using Python and HTML-Requests to scrape the following from over 1200 listings across 6 cities:
*  Location
*  Title
*  Price
*  Style
*  Bedrooms
*  Bathrooms
*  Size
*  Air Conditioning
*  Den
*  Bachelor/Studio

## Data Cleaning
Cleaned the raw data scraped from Kijiji to use for EDA, graph plotting, and model building. The cleaning included:

*  Removing "Wanted" listings
*  Streamlined bedrooms, bathroom and price to include integers only
*  Parsed through bedrooms to create binary columns for dens
*  Removed "Please Contact" listings

## Exploratory Data Analysis
Analyzed the clean data and making bar, scatterplot and heatmap graphs using Tableau & Jupyter Notebook [Seaborn, Matplotlib]

The following graphs analyze relationships between the various data columns including Size, Price, Bathrooms, Bedrooms, Location and Den status:
<div class='tableauPlaceholder' id='viz1706467624091' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ho&#47;HousingPriceBoard&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='HousingPriceBoard&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ho&#47;HousingPriceBoard&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                
View the Dashboard: https://public.tableau.com/views/HousingPriceBoard/Dashboard1?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link 

## Machine Learning Model
Trained a multiple linear regression model with sklearn (accuracy ~70-80%) to predict housing data based off the information I scraped and cleaned. Deployed the model using a Flask API.

![image](https://github.com/AJ-C22/DS-Uni-Housing-Market-Projection/assets/114104270/8a64041d-16e2-4446-8a1d-9c786a968e80)

## Resources & Packages Used
**Python Version:** 3.11.4

**Packages:** pandas, numpy, matplotlib, seaborn, html-requests 

**EDA video:** https://www.youtube.com/watch?v=QWgg4w1SpJ8&list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t&index=4&t=2011s&ab_channel=KenJee




