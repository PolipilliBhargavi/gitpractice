with open("login.txt") as f:
   print(f.read())
with open("login.txt", "w") as f:
    f.write("Deployment completed")
with open("login.txt", "a") as f:
    f.write("\nSuccess")
    f.write("\nDeployment completed successfully")

try:
    with open("logout.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("file is not present in the directory")
       
with open("createfile.txt", "x") as f:
    f.write("New file has been created")

with open("json.py", "x") as f:
    f.write("json")