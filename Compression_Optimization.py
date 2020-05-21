# Compression Optimization in main function
def compression(s):      #support function which will be called in main function
    s = s.upper()  # force all input to be capital to remove confusion
    s = s.replace(" ", "")  # remove spaces if any to prevent space being taken as a character

    compressed_text = ""  # s to hold compressed
    recursion_count = 1  # value holding consecutive recursions

    for i in range(len(s) - 1):  # using size of input -1
        if s[i] == s[i + 1]:
            recursion_count += 1  # if next input is equal to first, add 1
            if i == (len(s) - 2):  # last but one character's position
                if recursion_count != 1:
                    compressed_text += str(recursion_count) + s[i]  # frequency and character and put together
                else:  # 1 is not added to compressed finishing as a frequency
                    compressed_text += s[i]
                if s[i] != s[i + 1]:  # If last two characters are not equal
                    if recursion_count != 1:
                        compressed_text += str(recursion_count) + s[i]
                    else:
                        compressed_text += s[i]
                    recursion_count = 1
                    compressed_text += s[i + 1]
        else:  # if held character is not equal to the next
            if recursion_count != 1:
                compressed_text += str(recursion_count) + s[i]
            else:
                compressed_text += s[i]
            recursion_count = 1
            if i == (len(s) - 2):
                if recursion_count != 1:
                    compressed_text += str(recursion_count) + s[i + 1]
                else:
                    compressed_text += s[i]
    return compressed_text


def optimization(s, k):      #main function to be run
    s = s.upper()  # force all input to be capital to remove confusion
    s = s.replace(" ", "")  # remove spaces if any to prevent space being taken as a character
    k= int(k)
    temp = s  # temporary variable to store input
    print("initial: ", s)
    print("intial compress: ", compression(s))
    print("intial compress sized at ", len(compression(s)), " characters")
    sub = 0
    for i in range(len(s) - 2):  # i is the size of the input-1
        temp = temp[0:i:] + temp[i + k::]  # taking amount allowed to remove for optimum compression for
        # every iteration
        chars_left = len(compression(s))
        choice_len = len(compression(temp))  # holds number of characters in newly compressed
        pre_sub = chars_left - choice_len

        if pre_sub > sub:
            sub = pre_sub  # hold the size of the smallest compressed so far
            choice = compression(temp)  # take smallest compressed comparing the difference in sizes against the
            # initial compress
            chosen_length = chars_left - sub
        i += k  # increase iterator by amount allowed before removing
        temp = s  # reset temporary to store input
    print("best 3 removed gives ", chosen_length, " characters")
    return choice