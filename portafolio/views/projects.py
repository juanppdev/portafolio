import reflex as rx
import requests

# Define the URLs and the access token
repos_url = 'https://api.github.com/users/Juanppdev/repos?sort=created'
graphql_url = 'https://api.github.com/graphql'
access_token = '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'

# Fetch the repositories
response = requests.get(repos_url)
data = response.json()
repositories = data if isinstance(data, list) else []

# Extract repository names
repo_names = [repo['name'] for repo in repositories]

# Function to get openGraphImageUrl for a repository
def get_repo_image(repo_name):
    query = '''
    query {
      repository(owner: "Juanppdev", name: "%s") {
        openGraphImageUrl
      }
    }''' % repo_name

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
    }

    response = requests.post(graphql_url, json={'query': query}, headers=headers)
    if response.status_code == 200:
        result = response.json()
        if 'data' in result and 'repository' in result['data']:
            return result['data']['repository'].get('openGraphImageUrl', '')
    return ''

# Filter repositories with the topic 'projectoficial' and get their images
repositories_with_images = []

for repo in repositories:
    if 'topics' in repo and 'projectoficial' in repo['topics']:
        image_url = get_repo_image(repo['name'])
        repo['openGraphImageUrl'] = image_url
        repositories_with_images.append(repo)

# Print the filtered repositories with their images
for repo in repositories_with_images:
    print(f"Repo: {repo['name']}, Image: {repo['openGraphImageUrl']}")

# Reflex component to display projects
def projects() -> rx.Component:
    return rx.vstack(
        rx.heading("Proyectos", size="7"),
        rx.desktop_only(
            rx.grid(
            *[
                rx.link(
                    rx.card(
                        rx.vstack(
                            rx.image(
                                src=repo['openGraphImageUrl'],
                                width="100%",
                                height="auto",
                            ),
                            rx.heading(repo["name"], size="6"),
                            rx.text(repo["description"]),
                            spacing="3",
                            width="100%"
                        ),
                        background="center/contain no-repeat url('/img/bg.jpg')",
                        size="5",
                    ),
                    href=repo["html_url"],
                    is_external=True
                ) for repo in repositories_with_images
            ],
            columns="3",
            spacing="5",
            width="100%",
            margin_bottom="75px"
        )
        ),
        rx.mobile_and_tablet(
            rx.grid(
            *[
                rx.link(
                    rx.card(
                        rx.vstack(
                            rx.image(
                                src=repo['openGraphImageUrl'],
                                width="100%",
                                height="auto",
                            ),
                            rx.heading(repo["name"], size="6"),
                            rx.text(repo["description"]),
                            spacing="3",
                            width="100%"
                        ),
                        background="center/contain no-repeat url('/img/bg.jpg')",
                        size="5",
                        width="100%"
                    ),
                    href=repo["html_url"],
                    is_external=True
                ) for repo in repositories_with_images
            ],
            columns="1",
            spacing="2",
            width="100%",
            margin_bottom="75px"
        )
        )
    )
