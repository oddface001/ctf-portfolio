## PicoCTF - Scan Surprise (Forensics)

**Author:** Jeffery John  
**Description:**  
The flag is hidden in an image instead of plain text. We’re given a `challenge.zip` file which contains a suspicious PNG image. The goal is to extract the flag from it.

### Files Provided
- `challenge.zip` → `home/ctf-player/drop-in/flag.png`

---

### 🔍 Solution Steps

1. **Unzipped the archive**:
   ```bash
   unzip challenge.zip
````

2. **Found the image**:

   ```bash
   ls home/ctf-player/drop-in/
   # Output: flag.png
   ```

3. **Scanned the image for embedded data using `zbarimg`**:

   * Installed the tool (if not already installed):

     ```bash
     sudo apt update
     sudo apt install zbar-tools
     ```
   * Scanned the image:

     ```bash
     zbarimg home/ctf-player/drop-in/flag.png
     ```

4. **Output revealed the flag**:

   ```
   QR-Code:picoCTF{p33k_@_b00_b5ce2572}
   ```

---

### ✅ Flag

```
picoCTF{p33k_@_b00_b5ce2572}
