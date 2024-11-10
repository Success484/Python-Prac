import json
import os

def get_user_data():
    user_data = {}
    user_data['name'] = input("Enter your name: ")
    if user_data['name'] == None:
        print('enter a valid name')
        return False
    
    user_data['age'] = input("Enter your age: ")
    return user_data


def save_data_to_file(data, filename="user_data.txt"):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            existing_data = json.load(file)
    else:
        existing_data = []
    
    existing_data.append(data)
    
    with open(filename, 'w') as file:
        json.dump(existing_data, file, indent=4)



# def get_all_users(filename="user_data.txt"):
#     try:
#         with open(filename, 'r') as file:
#             all_user = json.load(file)
#             return all_user
#     except (FileNotFoundError, json.decoder.JSONDecodeError):
#         print(f"Failed to read data from {filename}. Returning an empty list.")
#         return []

if __name__ == "__main__":
    user_data = get_user_data()
    save_data_to_file(user_data)
    print("Data saved to user_data.txt")
    # user_data = get_all_users()
    for user in user_data:
        print(user)