tests={

    'test1':{

        'callFlow':[

            "This is first line",

            "This is second line",

            "This is third line"

        ]

    },

    'test2':{

        'callFlow':[

            "This is first line for test2",

            "This is second line for test2",

            "This is third line for test2"

        ]

    }

}



BREAK_TIME=5



import md5

import time

import sys



messageHash=dict()

for test in tests:

    tests[test]["hash"]=list()

    tests[test]["expect"]=0

    tests[test]["it"]=0

    for callflow in tests[test]['callFlow']:

        val=md5.new(callflow).digest()

  tests[test]["hash"].append(val)            

        try:

            messageHash[val].append(test)

#            tests[test]["hash"].append(val)            

        except (KeyError,NameError) as e:

            messageHash[val] = list()

#            tests[test]["hash"]=list()

#            tests[test]["expect"]=0

#            tests[test]["hash"].append(val)

            messageHash[val].append(test)



#print messageHash

#print tests        

#reading and processing log file starts here





f = open(sys.argv[1], 'r')

count=0

while True:

    rline = f.readline()

    if not rline:

    	if count <BREAK_TIME:

        	time.sleep(1)

        	count+=1

        else:

        	print "Halting Analyzer: No updates in last "+str(count)+" seconds...."

        	break; 

    else:

    	count=0

        line=rline.rstrip().lstrip()

#        print line

        lineHash = md5.new(line).digest()

#        print lineHash

        try:

            testList=messageHash[lineHash]

#            print testList

            for test in testList:

                hNum=tests[test]["expect"]

                if lineHash==tests[test]["hash"][hNum]:

                	if hNum==len(tests[test]['callFlow'])-1:

                		tests[test]['it']+=1

                		print "Completed "+str(tests[test]['it'])+" iteration of test:"+test

                		tests[test]["expect"]=0

                	else:

                		tests[test]["expect"]+=1

                else:

                	print "Cought call flow out of sequence:"+test

                	

                	

        except KeyError:

        	pass
