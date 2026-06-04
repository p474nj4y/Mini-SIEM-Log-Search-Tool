import os #useful module for python's built in os

SUPPORTED_EXTENSIONS = ( #creates a tuple containing file extensions)
    ".txt",
    ".log",
    ".http",
    ".dns",
    ".ftp",
    ".sh"
)

def search_logs(folder, keyword):
    results = []
    for root, dirs, files in os.walk(folder):# os.walk goes through every folder
         for file in files:
              if file.endswith(SUPPORTED_EXTENSIONS):
                   path = os.path.join(root, file) #combines folder path and filename
                   try:
                        with open(path, "r", errors="ignore") as f:
                             for line_num, line in enumerate(f, 1): #reads the file line by line - enumerate starts numbering at 1  
                                  if keyword.lower() in line.lower():
                                       results.append(
                                            (file, line_num, line.strip())
                                       )
                   except Exception as e:
                        print(f"Error reading {file}: {e}")
    return results

folder = input("Folder Path: ")
keyword = input("Search Keyword: ")
matches = search_logs(folder, keyword)
print("\n<<<<<<< RESULTS >>>>>>>\n")
for file, line_num, text in matches: #loops through every match found
     print(
          f"[{file}] Line {line_num}: {text}" #display each result
     )
print(f"\nTotal Matches: {len(matches)}") #shows total number of matches found
