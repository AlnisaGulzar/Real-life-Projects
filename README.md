Working on Real Project with python
(A part of Big Data Analysis)
The Weather Dataset
Here, The Weather Dataset is a time-series dataset with per-hour information about the weather conditions at a perticular location. It records Temperature, Der Point Temperature, Relative Humidity, wind speed, Pressure, and Conditions.

This dataset is availaible as csv file, we are going to analyze this dataset using pandas DataFrame.

1
import pandas as pd 
1
data = pd.read_csv(r"C:\Users\alnis\Downloads\file.csv")
1
data
Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa	Weather
0	01-01-2012 00:00	-1.8	-3.9	86	4	8.0	101.24	Fog
1	01-01-2012 01:00	-1.8	-3.7	87	4	8.0	101.24	Fog
2	01-01-2012 02:00	-1.8	-3.4	89	7	4.0	101.26	Freezing Drizzle,Fog
3	01-01-2012 03:00	-1.5	-3.2	88	6	4.0	101.27	Freezing Drizzle,Fog
4	01-01-2012 04:00	-1.5	-3.3	88	7	4.8	101.23	Fog
...	...	...	...	...	...	...	...	...
8779	12/31/2012 19:00	0.1	-2.7	81	30	9.7	100.13	Snow
8780	12/31/2012 20:00	0.2	-2.4	83	24	9.7	100.03	Snow
8781	12/31/2012 21:00	-0.5	-1.5	93	28	4.8	99.95	Snow
8782	12/31/2012 22:00	-0.2	-1.8	89	28	9.7	99.91	Snow
8783	12/31/2012 23:00	0.0	-2.1	86	30	11.3	99.89	Snow
8784 rows × 8 columns

How to Analyze DataFrames ?
.head()
It shows the first N rows in the data (by default, N=5)

1
data.head()
Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa	Weather
0	01-01-2012 00:00	-1.8	-3.9	86	4	8.0	101.24	Fog
1	01-01-2012 01:00	-1.8	-3.7	87	4	8.0	101.24	Fog
2	01-01-2012 02:00	-1.8	-3.4	89	7	4.0	101.26	Freezing Drizzle,Fog
3	01-01-2012 03:00	-1.5	-3.2	88	6	4.0	101.27	Freezing Drizzle,Fog
4	01-01-2012 04:00	-1.5	-3.3	88	7	4.8	101.23	Fog
.shape
It shows the total no. of rows and no. of columns of the dataframe

1
data.shape
(8784, 8)
.index
The attributes provides the index of the dataframe

1
data.index
RangeIndex(start=0, stop=8784, step=1)
.columns
it shows the name of each column

1
data.columns
Index(['Date/Time', 'Temp_C', 'Dew Point Temp_C', 'Rel Hum_%',
       'Wind Speed_km/h', 'Visibility_km', 'Press_kPa', 'Weather'],
      dtype='object')
.dtypes
it shows the data-types of each column

1
data.dtypes
Date/Time            object
Temp_C              float64
Dew Point Temp_C    float64
Rel Hum_%             int64
Wind Speed_km/h       int64
Visibility_km       float64
Press_kPa           float64
Weather              object
dtype: object
.unique()
In a column, it shows all the unique values. it can be applied on a single colimn only, not on the whole dataframe

1
data['Weather'].unique()
array(['Fog', 'Freezing Drizzle,Fog', 'Mostly Cloudy', 'Cloudy', 'Rain',
       'Rain Showers', 'Mainly Clear', 'Snow Showers', 'Snow', 'Clear',
       'Freezing Rain,Fog', 'Freezing Rain', 'Freezing Drizzle',
       'Rain,Snow', 'Moderate Snow', 'Freezing Drizzle,Snow',
       'Freezing Rain,Snow Grains', 'Snow,Blowing Snow', 'Freezing Fog',
       'Haze', 'Rain,Fog', 'Drizzle,Fog', 'Drizzle',
       'Freezing Drizzle,Haze', 'Freezing Rain,Haze', 'Snow,Haze',
       'Snow,Fog', 'Snow,Ice Pellets', 'Rain,Haze', 'Thunderstorms,Rain',
       'Thunderstorms,Rain Showers', 'Thunderstorms,Heavy Rain Showers',
       'Thunderstorms,Rain Showers,Fog', 'Thunderstorms',
       'Thunderstorms,Rain,Fog',
       'Thunderstorms,Moderate Rain Showers,Fog', 'Rain Showers,Fog',
       'Rain Showers,Snow Showers', 'Snow Pellets', 'Rain,Snow,Fog',
       'Moderate Rain,Fog', 'Freezing Rain,Ice Pellets,Fog',
       'Drizzle,Ice Pellets,Fog', 'Drizzle,Snow', 'Rain,Ice Pellets',
       'Drizzle,Snow,Fog', 'Rain,Snow Grains', 'Rain,Snow,Ice Pellets',
       'Snow Showers,Fog', 'Moderate Snow,Blowing Snow'], dtype=object)
.nunique()
It shows the total no. of unique values in each column. It can be applied on single column as well as the whole dataframe.

1
data.nunique()
Date/Time           8784
Temp_C               533
Dew Point Temp_C     489
Rel Hum_%             83
Wind Speed_km/h       34
Visibility_km         24
Press_kPa            518
Weather               50
dtype: int64
.count
It shows the total no. of non-null values in each column. It can be applied on single column as well as the whole dataframe.

1
data.count()
Date/Time           8784
Temp_C              8784
Dew Point Temp_C    8784
Rel Hum_%           8784
Wind Speed_km/h     8784
Visibility_km       8784
Press_kPa           8784
Weather             8784
dtype: int64
.value_counts
In a column, it shows all the unique values with their count. It can be applied on single column only

