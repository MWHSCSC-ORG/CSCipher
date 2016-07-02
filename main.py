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
      uniqueChars.push(char)
  return uniqueChars

def caesar(contents):
  localPossibilities = []
  mapping = [dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26))),dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))]
  for shift in range(1,26):
    print("Running shift " + str(shift))
    ceasarOut = ""
    for char in contents():
      if char.isalpha():
        ceasarOut += mapping[1][(mapping[0][char] + shift) % 26]
      else:
        ceasarOut += char
    localPossibilities.push(ceasarOut)
  return localPossibilities

def switchBase(uniqueChars, contents):
  localPossibilities = []
  def int2base(x, base):
    digs = string.digits + string.letters  
    if x < 0: sign = -1
    elif x == 0: return digs[0]
    else: sign = 1
    x *= sign
    digits = []
    while x:
      digits.append(digs[x % base])
      x /= base
    if sign < 0:
      digits.append('-')
    digits.reverse()
    return ''.join(digits)
  def convert(number, original_base, new_base):
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
      localPossibilities.push(binaryForm)
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
  localPossibilities.push(baconOut)
  oppBaconContents = contents.replace(uniqueChars[0],"B").replace(uniqueChars[1],"A")
  oppChunks = [oppBaconContents[i:i+5] for i in range(0, len(oppBaconContents), 5)]
  oppBaconOut = ""
  for oppChunk in oppChunks:
    if oppChunk in baconKey:
      oppBaconOut += j[oppChunk]
  localPossibilities.push(oppBaconOut)
  return localPossbilities

def main(contents):
  possibilities = []
  uniqueChars = findUniqueChars()
  print("A total of " + str(len(uniqueChars)) + " individual characters exist.")
  print("Solving for Ceasar cipher.")
  possibilities.push(ceasar(contents))
  print("Solving for multiple number bases.")
  possibilities.push(switchBase(uniqueChars, contents))
  if len(uniqueChars) is 2:
    print("Solving for Bacon's cipher.")
    possibilities.push(bacon(uniqueChars, contents))
    print("Solving for Morse code.")
    # TODO Morse Code

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
    if path[-3:] is not ".txt":
      print("Must be a text file (.txt)")
      noPath = True
    else:
      print("File does not exist.")
      noPath = True
  try:
    cipherFile = open(path, "r")
    cleanContents = cipherFile.read().replace(" ","").replace("\t","").replace("\n","").replace("\r","")
    rawContents = cipherFile.read()
    cipherFile.close()
  except Exception as e:
    print("Error reading file.")
  i = 0
  for possibility in (main(rawContents) + main(cleanContents)):
    print(str(i) + ":  " + possibility)

# Integrate as you choose, just created this for Caesar Cipher with auto key.
# Not sure how you would like to determine if it is a Caesar and to make this run, I'll leave that to you.
import collections
from string import ascii_lowercase
def caesar():  
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
  
  string = "THE INPUT FROM THE FILE FOR THIS STRING"
  key = str(find_key())
  decrypted = str(caesar_decrypt(find_key(), string.lower()))
  print "Used key: " + key + "\n" + decrypted






# Just call vigenere()
from string import uppercase
from operator import itemgetter
def vigenere():
    def vigenere_decrypt(target_freqs, input):
        nchars = len(uppercase)
        ordA = ord('A')
        sorted_targets = sorted(target_freqs)

        def frequency(input):
            result = [[c, 0.0] for c in uppercase]
            for c in input:
                result[c - ordA][1] += 1
            return result

        def correlation(input):
            result = 0.0
            freq = frequency(input)
            freq.sort(key=itemgetter(1))

            for i, f in enumerate(freq):
                result += f[1] * sorted_targets[i]
            return result

        cleaned = [ord(c) for c in input.upper() if c.isupper()]
        best_len = 0
        best_corr = -100.0

        for i in xrange(2, len(cleaned) // 20):
            pieces = [[] for _ in xrange(i)]
            for j, c in enumerate(cleaned):
                pieces[j % i].append(c)

            corr = -0.5 * i + sum(correlation(p) for p in pieces)

            if corr > best_corr:
                best_len = i
                best_corr = corr

        if best_len == 0:
            return ("Text is too short to analyze", "")

        pieces = [[] for _ in xrange(best_len)]
        for i, c in enumerate(cleaned):
            pieces[i % best_len].append(c)

        freqs = [frequency(p) for p in pieces]

        key = ""
        for fr in freqs:
            fr.sort(key=itemgetter(1), reverse=True)

            m = 0
            max_corr = 0.0
            for j in xrange(nchars):
                corr = 0.0
                c = ordA + j
                for frc in fr:
                    d = (ord(frc[0]) - c + nchars) % nchars
                    corr += frc[1] * target_freqs[d]

                if corr > max_corr:
                    m = j
                    max_corr = corr

            key += chr(m + ordA)

        r = (chr((c - ord(key[i % best_len]) + nchars) % nchars + ordA)
             for i, c in enumerate(cleaned))
        return (key, "".join(r))
    encoded = """
        MOMUD EKAPV TQEFM OEVHP AJMII CDCTI FGYAG JSPXY ALUYM NSMYH
        VUXJE LEPXJ FXGCM JHKDZ RYICU HYPUS PGIGM OIYHF WHTCQ KMLRD
        ITLXZ LJFVQ GHOLW CUHLO MDSOE KTALU VYLNZ RFGBX PHVGA LWQIS
        FGRPH JOOFW GUBYI LAPLA LCAFA AMKLG CETDW VOELJ IKGJB XPHVG
        ALWQC SNWBU BYHCU HKOCE XJEYK BQKVY KIIEH GRLGH XEOLW AWFOJ
        ILOVV RHPKD WIHKN ATUHN VRYAQ DIVHX FHRZV QWMWV LGSHN NLVZS
        JLAKI FHXUF XJLXM TBLQV RXXHR FZXGV LRAJI EXPRV OSMNP KEPDT
        LPRWM JAZPK LQUZA ALGZX GVLKL GJTUI ITDSU REZXJ ERXZS HMPST
        MTEOE PAPJH SMFNB YVQUZ AALGA YDNMP AQOWT UHDBV TSMUE UIMVH
        QGVRW AEFSP EMPVE PKXZY WLKJA GWALT VYYOB YIXOK IHPDS EVLEV
        RVSGB JOGYW FHKBL GLXYA MVKIS KIEHY IMAPX UOISK PVAGN MZHPW
        TTZPV XFCCD TUHJH WLAPF YULTB UXJLN SIJVV YOVDJ SOLXG TGRVO
        SFRII CTMKO JFCQF KTINQ BWVHG TENLH HOGCS PSFPV GJOKM SIFPR
        ZPAAS ATPTZ FTPPD PORRF TAXZP KALQA WMIUD BWNCT LEFKO ZQDLX
        BUXJL ASIMR PNMBF ZCYLV WAPVF QRHZV ZGZEF KBYIO OFXYE VOWGB
        BXVCB XBAWG LQKCM ICRRX MACUO IKHQU AJEGL OIJHH XPVZW JEWBA
        FWAML ZZRXJ EKAHV FASMU LVVUT TGK"""
    english_frequences = [
        0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
        0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
        0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
        0.00978, 0.02360, 0.00150, 0.01974, 0.00074]

    (key, decoded) = vigenere_decrypt(english_frequences, encoded)
    print "Key:", key
    print "\nText:", decoded

