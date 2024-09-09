package main

func main() {
	t := Constructor()
	t.PostTweet(1, 5)
	t.GetNewsFeed(1)
	t.Follow(1, 2)
	t.PostTweet(2, 6)
	t.GetNewsFeed(1)
	t.Unfollow(1, 2)
	t.GetNewsFeed(1)
}

type Twitter struct {
	// Pre-propagate user feed with post
	// When follow scan every tweets of the new followee.
	// How to remove tweets from each user feed when unfollow ?
	// follow : binary search tweet.Recency[i] <= min(recency of follower <
	tweetRecency map[int]int
	userBase     map[int]*user
}

type user struct {
	tweets    []int
	followers []int
	feeds     []int
}

func Constructor() Twitter {
	return Twitter{}
}

func (t *Twitter) PostTweet(userId int, tweetId int) {
	if t.userBase[userId] == nil {
		t.userBase[userId] = &user{
			tweets:    make([]int, 0),
			followers: make([]int, 0),
			feeds:     make([]int, 0),
		}
	}
	t.userBase[userId].tweets = append(t.userBase[userId].tweets, tweetId)
}

func (t *Twitter) GetNewsFeed(userId int) []int {
	res := make([]int, 10)
	return res
}

func (t *Twitter) Follow(followerId, followeeId int) {}

func (t *Twitter) Unfollow(followerId, followeeId int) {}
