#!/bin/sh

awk 'BEGIN {FS = ","} {print "\"created\":\""$1"\",\"score\":\""$2"\",\"domain\":\""$3"\",\"reddit_id\":\""$4"\",\"title\":\""$5"\",\"author\":\""$6"\",\"ups\":\""$7"\",\"downs\":\""$8"\",\"comment_count\":\""$9"\",\"permalink\":\""$10"\",\"thumbnail\":\""$11"\",\"subreddit_id\":\""$12"\",\"edited\":\""$13"\",\"is_self\":\""$14"\",\"name\":\""$15"\",\"url\":\""$16"\"" > "EDM.json"
}' EDM.txt
