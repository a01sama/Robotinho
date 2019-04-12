#!/usr/bin/env python 
#By Abdul, Devante, and Zach
#Robotinho(Soccer Robot)
#Date: November 19, 2018    
import rospy
import random 
from geometry_msgs.msg import Twist 
from std_msgs.msg import String
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient
move_cmd = Twist()

def talker():     
   pub = rospy.Publisher("/mobile_base/commands/velocity", Twist, queue_size=10)     
   rospy.init_node('listener', anonymous=True)   
   rate = rospy.Rate(10)
   rospy.loginfo(move_cmd.linear.x) 
   while not rospy.is_shutdown():
		
		rospy.loginfo(move_cmd.linear.x)            
		pub.publish(move_cmd)         
		rate.sleep()

		
    		
def callback(data): 
    #If the voicecommand is "start"
    #Plays the song WakaWaka
    if (data.data == "start"): 
        soundhandle = SoundClient()
        soundhandle.playWave('wakawaka.wav')
    #If the voicecommand is "resume"
    #Plays short audio clip of WakaWaka
    elif (data.data == "resume"): 
        soundhandle = SoundClient()
        soundhandle.playWave('wakawaka1.wav')
    #If the voicecommand is "dribble forward"
    elif(data.data == "dribble forward"):
        move_cmd.linear.x = 0.2
    #If the voicecommand is "dribble left"
    elif (data.data == "dribble left"):
        move_cmd.angular.z = 0.5
        rospy.sleep(4.4)
	move_cmd.angular.z = 0.0
        move_cmd.linear.x = 0.2
    #If the voicecommand is "dribble right"
    elif (data.data == "dribble right"):
	move_cmd.angular.z = -0.5
        rospy.sleep(4.4)
	move_cmd.angular.z = 0.0
	move_cmd.linear.x = 0.1
	rospy.sleep(1.4)
        move_cmd.linear.x = 0.2
    #If the voicecommand is "weave drill" robothino performs weave drill
    #Whistle indicates beginning of drill
    #WakaWaka plays during drill
    elif (data.data == "weave drill"):
	soundhandle = SoundClient()
        soundhandle.playWave('whistle.wav')
	rospy.sleep(3)
	soundhandle = SoundClient()
        soundhandle.playWave('wakawaka1.wav')
	#start left
	move_cmd.angular.z = 0.58
        rospy.sleep(4.4)
	move_cmd.angular.z = 0.0
	move_cmd.linear.x = 0.1
	rospy.sleep(4)
	#first right 
	move_cmd.angular.z = -0.47
        rospy.sleep(4.4)
	move_cmd.angular.z = 0.0
	move_cmd.linear.x = 0.1
	rospy.sleep(7.3)
	#second right
	move_cmd.angular.z = -0.4
        rospy.sleep(4.4)
	move_cmd.angular.z = 0.0
	move_cmd.linear.x = 0.1
	rospy.sleep(8)
	#first left
	move_cmd.angular.z = 0.45
        rospy.sleep(4.4)
	move_cmd.angular.z = 0.0
	move_cmd.linear.x = 0.1
	rospy.sleep(5)
	#second left
	move_cmd.angular.z = 0.38
        rospy.sleep(4.4)
	move_cmd.angular.z = 0.0
	move_cmd.linear.x = 0.1
	rospy.sleep(6)
	#third right
	move_cmd.angular.z = -0.3
        rospy.sleep(7.4)
	move_cmd.angular.z = 0.0

	move_cmd.linear.x = 0.8
	rospy.sleep(1)
	move_cmd.linear.x = 0.0
	rospy.sleep(2)

	soundhandle = SoundClient()
        #Plays audio clip after robotinho scores
        #Does a dance
        soundhandle.playWave('cheer.wav')
	move_cmd.angular.z = 1.5
	rospy.sleep(2)
	move_cmd.angular.z = -3
	rospy.sleep(2)
	move_cmd.angular.z = 3
	rospy.sleep(2)
	move_cmd.angular.z = -3
	rospy.sleep(2)
	move_cmd.angular.z = 3
	rospy.sleep(2)
	move_cmd.angular.z = -1.5
	rospy.sleep(2)
	move_cmd.angular.z = 0.0

    #If the voicecommand is "circle drill" performs circle drill
    #Whistle begins the drill
    #Song "Started from the bottom" plays during drill
    elif (data.data == "circle drill"):
	soundhandle = SoundClient()
        soundhandle.playWave('whistle.wav')
	rospy.sleep(3)

	soundhandle = SoundClient()
        soundhandle.playWave('started.wav')


	move_cmd.angular.z = -0.5
       	move_cmd.linear.x = 0.22
	rospy.sleep(27)
	move_cmd.angular.z = 0.0
       	move_cmd.linear.x = 0.0
	rospy.sleep(3)
	move_cmd.linear.x = 0.99
	rospy.sleep(3.8)
	move_cmd.linear.x = 0.0
	rospy.sleep(3)
        #The crowd cheers after robotinho scores
        #Does a dance
	soundhandle = SoundClient()
        soundhandle.playWave('cheer.wav')
	move_cmd.angular.z = 1.5
	rospy.sleep(2)
	move_cmd.angular.z = -3
	rospy.sleep(2)
	move_cmd.angular.z = 3
	rospy.sleep(2)
	move_cmd.angular.z = -3
	rospy.sleep(2)
	move_cmd.angular.z = 3
	rospy.sleep(2)
	move_cmd.angular.z = -1.5
	rospy.sleep(2)
	move_cmd.angular.z = 0.0

    #If the voicecommand is "diamond drill" robothino performs diamond drill
    #Whistle indicates beginning of drill
    #Standup plays during drill
    elif (data.data == "diamond drill"):
	soundhandle = SoundClient()
        soundhandle.playWave('whistle.wav')
	rospy.sleep(3)

	soundhandle = SoundClient()
        soundhandle.playWave('Standup.wav')

	#start right
	move_cmd.angular.z = -0.45
        rospy.sleep(4.4)
	move_cmd.angular.z = 0.0
	move_cmd.linear.x = 0.1
	rospy.sleep(4)

	#first left 
	move_cmd.angular.z = 0.33
        rospy.sleep(4.4)
	move_cmd.angular.z = 0.0
	move_cmd.linear.x = 0.1
	rospy.sleep(26)

	#left at top cone
	move_cmd.angular.z = 0.3
        rospy.sleep(4.4)
	move_cmd.angular.z = 0.0
	move_cmd.linear.x = 0.1
	rospy.sleep(4)
	
	#straight into right
	move_cmd.angular.z = 0.47
        rospy.sleep(4.4)
	move_cmd.angular.z = 0.0
	move_cmd.linear.x = 0.1
	rospy.sleep(15)

	#right at left cone
	move_cmd.angular.z = -0.45
        rospy.sleep(4.4)
	move_cmd.angular.z = 0.0
	move_cmd.linear.x = 0.1
	rospy.sleep(6)	
	
	#right to go around the left cone
	move_cmd.angular.z = -0.35
        rospy.sleep(4.4)
	move_cmd.angular.z = 0.0
	move_cmd.linear.x = 0.1
	rospy.sleep(4)	

	#Straight to right cone
	move_cmd.angular.z = -0.4
        rospy.sleep(4.6)
	move_cmd.angular.z = 0.0
	move_cmd.linear.x = 0.1
	rospy.sleep(25)	

	#right towards goal
	move_cmd.angular.z = -0.48
        rospy.sleep(4.4)
	move_cmd.angular.z = 0.0
	move_cmd.linear.x = 0.1
	rospy.sleep(4)	

	#Dash to score goal
	move_cmd.linear.x = 0.8
	rospy.sleep(1.8)
	move_cmd.linear.x = 0.0
	rospy.sleep(4)
	#Commentator screams "GOOOOOAAAAAALLLLLLL!!!"
	#Robotinho does a dance
	soundhandle = SoundClient()
        soundhandle.playWave('goal_scream.wav')
	move_cmd.angular.z = 1.5
	rospy.sleep(2)
	move_cmd.angular.z = -3
	rospy.sleep(2)
	move_cmd.angular.z = 3
	rospy.sleep(2)
	move_cmd.angular.z = -3
	rospy.sleep(2)
	move_cmd.angular.z = 3
	rospy.sleep(2)
	move_cmd.angular.z = -1.5
	rospy.sleep(2)
	move_cmd.angular.z = 0.0

    #Score penalty
    #Robothino speeds up, hits the ball, and scores
    #Whistle begins the penalty kick
    elif (data.data == "score penalty"):
	
	soundhandle = SoundClient()
        soundhandle.playWave('whistle.wav')
	rospy.sleep(2)

	#moves ahead 4 tiles
	move_cmd.linear.x = 0.99
	rospy.sleep(2)
	move_cmd.linear.x = 0.0
	rospy.sleep(2)
        #Commentator screams "GOOOOOAAAAAALLLLLLL!!!"
	#Robotinho does a dance
	soundhandle = SoundClient()
        soundhandle.playWave('goal_scream.wav')
	move_cmd.angular.z = 1.5
	rospy.sleep(2)
	move_cmd.angular.z = -3
	rospy.sleep(2)
	move_cmd.angular.z = 3
	rospy.sleep(2)
	move_cmd.angular.z = -3
	rospy.sleep(2)
	move_cmd.angular.z = 3
	rospy.sleep(2)
	move_cmd.angular.z = -1.5
	rospy.sleep(2)
	move_cmd.angular.z = 0.0

    #Voice command stops robothino
    elif (data.data == "stop"):
        move_cmd.linear.x = 0.0


def listener():     
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/recognizer/output", String, callback)
    talker()        
    rospy.spin()  

if __name__ == '__main__':     
        try:
           listener()
    	except rospy.ROSInterruptException: pass
