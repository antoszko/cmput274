count = 0
try:
    while(input() != "exit") :
        count += 1
        print("Count: %d" % count)
        continue
except EOFError :
    print("Hit a number lol")
    exit()
