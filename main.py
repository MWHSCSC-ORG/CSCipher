# TODO for Aaron:
  # If the frequency of the letters is similar to the number of times used in the english language withing a certain threshold, run a transposition cipher.
  # Run an initial test for the frequency of the most used letter. Find the difference with the letter 'E' (aka the find_key() function) Run second and third test to determine if the same key holds for the next most used char. If so, we can determine it is Caesar Ciphered. We can run these tests before exit for if there's multiple ciphers envolved.
  # Possible GUI Interface for final product
  # Calculate the Index of Coincidence to determind if it's a Vigenere Cipher.
# TODO for Thomas:
  # Actually test the program
  # Implement morse code
  # If program is be more intense, try running combinations?
def findUniqueChars(contents):
  uniqueChars = []
  for char in contents:
    if char not in uniqueChars:
      uniqueChars.append(char)
  return uniqueChars

def ceasar(contents):
  localPossibilities = []
  #mapping = [dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26))),dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))]
  #for shift in range(1,26):
  #  print("Running shift " + str(shift))
  #  ceasarOut = ""
  #  for char in contents:
  #    if char.isalpha():
  #      ceasarOut += mapping[1][(mapping[0][char] + shift) % 26]
  #    else:
  #      ceasarOut += char
  #  localPossibilities.append(ceasarOut)
  return localPossibilities

def switchBase(uniqueChars, contents):
  localPossibilities = []
  def int2base(x, base):
    digs = string.digits + string.ascii_letters  
    if x < 0: sign = -1
    elif x == 0: return digs[0]
    else: sign = 1
    x *= sign
    digits = []
    while x:
      digits.append(digs[int(x % base)])
      x /= base
    if sign < 0:
      digits.append('-')
    digits.reverse()
    return ''.join(digits)
  def convert(number, original_base, new_base):
    precision = None
    integral, point, fractional = number.strip().partition('.')
    num = -1
    try:
        num = int(integral + fractional, original_base) * original_base ** -len(fractional)
    except ValueError as e:
        pass
    precision = len(fractional) if precision is None else precision
    return int2base(int(round(num / new_base ** -precision)), new_base)
  for base in range(3,64):
    binaryForm = convert(contents,len(uniqueChars),2)
    if binaryForm is not -1:
      localPossibilities.append(binaryForm)
  return localPossibilities

def bacon(uniqueChars, contents):
  localPossibilities = []
  baconContents = contents.replace(uniqueChars[0],"A").replace(uniqueChars[1],"B")
  chunks = [baconContents[i:i+5] for i in range(0, len(baconContents), 5)]
  baconKey = {"AAAAA":"a","AAAAB":"b","AAABA":"c","AAABB":"d","AABAA":"e","AABAB":"f","AABBA":"g","AABBB":"h","ABAAA":"i","ABAAB":"j","ABAAB":"k","ABABA":"l","ABABB":"m","ABBAA":"n","ABBAB":"o","ABBBA":"p","ABBBB":"q","BAAAA":"r","BAAAB":"s","BAABA":"t","BAABB":"u","BAABB":"v","BABAA":"w","BABAB":"x","BABBA":"y","BABBB":"z"}
  baconOut = ""
  for chunk in chunks:
    if chunk in baconKey:
      baconOut += baconKey[chunk]
  localPossibilities.append(baconOut)
  oppBaconContents = contents.replace(uniqueChars[0],"B").replace(uniqueChars[1],"A")
  oppChunks = [oppBaconContents[i:i+5] for i in range(0, len(oppBaconContents), 5)]
  oppBaconOut = ""
  for oppChunk in oppChunks:
    if oppChunk in baconKey:
      oppBaconOut += j[oppChunk]
  localPossibilities.append(oppBaconOut)
  return localPossbilities

def main(contents):
  possibilities = []
  uniqueChars = findUniqueChars(contents)
  print("A total of " + str(len(uniqueChars)) + " individual characters exist.")
  print("Solving for Ceasar cipher.")
  possibilities.append(ceasar(contents))
  print("Solving for multiple number bases.")
  possibilities.append(switchBase(uniqueChars, contents))
  if len(uniqueChars) is 2:
    print("Solving for Bacon's cipher.")
    possibilities.append(bacon(uniqueChars, contents))
    print("Solving for Morse code.")
    # TODO Morse Code
  return possibilities

if __name__ == "__main__":
  print("Starting application...")
  import os, binascii, string
  noPath = True
  while noPath:
    path = input("Enter the file path of the ciphertext: ")
    print("Checking files...")
    if os.path.exists(path):
      print("File exists.")
      noPath = False
    else:
      print("File does not exist.")
      noPath = True
  try:
    cipherFile = open(path, "r")
    rawContents = cipherFile.read()
    print("Raw contents: " + rawContents)
    cleanContents = rawContents.replace(" ","").replace("\t","").replace("\n","").replace("\r","")
    print("Clean contents: " + cleanContents)
    cipherFile.close()
  except Exception as e:
    print("Error reading file.")
  i = 0
  for possibility in main(rawContents):
    print(possibility)
