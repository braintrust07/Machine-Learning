def count(input_string):
    vowels_set = set("aeiouAEIOU")  #initializing set of vowels
    vowels_count = 0  
    consonants_count = 0  

    for char in input_string:  #iterate through each character in the string
        if char.isalpha():  #check if character is alphabet
            if char in vowels_set:  #check if character is in vowels set
                vowels_count += 1  
            else:
                consonants_count += 1  


    return vowels_count, consonants_count

def main():
    string = input("Enter a string: ")
    vowels,consonants = count(string)
    print("Number of Vowels = ",vowels,"\nNumber of Consonants = ",consonants)

if __name__ == "__main__":
    main()