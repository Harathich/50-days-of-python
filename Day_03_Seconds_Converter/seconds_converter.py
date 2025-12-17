num_of_sec = int(input("Enter the seconds: "))
hours = num_of_sec//3600
rem_sec = num_of_sec%3600
mins = rem_sec//60
final_sec = rem_sec%60
if hours==0 and mins ==0:
    print(final_sec,'seconds')
elif hours==0:
    print(mins,'minutes',final_sec,'seconds')
else:
    print(hours, 'hours', mins, 'minutes', final_sec, 'seconds')
