import hashlib

def encrypt(data):
    return str(hashlib.sha256(data).hexdigest())

def auth(secret, digest):
    return encrypt(secret) == digest