def function(aantal: int = 0):
    lijst = ''
    for x in range(aantal):
        var = f'hello from function{x + 1}'
        lijst += var + '\n'
        return lijst
    
var = function(4)
print(var)