# Walkthrough everything!

## About the challenge

This is a CTF challenge that uses LSB steganography and web exploitation. The challenge consists of hiding a link in the photo given. The LSBs of pixels of the photo were modified ot store the link. The link directs us to the web page which id to be exploited to the flag. The flag is of the format `flag{...}`.

## Solution

To solve the CTF, we first need to decode the `.png` file given to us.
