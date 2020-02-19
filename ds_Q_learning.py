# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 16:44:20 2019

@author: ali hussain
"""



import numpy as np
R=np.matrix([[-1,-1,-1,-1,0,-1],
             [-1,-1,-1,0,-1,100],
             [-1,-1,-1,0,-1,-1],
             [-1,0,0,-1,0,-1],
             [0,-1,-1,0,-1,100],
             [-1,0,-1,-1,0,100]])
print(R)


Q=np.matrix(np.zeros([6,6]))
print(Q)


gamma=0.8
initial_state=1


def available_actions(state):
  current_state_row=R[state,]
  av_act=np.where(current_state_row>=0)[1]
  return av_act


available_act=available_actions(initial_state)
print(available_act)


def sample_next_action(available_actions_range):
  next_action=int(np.random.choice(available_act,1))
  return next_action


action=sample_next_action(available_act)
action




def update(current_state,action,gamma):
    max_index=np.where(Q[action,]==np.max(Q[action,]))[1]
    
    if max_index.shape[0] > 1:
        max_index = int(np.random.choice(max_index,size=1))
    else:
        max_index =int(max_index)
    max_value = Q[action, max_index]
    
    Q[current_state, action ] = R[current_state, action] + gamma * max_value
        




for i in range(10000):
    current_state = np.random.randint(0, int(Q.shape[0]))
    available_act = available_actions(current_state)
    action = sample_next_action(available_act)
    update(current_state,action,gamma)


print(Q)


Q = Q/np.max(Q)*100
print(Q)

current_state = 1
steps = [current_state]
while current_state != 5:
    next_step_index = np.where(Q[current_state,] == np.max(Q[current_state,]))[1]
    
    if next_step_index.shape[0] > 1:
        next_step_index = int(np.random.choice(next_step_index,size=1))
        
    else:
        next_step_index = int(next_step_index)
        
    steps.append(next_step_index)
    current_state = next_step_index
    
print(steps)    








