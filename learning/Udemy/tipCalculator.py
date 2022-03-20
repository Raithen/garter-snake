from multiprocessing.sharedctypes import Value


bill_amount = float(input('What is the bill amount?'))
tip_percents = {'10%':.10, 
                '15%':.15,
                '20%':.20,
                '25%':.25
                }

for key in tip_percents:
    print(tip_percents.values())