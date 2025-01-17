import requests

def fetch_data():
    url = 'https://github.com/posts'
    response = requests.get(url)

    if response.status_code == 200:
        print("Successfully fetched data!")
        posts = response.json()
        for post in posts:
            print(f"Post ID: {post['id']}, Title: {post['title']}")
    else:
        print("Failed to fetch data. Status code:", response.status_code)

if __name__ == "__main__":
    fetch_data()
