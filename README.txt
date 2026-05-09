README - Smart Download Organizer

Problem:
My downloads folder becomes messy because files from internships, college work, screenshots, PDFs, and code files all get mixed together.

Solution:
I built a small Python automation script that automatically scans a folder and organizes files into categories like Images, Documents, Videos, Code, Archives, and Others.

How it works:
- Reads all files from the target folder
- Detects file types using extensions
- Creates folders automatically
- Moves files into the correct category

What AI helped with:
I used ChatGPT to quickly generate the initial file-sorting logic and improve error handling.

What I did myself:
I customized the categories, tested the script locally, fixed folder path issues, and verified whether files were being moved correctly.

How to run:
1. Create a folder named "sample_downloads"
2. Add random files into it
3. Run:
   python organizer.py
