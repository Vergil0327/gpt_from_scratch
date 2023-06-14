# read it in to inspect it
with open('tiny_shakespeare.dataset.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    print("length of dataset in characters: ", len(text)) # output: length of dataset in characters:  1115393

    # first 1000 characters
    print(text[:1000])

    # here are all the unique characters that occur in this text
    chars = sorted(list(set(text)))
    vocab_size = len(chars)
    print(''.join(chars)) # ' !$&',-.3:;?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
    print(vocab_size) # 65
    