import fetch from 'isomorphic-fetch';
import queryString from 'query-string';
import * as config from 'helpers/config';

const apiUrl = config.get('API_URL');

export const REQUEST_STATS = 'REQUEST_STATS';
export const RECEIVE_STATS = 'RECEIVE_STATS';

export function requestStats() {
  return {type: REQUEST_STATS};
}

export function receiveStats(query, json) {
  return {
    type: RECEIVE_STATS,
    query,
    json
  };
}

export function fetchStats(query = {}) {
  return function next(dispatch) {
    dispatch(requestStats());

    return fetch(apiUrl + '/api/stats?' + queryString.stringify(query))
      .then(response => response.json())
      .then(json => new Promise(resolve => {
        dispatch(receiveStats(query, json));
        resolve();
      }));
  };
}