1
data['Weather'].value_counts()
Weather
Mainly Clear                               2106
Mostly Cloudy                              2069
Cloudy                                     1728
Clear                                      1326
Snow                                        390
Rain                                        306
Rain Showers                                188
Fog                                         150
Rain,Fog                                    116
Drizzle,Fog                                  80
Snow Showers                                 60
Drizzle                                      41
Snow,Fog                                     37
Snow,Blowing Snow                            19
Rain,Snow                                    18
Thunderstorms,Rain Showers                   16
Haze                                         16
Drizzle,Snow,Fog                             15
Freezing Rain                                14
Freezing Drizzle,Snow                        11
Freezing Drizzle                              7
Snow,Ice Pellets                              6
Freezing Drizzle,Fog                          6
Snow,Haze                                     5
Freezing Fog                                  4
Snow Showers,Fog                              4
Moderate Snow                                 4
Rain,Snow,Ice Pellets                         4
Freezing Rain,Fog                             4
Freezing Drizzle,Haze                         3
Rain,Haze                                     3
Thunderstorms,Rain                            3
Thunderstorms,Rain Showers,Fog                3
Freezing Rain,Haze                            2
Drizzle,Snow                                  2
Rain Showers,Snow Showers                     2
Thunderstorms                                 2
Moderate Snow,Blowing Snow                    2
Rain Showers,Fog                              1
Thunderstorms,Moderate Rain Showers,Fog       1
Snow Pellets                                  1
Rain,Snow,Fog                                 1
Moderate Rain,Fog                             1
Freezing Rain,Ice Pellets,Fog                 1
Drizzle,Ice Pellets,Fog                       1
Thunderstorms,Rain,Fog                        1
Rain,Ice Pellets                              1
Rain,Snow Grains                              1
Thunderstorms,Heavy Rain Showers              1
Freezing Rain,Snow Grains                     1
Name: count, dtype: int64
.info()
Provides basic information about the dataframe.

1
data.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 8784 entries, 0 to 8783
Data columns (total 8 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   Date/Time         8784 non-null   object 
 1   Temp_C            8784 non-null   float64
 2   Dew Point Temp_C  8784 non-null   float64
 3   Rel Hum_%         8784 non-null   int64  
 4   Wind Speed_km/h   8784 non-null   int64  
 5   Visibility_km     8784 non-null   float64
 6   Press_kPa         8784 non-null   float64
 7   Weather           8784 non-null   object 
dtypes: float64(4), int64(2), object(2)
memory usage: 549.1+ KB
Q) 1. Find all the unique 'Wind Speed' values in the data.
1
data.head(2)
Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa	Weather
0	01-01-2012 00:00	-1.8	-3.9	86	4	8.0	101.24	Fog
1	01-01-2012 01:00	-1.8	-3.7	87	4	8.0	101.24	Fog
1
data.nunique()
Date/Time           8784
Temp_C               533
Dew Point Temp_C     489
Rel Hum_%             83
Wind Speed_km/h       34
Visibility_km         24
Press_kPa            518
Weather               50
dtype: int64
1
data['Wind Speed_km/h'].nunique()
34
1
data['Wind Speed_km/h'].unique()  #Answere
array([ 4,  7,  6,  9, 15, 13, 20, 22, 19, 24, 30, 35, 39, 32, 33, 26, 44,
       43, 48, 37, 28, 17, 11,  0, 83, 70, 57, 46, 41, 52, 50, 63, 54,  2],
      dtype=int64)
Q) 2. Find the number of times when the 'Weather is exactly clear'
1
data.head(2)
Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa	Weather
0	01-01-2012 00:00	-1.8	-3.9	86	4	8.0	101.24	Fog
1	01-01-2012 01:00	-1.8	-3.7	87	4	8.0	101.24	Fog
1
# value_counts()
2
data.Weather.value_counts()
Weather
Mainly Clear                               2106
Mostly Cloudy                              2069
Cloudy                                     1728
Clear                                      1326
Snow                                        390
Rain                                        306
Rain Showers                                188
Fog                                         150
Rain,Fog                                    116
Drizzle,Fog                                  80
Snow Showers                                 60
Drizzle                                      41
Snow,Fog                                     37
Snow,Blowing Snow                            19
Rain,Snow                                    18
Thunderstorms,Rain Showers                   16
Haze                                         16
Drizzle,Snow,Fog                             15
Freezing Rain                                14
Freezing Drizzle,Snow                        11
Freezing Drizzle                              7
Snow,Ice Pellets                              6
Freezing Drizzle,Fog                          6
Snow,Haze                                     5
Freezing Fog                                  4
Snow Showers,Fog                              4
Moderate Snow                                 4
Rain,Snow,Ice Pellets                         4
Freezing Rain,Fog                             4
Freezing Drizzle,Haze                         3
Rain,Haze                                     3
Thunderstorms,Rain                            3
Thunderstorms,Rain Showers,Fog                3
Freezing Rain,Haze                            2
Drizzle,Snow                                  2
Rain Showers,Snow Showers                     2
Thunderstorms                                 2
Moderate Snow,Blowing Snow                    2
Rain Showers,Fog                              1
Thunderstorms,Moderate Rain Showers,Fog       1
Snow Pellets                                  1
Rain,Snow,Fog                                 1
Moderate Rain,Fog                             1
Freezing Rain,Ice Pellets,Fog                 1
Drizzle,Ice Pellets,Fog                       1
Thunderstorms,Rain,Fog                        1
Rain,Ice Pellets                              1
Rain,Snow Grains                              1
Thunderstorms,Heavy Rain Showers              1
Freezing Rain,Snow Grains                     1
Name: count, dtype: int64
1
# Filtering
2
data.head(2)
3
data[data.Weather == 'Clear']
Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa	Weather
67	01-03-2012 19:00	-16.9	-24.8	50	24	25.0	101.74	Clear
114	01-05-2012 18:00	-7.1	-14.4	56	11	25.0	100.71	Clear
115	01-05-2012 19:00	-9.2	-15.4	61	7	25.0	100.80	Clear
116	01-05-2012 20:00	-9.8	-15.7	62	9	25.0	100.83	Clear
117	01-05-2012 21:00	-9.0	-14.8	63	13	25.0	100.83	Clear
...	...	...	...	...	...	...	...	...
8646	12/26/2012 6:00	-13.4	-14.8	89	4	25.0	102.47	Clear
8698	12/28/2012 10:00	-6.1	-8.6	82	19	24.1	101.27	Clear
8713	12/29/2012 1:00	-11.9	-13.6	87	11	25.0	101.31	Clear
8714	12/29/2012 2:00	-11.8	-13.1	90	13	25.0	101.33	Clear
8756	12/30/2012 20:00	-13.8	-16.5	80	24	25.0	101.52	Clear
1326 rows × 8 columns

