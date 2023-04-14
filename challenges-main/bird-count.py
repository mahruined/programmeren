birds = [{'name':'mus','key':'m','count':0},
          {'name':'duif','key':'d','count':0},
          {'name':'koolmees','key':'k','count':0},
          {'name':'kraai','key':'i','count':0},
          ]


# 1) print all birds with key and name
print('Birds:')
for bird in birds:
    print(f"- {bird['key']}: {bird['name']}")

# 2) define function get_bird_by_key(birds: list, key:str) returns bird or None
def get_bird_by_key(birds:list,key:str):
    for bird in birds:
        if bird['key'] == key:
            return bird
    return None
# 3) repeat until given '.'
while True:
    key = input("Enter bird key (or '.' to exit): ")
    if key == '.':
        break
    bird = get_bird_by_key(birds, key)
    if bird:
        bird['count'] += 1
# 4) print all birds with name and count
for bird in birds:    
    print(f"{bird['name']}: {bird['count']}")
print('\n')

# 5) print per bird also the percentage of the total count
totaal = 0
for bird in birds:
    totaal += bird['count']
for bird in birds:    
    print(f"{bird['name']}: {round(bird['count']/ totaal * 100)}%")