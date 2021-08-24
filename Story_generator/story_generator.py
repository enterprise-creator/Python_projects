import random

when = ['10 years ago' , 'Last week' , 'Yesterday' , 'Two weeks a go']
who = ['a man' , 'a dog' , 'a girl', 'a raccoon' , 'a panda' ]
name = ['Stevie', 'Rafa' , 'Jane', 'Abdul', 'Raj', 'Jane','Rhonda']
residence = ['Portland' , 'Toronto' , 'NYC' , 'Berlin']
went = ['Paris' , 'Delhi' , 'Sydney', 'Louisiana']
happened = ['ate pie' , 'went to a party' , 'went hiking', 'went shopping']

print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to ' + random.choice(went)+' and '+random.choice(happened))