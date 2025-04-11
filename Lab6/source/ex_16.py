def format_justified(words, width = 30):
    lines = []
    line = []
    curr_len = 0
    for word in words:
        if curr_len + len(word) + len(line) > width:
            if len(line) == 1:
                lines.append(line[0].ljust(width))
            else:
                spaces = width - curr_len
                gap = spaces // (len(line) - 1)
                extra_spaces = spaces % (len(line) - 1)
                formatted = ""
                for i in range(len(line) - 1):
                    formatted += line[i] + ' ' * (gap + (1 if i < extra_spaces else 0))
                formatted += line[-1]
                lines.append(formatted)
            line = []
            curr_len = 0
        line += word
        curr_len += len(word)
    return lines

test_text = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin pretium neque vel erat faucibus dignissim."
              " Phasellus mollis dapibus turpis ut elementum. Vestibulum sed faucibus tellus, faucibus bibendum massa."
              " Interdum et malesuada fames ac ante ipsum primis in faucibus. Ut elit lorem, porttitor vitae ex in,"
              " dignissim laoreet magna. In non aliquam tellus, in elementum sapien. Etiam quis lobortis metus,"
              " at bibendum lacus. Vivamus feugiat consequat elementum. Integer id pellentesque mi.")

test_words = test_text.split()

print(f"Working with: {test_words}")
print(f"Result: {format_justified(test_words, 40)}")