import json
import os


# Function to load JSON data from files
def load_json(filename):
    if not os.path.exists(filename):
        print(f"Error: File {filename} not found.")
        return []
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(f"Error: File {filename} is not a valid JSON.")
        return []


# Function to extract user values from JSON data
def extract_user_values(json_data):
    user_values = set()
    for item in json_data:
        if "string_list_data" in item and len(item["string_list_data"]) > 0:
            user_values.add(item["string_list_data"][0].get("value", ""))
    return user_values


following = load_json("connections/followers_and_following/following.json")
followers = load_json("connections/followers_and_following/followers.json")


following_users = extract_user_values(following)
follower_users = extract_user_values(followers)

not_following_back = following_users - follower_users

# Print Results
print("Users you are following that are not following you back:")
for user in not_following_back:
    print(user)

print(
    f"\nTotal users you are following that are not following you back: {len(not_following_back)}"
)
