"""Question 5 The replace_ending function replaces a specified substring at the end of a given sentence 
with a new substring. If the specified substring does not appear at the end of the given sentence,
no action is performed and the original sentence is returned. If there is more than one occurrence
of the specified substring in the sentence, only the substring at the end of the sentence is replaced.
For example, replace_ending("abcabc", "abc", "xyz") should return abcxyz, not xyzxyz or xyzabc. 
The string comparison is case-sensitive, so replace_ending("abcabc", "ABC", "xyz") should return abcabc
(no changes made).  """
def replace_ending(sentence, old, new):
    # Check if the old substring is at the end of the sentence 
    old=old.lower()
    if old in sentence:
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the 
        # end with the new string
        i = sentence[-1:len(old)]
        new_sentence = i +" "+ new
        return new_sentence


    # Return the original sentence if there is no match 
    return sentence
    
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"