1
#groupby()
2
data.head(2)
3
data.groupby('Weather').get_group('Clear')
Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa	Weather
67	01-03-2012 19:00	-16.9	-24.8	50	24	25.0	101.74	Clear
114	01-05-2012 18:00	-7.1	-14.4	56	11	25.0	100.71	Clear
115	01-05-2012 19:00	-9.2	-15.4	61	7	25.0	100.80	Clear
116	01-05-2012 20:00	-9.8	-15.7	62	9	25.0	100.83	Clear
117	01-05-2012 21:00	-9.0	-14.8	63	13	25.0	100.83	Clear
...	...	...	...	...	...	...	...	...
8646	12/26/2012 6:00	-13.4	-14.8	89	4	25.0	102.47	Clear
8698	12/28/2012 10:00	-6.1	-8.6	82	19	24.1	101.27	Clear
8713	12/29/2012 1:00	-11.9	-13.6	87	11	25.0	101.31	Clear
8714	12/29/2012 2:00	-11.8	-13.1	90	13	25.0	101.33	Clear
8756	12/30/2012 20:00	-13.8	-16.5	80	24	25.0	101.52	Clear
1326 rows × 8 columns

Q) 3. Find the number of times when the 'Wind Speed was exactly 4 km/h'.
1
data.head(2)
Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa	Weather
0	01-01-2012 00:00	-1.8	-3.9	86	4	8.0	101.24	Fog
1	01-01-2012 01:00	-1.8	-3.7	87	4	8.0	101.24	Fog
1
data[data['Wind Speed_km/h'] == 4]
Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa	Weather
0	01-01-2012 00:00	-1.8	-3.9	86	4	8.0	101.24	Fog
1	01-01-2012 01:00	-1.8	-3.7	87	4	8.0	101.24	Fog
96	01-05-2012 00:00	-8.8	-11.7	79	4	9.7	100.32	Snow
101	01-05-2012 05:00	-7.0	-9.5	82	4	4.0	100.19	Snow
146	01-07-2012 02:00	-8.1	-11.1	79	4	19.3	100.15	Cloudy
...	...	...	...	...	...	...	...	...
8768	12/31/2012 8:00	-8.6	-10.3	87	4	3.2	101.14	Snow Showers
8769	12/31/2012 9:00	-8.1	-9.6	89	4	2.4	101.09	Snow
8770	12/31/2012 10:00	-7.4	-8.9	89	4	6.4	101.05	Snow,Fog
8772	12/31/2012 12:00	-5.8	-7.5	88	4	12.9	100.78	Snow
8773	12/31/2012 13:00	-4.6	-6.6	86	4	12.9	100.63	Snow
474 rows × 8 columns

Q) 4. Find out all the Null Values in the data.
1
data.isnull().sum()
Date/Time           0
Temp_C              0
Dew Point Temp_C    0
Rel Hum_%           0
Wind Speed_km/h     0
Visibility_km       0
Press_kPa           0
Weather             0
dtype: int64
1
data.notnull().sum()
Date/Time           8784
Temp_C              8784
Dew Point Temp_C    8784
Rel Hum_%           8784
Wind Speed_km/h     8784
Visibility_km       8784
Press_kPa           8784
Weather             8784
dtype: int64
Q. 5) Rename the column name 'Weather' of the dataframe to 'Weather Condition'.
1
data.head(2)
Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa	Weather
0	01-01-2012 00:00	-1.8	-3.9	86	4	8.0	101.24	Fog
1	01-01-2012 01:00	-1.8	-3.7	87	4	8.0	101.24	Fog
1
data.rename(columns={'Weather': 'Weather Condition'}, inplace= True)
1
data.head()
Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa	Weather Condition
0	01-01-2012 00:00	-1.8	-3.9	86	4	8.0	101.24	Fog
1	01-01-2012 01:00	-1.8	-3.7	87	4	8.0	101.24	Fog
2	01-01-2012 02:00	-1.8	-3.4	89	7	4.0	101.26	Freezing Drizzle,Fog
3	01-01-2012 03:00	-1.5	-3.2	88	6	4.0	101.27	Freezing Drizzle,Fog
4	01-01-2012 04:00	-1.5	-3.3	88	7	4.8	101.23	Fog
Q.6) What is the mean 'Visibility' ?
1
data.head(2)
Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa	Weather Condition
0	01-01-2012 00:00	-1.8	-3.9	86	4	8.0	101.24	Fog
1	01-01-2012 01:00	-1.8	-3.7	87	4	8.0	101.24	Fog
1
data.Visibility_km.mean()
27.664446721311478
Q.7) What is the Standard Deviation of 'Pressure' in this data?
1
data.head(2)
Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa	Weather Condition
0	01-01-2012 00:00	-1.8	-3.9	86	4	8.0	101.24	Fog
1	01-01-2012 01:00	-1.8	-3.7	87	4	8.0	101.24	Fog
1
data.Press_kPa.std()
0.8440047459486474
Q.8) What is the Variance of 'Relative Humidity 'in thia data
1
data['Rel Hum_%'].var()
286.2485501984998
Q.9) Find all instances when 'Snow' was recorded
1
#value_counts()
2
data['Weather Condition'].value_counts()
Weather Condition
Mainly Clear                               2106
Mostly Cloudy                              2069
Cloudy                                     1728
Clear                                      1326
Snow                                        390
Rain                                        306
Rain Showers                                188
Fog                                         150
Rain,Fog                                    116
Drizzle,Fog                                  80
Snow Showers                                 60
Drizzle                                      41
Snow,Fog                                     37
Snow,Blowing Snow                            19
Rain,Snow                                    18
Thunderstorms,Rain Showers                   16
Haze                                         16
Drizzle,Snow,Fog                             15
Freezing Rain                                14
Freezing Drizzle,Snow                        11
Freezing Drizzle                              7
Snow,Ice Pellets                              6
Freezing Drizzle,Fog                          6
Snow,Haze                                     5
Freezing Fog                                  4
Snow Showers,Fog                              4
Moderate Snow                                 4
Rain,Snow,Ice Pellets                         4
Freezing Rain,Fog                             4
Freezing Drizzle,Haze                         3
Rain,Haze                                     3
Thunderstorms,Rain                            3
Thunderstorms,Rain Showers,Fog                3
Freezing Rain,Haze                            2
Drizzle,Snow                                  2
Rain Showers,Snow Showers                     2
Thunderstorms                                 2
Moderate Snow,Blowing Snow                    2
Rain Showers,Fog                              1
Thunderstorms,Moderate Rain Showers,Fog       1
Snow Pellets                                  1
Rain,Snow,Fog                                 1
Moderate Rain,Fog                             1
Freezing Rain,Ice Pellets,Fog                 1
Drizzle,Ice Pellets,Fog                       1
Thunderstorms,Rain,Fog                        1
Rain,Ice Pellets                              1
Rain,Snow Grains                              1
Thunderstorms,Heavy Rain Showers              1
Freezing Rain,Snow Grains                     1
Name: count, dtype: int64
1
#Filtering
2
data[data['Weather Condition'] == 'Snow']
Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa	Weather Condition
55	01-03-2012 07:00	-14.0	-19.5	63	19	25.0	100.95	Snow
84	01-04-2012 12:00	-13.7	-21.7	51	11	24.1	101.25	Snow
86	01-04-2012 14:00	-11.3	-19.0	53	7	19.3	100.97	Snow
87	01-04-2012 15:00	-10.2	-16.3	61	11	9.7	100.89	Snow
88	01-04-2012 16:00	-9.4	-15.5	61	13	19.3	100.79	Snow
...	...	...	...	...	...	...	...	...
8779	12/31/2012 19:00	0.1	-2.7	81	30	9.7	100.13	Snow
8780	12/31/2012 20:00	0.2	-2.4	83	24	9.7	100.03	Snow
8781	12/31/2012 21:00	-0.5	-1.5	93	28	4.8	99.95	Snow
8782	12/31/2012 22:00	-0.2	-1.8	89	28	9.7	99.91	Snow
8783	12/31/2012 23:00	0.0	-2.1	86	30	11.3	99.89	Snow
390 rows × 8 columns

