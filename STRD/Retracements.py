 
#retrace identifying tool
    
# using a beginning and an ending prices of a move we determine potential correction retraces (zig-zag stuff)

# 1/3, 1/2, 2/3 retraces

# • 1/3 is a potential opportunity to buy in bull and sell in bear, a signal to keep an eye out on the direction
# after this point

# • 1/2 most often need to buy in bull sell in bear. 

# ***HLAVING RULE*** 
# Consider selling a portion of a stock if the price doubles in value. Consider buying stock that has lost half 
# of its value (and not half the difference like retrace)


# • 2/3 the "extreme" cases, signals potential trend reversal

# most often the retrace happens around the 50% mark
   
   
   
   
   
   
def Retracement(orig, end): 
    
    
    
    if orig < end:
        thr = (end-orig)/3
        twThr = (end-orig)*(2/3)
        third = end - thr
        twoThird = end - twThr
        
        retrList = [
        "•           •            •            •            •            •            •            •            •            •            •","",
        "The Trend is BULLISH!","","",
        "ONE THIRD Retrace is: " + str(third) + "    <--- Potential buying point. [GOOD ALERT]","","",
        "ONE HALF Retrace is: " + str((orig + end)/2) + "    <--- Price will fall to this point before resuming its advance. [BUY]","","",
        "TWO THIRD Retrace is: " + str(twoThird) + "    <--- New SUPPORT. If this SUPPORT breaks expect a trend reversal. [WATCH OUT]","",
        "•           •            •            •            •            •            •            •            •            •            •"]
    
        print(*retrList,sep='\n')
        
    else:
        thr = (orig - end)/3
        twThr = (orig - end)*(2/3)
        third = end + thr
        twoThird = end + twThr
        retrList = [
        "•           •            •            •            •            •            •            •            •            •            •","",
        "The Trend is BEARISH!","","",
        "ONE THIRD Retrace is: " + str(third) + "    <--- Potential selling point. [WATCH OUT, MIGHT DECREASE SOON]","","",
        "ONE HALF Retrace is: " + str((orig + end)/2) + "    <--- Price will rise to this point before resuming its decline. [SELL!!]","","",
        "TWO THIRD Retrace is: " + str(twoThird) + "    <--- New RESISTANCE. If this SUPPORT breaks expect a trend reversal. [GOOD ALERT!]","","",
        "•           •            •            •            •            •            •            •            •            •            •"]

        print(*retrList,sep='\n')
    
orig = int(input("Input beginning price of the move: "))   
end = int(input("Input ending price of the move: "))  

res = Retracement(orig,end)

print(res)