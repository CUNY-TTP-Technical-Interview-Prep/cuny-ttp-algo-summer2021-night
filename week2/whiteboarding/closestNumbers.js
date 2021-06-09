function closestNumbers(numbers) {

  // first, sort the array in ascending order   ---> time O(n log n)
  let sortedArr = numbers.sort((a, b) => a - b)

  // keep track of minimum absolute difference starting with the first two elements
  let minAbsDifference = sortedArr[1] - sortedArr[0]

  // initialize an new "returnElements" array where you store the pairs that return minimum absolute difference
  let returnElements = [sortedArr[0], sortedArr[1]] // ----> space O(n)

  // loop through given array starting at index 2 (since we already went over the first pair)
  for (let i=2; i<sortedArr.length; i++) {

    // find the difference between the value of the current element and the previous element
      let currentDifference = sortedArr[i] - sortedArr[i-1]

      // if the difference is smaller than minAbsDifference on line 7
      if (currentDifference < minAbsDifference) {

          // reassign minAbsDiffernce to current difference
          minAbsDifference = currentDifference;
          // reassign returnElements array
          returnElements = [sortedArr[i-1], sortedArr[i]]
      } else if (currentDifference === minAbsDifference) {

          // if the difference is the same as minsAbsDifference, add the pair to returnElements array
          returnElements.push(sortedArr[i-1], sortedArr[i])
      }
  }

  // loop through the returnElements array and print pairs
  for (let i=0; i<returnElements.length; i+=2) {
      console.log(returnElements[i], returnElements[i+1])
  }
}

// time O(n log n), space O(n)




