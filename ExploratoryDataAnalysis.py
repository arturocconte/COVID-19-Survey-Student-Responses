# -*- coding: utf-8 -*-

#Data processing
import pandas as pd
import numpy as np

#Visualization
import matplotlib.pyplot as plt
import seaborn as sns


#Plot parameters
sns.set_style('darkgrid')
plt.rcParams.update({'font.size': 6})


#Reading data 
pd.read_csv("COVID-19 Survey Student Responses.csv")
covid = pd.read_csv("COVID-19 Survey Student Responses.csv")
covid.columns = ["id","region","age","time_online_classes",
"rating_of_classes","medium_for_classes","time_study","time_fitness","time_sleep",
"time_social_media","prefered_social_media","time_tv","meals_day","weight_change",
"health_issue","stress_buster","time_utilized","connection","miss_the_most"]


#Exploring
covid.head()


#Pre-Processing data
covid['time_tv'].replace('No tv', 0, inplace=True)
covid['time_tv'].replace('n', 0, inplace=True)
covid['time_tv'].replace('N', 0, inplace=True)
covid['time_tv'].replace(' ', 0, inplace=True)
covid['time_tv'] = covid['time_tv'].astype('float')


#Removing outliner point 
covid.loc[covid['time_study']==18.0]
covid.drop([31] , axis=0, inplace=True)


#Age distribution
plt.figure(figsize=(20, 12))
ax = sns.countplot(x='age', data=covid, palette='dark:salmon_r')
ax.set_xlabel("Age of Subject",fontsize=22)
ax.set_ylabel("Number of Subjects",fontsize=22)
plt.yscale('log')
plt.show()


#What gadgets were used
pie_df = covid['medium_for_classes'].value_counts().to_dict()
plt.figure(figsize=(12,12))
plt.pie(x=pie_df.values(),
        startangle=0, explode=[0.0, 0.01, 0.05, 0.1, 0.2])
plt.legend(labels=pie_df.keys(), loc='lower right',shadow=True, facecolor='lightgrey')
plt.show()


#Concatening dataframes and exploring rate of online classes for different gadgets
smartphone_df = covid[covid['medium_for_classes']=='Smartphone']
desktop_df = covid[covid['medium_for_classes']=='Laptop/Desktop']

plt.figure(figsize=(14, 12))
smartphone_df['Gadget']='Smartphone'
desktop_df['Gadget']='Desktop'
df_combined = pd.concat([smartphone_df,desktop_df])
ax = sns.countplot(x='rating_of_classes', hue='Gadget',
 data=df_combined, palette='rocket_r',order=['Excellent','Good','Average','Poor','Very poor'])
ax.set_xlabel("Rating of Online Class experience",fontsize=22)
ax.set_ylabel("Number of Subjects",fontsize=22)
plt.show()


#Boxplot on time spent on different activities
plt.figure(figsize=(16, 15))
ax = sns.boxplot(data=covid[['time_study','time_fitness','time_sleep','time_social_media','time_tv']],orient='h',palette='rocket_r')
ax.set_yticklabels(["Time spent on self study","Time spent on fitness","Time spent on sleep","Time spent on social media","Time spent on TV"])
plt.show()


#Violinplots on health issues
fig, ax = plt.subplots(2,2, figsize=(16,18))
sns.violinplot(y='health_issue', x='age', data=covid, palette='rocket_r',ax=ax[0,0])
ax[0,0].set_xlabel("Age of Subject",fontsize=18)
ax[0,0].set_ylabel("Health issue during lockdown",fontsize=18)
sns.violinplot(y='health_issue', x='time_sleep', data=covid, palette='rocket_r',ax=ax[0,1])
ax[0,1].set_xlabel("Time spent on sleep",fontsize=18)
ax[0,1].set_ylabel("Health issue during lockdown",fontsize=18)
sns.violinplot(y='health_issue', x='time_fitness', data=covid, palette='rocket_r', ax=ax[1,0])
ax[1,0].set_xlabel("Time spent on fitness",fontsize=18)
ax[1,0].set_ylabel("Health issue during lockdown",fontsize=18)
sns.violinplot(y='health_issue', x='time_study', data=covid, palette='rocket_r', ax=ax[1,1])
ax[1,1].set_xlabel("Time spent on self study",fontsize=18)
ax[1,1].set_ylabel("Health issue during lockdown",fontsize=18)
plt.show()


