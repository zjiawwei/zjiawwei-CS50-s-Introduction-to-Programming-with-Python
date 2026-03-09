import re 
import sys 

def main():
    print(parse(input("HTML:").strip()))

def parse(s):
    match = re.search(r"https?://(?:www\.)?youtube\.com/embed/([a-zA-z0-9_-]+)",s,re.IGNORECASE)
    if match:
        return(f"https://youtube.be/{match.group(1)}")
if __name__ == "__main__":
    main()