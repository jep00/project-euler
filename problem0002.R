#Problem 2
#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

#Initialise
term_i <- 1 + 2 #Term 3
term_ii <- term_i + 2 #Term 4
terms <- c(1, 2, term_i, term_ii) #Creates list of all terms
term_iii <- term_i + term_ii #Generates new term
#Create Fib Seq
while (term_iii < 4000000){ #Only considers terms under 4 million
  terms <- c(terms, term_iii)
  term_i <- term_ii
  term_ii <- term_iii
  term_iii <- term_i + term_ii
}

even_terms <- NULL #New list for any terms that are even
for (i in 1:length(terms)){
  if (terms[i]%%2 == 0){even_terms <- c(even_terms, terms[i])} #Checks if even, if so adds to list
  else{}
}
print(sum(even_terms)) #Ouputs answer