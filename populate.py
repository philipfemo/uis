count = 0
# Set X to the amount of timeslots needed
x = 18
#Set d to to monday ("mon") or thursday ("thu")
d = "mon"

while count < x:
    time = input("Enter a time: ")
    #Will ask you to enter start time for your timeslot
    day = d
    SlotField.objects.create(start_time = time, day = day)
    count = count + 1
