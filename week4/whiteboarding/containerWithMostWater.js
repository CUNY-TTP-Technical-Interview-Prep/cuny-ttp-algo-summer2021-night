const maxArea = (height) => {

	// initialize a maximum variable. this will be updated throughout
	let maximumArea = 0;
	// initialize two pointers on opposite ends of given array
	let leftLineIdx = 0;
	let rightLineIdx = height.length-1;

	// while the pointers haven't met
	while (leftLineIdx < rightLineIdx) {
	    // figure out which pointer is pointing to a shorter line since this is needed to determine area
	    let shorterSide = Math.min(height[leftLineIdx], height[rightLineIdx]);
	    // calculate area
	    let area = (rightLineIdx - leftLineIdx) * shorterSide;
	    // if the area is greater than the previous maximum area, reassign maximum area
	    if (area > maximum) maximum = area;
	    // move the pointer that's pointing to the shorter line
	    if (height[leftLineIdx] < height[rightLineIdx]) {
		leftLineIdx++;
	    } else {
		rightLineIdx--;
	    }
	}

	return maximumArea;
    };
