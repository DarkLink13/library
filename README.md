# Library API
The Library API is a RESTful API that provides clients with access to a list of available books and the ability to read those books page by page in plain text or HTML format. In the future, the API may support additional reading formats and integration with other online book service providers.

## Technical Requirements
- Python 3.x
- PostgreSQL
- psycopg2 (Python PostgreSQL adapter)
- Git

# Getting Started
## Installation
1. Clone the Git repository:
```
bash
git clone https://gitlab.com/gbh-candidates/jorge-amado-hernandez-betancourt-darklink13-2023-3-23-dev-backend-coding-challenge-library-api.git
```

2. Install the required dependencies:
```
pip install -r requirements.txt
```

## Configuration
1. Set the following environment variables and save it in a `.env` file in root project folder:
```
USER=<username of the postgresql database>
PASS=<password of the postgresql database>
NAME=<name of the postgresql database>
PORT=<port of the postgresql database>
HOST=<host of the postgresql database>
SERVER_PORT=<port of the server>
SERVER_HOST=<host of the server>
```

2. Run the following command to create the database and populate it with seed data:
```
python run_migrations.py
python run_seeds.py
```

3. Start the server by running the following command:

```
python setup.py
```
## API Endpoints

### Get List of Books
- Request:
```
GET /book
```
- Response:
```
[
    {
        "id": 1,
        "title": "Ut vel mauris",
        "author": "Phasellus"
    },
    {
        "id": 2,
        "title": "Nam vel quam",
        "author": "Maecenas"
    },
    {
        "id": 3,
        "title": "Nunc vehicula, ligula",
        "author": "Curabitur"
    }
]
```
### Get Book
- Request:
```
GET /book/{book_id}
```
- Response:

```
{
    "id": 5,
    "title": "Donec vitae",
    "author": "Phasellus"
}
```
### Get Book Page
- Request:
```
GET /book/{book_id}/page/{page_number}/{format}
```
- Response:

```
{ 
    "number": 1, 
    "text" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac elit eu elit sagittis vestibulum. Proin aliquam eros quam, quis malesuada felis laoreet ac. Duis sit amet quam quis metus hendrerit elementum nec ac ipsum. Sed euismod nisi id justo ullamcorper, quis tristique ipsum lobortis. Sed vel efficitur ipsum. Vestibulum et suscipit arcu, at luctus dolor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Fusce fringilla vitae lorem ut varius. Donec euismod aliquam magna, a suscipit enim commodo nec. Sed efficitur consectetur purus, eget feugiat eros ultrices in. Quisque dictum dignissim nunc, ac consequat elit ornare id. Vestibulum tincidunt erat sit amet eros dignissim dapibus. Ut non elit eu turpis sollicitudin sagittis vitae id ipsum.", 
    "book_id": 3
}
```