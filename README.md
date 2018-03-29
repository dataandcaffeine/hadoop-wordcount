# hadoop-wordcount

Running a MapReduce on Hadoop with Python 

# 1.Prerequisites : Single-Node Hadoop Cluster with Pydoop
	1.1. Ubuntu 12.10, 64-bit desktop version
	
	1.2. Oracle Java 8
			Install from command line :
			sudo add-apt-repository ppa:webupd8team/java
			sudo apt-get update
			sudo apt-get install oracle-java8-installer  
		
	1.3. Hadoop 2.7.4
			Download from : http://hadoop.apache.org/releases.html

	1.4. Pydoop 1.2.0
			Download from : https://pypi.python.org/pypi/pydoop
		
# 2. Start Hadoop
	2.1. Start from command line : 
			./start-all.sh
	2.2. Check processes by running jps
			DataNode
			NameNode
			SecondaryNameNode
			TaskTracker
			JobTracker
			JPS
	2.3. For details and troubleshooting : http://www.drdobbs.com/database/pydoop-writing-hadoop-programs-in-python/240156473
	
	
3. Running WordCount
	3.1. Create input directories
			hdfs dfs mkdir ~/input/
	3.2. Save input.txt to ~/input/
			hdfs dfs -copyFromLocal input.txt /input
	3.3. Save wordcount.py to ~/home/ubuntu/
	3.4. Run program from ~/pydoop/ :
		pydoop script wordcount.py input.txt output
	3.5. output will be containted in hdfs file called output
	