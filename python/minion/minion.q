// use q to solve minion game problem to compare to python in performance
// 80 seconds for minion_test.txt. Not great either!
// python is way to slow if not using itertools

// s:"banana"
s: first read0 `:minion_test.txt

\t scores:count each group raze s@reverse[t1]+\:' t1:til each 1+til count s
total_socre:sum scores
\t vowel_score:sum scores@key[scores] where sum each "aeiouAEIOU" in/: key[scores]@\:0
show vowel_score
show total_socre - vowel_score
