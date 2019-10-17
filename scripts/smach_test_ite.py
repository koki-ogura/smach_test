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
        # 'it_data' is Iterator's it_label which hold iterator's current value
        smach.State.__init__(self, outcomes = ['succeeded', 'aborted', 'preempted'],
                             input_keys = ['it_data'])

    def execute(self, userdata):
        rospy.loginfo('Executing state BAR with %s', userdata.it_data)
        #rospy.sleep(1)
        for i in range(10):
            if self.preempt_requested():
                return 'preempted'
            #print 'BAR %s' % i
            rospy.sleep(0.1)
        return 'succeeded'

# define state BAS
class Bas(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['succeeded', 'aborted', 'preempted'])

    def execute(self, userdata):
        rospy.loginfo('Executing state BAS')
        rospy.sleep(1)
        return 'succeeded'


# main
static_list = ['i', 'my', 'me', 'mine']

def dynamic_iterator():
    return range(5)

def main():
    rospy.init_node('smach_example_state_machine')

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes = ['succeeded', 'aborted', 'preempted'])
    #sm.userdata.num = 5
    sm.userdata.result = []

    # Open the container
    with sm:
        # Add states to the container
        smach.StateMachine.add('FOO', Foo(), transitions = {'succeeded': 'SUB', 'aborted': 'aborted', 'preempted': 'preempted'})
        sm_ite = smach.Iterator(outcomes = ['succeeded', 'aborted', 'preempted'],
                            input_keys = ['result'],
                            output_keys = ['result'],
                            #it = lambda: range(sm.userdata.num),
                            #it = lambda: ['i', 'my', 'me'],
                            #it = ['i', 'my', 'me'],
                            #it = range(5),
                            #it = dynamic_iterator,
                            it = static_list,
                            it_label = 'it_data',
                            exhausted_outcome = 'succeeded')
        with sm_ite:
            # if BAR's result is 'succeeded' then loop, otherwise exit with result.
            smach.Iterator.set_contained_state('BAR', Bar(), loop_outcomes = ['succeeded'])

        smach.StateMachine.add('SUB', sm_ite, transitions = {'succeeded': 'BAS', 'aborted': 'aborted', 'preempted': 'preempted'})
        smach.StateMachine.add('BAS', Bas())

    # Create and start the introspection server
    sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')
    sis.start()

    # Execute SMACH plan
    outcome = sm.execute()
    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()
