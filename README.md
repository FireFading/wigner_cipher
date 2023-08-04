## About Wigner Cipher
The Wigner Cipher, also known as the Autokey Cipher, is a classical polyalphabetic substitution cipher used for encrypting and decrypting text. It belongs to the family of substitution ciphers, where each letter in the plaintext is replaced by another letter based on a secret key.

## How it works
The Wigner Cipher operates by shifting the letters of the plaintext based on the letters of a secret key. Unlike other polyalphabetic ciphers, such as the Vigenère Cipher, the Wigner Cipher uses the original plaintext itself as part of the key during encryption. This characteristic makes the cipher unique and relatively stronger compared to traditional Vigenère Cipher.

The encryption process involves the following steps:

- Convert the plaintext and the secret key to uppercase (or lowercase) and remove any non-alphabetic characters from both.
- Encrypt each letter in the plaintext by adding the numerical value of the corresponding letter in the key. If the resulting value exceeds the length of the alphabet, it wraps around.
- Append the encrypted letter to the ciphertext and update the key with the newly encrypted letter.

The decryption process is similar to encryption but instead uses the ciphertext and the secret key to recover the original plaintext.

## Usage
The Wigner Cipher is a simple encryption technique and can be used for educational purposes to understand basic encryption principles. However, it should not be considered secure for real-world applications. Modern cryptographic algorithms provide much higher levels of security.

## Example
To encrypt a message with the Wigner Cipher, a user needs to choose a secret key and then apply the encryption process on the plaintext. Similarly, decryption requires the original secret key used for encryption.

- by default is encrypt
- secret key you can pass by adding into `.env` file or pass as argument

```bash
    usage: main.py [-h] [-d] [-k KEY] [-l {russian,english}] [-s]

    Encrypt and Decrypt

    options:
    -h, --help            show this help message and exit
    -d, --decrypt         Decrypt encrypted text
    -k KEY, --key KEY     Key to encrypt/decrypt
    -l {russian,english}, --language {russian,english}
                            Language to encrypt/decrypt
    -s, --save            Save result to file
```

## Note
The Wigner Cipher, while an interesting historical cipher, is not secure against modern cryptographic attacks. It is susceptible to frequency analysis and other classical methods of breaking substitution ciphers. For secure communication, it is advised to use modern encryption algorithms such as AES, RSA, or elliptic curve cryptography.