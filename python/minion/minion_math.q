// refer to README.md for algorithm

//s:"banana"
s:first read0 `:minion_test5.txt
vowel_score:sum count[s]-where s in "aeiouAEIOU"
// the number is too big, overflow
// fact:{x:12$x; prd 1+til x}
// total_socre:fact[count[s]+1]%fact[2]*fact[count[s]-1]
total_socre:(prd(count[s]+1) - til 2) % 2 
show vowel_score
show 7h$total_socre - vowel_score