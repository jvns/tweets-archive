function sortTweets(tweets) {
    return tweets.sort(function(a,b){
            return new Date(b.created_at) - new Date(a.created_at);
    });
}
const app = Vue.createApp({
    data() {
        const tweets = sortTweets(searchDocuments);
        return {
            tweets: tweets,
            results: undefined,
            search: '',
            lastIndex: 30,
            minisearch: undefined,
        }
    },
    mounted() {
        /* make timeline visible */
        this.$refs.timeline.style.display = 'block';
        this.miniSearch = new MiniSearch({
            fields: ['full_text'], // fields to index for full-text search
            storeFields: ['full_text', 'created_at', 'id_str', 'favorite_count', 'retweet_count'],
            idField: 'id_str',
        });
        this.miniSearch.addAll(this.tweets);
        /* infinite scroll */
        window.addEventListener('scroll', () => {
            if (window.innerHeight + window.pageYOffset >= document.body.offsetHeight - 50) {
                this.lastIndex += 20;
                console.log(this.lastIndex);
            }
        });

    },
    methods: {
        currentTweets() {
            const results = (this.search) ? sortTweets(this.miniSearch.search(this.search)) : this.tweets;
            console.log("currentTweets", this.tweets.length);
            return results.slice(0, this.lastIndex);
        },
        shortDate(created_at) {
            /* if it's in the current year, jun 9, else jun 9 2022 */
            const date = new Date(created_at);
            if (date.getFullYear() === new Date().getFullYear()) {
                return date.toLocaleString('default', { month: 'short', day: 'numeric' });
            }
            return date.toLocaleString('default', { month: 'short', day: 'numeric', year: 'numeric' });
        },
        fix_full_text(item) {
            const media = item.full_text.replace(/\.\.\/\.\.\/tweets_media\//g,'b0rk/tweets_media/');
            return media;
        },
        search(event) {
            event.preventDefault();
        },
        url(item) {
            return "https://twitter.com/b0rk/status/" + item.id_str;
        },
    }
})
app.mount('#app')
