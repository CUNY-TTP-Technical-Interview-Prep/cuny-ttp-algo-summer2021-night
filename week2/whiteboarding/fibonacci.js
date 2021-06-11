// Tips for Interviewers --> Make sure the interviewee understands what the fibonacci sequence is. Give them some time to ask you clarifying questions. If they don't ask, provide them what a fibonacci sequnce looks like. Fibonacci Sequence looks like this --> 0, 1, 1, 2, 3, 5, 8, ...

// There are multiple ways to solve this problem. See below for two examples.

// ******************************************

// SOLUTION 1 (Iterative Approach)

// Psuedocode:

// If given n is 0 -> we can just return n
// If given n is 1 -> we can also still return n (or n + n-1)
// This is because the first two numbers in a fibonacci sequence are 0 and 1
// If given n is > 1
   // initialize two variables at the values of the first two indices of F sequence
   // create a variable to hold currentValue (which would be the sum of the first two indices)
   // until it reaches nth index, keep updating currentValue by initializing i at 2 and updating prevValA, prevValB and currentVal
// return currentValue

// Complexity Analysis

// Time complexity : O(N)O(N). Each value from 2 to N will be visited at least once. The time it takes to do this is directly proportionate to N where N is the Fibonacci Number we are looking to compute.

// Space complexity : O(1)O(1). This requires 1 unit of Space for the integer N and 3 units of Space to store the computed values (curr, prev1 and prev2) for every loop iteration. The amount of Space doesn't change so this is constant Space complexity.

const fib = function(n) {
	if (n < 2) {
	    return n;
	}
	let prevValueA = 0;
	let prevValueB = 1;
	let currentVal = prevValueA + prevValueB;
	for (let i=2; i<n; i++) {
	    prevValueA = prevValueB;
	    prevValueB = currentVal;
	    currentVal = prevValueA + prevValueB;
	}
	return currentVal;
    };

    console.log(fib(3)) // Expected Answer: 2

    // ******************************************

    // SOLUTION 2 (Recursive Approach)

    // Psuedocode:
    // Base Case -> return n if it's less than 2
    // Recursive Case -> invoke the function of the two preceding indices using recursion and return their sum

    // Complexity Analysis

    // Time complexity : O(2^N)O(2
    // N
    //  ). This is the slowest way to solve the Fibonacci Sequence because it takes exponential time. The amount of operations needed, for each level of recursion, grows exponentially as the depth approaches N.

    // Space complexity : O(N)O(N). We need space proportionate to N to account for the max size of the stack, in memory. This stack keeps track of the function calls to fib(N). This has the potential to be bad in cases that there isn't enough physical memory to handle the increasingly growing stack, leading to a StackOverflowError. The Java docs have a good explanation of this, describing it as an error that occurs because an application recurses too deeply.


    const fibRecursive = function(n) {
	if (n < 2) {
	    return n;
	}
	return fibRecursive(n-1) + fibRecursive(n-2);
    };

    console.log(fibRecursive(3)) // Expected Answer: 2

    // ******************************************
