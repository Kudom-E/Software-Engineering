from collections import Counter


# compression function
def compression(input_string):
    compressed_text = ""  # input_string to hold compressed
    recursion_count = 1  # value holding consecutive recursions

    for i in range(len(input_string) - 1):  # using size of input -1
        if input_string[i] == input_string[i + 1]:
            recursion_count += 1  # if next input is equal to first, add 1
            if i == (len(input_string) - 2):  # last but one character's position
                if recursion_count != 1:
                    compressed_text += str(recursion_count) + input_string[i]  # frequency and character and put
                    # together
                else:  # 1 is not added to compressed finishing as a frequency
                    compressed_text += input_string[i]
                if input_string[i] != input_string[i + 1]:  # If last two characters are not equal
                    if recursion_count != 1:
                        compressed_text += str(recursion_count) + input_string[i]
                    else:
                        compressed_text += input_string[i]
                    recursion_count = 1
                    compressed_text += input_string[i + 1]
        else:  # if held character is not equal to the next
            if recursion_count != 1:
                compressed_text += str(recursion_count) + input_string[i]
            else:
                compressed_text += input_string[i]
            recursion_count = 1
           if i == (len(input_string) - 2):
                if recursion_count != 1:
                    compressed_text += str(recursion_count) + input_string[i + 1]
                else:
                    compressed_text += input_string[i + 1]
    return compressed_text


def optimization(input_string, chars_left, compression):
    temp = input_string  # temporary variable to store input
    sub = 0
    for i in range(len(input_string) - 1):  # i is the size of the input-1
        temp = temp[0:i:] + temp[i + remove_amount::]  # taking amount allowed to remove for optimum compression for 
        # every iteration 
        choice_len = len(compression(temp))  # holds number of characters in newly compressed
        if (chars_left - choice_len) > sub:
            sub = chars_left - choice_len  # hold the size of the smallest compressed so far
            choice = compression(temp)  # take smallest compressed comparing the difference in sizes against the initial compress
            chosen_length = chars_left - sub
        i += remove_amount  # increase iterator by amount allowed before removing
        temp = input_string  # reset temporary to store input
    print("With an improved size of ", chosen_length, " characters")
    return choice


if __name__ == "__main__":
    input_string = input("enter string:\n").upper()  # force all input to be capital to remove confusion
    remove_amount = int(input("enter value to remove for optimization: "))  # take an integer input for number of characters to be removed 
    # for optimization 

print("\ninput has ", len(input_string), " characters")
print("After first compression:", compression(input_string))
chars_left = len(compression(input_string))
print("Now has ", chars_left, " characters\n")

# Each character actual frequency
count_rec = Counter(input_string)  # count the frequency of every character
print("actual frequency:\n", count_rec, "\n")
print("After optimizing the compression:")
print(optimization(input_string, chars_left, compression))
