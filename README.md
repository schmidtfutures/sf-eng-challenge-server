# frontend-engineering-challenge

Welcome to the Schmidt Futures Frontend Engineering Challenge Server!

To share with an applicant:

1. Share the docker-compose.yml file with the applicant
2. Instruct them to run `docker-compose up --build` in the same directory as the file.
3. This will run a server locally that accepts requests from any origin (no CORS issues)
4. The applicant can then create their solution using the endpoints provided by the API

If an applicant has issues with the docker image, they can be shared on this repo directly and run things locally or they could be provided the `MockDB` file directly.

The google doc for this challenge is [available here](https://docs.google.com/document/d/1Hs8iKE__AlDmJokUU1z-y3nhhKd72JgMcK4hq_aGhGk).

## Next Steps

### Option A: Docker Compose

We have provisioned a docker image for the API that you can pull down and run locally. This docker image will expose an API server that will accept requests from the frontend running on your your local machine (don’t worry, we have taken care of CORS so you should be able to immediately start using it without hassle\*).

1. Download and install docker on your machine if you haven’t already (see docker desktop)
2. Download the following `docker-compose.yml` file into a directory of your choice: 
3. Run docker compose in the same directory as the file -- this will start the challenge API server

   `docker-compose up --build`

4. Go to `localhost:3000/health` and verify that the server is running
5. Check out the api documentation at `localhost:3000/docs`

Enjoy the challenge - we look forward to seeing what you come up with!

If you have any questions or run into any issues\*, please reach out to the team member who sent you the challenge or Josh Hendler (jhendler@schmidtfutures.com).

### Option B: Cloning the repo directly

If you are running the server directly from this repo instead of using the provided docker-compose file, be sure to run the API in its Docker environment.

```bash
docker-compose up --build
```

If you need to run the application directly for some reason you may use the following commands to spin up a virtual environment, download needed packages, and explicitly run the server.

```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

You can access the docs at http://localhost:3000/docs

Happy Building!
