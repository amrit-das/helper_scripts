import itertools
text = "aforapple"

text_list = list(text)
new_text = [k for k,g in itertools.groupby(text_list)]
print("".join(new_text)
