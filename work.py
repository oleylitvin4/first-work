def unique_in_order(sequence):
    unique_list = []  # List to store the unique elements in order

    # Iterate over the sequence
    for i, item in enumerate(sequence):
        # Check if the current item is the same as the next item
        if i < len(sequence) - 1 and item == sequence[i + 1]:
            continue  # Skip if the item is a duplicate
        unique_list.append(item)  # Add the unique item to the list

    return unique_list
