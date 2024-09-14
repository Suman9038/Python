def Match (value) :
    match value :
        case 500 :
            return "hi"
        case 200 :
            return "my bad"
        case _ :
            return "WRONG"

print(Match(300))
print(Match(500))
print(Match(200))
    