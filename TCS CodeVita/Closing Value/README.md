Stock Exchange of country XYZ is still working on pen paper mode, wherein the traders have to bid the price for buying and selling the stocks and the stocks prices are checked manually, then the buying and selling data is validated and if the condition matches then it is recorded in the record book. For example, if A wants to buy stocks at 100 and B is willing to sell the required stocks at 95, then A can buy his desired share at 95 and the price of the share will become 95. The price of shares of a company is determined by the latest transaction recorded in the record book.

As the number of transactions are increasing it is getting hard to match and record the transactions manually.

The stock exchange wants to go online and has hired Karim to make the process online. The stock exchange personnel will give him the bid and he has to design a program to match the values and if the transaction is done, then record it in the record book which will also be online.

Help Karim in recording the completed transactions and enter the closing price in record book. He has to give the closing values of all the companies whose transactions have been recorded in ascending order.

In case, if more than one matching bids are received then the trader with lower TraderId will get the preference. In case only a partial match is received then it will be a split transaction. For example, consider following transaction below:

TraderId

TradeType

StockName

Price

Quantity

1

Buy

ABC

50

90

2

Buy

ABC

50

90

3

Sell

ABC

50

100

Trader 3 will sell his 90 stocks to Trader 1 at price of 50. Since Trader 3 has 10 stocks left, the remaining stocks can be purchased by Trader 2. Hence, Trader 1 and Trader 3 have squared off their positions whereas as Trader 2 has open bid for 80 stocks of ABC at a price of 5.

Here, Trader 3 had a split transaction which is closed whereas Trader 2 also had split transaction which is still open.

Constraints
0 < N <=10000

Input
First line contains an integer N, denoting the number of bids

Next N lines, each contains 5 space separated values denoting <TraderId, Tradetype, StockName, Price, Quantity>

Where,

TraderId is single integer containing the id of trader, smaller trader id indicates the timestamp of the trade

Tradetype can be either Buy/Sell

StockName is the name of the company that trader wants to bid

Price indicates the price at which the trader has bid

Quantity indicates the number of stocks trader wants to purchase/buy

Output
Lexicographically ascending order of Stock Name(S) along with respective values(C) in the format (S:C). If no company has traded the stock, then print "Stocks not traded"

Time Limit
1

Examples
Example 1

Input

3

1 Sell ABC 1876 173

2 Sell DEF 7160 221

3 Buy ABC 6986 864

Output

ABC:1876

Explanation

Here transaction of ABC is recorded but the DEF is not recorded as no one has bid to buy the stocks of DEF.

Trader with id 3 will buy 173 shares from trader with id 1 of Stock ABC at unit price of 1876. Since this becomes the closing price of ABC, output is ABC:1876

 

Example 2

Input

3

1 Sell ABC 1876 173

2 Sell DEF 7160 221

3 Buy ABC 1200 864

 

Output

Stocks not traded

 

Explanation

Since, no transaction has taken place as the buy bid is less than sell for company ABC and there is no trade to buy DEF, there is no record in the record book. Hence "Stocks not traded" will be the output.