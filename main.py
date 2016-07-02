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

