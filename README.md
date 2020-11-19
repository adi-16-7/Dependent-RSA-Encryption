# Dependent-RSA-Encryption Algorithm
There are multiple variations of RSA in literature. One such variation is the Dependent RSA.

The steps in a Dependent RSA Algorithm are:
a. The key generation process is exactly as in the original RSA.
b. Choose a random integer k in the residue class of Zn*
c. Encryption: to obtain ciphertexts C1 C2 given a message M
  i. C1 = (K + 1)^e (mod n)
  ii. C2 = m[K^e (mod n)]
d. Decryption: to get the message
  i. K = {C1^d (mod n)} – 1
  ii. m = [K^e (mod n)]/C2
  
 
 
