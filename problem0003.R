#Problem 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#We know any input will be valid i.e. > 0, we create a function to test for primality
problem <- function(a){
  
  #This function will check if each factor is prime
  primecheck <- function(n) {
    if (n == 2) {T}
    else if (any(n%% 2:(n-1) == 0)){F}
    else {T}
  }
  
  #This function will find the factors
  factors <- function(m) {
    list.factors <- NULL
    for (i in 1: (m/2)){
      if (m%%i == 0){list.factors <- c(list.factors, i)}
    }
    list.factors <- c(list.factors, m)
    return(list.factors)
  }
  list.factors <- factors(a)
  
  primefactors <- NULL
  for (j in 1:length(list.factors)){
    if (primecheck(list.factors[j])){primefactors <- c(primefactors, list.factors[j])}
  }
  return(paste("Largest prime factor is: ",max(primefactors)))
}

problem(600851475143)