#Violinplot on change of weight
fig, ax = plt.subplots(2,1, figsize=(16,18))
sns.violinplot(y='weight_change', x='time_fitness', data=covid, palette='rocket_r',ax=ax[0])
ax[0].set_xlabel("Time spent on fitness",fontsize=18)
ax[0].set_ylabel("Change in your weight",fontsize=18)
sns.violinplot(y='weight_change', x='meals_day', data=covid, palette='rocket_r',ax=ax[1])
ax[1].set_xlabel("Number of meals per day",fontsize=18)
ax[1].set_ylabel("Change in your weight",fontsize=18)
plt.show()


#Violinplot on time utilized
fig, ax = plt.subplots(3,  sharey=True,figsize=(16,18))
sns.violinplot(y='time_utilized', x='time_fitness', data=covid, palette='rocket_r' ,ax=ax[0])
ax[0].set_xlabel("Time spent on fitness",fontsize=18)
ax[0].set_ylabel("Time utilized",fontsize=18)
sns.violinplot(y='time_utilized', x='time_social_media', data=covid, palette='rocket_r', ax=ax[1])
ax[1].set_xlabel("Time spent on social media",fontsize=18)
ax[1].set_ylabel("Time utilized",fontsize=18)
sns.violinplot(y='time_utilized', x='time_online_classes', data=covid, palette='rocket_r', ax=ax[2])
ax[2].set_xlabel("Time spent on Online Class",fontsize=18)
ax[2].set_ylabel("Time utilized",fontsize=18)
plt.show()


#Selecting especific data on the dataframe
health_con_time_YES = covid[covid['time_utilized']=='YES']
health_con_time_NO = covid[covid['time_utilized']=='NO']

health_con_time1 = health_con_time_YES[health_con_time_YES['connection']=='YES']
health_con_time2 = health_con_time_YES[health_con_time_YES['connection']=='NO']
health_con_time3 = health_con_time_NO[health_con_time_NO['connection']=='YES']
health_con_time4 = health_con_time_NO[health_con_time_NO['connection']=='NO']


#Illustrating results from the researchers on health issues
fig, ax = plt.subplots(1,2, sharey=True, sharex=True, figsize=(16,16))
sns.countplot(x='health_issue', data=health_con_time3, palette='rocket_r',ax=ax[0])
ax[0].set_xlabel("Health issue during lockdown",fontsize=18)
ax[0].set_ylabel("Number of Subjects",fontsize=18)
ax[0].title.set_text('Time Utilized = NO; Connection = YES')
sns.countplot(x='health_issue', data=health_con_time4, palette='rocket_r', ax=ax[1])
ax[1].set_xlabel("Health issue during lockdown",fontsize=18)
ax[1].set_ylabel("",fontsize=18)
ax[1].title.set_text('Time Utilized = NO; Connection = NO')
plt.show()


fig, ax = plt.subplots(1,2, sharey=True, sharex=True, figsize=(16,16))
sns.countplot(x='health_issue', data=health_con_time2, palette='rocket_r',ax=ax[0])
ax[0].set_xlabel("Health issue during lockdown",fontsize=18)
ax[0].set_ylabel("Number of Subjects",fontsize=18)
ax[0].title.set_text('Time Utilized = YES; Connection = YES')
sns.countplot(x='health_issue', data=health_con_time1, palette='rocket_r', ax=ax[1])
ax[1].set_xlabel("Health issue during lockdown",fontsize=18)
ax[1].set_ylabel("",fontsize=18)
ax[1].title.set_text('Time Utilized = YES; Connection = NO')
plt.show()


#Kendall correlation heatmap
sns.set(font_scale=1.8) 
corr = covid.corr(method='kendall')
mask = np.zeros_like(corr)
mask[np.triu_indices_from(mask)] = True
plt.figure(figsize=(16,18))
sns.heatmap(corr, mask=mask, center=0, annot=True,
            square=True, linewidths=.5, cbar_kws={"shrink": .5},cmap='coolwarm')
plt.show()













