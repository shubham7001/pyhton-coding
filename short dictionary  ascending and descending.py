#Write a Python script to sort (ascending and descending) a dictionary by value.

d = {'apple': 5, 'banana': 2, 'orange': 4, 'kiwi': 1}
ascending_dict = dict(sorted(d.items(), key=lambda item: item[1]))
descending_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
print("Ascending order:", ascending_dict)
print("Descending order:", descending_dict)
