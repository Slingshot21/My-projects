#change a number of days to years,months,weeks, and days. 
n = 15443
print(f'{n//365}years,{(r:=n%365)//30} months,{r%30//7}weeks,{r%30%7}days')
