````markdown
## PicoCTF - Even RSA Can Be Broken??? (Cryptography)

**Description:**  
You're given multiple RSA ciphertexts and public keys. All of them use the same public exponent `e = 65537`, but different moduli `N`. The challenge title and setup hint that something is wrong with how the RSA keys were generated.

---

### Solution Steps

1. Collected multiple outputs by repeatedly running:
   ```bash
   nc verbal-sleep.picoctf.net 60565
````

Each connection returned values of `N`, `e`, and `ciphertext`.

2. Parsed and stored each triplet of values for further analysis.

3. Wrote a Python script (`rsa_break.py`) to:

   * Loop through every pair of modulus values (`N`).
   * Use the `gcd(N1, N2)` function to check for shared factors.
   * If a common prime factor `p` is found, compute `q = N // p`.
   * Use the `inverse` function to compute the private key `d = inverse(e, (p-1)*(q-1))`.
   * Decrypt the ciphertext using `m = pow(ciphertext, d, N)` and convert it to bytes with `long_to_bytes`.

4. The script identified that `p = 2` was shared in at least one pair:

   ```
   Found common factor between entry 0 and 1!
   Factored N[0]: p = 2, q = ...
   Decrypted Flag from entry 0:
   picoCTF{tw0_1$_pr!m3f81fef0a}
   ```

---

### Script (`rsa_break.py`)

```python
from math import gcd
from Crypto.Util.number import long_to_bytes, inverse

# Replace with all the collected values from the netcat outputs
data = [
    {
        "N": 22600156565298292704467857703915388079094884496939475169201170689320715327184859247931203775997760057232943322258704707658127855004739417002270054546756874,
        "e": 65537,
        "ciphertext": 3406905158151934326242743055873605855773021998083443118100479123844760033890892252332747124706425547936070808782842695892545349360276108421634045351232839
    },
    {
        "N": 14038908428221568994770303214813903101810285787373127732883929938720699595685257287422670944558641973421040481108225846004946476089801135997391577221884022,
        "e": 65537,
        "ciphertext": 8108194785005187277618439067007035769875630111191932653278841630381315900005487371243321966755669622665875744815758735578570264211483097445849183385474073
    },
    # Add more entries as needed...
]

def try_factoring():
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            N1 = data[i]["N"]
            N2 = data[j]["N"]
            common_factor = gcd(N1, N2)
            if 1 < common_factor < min(N1, N2):
                print(f"Found common factor between entry {i} and {j}!")
                p = common_factor
                q = N1 // p
                print(f"Factored N[{i}]: p = {p}, q = {q}")
                e = data[i]["e"]
                ciphertext = data[i]["ciphertext"]
                phi = (p - 1) * (q - 1)
                d = inverse(e, phi)
                plaintext = pow(ciphertext, d, N1)
                flag = long_to_bytes(plaintext)
                print(f"Decrypted Flag from entry {i}:\n{flag.decode('utf-8')}\n")
                return
    print("No common factors found between any pair of N values.")

try_factoring()
```

---

### Flag

```
picoCTF{tw0_1$_pr!m3f81fef0a}
```