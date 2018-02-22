_author_='Arun_Raj_R'
import configparser
import argparse
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


def helperMethod():
        _mParser = argparse.ArgumentParser(prog='jvm_perf_catcher',usage='%(prog)s [--auto AUTO] [--pid PID [PID ...]] [--takeHD] [--takeTD] [--jm options [heapdump heap histogram]] [--ji options [flags flag sysprops]] [--js options [gc gcutil ...]] [-h]',description='This is used to take Thread Dump & Heap Dump based on the switches. It provides auditing facility as well. It captures the dump and store it in the configured destination.',epilog='copyrights to Solartis,INC - AR')
        _mParser.add_argument('--pid', type=int, nargs='+',help='provide PID of Node name / Server name')
        _mParser.add_argument('--takeHD',help='take heap dump for the specified node')
        _mParser.add_argument('--takeTD',help='take thread dump for the specified node')
        _mParser.add_argument('--jm',help='collect all JMap values')
        _mParser.add_argument('--ji',help='collect all JInfo values')
        _mParser.add_argument('--js',help='collect all JStat values')
        _mParser.add_argument('--auto',help='collects all based on the configuration files')
        _mArgs=_mParser.parse_args()
        return()
def checkJava():
        return()
def takeThreadDump():
        return()
def takeHeapDump():
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
