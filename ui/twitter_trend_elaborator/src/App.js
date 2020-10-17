import React, { Component } from 'react';
import TopTweets from './components/top_tweets';
import ButtonAppBar from './components/navbar';
import './App.css';
import Button from '@material-ui/core/Button';
import Container from '@material-ui/core/Container';
import Box from '@material-ui/core/Box';

class App extends Component {


  render() {
    const show_tweets = this.state.show_tweets;
    return (
      <Container >
        <ButtonAppBar></ButtonAppBar>
        <Box display = "flex" my = {2}>
        <Box mr = {2}>
        <Button variant="contained" color = "primary" onClick={this.handleInput.bind(this)} >Get Top Tweets</Button>
        </Box>
        <Button variant="contained" color = "primary" onClick={this.handleInputHide.bind(this)} >Hide Top Tweets</Button>
        </Box>
        {show_tweets == "True" ? (
          <TopTweets top_tweets={this.state.top_tweets} />
        ) : (<span></span>)}
      </Container >
    );
  }

  handleInput() {
    this.setState({ show_tweets: "True" });
  }
  handleInputHide() {
    this.setState({ show_tweets: "False" });
  }
  state = {
    top_tweets: [],
    show_tweets: "False"
  };

  componentDidMount() {
    fetch('http://localhost:5000/get_top_tweets')
      .then(res => res.json())
      .then((data) => {
        this.setState({ top_tweets: data })
      })
      .catch(console.log)

  }
}

export default App;
