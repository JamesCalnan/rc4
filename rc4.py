s = [0] * 256

def swap(arr, i, j):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp

def convertToBinary(st):
  
  key = ' '.join(format(ord(x), 'b') for x in st)
  keyArr = key.split(" ")

  return formatBinary(keyArr)

def formatBinary(arr):
  returnlist = [0] * len(arr)
  j = 0
  for value in arr:
    tempByte = value
    bytesNeeded = 8 - len(tempByte)
    finalByte = ''
    for i in range(bytesNeeded):
      finalByte += "0"
    finalByte += tempByte
    returnlist[j] = finalByte
    j += 1
  
  finalString = "".join(returnlist)

  return finalString
  

va = input("Plaintext: ")
key = input("Key: ")

for i in range(0,256):
  s[i] = i

#print(s)

j = 0

#key = "Wiki" #convertToBinary("pwd12")

keylength = len(key)

for i in range(0, 256):
  j = (j + s[i] + int(ord(key[i % keylength]))) % 256

  swap(s, i, j)



result = ""
j = 0
for i in range(len(va)):
  i = (i + 1) % 256
  j = (j + s[i]) % 256
  swap(s, i, j)

  k = s[(s[i] + s[j]) % 256]
  
  letter = va[i - 1]
  
  bitwise = ord(letter) ^ k
  
  outLetter = chr(bitwise)
  
  hexNum = hex(ord(outLetter))[2:]
  hexString = str(hexNum).upper() + " "
  result += hexString 

print(f"ciphertext: {result}")
#print(result == "6CA86FE3CBC33C162595C3E78B9C97BC")

#https://sites.math.washington.edu/~nichifor/310_2008_Spring/Pres_RC4%20Encryption.pdf
#https://en.wikipedia.org/wiki/RC4