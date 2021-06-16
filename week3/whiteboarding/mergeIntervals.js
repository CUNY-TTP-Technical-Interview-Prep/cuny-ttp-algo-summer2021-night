// Leet # 56: https://leetcode.com/problems/merge-intervals/

const mergeInterval = (intervals) => {
	// if the intervals array doesn't contain any interval or only has one, return it
	if(intervals.length < 2) return intervals;

	// sort the intervals but the first value in each interval
	intervals.sort((a,b) => a[0] - b[0])

	// loop through the sorted array initializing the pointer at index 1
	for (let i = 1; i< intervals.length; i++) {

	    let current = intervals[i];
	    // create another pointer at the previous interval
	    let previous = intervals[i-1];

	    // compare the first index of the current interval is less than or equal to the second index of the previous interval, you have an overlap
	    if (current[0] <= previous[1]) {
		// change the current interval to reflect the merged interval
		intervals[i] = [previous[0], Math.max(previous[1],current[1])]

		// use the splice method to cut out the previous interval
		// Reminder: splice(start, deleteCount)
		intervals.splice(i-1, 1);

		// since the array has been shortened, decrement i to avoid skipping an interval with automatic incrementation
		i -= 1;
	    }
	}
	return intervals
};

    // time complexity --> O(n log n)

    // space complexity --> O(1)
