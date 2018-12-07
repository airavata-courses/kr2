#File to read the raw airavata debug logs, process and write them to processed.log

#memory map useful for easier pattern matching, reading and writing data starting at different position using seek
import mmap

with open('airavata.log', 'r') as raw_log: #api dev server raw logs
    
    # size 0 means whole file, prot for Unix version
    mmap = mmap.mmap(raw_log.fileno(), 0, prot=mmap.PROT_READ)
    startIndex = mmap.rfind('Experiment Created') # search for last occurrence of 'string'
    				   
    mmap.seek(startIndex)             # seek to the location
    # line = mmap.readline()
       				
    
    line=mmap.readline()
    with open('processed.log', 'a') as processed_log:
        while (line):
            # print(line)
            processed_log.write(line)
            line=mmap.readline()
    