#!/usr/bin/env python
# coding: utf-8

# In[1]:


# pip install faker


# In[2]:


import pandas as pd
import random
from faker import Faker

fake = Faker('en_IN')

# Creating a list of real Indian online education platforms
platforms = ['Coursera', 'edX', 'Udemy', 'BYJU’S', 'Unacademy', 'Toppr', 'Vedantu', 'Khan Academy', 'UpGrad']

# Creating a list of Indian cities for location data
indian_cities = ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata', 'Hyderabad', 'Pune', 'Jaipur', 'Ahmedabad', 'Lucknow']

# Initialize an empty dataframe
df = pd.DataFrame(columns=['Platform_Name', 'User_ID', 'Age', 'Gender', 'Location', 'Course_ID', 'Course_Category',
                           'Course_Duration', 'Instructor', 'Enrollment_Date', 'Time_Spent', 'Logins',
                           'Modules_Completed', 'User_Rating', 'Subscription_Type', 'Payment_History', 'Course_Completion',
                           'Dropout_Rate', 'Support_Tickets', 'Competitor_Platform'])

# Generating realistic dummy data for each row
for _ in range(1000):
    platform_name = random.choice(platforms)
    user_id = fake.unique.random_int(min=1, max=1000)
    age = random.randint(18, 60)
    gender = random.choice(['Male', 'Female', 'Other'])
    location = random.choice(indian_cities)
    course_id = fake.unique.random_int(min=1, max=500)
    course_category = random.choice(['Mathematics', 'Science', 'History', 'Programming', 'Language'])
    course_duration = random.randint(1, 12)  # In months
    instructor = fake.name()
    enrollment_date = fake.date_between(start_date='-1y', end_date='today')
    time_spent = random.uniform(1, 30)  # In hours
    logins = random.randint(1, 100)
    modules_completed = random.randint(0, 50)
    user_rating = round(random.uniform(3, 5), 2)
    subscription_type = random.choice(['Free', 'Basic', 'Premium'])
    payment_history = random.choice(['Paid', 'Refunded', 'Pending'])
    course_completion = random.uniform(0, 100)  # Completion percentage
    dropout_rate = round(random.uniform(0, 30), 2)
    support_tickets = random.randint(0, 10)
    competitor_platform = random.choice(platforms)

    df = df.append({'Platform_Name': platform_name, 'User_ID': user_id, 'Age': age, 'Gender': gender,
                    'Location': location, 'Course_ID': course_id, 'Course_Category': course_category,
                    'Course_Duration': course_duration, 'Instructor': instructor, 'Enrollment_Date': enrollment_date,
                    'Time_Spent': time_spent, 'Logins': logins, 'Modules_Completed': modules_completed,
                    'User_Rating': user_rating, 'Subscription_Type': subscription_type,
                    'Payment_History': payment_history, 'Course_Completion': course_completion,
                    'Dropout_Rate': dropout_rate, 'Support_Tickets': support_tickets,
                    'Competitor_Platform': competitor_platform},
                   ignore_index=True)


# ## Data Loading and Initial Exploration

# In[6]:


# Display the first few rows
df.head()


# In[7]:


# Check for missing values
df.isnull().sum()


# In[8]:


# Summary statistics
df.describe()


# In[9]:


# Address missing values (if any)
df.fillna(0, inplace=True)


# In[10]:


# Convert date columns to datetime objects
df['Enrollment_Date'] = pd.to_datetime(df['Enrollment_Date'])


# ## Exploratory Data Analysis (EDA)

# In[11]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[12]:


# Visualize the distribution of user age
sns.histplot(df['Age'], kde=True)
plt.title('User Age Distribution')
plt.show()


# In[13]:


# Visualize user ratings
sns.histplot(df['User_Rating'], kde=True)
plt.title('User Rating Distribution')
plt.show()


# In[14]:


# Explore user engagement metrics
sns.pairplot(df[['Time_Spent', 'Logins', 'Modules_Completed']])
plt.title('User Engagement Metrics')
plt.show()


# In[15]:


# Analyze course categories
sns.countplot(data=df, x='Course_Category')
plt.xticks(rotation=45)
plt.title('Course Category Distribution')
plt.show()


# ## Statistical Analysis
# 
# 

# In[16]:


from scipy import stats


# In[17]:


# Correlation between user age and course completion
corr, p = stats.pearsonr(df['Age'], df['Course_Completion'])
print(f'Pearson Correlation: {corr}, p-value: {p}')


# In[18]:


# Hypothesis testing: Compare Premium vs. Free subscriptions
premium = df[df['Subscription_Type'] == 'Premium']
free = df[df['Subscription_Type'] == 'Free']
t_stat, p_value = stats.ttest_ind(premium['Course_Completion'], free['Course_Completion'])
print(f'T-statistic: {t_stat}, p-value: {p_value}')


# ## User Behavior Analysis
# 
# 

# In[19]:


# User demographics analysis
sns.barplot(data=df, x='Gender', y='Course_Completion')
plt.title('Course Completion by Gender')
plt.show()


# In[20]:


# Time spent vs. course completion
sns.scatterplot(data=df, x='Time_Spent', y='Course_Completion')
plt.title('Time Spent vs. Course Completion')
plt.show()


# ## Competitor Analysis

# In[21]:


# Comparison with competitor platform
sns.boxplot(data=df, x='Competitor_Platform', y='User_Rating')
plt.xticks(rotation=45)
plt.title('User Ratings by Competitor Platform')
plt.show()


# In[ ]:




