import Kaggle_discussion as kg
import pandas as pd 
df=kg.kagglee()
data=df.kagglediscussion('https://www.kaggle.com',initial_page=1,last_page=1)
datf=pd.DataFrame(data)
datf.to_csv('comments.csv',index=False)
# print(data)