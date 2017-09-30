from Adafruit_IO import Client
aio = Client('YOUR ADAFRUIT IO KEY')

count = 0
ping_list = []
ping_avg = 0

# Get an array of all data from feed 'ping'
ping_data = aio.data('ping')

# Print out all the results.
for data in ping_data:
    #print('Data value: {0}'.format(data.value))
    ping_list.append(round(float(data.value), 3))

ping_avg = round(sum(ping_list)/len(ping_list), 3)

#print('Average: ', ping_avg)

ping_min = ping_list[0]
ping_max = ping_list[0]

#print('Initial Ping min: ', ping_min)
#print('Initial Ping max: ', ping_max)

for ping in ping_list:
    #print('ping_list value: ', ping)
    if ping < ping_min: 
        ping_min = ping
        #print('new ping_min value: ', ping_min)
    if ping > ping_max: 
        ping_max = ping
        #print('new ping_max value: ', ping_max)
    
#print('Low Ping Min: ', ping_min)
#print('High Ping Max: ', ping_max)


#return the average, min, and max values to adafruit
aio.send('ping_avg', ping_avg)
aio.send('ping_min', ping_min)
aio.send('ping_max', ping_max)
