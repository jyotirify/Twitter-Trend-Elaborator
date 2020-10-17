import React from 'react'
import Paper from '@material-ui/core/Paper';

const TopTweets = ({ top_tweets }) => {
  return (
    <Paper elevation={3}>
      <center><h1>Top Tweets List</h1></center>
      {/* <h2>{top_tweets}</h2> */}
      <center><table>
        <thead>
          <th>Tweet</th>
          <th>Url</th>
          <th>Tweet Count</th>
        </thead>
        <tbody>
          {top_tweets.map((top_tweet) => (
            <tr>
              <td>{top_tweet.name}</td>
              <td>{top_tweet.url}</td>
              <td>{top_tweet.volume}</td>
            </tr>
          ))}
        </tbody>
      </table>
      </center>
    </Paper>
  )
};

export default TopTweets