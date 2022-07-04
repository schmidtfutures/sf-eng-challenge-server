# frontend-engineering-challenge

Welcome to the Schmidt Futures Frontend Engineering Challenge!

If an applicant has issues with the docker image, they can be shared on this repo and run things locally or they can be provided the `userDB.json` file directly.

The google doc for this challenge is [available here](https://docs.google.com/document/d/1Hs8iKE__AlDmJokUU1z-y3nhhKd72JgMcK4hq_aGhGk).

## Background

You are welcome to use whatever tools or frameworks you wish. The current team primarily makes use of ReactJS but is familiar with a wide variety of frameworks. So if you’d prefer to use a different one, feel free.

This challenge is not intended to take beyond 3-5 hours–if that time commitment represents a difficulty, please let us know and we are happy to accommodate. You are not tightly bound to the 3-5 hour window, if you wish to go slightly over or under the time, you are welcome to make note of that and proceed.

The intent of this challenge is not to develop perfect code nor a pixel-perfect design; rather, our intent is to get a sense of how you approach the type of engineering and design challenges we are likely to encounter.

When you complete your solution, we’d appreciate you making it accessible to us either via a public code repository or an emailed zipfile. The solution that you write is yours to own–we will not reuse the code you’ve written.

## Challenge

Your challenge is to build a frontend feature that displays matches between users and opportunities. This consists of two parts: ingesting user-opportunity matches from an API, and building a frontend feature to display those results in a useful way.

As part of the signup process users indicated the types of roles they are interested in. Similarly, organizations indicated their open opportunities (roles they are trying to fill). Matches were then generated between each opportunity and user interest through a Lvenshtein Distance algorithm. This generated a match level score from 0-100 where 100 indicates a perfect match between an open role and user interest.

For the purposes of this challenge, you only need to create a feature that displays the data returned from the GET matches_by_user endpoint. However, it is conceivable that, in the future, other endpoints such as GET matches_by_organization could be implemented that would return similar JSON objects.

Feel free to add (and ideally document!) any other features or functionalities that might make sense such as: filtering to a specific user or organization, paging results, implementing sorts or filters, beautifying with CSS, implementing tests, etc.

### Some things we’ll be looking out for

- Does the solution make sense?
- How usable and useful is this feature for the targeted user?
- How are matches displayed? What data is most apparent?
- How are edge cases, if any, handled?
- How is the code itself organized?
- Is the feature extensible for potential future use?
- Would the solution fit well into an existing tool or application?
- Does the code run and are instructions for use clearly documented?
- What kinds of UI, UX, functional, and stylistic choices were made?

After submitting, we will schedule approximately 45-minutes for a presentation of your solution including a live demo (if applicable), questions and discussion around your code and design choices, and of course leaving room for questions you have about the team or position.

## Next Steps

Ensure you have Docker installed on your machine.
[Docker Desktop](https://docs.docker.com/desktop/) is recommended for all operating systems.

### Option A: pulling the docker image

NOTE: If you have cloned this repo, you may skip to Docker & NPM

We have provisioned a docker container that you can pull down and run locally. This docker container will expose an API server on that will accept requests from the frontend running on your your local machine (don’t worry, we have taken care of CORS so you should be able to immediately start using it without hassle\*).

1. Download and install docker on your machine if you haven’t already
2. Pull down our publicly available docker image: `schmidtfutures/matching-challenge-server`
3. Run the docker image to spin up the local web server using port 3000 from Docker Desktop or via the CLI:

   `docker run -p 3000:3000 sf-frontend-challenge-api`

4. Go to `localhost:3000/health` and verify that the server is running
5. Check out the api docs at `localhost:3000/docs`

Enjoy the challenge - we look forward to seeing what you come up with!

If you have any questions or run into any issues\*, please reach out to the team member who sent you the challenge or Josh Hendler (jhendler@schmidtfutures.com).

### Option B: cloning the repo

If you are running the server directly from this repo instead of using the image, be sure to run the API in its Docker environment.

First, after cloning this repo install the needed npm packages.

```bash
npm install
```

Once installed, execute the following commands from this repository's root directory:

This command will build the initial docker image based off the Dockerfile and create a new container.

```bash
docker-compose up --build
```

You can access the docs at http://localhost:3000/docs

Happy Building!
