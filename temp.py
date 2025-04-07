import pandas as pd

# using dictionary
data = {
    'Name':['Ali','Sara','Ahmed'],
    'Age':[25,30,22],
    'City':['Lahore','Karachi','Islamabad']
}

df = pd.DataFrame(data)

print(df)

print("\n\n We can also use List of lists as follows: ")

# using lists in a list
datalist = [
    ['Ali',25,'Lahore'],
    ['Sara',30,'Karachi'],
    ['Ahmed',22,'Islamabad']
]

frame = pd.DataFrame(data, columns=['Name','Age','City'])

print(df)

#using a list of dictionaries 
print("\n\nWe also have a 3rd way using dictionaries in a list")
list_dic = [
    {
        'Name':'Ali',
        'Age':25,
        'City':'Lahore'
    },
    {
        'Name':'Sara',
        'Age':30,
        'City':'Karachi'
    },
    {
        'Name':'Ahmed',
        'Age':22,
        'City':'Islamabad'
    }
]

d = pd.DataFrame(list_dic)

print(d)



