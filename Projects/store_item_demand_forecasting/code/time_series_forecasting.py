# Import Information
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import keras
from keras import optimizers
from keras.utils import plot_model
from keras.models import Sequential, Model
from keras.layers import Dense, LSTM, RepeatVector, TimeDistributed, Flatten
from sklearn.metrics import mean_squared_error
from sklearn.discriminant_analysis import StandardScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load the dataset
train = pd.read_csv('/Users/jamespecore/Documents/Github/data_science/Projects/store_item_demand_forecasting/data/train.csv')
test = pd.read_csv('/Users/jamespecore/Documents/Github/data_science/Projects/store_item_demand_forecasting/data/test.csv')

def preprocess_data(data):
    # Convert the 'date' column to datetime format
    data['date'] = pd.to_datetime(data['date'])
    return data

# Apply preprocessing to train and test data
train = preprocess_data(train)
test = preprocess_data(test)

def format_datetime(data):
    # Extract additional date-related features
    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.month
    data['day'] = data['date'].dt.day
    data['day_of_week'] = data['date'].dt.dayofweek
    return data

train = format_datetime(train)
test = format_datetime(test)

print(train)

# Exploratory Data Analysis
train.describe()

# Min and Max Date Retrieval Functions
def min_date(data):
    return data['date'].min().date()

def max_date(data):
    return data['date'].max().date()

# MiniMax Date from Train Set
print('Min date from train set:', min_date(train))
print('Max date from train set:', max_date(train))

# MiniMax Date from Test Set
print('Min date from test set:', min_date(test))
print('Max date from test set:', max_date(test))

# Calculate the forecast lag size, which represents the number of days between the last date in the train set
# and the last date in the test set
lag_size = (test['date'].max().date() - train['date'].max().date()).days

# Print the results
print('Last date in the train set: %s' % train['date'].max().date())
print('Last date in the test set: %s' % test['date'].max().date())
print('Forecast lag size (days between train and test set):', lag_size)

# Aggregate daily sales
daily_sales = train.groupby('date')['sales'].sum().reset_index()

# Aggregate daily sales per store
store_daily_sales = train.groupby(['store', 'date'])['sales'].sum().reset_index()

# Aggregate daily sales per item
item_daily_sales = train.groupby(['item', 'date'])['sales'].sum().reset_index()

# Plot daily sales using Matplotlib
plt.figure(figsize=(10, 6))
plt.plot(daily_sales['date'], daily_sales['sales'], marker='o', linestyle='-', color='b')
plt.title('Daily Sales')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

# Step 1: Rearrange Dataset
def rearrange_dataset(data):
    # Group by item, store, and date, calculate mean sales
    data_grouped = data.sort_values('date').groupby(['item', 'store', 'date'], as_index=False)
    data_grouped = data_grouped.agg({'sales': 'mean'})
    data_grouped.columns = ['item', 'store', 'date', 'sales']
    return data_grouped

# Step 2: Transform Data into a Time Series Problem
def series_to_supervised(data, window=1, lag=1, dropnan=True):
    cols, names = list(), list()
    for i in range(window, 0, -1):
        cols.append(data.shift(i))
        names += [('%s(t-%d)' % (col, i)) for col in data.columns]
    cols.append(data)
    names += [('%s(t)' % (col)) for col in data.columns]
    cols.append(data.shift(-lag))
    names += [('%s(t+%d)' % (col, lag)) for col in data.columns]
    agg = pd.concat(cols, axis=1)
    agg.columns = names
    if dropnan:
        agg.dropna(inplace=True)
    return agg

# Step 3: Remove Rows with Different Item or Store Values
def filter_inconsistent_data(data):
    last_item = 'item(t-%d)' % window
    last_store = 'store(t-%d)' % window
    data_filtered = data[(data['store(t)'] == data[last_store])]
    data_filtered.reset_index(drop=True, inplace=True)
    
    # Reset indices of the original data DataFrame
    data.reset_index(drop=True, inplace=True)
    
    return data_filtered

# Step 4: Remove Unwanted Columns
def drop_unwanted_columns(data, window, lag):
    columns_to_drop = [('%s(t+%d)' % (col, lag)) for col in ['item', 'store']]
    for i in range(window, 0, -1):
        columns_to_drop += [('%s(t-%d)' % (col, i)) for col in ['item', 'store']]
    data.drop(columns_to_drop, axis=1, inplace=True)
    data.drop(['item(t)', 'store(t)'], axis=1, inplace=True)
    return data

# Step 5: Train/Validation Split
def split_train_valid(data, labels_col, test_size=0.4, random_state=0):
    labels = data[labels_col]
    data = data.drop(labels_col, axis=1)
    X_train, X_valid, Y_train, Y_valid = train_test_split(data, labels.values, test_size=test_size, random_state=random_state)
    print('Train set shape:', X_train.shape)
    print('Validation set shape:', X_valid.shape)
    return X_train, X_valid, Y_train, Y_valid

# Apply preprocessing steps
train_gp = rearrange_dataset(train)
window = 29
lag = lag_size
series = series_to_supervised(train_gp.drop('date', axis=1), window=window, lag=lag)
series = filter_inconsistent_data(series)
series = drop_unwanted_columns(series, window, lag)
X_train, X_valid, Y_train, Y_valid = split_train_valid(series, 'sales(t+%d)' % lag_size)

# Check the shape of the input data
print("X_train shape:", X_train.shape)
print("X_valid shape:", X_valid.shape)

# Reshape input data for LSTM model (add a third dimension for the single channel)
X_train_lstm = X_train.values.reshape(X_train.shape[0], X_train.shape[1], 1)
X_valid_lstm = X_valid.values.reshape(X_valid.shape[0], X_valid.shape[1], 1)

# Build LSTM model architecture
lstm_model = Sequential([
    LSTM(10, activation='relu', input_shape=(X_train_lstm.shape[1], 1)),
    Dense(1)
])

# Compile LSTM model
lstm_model.compile(optimizer='adam', loss='mse')

# Train LSTM model
history = lstm_model.fit(X_train_lstm, Y_train, epochs=10, batch_size=32, validation_data=(X_valid_lstm, Y_valid), verbose=1)