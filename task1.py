my_text = "абв влодджр внабв вав"
fragment = "абв"
words = my_text.split(" ")
new_text_list = []
for e in words:
    if fragment not in e:
        new_text_list.append(e)
new_text = ''
for x in new_text_list:
    new_text += str(x) + " "
print(new_text)

