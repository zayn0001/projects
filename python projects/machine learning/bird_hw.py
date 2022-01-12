import pandas as pd
import datetime
import matplotlib.pyplot as plt

birddata = pd.read_csv("C:\\Users\\mishal\\Desktop\\pdfs\\bird_tracking.csv")

dates = []
for i in range(birddata.date_time.size):
    date_str = birddata.date_time[i]
    date = datetime.datetime.strptime(date_str[:-12], "%Y-%m-%d")
    dates.append(date)

birddata['date'] = pd.Series(dates)

daily_mean_altitude = birddata.groupby(['bird_name','date']).altitude.mean()
daily_mean_speed = birddata.groupby(['bird_name','date']).speed_2d.mean()


eric_daily_speed  = birddata[birddata.bird_name=='Eric'].groupby('date').speed_2d.mean()
sanne_daily_speed = birddata[birddata.bird_name=='Sanne'].groupby('date').speed_2d.mean()
nico_daily_speed  = birddata[birddata.bird_name=='Nico'].groupby('date').speed_2d.mean()

eric_daily_altitude  = birddata[birddata.bird_name=='Eric'].groupby('date').altitude.mean()
sanne_daily_altitude = birddata[birddata.bird_name=='Sanne'].groupby('date').altitude.mean()
nico_daily_altitude  = birddata[birddata.bird_name=='Nico'].groupby('date').altitude.mean()

plt.figure(figsize=(20,20))

plt.subplot(221)
eric_daily_speed.plot(label="Eric")
sanne_daily_speed.plot(label="Sanne")
nico_daily_speed.plot(label="Nico")
plt.xlabel('Date')
plt.ylabel('Speed(m/s)')
plt.legend(loc="upper left")

plt.subplot(222)
eric_daily_altitude.plot(label="Eric")
sanne_daily_altitude.plot(label="Sanne")
nico_daily_altitude.plot(label="Nico")
plt.xlabel('Date')
plt.ylabel('Height(m)')
plt.legend(loc="upper left")
plt.show()














        
        
    