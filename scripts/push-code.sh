set -eu
git branch -D dns-weekend-book || true
git subtree split --prefix=book --branch dns-weekend-book
git push git@github.com:jvns/dns-weekend.git dns-weekend-book:master
