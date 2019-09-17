# Cryptography
A couple of programs I did in my Computer Security class


Caeser Cipher:
A Caesar Cipher is a simple cipher where each letter within some plaintext is replaced by a letter at some fixed offset down the alphabet. For example, if you were to use a Caesar Cipher with an offset of +4, the letter "A" would be replaced with the letter "E" since "E" is +4 positions after "A".
I used a brute force approach to find all the possible offsets by generating all possible plaintexts at each offset and picking the one that makes the most sense.
Overview of the Implementation:
In general, the CrackCaesar program will do the following:
1. Take in two text files as arguments (in order):
(a) A text file containing ciphertext needing to be decrypted
(b) A text file containing common words to check your plaintext against
2. Break the ciphertext using brute force, determining the correct decoded plaintext by checking if decoded words match words in the text file of common words.
3. Print out the determined offset for the Casesar Cipher and the decoded plaintext.


Monoalphabetic Cipher:
A monoalphabetic cipher is where each letter from the original alphabet text is encrypted using some fixed alphabet mapping. This means each letter is replaced by one other letter. In the case of the Caesar Cipher, the fixed alphabet mapping was simply the original alphabet offset by a certain value, but in general the mapping for a monoalphabetic cipher can be completely arbitrary.
To decrypt, I used frequency analysis which is the study of the frequency of letters or sets of letters.
Overview of the Implementation:
The CrackCipher program will do the following: 
1. Take in two arguments (in order)
(a) A text file containing ciphertext needing to be decoded
(b) A fairly long text file containing known text related to the plaintext trying to be recovered
2. Perform frequency analysis on the letters within the known text (including spaces).
3. Perform frequency analysis on the letters within the ciphertext (including spaces).
4. Generate an alphabet mapping to use based on similar letter frequencies (which includes mapping the space character).
5. Print out the decoded plaintext using the determined alphabet key.
