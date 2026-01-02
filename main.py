import os
from manager import * 

def main():
    while True:
        list_all_videos()
        print("\n Youtube Manager | Choose an option")
        print("1.List all youtube videos")
        print("2.Add a youtube video")
        print("3.update a youtube video details")
        print("4.Delete a youtube video")
        print("5.Exit the app ")
        # 
        try:
            choice=int(input("Choose Option:- "))
            match choice:
                case 1:
                    videos=load_data()
                    list_all_videos()
                case 2:
                   
                    add_video()
                case 3:
                    update_video()
                case 4:
                    delete_video()
                case 5:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Thank you for using my app")
                    break
                case _:
                    raise(ValueError)
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Enter only number between 1 to 5")
            continue
        
if __name__ == "__main__":
    main()