def count_common_elements(list_1, list_1):  # convert lists to sets to remove duplicates
    set_1 = set(list_1)
    set_2 = set(list_2)

    common_elements = set_1.intersection(set_2)  # find common elements using set intersection

    return len(common_elements)


def main():
    list_1 = eval(input("Enter first list: "))
    list_2 = eval(input("Enter second list: "))

    common_count = count_common_elements(list_1, list_2)

    print("Number of common elements =", common_count)


if __name__ == "__main__":
    main()
