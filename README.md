##how to run:
- make sure you are in `app` directory
- build the docker image: `docker build -t task_browser .`
- run the container:
  
  ` docker run 
  -p 8007:8000
  --name task_browser
  task_browser
  gunicorn task_browser.wsgi:application --bind 0.0.0.0:8000
`
- head to <http://localhost:8007> to play with the graphql queries
- the code is also deployed to aws to simulate production settings:

`http://production-alb-1305611180.us-east-1.elb.amazonaws.com/`


