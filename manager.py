import json
import os
FILE_NAME="youtube.txt"

def load_data():
    try:
        with open(FILE_NAME,"r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

videos=load_data()

def list_all_videos():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("---------------------------------------------")
    print(f" index : video name   - time")
    for index,video in enumerate(videos,start=1): 
       print(f"({index}) :  {video["name"]} - {video["time"]}")
    print("---------------------------------------------")

def add_video():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        list_all_videos()
        name=input("Enter video Name: ")
        time=input("Enter video time: ")
        videos.append({"name":name,"time":time})
        save_data(videos)
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        print("add_video")
        
def update_video():
    os.system('cls' if os.name == 'nt' else 'clear')
    list_all_videos()
    try:
        index=int(input("Enter Video number to update: "))
        if 1<= index<=len(videos):
            new_name=input("Enter the Updated video name :")
            new_time=input("Enter the Updated video time :")
            videos[index-1]={'name':new_name,'time':new_time}
            save_data(videos)
        else:
            print("Invalid Index")
    except ValueError:
        print("Wrong input")
    
def delete_video():
    os.system('cls' if os.name == 'nt' else 'clear')
    list_all_videos()
    try:
        index=int(input("Enter Video number to update: "))
        if 1<= index<=len(videos):
            videos.pop(index-1)
            save_data(videos)
        else:
                print("Invalid Index")
    except ValueError:
        print("Wrong input")

def save_data(videos):
    try:
        with open(FILE_NAME,"w") as file:
            json.dump(videos,file)
    except Exception as e:
        print("Error saving data:", e)
