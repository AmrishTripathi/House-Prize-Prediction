# -*- coding: utf-8 -*-
"""Amrish Tripathi24_iem_03_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11BceYl2MrwXnVo0xIY75mw3n2ENNNm8M
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics
# %matplotlib inline

from google.colab import drive
drive.mount('/content/train.csv')

import pandas as pd
pd.read_csv('/content/train.csv')

from google.colab import drive
drive.mount('/content/drive')
import drive as drive_module

df = pd.read_csv('/content/drive/MyDrive/train.csv')
df.head()

df.describe()

df.shape

df.dtypes

df.info()

df.isna().sum()

target_feature = 'medv'
y = df[target_feature]
x = df.drop(target_feature,axis=1)
x.head()

y.head()

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=7)
from sklearn.linear_model import LinearRegression
regression=LinearRegression()
regression.fit(x_train,y_train)

train_score=round(regression.score(x_train,y_train)*100,2)
print('Train Score of linear regression:',train_score)

y_pred=regression.predict(x_test)
from sklearn.metrics import r2_score
score=round(r2_score(y_test,y_pred)*100,2)
print('r_2 scar',score)

round(regression.score(x_train,y_train)*100,2)

from sklearn import metrics
import numpy as np # Added this line to import numpy and alias it as np

print('Mean Absolute Error on TEST DATA of Linear regression:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error on TEST DATA of Linear regression:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error on TEST DATA of Linear regression:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

df1=pd.DataFrame({'Actual':y_test,'Predicted':y_pred,'variance':y_test-y_pred})
df1.head()

df.head(20)
df=df.drop(['ID'],axis=1)

import matplotlib.pyplot as plt # import the matplotlib.pyplot module and alias it as plt
import seaborn as sns # make sure to import seaborn as well since it's used in the code

fig,ax=plt.subplots(ncols=7,nrows=2,figsize=(20,10))
index=0
ax=ax.flatten()
for col,value in df.items():
  sns.boxplot(y=col,data=df,ax=ax[index])
  index+=1
plt.tight_layout(pad=0.5,w_pad=0.5,h_pad=5.0)

regression.intercept_

regression.coef_

lr_coefficient=pd.DataFrame()
lr_coefficient['Columns']=x_train.columns
lr_coefficient['Coefficient Estimte']=pd.Series(regression.coef_)
print(lr_coefficient)

fig,ax=plt.subplots(figsize=(20, 10))
ax.bar(lr_coefficient['Columns'],lr_coefficient['Coefficient Estimte'])
ax.spines['bottom'].set_position('zero')
plt.style.use('ggplot')
plt.grid()
plt.show()

fig,ax=plt.subplots(figsize=(20, 10))
color=['tab:gray','tab:blue','tab:orange','tab:brown','tab:green','tab:pink','tab:red','tab:purple','tab:olive','tab:cyan','tab:gray']
ax.bar(lr_coefficient['Columns'],lr_coefficient['Coefficient Estimte'],color=color)
ax.spines['bottom'].set_position('zero')
plt.style.use('ggplot')
plt.grid()
plt.show()

import pickle
filename='linear_model.pkl'
pickle.dump(regression,open(filename,'wb'))

import pickle
loaded_model=pickle.load(open(filename,'rb'))
a=loaded_model.predict([[7,0.08829,12.5,7.87,0,0.524,6.012,66.6,5.5605,5,311,15.2,395.60,12.43]])
print("predicted value will be:\n",a)

df1=pd.DataFrame({'Actual':y_test,'Predicted':y_pred,'variance':y_test-y_pred})
df1.head()

fig,ax=plt.subplots(figsize=(20,10))
x_ax=range(len(x_test))
plt.scatter(x_ax,y_test,s=30,color='green',label='original')
plt.scatter(x_ax,y_pred,s=30,color='blue',label='predicted')
plt.legend()
plt.show()

fig,ax=plt.subplots(figsize=(20,10))
x_ax=range(len(x_test))
plt.scatter(x_ax,y_test,s=30,color='green',label='original')
plt.plot(x_ax,y_pred,lw=0.8,color='blue',label='predicted')
plt.legend()
plt.show()

fig,ax=plt.subplots(figsize=(20,10))
x_ax=range(len(x_test))
plt.plot(x_ax,y_test,lw=0.9,color='green',label='original')
plt.plot(x_ax,y_pred,lw=0.8,color='blue',label='predicted')
plt.legend()
plt.show()