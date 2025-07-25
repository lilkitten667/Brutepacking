import os
import zipfile
from time import time
print("BruteForce Python")
print("Author: Cynthia Rattey")
print("Version: 1.0") 
def cls():
	os.system('cls' if os.name == 'nt' else 'clear')
	
def main():
    cls()
    file_path = r"C:/python/Brutepacking/crackmeEn.zip"
    word_list = r"C:/python/Brutepacking/rockyou.txt"

    try:
        zip_ = zipfile.ZipFile(file_path)
    except zipfile.BadZipfile:
        print("error, please check path and try again")
        return
    password = None
    i = 0
    timeCount = time()
    with open(word_list, "r", encoding="utf-8", errors="ignore") as f:
         for x in f:
              i += 1
              password = x.strip()
              try:
                   zip_.extractall(pwd=password.encode())
                   totalTime = time() - timeCount
                   print(f"\n Bygolly we are in luck! Password found: " + "\n unlocked with: " + password)
                   print(f" Took {totalTime:.2f} seconds to arrive at the correct combo." + 
                         f"\n That is, {i/totalTime:.2f} attempts per second. ")
                   return
              except RuntimeError as e:
                     continue
    print("Troubling news, Password Not Found :(" + str(e))
if __name__ == "__main__":
    main()