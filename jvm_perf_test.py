_author_='Arun_Raj_R'
import configparser
import argparse
import os
#from apihelper import info
from multiprocessing import Process
from pathlib import Path


_mJavaHome=''
_mJmapHome=''
_mJstackPath=''
_mNodeList=''
_mPIDList=''
_mHeapDumpDest=''
_mHeapDumpLog=''
_mThreadDumpDest=''
_mThreadDumpLog=''

config = configparser.ConfigParser()
config.read('config.ini')
config.sections()

FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'

def helperMethod():
        _mParser = argparse.ArgumentParser(prog='jvm_perf_catcher',usage='%(prog)s [--auto AUTO] [--pid PID [PID ...]] [--takeHD] [--takeTD] [--jm options [heapdump heap histogram]] [--ji options [flags flag sysprops]] [--js options [gc gcutil ...]] [-h]',description='This is used to take Thread Dump & Heap Dump based on the switches. It provides auditing facility as well. It captures the dump and store it in the configured destination.',epilog='copyrights to Solartis,INC - AR')
        _mParser.add_argument('--pid',metavar='pid_no',type=int, nargs='+',help='provide PID of Node name / Server name')
        _mParser.add_argument('--takeHD',metavar='heapdump',help='take heap dump for the specified node')
        _mParser.add_argument('--takeTD',metavar='threaddump',help='take thread dump for the specified node')
        _mParser.add_argument('--jm',choices=['hr','hd','histo'],help='collect all JMap values')
        _mParser.add_argument('--ji',choices=['flags','flag','sysprop'],help='collect all JInfo values')
        _mParser.add_argument('--js',choices=['all','gc','gccause','gcnew','gcold','gcutil'],help='collect all JStat values')
        _mParser.add_argument('--auto',help='collects all based on the configuration files')
        _mArgs=_mParser.parse_args()
        return()
#print(config['JINFO']['Flag'])
#print("Before funcations")
def checkJava():
        return()
def takeThreadDump(x):
        temp_value=x
        print("_mJavaHome/bin/jstack -l " + temp_value + "> $_mThreadDumpDest/$_mPid+$_mTime")
        print('module_name: ',__name__)
        print('parent process: ',os.getppid())
        print('process id: ',os.getpid())
        print('Loop id: ',temp_value)
        return()
def takeHeapDump():
        print("_mJavaHome/bin/jmap -dump:live,format=b,file=$_mHeapDumpDest/$_mPid+$_mTime $_mPid")
        return()
def listJnfo():
        for keys in config['JINFO']: print(keys)
        return()
#print ("Exited JINFOList")
def listJMAP():
        for keys in config['JMAP']: print(keys)
        return()
def listJSTAT():
        for keys in config['JSTAT']: print(keys)
        return()
def listNodeName():
        for keys in config['NodeName']: print(keys)
        return()
helperMethod()
listJnfo()
listNodeName()
listJSTAT()
listJMAP()

if __name__=='__main__':
    for counter in range(1,10):
            p = Process(target=takeThreadDump,args=(str(counter),))
            p.start()
            p.join()

#print("END CARD")
#config['JINFO'] = {}
#config['JMAP'] = {}
#config['JSTAT'] = {}
#config['NodeName'] = {}
