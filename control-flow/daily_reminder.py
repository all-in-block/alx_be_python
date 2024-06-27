task =input("enter a task description ")
priority = input("enter the task’s priority (high, medium, low) ")
time_bound = input("is the task time bound (yes or no)? ")
match priority:
    case "high":
        if time_bound == "yes":
            print("reminder: ", task,"is a ",priority,"priority task that requires immediate attention today!")
        else:
            print("reminder: ", task,"is a ",priority, "priority")
    case "medium":
        if time_bound == "yes":
            print("reminder: ", task,"is a ",priority,"priority task that requires immediate attention today!")
        else:
            print("reminder: ", task,"is a ",priority, "priority")
    case "low":
        if time_bound == "yes":
            print("reminder: ", task,"is a ",priority,"priority task that requires immediate attention today!")
        else:
            print("reminder: ", task,"is a ",priority, "priority")
    case _:
        print("enter a valid priority")