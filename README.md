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

## sequence state test
Create a state that executes multiple states in order.
```
$ rosrun smach_test smach_test_seq.py
```

## concurrence state test
Create a state that executes multiple states simultaneously.
```
$ rosrun smach_test smach_test_con.py
```

## iterator state test
Create a state that repeatedly executes the same states.
```
$ rosrun smach_test smach_test_ite.py
```
