/* eslint-disable @typescript-eslint/no-unsafe-assignment */
/* eslint-disable @typescript-eslint/no-unsafe-member-access */
/* eslint-disable @typescript-eslint/no-unsafe-call */
import express, { Application, Request, Response } from 'express';
import * as swaggerUi from 'swagger-ui-express';
import * as spec from './spec.json';
import getMatches from './controller';

const app: Application = express();
const port = 3000;

// eslint-disable-next-line func-names
app.use(function (req, res, next) {
  res.header('Access-Control-Allow-Origin', '*'); // update to match the domain you will make the request from
  res.header(
    'Access-Control-Allow-Headers',
    // eslint-disable-next-line @typescript-eslint/comma-dangle
    'Origin, X-Requested-With, Content-Type, Accept'
  );
  next();
});

app.use('/docs', swaggerUi.serve, swaggerUi.setup(spec));

// Health endpoint
/**
 * @param {Request} req - Express request
 * @param {Response} res - Express response
 * */
app.get('/health', (req: Request, res: Response) => {
  res.json({ healthy: true });
});

// Health endpoint
/**
 * @param {Request} req - Express request
 * @param {Response} res - Express response
 * */
app.get('/matches', (req: Request, res: Response) => {
  const { userId } = req.query;

  const users = getMatches(userId);
  res.json({ users });
});

app.listen(port, () => {
  /* eslint-disable-next-line no-console */
  console.log(`server running at http://localhost:${port}`);
});
