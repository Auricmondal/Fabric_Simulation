Idea:

1. We are making a simulation of 1 m x 1m fabric of variable epi, ppi and yarn dia

what we have is the probability of occurance of faults

Basic Structure

1. Take user input of yarn count or diameter and convert it into mm
2. Take the input of epi and ppi
3. Convert epi and ppi into ep mm and pp mm
4. Calculate the total yarn lenght that will be used to create the fabric (warp and weft respec.)
5. generate fault positions using poissions ratio and the previously collected data of probability of occurance of faults
6. use the generated list and use proper traversing method to generate the simulation
7. For (currently) 6 possible combinations find how many are close to them , in order to do so, store the fault coordinates in a seperate list and then traverse through it properly to generate the count list

8. print the list
9. show the simulation
