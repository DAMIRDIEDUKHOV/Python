names= {
    'John' : {
        'age' : 13,
        'ages' : 14
    },
    'Elly' : {
        'age' : 12
    }
}

for name in names:
    print(name,":")
    for age, num in names["Elly"].items():
        print("\n-", age, ":", num)