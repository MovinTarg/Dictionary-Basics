me = {}
me['Name'] = 'Pete'
me['Age'] = 29
me ['Country of Birth'] = "USA"
me ["Favorite Langauge"] = 'JavaScript'

def dictionaryInputs (dictionary):
    for key, data in dictionary.iteritems():
        print 'My', key, 'is', data
dictionaryInputs(me)