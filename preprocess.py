from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd

def preprocess(df):
  df['Date'] = pd.to_datetime(df['Date'])
  df['StateHoliday'].replace({'a':1,'b':2,'c':3}, inplace=True)
  df['StoreType'].replace({'a':1,'b':2,'c':3,'d':4}, inplace=True)
  df['Assortment'].replace({'a':1,'b':2,'c':3}, inplace=True)
  interval = df['PromoInterval'].str.split(',',1,expand=True).rename({0:'start',1:'rep'},axis=1)
  interval[['rep','end']] = interval['rep'].str.rsplit(',',1,expand=True)
  df[['PromoStart','PromoEnd']] = interval[['start','end']]
  df['PromoDuration'] = df['PromoInterval'].str.count(',')

  with_promo = df[df['PromoStart'].isna()==False]
  with_promo['PromoEnd'] = with_promo['PromoEnd'].apply(lambda x: pd.datetime.strptime(x,'%b').month)
  with_promo['PromoStart'] = with_promo['PromoStart'].apply(lambda x: pd.datetime.strptime(x,'%b').month)
  df = with_promo.combine_first(df)
  df['Avg SalesCust'] = df['Sales'] / df['Customers']
  df = df.fillna(0)

  df.drop(columns='PromoInterval',inplace=True)
  df['Date'] = df['Date'].apply(lambda x: x.toordinal())
  cols = ['PromoEnd','Open','Assortment','StateHoliday','CompetitionOpenSinceMonth',
 'Date','Store','CompetitionDistance','Promo','Customers','DayOfWeek','Promo2SinceWeek']
  inputs = df[cols]
  return inputs