from typing import List
from collections import deque, defaultdict


class Twitter:

    # problem: How to update a user's feed when he follows someone new

    # other approach: keep data of tweets centralized in some database and
    # when a user requests the feed, fetch data from database
    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = defaultdict(lambda: deque(maxlen=10))
        self.time_stamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].appendleft((self.time_stamp, tweetId))
        self.time_stamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followers[userId].add(userId)  # make sure user follows himself

        feed = []
        used_time_stamps = set()
        for i in range(10):
            max_time_stamp = -1
            tweet = None
            for user in self.followers[userId]:
                i = 0
                while i < len(self.tweets[user]) and self.tweets[user][i][0] in used_time_stamps:
                    i += 1
                if i < len(self.tweets[user]):
                    time, tweetId = self.tweets[user][i]
                    if time > max_time_stamp:
                        tweet = tweetId
                        max_time_stamp = time

            if tweet is None:
                break

            used_time_stamps.add(max_time_stamp)
            feed.append(tweet)

        return list(feed)

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
