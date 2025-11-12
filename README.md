# Windows 11 Login Page

A Windows 11 Login Page Made With Pure HTML & CSS

## jsencrypt

### Key Concepts : Public vs Private Keys

- **Public Key**: Used for **encryption**. Safe to share publicly.
- **Private Key**: Used for **decryption**. Keep this secret!

```javascript
const crypt = new JSEncrypt();

// For encryption only (using public key)
crypt.setPublicKey(publicKeyString);
const encrypted = crypt.encrypt('secret message');

// For decryption (requires private key)
crypt.setPrivateKey(privateKeyString);  
const decrypted = crypt.decrypt(encrypted);
```

### Key Generation : OpenSSL Key Generation (Recommended)

For production applications and maximum security, generate keys using OpenSSL:

```bash
# Generate a 2048-bit private key (recommended minimum)
openssl genrsa -out private.pem 2048

# Generate a 4096-bit private key (higher security)
openssl genrsa -out private.pem 4096

# Extract the public key
openssl rsa -pubout -in private.pem -out public.pem

# View the private key
cat private.pem

# View the public key  
cat public.pem
```

### Tests

On the first terminal, launch the test server

```bash
python3 test_local_server.py
```

On the second terminal, launch the phishing web page

```
chromium-browser index.html &
```

Insert credentials and check the output on test server
