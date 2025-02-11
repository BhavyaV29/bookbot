book_path="books/frankenstein.txt"
def read_contents():
    with open(book_path) as f:
        file_contents=f.read()
    return file_contents

def main():
    file_contents=read_contents()
    file_contents_words=file_contents.split()
    no_of_words=len(file_contents_words)
    return no_of_words
def dictionary_contents():
    file_contents=read_contents()
    dictionary={}
    for character in file_contents:
        character=character.lower()
        if character not in dictionary:
            dictionary[character]=1
        else:
            dictionary[character]+=1
    return dictionary
def report():
    no_of_words=main()
    print(f"--- Begin report of {book_path} --- \n")
    print(f"{no_of_words} words found in the document")
    dictionary=dictionary_contents()
    print("\n \n")
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for letter in alphabet:
        for character in dictionary:
            if character == letter:
                print(f"The '{character}' character was found {dictionary[character]} times")

    
    print("\n --- End report---")
    
report()