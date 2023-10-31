""" The array to test it with
{
    "array": ["26", "6", "90", "55"]
}
"""

user_file <- GET file containing a list of words
READ user_file as json_user_file
words <- load(json_user_file)                   # 1

SET i_pivot <- length of words - 1              # 2

WHILE i_pivot > 0

    SET i_largets <- first item of words        # 4

    FOR i_check ... words before i_pivot        # 5
        IF i_check > i_largest                  # 5.1
            SET i_largest <- i_check

    IF i_largest > words[i_pivot]               
        SWAP words[i_pivot] and i_largest       # 6

    SET i_pivot - 1                             # 7

PUT words                                       # 8