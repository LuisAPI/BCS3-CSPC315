De La Salle University – Dasmariñas  
College of Information and Computer Studies

S–CSPC315 — Algorithms & Complexity  
Session 3: Class Participation

tree/computation log2 n = ?
Screen shot and send it to chatbox

1) 20 elements
2) 16 elements

Luis Anton P. Imperial  
BCS32

-----

## 1. log_2(20) = ?

log_2(20) = 5 levels

            20                                  // level 0
        /                    \  
        10                   10                 // level 1
      /    \              /     \  
    5       5            5       5              // level 2
   /  \    /  \      /      \     /  \ 
  3   2    3    2   3       2     3    2        // level 3
/  \  /\   /\   /\  /\      /\    /\   /\
2  1  1 1  2 1 1 1 2  1     1 1   2 1  1 1      // level 4
/\         /\      /\             /\
1 1        1 1     1 1            1 1           // level 5

## 2. log_2(16) = ?

log_2(16) = 4 levels

            16                                  // level 0
        /                    \  
        8                   8                   // level 1
      /    \              /     \  
    4       4            4       4              // level 2
   /  \    /  \      /      \     /  \
  2   2    2    2   2       2     2    2        // level 3
/  \  /\   /\   /\  /\      /\    /\   /\
1  1  1 1  1 1 1 1 1  1     1 1   1 1  1 1      // level 4