def get_word(sentence, n):
	words = sentence.split()
	# Only proceed if n is positive 
	if n >= 0:
		# Only proceed if n is not more than the number of words 
		if n <= len(words):
			return(words[n-1])
		else:
			return("Nothing")
	else: 
		    if n <= len(words):
			    return(words[n])
		    else:
			    return("Nothing")
   
print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing

