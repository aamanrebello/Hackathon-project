import matplotlib.pyplot as plt
import boto3

bucket_name = "aamanrebellohack"
s3_file_path = "readings.txt"
save_as = "data.txt"

# Downloads readings.txt from s3 bucket.
try:
    s3 = boto3.client('s3')
    s3.download_file(bucket_name , s3_file_path, save_as)
except:
    print('Unable to find file: ' + s3_file_path)

f = open("data.txt", "r")
lines = f.readlines()
f.close()
# For each array, index 0: appliance unused but on, index 1: appliance used, index 2: appliance off.
light_sizes = [0, 0, 0]
heater_sizes = [0, 0, 0]
ac_sizes = [0, 0, 0]
# Perform analyses to find how much time each appliance was used, unused or off.
for line in lines:
    # Indicates nobody is in the room if line[0] == 0
    if line[0] == "0":
        # Light is on
        if line[2] == "1":
            light_sizes[0] = light_sizes[0] + 1
        # Light is off
        else:
            light_sizes[2] = light_sizes[2] + 1
        # Heater is on
        if line[4] == "1":
            heater_sizes[0] = heater_sizes[0] + 1
        # Heater is off
        else:
            heater_sizes[2] = heater_sizes[2] + 1
        # AC is on
        if line[6] == "1":
            ac_sizes[0] = ac_sizes[0] + 1
        # AC is off
        else:
            ac_sizes[2] = ac_sizes[2] + 1
    # Somebody is in the room
    else:
        if line[2] == "1":
            light_sizes[1] = light_sizes[1] + 1
        else:
            light_sizes[2] = light_sizes[2] + 1

        if line[4] == "1":
            heater_sizes[1] = heater_sizes[1] + 1
        else:
            heater_sizes[2] = heater_sizes[2] + 1

        if line[6] == "1":
            ac_sizes[1] = ac_sizes[1] + 1
        else:
            ac_sizes[2] = ac_sizes[2] + 1



light_labels = ['Light Unused', 'Light Used', 'Lights off']
heater_labels = ['Heater Unused', 'Heater Used', 'Heater off']
ac_labels = ['AC Unused', 'AC Used', 'AC off']

colors = ['lightcoral', 'gold', 'yellowgreen']

# Generate plots as pngs

plt.pie(light_sizes, colors=colors, shadow=True, autopct='%1.1f%%', startangle=140)
plt.legend(light_labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.savefig('static/lightusage.png')
plt.clf()

plt.pie(heater_sizes, colors=colors, shadow=True, autopct='%1.1f%%', startangle=140)
plt.legend(heater_labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.savefig('static/heaterusage.png')
plt.clf()

plt.pie(ac_sizes, colors=colors, shadow=True, autopct='%1.1f%%', startangle=140)
plt.legend(ac_labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.savefig('static/acusage.png')
plt.close()
