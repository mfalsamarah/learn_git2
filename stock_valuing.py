
import pandas as pd
from finvizfinance.quote import finvizfinance
import numpy as np

stock = finvizfinance('tsla')
stock_fundament = stock.ticker_fundament()
stock_description = stock.ticker_description()
outer_ratings_df = stock.ticker_outer_ratings()
news_df = stock.ticker_news()
inside_trader_df = stock.ticker_inside_trader()

# --- If you want to display images, run code below ---
# stock.ticker_charts()
# from IPython.display import Image
# Image(filename='tsla.jpg')

stock_info = pd.DataFrame(stock_fundament.items())
stock_info = stock_info.transpose()
new_header = stock_info.iloc[0] #grab the first row for the header
stock_info = stock_info[1:] #take the data less the header row
stock_info.columns = new_header #set the header row as the df header

from finvizfinance.screener.overview import Overview
foverview = Overview()
filters_dict = {'Exchange':'NASDAQ', 'Country':'USA', 'Average Volume':'Over 1M', 'P/E':'Over 5', 'Sector':'Technology'}
foverview.set_filter(filters_dict=filters_dict)
# df = foverview.screener_view(order='Price/Earnings')
df = foverview.screener_view()
df.head()

PE = df['P/E']
med_PE = np.median(PE)

df_PE_filtered = df[df['P/E'] < med_PE] 
df_PE_filtered.head()
