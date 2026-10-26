
# Exercise 1
def read_line(filename, line_number):
    if line_number<=0:
        return ""
    f=""
    file=open(filename,'r')
    for i in range(line_number):
        f=file.readline()
    file.close()
    if f=="":
        return ""
    return f.strip("\n")
    pass

# Exercise 2
def reverse_lines(source, destination):
    c=0
    file=open(source,'r')
    line=file.readlines()
    file.close()
    reversed_lines=line[::-1]
    file=open(destination,'w')
    for line in reversed_lines:
        file.write(line.strip()+"\n")
        c+=1
    file.close()
    return c

# Exercise 3
def merge_files(first, second, destination):
    c=0
    file=open(first,'r')
    line1=file.readlines()
    file.close()

    file=open(second,'r')
    line2=file.readlines()
    file.close()

    file=open(destination,'w')
    for line in line1:
        file.write(line.strip()+"\n")
        c=c+1
    for line in line2:
        file.write(line.strip()+"\n")
        c=c+1
    file.close()
    return c
    pass

# Exercise 4
def find_score(filename, name):
    # Write your code here
    pass

# Exercise 5
def update_score(filename, name, new_score):
    # Write your code here
    pass