1
#str.contains
2
data[data['Weather Condition'].str.contains('Snow')].tail(50)
Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa	Weather Condition
8680	12/27/2012 16:00	-4.5	-6.2	88	37	2.0	100.44	Snow,Blowing Snow
8681	12/27/2012 17:00	-4.2	-5.9	88	32	3.2	100.47	Snow,Blowing Snow
8682	12/27/2012 18:00	-4.0	-5.7	88	28	8.0	100.49	Snow,Blowing Snow
8683	12/27/2012 19:00	-3.9	-5.6	88	26	9.7	100.52	Snow,Blowing Snow
8684	12/27/2012 20:00	-3.7	-5.3	89	37	16.1	100.58	Snow
8685	12/27/2012 21:00	-3.7	-4.8	92	24	4.8	100.62	Freezing Drizzle,Snow
8686	12/27/2012 22:00	-3.8	-4.6	94	20	4.8	100.65	Freezing Drizzle,Snow
8687	12/27/2012 23:00	-4.0	-5.6	89	24	9.7	100.70	Snow
8688	12/28/2012 0:00	-4.2	-5.7	89	19	8.0	100.78	Freezing Drizzle,Snow
8689	12/28/2012 1:00	-4.4	-6.6	85	15	6.4	100.83	Freezing Drizzle,Snow
8690	12/28/2012 2:00	-4.3	-6.3	86	11	12.9	100.93	Freezing Drizzle,Snow
8691	12/28/2012 3:00	-4.6	-5.9	91	13	4.0	101.01	Snow
8692	12/28/2012 4:00	-4.9	-5.9	93	9	9.7	101.00	Snow
8723	12/29/2012 11:00	-10.9	-12.2	90	7	6.4	101.09	Snow Showers,Fog
8724	12/29/2012 12:00	-10.5	-11.6	92	11	8.0	100.93	Snow Showers,Fog
8725	12/29/2012 13:00	-10.0	-11.1	92	22	9.7	100.63	Snow Showers,Fog
8726	12/29/2012 14:00	-9.3	-10.5	91	22	4.8	100.60	Snow,Fog
8727	12/29/2012 15:00	-8.8	-10.0	91	20	1.2	100.55	Snow,Fog
8728	12/29/2012 16:00	-8.5	-9.9	90	24	1.2	100.49	Snow,Fog
8729	12/29/2012 17:00	-9.0	-10.4	90	19	2.4	100.46	Snow,Fog
8730	12/29/2012 18:00	-9.3	-10.9	88	26	6.4	100.38	Snow,Fog
8731	12/29/2012 19:00	-9.5	-11.2	87	26	3.2	100.33	Snow,Fog
8732	12/29/2012 20:00	-9.7	-11.6	86	24	9.7	100.25	Snow,Fog
8733	12/29/2012 21:00	-9.8	-11.8	85	24	8.0	100.24	Snow,Fog
8734	12/29/2012 22:00	-10.1	-11.6	89	15	2.4	100.20	Snow,Fog
8735	12/29/2012 23:00	-10.0	-12.0	85	20	6.4	100.19	Snow,Fog
8736	12/30/2012 0:00	-9.6	-11.3	87	13	3.2	100.23	Snow,Fog
8737	12/30/2012 1:00	-9.4	-10.5	92	9	2.4	100.22	Snow,Fog
8738	12/30/2012 2:00	-9.3	-10.4	92	9	4.0	100.28	Snow,Fog
8739	12/30/2012 3:00	-9.1	-10.4	90	11	3.6	100.30	Snow,Fog
8740	12/30/2012 4:00	-9.3	-10.6	90	13	9.7	100.28	Snow,Fog
8741	12/30/2012 5:00	-9.1	-10.4	90	11	4.0	100.32	Snow,Fog
8742	12/30/2012 6:00	-9.3	-10.8	89	17	8.0	100.39	Snow,Fog
8767	12/31/2012 7:00	-9.3	-11.3	85	0	19.3	101.19	Snow Showers
8768	12/31/2012 8:00	-8.6	-10.3	87	4	3.2	101.14	Snow Showers
8769	12/31/2012 9:00	-8.1	-9.6	89	4	2.4	101.09	Snow
8770	12/31/2012 10:00	-7.4	-8.9	89	4	6.4	101.05	Snow,Fog
8771	12/31/2012 11:00	-6.7	-7.9	91	9	9.7	100.93	Snow
8772	12/31/2012 12:00	-5.8	-7.5	88	4	12.9	100.78	Snow
8773	12/31/2012 13:00	-4.6	-6.6	86	4	12.9	100.63	Snow
8774	12/31/2012 14:00	-3.4	-5.7	84	6	11.3	100.57	Snow
8775	12/31/2012 15:00	-2.3	-4.6	84	9	9.7	100.47	Snow
8776	12/31/2012 16:00	-1.4	-4.0	82	13	12.9	100.40	Snow
8777	12/31/2012 17:00	-1.1	-3.3	85	19	9.7	100.30	Snow
8778	12/31/2012 18:00	-1.3	-3.1	88	17	9.7	100.19	Snow
8779	12/31/2012 19:00	0.1	-2.7	81	30	9.7	100.13	Snow
8780	12/31/2012 20:00	0.2	-2.4	83	24	9.7	100.03	Snow
8781	12/31/2012 21:00	-0.5	-1.5	93	28	4.8	99.95	Snow
8782	12/31/2012 22:00	-0.2	-1.8	89	28	9.7	99.91	Snow
8783	12/31/2012 23:00	0.0	-2.1	86	30	11.3	99.89	Snow
Q.10) Find all the instances when 'When Speed is above 24'and 'Visibility'is 25'.
1
data[(data['Wind Speed_km/h'] > 24) &  (data['Visibility_km'] == 25)]
Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa	Weather Condition
23	01-01-2012 23:00	5.3	2.0	79	30	25.0	99.31	Cloudy
24	01-02-2012 00:00	5.2	1.5	77	35	25.0	99.26	Rain Showers
25	01-02-2012 01:00	4.6	0.0	72	39	25.0	99.26	Cloudy
26	01-02-2012 02:00	3.9	-0.9	71	32	25.0	99.26	Mostly Cloudy
27	01-02-2012 03:00	3.7	-1.5	69	33	25.0	99.30	Mostly Cloudy
...	...	...	...	...	...	...	...	...
8705	12/28/2012 17:00	-8.6	-12.0	76	26	25.0	101.34	Mainly Clear
8753	12/30/2012 17:00	-12.1	-15.8	74	28	25.0	101.26	Mainly Clear
8755	12/30/2012 19:00	-13.4	-16.5	77	26	25.0	101.47	Mainly Clear
8759	12/30/2012 23:00	-12.1	-15.1	78	28	25.0	101.52	Mostly Cloudy
8760	12/31/2012 0:00	-11.1	-14.4	77	26	25.0	101.51	Cloudy
308 rows × 8 columns

