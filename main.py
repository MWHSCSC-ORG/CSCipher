def main(d):
  e = []
  for f in d.replace(" ","").replace("\t","").replace("\n","").replace("\r",""):
    if f not in e:
      e.push(f)
  print("A total of " + str(len(e)) + " individual characters exist.")
  g = []
  if len(e) is 2:
    print("Solving for binary encoding.")
    #TODO fix
    #g.push(int("0b" + d.replace(e[0],"0").replace(e[1],"1",2)).to_bytes((n.bit_length() + 7) // 8, 'big').decode())
    #g.push((int("0b" + d.replace(e[0],"1").replace(e[1],"0",2)))
    print("Solving for Bacon's cipher.")
    h = d.replace(e[0],"A").replace(e[1],"B")
    i = [h[i:i+5] for i in range(0, len(h), 5)]
    # TODO programmatically
    j = {"AAAAA":"a","AAAAB":"b","AAABA":"c","AAABB":"d","AABAA":"e","AABAB":"f","AABBA":"g","AABBB":"h","ABAAA":"i","ABAAB":"j","ABAAB":"k","ABABA":"l","ABABB":"m","ABBAA":"n","ABBAB":"o","ABBBA":"p","ABBBB":"q","BAAAA":"r","BAAAB":"s","BAABA":"t","BAABB":"u","BAABB":"v","BABAA":"w","BABAB":"x","BABBA":"y","BABBB":"z"}
    k = ""
    for l in i:
      if l in j:
        k += j[l]
    g.push(k)
    m = d.replace(e[0],"B").replace(e[1],"A")
    n = [h[i:i+5] for i in range(0, len(h), 5)]
    o = ""
    for p in n:
      if p in j:
        o += j[p]
    g.push(o)
    print("Solving for Morse code.")
    
if __name__ == "__main__":
  print("Starting application...")
  import os, binascii
  a = True
  while a:
    b = input("Enter the file path of the ciphertext: ")
    print("Checking files...")
    if os.path.exists(b):
      print("File exists.")
      a = False
    if b[-3:] is not ".txt":
      print("Must be a text file (.txt)")
      a = False
    else:
      print("File does not exist.")
      a = True
  try:
    c = open(b, "r")
    d = c.read().replace(" ","").replace("\t","").replace("\n","").replace("\r","")
    c.close()
  except Exception as e:
    print("Error reading file.")
  main(d)
  
# Integrate as you choose, just created this for Caesar Cipher with auto key.
# Not sure how you would like to determine if it is a Caesar and to make this run, I'll leave that to you.
import collections
from string import ascii_lowercase

def find_key():
    number = len(string)
    array = []

    dict = collections.defaultdict(int)
    for character in string:
        dict[character] += 1

    for character in ascii_lowercase:
        array.append((dict[character]/float(number)))

    num = array.index(max(array))
    key = (((num - 5) % 26) + 1)
    return key

def caesar_decrypt(n, ciphertext):
    key = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result

string = "a"
key = str(find_key())
decrypted = str(caesar_decrypt(find_key(), string.lower()))
print "Used key: " + key + "\n" + decrypted

