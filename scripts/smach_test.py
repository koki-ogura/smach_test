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
def main():
    rospy.init_node('smach_example_state_machine')

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes = ['succeeded', 'aborted', 'preempted'])

    # Open the container
    with sm:
        smach.StateMachine.add('FOO', Foo(), transitions={'succeeded':'BAR'})
        smach.StateMachine.add('BAR', Bar(), transitions={'succeeded':'BAS'})
        smach.StateMachine.add('BAS', Bas())

    # Create and start the introspection server
    #sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')
    #sis.start()

    # Execute SMACH plan
    outcome = sm.execute()
    #rospy.spin()
    #sis.stop()

if __name__ == '__main__':
    main()
