from datetime import date
import boto3
import matplotlib.pyplot as plt

client = boto3.client('ce')

today = date.today().strftime('%Y-%m-%d')
start_of_month = f"{date.today().strftime('%Y-%m')}-01"

resp = client.get_cost_and_usage(
    TimePeriod={
        'Start': start_of_month,
        'End': today
    },
    Granularity='DAILY',
    Metrics=['AmortizedCost']
)

plt.title('AWS Costs')

plt.xlabel('Day of Month')
days = range(1, date.today().day)

plt.ylabel('Cost in USD')
costs = [float(cost['Total']['AmortizedCost']['Amount']) for cost in resp['ResultsByTime']]

plt.plot(days, costs)
plt.show()
