import requests,sys
from multiprocessing.pool import ThreadPool

def get_time(id,che=False):
    try:
        dat={"_id":id}
        a=requests.post(url,json=dat)
        min=int(a.text.split("\n")[-1].split(": ")[-1].split(" minutes")[0])
        if che:
            return a.text.split("\n")[-1]
        print(id,min,end='\r')
        if glob['max']==min:
            if 'id' not in glob:
                glob['stop']=True
                glob['id']=id
            if glob['id'] > id:
                glob['id']=id
    except:
        return get_time(id)

def get_sub():
    a=requests.get(url)
    id=int(a.text.split("\n")[0].split(": ")[-1])
    max_time=int(a.text.split("\n")[-1].split(": ")[-1].split(" minutes")[0])
    Threadcount=75
    glob['max']=max_time
    glob['stop']=False
    while True:
        ThreadPool(Threadcount).map(get_time,[i for i in range(id,id+Threadcount)])
        id+=Threadcount
        if glob['stop']:
            break
    print("Number of Submissions :",glob['id'])
    #a=requests.post(url,json=dat)

def main():
    global url,glob
    url='http://34.134.176.176:5000/wait'
    a=requests.get(url)
    glob={}
    print(a.text)
    if 'num' in sys.argv:
        get_sub()
    for i in range(1,len(sys.argv)):
        if sys.argv[i].isdigit():
            id=int(sys.argv[i])
            print(id,get_time(id,True),sep=" : ")

if __name__=='__main__':
    main()
