# 只有一次買賣(BestTimeWithOneChoice.py)
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie,
buy one and sell one share of the stock), design an algorithm to find the maximum profit.

問題：

假設你有一個陣列，該陣列第 i 個元素代表第 i 天股票的價格，並且你指有一次買賣的機會，請設計一個演算法求得最大的力論為何？

例子

股市 = {3, 2, 6, 5, 0, 3},
則最大利潤為 4 (第二天買進 第三天賣出)
股市 = { 2, 1 },
則最大利潤為 0 (因為買了一定賠)

REFERENCE<br>
itHelp, pajace2001, 股市中最佳買賣時機-I<br>
http://ithelp.ithome.com.tw/articles/10157884

# 多次買賣(BestTimeWithMultiChoice.py)
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like

(ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple

transactions at the same time (ie, you must sell the stock before you buy again).

Thinking:
stock = [1, 2, 3, 4, 5, 6]
 
6                *
5             *  1
4          *  1  2    => Max Profit = (5, 5)
3       *  1  2  3                  = (4, 5) + (5, 4)
2    *  1  2  3  4                  = (3, 5) + (4, 4) + (5, 3)
1 *  1  2  3  4  5                  = (4, 4) + (3, 3) + (5, 5)
  1  2  3  4  5  6

stock = [1, 5, 3, 6, 3, 2, 7, 4]
  
4                      *
7                   *  *
2                *  5  2     => Max Profit = (7, 7)
3             *  *  4  1                   = (6, 7)
6          *  *  *  1  *                   = (6, 7) + (7, 5) 
3       *  3  *  *  4  1                   = (6, 7) + (7, 5) + (3, 6) 
5    *  *  1  *  *  2  *                   = (1, 7) + (6, 2) + (3, 5) + (7, 3)
1 *  4  2  5  2  1  6  3                   = 4      + 5      + 3      + 1
  1  5  3  6  3  2  7  4                   = 13
  
REFERENCE<br>
itHelp, pajace2001, 股市中最佳買賣時機-II<br>
http://ithelp.ithome.com.tw/articles/10158073<br>
[註] 這邊的寫法和理解與原po有點不同
