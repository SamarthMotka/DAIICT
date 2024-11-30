import numpy as np

def get_next_state(current_state, transition_prob):
    return transition_prob@current_state
    
# Notice how each column adds up to 1
x = np.array([[0,1,0], [1,0,0], [0,0,1]])

threshold = 0.05

# Without any normalization

print("=================================")
print("Processing orginal matrix now")
print("=================================")

count = 0
x_curr = x
while True:
    count += 1
    reached_steady_state = False
    
    # Break if you reach 100 steps
    if count == 100:
        break
    x_next = get_next_state(x_curr, x)
    
    # Or break if your L1 norm is below a thresold
    diff = np.sum(abs(x_next-x_curr))
    if diff < threshold:
        reached_steady_state = True
        print(f"Steps completed: {count}, Diff: {diff}, Reached Steady State: {reached_steady_state}")        
        break
    
    x_curr = x_next
    print(f"Steps completed: {count}, Diff: {diff}, Reached Steady State: {reached_steady_state}")

print("=================================")
print("Completed processing orginal matrix")
print(f"Final Transition matrix: {x_curr}")
print("=================================")
print("Processing normalized matrix now")
print("=================================")
        
# Ensuring x is acyclic and irreducible

a = 0.15
N = x.shape[0]
x_normalized = (a/N) + (1-a)*x

count = 0
x_curr = x_normalized
while True:
    count += 1
    reached_steady_state = False
    
    # Break if you reach 100 steps
    if count == 100:
        break
    x_next = get_next_state(x_curr, x_normalized)
    
    # Or break if your L1 norm is below a thresold
    diff = np.sum(abs(x_next-x_curr))
    if diff < threshold:
        reached_steady_state = True
        print(f"Steps completed: {count}, Diff: {diff}, Reached Steady State: {reached_steady_state}")       
        break
    
    x_curr = x_next
    print(f"Steps completed: {count}, Diff: {diff}, Reached Steady State: {reached_steady_state}")

print("=================================")
print("Completed processing normalized matrix")
print("=================================")
print(f"Final Transition matrix: {x_curr}")

# What happens when value of a is increaseed to a large number? Say 0.5
# What happens when the threshold is changed?

