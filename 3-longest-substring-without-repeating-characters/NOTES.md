**Sliding window**
increment window as long as there isn't a repeating character already in the window
if there is
replace character if repeating character in window is the first index of window
remove all elements up to the index of repeating character in window and make that the new window
after every iteration, update maximum length of window and return length when finished