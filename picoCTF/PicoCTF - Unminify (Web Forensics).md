## PicoCTF - Unminify (Web Forensics)

**Description:**  
A minified webpage that "delivers" the flag but doesn’t display it visibly.

### Solution Steps
1. Viewed page source using CTRL+U.
2. Inspected the HTML and found the flag hidden in an unusual place.
3. The flag was embedded in the class attribute of a `<p>` tag:
   ```html
   <p class="picoCTF{pr3tty_c0d3_dbe259ce}"></p>
