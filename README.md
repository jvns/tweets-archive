### a twitter archive thing

Powers https://tweets.jvns.ca

### how to set it up

1. Get your twitter archive from Twitter (at this point I think their archive tool doesn't work anymore, so ideally you got it in 2022)
1. Use Darius Kazemi's [twitter archive tool](https://tinysubversions.com/twitter-archive/make-your-own/) to generate a zip file, and unzip it into a directory, let's call it ARCHIVE_DIR
3. 
  ```
  git clone https://github.com/jvns/tweets-archive
  cd tweets-archive
  cp ARCHIVE_DIR/searchDocuments.js .
  cp -R ARCHIVE_DIR/TWITTER_USERNAME/tweets_media .
  ```
4. Edit `index.html` and replace "julia" with your name

