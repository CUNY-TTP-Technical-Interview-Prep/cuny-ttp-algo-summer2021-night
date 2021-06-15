// Prompt https://leetcode.com/problems/flipping-an-image/

const flipAndInvertImage = function(image) {
	// intialize a pointer at 0
	let currentIdx = 0
	// loop through each row in the image
	for ( let currentRowIdx in image) {
	    // determine the center
	    let middle = image.length/2
	    // while your pointer hasn't arrived to the middle
	    while (currentIdx < middle) {
		// swap the values between your pointer element and the element on the opposing side
		const temp = 1 - image[currentRowIdx][currentIdx]
		image[currentRowIdx][currentIdx] = 1 - image[currentRowIdx][image.length - 1 - currentIdx]
		image[currentRowIdx][image.length - 1 - currentIdx] = temp;
		// increase your pointer
		currentIdx++;
	    }
	    // reset your pointer back to zero when you go to the next row
	    currentIdx = 0;
	}
        return image
};

// time complexity O(n)
// space complexity O(1)
