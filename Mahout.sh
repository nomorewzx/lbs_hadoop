#!/bin/bash
cd ~/ubuntu/hadoop-1.2.1
bin/hadoop fs -rmr cf
bin/hadoop fs -rmr temp
bin/hadoop fs -rmr output2

bin/hadoop fs -mkdir cf
bin/hadoop fs -put /home/administrator/scores cf

bin/hadoop jar /home/administrator/ubuntu/mahout-distribution-0.9/mahout-core-0.9-job.jar org.apache.mahout.cf.taste.hadoop.item.RecommenderJob -i cf -o output2 -s SIMILARITY_COOCCURRENCE -n
hadoop fs -get output2/part-r-00000 ~/result
