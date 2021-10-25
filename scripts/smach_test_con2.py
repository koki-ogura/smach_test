#!/usr/bin/env python

import rospy
import smach
import smach_ros

# define state FOO
class Foo(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['succeeded', 'aborted', 'preempted'])

    def execute(self, userdata):
        rospy.loginfo('Executing state FOO')
        rospy.sleep(1)
        return 'succeeded'

# define state BAR
class Bar(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['succeeded', 'aborted', 'preempted'])

    def execute(self, userdata):
        rospy.loginfo('Executing state BAR')
        #rospy.sleep(1)
        for i in range(10):
            if self.preempt_requested():
                return 'preempted'
            print 'BAR %s' % i
            rospy.sleep(0.1)
        return 'succeeded'

# define state BAS
class Bas(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['succeeded', 'aborted', 'preempted'])

    def execute(self, userdata):
        rospy.loginfo('Executing state BAS')
        for i in range(20):
            if self.preempt_requested():
                return 'preempted'
            print 'BAS %s' % i
            rospy.sleep(0.1)
        return 'succeeded'


# main
# one finished
def child_term_cb(outcome_map):
    print('child_term_cb')
    for outcome in outcome_map.values():
        if outcome == None:
            continue
        if outcome != 'succeeded':
            return True
    return False

# all finished
def out_cb(outcome_map):
    print('out_cb')
    succeeded = True
    for outcome in outcome_map.values():
        if outcome != 'succeeded':
            succeeded = False
            break
    if succeeded:
        return 'succeeded'
    for outcome in outcome_map.values():
        if outcome == 'aborted':
            return 'aborted'
    return 'preempted'

'''
goal=MoveBaseGoal()
goal.target_pose.header.frame_id = "dtw_robot1/map"
goal.target_pose.pose.position.x = 0.5
goal.target_pose.pose.orientation.w = 1.0
smach.StateMachine.add('MOVE1', smach_ros.SimpleActionState('/dtw_robot1/move_base', MoveBaseAction, goal=goal), transitions={'succeeded':'TASK2', 'preempted':'done', 'aborted':'done'})
'''

def main():
    rospy.init_node('smach_example_state_machine')

    # Create a SMACH state machine
    #sm = smach.StateMachine(outcomes = ['succeeded', 'aborted', 'preempted'])
    sm = smach.Concurrence(outcomes = ['succeeded', 'aborted', 'preempted'],
                               default_outcome = 'aborted',
                               child_termination_cb = child_term_cb,
                               outcome_cb = out_cb)

    # Open the container
    with sm:
        smach.Concurrence.add('FOO', Foo())
        smach.Concurrence.add('BAR', Bar())
        smach.Concurrence.add('BAS', Bas())

    # Create and start the introspection server
    sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')
    sis.start()

    # Execute SMACH plan
    outcome = sm.execute()
    print(outcome)
    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
