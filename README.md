# hedgehog4-server
Ratings and reviews x-platform app allowing anyone to know whether something or somewhere will be a good use of their time or money before they spend it


--Running Server Locally

 - set env variables
    - Export FLASK_APP='runserver.py'
    - Export FLASK_ENV='development'
    - Export SCRIPT_NAME='/api'
    - Export GPT_API_KEY={your_api_key}'
    
- run gunicorn -b :5000 --access-logfile - --error-logfile - runserver:app