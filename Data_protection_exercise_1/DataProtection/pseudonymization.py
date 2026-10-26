from cryptography.fernet import Fernet
"""
TODO:
- Generate a key once and reuse it for both pseudonymization and restoration. In a real system, this key would be securely stored.
"""
key = Fernet.generate_key()
f = Fernet(key)

def pseudonymize_names(names):
    """
    TODO: Encrypt each name with Fernet symmetric encryption.
    - return list of encrypted names
    """
    cryptedNames = []
    print(names)
    for name in names:
        byteName = bytes(name, "utf-8")
        token = f.encrypt(byteName)
        print(token)
        cryptedNames.append(token)
            
    return cryptedNames


def restore_names(encrypted):
    """
    TODO: Decrypt previously pseudonymized names.
    - return list of decrypted names
    """

    decryptedNames = []
    print(encrypted)
    for name in encrypted:
        token = f.decrypt(name)
        decrypt = token.decode("utf-8")
        print(decrypt)
        decryptedNames.append(decrypt)

    print(decryptedNames)
    return decryptedNames