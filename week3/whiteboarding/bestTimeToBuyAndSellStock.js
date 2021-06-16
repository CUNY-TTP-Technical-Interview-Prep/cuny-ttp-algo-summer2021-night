// Leet # 121: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

const maxProfit = (prices) => {
	// initialize maxProfit at 0 and local lowest price at the first price in the array
	let maxProfit = 0;
	let localLowestPrice = prices[0];
	// loop through the prices
	for (let i=0; i<prices.length; i++) {
	    let currentPrice = prices[i]
	    // if your current price is less than the lowest price, reassign local lowest price to current price
	    if (currentPrice < localLowestPrice) {
		localLowestPrice = currentPrice
	    // otherwise, check to see if the difference between current price and the local lowest price is greater than maxProfit
	    } else if (currentPrice - localLowestPrice > maxProfit) {
		// if yes, update your maxProfit to that difference
		maxProfit = currentPrice - localLowestPrice;
	    }
	}
	return maxProfit;
};
