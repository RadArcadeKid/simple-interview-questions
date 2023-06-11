# this function returns the length of the longest substring (without repeating characters) using the slidng window algorithm
# Jackie Henson

def lengthOfLongestSubstring(self, s):
    output, l, r = 0, 0, 0              # Initialize variables for the outputw, left and right pointers
    slength = len(s)             
    map = [-1] * 256  # Create a map to store the last occurrence index of each character (ASCII range)

    while r < slength:                          # Loop through the string using the right pointer 
        if map[ord(s[r])] != -1:                # If the character at index r has been seen before
            l = max(map[ord(s[r])] + 1, l)      # Move the left pointer to the next position after the last occurrence of the character

        map[ord(s[r])] = r                      # Update the last occurrence index of the character
        output = max(output, r - l + 1)         # Calculate the length of the current substring and update the maximum length if necessary
        r += 1                                  # Move the right pointer to the next position, most optimal 

    return output  # Return the length of the longest substring without repeating characters


# this code is an example of the sliding window algorithm, in which the time complexity is O(n)
# since the "window" pointer moves once through the string in linear time