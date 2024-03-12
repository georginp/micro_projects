import requests


def fetch_user_repositories(username):
    desired_keys = ["name", "description", "language", "stargazers_count"]
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code == 200:
        user_info = response.json()
        repositories = []

        for repo_info in user_info:
            selected_data = {key: repo_info[key] for key in desired_keys}
            repositories.append(selected_data)

        return repositories
    else:
        print(f"Failed to fetch info. Status code: {response.status_code}")


def display_repository_info(repositories):
    for repository in repositories:
        print(repository)


def main():
    username = input("Please enter a GitHub username: ")
    repositories = fetch_user_repositories(username)
    display_repository_info(repositories)


if __name__ == "__main__":
    main()
