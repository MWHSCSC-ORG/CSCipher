def main():
  print("Starting application...")
  import os
  a = True
  while a:
    b = input("Enter the file path of the ciphertext: ")
    print("Checking files...")
    if os.path.exists(b):
      print("File exists.")
      a = False
    if b[-3:] is ".txt":
      print("Must be a text file (.txt)")
      a = False
    else:
      print("File does not exist.")
      a = True
  try:
    c = open(b, "r")
    d = c.read()
    c.close()
  except Exception as e:
    print("Error reading file.")
  # Bacon Cipher
  e = []
  for f in d.replace(" ","").replace("\t","").replace("\n","").replace("\r",""):
    if f not in e:
      e.push(f)
  print("A total of " + str(len(e)) + " individual characters exist.")
  if len(e) is 2:
    #binary, bacon, morse
    g = d.replace(e[0],"0").replace(e[1],"1")
    h = d.replace(e[0],"1").replace(e[1],"0")
    
if __name__ == "__main__":
  main()
