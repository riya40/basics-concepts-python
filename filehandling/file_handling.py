f = open("demofile.txt", "r")

with open('demofile.txt', 'wt') as f:
    f.write('hi there, this is filehandling concept.\n')
    f.write('hello priya.\n')

with open("demofile.txt",'r') as f:
    content = f.read();
    print(content)
