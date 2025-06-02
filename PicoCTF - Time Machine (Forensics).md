## PicoCTF - Time Machine (Forensics)

**Description:**  
"What was I last working on? I remember writing a note to help me remember..."

### Tools Used
- `git log --oneline`
- Terminal

### Solution Steps
1. Unzipped the challenge files.
2. Navigated to the directory containing the `.git` folder.
3. Used `git log --oneline` to check commit history.
4. Discovered the flag directly embedded in the commit message.

### Flag
`picoCTF{t1m3m@ch1n3_b476ca06}`

### Lessons Learned
- Git commit messages can contain sensitive information.
- Always inspect Git history when investigating forensics challenges.
