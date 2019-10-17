# smach_test

## prepare

### download and setup
```
$ cd ~/catkin_ws/src
$ git clone https://github.com/koki-ogura/smach_test.git
$ cd ~/catkin_ws
$ catkin_make
```

## execute roscore
```
$ roscore
```

## execute smach_viewer
```
$ rosrun smach_viewer smach_viewer.py
```

## Create a state that executes multiple states in order.
![view](https://github.com/koki-ogura/smach_test/blob/master/image/smach_test_seq.png)
```
$ rosrun smach_test smach_test_seq.py
```

## Create a state that executes multiple states simultaneously.
![view](https://github.com/koki-ogura/smach_test/blob/master/image/smach_test_con.png)
```
$ rosrun smach_test smach_test_con.py
```

## Create a state that repeatedly executes the same states.
![view](https://github.com/koki-ogura/smach_test/blob/master/image/smach_test_ite.png)
```
$ rosrun smach_test smach_test_ite.py
```
