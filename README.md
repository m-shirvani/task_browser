##how to run:
- make sure you are in `app` directory
- build the docker image: `docker build -t task_browser .`
- run the container:
  
  ` docker run -p 8007:8000 --name task_browser task_browser gunicorn task_browser.wsgi:application --bind 0.0.0.0:8000`
  
- head to <http://localhost:8007> to see the tasks table
- head to <http://localhost:8007/qraphql> to play with the graphql playground 


