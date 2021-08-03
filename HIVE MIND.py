import datetime

class hivemind:
    class mind:
        class neurone:
            def __init__(self,name,resistance=0,accelerate=0.999,brake=0.999,bayeslearningrate=10):
                import random
                self.learningrate={}
                self.bayeslearningrate=bayeslearningrate
                self.inputs={}
                self.bias={}
                self.bayesbias={}
                if isinstance(resistance,str):
                    self.resistance=ramdom.random()
                else:
                    self.resistance=resistance
                self.pain=2
                self.fired=[]
                self.name=name
                self.temp={}
                self.me=0
                self.accelerate=accelerate
                self.brake=brake

            def forward(self,imp={},bayes={},error=0):
                import random
                a=0
                c=0
                for i in bayes:
                    if i in self.bayesbias:
                        try:
                            c+=(self.bayesbias[i]*bayes[i])
                        except Exception as ex:
                            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                            message = template.format(type(ex).__name__, ex.args)
                            print(message)
                            print(c)
                            print(self.bayesbias[i])
                            print(bayes[i])
                            print(i)
                            print(bayes)
                            input("pause in forward")
                    else:
                        if error==2:
                            print(i)
                            print(self.bayesinputs)
                            
                            input("pause")
                        self.bayesbias[i]=random.random()
                        self.learningrate[i]=random.random()
                        c+=self.bayesbias[i]
                c=self.outputactivation(c)
                if error==1:
                    print(self.name)
                    print(c)
                    input()
                
                if c > self.resistance or self.name=="output":
                    a=0
                    for i in imp:
                        if i in self.bias:
                           a+=(self.bias[i]*imp[i])
                        else:
                            self.bias[i]=random.random()
                            
                    a=self.outputactivation(a)

                    
                    self.fired=imp
                    
                    self.pain=a
                    return [self.name,a,c]
                else:
                    return []

            def backwards(self,actual,estimate,lisp,error=0):

                import random

                if self.name in lisp or self.name=='output':

                    if len(self.fired)>0:
                        a=0
                        c=actual-abs(estimate)
                        d=estimate/actual
                        e=0

                        if c > 0:
                            if self.pain < 0:
                                if actual >0:
                                    sel=0
                                else:
                                    sel=1
                            else:
                                sel=1
                        else:
                            if self.pain < 0:
                                if actual >0:
                                    sel=1
                                else:
                                    sel=0
                            else:
                                sel=0

                        for i in self.fired:
                            if i in self.temp:
                                if sel==1 and self.temp == 1:
                                    self.learningrate[i]=self.learningrate[i]*self.accelerate
                                else:
                                    self.learningrate[i]=self.learningrate[i]*self.brake
                    
                            #self.temp[i]=c
                                    
                                    
                        try:
                            if c>0:
                                for i in self.fired:
                                    self.bias[i]+=self.learningrate[i]
                                    self.bayesbias[i]+=(self.learningrate[i]/self.bayeslearningrate)
                                    self.temp[i]=sel

                            else:
                                for i in self.fired:
                                    self.bias[i]-=self.learningrate[i]
                                    self.bayesbias[i]-=(self.learningrate[i]/self.bayeslearningrate)
                                    self.temp[i]=sel


                        except Exception as ex:
                            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                            message = template.format(type(ex).__name__, ex.args)
                            print(message)
                            print(self.fired)
                            print(i)
                            input("Error in backwards")

                        temp=self.fired.copy()
                        self.fired=[]

                        return temp

                

                #mind needs to take the reply and group all the returns and then feed into next row.
                #if mind gets a empty dict back for whole line then it needs to cycle through neurones and top up the bayes dict

            def nonresponse(self,estimate):
                import random
                for i in estimate:
                    if i !=self.name:
                        if i in self.bayesbias:
                            self.bayesbias[i]+=1
                        else:
                            self.bayesbias[i]=random.random()+1
                            self.learningrate[i]=random.random()
            def experience(self):
                self.accelerate-=0.00000001
                self.brake-=0.00000001
                if self.brake<0.00000001:
                    self.brake=0.00000001
                if self.accelerate < 1.00000001:
                    self.accelerate=1.00000001
            def reset(self):
                self.fired=[]

        class Relu:
            def outputactivation(self,x):
                if x > 0:
                    return x
                else:
                    return (x*0.1)
                return 1 / (1 + math.exp(-x))

        class Sigmoid:
            def outputactivation(self,x):
                import math
                return 1 / (1 + math.exp(-x))

        class Tanh:
            def outputactivation(self,x):
                import math
                x=math.tanh(x)
                return x
            
        class sigmoidneurone(Sigmoid,neurone):
            pass
        
        class reluneurone(Relu,neurone):
            pass
        
        class tanhneurone(Tanh,neurone):
            pass

        def __init__(self,width,depth,repeat=0,resistance=0,bayeslearningrate=10,linearegression=0):
            self.outputbias={}
            self.mind=[]
            self.source=[]
            self.fired={}
            self.repeat=repeat
            self.me=0
            self.critime={}
            self.resistance=resistance
            c=0


            
            for i in range(depth):
                cortex=[]
                for w in range(width):
                    c+=1
                    name=str("No:"+str(c)+" row:"+str(i)+" width:"+str(w))
                    cortex.append(self.reluneurone(name,resistance=resistance,bayeslearningrate=bayeslearningrate))
                    if linearegression==1:
                        name='output'
                        self.output=self.reluneurone(name,resistance=0,bayeslearningrate=bayeslearningrate)
                self.mind.append(cortex.copy())
            name='output'
            self.output=self.reluneurone(name,resistance=0,bayeslearningrate=bayeslearningrate)

        def labotomy(self,width=[4,4,4,4,4],typo=['r','r','r','r','r','r'],resistance=[0,0,0,0,0,0],bayeslearningrate=[10,10,10,10,10],linearegression=[0,0,0,0,0]):
            count=0
            work=4
            self.mind=[]
            rest=0
            bayes=10
            c=0

            for i in range(len(typo)):
                try:
                    work=width[count]
                    rest=resistance[count]
                    bayes=bayeslearningrate[count]
                except:
                    pass
                cortex=[]
                
                for w in range(work):
                    c+=1
                    name=str("No:"+str(c)+" row:"+str(i)+" width:"+str(w))
                    if typo[i].lower()=='r':
                        cortex.append(self.reluneurone(name,resistance=resistance,bayeslearningrate=bayeslearningrate))

                    if typo[i].lower()=='s':
                        cortex.append(self.sigmoidneurone(name,resistance=resistance,bayeslearningrate=bayeslearningrate))

                    if typo[i].lower()=='t':
                        cortex.append(self.tanhneurone(name,resistance=resistance,bayeslearningrate=bayeslearningrate))
                    
                if linearegression[i].lower()==1:
                    name='output'
                    self.output=self.reluneurone(name,resistance=resistance,bayeslearningrate=bayeslearningrate)
                self.mind.append(cortex.copy())
                count+=1
            name='output'
            self.output=self.reluneurone(name,resistance=resistance,bayeslearningrate=bayeslearningrate)
                
        def forwardpage(self,inputs,error=0):
            output=0
            nay={}
            bay={}
            responsenay={}
            responsebay={}
            for i in inputs:
                if isinstance(i,(int,float)):
                    nay[i]=i
                    bay[i]=i                   
                else:
                    nay[i]=1
                    bay[i]=1

            if error==2:
                print(inputs)

            for cortex in range(len(self.mind)):
                responsenay={}
                responsebay={}
                for nerve in self.mind[cortex]:
                    response=nerve.forward(nay,bay)
                    if len(response) >0:
                        responsenay[response[0]]=response[1]
                        responsebay[response[0]]=response[2]
                if len(responsenay)==0:
                    for nerve in self.mind[cortex]:
                        nerve.nonresponse(bay)
                if error==2:
                    print(responsenay)
                    print(responsebay)
                    input("pause error 2 at forward page")
                nay=responsenay
                bay=responsebay


            response=self.output.forward(nay,bay)

            if len(response)==0:
                self.output.nonresponse(bay)
                self.output.nonresponse(bay)
            else:
                output=response[1]

                return output
        def slow(self):
            for cortex in range(len(self.mind)):
                for nerve in self.mind[cortex]:
                    nerve.experience()


        def backapage(self,actual,estimate,error=0):
            nex=[]
            r=[]
            if estimate==None:
                estimate=0
            nex=self.output.backwards(float(actual),float(estimate),[])
            #print(nex)
            #input()
            for cortex in reversed(self.mind):
                for nerve in cortex:
                    try:
                        response=nerve.backwards(float(actual),float(estimate),nex)
                        for re in response:
                            if not re in r:
                                r.append(re)
                    except Exception as ex:  
                        pass
                nex=r
                #print(nex)
                #input("Previous Rows")
                
            self.fired=0

        def learnbook(self,reader,element,accuracy=30,epochs=10,error=0,key=0,SECONDREAD=0):
            estimate=0
           lastcount=1
            count=1
            rightcount=0
            mike=0
            check=0
            for row in reader:
                if row.get(element):
                    
                    project_list=list(row.values())
                    project_list.remove(row.get(element))
                    estimate=self.forwardpage(project_list)
                    self.backapage(row.get(element),estimate)
            
            step=0
            temp=0
            while step < epochs:
                lastcount=rightcount
                consider=[0,0,0,0,0,0,0,0,0,0,0,0,0]
                count=1
                
                for row in reader:

                    if row.get(element):
                        count+=1
                        project_list=list(row.values())
                        if key !=0:
                            project_list.remove(row.get(key))
                        project_list.remove(row.get(element))
                        estimate=self.forwardpage(project_list)
                        if row.get(element) !=0:
                            self.backapage(row.get(element),estimate)

                        if error==1:
                            print(estimate)
                            print(row.get(element))
                            input("pause for error in learnbook")
                        try:
                            temp=int(round(abs(estimate-row.get(element))/accuracy,0))
                        except:
                            pass
                        try:
                            consider[temp]+=1
                        except Exception as ex:  
                            pass

                        if error==1:
                            print(project_list)
                            print(row.get(element))
                            print(estimate)
                            print(lastcount)
                            input("pause error 1 in learnbook")

                cumu=0
                rightcount=consider[0]/count
                if rightcount <check:
                    self.slow()
                check=rightcount
                for i in range(len(consider)):
                    cumu+=((consider[i]/count)*100)
                    #print("Within a accuracy " + str(i) + " we had a accuracy of " + str((consider[i]/count)*100) + " with cumulatve of " + str(cumu))
                step+=1
                #print("New Epoch " + str(step))
            if isinstance(SECONDREAD,list):
                for row in SECONDREAD:
                    project_list=list(row.values())
                    project_list.remove(row.get(element))
                    if key !=0:
                        project_list.remove(row.get(key))
                    estimate=self.forwardpage(project_list)
                    #if estimate < accuracy:
                    #    estimate=accuracy
                    if error==2:
                        print(row)
                        print(project_list)
                        input("Error 2 in learnbook")
                    try:
                        row["ESTIMATE"]=round(estimate,0)
                    except:
                        row["ESTIMATE"]="None response from AI, unrecognised engram - pleaser forecast manually"                                                    
                        
                    
                return SECONDREAD

        def prognosticate(self,reader,key,element):

            newreader=[]

            for row in reader:
                newrow={}
                project_list=list(row.values())
                project_list.remove(row.get(element))
                estimate=self.forwardpage(project_list)
                if estimate < 30:
                    estimate=30
                for cortex in reversed(self.mind):
                    for nerve in cortex:
                        nerve.reset()
                estimate=round(estimate,0)
                newrow[key]=row[key][-(len(row[key])-(len(key)+1)):]
                newrow[str(element)+" Estimate"]=estimate
                newreader.append(newrow.copy())

            return newreader

        def testday(self,reader,accuracy,element,key=0):

            newreader=[]
            step=0
            count=0
            eva=0
            eve=0
            errors=0

            checkframe=[]
            fileframe=[]
            column=0
            row=0

            for row in reader:
                try:
                    eve+=row.get(element)
                    count+=1
                except:
                    print(row)
                    print(row.get(element))
                    input("error in testday")

            try:
                average=eve/count
            except:
                average=0
            eve=0
            count=0
            var=0
            hypo=0

            for row in reader:
                count+=1
                newrow={}
                project_list=list(row.values())
                project_list.remove(row.get(element))
                if key !=0:
                    project_list.remove(row.get(key))
                estimate=self.forwardpage(project_list)
                try:
                    eva=estimate-row.get(element)
                except:
                    errors+=1
                
                if abs(eva) < accuracy:
                    step+=1
                var=abs(row.get(element)-average)

                hypo+=(var*var)
                eve+=(eva*eva)
                for cortex in reversed(self.mind):
                    for nerve in cortex:
                        nerve.reset()
            try:
                return [(step/count),(eve/count),errors,hypo/count,]
            except:
                return [0,0,errors,0,]

    def __init__(self,reader,key,startdate,endate,renamekey,start=1,accuracy=15,csvloci=r'C:\CSVs\\',setcritdelay=14,setalert=0,taskmove=1,setpercntile=0.95,setdependency=1):
        
        self.source=[]
        self.innaccurate=[]
        self.accuraccy=accuracy
        self.key=key
        self.uPDATE=0
        self.renamekey=renamekey
        self.startdate=startdate
        import os
        directory=csvloci+'Analysis\\'
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
            except OSError:
                print ('Error: Creating directory. ' +  directory) 

        self.csvloci=directory

        directory=csvloci+'BrainsInAJar\\'
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
            except OSError:
                print ('Error: Creating directory. ' +  directory) 

        self.geniusloci=directory

        directory=csvloci+'Analysis\\'
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
            except OSError:
                print ('Error: Creating directory. ' +  directory) 

        self.analysisloci=directory

        directory=csvloci+'HIVE\\'
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
            except OSError:
                print ('Error: Creating directory. ' +  directory) 

        self.hiveloci=directory
        
        self.enddate=endate
        self.hive(reader,startdate)
        if start!=0:
            if start=="test":
                self.randomdata()
            else:
                self.swarm()
            #self.workplanner()                

    def run(self,reader,queenme=0):

        if len(self.deps)==0:
            try:
                self.deps=self.Open(file_Name=self.geniusloci + '\DEPENDENCIES_FILE')
                if self.deps==False:
                    self.deps={}
            except:
                self.deps={}
            try:
                self.tickboxes=self.Open(file_Name=self.geniusloci + '\TICKBOX_FILE')
                if self.tickboxes==False:
                    self.tickboxes={}
            except:
                self.tickboxes={}
            try:
                self.alerts=self.Open(file_Name=self.geniusloci +'\ALERT_FILE')
                if self.alerts==False:
                    self.alerts={}
            except:
                self.alerts={}
            try:
                self.critime=self.Open(file_Name=self.geniusloci +'\CRITIME_FILE')
                if self.critime==False:
                    self.critime={}
            except:
                self.critime={}
            try:
                self.hardforward=self.Open(file_Name=self.geniusloci+'\HARD_FILE')
                if self.hardforward==False:
                    self.hardforward={}
            except:
                self.hardforward={}

        self.hive(reader,self.startdate)
        x = threading.Thread(target=self.swarm, args=(self.startdate))
        x.start()
        q = threading.Thread(target=self.reforecast, args=())
        q.start()
        if queenme==1:
            queeme=threading.Thread(target=self.queen, args=())
            queeme.start()

    def reference(self):
        print("Building the Hive")
        print("this is the dates i have found")
        print(self.dates)
        print(len(self.dates))
        print("this is the labels i have found")
        print(self.kill)
        print(len(self.kill))
        print("this is the numbers i have found")
        print(self.numbers)
        print(len(self.numbers))
            
        
    def hive(self,reader,startdate,error=0):

        def inreader(row,reader,key):
            count=0
            for newrow in reader:
                if row[key]==newrow[key]:
                    return count
                count+=1
        
            return False

        def addrow(row,startdate):
            newrow={}
            newrow["end"]=row[self.enddate]
            newrow[self.key]=row[self.key]
            newrow[startdate]=row[startdate]
            datarea={}
            for d in self.dates:
                temp=self.tryfindcmrdates(newrow[startdate],row[d])
                try:
                    if temp > 0:
                        dateme[d]=1
                except:
                    pass
                datarea[d]=self.tryfindcmrdates(newrow[startdate],row[d])
            #print(datarea.copy())
            #input()
            newrow["Dates"]=datarea.copy()
            datarea={}
            for n in self.numbers:
                try:
                    if isinstance(float(row[n]),(float,int)):
                        datarea[n]=float(row[n])
                    else:
                        datarea[n]=None
                except:
                    datarea[n]=None
                    pass
            newrow["Numbers"]=datarea.copy()
            for k in self.kill:
                if k in row:
                    if isinstance(row[k],str):
                        if not self.isdate(row[k]):
                            if not len(row[k])==0:
                                if error==1:
                                    print(row[self.key])
                                    print(k)
                                    input(row[k])
                                datarea[k]=str(k)+':' +str(row[k])
            newrow["Labels"]=datarea.copy()
            if row[self.key] in tempforecastdates:
                newrow["Forecast Dates"]=tempforecastdates[row[self.key]]
                del tempforecastdates[row[self.key]]
            else:
                newrow["Forecast Dates"]={}
            if row[self.key] in tempforecastnumbers:
                newrow["Forecast Numbers"]=tempforecastnumbers[row[self.key]]
                del tempforecastnumbers[row[self.key]]
            else:
                newrow["Forecast Numbers"]={}
            newrow["Reforecast Dates"]={}
            newrow["Overide Dates"]={}
            newrow["Overide Numbers"]={}
            return newrow


        if len(self.source)==0:
            tech=[]

            self.dates=[]
            self.numbers=[]
            self.kill=[]

            tempforecastdates={}
            tempforecastnumbers={}

            for s in self.source:
                tempforecastdates[s[self.key]]=s["Forecast Dates"]
                tempforecastnumbers[s[self.key]]=s["Forecast Numbers"]

            for row in reader:
                for cell in row:
                    if self.isdate(row[cell]) and cell !=self.key and cell !=startdate:
                        if not cell in self.dates:
                            self.dates.append(cell)
                    try:
                        if isinstance(float(row[cell]),(float,int)):
                            if cell !=self.key and cell !=startdate:
                                if not cell in self.numbers:
                                    self.numbers.append(cell)
                    except:
                        pass
                    if isinstance(row[cell],str) and cell !=self.key and cell !=startdate:
                        if not isinstance(row[cell],(float,int)):
                            if not cell in self.kill:
                                self.kill.append(cell)
        


            now=''
            now=self.today
            for row in reader:
                tech.append(addrow(row,self.startdate))

            self.source=tech
        else:
            temp=[]
            for row in reader:
                temp=inreader(source,self.source,self.key)
                if temp==False:
                    self.source.append(addrow(row,now))
                else:
                    for d in self.dates:
                        self.source[temp]["Dates"][d]=row[d]
                    for n in self.numbers:
                        self.source[temp]["Numbers"][n]=row[n]
                    for k in self.kill:
                        self.source[temp]["Labels"][k]=row[k]
                        
    def swarm(self,error=0):
        
        print("Forecasting Dates")
        for d in self.dates:
            tempreader=[]
            otherereader=[]
            for row in self.source:
                
                if not d in row["Labels"]:
                    newrow={}
                    newrow["TARGET"]=row["Dates"][d]
                   
                    for k in row["Labels"]:
                        if k !=d:
                            newrow[k]=row["Labels"][k]
                    newrow[self.key]=row[self.key]
                    if newrow["TARGET"]==None:
                        otherereader.append(newrow.copy())
                    else:
                        if newrow["TARGET"] < 0:
                            newrow["TARGET"]=0
                        tempreader.append(newrow.copy())
                    
                elif error==1:
                    print(row[self.key])
                    print(d)
                    input()
            #print(d)
            #self.timestamp()
            #print(len(tempreader))
            #print(len(otherereader))

            #try: 
            r2=[]
            #print(d)
            STRING=d.replace('/','-')
            mymind=self.Open(file_Name=self.geniusloci + '\prognostication' + STRING + '_BRAININAJAR')
            if mymind==False:
                mymind=self.mind(4,5)
                epo=1
            else:
                epo=1
            r2=mymind.learnbook(tempreader,"TARGET",accuracy=self.accuraccy,epochs=epo,key=self.key,SECONDREAD=otherereader)

        
            for row in self.source:
                row=self.updaterow(row,r2,self.key,d)
            
            self.Save(mymind,file_Name=self.geniusloci + '\prognostication' + STRING + '_BRAININAJAR')
            self.csvwrite(r2,CSV=self.hiveloci + '\prognostication' + STRING + '_OUTPUT.csv',KEY=self.key,NEWKEY=self.renamekey)

            csv=[]
            #print(self.csvloci+'\Test_Records_' + STRING + '_OUTPUT.csv')
            csv=self.csvopen(x=(self.csvloci+'\Test_Records_' + STRING + '_OUTPUT.csv'))
            vale=mymind.testday(tempreader,self.accuraccy,"TARGET",key=self.key)
            data={}
            data["Type"]=d
            data["Accuraccy"]=vale[0]
            data["Loss Function"]=vale[1]
            data["Date"]=self.today()
            data["Variance Around Average"]=vale[3]
            if vale[3]==0:
                data["Hypothesis Test"]="Error in hypothesis test"
            else:
                data["Hypothesis Test"]=vale[1]/vale[3]
                if vale[1]/vale[3] > 1:
                    self.innaccurate.append(d)
                elif d in self.innaccurate:
                    self.innaccurate.remove(d)
            data["Errors"]=vale[2]

            csv.append(data)
            
            self.csvwrite(csv,CSV=self.analysisloci +'\Test_Records_' + STRING + '_OUTPUT.csv',KEY="Type",NEWKEY=0)
            
                

            #except:
             #   print(d)
              #  print("We found no instances of this to forecast, press enter too accept")
               # input()

        tempreader=[]
        LOAD=''
        concat=''
        unload=[]
        for row in self.source:
            if len(row["end"]) == 0:
                try:
                    unload=min(row["Forecast Dates"])
                except:
                    print(row["Dates"])
                    print(row["Forecast Dates"])
                    input()
  

                datarea={}
                datarea[self.key]=row[self.key]
                datarea["Next Task"]=unload
                datarea["Date"]=self.today()
                tempreader.append(datarea.copy())
            
        self.csvwrite(tempreader,CSV=self.analysisloci + 'prognostication' + '_Next_Task_' + '_OUTPUT.csv',KEY=self.key,NEWKEY=self.renamekey)
        self.uPDATE=0

        print("Forecasting Numbers")
        for d in self.numbers:
            tempreader=[]
            otherereader=[]
            for row in self.source:
                newrow={}
                newrow[self.key]=row[self.key]
                if len(row["end"])>0:
                    #print(row["Numbers"])
                    #print(row["end"])
                    #input()
                    newrow["TARGET"]=row["Numbers"][d]
                else:
                    newrow["TARGET"]=None
                for k in row["Labels"]:
                    if k !=d:
                        newrow[k]=row["Labels"][k]
                if newrow["TARGET"]==None:
                    otherereader.append(newrow.copy())
                        
                elif isinstance(newrow["TARGET"],(int,float)):
                    tempreader.append(newrow.copy())

            if len(tempreader) >0:
                #try: 
                r2=[]
                
                #print(d)
                STRING=d.replace('/','-')
                mymind=self.Open(file_Name=self.geniusloci + '\prognostication' + STRING + '_BRAININAJAR')
                if mymind==False:
                    mymind=self.mind(4,5)
                    epo=1
                else:
                    epo=1            

                r2=mymind.learnbook(tempreader,"TARGET",accuracy=self.accuraccy,epochs=epo,key=self.key,SECONDREAD=otherereader)
                STRING=d.replace('/','-')
                self.csvwrite(r2,CSV=self.hiveloci + '\prognostication' + STRING + '_OUTPUT.csv',KEY=self.key,NEWKEY=self.renamekey)
                self.Save(mymind,file_Name=self.geniusloci + '\prognostication' + STRING + '_BRAININAJAR')
                #except:
                 #   print(d)
                  #  print("We found no instances of this to forecast, press enter too accept")
               # input()

                csv=[]
                csv=self.csvopen(x=(self.csvloci+'\Test_Records_' + STRING + '_OUTPUT.csv'))
                vale=mymind.testday(tempreader,self.accuraccy,"TARGET",key=self.key)
                data={}
                data["Type"]=d
                data["Accuraccy"]=vale[0]
                data["Loss Function"]=vale[1]
                data["Date"]=self.today()
                data["Variance Around Average"]=vale[3]
                if vale[3]==0:
                    data["Hypothesis Test"]="Error in hypothesis test"
                else:
                    data["Hypothesis Test"]=vale[1]/vale[3]
                    if vale[1]/vale[3] > 1:
                        self.innaccurate.append(d)
                    elif d in self.innaccurate:
                        self.innaccurate.remove(d)
                data["Errors"]=vale[2]

                csv.append(data)
            
                self.csvwrite(csv,CSV=self.analysisloci + '\Test_Records_' + STRING + '_OUTPUT.csv',KEY="Type",NEWKEY=0)
                self.swarmin=0

        print("Innaccurate models detected")
        print(self.innaccurate)
               
    def Save(self,a,file_Name):
        import pickle


        fileObject = open(file_Name,'wb') 
        pickle.dump(a,fileObject)   
        fileObject.close()

    def Open(self,file_Name):
        import os.path
        if os.path.isfile(file_Name)==True:
            import pickle
            fileObject = open(file_Name,'rb')
            try:
                b = pickle.load(fileObject,encoding="utf8")
                return b
            except:
                print(file_Name)
                print("got a error in opening pickle RESTARTING FILE")
                return False
        else:
            return False
                    
                
    def updaterow(self,row,r2,key,d,look="Forecast Dates",error=0):
        for r in r2:
            if row[self.key]==r[self.key]:
                if r["ESTIMATE"] !="None response from AI, unrecognised engram - pleaser forecast manually":
                    row[look][d]=r["ESTIMATE"]
                return row
        return row
                    
            

    def isdate(self,check):
        from datetime import datetime
        try:
            h=check.split('/')
            x=datetime(int(h[2]), int(h[1]), int(h[0]), 0, 0, 0, 0)
            return True
        except:
            return False
    def today(self):
        from datetime import datetime
        check = datetime.now()
        return (str(check.day)+'/'+str(check.month)+'/'+str(check.year))
    def tryfindcmrdates(self,a,b):
        from datetime import datetime
        try:
            h=a.split('/')
            x=datetime(int(h[2]), int(h[1]), int(h[0]), 0, 0, 0, 0)
            t=b.split('/')
            t=datetime(int(t[2]), int(t[1]), int(t[0]), 0, 0, 0, 0)
            dt = t - x

            return dt.days
        except:
            return None

    def csvwrite(self,reader,CSV='C:\CSVs\OUTPUT.csv',KEY=0,NEWKEY=0):
        import csv
                              
        fieldnombre=[]
        for row in reader:
            for cell in row:         
                if not cell in fieldnombre:
                    fieldnombre.append(cell)
                    
        if NEWKEY !=0:
            try:
                fieldnombre.remove(KEY)
            except:
                pass
            fieldnombre.append(NEWKEY)

            for row in reader:
                row[NEWKEY]=row.get(KEY)
        

        frame=[]
        with open(CSV, 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(fieldnombre)
            for row in reader:
                frame=[]
                for field in fieldnombre:
                    frame.append(row.get(field))
                spamwriter.writerow(frame.copy())

            csvfile.close()

    def csvopen(self,x):
        import csv
        import os.path
        if os.path.isfile(x)==False:
            return []

        with open(x, newline='') as csvfile:
            data = csv.DictReader(csvfile)
            reader = [item for item in data]
            newreader=[]
            data=None
            count=0
                                  
        return reader

    def randomdata(self):
        import random

        for row in self.source:
            for d in self.dates:
                row["Forecast Dates"][d]=random.randint(0,120)
            for n in self.numbers:
                row["Forecast Numbers"][d]=random.randint(0,120)

    def multitest(self,reader,tag):

        innaccurate=[]

        def makeworksheet(typo,reader,num):
            newreader=[]
            if num==True:
                for row in reader:
                    if self.key in row:
                        newrow={}
                        try:
                            newrow[self.key]=row[self.key]
                        except:
                            print(row)
                            print(newrow)
                            input("error in makeworksheet")
                        if isinstance(row[typo],(int,float)):
                            newrow["TARGET"]=self.tryfindcmrdates(row[self.startdate],row[typo])
                            for k in self.kill:
                                if k in row:
                                    if isinstance(row[k],str):
                                        if not self.isdate(row[k]):
                                            if not len(row[k])==0:
                                                newrow[k]=str(k)+':' +str(row[k])
                                newreader.append(newrow.copy())

            else:
                for row in reader:
                    if self.key in row:
                        newrow={}
                        try:
                            newrow[self.key]=row[self.key]
                        except:
                            print(row)
                            print(newrow)
                            input("error in makeworksheet")
                        if self.isdate(row[self.startdate]):
                            if self.isdate(row[typo]):
                                newrow["TARGET"]=self.tryfindcmrdates(row[self.startdate],row[typo])
                                for k in self.kill:
                                    if k in row:
                                        if isinstance(row[k],str):
                                            if not self.isdate(row[k]):
                                                if not len(row[k])==0:
                                                    newrow[k]=str(k)+':' +str(row[k])
                                newreader.append(newrow.copy())
            return newreader

        for d in self.dates:

            tempreader=makeworksheet(d,reader,False)
            print("multitest")
            print(d)
            print(len(tempreader))
            if len(tempreader)>0:
                STRING=d.replace('/','-')
                mymind=self.Open(file_Name=self.geniusloci + '\prognostication' + STRING + '_BRAININAJAR')

                csv=[]
                csv=self.csvopen(x=(self.csvloci+'\Test_Records_' + STRING + '_OUTPUT.csv'))
                try:
                    vale=mymind.testday(tempreader,self.accuraccy,"TARGET",key=self.key)
                except:
                    print(vale)
                    input("error")
                data={}
                data["Type"]=d
                data["Accuraccy"]=vale[0]
                data["Loss Function"]=vale[1]
                data["Date"]=self.today()
                data["Tag"]=tag
                data["Variance Around Average"]=vale[3]

                if vale[3]==0:
                    data["Hypothesis Test"]="Error in hypothesis test"
                else:
                    data["Hypothesis Test"]=vale[1]/vale[3]
                    if vale[1]/vale[3] > 1:
                        innaccurate.append(d)
                data["Errors"]=vale[2]

                csv.append(data)
            
                self.csvwrite(csv,CSV=self.analysisloci + '\Test_Records_' + STRING + '_OUTPUT.csv',KEY="Type",NEWKEY=0)

        for d in self.numbers:
            tempreader=makeworksheet(d,reader,True)   
            print("multitest")
            print(d)
            print(len(tempreader))
            if len(tempreader)>0:
                STRING=d.replace('/','-')
                mymind=self.Open(file_Name=self.geniusloci + '\prognostication' + STRING + '_BRAININAJAR')

                csv=[]
                csv=self.csvopen(x=(self.csvloci+'\Test_Records_' + STRING + '_OUTPUT.csv'))
                vale=mymind.testday(tempreader,self.accuraccy,"TARGET",key=self.key)
                data={}
                data["Type"]=d
                data["Accuraccy"]=vale[0]
                data["Loss Function"]=vale[1]
                data["Date"]=self.today()
                data["Tag"]=tag
                data["Variance Around Average"]=vale[3]

                if vale[3]==0:
                    data["Hypothesis Test"]="Error in hypothesis test"
                else:
                    data["Hypothesis Test"]=vale[1]/vale[3]
                    if vale[1]/vale[3] > 1:
                        innaccurate.append(d)
                data["Errors"]=vale[2]

                csv.append(data)
            
                self.csvwrite(csv,CSV=self.analysisloci + '\Test_Records_' + STRING + '_OUTPUT.csv',KEY="Type",NEWKEY=0)
        print("Inaccuracies in Historic Data Found")
        print(innaccurate)

            
    def workplanner(self,setcritdelay=0,setalerts=0,taskmove=0,setpercntile=0,setdependency=0):

        averageburndown={}
        countdates={}
        burndown=0
        evaluate=[]

        csv=[]
        csv=self.csvopen(x=(self.hiveloci+'\RESOURCE PLAN.csv'))

        if len(csv)==0:
            for d in self.dates:
                newrow={}
                newrow["Type"]=d
                csv.append(newrow.copy())
            self.csvwrite(csv,CSV=(self.csvloci+'\RESOURCE PLAN.csv'),KEY=0,NEWKEY=0) 
                    
        newrow={}
        dat={}
        for c in csv:
            dat[c['Task']]={}
            for s in c:
                if s !=dat[c['Task']]:
                    dat[c['Task']][s]=c[s]

        for row in self.source:
            if len(row[self.startdate])>0:
                if len(row["end"])==0:
                    todah=self.tryfindcmrdates(row[self.startdate],self.today())
                    for d in row["Forecast Dates"]:
                        if not d in self.innaccurate:
                            if row["Dates"][d]==None:
                                if not d in row["Labels"]:
                                    count=1
                                    check=1
                                    reforecast=0
                                    newrow={}
                                    for e in row["Forecast Dates"]:
                                        if not e in self.innaccurate:
                                            if e !=d:
                                                if not e in row["Labels"]:
                                                    if row["Forecast Dates"][e]!=None:
                                                        if row["Dates"][e]!= None and row["Forecast Dates"][d]>row["Dates"][e]:
                                                            count+=1
                                                        elif row["Forecast Dates"][d]>row["Forecast Dates"][e]:
                                                            count+=1
                                                            if row["Dates"][e]==None:
                                                                check+=1

                                             
                                    burndown=row["Forecast Dates"][d]/count
                                    if burndown < 0 or burndown==row["Forecast Dates"][d]:
                                        burndown=0
                                    reforecast=round(todah+(check*burndown))
                                    
                                    newrow[self.renamekey]=row[self.key]
                                    newrow["Reforecast"]=reforecast
                                    newrow["Burndown"]=burndown
                                    newrow["Type"]=d
                                    newrow["Previous Tasks"]=count
                                    newrow["Original Forecast"]=row["Forecast Dates"][d]
                                    newrow["Previous Tasks Remainder"]=check

                                    if todah > row["Forecast Dates"][d]:
                                        if todah > (row["Forecast Dates"][d]*1.5):
                                            newrow["Late Flag"]="Late - long delay"
                                        else:
                                            newrow["Late Flag"]="Late"
                                    elif reforecast < row["Forecast Dates"][d]:
                                        newrow["Late Flag"]="Running Ahead"
                                    elif (row["Forecast Dates"][d]-reforecast)<burndown:
                                        newrow["Late Flag"]="On Schedule"
                                    else:
                                        newrow["Late Flag"]="Behind Schedule"
                                    if d in dat:
                                        for a in dat[d]:
                                            if a !=d:
                                                newrow[a]=dat[d][a]
                                    evaluate.append(newrow.copy())                 
        
        self.csvwrite(evaluate,CSV=(self.hiveloci+'\prognostication_REFORECAST.csv'),KEY=0,NEWKEY=0)

    def scheduletests(self):

        csv=[]
        import collections
        for me in self.dates:

            import random
            ra=[]
            for m in range(20):
                ra.append(m)
            print(ra)
            ra=random.sample(ra,len(ra)) 
            print(ra)
            
            for L in range(1):
                for r in ra:
                    for b in ra:
                        for d in ra:
                            for w in ra:
  
                                newrow=collections.OrderedDict()
                                newrow["Type"]=me
                                newrow["width"]=w+1
                                newrow["depth"]=d+1
                                newrow["resistance"]=r/10
                                newrow["bayeslearningrate"]=b+1
                                newrow["linearegression"]=L
                                newrow["epochs"]=1
                                newrow["n"]=False
                                
                                yield newrow
                                


        for d in self.numbers:
            
            
            for l in range(1):
                for r in ra:
                    for b in ra:
                        for d in ra:
                            for w in ra:
                                
                                newrow=collections.OrderedDict()
                                newrow["Type"]=d
                                newrow["width"]=w+1
                                newrow["depth"]=d+1
                                newrow["resistance"]=r/10
                                newrow["bayeslearningrate"]=b+1
                                newrow["linearegression"]=l
                                newrow["epochs"]=1
                                newrow["n"]=True
                                yield newrow

    def makeworksheet(self,d,reader,num):

        if num==True:

            tempreader=[]
            otherereader=[]
            for row in self.source:
                newrow={}
                newrow[self.key]=row[self.key]
                if len(row["end"])>0:
                    #print(row["Numbers"])
                    #print(row["end"])
                    #input()
                    newrow["TARGET"]=row["Numbers"][d]
                else:
                    newrow["TARGET"]=None
                for k in row["Labels"]:
                    if k !=d:
                        newrow[k]=row["Labels"][k]
                if newrow["TARGET"]!=None:
                    if newrow["TARGET"] > 0:
                        otherereader.append(newrow.copy())
                else:
                    tempreader.append(newrow.copy())

        else:
            tempreader=[]
            otherereader=[]
            for row in self.source:
                
                if not d in row["Labels"]:
                    newrow={}
                    newrow["TARGET"]=row["Dates"][d]
                   
                    for k in row["Labels"]:
                        if k !=d:
                            newrow[k]=row["Labels"][k]
                    newrow[self.key]=row[self.key]
                    if newrow["TARGET"]==None:
                        otherereader.append(newrow.copy())
                    else:
                        if newrow["TARGET"] < 0:
                            newrow["TARGET"]=0
                        tempreader.append(newrow.copy())

        return [tempreader,otherereader]                

    def queen(self,overide=0):

        def chack(reader,find):

            for row in reader:
                if row["Type"]==find:
                    return True

            return False
        def getacc(tye):
            STRING=tye.replace('/','-')
            try:
                CSV=self.csvopen(self.analysisloci + '\Test_Records_' + STRING + '_OUTPUT.csv')
            except:
                return False

            ROW=CSV[(len(CSV)-1)]

            vale=[]
            
            vale.append(float(ROW["Loss Function"]))
            vale.append(eval(ROW["Accuraccy"]))
            vale.append((len(CSV)))

            return vale

        bestwidth=0                       
        otherereader=[]
        tempreader=[]
        val1=[]
        val2=[]
        import random
        import collections
        comptests=[]
        #def __init__(self,width,depth,repeat=0,resistance=0,bayeslearningrate=10,linearegression=0):
        #def labotomy(self,width=[4,4,4,4,4],typo=['r','r','r','r','r','r'],resistance=[0,0,0,0,0,0],bayeslearningrate=[10,10,10,10,10]):
        csv=self.csvopen(x=(self.csvloci+'\Test_Records_SCHEDULED_TESTS.csv'))
        newcsv=[]
        ty=''
        for row in csv:
            if len(row["date"])>0:
                work=[]
                if not ty ==row["Type"]:
                    ty =row["Type"]
            
                    tempreader=[]
                    otherereader=[]
                    work=self.makeworksheet(row["Type"],self.source,row["number"])
                
                    tempreader=work[0]
                    otherereader=work[1]
                testmind=self.mind(width=int(row["width"]),depth=int(row["depth"]),resistance=int(row["resistance"]),bayeslearningrate=int(row["bayeslearningrate"]),linearegression=int(row["linearegression"]))
                try:
                    if len(row["labotomy.width"]) > 0:
                        testmind.labotomy(width=eval(row["labotomy.width"]),depth=eval(row["labotomy.width"]),resistance=int(row["labotomy.resistance"]),bayeslearningrate=eval(row["labotomy.bayeslearningrate"]),linearegression=eval(row["labotomy.linearegression"]))
                except:
                    pass
                testmind.learnbook(tempreader,"TARGET",accuracy=int(row["accuracy"]),epochs=int(row["epochs"]),key=self.key,SECONDREAD=otherereader)
                val1=getacc(row["Type"])
                val1e=testmind.testday(tempreader,int(row["accuracy"]),"TARGET",key=self.key)
                row["percentage"]=val1e[0]
                row["loss function"]=val1e[1]
                row["date"]=self.today()
                if val1e[0] > val1[0] and val1e[1] > val1[1]:
                    row["acceptance"]=1
                    STRING=str(row["Type"])
                    STRING=STRING.replace('/','-')
                    self.Save(testmind,file_Name=r'C:\CSVs\BrainsInAJar\prognostication' + STRING + '_BRAININAJAR')
                    row["Test passed type"]="Scheduled Test Passed"
                    comptests.append(row.copy())
                    self.csvwrite(comptests,CSV=(self.csvloci+'\Test_Records_COMPLETED_TESTS.csv'),KEY=0,NEWKEY=0)
                else:
                    row["acceptance"]=0
        c=0
        import time
        
        if len(comptests)==0:
            genny=self.scheduletests()
            ty=''
            for row in genny:
                work=[]
                if ty !=row["Type"]:
                    tempreader=[]
                    otherereader=[]
                    ty =row["Type"]
                    work=self.makeworksheet(row["Type"],self.source,row["n"])
                    tempreader=work[0]
                    otherereader=work[1]
                    val1=getacc(row["Type"])
                testmind=self.mind(width=int(row["width"]),depth=int(row["depth"]),resistance=int(row["resistance"]),bayeslearningrate=int(row["bayeslearningrate"]),linearegression=int(row["linearegression"]))
                testmind.learnbook(tempreader,"TARGET",accuracy=self.accuraccy,epochs=val1[2],key=self.key,SECONDREAD=otherereader)
                count=0
                val1e=testmind.testday(tempreader,self.accuraccy,"TARGET",key=self.key)
                row["percentage original"]=val1e[0]
                row["loss function"]=val1e[1]
                row["date"]=self.today()
                print("%")
                print(val1e[0])
                print("old")
               print(val1[1])
                print("loss")
                print(val1e[1])
                print("old")
                print(val1[0])
                print("epochs")
                print(val1[2])
                print(len(tempreader))
                print(len(otherereader))
                print(str(row["depth"]))
                print(str(row["width"]))
                print(str(row["resistance"]))
                print(str(row["bayeslearningrate"]))
                if val1e[0] > val1[1] and val1e[1] < val1[0]:
                    val1[1]=val1e[0]
                    val1[0]=val1e[1]
                    print("upgrade")
                    row["acceptance"]=1
                    STRING=str(row["Type"])
                    STRING=STRING.replace('/','-')
                    print(STRING)
                    self.Save(testmind,file_Name=r'C:\CSVs\BrainsInAJar\prognostication' + STRING + '_BRAININAJAR')
                    row["Test passed type"]="Auto Generated Test Passed"
                    comptests.append(row.copy())
                    self.csvwrite(comptests,CSV=(self.csvloci+'\Test_Records_COMPLETED_TESTS.csv'),KEY=0,NEWKEY=0)

        csv=self.csvopen(x=(self.csvloci+'\Test_Records_COMPLETED_TESTS.csv'))

        for row in csv:
            testmind=mind(width=int(row["width"]),depth=int(row["width"]),resistance=int(row["resistance"]),bayeslearningrate=int(row["bayeslearningrate"]),linearegression=int(row["linearegression"]))
            if len(row["labotomy.width"]) > 0:
                testmind.labotomy(width=eval(row["labotomy.width"]),depth=eval(row["labotomy.width"]),resistance=int(row["labotomy.resistance"]),bayeslearningrate=eval(row["labotomy.bayeslearningrate"]),linearegression=eval(row["labotomy.linearegression"]))
            c=float(inf)
            d=0
            work=self.makeworksheet(row["Type"],self.source)
            tempreader=work[0]
            otherereader=work[1]

            testmind.learnbook(tempreader,"TARGET",accuracy=int(row["accuraccy"]),epochs=1,key=self.key,SECONDREAD=otherereader)
            vale=testmind.testday(tempreader,int(row["accuraccy"]),"TARGET",key=self.key)
            count=1

            while vale[1] < c and vale[2] > d:
                testmind.learnbook(tempreader,"TARGET",accuracy=int(row["accuraccy"]),epochs=1,key=self.key,SECONDREAD=otherereader)
                vale=testmind.testday(tempreader,int(row["accuraccy"]),"TARGET",key=self.key)
                count+=1
            count-=1
            newrow=row.copy()
            newrow["epochs"]=count
            self.Save(testmind,file_Name=self.geniusloci + '\prognostication' + str(row["Type"]) + '_BRAININAJAR')
            newrow["Test passed type"]="Evaluation of earlystopping"
            csv.append(newrow.copy())
            self.csvwrite(csv,CSV=(self.csvloci+'\Test_Records_COMPLETED_TESTS.csv'),KEY=0,NEWKEY=0)
            
                
        self.queenIN=0
    def timestamp(self):
        import datetime
        now = datetime.datetime.now()
        print(now)
                    


def readmaker(x=0,kill=[],educational=[],ConverTOstrings=[]):
    import csv
    import random


    import datetime
    now = datetime.datetime.now()

    if len(str(now.month))==1:
        t='0'+str(now.month)
    else:
        t=str(now.month)

    if len(str(now.day))==1:
        y='0'+str(now.day)
    else:
        y=str(now.day)
    if x==0:
        x='\\\\wcrwvfilprd01\\shared$\\Telecoms Reporting\\QlikView nPrinting Output\\CMR\\IS_CMR_' + str(now.year) + '-' + t + '-' + y + '.csv'
        
    def infermeaning(reader,column):
        text=''
        textlist=[]
        corpuscount={}
        count=0
        average=0
        
        import math
        
        for row in reader:
            intext=[]
            text=row.get(column)
            if text !='':
                if text:
                    textlist=text.split()
                    for t in textlist:
                        count+=1
                        if t in corpuscount:
                            corpuscount[t]+=1
                        else:
                            corpuscount[t]=1
            

        for c in corpuscount:
            corpuscount[c]=math.log(count/corpuscount[c])
            average+=corpuscount[c]
        average=average/count

        newcorpuscount={}
        for c in corpuscount:
            if corpuscount[c] > average:
                newcorpuscount[c]=corpuscount[c]

        for row in reader:
            text=row.get(column)
            textlist=text.split()
            for t in text:
                if t in newcorpuscount:
                    row[t]=t
            del row[column]
        
        return reader

    with open(x, newline='') as csvfile:
        data = csv.DictReader(csvfile)
        reader = [item for item in data]
        newreader=[]
        data=None
        count=0

    for row in reader:
        for k in kill:
            try:
                del row[k]
            except:
                pass
        for con in ConverTOstrings:
            row["StrVer:"+str(con)]=con + ':' + str(row[con])
    for e in educational:
        reader=infermeaning(reader,e)
                              
    return reader



def ratiosplit(reader,ratio):
    count=0
    ratioreader=[]
    oldreader=[]

    for row in reader:
        count+=1
        newrow=row.copy()
        if count % ratio==0:
            ratioreader.append(newrow)
        else:
            oldreader.append(newrow)
    return [oldreader,ratioreader]


#SECTION TO SETUP FOR YOUR OWN DATA - ONE # = CODE LINE MULTIPLE ###### NOTES
#####DECLARE TIME 
##NOW=datetime.datetime.now()
#print(datetime.datetime.now())
##### ADD NAME OF FIELD TO CONVERTS TO CONVERT SOMETHING TO STRING
#converts=[]
##### EDUCATIONAL WILL SPLIT A COMMENTS FIELD
#edX=[]
##### KILL WILL DROP A FIELD 
#kill=[]
##### x IS required as a raw string to indicate the string of the filepath where the CSV you want it to use exists
#x=r''
##### below line creates a list containing ordered dicts from a CSV that represents the 
#r=readmaker(x=x,kill=kill,educational=edX,ConverTOstrings=converts)
##### splits data, assumes a ratio of 5 learn to 1 test change to taste, relies on data output being sorted. Hint i suggest sort on key
#r=ratiosplit(r,5)
#r2=r[1]
#r=r[0]
##### relies on knowing the key for the CSV need to 
#lockpick='ï»¿KEY FOR WORK NEEDS ï»¿ before string of key'
#update='KEY FOR WORK DOES NOT NEED NEEDS ï»¿ before string of key - RENAMES KEY AND REMOVES ï»¿ FOR FINAL OUTPUT'
##### START AND END
#START='FIELD NAME OF START DATE'
#END='FIELD NAME OF END DATE'
#ACCURACY=NUMBER OF DAYS YOU FIND AN ACCEPTABLE "CORRECT FORECAST"
#csvloci=
#csvloci=SUGGESTED: r'C:\CSVs\\' FILE LOCATION TO OUTPUT DATA AND BBUILD DATABASE AS LONG AS POINTED AT SAME LOCATION AT TIME WILL REUSE SAME AI
##### THE CODE THAT BUILDS MINDS DONT CHANGE UUNLESS READ THE FULL CODE
#for i in range(100):
#    countalot+=1
#    myhive=hivemind(r,lockpick,START,END,update,start=1,accuracy=ACCURACY,csvloci=csvloci)
#    myhive.multitest(r2,str("Random Test "+str(datetime.datetime.now())+" (1 in 5 chosen to test) Epoch: " + str(countalot)))

#print((datetime.datetime.now()-NOW))
