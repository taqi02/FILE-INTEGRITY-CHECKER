# FILE-INTEGRITY-CHECKER

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: ANSARI MOHD TAKI

*INTERN ID*: CT04DL765

*DOMAIN*: CYBER SECURITY & ETHICAL HACKING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

*DISCRIPTION*:  

In any digital environment, ensuring the accuracy and consistency of files is essential. Whether it's for securing sensitive documents, verifying software files, or detecting tampering, having a reliable way to confirm that a file hasn't changed is critical. This project introduces a File Integrity Checker, a simple Python script that uses cryptographic hashing to confirm whether two files are identical or if any changes have occurred.

The core idea behind the tool is based on hashing—a method used to generate a unique code that represents a file's contents. Specifically, this project uses the SHA-256 hashing algorithm, known for its high level of security and wide acceptance in the cybersecurity industry. A hash value, once generated, acts like a fingerprint of the file. Even the smallest change in the file—like adding a space or changing one character—will produce a completely different hash.

The script built for this project is straightforward and user-friendly. When executed, it asks the user to input the paths of two files. It then reads the contents of each file and computes the SHA-256 hash values for both. After generating the hashes, the script displays them and clearly states whether the files match or differ. This comparison provides a fast and effective way to check file integrity.

One of the main benefits of this tool is its simplicity. It is written entirely in Python and only uses the standard hashlib module, which comes pre-installed with Python. This means there’s no need to install additional libraries or use complicated interfaces. The script is designed to run on any system with Python installed, making it highly portable and easy to integrate into other processes or workflows.

This File Integrity Checker has multiple real-world applications. For example, system administrators can use it to check if key system files have been altered unexpectedly. Developers can verify the consistency of project files when transferring data between machines or during deployment. Even regular users can use it to ensure that downloaded files haven’t been modified or corrupted.

From an educational perspective, the project is also a great way to understand how hashing works and why it is so important in maintaining data security. It connects theoretical knowledge of cryptographic functions with a practical implementation that anyone can use. It also introduces basic principles of cybersecurity in a hands-on manner, helping learners develop a deeper understanding of file verification and integrity techniques.

In conclusion, this Python-based File Integrity Checker is a useful tool for anyone who needs to confirm the authenticity of their files. It offers a quick and efficient way to detect changes using reliable cryptographic methods. By combining ease of use with robust functionality, the project demonstrates how simple programming solutions can solve important problems in digital security and file management.

*OUTPUT*

![Image](https://github.com/user-attachments/assets/601780cd-a357-472a-b9a3-98d457495605)