Q.11) What is the Mean value of each column against each 'Weather Condition'?
1
data.head(2)
Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa	Weather Condition
0	01-01-2012 00:00	-1.8	-3.9	86	4	8.0	101.24	Fog
1	01-01-2012 01:00	-1.8	-3.7	87	4	8.0	101.24	Fog
1
data.groupby('Weather Condition').mean(numeric_only=True)
2
​
Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa
Weather Condition						
Clear	6.825716	0.089367	64.497738	10.557315	30.153243	101.587443
Cloudy	7.970544	2.375810	69.592593	16.127315	26.625752	100.911441
Drizzle	7.353659	5.504878	88.243902	16.097561	17.931707	100.435366
Drizzle,Fog	8.067500	7.033750	93.275000	11.862500	5.257500	100.786625
Drizzle,Ice Pellets,Fog	0.400000	-0.700000	92.000000	20.000000	4.000000	100.790000
Drizzle,Snow	1.050000	0.150000	93.500000	14.000000	10.500000	100.890000
Drizzle,Snow,Fog	0.693333	0.120000	95.866667	15.533333	5.513333	99.281333
Fog	4.303333	3.159333	92.286667	7.946667	6.248000	101.184067
Freezing Drizzle	-5.657143	-8.000000	83.571429	16.571429	9.200000	100.202857
Freezing Drizzle,Fog	-2.533333	-4.183333	88.500000	17.000000	5.266667	100.441667
Freezing Drizzle,Haze	-5.433333	-8.000000	82.000000	10.333333	2.666667	100.316667
Freezing Drizzle,Snow	-5.109091	-7.072727	86.090909	16.272727	5.872727	100.520909
Freezing Fog	-7.575000	-9.250000	87.750000	4.750000	0.650000	102.320000
Freezing Rain	-3.885714	-6.078571	84.642857	19.214286	8.242857	99.647143
Freezing Rain,Fog	-2.225000	-3.750000	89.500000	15.500000	7.550000	99.945000
Freezing Rain,Haze	-4.900000	-7.450000	82.500000	7.500000	2.400000	100.375000
Freezing Rain,Ice Pellets,Fog	-2.600000	-3.700000	92.000000	28.000000	8.000000	100.950000
Freezing Rain,Snow Grains	-5.000000	-7.300000	84.000000	32.000000	4.800000	98.560000
Haze	-0.200000	-2.975000	81.625000	10.437500	7.831250	101.482500
Mainly Clear	12.558927	4.581671	60.667142	14.144824	34.264862	101.248832
Moderate Rain,Fog	1.700000	0.800000	94.000000	17.000000	6.400000	99.980000
Moderate Snow	-5.525000	-7.250000	87.750000	33.750000	0.750000	100.275000
Moderate Snow,Blowing Snow	-5.450000	-6.500000	92.500000	40.000000	0.600000	100.570000
Mostly Cloudy	10.574287	3.131174	62.102465	15.813920	31.253842	101.025288
Rain	9.786275	7.042810	83.624183	19.254902	18.856536	100.233333
Rain Showers	13.722340	9.187766	75.159574	17.132979	22.816489	100.404043
Rain Showers,Fog	12.800000	12.100000	96.000000	13.000000	6.400000	99.830000
Rain Showers,Snow Showers	2.150000	-1.500000	76.500000	22.500000	21.700000	101.100000
Rain,Fog	8.273276	7.219828	93.189655	14.793103	6.873276	100.500862
Rain,Haze	4.633333	2.066667	83.333333	11.666667	6.700000	100.540000
Rain,Ice Pellets	0.600000	-0.600000	92.000000	24.000000	9.700000	100.120000
Rain,Snow	1.055556	-0.566667	89.000000	28.388889	11.672222	99.951111
Rain,Snow Grains	1.900000	-2.100000	75.000000	26.000000	25.000000	100.600000
Rain,Snow,Fog	0.800000	0.300000	96.000000	9.000000	6.400000	100.730000
Rain,Snow,Ice Pellets	1.100000	-0.175000	91.500000	23.250000	6.000000	100.105000
Snow	-4.524103	-7.623333	79.307692	20.038462	11.171795	100.536103
Snow Pellets	0.700000	-6.400000	59.000000	35.000000	2.400000	99.700000
Snow Showers	-3.506667	-7.866667	72.350000	19.233333	20.158333	100.963500
Snow Showers,Fog	-10.675000	-11.900000	90.750000	13.750000	7.025000	101.292500
Snow,Blowing Snow	-5.410526	-7.621053	84.473684	34.842105	4.105263	99.704737
Snow,Fog	-5.075676	-6.364865	90.675676	17.324324	4.537838	100.688649
Snow,Haze	-4.020000	-6.860000	80.600000	5.000000	4.640000	100.782000
Snow,Ice Pellets	-1.883333	-3.666667	87.666667	23.833333	7.416667	100.548333
Thunderstorms	24.150000	19.750000	77.000000	7.500000	24.550000	100.230000
Thunderstorms,Heavy Rain Showers	10.900000	9.000000	88.000000	9.000000	2.400000	100.260000
Thunderstorms,Moderate Rain Showers,Fog	19.600000	18.500000	93.000000	15.000000	3.200000	100.010000
Thunderstorms,Rain	20.433333	18.533333	89.000000	15.666667	19.833333	100.420000
Thunderstorms,Rain Showers	20.037500	17.618750	86.375000	18.312500	15.893750	100.233750
Thunderstorms,Rain Showers,Fog	21.600000	18.700000	84.000000	19.666667	9.700000	100.063333
Thunderstorms,Rain,Fog	20.600000	18.600000	88.000000	19.000000	4.800000	100.080000
Q. 12 What is the Minimum and Maximum value of each column against each 'Weather Condition'?
1
data.groupby('Weather Condition').min()
Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa
Weather Condition							
Clear	01-03-2012 19:00	-23.3	-28.5	20	0	11.3	99.52
Cloudy	01-01-2012 17:00	-21.4	-26.8	18	0	11.3	98.39
Drizzle	05-01-2012 15:00	1.1	-0.2	74	0	6.4	97.84
Drizzle,Fog	05-01-2012 16:00	0.0	-1.6	85	0	1.0	98.65
Drizzle,Ice Pellets,Fog	12/17/2012 9:00	0.4	-0.7	92	20	4.0	100.79
Drizzle,Snow	12/17/2012 15:00	0.9	0.1	92	9	9.7	100.63
Drizzle,Snow,Fog	12/18/2012 21:00	0.3	-0.1	92	7	2.4	97.79
Fog	01-01-2012 00:00	-16.0	-17.2	80	0	0.2	98.31
Freezing Drizzle	01-07-2012 11:00	-9.0	-12.2	78	6	4.8	98.44
Freezing Drizzle,Fog	01-01-2012 02:00	-6.4	-9.0	82	6	3.6	98.74
Freezing Drizzle,Haze	02-01-2012 11:00	-5.8	-8.3	81	9	2.0	100.28
Freezing Drizzle,Snow	03-02-2012 12:00	-8.3	-10.4	79	6	2.4	99.19
Freezing Fog	02-05-2012 10:00	-19.0	-22.9	71	0	0.2	101.97
Freezing Rain	01-07-2012 10:00	-6.5	-9.0	81	7	2.8	98.22
Freezing Rain,Fog	01-07-2012 09:00	-6.1	-8.7	82	7	2.8	98.32
Freezing Rain,Haze	02-01-2012 14:00	-4.9	-7.5	82	6	2.0	100.34
Freezing Rain,Ice Pellets,Fog	12/17/2012 3:00	-2.6	-3.7	92	28	8.0	100.95
Freezing Rain,Snow Grains	1/13/2012 9:00	-5.0	-7.3	84	32	4.8	98.56
Haze	02-01-2012 10:00	-11.5	-16.0	68	0	4.8	100.35
Mainly Clear	01-02-2012 12:00	-22.8	-28.0	20	0	12.9	98.67
Moderate Rain,Fog	12-10-2012 08:00	1.7	0.8	94	17	6.4	99.98
Moderate Snow	01-12-2012 15:00	-6.3	-7.6	83	26	0.6	99.88
Moderate Snow,Blowing Snow	12/27/2012 10:00	-5.5	-6.6	92	39	0.6	100.50
Mostly Cloudy	01-01-2012 16:00	-23.2	-28.5	18	0	11.3	98.36
Rain	01-01-2012 18:00	0.3	-5.7	40	0	4.0	97.52
Rain Showers	01-01-2012 22:00	1.6	-7.2	37	0	6.4	98.51
Rain Showers,Fog	10/20/2012 3:00	12.8	12.1	96	13	6.4	99.83
Rain Showers,Snow Showers	11-04-2012 08:00	2.1	-1.8	75	17	19.3	101.09
Rain,Fog	03-08-2012 22:00	0.0	-1.2	83	0	2.0	98.61
Rain,Haze	3/13/2012 7:00	4.0	1.0	81	7	4.0	100.50
Rain,Ice Pellets	12/18/2012 5:00	0.6	-0.6	92	24	9.7	100.12
Rain,Snow	01-10-2012 05:00	0.6	-1.7	81	13	2.4	98.18
Rain,Snow Grains	12/21/2012 0:00	1.9	-2.1	75	26	25.0	100.60
Rain,Snow,Fog	12-08-2012 21:00	0.8	0.3	96	9	6.4	100.73
Rain,Snow,Ice Pellets	12/21/2012 1:00	0.9	-0.7	88	17	4.8	99.85
Snow	01-03-2012 07:00	-16.7	-24.6	41	0	1.0	97.75
Snow Pellets	11/24/2012 15:00	0.7	-6.4	59	35	2.4	99.70
Snow Showers	01-02-2012 17:00	-13.3	-19.3	52	0	2.4	99.49
Snow Showers,Fog	12/26/2012 9:00	-11.3	-12.7	89	7	4.0	100.63
Snow,Blowing Snow	1/13/2012 21:00	-12.0	-16.2	70	24	0.6	98.11
Snow,Fog	02-10-2012 23:00	-10.1	-12.0	77	4	1.2	99.38
Snow,Haze	02-01-2012 17:00	-4.3	-7.2	80	0	4.0	100.61
Snow,Ice Pellets	03-03-2012 04:00	-4.3	-5.9	76	19	2.8	99.40
Thunderstorms	07-04-2012 16:00	21.6	19.4	67	0	24.1	99.84
Thunderstorms,Heavy Rain Showers	5/29/2012 6:00	10.9	9.0	88	9	2.4	100.26
Thunderstorms,Moderate Rain Showers,Fog	7/17/2012 6:00	19.6	18.5	93	15	3.2	100.01
Thunderstorms,Rain	5/25/2012 20:00	19.4	18.2	83	4	16.1	100.19
Thunderstorms,Rain Showers	07-04-2012 17:00	11.0	7.0	68	7	6.4	99.65
Thunderstorms,Rain Showers,Fog	6/29/2012 3:00	19.5	16.1	80	7	9.7	99.71
Thunderstorms,Rain,Fog	7/17/2012 5:00	20.6	18.6	88	19	4.8	100.08
1
data.groupby('Weather Condition').max()
Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa
Weather Condition							
Clear	9/28/2012 4:00	32.8	20.4	99	33	48.3	103.63
Cloudy	9/30/2012 9:00	30.5	22.6	99	54	48.3	103.65
Drizzle	9/30/2012 3:00	18.8	17.7	96	30	25.0	101.56
Drizzle,Fog	9/30/2012 2:00	19.9	19.1	100	28	9.7	102.07
Drizzle,Ice Pellets,Fog	12/17/2012 9:00	0.4	-0.7	92	20	4.0	100.79
Drizzle,Snow	12/19/2012 18:00	1.2	0.2	95	19	11.3	101.15
Drizzle,Snow,Fog	12/22/2012 3:00	1.1	0.6	98	32	9.7	100.15
Fog	9/22/2012 0:00	20.8	19.6	100	22	9.7	103.04
Freezing Drizzle	12/17/2012 0:00	-2.3	-3.3	93	26	12.9	101.02
Freezing Drizzle,Fog	12-10-2012 05:00	-0.3	-2.3	94	33	8.0	101.27
Freezing Drizzle,Haze	02-01-2012 13:00	-5.0	-7.7	83	11	4.0	100.36
Freezing Drizzle,Snow	12/28/2012 2:00	-3.3	-4.6	94	24	12.9	101.18
Freezing Fog	3/17/2012 6:00	-0.1	-0.3	99	9	0.8	102.85
Freezing Rain	12/17/2012 2:00	0.3	-1.7	92	28	16.1	101.00
Freezing Rain,Fog	12/17/2012 1:00	0.1	-0.9	93	26	9.7	101.01
Freezing Rain,Haze	02-01-2012 15:00	-4.9	-7.4	83	9	2.8	100.41
Freezing Rain,Ice Pellets,Fog	12/17/2012 3:00	-2.6	-3.7	92	28	8.0	100.95
Freezing Rain,Snow Grains	1/13/2012 9:00	-5.0	-7.3	84	32	4.8	98.56
Haze	3/13/2012 23:00	14.1	11.1	86	17	9.7	102.97
Mainly Clear	9/28/2012 8:00	33.0	21.2	99	63	48.3	103.59
Moderate Rain,Fog	12-10-2012 08:00	1.7	0.8	94	17	6.4	99.98
Moderate Snow	12/27/2012 9:00	-4.9	-6.7	93	39	0.8	100.67
Moderate Snow,Blowing Snow	12/27/2012 12:00	-5.4	-6.4	93	41	0.6	100.64
Mostly Cloudy	9/29/2012 9:00	32.4	24.4	100	83	48.3	103.65
Rain	9/30/2012 22:00	22.8	20.4	99	52	48.3	102.26
Rain Showers	9/26/2012 16:00	26.4	23.0	97	41	48.3	102.31
Rain Showers,Fog	10/20/2012 3:00	12.8	12.1	96	13	6.4	99.83
Rain Showers,Snow Showers	12-05-2012 10:00	2.2	-1.2	78	28	24.1	101.11
Rain,Fog	9/30/2012 23:00	21.7	19.5	100	46	9.7	101.77
Rain,Haze	3/13/2012 9:00	5.5	2.9	86	17	9.7	100.61
Rain,Ice Pellets	12/18/2012 5:00	0.6	-0.6	92	24	9.7	100.12
Rain,Snow	4/23/2012 3:00	1.7	0.5	94	52	25.0	101.07
Rain,Snow Grains	12/21/2012 0:00	1.9	-2.1	75	26	25.0	100.60
Rain,Snow,Fog	12-08-2012 21:00	0.8	0.3	96	9	6.4	100.73
Rain,Snow,Ice Pellets	12/21/2012 5:00	1.3	0.1	94	28	6.4	100.47
Snow	4/27/2012 9:00	3.7	0.3	96	57	25.0	102.73
Snow Pellets	11/24/2012 15:00	0.7	-6.4	59	35	2.4	99.70
Snow Showers	2/23/2012 13:00	2.9	-0.7	94	37	48.3	102.50
Snow Showers,Fog	12/29/2012 13:00	-10.0	-11.1	92	22	9.7	102.52
Snow,Blowing Snow	2/25/2012 9:00	-1.4	-2.9	91	48	9.7	100.62
Snow,Fog	3/14/2012 19:00	1.1	0.8	99	35	9.7	102.07
Snow,Haze	02-01-2012 21:00	-3.6	-6.4	81	15	6.4	100.99
Snow,Ice Pellets	3/28/2012 8:00	0.8	-1.7	92	33	11.3	100.96
Thunderstorms	7/16/2012 1:00	26.7	20.1	87	15	25.0	100.62
Thunderstorms,Heavy Rain Showers	5/29/2012 6:00	10.9	9.0	88	9	2.4	100.26
Thunderstorms,Moderate Rain Showers,Fog	7/17/2012 6:00	19.6	18.5	93	15	3.2	100.01
Thunderstorms,Rain	7/23/2012 18:00	21.3	19.1	93	30	24.1	100.83
Thunderstorms,Rain Showers	9/14/2012 20:00	25.5	23.1	98	32	25.0	101.06
Thunderstorms,Rain Showers,Fog	7/31/2012 20:00	22.9	21.3	91	35	9.7	100.64
Thunderstorms,Rain,Fog	7/17/2012 5:00	20.6	18.6	88	19	4.8	100.08
Q.13) show all the records where Weather Condition is Fog.
1
data[data['Weather Condition'] == 'Fog']
Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa	Weather Condition
0	01-01-2012 00:00	-1.8	-3.9	86	4	8.0	101.24	Fog
1	01-01-2012 01:00	-1.8	-3.7	87	4	8.0	101.24	Fog
4	01-01-2012 04:00	-1.5	-3.3	88	7	4.8	101.23	Fog
5	01-01-2012 05:00	-1.4	-3.3	87	9	6.4	101.27	Fog
6	01-01-2012 06:00	-1.5	-3.1	89	7	6.4	101.29	Fog
...	...	...	...	...	...	...	...	...
8716	12/29/2012 4:00	-16.0	-17.2	90	6	9.7	101.25	Fog
8717	12/29/2012 5:00	-14.8	-15.9	91	4	6.4	101.25	Fog
8718	12/29/2012 6:00	-13.8	-15.3	88	4	9.7	101.25	Fog
8719	12/29/2012 7:00	-14.8	-16.4	88	7	8.0	101.22	Fog
8722	12/29/2012 10:00	-12.0	-13.3	90	7	6.4	101.15	Fog
150 rows × 8 columns

