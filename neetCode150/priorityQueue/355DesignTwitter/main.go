package main

import (
	"container/heap"
	"fmt"
)

func main() {
	t := Constructor()
	t.PostTweet(1, 5)
	t.GetNewsFeed(1)
	t.Follow(1, 2)
	t.PostTweet(2, 6)
	t.GetNewsFeed(1)
	t.Unfollow(1, 2)
	t.GetNewsFeed(1)

	fmt.Println("----------------")
	t = Constructor()
	t.PostTweet(2, 5)
	t.Follow(1, 2)
	t.Follow(1, 2)
	t.GetNewsFeed(1)

	fmt.Println("----------------------")
	// ["Twitter","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","getNewsFeed"]
	// [[],[1,5],[1,3],[1,101],[1,13],[1,10],[1,2],[1,94],[1,505],[1,333],[1,22],[1,11],[1]]
	t = Constructor()
	t.PostTweet(1, 5)
	t.PostTweet(1, 3)
	t.PostTweet(1, 101)
	t.PostTweet(1, 13)
	t.PostTweet(1, 10)
	t.PostTweet(1, 2)
	t.PostTweet(1, 94)
	t.PostTweet(1, 505)
	t.PostTweet(1, 333)
	t.PostTweet(1, 22)
	t.PostTweet(1, 11)
	t.GetNewsFeed(1)

	// Posting tweets
	t = Constructor()
	t.PostTweet(1, 5)
	t.PostTweet(2, 3)
	t.PostTweet(1, 101)
	t.PostTweet(2, 13)
	t.PostTweet(2, 10)
	t.PostTweet(1, 2)
	t.PostTweet(1, 94)
	t.PostTweet(2, 505)
	t.PostTweet(1, 333)
	t.PostTweet(2, 22)
	t.PostTweet(1, 11)
	t.PostTweet(1, 205)
	t.PostTweet(2, 203)
	t.PostTweet(1, 201)
	t.PostTweet(2, 213)
	t.PostTweet(1, 200)
	t.PostTweet(2, 202)
	t.PostTweet(1, 204)
	t.PostTweet(2, 208)
	t.PostTweet(2, 233)
	t.PostTweet(1, 222)
	t.PostTweet(2, 211)
	t.GetNewsFeed(1)
	t.Follow(1, 2)
	t.GetNewsFeed(1)
	t.Unfollow(1, 2)
	t.GetNewsFeed(1)
}

// If each user has a feed cache then it is push-based => store list of follower to push tweets
// If each user generate feed on then it is pull-based => store list of followee to get tweets
// A lot of follower, write more -> pull based
// A lot of followee, read more -> push based
// When unfollow user must pull more tweets

// PUSH BASED SOLUTION
const (
	feedSize = 10
)

type Twitter struct {
	now      uint
	userBase map[int]*user //userId to user
}

func Constructor() Twitter {
	return Twitter{
		now:      1,
		userBase: make(map[int]*user),
	}
}

func (t *Twitter) PostTweet(userId int, tweetId int) { // O(log(feedSize)*#followers)
	if t.userBase[userId] == nil {
		t.userBase[userId] = newUser(userId)
	}
	u := t.userBase[userId]

	tw := tweet{
		id:     tweetId,
		author: userId,
		epoch:  t.now,
	}
	// add to user tweet list
	u.tweets = append(u.tweets, tw)

	// Push tweet to follower
	for k := range t.userBase[userId].followers {
		if len(t.userBase[k].feeds) >= feedSize {
			heap.Pop(&t.userBase[k].feeds)
		}
		heap.Push(&t.userBase[k].feeds, tw)
	}

	t.now++
}

func (t *Twitter) GetNewsFeed(userId int) []int {
	u := t.userBase[userId]
	if u == nil {
		return []int{}
	}

	temp := make(MinHeap, u.feeds.Len())
	res := make([]int, u.feeds.Len())
	copy(temp, u.feeds)
	for temp.Len() > 0 {
		res[temp.Len()-1] = heap.Pop(&temp).(tweet).id
	}
	fmt.Println(len(res))
	fmt.Println(res)
	return res
}

func (t *Twitter) Follow(followerId, followeeId int) { //O(feedSize * log(feedSize))
	// Check if user exists
	if t.userBase[followeeId] == nil {
		t.userBase[followeeId] = newUser(followeeId)
	}
	if t.userBase[followerId] == nil {
		t.userBase[followerId] = newUser(followerId)
	}
	follower := t.userBase[followerId]
	followee := t.userBase[followeeId]
	// If already follow abort pushing
	_, ok1 := followee.followers[followerId]
	_, ok2 := follower.followees[followeeId]
	if ok1 && ok2 {
		return
	}
	// Add followee
	followee.followers[followerId] = struct{}{}
	follower.followees[followeeId] = struct{}{}
	// Add followee's tweets
	for i := len(followee.tweets) - 1; i >= 0; i-- {
		if follower.feeds.Len() < feedSize {
			heap.Push(&follower.feeds, followee.tweets[i])
			continue
		}
		if follower.feeds[0].epoch < followee.tweets[i].epoch {
			heap.Pop(&follower.feeds)
			heap.Push(&follower.feeds, followee.tweets[i])
			continue
		}
		break
	}
}

func (t *Twitter) Unfollow(followerId, followeeId int) { //O(#followee*feedSize)
	if t.userBase[followeeId] == nil {
		return
	}
	if t.userBase[followerId] == nil {
		return
	}
	follower := t.userBase[followerId]
	followee := t.userBase[followeeId]

	delete(followee.followers, followerId)
	delete(follower.followees, followeeId)

	// regenerate feed of follower O(#followee*feedSize)
	newFeed := make(MinHeap, feedSize)
	ff := follower.followees
	ps := make([]struct{ f, i int }, 0, len(follower.followees)) // index to followee tweets
	for k := range ff {
		ps = append(ps, struct {
			f int
			i int
		}{
			f: k,
			i: len(t.userBase[k].tweets) - 1,
		})
	}
	i := 9
	for !allNegative(ps) && i >= 0 {
		minId := -1
		var mrEpoch uint // most recent epoch
		for i := range ps {
			if ps[i].i < 0 {
				continue
			}
			if t.userBase[ps[i].f].tweets[ps[i].i].epoch > mrEpoch {
				minId = i
				mrEpoch = t.userBase[ps[i].f].tweets[ps[i].i].epoch
			}
		}
		if minId == -1 {
			break
		}
		newFeed[i] = t.userBase[ps[minId].f].tweets[ps[minId].i]
		i--
		ps[minId] = struct {
			f int
			i int
		}{
			f: ps[minId].f,
			i: ps[minId].i - 1,
		}
	}
	follower.feeds = newFeed[i+1:]
}

func allNegative(ps []struct{ f, i int }) bool {
	for _, p := range ps {
		if p.i >= 0 {
			return false
		}
	}
	return true
}

type user struct {
	id        int
	feeds     MinHeap
	tweets    []tweet
	followers map[int]struct{} // who follow this user
	followees map[int]struct{} // who this user follows
}

func newUser(uid int) *user {
	return &user{
		id:        uid,
		feeds:     make(MinHeap, 0, feedSize),
		tweets:    make([]tweet, 0),
		followers: map[int]struct{}{uid: {}},
		followees: map[int]struct{}{uid: {}},
	}
}

type tweet struct {
	id     int
	author int
	epoch  uint
}

// more recent > higher epoch => Min heap
type MinHeap []tweet

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i].epoch < h[j].epoch }
func (h MinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MinHeap) Push(x any) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(tweet))
}

func (h *MinHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}
