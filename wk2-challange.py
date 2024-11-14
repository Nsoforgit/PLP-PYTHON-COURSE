def get_integer_list():
    numbers = input("Enter integers separated by spaces: ").split()
    return [int(num) for num in numbers]

def sum_integers():
    numbers = get_integer_list()
    total = sum(numbers)
    print(f"Sum of integers: {total}")

def print_favorite_books():
    books = ("1984", "The Hobbit", "Dune", "Foundation", "Neuromancer")
    print("\nFavorite Books:")
    for book in books:
        print(book)

def create_person_dict():
    person = {}
    person["name"] = input("\nEnter name: ")
    person["age"] = int(input("Enter age: "))
    person["favorite_color"] = input("Enter favorite color: ")
    print("\nPerson Information:")
    print(person)

def find_common_integers():
    print("\nFirst set of integers:")
    set1 = set(get_integer_list())
    print("Second set of integers:")
    set2 = set(get_integer_list())
    
    common = set1.intersection(set2)
    print(f"Common elements: {common}")

def odd_length_words():
    words = input("\nEnter words separated by spaces: ").split()
    odd_words = [word for word in words if len(word) % 2 != 0]
    print(f"Words with odd number of characters: {odd_words}")

def main():
    print("1. Sum of integers")
    sum_integers()
    
    print("\n2. Favorite books")
    print_favorite_books()
    
    print("\n3. Person dictionary")
    create_person_dict()
    
    print("\n4. Common integers")
    find_common_integers()
    
    print("\n5. Odd length words")
    odd_length_words()

if __name__ == "__main__":
    main()