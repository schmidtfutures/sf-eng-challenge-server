/* eslint-disable @typescript-eslint/no-unsafe-return */
/* eslint-disable @typescript-eslint/no-unsafe-assignment */
import * as data from './db/usersDB.json';

const getMatches = function getMatches(userId) {
  if (userId) {
    // eslint-disable-next-line @typescript-eslint/no-unsafe-member-access
    const filtered = data[userId];

    return filtered;
  }
  return data;
};

export default getMatches;
