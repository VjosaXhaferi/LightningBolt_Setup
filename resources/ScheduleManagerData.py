import random


class ScheduleManagerData:
    randInt = random.randint(0, 1000)  # this will generate a random num from 0-100, adding it to dep. and tem.

    url = "https://s2.usw2.qa.lightning-bolt.com/Console.aspx"
    SearchDepartment = "Telmediq"
    ScheduleName = "Ritech Schedule " + str(randInt)
    Template = "Telmediq Template"
