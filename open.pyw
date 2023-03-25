import webbrowser 
import time 
import random 
while True: 
 site=random.choice(["localhost:3000/api/v1/tasks","localhost:3000/tasks/hello","localhost:3000/index.html"]) 
 webbrowser.open(f"http://{site}") 
 time.sleep(random.randint(15,300)) 
