import pyjokes

total_jokes = int(input("Number of jokes: "))

num_jokes = 1

while num_jokes <= total_jokes:
    print(f"{num_jokes} {pyjokes.get_joke()}")
    num_jokes += 1
