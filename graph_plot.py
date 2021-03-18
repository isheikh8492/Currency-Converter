import urllib.request
import dateutil.relativedelta
import datetime
import urllib.request
import json
import dateutil.relativedelta
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

target_currency = "PKR"
init_currency = "USD"

start_date = datetime.date.today()
end_date = start_date + dateutil.relativedelta.relativedelta(months=-1)

delta = datetime.timedelta(days=1)

y_values = []
while end_date <= start_date:
    with urllib.request.urlopen("http://data.fixer.io/api/" + str(
            end_date) + "?access_key=2179433ad61d935639f9bc75e180bdf0&base=EUR&symbols=USD,PKR") as url:
        json_data = json.loads(url.read().decode())
        y_values.append((float(json_data['rates'][target_currency]) / float(json_data['rates'][init_currency])))
        end_date += delta

start_date = datetime.date.today()
end_date = start_date + dateutil.relativedelta.relativedelta(months=-1)

x_values = []
while end_date <= start_date:
    x_values.append(end_date)
    end_date += delta

ax = plt.gca()

formatter = mdates.DateFormatter("%Y-%m-%d")

ax.xaxis.set_major_formatter(formatter)

locator = mdates.DayLocator()

ax.xaxis.set_major_locator(locator)

x_ticks = np.arange(x_values[len(x_values) - 1], x_values[0], datetime.timedelta(days=-15))
plt.xticks(x_ticks)

plt.plot(x_values, y_values)