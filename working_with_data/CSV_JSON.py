import json

print('JSON file containing reviews about films')

f = open('example_json.json')
movies = json.load(f)
print("Current content: ")
for i in movies.items():
    print(i)

print('\nDo you want to add new review or maybe delete the existing review? Please type "or" lub "delete": ')
decision = input()
if(decision == 'add'):
    print('\nType record name which you want to add: ')
    record_name = input()
    print('Type film title: ')
    title = input()
    print('Type release date: ')
    release_date = input()
    print('Type review: ')
    review = input()
    movies[str(record_name)] = {'title': str(title), 'release date': str(release_date), 'review': str(review)}
elif(decision == 'delete'):
    print('Type record name which you want to delete: ')
    record_name = input()
    movies.pop(str(record_name))
else:
    print("Unknown command")

print("\nContent after modification: ")
for i in movies.items():
    print(i)
with open('example_json.json', 'w') as f:
    json.dump(movies, f)