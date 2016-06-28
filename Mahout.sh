#!/bin/bash
# hadoop location: ~/ubuntu/hadoop-1.2.1
# mahout location: ~/ubuntu/mahout-distribution-0.9
hadoop fs -rmr cf
hadoop fs -rmr temp
hadoop fs -rmr output2

hadoop fs -mkdir cf
hadoop fs -put ./scores cf

hadoop jar /home/administrator/ubuntu/mahout-distribution-0.9/mahout-core-0.9-job.jar org.apache.mahout.cf.taste.hadoop.item.RecommenderJob -i cf -o output2 -s SIMILARITY_COOCCURRENCE -n
hadoop fs -get output2/part-r-00000 ./result
