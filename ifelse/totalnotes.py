balance=200000
def recurseCountNotes(balance):
    if balance == 0:
        return 0

    if balance>=500:
        return 1+recurseCountNotes(balance-500)
    elif balance>=200:
        return 1+recurseCountNotes(balance-200)
    elif balance>=100:
        return 1+recurseCountNotes(balance-100)
    elif balance>=50:
        return 1+recurseCountNotes(balance-50)
    elif balance>=20:
        return 1+recurseCountNotes(balance-20)
    elif balance>=10:
        return 1+recurseCountNotes(balance-10)
    elif balance>=5:
        return 1+recurseCountNotes(balance-5)
    elif balance>=2:
        return 1+recurseCountNotes(balance-2)
    elif balance>=1:
        return 1+recurseCountNotes(balance-1)
    
print(recurseCountNotes(balance))