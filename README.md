# frontend-engineering-challenge

This is a server that provides an API for the Frontend Engineer Challenge for Schmidt Futures. It is meant to be delivered to a potential applicant as a Docker Image.

## Local Development

### Code Formatting

If there are particular rules that you want to add or otherwise toggle, you should generally use the `.prettierrc` file to configure the rules.
[Prettier](https://prettier.io/docs/en/index.html) is an opinionated multi-language code formatter. We use this to make sure our code is consistently formatted.

The general rule of thumb is: _use Prettier for formatting and ESLint for everything else (e.g. code-quality bugs)_

### Hooks

This repository uses [husky](https://www.npmjs.com/package/husky) to run git hooks (found in the `.husky` directory) to aid in development.
Before each commit, `husky` will run a `pre-commit` hook to run eslint and prettier formatter on your code to ensure consistent code syntax and style uniformity.

Additional hooks should be [added](https://typicode.github.io/husky/#/?id=create-a-hook) under the `.husky` directory as seperate scripts and this README should be updated accordingly.

### Docker

When doing local development and testing, the API should always be run in a Docker environment. This ensures consistency in environments amongst all contributors.

First ensure you have Docker installed on your machine.
[Docker Desktop](https://docs.docker.com/desktop/) is recommended for all operating systems.

Once installed, execute the following commands from this repository's root directory:

This command will build the initial docker image based off the Dockerfile and create a new container.

```bash
docker-compose up --build
```

You can now access the API at http://localhost:3000/health
