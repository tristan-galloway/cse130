# Prompt the user for a number n, from which we will find all the primes at or below that value.
GET user_num
num_list <- 1 to user_num
bool_list <- length of num_list where each value is True
prime_nums <- []

# Compute the primes at or below n.
FOR i <- 2 ... user_num/user_num
    IF bool_list[i + 2] = True
        current_i <- num_list[i] * 2
        WHILE current_i <= user_num
            bool_list[] <- False
            current_i = current_i + i

# Place all the primes in an array.
FOR i ... bool_list
    IF bool_list[i] = True
        append num_list[i] to prime_nums

# Display the primes on the screen.
PUT prime_nums