Q.14) Find all the instances when 'Weather is Clear' or 'Visibility is above 40'.
1
data[(data['Weather Condition']=='Clear') | (data['Visibility_km'] > 40)]
Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa	Weather Condition
67	01-03-2012 19:00	-16.9	-24.8	50	24	25.0	101.74	Clear
106	01-05-2012 10:00	-6.0	-10.0	73	17	48.3	100.45	Mainly Clear
107	01-05-2012 11:00	-5.6	-10.2	70	22	48.3	100.41	Mainly Clear
108	01-05-2012 12:00	-4.7	-9.6	69	20	48.3	100.38	Mainly Clear
109	01-05-2012 13:00	-4.4	-9.7	66	26	48.3	100.40	Mainly Clear
...	...	...	...	...	...	...	...	...
8749	12/30/2012 13:00	-12.4	-16.2	73	37	48.3	100.92	Mostly Cloudy
8750	12/30/2012 14:00	-11.8	-16.1	70	37	48.3	100.96	Mainly Clear
8751	12/30/2012 15:00	-11.3	-15.6	70	32	48.3	101.05	Mainly Clear
8752	12/30/2012 16:00	-11.4	-15.5	72	26	48.3	101.15	Mainly Clear
8756	12/30/2012 20:00	-13.8	-16.5	80	24	25.0	101.52	Clear
3027 rows × 8 columns

