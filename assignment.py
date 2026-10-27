
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
    file=open(filename,'r')
    for line in file:
        lines=line.strip().split(",")
        if len(lines)==2:
          stname,score=lines
          if stname==name:
            return int(score)
    file.close()        
    pass

# Exercise 5
def update_score(filename, name, new_score):
    file=open(filename,'r')
    lines=file.readlines()
    file.close()
    found=False
    new_line=[]
    for line in lines:
        parts=line.strip().split(",")
        if len(parts)==2:
          names,score=parts
          if names==name:
            new_line.append(f"{name},{new_score}\n")
            found=True
          else:
            new_line.append(line.strip()+"\n")
      else:
        new_line.append(line)
    if found==True:
      file=open(filename,'w')
      for line in new_line:
        file.write(line)
      file.close()
      return True
    else:
      return False

  
    pass
