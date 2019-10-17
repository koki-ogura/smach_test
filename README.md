# smach_test

## prepare

### Prepare for smach and smach_viewer (ubuntu 18.04 melodic)
```
$ sudo apt install python-wxgtk2.8
$ sudo apt install python-gi-cairo
$ cd ~/catekin_ws/src
$ git clone https://github.com/ros/executive_smach.git
$ git clone -b melodic-devel https://github.com/k-okada/executive_smach_visualization.git
$ cd ~/catekin_ws
$ catekin_make
```

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