Q 15) Find all the instances when:
A. 'Weather is Clear' and 'Relative Humidity is greater than 50'

or

B. 'Visibility is above 40'
1
data.head(2)
Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa	Weather Condition
0	01-01-2012 00:00	-1.8	-3.9	86	4	8.0	101.24	Fog
1	01-01-2012 01:00	-1.8	-3.7	87	4	8.0	101.24	Fog
1
data[(data['Weather Condition']== 'Clear')&(data['Rel Hum_%']>50)|(data['Visibility_km']>40)]
Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa	Weather Condition
106	01-05-2012 10:00	-6.0	-10.0	73	17	48.3	100.45	Mainly Clear
107	01-05-2012 11:00	-5.6	-10.2	70	22	48.3	100.41	Mainly Clear
108	01-05-2012 12:00	-4.7	-9.6	69	20	48.3	100.38	Mainly Clear
109	01-05-2012 13:00	-4.4	-9.7	66	26	48.3	100.40	Mainly Clear
110	01-05-2012 14:00	-5.1	-10.7	65	22	48.3	100.46	Mainly Clear
...	...	...	...	...	...	...	...	...
8749	12/30/2012 13:00	-12.4	-16.2	73	37	48.3	100.92	Mostly Cloudy
8750	12/30/2012 14:00	-11.8	-16.1	70	37	48.3	100.96	Mainly Clear
8751	12/30/2012 15:00	-11.3	-15.6	70	32	48.3	101.05	Mainly Clear
8752	12/30/2012 16:00	-11.4	-15.5	72	26	48.3	101.15	Mainly Clear
8756	12/30/2012 20:00	-13.8	-16.5	80	24	25.0	101.52	Clear
2921 rows × 8 columns

1
​
