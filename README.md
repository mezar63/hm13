# Project Name

Brief description of your project.

## Installation

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the Redis broker using Docker:

    ```bash
    docker run -p 6379:6379 redis
    ```

3. Generate blogs into the database:

    ```bash
    python manage.py generate_blogs 50
    ```

4. Run the Django web server:

    ```bash
    python manage.py runserver
    ```

