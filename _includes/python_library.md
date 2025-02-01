A Python library is a collection of programs that do a specific task, and can be called in your program by their name. Libraries make it easy to do things that would've otherwise needed you to write out, manually, the several lines of code needed to do that thing. For example, assume you need to count the number of words in a sentence. The manual (non-library) way of doing so would be to write something like this:

```
sentence = 'Beside the lake, beneath the trees, fluttering and dancing'
word_counts = {}
words = sentence.split()  # Split the sentence into words
for word in words:
    word = word.lower().strip(".,!?")  # Remove punctuation
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
print('This sentence contains`, word_counts, 'words.')
```

Now, imagine doing the same thing with a library called `collections`, which contains code to do the heavy lifting. If you were to use this library, your code would look something like this, where you use a class called `Counter` to do the counting:

```
from collections import Counter

# Count word occurrences using a library
sentence = 'There was a time when meadow, grove, and stream, and every common sight to me did seem apparelled in celestial light.'
words = sentence.lower().split()
normalized_words = [word.strip(".,!?") for word in words]
word_counts = Counter(normalized_words)

print('This sentence contains`, word_counts, 'words.')
```

With libraries, you can write your programs with fewer lines of code, while using universal methods that can be recognised by any other Python programmer more easily than if they had to read non-library code.