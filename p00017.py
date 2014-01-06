length_9 = len("one") + len("two") + len("three") + len("four") + len("five") + len("six") + len("seven") + len("eight") + len("nine")
length_10_19 = len("ten") + len("eleven") + len("twelve") + len("thirteen") + len("fourteen") + len("fifteen") + len("sixteen") + len("seventeen") + len("eighteen") + len("nineteen")
length_99 = length_9 * 9 + length_10_19 + (len("twenty")+len("thirty")+len("forty") + len("fifty") + len("sixty") + len("seventy") + len("eighty") + len("ninety")) * 10
length = length_99 * 10 + length_9 * 100 + len("hundred") * 100 * 9 + +len("and") * 99 * 9 + len("one") + len("thousand")
print length
