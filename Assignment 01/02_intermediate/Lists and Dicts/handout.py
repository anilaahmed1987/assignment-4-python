def main():
    # Create a list called fruit_list with the specified fruits
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Print the list to verify its contents
    print("Fruit list:", fruit_list)
    
    # Example operations you might perform:
    # 1. Access the first fruit (index 0)
    print("\nFirst fruit:", fruit_list[0])
    
    # 2. Add a new fruit to the end
    fruit_list.append('mango')
    print("After adding mango:", fruit_list)
    
    # 3. Remove 'grape' from the list
    fruit_list.remove('grape')
    print("After removing grape:", fruit_list)
    
    # 4. Check if 'banana' is in the list
    if 'banana' in fruit_list:
        print("\nYes, banana is in the fruit list!")
    else:
        print("No banana found!")

if __name__ == "__main__":
    main()