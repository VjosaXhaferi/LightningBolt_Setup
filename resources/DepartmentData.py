import random


class Department:
    randInt = random.randint(0, 1000)  # this will generate a random num from 0-100, adding it to dep. and tem.

    url = "https://s2.usw2.qa.lightning-bolt.com/Setup.aspx?page=departments"
    departmentName = "Ritech Department " + str(randInt)
    templateName = "Ritech Template " + str(randInt)
    templateDescription = "Ritech Description " + str(randInt)
