### a twitter archive thing

Powers [https://tweets.jvns.ca](https://tweets.jvns.ca). As usual for me it's
only designed for me to use and not really general software, a lot of my
information is hardcoded into it.

To make it work, you need two things:

1. a `searchDocuments.js` with your tweets
1. a `tweets_media` directory

I got those from [this tool by Darius Kazemi](https://tinysubversions.com/twitter-archive/make-your-own/)

### how to set it up

1. Get your twitter archive from Twitter (seems to still be working as of July 25, 2023)
2. Use Darius Kazemi's [twitter archive tool](https://tinysubversions.com/twitter-archive/make-your-own/) to generate a zip file, and unzip it into a directory, let's call it ARCHIVE_DIR
3. 
  ```
  git clone https://github.com/jvns/tweets-archive
  cd tweets-archive
  cp ARCHIVE_DIR/searchDocuments.js .
  cp -R ARCHIVE_DIR/TWITTER_USERNAME/tweets_media .
  # build all of the individual tweet HTML pages
  ```
4. Edit `app.js`, `index.html`, and `build.py` to replace my information with your information (described in the next section)
5. Run `python3 scripts/build.py`

### edits you'll need to make

All of my information is hardcoded into the files. You'll need to edit `index.html`, `build.py`, and `app.js`. To replace it with your information, search the code for:

* `julia`
* `Julia`
* `b0rk`
* `profile.jpg`

and replace it with your information instead.

### themes

It literally copies all of the CSS from https://nitter.net so you should be able to
use any of Nitter's [themes](https://github.com/zedeus/nitter/tree/master/public/css/themes). Just
copy the CSS file and replace `twitter.css` in the `index.html` with the theme
of your choice.
